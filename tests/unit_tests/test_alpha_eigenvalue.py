"""Pin-test for the alpha eigenvalue formulas.

Verifies that the values stored in the statepoint by the C++ kinetics
calculation satisfy the formulas published in Zywiec, "Rossi-alpha Benchmark
Validation of a Static Alpha Eigenvalue Capability in OpenMC":

    ell_p     = S_ifp-prompt-time-numerator / S_ifp-prompt-denominator
    Lambda_p  = ell_p / k_p
    alpha_dc  = -beta_eff / ell_p
    alpha     = (k_p - 1) / ell_p

with k_p = k_eff * (1 - beta_eff). Five formula revisions landed on this code
without an end-to-end pin test; this guards against silently drifting back to
one of the earlier (incorrect) forms.
"""

import math

import openmc


def test_alpha_eigenvalue_formulas(run_in_tmpdir):
    material = openmc.Material(name="core")
    material.add_nuclide("U235", 1.0)
    material.set_density("g/cm3", 18.0)

    sphere = openmc.Sphere(r=10.0, boundary_type="vacuum")
    cell = openmc.Cell(region=-sphere, fill=material)
    geometry = openmc.Geometry([cell])

    settings = openmc.Settings()
    settings.particles = 1000
    settings.batches = 20
    settings.inactive = 5
    settings.calculate_alpha = True
    settings.source = openmc.IndependentSource(
        space=openmc.stats.Box(*cell.bounding_box),
        constraints={"fissionable": True},
    )

    model = openmc.Model(geometry=geometry, settings=settings)
    sp_path = model.run()

    with openmc.StatePoint(sp_path) as sp:
        k_eff = sp.keff.nominal_value
        beta = sp.beta_eff.nominal_value
        ell_p = sp.lifetime_p_ifp.nominal_value
        lambda_p = sp.lambda_p_ifp.nominal_value
        alpha_dc = sp.alpha_dc_ifp.nominal_value
        alpha = sp.alpha_ifp.nominal_value

    assert ell_p > 0.0
    k_p = k_eff * (1.0 - beta)

    # Lambda_p = ell_p / k_p
    assert math.isclose(lambda_p, ell_p / k_p, rel_tol=1e-9)

    # alpha_dc = -beta_eff / ell_p
    assert math.isclose(alpha_dc, -beta / ell_p, rel_tol=1e-9)

    # alpha = (k_p - 1) / ell_p
    assert math.isclose(alpha, (k_p - 1.0) / ell_p, rel_tol=1e-9)
