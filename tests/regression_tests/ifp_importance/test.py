"""Self-consistency regression test for the `ifp-importance` score.

Runs a small Godiva-like sphere problem and asserts:

  * the spatial+energy sum of ``ifp-importance`` equals ``ifp-denominator``
    within 5 sigma (this is exact in the asymptotic limit; the bound is
    statistical).
  * the spatial shape of ``ifp-importance(r)`` peaks near the center of
    the sphere (fundamental adjoint mode for a bare critical sphere).
  * outlier capping (``ifp_importance_cap``) cannot increase the total.

The test does not depend on a pre-baked ``results_true.dat`` file; it
self-validates from physics that the run itself produces.  It is skipped
automatically if ENDF/B cross sections are not available on the system.
"""
from __future__ import annotations

import os

import numpy as np
import pytest

import openmc


def _have_cross_sections() -> bool:
    return (os.environ.get("OPENMC_CROSS_SECTIONS") is not None
            or os.environ.get("OPENMC_ENDF_DATA") is not None)


pytestmark = pytest.mark.skipif(
    not _have_cross_sections(),
    reason="OPENMC_CROSS_SECTIONS / OPENMC_ENDF_DATA not set; "
           "skipping regression test that requires nuclear data.")


@pytest.fixture()
def godiva_like_model():
    openmc.reset_auto_ids()

    heu = openmc.Material(name="HEU")
    heu.set_density("g/cm3", 18.74)
    heu.add_nuclide("U234", 0.01017, "wo")
    heu.add_nuclide("U235", 0.93714, "wo")
    heu.add_nuclide("U238", 0.05269, "wo")

    sphere = openmc.Sphere(r=8.7407, boundary_type="vacuum")
    cell = openmc.Cell(region=-sphere, fill=heu)
    geometry = openmc.Geometry([cell])

    model = openmc.Model(geometry, openmc.Materials([heu]))
    model.settings.particles = 5_000
    model.settings.batches = 30
    model.settings.inactive = 10
    model.settings.ifp_n_generation = 5
    model.settings.source = openmc.IndependentSource(
        space=openmc.stats.Box(*cell.bounding_box),
        constraints={"fissionable": True},
    )

    # Cross-check tally.
    denom = openmc.Tally(name="ifp-denominator")
    denom.scores = ["ifp-denominator"]
    model.tallies.append(denom)

    # The score under test.
    model.add_ifp_importance_tally(mesh_dimension=(8, 8, 8))

    return model


def test_ifp_importance_sum_equals_denominator(run_in_tmpdir, godiva_like_model):
    sp_path = godiva_like_model.run()
    with openmc.StatePoint(sp_path) as sp:
        importance = sp.get_importance_function()
        denom = sp.get_tally(scores=["ifp-denominator"])

        importance_total = float(importance.mean.sum())
        importance_unc = float(np.sqrt(np.sum(importance.std_dev**2)))
        denom_value = float(denom.mean.sum())
        denom_unc = float(np.sqrt(np.sum(denom.std_dev**2)))

    sigma = float(np.hypot(importance_unc, denom_unc))
    diff = abs(importance_total - denom_value)
    assert sigma > 0.0, "sigma should be non-zero with a real run"
    assert diff < 5 * sigma, (
        f"sum(ifp-importance) = {importance_total:.4g} "
        f"differs from ifp-denominator = {denom_value:.4g} by "
        f"{diff/sigma:.2f}sigma (>5sigma tolerance).")


def test_ifp_importance_peaks_at_center(run_in_tmpdir, godiva_like_model):
    sp_path = godiva_like_model.run()
    with openmc.StatePoint(sp_path) as sp:
        importance = sp.get_importance_function()

    phi_r = importance.mean.sum(axis=-1)        # collapse energy
    nx, ny, nz = phi_r.shape
    central = phi_r[nx // 2, ny // 2, nz // 2]
    edge = phi_r[0, 0, 0]
    assert central > edge, (
        f"phi-dagger should peak at the center but central={central:.4g}, "
        f"edge={edge:.4g}.")


def test_ifp_importance_cap_cannot_increase_total(
        run_in_tmpdir, godiva_like_model):
    """A non-trivial cap can only reduce or preserve the total score."""
    # Reference run.
    sp_path = godiva_like_model.run()
    with openmc.StatePoint(sp_path) as sp:
        ref_total = float(sp.get_importance_function().mean.sum())

    # Capped run.
    godiva_like_model.settings.ifp_importance_cap = 0.5
    sp_path = godiva_like_model.run()
    with openmc.StatePoint(sp_path) as sp:
        capped_total = float(sp.get_importance_function().mean.sum())

    # Allow a small statistical slack: capping is monotone in expectation
    # but each run uses different random sampling.
    assert capped_total <= 1.05 * ref_total, (
        f"capped total {capped_total:.4g} exceeded reference total "
        f"{ref_total:.4g} by more than 5%; capping should not increase "
        f"contributions.")
