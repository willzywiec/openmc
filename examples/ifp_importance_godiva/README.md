# Godiva benchmark for `ifp-importance`

A bare HEU sphere from ICSBEP HEU-MET-FAST-001, used to validate the
binned IFP adjoint flux against published kinetics parameters and against
the textbook fundamental-mode shape for a critical sphere.

## Files

| File                  | Purpose                                                                |
| --------------------- | ---------------------------------------------------------------------- |
| `build_godiva.py`     | Pure model builder: returns an `openmc.Model`. Importable.             |
| `run_godiva.py`       | End-to-end driver: build, run, report.                                 |
| `analyze_godiva.py`   | Statepoint analysis: consistency, kinetics, spatial-shape checks, plot.|

The build / run / analyze split lets the regression test reuse `build_model()`
and `check_consistency()` without depending on cross sections being present.

## Quick start

```bash
# Build XML only (no run)
python build_godiva.py

# Full run + report (requires ENDF/B cross sections)
python run_godiva.py --particles 50000 --active 200 --plot phi_dagger.png

# Just analyze an existing statepoint
python analyze_godiva.py godiva_run/statepoint.230.h5 --plot phi_dagger.png
```

## What the analysis checks

1. **Self-consistency.** The spatial+energy sum of `ifp-importance`
   must equal the scalar `ifp-denominator` to within statistical
   uncertainty.  This catches every wiring bug.

2. **Kinetics parameters.** Running this same model with Dorville's
   IFP machinery active produces `beta_eff` and `Lambda` from the
   pre-existing scores.  These are checked against the ICSBEP
   reference values (`645 +/- 13 pcm`, `~5.8 ns`).

3. **Spatial shape.** For a bare critical sphere, `phi-dagger(r)` peaks
   at the center and falls toward the surface (the J₀-like fundamental
   adjoint mode).  The script verifies the central voxel exceeds a
   surface-shell mean and, with `--plot`, overlays the analytic
   shape `sin(pi (1 - r/R))` for visual comparison.

## Cross-checking against deterministic adjoints

The analytic shape is a one-group, infinite-cylinder approximation;
a quantitative cross-check requires running the same problem in a
deterministic adjoint code (Denovo, PARTISN) on the same mesh + group
structure, then comparing cosine similarity:

```python
mc = importance.mean.sum(axis=-1).ravel()
mc /= np.linalg.norm(mc)
det = denovo_phi_dagger.ravel()
det /= np.linalg.norm(det)
cos_sim = float(mc @ det)   # acceptance: > 0.99 for fundamental mode
```

The deterministic-solver coupling is left as a future exercise (see
`IFP_IMPORTANCE_ROADMAP.md`).
