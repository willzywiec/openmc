"""
Godiva — Full Pipeline Example
==============================

End-to-end demonstration of every fission-library capability added by the
fork's recent phases, applied to the canonical Godiva benchmark (bare HEU
sphere, ~52 kg U, ~8.74 cm radius). The example runs in two parts:

    Part A — Eigenvalue + alpha eigenvalue + analog FREYA
        Standard criticality / Rossi-alpha analysis. Reports k_eff,
        beta_eff, ell_p, alpha_dc, alpha. Exercises:
          - settings.calculate_alpha = True   (Phase 1)
          - settings.freya_analog    = True   (Phase 4)

    Part B — Passive-source characterization (no transport run)
        Builds the source descriptions you'd hand to a fixed-source
        simulation for an NDA / safeguards problem with the same
        geometry. Exercises:
          - openmc.FreyaSFSource(...)                (Phase 5)
          - openmc.model.alphanso_source(...)        (ALPHANSO helper)

        Note: Godiva is bare HEU metal, so both passive contributions
        are tiny (small SF rate from U-238/U-234, no (alpha,n) target
        nuclei). The point of Part B is to demonstrate the API on real
        material — for a meaningful passive source you'd swap in PuO2,
        MOX, or attach an external Cf-252 calibration source as shown.

Requirements
------------
    Part A:   OpenMC built with -DOPENMC_USE_FISSION_LIB=ON, ENDF/B
              cross-section data, and gfortran for the FREYA library.
    Part B:   `pip install alphanso` for the (alpha,n) helper. The
              FreyaSFSource construction needs the same OpenMC build as
              Part A.

Quick build:  ./setup.sh --with-fission-lib  (then `source openmc_env.sh`)

Reference for the Godiva specification:
    Cullen, D.E. et al., "Static and Dynamic Criticality: Are They
    Different?", UCRL-TR-201506 (LLNL, 2003).
"""

from __future__ import annotations

import openmc
import openmc.model
import openmc.stats


# ---------------------------------------------------------------------------
# Godiva specification (UCRL-TR-201506)
# ---------------------------------------------------------------------------
GODIVA_RADIUS_CM = 8.7407
GODIVA_DENSITY_G_CC = 18.7398
GODIVA_COMPOSITION = {           # atom fractions
    'U235': 0.937695,
    'U238': 0.052053,
    'U234': 0.010252,
}
GODIVA_TEMPERATURE_K = 293.6
GODIVA_MASS_G = (4.0 / 3.0) * 3.141592653589793 \
    * GODIVA_RADIUS_CM**3 * GODIVA_DENSITY_G_CC


def build_godiva_material() -> openmc.Material:
    mat = openmc.Material(name='Godiva HEU')
    mat.set_density('g/cm3', GODIVA_DENSITY_G_CC)
    for nuc, frac in GODIVA_COMPOSITION.items():
        mat.add_nuclide(nuc, frac)
    mat.temperature = GODIVA_TEMPERATURE_K
    return mat


def build_godiva_geometry(mat: openmc.Material) -> openmc.Geometry:
    sphere = openmc.Sphere(r=GODIVA_RADIUS_CM, boundary_type='vacuum')
    cell = openmc.Cell(name='Godiva sphere', fill=mat, region=-sphere)
    return openmc.Geometry([cell])


# ===========================================================================
# Part A — eigenvalue + alpha + analog FREYA
# ===========================================================================
def part_a_eigenvalue_with_alpha_and_freya() -> None:
    print("=" * 72)
    print("Part A: eigenvalue + alpha eigenvalue + analog FREYA")
    print("=" * 72)

    material = build_godiva_material()
    openmc.Materials([material]).export_to_xml()
    build_godiva_geometry(material).export_to_xml()

    settings = openmc.Settings()
    settings.run_mode = 'eigenvalue'
    settings.batches = 150
    settings.inactive = 50
    settings.particles = 50_000

    # Initial fission source: point at the centre. Eigenvalue mode does
    # not consume external sources past the first generation.
    settings.source = openmc.IndependentSource(
        space=openmc.stats.Point((0.0, 0.0, 0.0)),
    )

    # Alpha eigenvalue + IFP-weighted prompt lifetime + beta_eff. Auto-
    # enables calculate_prompt_k and IFP with sensible defaults.
    settings.calculate_alpha = True

    # Full-analog FREYA: invoke FREYA once per fission and bank all
    # nn correlated prompt neutrons together. Total banked weight per
    # fission is unchanged from the default (per-slot) path, so k_eff
    # / alpha estimates are unbiased; what changes is the within-event
    # joint distribution available to multiplicity-style tallies.
    settings.freya_analog = True

    settings.export_to_xml()

    sp_path = openmc.run()

    with openmc.StatePoint(sp_path) as sp:
        keff       = sp.keff
        k_prompt   = sp.k_prompt
        beta_eff   = sp.beta_eff
        ell_p      = sp.lifetime_p_ifp
        lambda_p   = sp.lambda_p_ifp
        alpha_dc   = sp.alpha_dc_ifp
        alpha_stat = sp.alpha_ifp

    print()
    print(f"  k_eff       = {keff.nominal_value:.5f} +/- {keff.std_dev:.5f}")
    print(f"  k_prompt    = {k_prompt.nominal_value:.5f} "
          f"+/- {k_prompt.std_dev:.5f}")
    print(f"  beta_eff    = {beta_eff.nominal_value*1e5:.1f} "
          f"+/- {beta_eff.std_dev*1e5:.1f}  pcm")
    print(f"  ell_p       = {ell_p.nominal_value*1e9:.3f} "
          f"+/- {ell_p.std_dev*1e9:.3f}  ns  (IFP-weighted prompt lifetime)")
    print(f"  Lambda_p    = {lambda_p.nominal_value*1e9:.3f} "
          f"+/- {lambda_p.std_dev*1e9:.3f}  ns  (= ell_p / k_p, reported only)")
    print(f"  alpha_dc    = {alpha_dc.nominal_value:.3e} "
          f"+/- {alpha_dc.std_dev:.3e}  1/s  (-beta_eff / ell_p)")
    print(f"  alpha       = {alpha_stat.nominal_value:.3e} "
          f"+/- {alpha_stat.std_dev:.3e}  1/s  ((k_p - 1) / ell_p)")
    print()
    print("Reference Rossi-alpha for Godiva (Mosteller 2011, expt.):")
    print("  alpha_dc ~ -1.11e6 1/s")
    print()


# ===========================================================================
# Part B — passive source characterization
# ===========================================================================
def part_b_passive_sources() -> None:
    print("=" * 72)
    print("Part B: passive source characterization (construction only)")
    print("=" * 72)
    print()

    # ----- ALPHANSO (alpha, n) source on the HEU matdef ---------------------
    #
    # ALPHANSO computes the (alpha, n) source rate and energy spectrum from
    # a material composition. For pure HEU there are no light-element targets
    # and the rate will be near zero — Pu-bearing oxide systems are where
    # this matters. Shown here to demonstrate the API.
    #
    # Composition keys for ALPHANSO use isotope ID strings ('U-235', not
    # 'U235') matching its native convention.
    alphanso_matdef = {
        'U-234': GODIVA_COMPOSITION['U234'],
        'U-235': GODIVA_COMPOSITION['U235'],
        'U-238': GODIVA_COMPOSITION['U238'],
    }
    print("ALPHANSO (alpha, n):")
    try:
        alphanso_src = openmc.model.alphanso_source(
            matdef=alphanso_matdef,
            calc_type='homogeneous',
            position=(0.0, 0.0, 0.0),
        )
        rate_per_g = alphanso_src.strength      # n/s/g, per ALPHANSO units
        total_rate = rate_per_g * GODIVA_MASS_G
        print(f"  matdef        = {alphanso_matdef}")
        print(f"  rate          = {rate_per_g:.3e} n/s/g")
        print(f"  Godiva mass   = {GODIVA_MASS_G:.1f} g")
        print(f"  total rate    = {total_rate:.3e} n/s   (no light targets)")
    except ImportError as exc:
        print(f"  skipped — {exc}")
    print()

    # ----- FreyaSFSource for U-238 (intrinsic SF in HEU) --------------------
    #
    # U-238 is the dominant SF contributor in HEU at this enrichment.
    # SF half-life ~8.2e15 yr → vanishingly small rate compared to the
    # multiplied source from criticality. Shown to demonstrate the API.
    print("FreyaSFSource — U-238 intrinsic SF (Godiva is barely SF-active):")
    u238_sf_src = openmc.FreyaSFSource(
        za=92238,
        position=(0.0, 0.0, 0.0),
        n_events=10_000,
        include_photons=True,
        seed=1,
        strength=1.0,    # placeholder — supply n/s for absolute tallies
    )
    print(f"  za            = {u238_sf_src.za}")
    print(f"  position      = {u238_sf_src.position}")
    print(f"  n_events      = {u238_sf_src.n_events}")
    print(f"  include_photons = {u238_sf_src.include_photons}")
    print()

    # ----- External Cf-252 calibration source -------------------------------
    #
    # Realistic NDA setup: place a Cf-252 SF source ~50 cm from the Godiva
    # surface to drive a passive multiplication measurement. Cf-252
    # specific activity ~0.116 fissions/g/s × <nu>=3.76 → ~0.43 n/s/g of
    # bulk Cf-252.
    cf252_position_cm = (GODIVA_RADIUS_CM + 50.0, 0.0, 0.0)
    cf252_mass_g = 1e-6  # 1 ug source
    cf252_strength = 0.116 * 3.76 * cf252_mass_g  # n/s
    print("FreyaSFSource — external Cf-252 calibration point (1 ug):")
    cf252_src = openmc.FreyaSFSource(
        za=98252,
        position=cf252_position_cm,
        n_events=50_000,
        include_photons=True,
        seed=2,
        strength=cf252_strength,
    )
    print(f"  za            = {cf252_src.za}")
    print(f"  position      = {cf252_src.position} cm")
    print(f"  strength      = {cf252_strength:.3e} n/s "
          f"(0.116 fiss/g/s * 3.76 n/fiss * {cf252_mass_g} g)")
    print()

    # ----- How to wire these into a fixed-source run ------------------------
    #
    # For a real NDA simulation, you would set:
    #     settings.run_mode = 'fixed source'
    #     settings.source   = [cf252_src, u238_sf_src, alphanso_src]
    # and tally e.g. neutron leakage out of the Godiva surface, or a
    # detector tally elsewhere. We don't run that here because for pure
    # Godiva the relevant physics is the eigenvalue / alpha analysis in
    # Part A; passive sources matter for sub-critical / passive
    # configurations (Pu metal sphere, oxide containers, etc.).
    print("Wire-up sketch for a fixed-source NDA run (not executed):")
    print("  settings.run_mode = 'fixed source'")
    print("  settings.source   = [cf252_src, u238_sf_src, alphanso_src]")
    print()


# ===========================================================================
if __name__ == '__main__':
    part_a_eigenvalue_with_alpha_and_freya()
    part_b_passive_sources()
