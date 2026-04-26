"""Validation: FREYA-enabled fission sampling smoke tests.

These tests run actual OpenMC simulations exercising the Phase 4 analog
FREYA mode and the Phase 5 FreyaSFSource. They are marked to skip unless:

  - OPENMC_USE_FISSION_LIB=1 in the environment (OpenMC was built with
    FREYA support), and
  - OPENMC_CROSS_SECTIONS points at a valid HDF5 cross-section library.

Without those, the tests are skipped — they can't even run, let alone
assert numbers. With them, the tests assert *coarse* sanity bounds, not
benchmark-grade reference values; the latter is a paper-scale effort.
For tighter regression coverage, see the Zywiec 2026 paper validation
(``Rossi-alpha Benchmark Validation of a Static Alpha Eigenvalue
Capability in OpenMC``) which compares 21 + 33 benchmark configurations
against measured Rossi-α data.
"""

import os
import math

import openmc
import pytest


def _has_fission_lib() -> bool:
    return os.environ.get('OPENMC_USE_FISSION_LIB', '').lower() in (
        '1', 'true', 'yes', 'on')


def _has_cross_sections() -> bool:
    path = os.environ.get('OPENMC_CROSS_SECTIONS', '')
    return bool(path) and os.path.isfile(path)


needs_freya = pytest.mark.skipif(
    not (_has_fission_lib() and _has_cross_sections()),
    reason='Requires OpenMC built with OPENMC_USE_FISSION_LIB and a '
           'cross-section library at OPENMC_CROSS_SECTIONS.')


def _heu_sphere_model(*, calculate_alpha: bool, freya_analog: bool):
    material = openmc.Material(name='heu')
    material.add_nuclide('U235', 0.94)
    material.add_nuclide('U238', 0.05)
    material.add_nuclide('U234', 0.01)
    material.set_density('g/cm3', 18.74)

    sphere = openmc.Sphere(r=8.74, boundary_type='vacuum')
    cell = openmc.Cell(region=-sphere, fill=material)
    geometry = openmc.Geometry([cell])

    settings = openmc.Settings()
    settings.batches = 30
    settings.inactive = 10
    settings.particles = 1000
    settings.calculate_alpha = calculate_alpha
    if freya_analog:
        settings.freya_analog = True
    settings.source = openmc.IndependentSource(
        space=openmc.stats.Point((0.0, 0.0, 0.0)),
        constraints={'fissionable': True},
    )

    return openmc.Model(geometry=geometry, settings=settings)


@needs_freya
def test_freya_analog_runs_to_completion(run_in_tmpdir):
    """Phase 4 smoke: a Godiva-like sphere runs cleanly with analog FREYA on
    and produces a sane k_eff."""
    model = _heu_sphere_model(calculate_alpha=False, freya_analog=True)
    sp_path = model.run()
    with openmc.StatePoint(sp_path) as sp:
        keff = sp.keff.nominal_value
    # Bare HEU sphere of this size sits very near critical; permit broad
    # tolerance for low-statistics smoke run.
    assert 0.7 < keff < 1.3, f'unexpected k_eff: {keff}'


@needs_freya
def test_freya_analog_alpha_eigenvalue_signs(run_in_tmpdir):
    """Phase 4 + alpha: HEU sphere with analog FREYA + IFP should give a
    negative alpha_dc (subcritical on prompt timescale) of order 1e6 s^-1."""
    model = _heu_sphere_model(calculate_alpha=True, freya_analog=True)
    sp_path = model.run()
    with openmc.StatePoint(sp_path) as sp:
        alpha_dc = sp.alpha_dc_ifp.nominal_value
        ell_p = sp.lifetime_p_ifp.nominal_value
        beta = sp.beta_eff.nominal_value

    assert ell_p > 0
    # alpha_dc = -beta_eff / ell_p; for HEU beta ~ 0.0065 and ell_p ~ ns,
    # so |alpha_dc| ~ 1e6 s^-1.
    assert alpha_dc < 0, f'expected negative alpha_dc, got {alpha_dc}'
    assert 1e5 < abs(alpha_dc) < 1e8, (
        f'alpha_dc ({alpha_dc}) out of plausible HEU range')
    # Pin-test the paper-form relationship.
    assert math.isclose(alpha_dc, -beta / ell_p, rel_tol=1e-9)


@needs_freya
@pytest.mark.parametrize('za', [92238, 94238, 94240, 94242, 96244, 98252])
def test_freya_sf_source_runs(run_in_tmpdir, za):
    """Phase 5 smoke: FreyaSFSource for each FREYA-supported SF isotope
    (U-238, Pu-238, Pu-240, Pu-242, Cm-244, Cf-252 per react.dat) builds
    a populated source bank and a fixed-source run completes."""
    material = openmc.Material()
    material.add_nuclide('H1', 1.0)
    material.set_density('g/cm3', 1.0)

    sphere = openmc.Sphere(r=50.0, boundary_type='vacuum')
    cell = openmc.Cell(region=-sphere, fill=material)
    geometry = openmc.Geometry([cell])

    settings = openmc.Settings()
    settings.run_mode = 'fixed source'
    settings.particles = 200
    settings.batches = 5
    settings.source = openmc.FreyaSFSource(
        za=za, position=(0, 0, 0), n_events=500)

    model = openmc.Model(geometry=geometry, settings=settings)
    # Just verifying it runs; the C++ FreyaSFSource ctor exercises FREYA's
    # SF generator and would fatal_error if the isotope or data are missing.
    model.run()
