# `ifp-importance`: deferred work

This branch ships Phases 1-4 plus selected Phase 6 items (adjoint-weighted
Shannon entropy).  The items below are intentionally deferred; each is large
enough to deserve its own PR and validation cycle.

## Phase 4 (deferred)

These optimizations were considered but skipped because the simpler
implementation in this branch is fast enough for typical benchmarks:

- **Cache filter bin indices in the chain**.  At chain birth, evaluate each
  active `ifp-importance` tally's filter bin once and store the resulting
  integer index alongside `r_born` / `E_born`.  Removes the per-fission
  `exhaustive_find_cell` call.  Estimated 10-100x speedup for cell-heavy
  tallies.  Requires substantial refactor of the chain layout and is best
  done after profiling shows the geometry walk is hot.
- **Flat-array chain storage**.  Replace `vector<vector<T>>` with a flat
  `vector<double>` of size `n_particles * n_generation * stride` and a
  stride accessor.  Better cache locality, serializes to MPI buffer for
  free.  Bigger refactor; pure speed win.

## Phase 5 (new physics)

- **Angular-resolved adjoint**.  Add a direction bank parallel to the
  position bank; allow `PolarFilter` / `AzimuthalFilter`.  Needed for
  streaming geometries (ducts, fast-reactor coolant channels).
- **Time-binned adjoint**.  Add a birth-time bank; allow `TimeFilter`.
  Couples directly to time-dependent / alpha-eigenvalue work.
- **Adjoint-weighted current**.  Bin per-collision contributions instead of
  per-fission progeny weight.  Equivalent to a more general adjoint-weighted
  reaction rate.
- **Generalized response score**.  Allow the user to supply a
  response function `R(E_origin)` from XML.  Score becomes
  `Σ R(E_origin) * progeny`, generalizing every fixed response that the
  current `ifp-beta-numerator` / `ifp-time-numerator` pair encodes.

## Phase 6 (new applications)

- **Adjoint-weight-window generation**.  Take the binned `phi†(r,E)`,
  smooth it, invert it, emit an OpenMC weight-window file.  CADIS-style
  automatic variance reduction without a deterministic solver.  Integrates
  with the existing `openmc.WeightWindows` infrastructure.
- **Sensitivity / uncertainty (S/U) integration**.  Combine
  `ifp-importance` with the existing perturbation infrastructure
  (`openmc.Tally(derivative=...)`) to compute properly adjoint-weighted
  `dk/dΣ`.  Closes the loop for cross-section uncertainty propagation.
- **Generalized perturbation theory (GPT)**.  Reaction-rate sensitivities
  and dose-rate sensitivities.  Once `phi†` is available pointwise, GPT is
  bookkeeping plus a few new score types.
- **Coupling to deterministic adjoint solvers**.  Export `phi†` in formats
  Denovo / MPACT / Serpent can ingest, and vice versa.  Lets users mix
  adjoints across codes.

## Tracking

Each item gets its own branch off `develop`.  Pre-merge gate per item:

- A regression test demonstrating the new feature exercises real
  cross sections.
- Validation against a published reference (deterministic code or
  benchmark study).
- Documentation in `docs/source/usersguide/`.

The Phase 1-4 + adjoint-Shannon-entropy work in this branch is the
foundation everything above stands on.  None of it is a prerequisite for
shipping the current PR.
