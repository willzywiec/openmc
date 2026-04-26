#!/usr/bin/env python3
"""Run GEF for neutron-induced fission, parse delayed neutron output,
compute per-isotope evaporation spectra, and emit gef_induced_spectra.h.

Usage:
    python run_gef_induced.py

Requires GEF64 at /home/user/gef/GEF64 (self-contained binary).

Method:
    For each induced-fission isotope, GEF is run with enhancement=100
    (10^7 events) at E_n=2.0 MeV.  The <Delayed> section is parsed to
    extract per-precursor Pn values.  Q_bn for each precursor is computed
    from AME/NUBASE2020 masses via the 'periodictable' package (whose mass
    values match the NUBASE2020 data embedded in GEF).  The composite
    evaporation spectrum is computed as:

        chi(E) = sum_i [ Pn_i * E * exp(-E/T_i) ]  (unnormalised)
        T_i    = sqrt(Q_bn_i / (3 * a_i))           [MeV]
        a_i    = (A_parent - 1) / 8.0               [MeV^-1]

    For beta-2n emitters: Q_bn_eff = Q_bn / 2 per neutron.
    The spectrum is binned into 200 bins of 0.05 MeV (0–10 MeV).

Reference: T.J. Nel, sf-delayed-neutron-data (2025) for SF analogues.
"""

import json
import math
import os
import re
import shutil
import subprocess
import sys
import tempfile
from concurrent.futures import ProcessPoolExecutor, as_completed

import periodictable

GEF_BIN  = "/home/user/gef/GEF64"
WORK_DIR = "/tmp/gef_induced"
OUT_DIR  = os.path.join(os.path.dirname(os.path.abspath(__file__)))

E_NEUTRON = 2.0    # MeV — fast fission
ENHANCE   = 100    # 10^7 events per isotope
NBIN      = 200
BIN_WIDTH = 0.05   # MeV
E_CENTERS = [0.025 + i * BIN_WIDTH for i in range(NBIN)]

# ---------------------------------------------------------------------------
# Induced fission isotopes:
#   (target_ZA, compound_Z, compound_A, label)
# SmpDelayed uses the TARGET ZA as the key.
# GEF needs the compound nucleus (target + neutron): A_compound = A_target + 1.
# ---------------------------------------------------------------------------
ISOTOPES = [
    # --- Spriggs table induced fission (5 tabulated) ---
    (92233, 92, 234, "n+U-233"),
    (92235, 92, 236, "n+U-235"),
    (92238, 92, 239, "n+U-238"),
    (94239, 94, 240, "n+Pu-239"),
    (94241, 94, 242, "n+Pu-241"),
    # --- Extended coverage ---
    (93237, 93, 238, "n+Np-237"),
    (94238, 94, 239, "n+Pu-238"),
    (94240, 94, 241, "n+Pu-240"),
    (94242, 94, 243, "n+Pu-242"),
    (95241, 95, 242, "n+Am-241"),
    (95243, 95, 244, "n+Am-243"),
    (96244, 96, 245, "n+Cm-244"),
    (96246, 96, 247, "n+Cm-246"),
    (98252, 98, 253, "n+Cf-252"),
]

# ---------------------------------------------------------------------------
# Mass excess (MeV) via periodictable (matches NUBASE2020 values in GEF).
# ---------------------------------------------------------------------------
_ME_N = (periodictable.n.mass - 1) * 931.494  # 8.0713 MeV

def mass_excess(Z, A):
    try:
        return (periodictable.elements[Z][A].mass - A) * 931.494
    except Exception:
        return None

def q_bn(Z_parent, A_parent, is_2n=False):
    """Q_bn = ME(parent) - ME(Z+1, A-1) - ME(n).  None if not computable."""
    me_p = mass_excess(Z_parent, A_parent)
    me_d = mass_excess(Z_parent + 1, A_parent - 1)
    if me_p is None or me_d is None:
        return None
    q = me_p - me_d - _ME_N
    if is_2n:
        q /= 2.0   # effective Q per neutron for beta-2n
    return q if q > 0 else None

# ---------------------------------------------------------------------------
# Evaporation spectrum for one precursor: chi(E) = E * exp(-E/T), normalised.
# Returns array of NBIN probability-density values.
# ---------------------------------------------------------------------------
def evap_spectrum(Z_parent, A_parent, is_2n=False):
    q = q_bn(Z_parent, A_parent, is_2n)
    if q is None or q <= 0:
        return None
    A_res = A_parent - 1
    a_ld  = A_res / 8.0
    T     = math.sqrt(q / (3.0 * a_ld))
    raw   = [E * math.exp(-E / T) for E in E_CENTERS]
    norm  = sum(raw) * BIN_WIDTH
    if norm <= 0:
        return None
    return [v / norm for v in raw]

# ---------------------------------------------------------------------------
# GEF runner: creates a temp working dir, runs GEF, returns output path.
# ---------------------------------------------------------------------------
def run_gef(target_ZA, cZ, cA, label, workbase):
    wdir = os.path.join(workbase, f"run_{target_ZA}")
    os.makedirs(os.path.join(wdir, "in"), exist_ok=True)

    # Input file: enhancement, energy, (no options), compound nucleus
    infile = os.path.join(wdir, "in", f"{target_ZA}.in")
    with open(infile, "w") as f:
        f.write(f"{ENHANCE}\n")
        f.write(f"{E_NEUTRON}\n")
        f.write("\n")                          # no special options
        f.write(f'{cZ},{cA},"EN"\n')

    with open(os.path.join(wdir, "file.in"), "w") as f:
        f.write(f"in/{target_ZA}.in\n")

    result = subprocess.run(
        [GEF_BIN],
        cwd=wdir,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        timeout=1800,   # 30 min per isotope
    )
    if result.returncode != 0:
        raise RuntimeError(f"GEF failed for {label}: {result.stdout.decode()[-500:]}")

    # Find output file
    outfile = os.path.join(wdir, "out", f"GEF_{cZ}_{cA}_n{E_NEUTRON}MeV.dat")
    if not os.path.exists(outfile):
        # GEF names the file differently for integer energies
        candidates = [f for f in os.listdir(os.path.join(wdir, "out"))
                      if f.endswith(".dat")]
        if not candidates:
            raise RuntimeError(f"No GEF output file found for {label}")
        outfile = os.path.join(wdir, "out", candidates[0])

    return outfile

# ---------------------------------------------------------------------------
# Parse GEF output: extract per-precursor Pn values and total nu_d.
# ---------------------------------------------------------------------------
def parse_gef_output(filepath):
    with open(filepath) as f:
        text = f.read()

    # Extract dn_emitters block
    m = re.search(r'<dn_emitters>(.*?)</dn_emitters>', text, re.DOTALL)
    if not m:
        raise ValueError(f"No <dn_emitters> block in {filepath}")

    precursors = []
    pn_re = re.compile(
        r'^\s*([\d.e+\-]+)\s+(\d+)\s+(\d+)\s+(.*?)\s*$',
        re.IGNORECASE
    )
    for line in m.group(1).splitlines():
        pm = pn_re.match(line)
        if pm:
            pn_val  = float(pm.group(1))
            Z       = int(pm.group(2))
            A       = int(pm.group(3))
            decay   = pm.group(4).lower()
            is_2n   = "2n" in decay
            precursors.append((pn_val, Z, A, is_2n))

    # Extract total nu_delayed
    nm = re.search(r'Multiplicity of delayed neutrons per fission:\s*([\d.e+\-]+)', text)
    if not nm:
        raise ValueError(f"No nu_delayed in {filepath}")
    nu_d = float(nm.group(1))

    return precursors, nu_d

# ---------------------------------------------------------------------------
# Build composite spectrum from precursors.
# ---------------------------------------------------------------------------
def build_spectrum(precursors):
    composite = [0.0] * NBIN
    total_pn  = 0.0
    n_skipped = 0

    for pn_val, Z, A, is_2n in precursors:
        spec = evap_spectrum(Z, A, is_2n)
        if spec is None:
            n_skipped += 1
            continue
        for i in range(NBIN):
            composite[i] += pn_val * spec[i]
        total_pn += pn_val

    if total_pn <= 0:
        raise ValueError("No usable precursors")

    # Normalise to probability density (sum * bin_width = 1)
    norm = sum(composite) * BIN_WIDTH
    spectrum = [v / norm for v in composite]
    mean_e   = sum(E_CENTERS[i] * spectrum[i] * BIN_WIDTH for i in range(NBIN))
    return spectrum, mean_e, n_skipped

# ---------------------------------------------------------------------------
# Process one isotope end-to-end.
# ---------------------------------------------------------------------------
def process_isotope(target_ZA, cZ, cA, label, workbase):
    print(f"  Running GEF for {label} (ZA={target_ZA}, compound {cZ},{cA})...",
          flush=True)
    outfile = run_gef(target_ZA, cZ, cA, label, workbase)
    precursors, nu_d = parse_gef_output(outfile)
    spectrum, mean_e, n_skip = build_spectrum(precursors)
    print(f"  {label}: nu_d={nu_d:.6e}  <E>={mean_e:.4f} MeV  "
          f"precursors={len(precursors)}  skipped={n_skip}", flush=True)
    return {
        "label":       label,
        "target_ZA":   target_ZA,
        "compound_Z":  cZ,
        "compound_A":  cA,
        "E_neutron":   E_NEUTRON,
        "nu_d":        nu_d,
        "mean_E_MeV":  mean_e,
        "n_precursors":len(precursors),
        "spectrum":    spectrum,
    }

# ---------------------------------------------------------------------------
# Emit C header.
# ---------------------------------------------------------------------------
def emit_header(results, outpath):
    lines = [
        "/*",
        " * gef_induced_spectra.h",
        " *",
        " * GEF-derived delayed neutron energy spectra for neutron-induced fission.",
        f" * Generated by run_gef_induced.py (GEF 2025/1.3, E_n={E_NEUTRON} MeV, {ENHANCE}*10^5 events).",
        " *",
        " * Spectrum model: composite evaporation sum over GEF fission-fragment yields.",
        " *   chi(E) = sum_i [ Pn_i * E * exp(-E/T_i) ]",
        " *   T_i = sqrt(Q_bn_i / (3 * (A_i-1)/8))  [MeV]",
        " * Masses from NUBASE2020 (via periodictable, matching GEF internal data).",
        " * 200 bins, 0.05 MeV/bin, 0-10 MeV.  Probability density [1/MeV].",
        " *",
        " * SmpDelayed.cc uses these spectra for induced-fission events when the",
        " * target ZA matches an entry; Maxwellian fallback otherwise.",
        " */",
        "",
        "#ifndef GEF_INDUCED_SPECTRA_H",
        "#define GEF_INDUCED_SPECTRA_H",
        "",
        "#define GEF_IND_NBIN       200",
        "#define GEF_IND_BIN_WIDTH  0.05   /* MeV per bin */",
        "#define GEF_IND_E_MIN      0.025  /* centre of first bin [MeV] */",
        "",
        "typedef struct {",
        "   int    target_ZA;                  /* ZA of fissioning nucleus (target) */",
        "   double nu_d;                       /* delayed neutrons per fission (GEF) */",
        "   double spectrum[GEF_IND_NBIN];     /* probability density [1/MeV] */",
        "} GEFIndSpectrum;",
        "",
        "static const GEFIndSpectrum gef_ind_table[] = {",
    ]

    for r in sorted(results, key=lambda x: x["target_ZA"]):
        za    = r["target_ZA"]
        label = r["label"]
        nu_d  = r["nu_d"]
        mean_e= r["mean_E_MeV"]
        En    = r["E_neutron"]
        spec  = r["spectrum"]
        lines.append(
            f"  /* {label} (target ZA={za})  "
            f"nu_d={nu_d:.6e}  <E>={mean_e:.4f} MeV  E_n={En} MeV */"
        )
        lines.append(f"  {{ {za}, {nu_d:.8e},")
        lines.append("    {")
        for i in range(0, NBIN, 5):
            chunk = spec[i:i+5]
            row   = ", ".join(f"{v:.8e}" for v in chunk)
            comma = "," if i + 5 < NBIN else ""
            lines.append(f"      {row}{comma}")
        lines.append("    }},")

    lines += [
        "};",
        "",
        f"#define GEF_IND_NENTRIES  "
        f"((int)(sizeof(gef_ind_table)/sizeof(gef_ind_table[0])))",
        "",
        "static const GEFIndSpectrum* find_gef_ind_spectrum(int target_za) {",
        "   for (int i = 0; i < GEF_IND_NENTRIES; i++)",
        "      if (gef_ind_table[i].target_ZA == target_za) return &gef_ind_table[i];",
        "   return NULL;",
        "}",
        "",
        "static double smpGEFIndEnergy(const GEFIndSpectrum* sp, double u) {",
        "   double cdf = 0.0;",
        "   for (int i = 0; i < GEF_IND_NBIN; i++) {",
        "      cdf += sp->spectrum[i] * GEF_IND_BIN_WIDTH;",
        "      if (u <= cdf)",
        "         return GEF_IND_E_MIN + i * GEF_IND_BIN_WIDTH;",
        "   }",
        "   return GEF_IND_E_MIN + (GEF_IND_NBIN - 1) * GEF_IND_BIN_WIDTH;",
        "}",
        "",
        "#endif /* GEF_INDUCED_SPECTRA_H */",
    ]

    with open(outpath, "w") as f:
        f.write("\n".join(lines) + "\n")
    print(f"\nWrote {outpath}")

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    os.makedirs(WORK_DIR, exist_ok=True)
    print(f"GEF working directory: {WORK_DIR}")
    print(f"Enhancement: {ENHANCE} ({ENHANCE * 1e5:.0e} events per isotope)")
    print(f"Neutron energy: {E_NEUTRON} MeV")
    print(f"Isotopes: {len(ISOTOPES)}")
    print()

    results = []
    failed  = []

    # Run sequentially (GEF instances conflict when sharing a directory).
    for target_ZA, cZ, cA, label in ISOTOPES:
        try:
            r = process_isotope(target_ZA, cZ, cA, label, WORK_DIR)
            results.append(r)
        except Exception as e:
            print(f"  ERROR {label}: {e}", file=sys.stderr)
            failed.append(label)

    print(f"\nCompleted {len(results)}/{len(ISOTOPES)} isotopes.")
    if failed:
        print(f"Failed: {failed}", file=sys.stderr)

    if not results:
        print("ERROR: no results", file=sys.stderr)
        sys.exit(1)

    json_path = os.path.join(OUT_DIR, "gef_induced_spectra.json")
    with open(json_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"Wrote {json_path}")

    h_path = os.path.join(OUT_DIR, "gef_induced_spectra.h")
    emit_header(results, h_path)
