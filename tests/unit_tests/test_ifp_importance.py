"""Tests for the `ifp-importance` tally score.

These tests exercise the input-validation and bookkeeping paths that don't
require nuclear cross-section data; the end-to-end run is exercised by the
Godiva benchmark in ``examples/ifp_importance_godiva/`` and (when cross
sections are available) by the regression test
``tests/regression_tests/ifp_importance/``.
"""
from __future__ import annotations

import numpy as np
import pytest

import openmc


# ---------------------------------------------------------------------------
# Settings serialization
# ---------------------------------------------------------------------------

def test_xml_roundtrip_ifp_importance_cap(run_in_tmpdir):
    """ifp_importance_cap should round-trip through XML."""
    settings = openmc.Settings()
    settings.ifp_n_generation = 5
    settings.ifp_importance_cap = 12.5
    settings.export_to_xml()

    rt = openmc.Settings.from_xml()
    assert rt.ifp_importance_cap == pytest.approx(12.5)


def test_ifp_importance_cap_rejects_negative():
    settings = openmc.Settings()
    with pytest.raises(ValueError):
        settings.ifp_importance_cap = -1.0


# ---------------------------------------------------------------------------
# Convenience helper
# ---------------------------------------------------------------------------

@pytest.fixture
def fissile_geometry():
    openmc.reset_auto_ids()
    mat = openmc.Material()
    mat.add_nuclide("U235", 1.0)
    mat.set_density("g/cm3", 18.0)
    sphere = openmc.Sphere(r=5.0, boundary_type="vacuum")
    cell = openmc.Cell(region=-sphere, fill=mat)
    return openmc.Geometry([cell])


def test_add_ifp_importance_tally_default_mesh(fissile_geometry):
    """Helper builds a Mesh + Energy tally fitted to the geometry."""
    model = openmc.Model(geometry=fissile_geometry)
    model.settings.particles = 100
    model.settings.batches = 10
    model.settings.inactive = 5
    model.settings.ifp_n_generation = 3

    tally = model.add_ifp_importance_tally(mesh_dimension=(4, 4, 4))

    assert "ifp-importance" in tally.scores
    assert any(isinstance(f, openmc.MeshFilter) for f in tally.filters)
    assert any(isinstance(f, openmc.EnergyFilter) for f in tally.filters)

    # Calling the helper twice should not duplicate the tally.
    tally2 = model.add_ifp_importance_tally(mesh_dimension=(4, 4, 4))
    assert tally2 is tally
    assert sum(1 for t in model.tallies
               if "ifp-importance" in t.scores) == 1


def test_add_ifp_importance_tally_explicit_mesh(fissile_geometry):
    """User-supplied mesh and energy bins are honored."""
    model = openmc.Model(geometry=fissile_geometry)
    mesh = openmc.RegularMesh()
    mesh.dimension = (3, 3, 3)
    mesh.lower_left = (-2, -2, -2)
    mesh.upper_right = (2, 2, 2)

    bins = np.array([1e-5, 1.0, 1e3, 1e6, 2e7])
    tally = model.add_ifp_importance_tally(mesh=mesh, energy_groups=bins)

    e_filter = next(f for f in tally.filters if isinstance(f, openmc.EnergyFilter))
    np.testing.assert_allclose(e_filter.values, bins)


# ---------------------------------------------------------------------------
# Diagnostic helper
# ---------------------------------------------------------------------------

def test_adjoint_weighted_shannon_entropy_zero_when_degenerate():
    """All mass in one bin -> entropy = 0."""
    forward = np.array([1.0, 0.0, 0.0])
    adjoint = np.array([1.0, 1.0, 1.0])
    h = openmc.adjoint_weighted_shannon_entropy(forward, adjoint)
    assert h == pytest.approx(0.0, abs=1e-12)


def test_adjoint_weighted_shannon_entropy_uniform():
    """Uniform weighted distribution over N bins -> log2(N) bits."""
    forward = np.ones(8)
    adjoint = np.ones(8)
    h = openmc.adjoint_weighted_shannon_entropy(forward, adjoint)
    assert h == pytest.approx(3.0, rel=1e-9)


def test_adjoint_weighted_shannon_entropy_shape_check():
    with pytest.raises(ValueError):
        openmc.adjoint_weighted_shannon_entropy(
            np.zeros(3), np.zeros(4))


def test_adjoint_weighted_shannon_entropy_negative_clipped():
    """Tally noise (negative entries) should be clipped, not crash."""
    forward = np.array([1.0, 1.0, 1.0])
    adjoint = np.array([1.0, -1e-12, 1.0])  # tiny negative noise
    h = openmc.adjoint_weighted_shannon_entropy(forward, adjoint)
    assert np.isfinite(h) and h >= 0.0
