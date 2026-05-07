"""Build the Godiva (HEU-MET-FAST-001) reference model.

Godiva is a bare highly enriched uranium sphere from the ICSBEP handbook.
Published parameters:

    radius      = 8.7407 cm
    density     = 18.74 g/cm^3
    composition = 93.71 wt% U-235, 5.27 wt% U-238, 1.02 wt% U-234
    k_eff       = 1.0000 +/- 0.0010
    beta_eff    = 645 +/- 13 pcm
    Lambda      = 5.8 ns

Reference: International Handbook of Evaluated Criticality Safety Benchmark
Experiments (ICSBEP), HEU-MET-FAST-001.

This module exports a single function ``build_model`` that returns a fully
configured :class:`openmc.Model`.  It is consumed by the run / analysis
scripts in this directory and by the regression test
``tests/regression_tests/ifp_importance/``.
"""
from __future__ import annotations

import openmc


GODIVA_RADIUS_CM = 8.7407
GODIVA_DENSITY_G_CC = 18.74

# ICSBEP HEU-MET-FAST-001 reference values for cross-checking results.
GODIVA_REFERENCE = {
    "k_eff":      (1.0000, 0.0010),
    "beta_eff":   (645e-5,  13e-5),    # 645 +/- 13 pcm
    "Lambda":     (5.8e-9,  0.2e-9),   # ~ 5.8 ns
}


def build_model(
    n_particles: int = 50_000,
    n_inactive: int = 30,
    n_active: int = 200,
    ifp_n_generation: int = 10,
    mesh_dimension: tuple[int, int, int] = (30, 30, 30),
    n_energy_groups: int = 20,
) -> openmc.Model:
    """Construct the Godiva model with an `ifp-importance` tally."""

    # --- Materials ----------------------------------------------------------
    heu = openmc.Material(name="HEU (Godiva)")
    heu.set_density("g/cm3", GODIVA_DENSITY_G_CC)
    heu.add_nuclide("U234", 0.01017, "wo")
    heu.add_nuclide("U235", 0.93714, "wo")
    heu.add_nuclide("U238", 0.05269, "wo")

    materials = openmc.Materials([heu])

    # --- Geometry -----------------------------------------------------------
    sphere = openmc.Sphere(r=GODIVA_RADIUS_CM, boundary_type="vacuum")
    fuel_cell = openmc.Cell(name="HEU sphere", fill=heu, region=-sphere)

    geometry = openmc.Geometry([fuel_cell])

    # --- Settings -----------------------------------------------------------
    settings = openmc.Settings()
    settings.run_mode = "eigenvalue"
    settings.batches = n_inactive + n_active
    settings.inactive = n_inactive
    settings.particles = n_particles
    settings.ifp_n_generation = ifp_n_generation

    # Initial fission source: uniform inside the sphere.
    bb_lo = (-GODIVA_RADIUS_CM,) * 3
    bb_hi = (GODIVA_RADIUS_CM,) * 3
    settings.source = openmc.IndependentSource(
        space=openmc.stats.Box(bb_lo, bb_hi),
        constraints={"fissionable": True},
    )

    # --- Tallies ------------------------------------------------------------
    # Cross-check tally: scalar IFP denominator.  The spatial+energy sum of
    # the ifp-importance map must equal this within statistical uncertainty.
    denom_tally = openmc.Tally(name="ifp-denominator")
    denom_tally.scores = ["ifp-denominator"]

    # The kinetics-parameter tallies that Dorville's IFP machinery already
    # produces; included so we can sanity-check beta_eff and Lambda alongside
    # the importance map.
    beta_tally = openmc.Tally(name="ifp-beta-numerator")
    beta_tally.scores = ["ifp-beta-numerator"]
    time_tally = openmc.Tally(name="ifp-time-numerator")
    time_tally.scores = ["ifp-time-numerator"]

    tallies = openmc.Tallies([denom_tally, beta_tally, time_tally])

    model = openmc.Model(geometry, materials, settings, tallies)

    # The new convenience helper: builds a (Mesh, Energy) ifp-importance
    # tally fitted to the geometry bounding box.
    model.add_ifp_importance_tally(
        mesh_dimension=mesh_dimension,
        # 20 log-spaced groups from 1e-5 eV to 20 MeV by default.
    )

    return model


if __name__ == "__main__":
    model = build_model()
    model.export_to_xml()
    print("Wrote materials.xml, geometry.xml, settings.xml, tallies.xml.")
