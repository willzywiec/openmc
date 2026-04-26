#!/usr/bin/env python3
"""
Extract six-group delayed neutron decay constants from OpenMC's processed
ENDF/B-VIII.0 nuclear data library for embedding in SmpDelayed.cc.

Usage:
  export OPENMC_CROSS_SECTIONS=/path/to/endfb80_hdf5/cross_sections.xml
  python3 extract_endf_delayed.py

Output:
  Prints keepin_table[] entries with ENDF/B-VIII.0 decay constants (lambda)
  and per-group yields at 2 MeV (representative fast-spectrum energy), which
  can be copy-pasted into SmpDelayed.cc to replace the Keepin-1965 values.

Notes:
  - lambda_i (decay_rate) values come from ENDF MF1/MT455 and are
    independent of incident energy.
  - Group abundances a_i = nu_i / nu_d are computed at E=2 MeV;
    they vary slowly with energy for most actinides.
  - nu_d at the energy of interest is sum(nu_i(E)).
  - For spontaneous fission: ENDF does not supply SF delayed neutron data;
    those entries use SF-specific measurements (Cf-252) or induced-fission
    approximations (the rest) and cannot be extracted from ENDF.
"""
import sys
import os

try:
    import numpy as np
    import openmc.data
except ImportError:
    sys.exit("Requires: numpy, h5py, openmc   (pip install numpy h5py openmc)")

cross_sections = os.environ.get('OPENMC_CROSS_SECTIONS')
if not cross_sections:
    sys.exit("Set OPENMC_CROSS_SECTIONS=/path/to/endfb80_hdf5/cross_sections.xml")

data_dir = os.path.dirname(cross_sections)

# Induced-fission isotopes to extract (ZA, symbol, mass)
INDUCED = [
    (92233, 'U',  233),
    (92235, 'U',  235),
    (92238, 'U',  238),
    (94239, 'Pu', 239),
    (94241, 'Pu', 241),
]

E_fast = 2.0e6  # 2 MeV — representative FREYA energy

def h5name(sym, A):
    return f"{sym}{A}.h5"

print("/*")
print(" * ENDF/B-VIII.0 six-group delayed neutron parameters")
print(" * extracted with extract_endf_delayed.py")
print(" * lambda_i from MF1/MT455 (energy-independent decay constants)")
print(" * a_i = nu_i/nu_d evaluated at E=2 MeV incident neutron energy")
print(" */")
print()
print("/* ---- induced fission ---- */")

for za, sym, A in INDUCED:
    fname = os.path.join(data_dir, h5name(sym, A))
    if not os.path.exists(fname):
        print(f"   // {sym}-{A} ({za}): {fname} not found -- skipped")
        continue

    nuc = openmc.data.IncidentNeutron.from_hdf5(fname)
    if 18 not in nuc.reactions:
        print(f"   // {sym}-{A} ({za}): no MT=18 -- skipped")
        continue

    fission = nuc.reactions[18]
    delayed = [p for p in fission.products if p.emission_mode == 'delayed']
    if not delayed:
        print(f"   // {sym}-{A} ({za}): no delayed products -- skipped")
        continue

    lambdas = [d.decay_rate for d in delayed]
    try:
        yields = [float(d.yield_(E_fast)) for d in delayed]
    except Exception:
        yields = [0.0] * len(delayed)

    nu_d = sum(yields)
    a    = [y / nu_d if nu_d > 0 else 1.0 / len(yields) for y in yields]

    lam_str = ', '.join(f"{l:.5f}" for l in lambdas)
    a_str   = ', '.join(f"{ai:.4f}" for ai in a)
    print(f"   /* {sym}-{A} ({za}) induced, ENDF/B-VIII.0  sum(lambda)={sum(lambdas):.6f}  nu_d(2MeV)={nu_d:.5f} */")
    print(f"   {{ {za}, 1, {nu_d:.5f},")
    print(f"     {{{a_str}}},")
    print(f"     {{{lam_str}}} }},")
    print()

print()
print("/* ---- spontaneous fission ---- */")
print("/* SF delayed neutron data is NOT in ENDF; entries in keepin_table[]")
print("   for SF isotopes use Keepin-1965 / literature values directly. */")
