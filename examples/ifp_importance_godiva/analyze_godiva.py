"""Analyze a Godiva statepoint for `ifp-importance` validation.

Runs three checks against a statepoint produced by ``run_godiva.py``:

  1. Internal consistency: spatial+energy sum of `ifp-importance` should
     equal the scalar `ifp-denominator` to within statistical uncertainty.
  2. Kinetics parameters from the IFP scores (beta_eff, Lambda) should
     match the published Godiva values within a tolerance.
  3. Spatial shape of phi-dagger(r) should peak at the sphere center and
     fall toward the surface (the fundamental adjoint mode for a bare
     sphere).

The script does not depend on plotting libraries; it prints a tabular
report to stdout.  An optional plotting helper is provided if matplotlib
is available.
"""
from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np

import openmc
from build_godiva import GODIVA_RADIUS_CM, GODIVA_REFERENCE


def _format_with_unc(value: float, unc: float, fmt: str = ".4g") -> str:
    return f"{value:{fmt}} +/- {unc:{fmt}}"


def _agreement(value: float, unc: float, ref: float, ref_unc: float) -> str:
    """Two-sided agreement check on (value +/- unc) vs (ref +/- ref_unc)."""
    sigma = float(np.hypot(unc, ref_unc))
    if sigma == 0.0:
        return "exact" if value == ref else "DISAGREE"
    n_sigma = abs(value - ref) / sigma
    return f"{n_sigma:.1f}σ"


def check_consistency(sp: openmc.StatePoint) -> dict:
    """Sum-equals-denominator self-consistency check."""
    importance = sp.get_importance_function()
    importance_total = float(importance.mean.sum())
    importance_unc = float(np.sqrt(np.sum(importance.std_dev**2)))

    denom_tally = sp.get_tally(scores=["ifp-denominator"])
    denom_value = float(denom_tally.mean.sum())
    denom_unc = float(np.sqrt(np.sum(denom_tally.std_dev**2)))

    return {
        "importance_total": (importance_total, importance_unc),
        "denominator":      (denom_value, denom_unc),
        "agreement":        _agreement(importance_total, importance_unc,
                                       denom_value, denom_unc),
        "n_generation":     importance.ifp_n_generation,
    }


def check_kinetics_parameters(sp: openmc.StatePoint) -> dict:
    """Compute beta_eff and Lambda from IFP scores; compare to Godiva refs."""
    params = sp.get_kinetics_parameters()
    out: dict = {}

    if params.beta_effective is not None:
        b = params.beta_effective
        # `beta_effective` may be a scalar ufloat or a numpy array of ufloats.
        if hasattr(b, "shape") and b.shape:
            beta_total = float(sum(x.nominal_value for x in b))
            beta_total_unc = float(np.sqrt(sum(x.std_dev**2 for x in b)))
        else:
            beta_total = float(b.nominal_value)
            beta_total_unc = float(b.std_dev)
        ref, ref_unc = GODIVA_REFERENCE["beta_eff"]
        out["beta_eff"] = {
            "value":     (beta_total, beta_total_unc),
            "reference": (ref, ref_unc),
            "agreement": _agreement(beta_total, beta_total_unc, ref, ref_unc),
        }

    if params.generation_time is not None:
        L = params.generation_time
        L_value = float(L.nominal_value)
        L_unc = float(L.std_dev)
        ref, ref_unc = GODIVA_REFERENCE["Lambda"]
        out["Lambda"] = {
            "value":     (L_value, L_unc),
            "reference": (ref, ref_unc),
            "agreement": _agreement(L_value, L_unc, ref, ref_unc),
        }

    return out


def check_spatial_shape(sp: openmc.StatePoint) -> dict:
    """Verify phi-dagger peaks near the center of the sphere."""
    importance = sp.get_importance_function()
    phi_r = importance.mean.sum(axis=-1)        # collapse energy

    nx, ny, nz = phi_r.shape
    cx, cy, cz = nx // 2, ny // 2, nz // 2

    central_value = float(phi_r[cx, cy, cz])

    # Compare to a thin shell near the surface (last 10% of voxels along x).
    surface_slice = phi_r[-max(1, nx // 10):, :, :]
    surface_mean = float(surface_slice[surface_slice > 0].mean()) \
        if (surface_slice > 0).any() else 0.0

    return {
        "central_value":   central_value,
        "surface_mean":    surface_mean,
        "ratio":           (central_value / surface_mean) if surface_mean > 0
                            else float("inf"),
        "expected":        "central > surface (bare sphere fundamental mode)",
    }


def report(sp: openmc.StatePoint) -> None:
    print("=" * 78)
    print(f" Godiva ifp-importance validation report")
    print(f" statepoint: {sp.filename}")
    print("=" * 78)

    consistency = check_consistency(sp)
    print()
    print("Self-consistency check (sum of ifp-importance vs ifp-denominator)")
    print("-" * 78)
    imp = consistency["importance_total"]
    den = consistency["denominator"]
    print(f"  sum(ifp-importance)  = {_format_with_unc(*imp)}")
    print(f"  ifp-denominator      = {_format_with_unc(*den)}")
    print(f"  agreement            = {consistency['agreement']}")
    print(f"  ifp_n_generation     = {consistency['n_generation']}")

    kin = check_kinetics_parameters(sp)
    if kin:
        print()
        print("Kinetics parameters (IFP) vs published Godiva reference")
        print("-" * 78)
        if "beta_eff" in kin:
            v = kin["beta_eff"]
            print(f"  beta_eff   = {_format_with_unc(*v['value'], '.4e')}")
            print(f"  reference  = {_format_with_unc(*v['reference'], '.4e')}")
            print(f"  agreement  = {v['agreement']}")
        if "Lambda" in kin:
            v = kin["Lambda"]
            print(f"  Lambda     = {_format_with_unc(*v['value'], '.4e')} s")
            print(f"  reference  = {_format_with_unc(*v['reference'], '.4e')} s")
            print(f"  agreement  = {v['agreement']}")

    shape = check_spatial_shape(sp)
    print()
    print("Spatial shape of phi-dagger (collapsed over energy)")
    print("-" * 78)
    print(f"  central voxel value  = {shape['central_value']:.4g}")
    print(f"  surface-shell mean   = {shape['surface_mean']:.4g}")
    print(f"  central / surface    = {shape['ratio']:.3f}")
    print(f"  expectation          = {shape['expected']}")
    print()
    print(f"k_eff = {sp.keff}")


def maybe_plot_radial(sp: openmc.StatePoint, output: Path) -> None:
    """Plot phi-dagger vs r if matplotlib is available; otherwise skip."""
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print("(matplotlib not installed; skipping radial plot)")
        return

    importance = sp.get_importance_function()
    phi_r = importance.mean.sum(axis=-1)

    nx, ny, nz = phi_r.shape
    mesh = importance.mesh
    ll = np.asarray(mesh.lower_left)
    ur = np.asarray(mesh.upper_right)
    centers_x = np.linspace(ll[0], ur[0], nx + 1)
    centers_x = 0.5 * (centers_x[:-1] + centers_x[1:])
    centers_y = np.linspace(ll[1], ur[1], ny + 1)
    centers_y = 0.5 * (centers_y[:-1] + centers_y[1:])
    centers_z = np.linspace(ll[2], ur[2], nz + 1)
    centers_z = 0.5 * (centers_z[:-1] + centers_z[1:])

    X, Y, Z = np.meshgrid(centers_x, centers_y, centers_z, indexing="ij")
    R = np.sqrt(X**2 + Y**2 + Z**2)

    mask = phi_r > 0
    r_vals = R[mask].ravel()
    phi_vals = phi_r[mask].ravel()
    order = np.argsort(r_vals)
    r_vals = r_vals[order]
    phi_vals = phi_vals[order]

    # Bin radially.
    n_bins = 30
    edges = np.linspace(0, GODIVA_RADIUS_CM, n_bins + 1)
    means = np.zeros(n_bins)
    for i in range(n_bins):
        sel = (r_vals >= edges[i]) & (r_vals < edges[i + 1])
        if sel.any():
            means[i] = phi_vals[sel].mean()

    centers = 0.5 * (edges[:-1] + edges[1:])
    means_normalized = means / means.max() if means.max() > 0 else means

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(centers, means_normalized, "o-", label=r"$\phi^{\dagger}(r)$ (Monte Carlo)")
    # Reference fundamental-mode shape: cosine-like for a bare sphere.
    r_ref = np.linspace(0, GODIVA_RADIUS_CM, 200)
    sin_ref = np.sin(np.pi * (1 - r_ref / GODIVA_RADIUS_CM))
    sin_ref /= sin_ref.max() if sin_ref.max() > 0 else 1.0
    ax.plot(r_ref, sin_ref, "k--", label=r"$\sin(\pi (1 - r/R))$ (analytic shape)")
    ax.set_xlabel("radius r [cm]")
    ax.set_ylabel(r"$\phi^{\dagger}$ (normalized)")
    ax.set_title("Godiva adjoint flux: ifp-importance vs analytic shape")
    ax.legend()
    fig.tight_layout()
    fig.savefig(output, dpi=120)
    print(f"Wrote radial plot: {output}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("statepoint", type=Path,
                        help="Path to OpenMC statepoint HDF5 file.")
    parser.add_argument("--plot", type=Path, default=None,
                        help="Optional path to write a radial plot to.")
    args = parser.parse_args()

    with openmc.StatePoint(args.statepoint) as sp:
        report(sp)
        if args.plot is not None:
            maybe_plot_radial(sp, args.plot)


if __name__ == "__main__":
    main()
