"""Run the Godiva ifp-importance benchmark end-to-end.

Builds the model from ``build_godiva.py``, runs OpenMC, and prints the
analysis report from ``analyze_godiva.py``.

Requires ENDF/B cross sections (set ``OPENMC_CROSS_SECTIONS`` or pass
``--cross-sections``).
"""
from __future__ import annotations

import argparse
from pathlib import Path

from build_godiva import build_model
from analyze_godiva import maybe_plot_radial, report

import openmc


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--particles", type=int, default=50_000)
    parser.add_argument("--inactive", type=int, default=30)
    parser.add_argument("--active", type=int, default=200)
    parser.add_argument("--ifp-generations", type=int, default=10)
    parser.add_argument("--mesh", type=int, default=30,
                        help="cubic mesh dimension (--mesh N -> NxNxN)")
    parser.add_argument("--energy-groups", type=int, default=20)
    parser.add_argument("--cross-sections", type=Path, default=None)
    parser.add_argument("--cwd", type=Path, default=Path("godiva_run"))
    parser.add_argument("--plot", type=Path, default=None)
    args = parser.parse_args()

    args.cwd.mkdir(parents=True, exist_ok=True)

    model = build_model(
        n_particles=args.particles,
        n_inactive=args.inactive,
        n_active=args.active,
        ifp_n_generation=args.ifp_generations,
        mesh_dimension=(args.mesh,) * 3,
        n_energy_groups=args.energy_groups,
    )

    if args.cross_sections is not None:
        model.materials.cross_sections = str(args.cross_sections)

    sp_path = model.run(cwd=str(args.cwd))

    with openmc.StatePoint(sp_path) as sp:
        report(sp)
        if args.plot is not None:
            maybe_plot_radial(sp, args.plot)


if __name__ == "__main__":
    main()
