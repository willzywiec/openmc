# IFP Importance Tally: Design Document

## 1. Goal

Expose the per-neutron progeny weights that the iterated fission probability
(IFP) machinery already tracks as a **binned tally**, producing the
forward-adjoint importance function

```
phi†(r, E) ≈ < N_progeny >  bin-by-bin
```

on a user-specified phase-space grid, instead of collapsing it into the two
scalar inner products that the existing IFP scores already compute
(`ifp-beta-numerator`, `ifp-time-numerator`, `ifp-denominator`).

The new tally score is named **`ifp-importance`**.

## 2. Background: how the existing IFP code works

References:
- `src/ifp.cpp`, `include/openmc/ifp.h`
- `src/tallies/tally_scoring.cpp:944-1034`  (existing IFP score cases)
- `src/tallies/tally.cpp:192-248`            (IFP detection / activation)
- `src/eigenvalue.cpp:148-427`               (IFP MPI transfer in `synchronize_bank`)
- `src/physics.cpp:341-344`                  (call site of `ifp()`)
- `include/openmc/bank.h:27-33`              (global IFP banks)
- `include/openmc/constants.h:309-332`       (`SCORE_IFP_*` enum)
- `openmc/lib/tally.py:102-111`              (Python score map)
- `openmc/statepoint.py:817-868`, `openmc/model/model.py:248-275`
- Kiedrowski, Brown, Wilson (ANS 2017); Dorville, Labrie-Cleary, Romano (M&C 2025).

### 2.1 Per-neutron progeny chain

For each source neutron currently being transported on a rank, OpenMC keeps an
**ordered chain of length up to N = `settings::ifp_n_generation`**, stored as a
`vector<vector<T>>` indexed by the neutron's local index in the source bank
(`p.current_work() - 1`):

| Bank                                    | Type                  | Meaning                                         |
| --------------------------------------- | --------------------- | ----------------------------------------------- |
| `simulation::ifp_source_delayed_group_bank` | `vector<vector<int>>`    | Birth delayed group of each ancestor            |
| `simulation::ifp_source_lifetime_bank`      | `vector<vector<double>>` | Lifetime (at fission) of each ancestor          |
| `simulation::ifp_fission_delayed_group_bank` | `vector<vector<int>>`    | Same, indexed by fission-bank slot              |
| `simulation::ifp_fission_lifetime_bank`     | `vector<vector<double>>` | Same, indexed by fission-bank slot              |

Convention: `chain[0]` = oldest (originator, N-1 generations ago);
`chain[N-1]` = parent of the descendant currently being transported.

### 2.2 Chain update on fission

In `src/physics.cpp:316-344`, when a fissioning particle `p` deposits a progeny
site at `idx` of `simulation::fission_bank`, `ifp(p, idx)` is invoked
(`src/ifp.cpp:31-44`). It calls the rolling-buffer template `_ifp()`
(`include/openmc/ifp.h:46-65`) which appends `p`'s value (e.g.
`p.delayed_group()`, `p.lifetime()`) to the parent's chain and trims the head if
the chain has reached length N.  Thread safety is provided by the unique `idx`
returned by `fission_bank.thread_safe_append()` and by per-source-slot indexing
on the source side.

### 2.3 Inter-generation MPI transfer

In `src/eigenvalue.cpp:148-427` the function `synchronize_bank()` combs the
fission bank to build the next generation's source bank.  The IFP chains are
shipped alongside the source sites:

- `broadcast_ifp_n_generation`        (rank 0 establishes N)
- `send_ifp_info` / `receive_ifp_data` (flatten chain to `n_gen × n_sites` and
  Isend/Irecv as `MPI_INT` / `MPI_DOUBLE`)
- `deserialize_ifp_info`              (reconstruct `vector<vector<...>>` on
  receiver)

After `MPI_Waitall` the new generation's `source_bank` and the matching
`ifp_source_*_bank` are both populated.

### 2.4 Scoring

In `src/tallies/tally_scoring.cpp:944-1034`, the existing IFP scores all live in
the **collision** path (`score_general_ce_nonanalog`), guarded by
`p.fission()`.  The pattern is uniform:

```cpp
const auto& chain = simulation::ifp_source_delayed_group_bank[p.current_work()-1];
if (chain.size() == settings::ifp_n_generation) {
    if (chain[0] > 0)               // <-- this is the response function
        score = p.wgt_last();       // <-- this is the progeny weight
}
```

The two inner products that exist today are:

- **β_eff numerator**: response = `chain[0] > 0` (delayed indicator)
- **Λ numerator**:    response = `chain[0]` interpreted as lifetime
- **denominator**:    response = 1

### 2.5 Filter binning currently uses the *current* particle

`FilterBinIter` (top of `score_collision_tally` /
`score_analog_tally`, `tally_scoring.cpp:31-92, 2576-2650`) resolves filter bins
from `p`'s current state (`p.r()`, `p.E()`, `p.cell_last(...)`).  This is the
descendant's state, not the originator's.  This is the central obstacle for
binning progeny by the originator's phase space.

## 3. Conceptual change

Conceptually we want exactly the existing `ifp-denominator` behavior, except
the score `p.wgt_last()` is binned by **the originator's birth phase space**
(`r_born^(0)`, `E_born^(0)`) instead of the descendant's current phase space.

```
S_ifp-importance(r, E) = sum over fissions of asymptotic-gen descendants
                         of  p.wgt_last(),
                         binned by   (r_born^(0), E_born^(0))
                         where (0) = oldest entry of the IFP chain
```

Normalising by the per-bin source rate yields `phi†(r, E)` up to an overall
constant.

## 4. Files to modify

### 4.1 New / extended data structures

| File                             | Change                                                                      |
| -------------------------------- | --------------------------------------------------------------------------- |
| `include/openmc/constants.h`     | Add `SCORE_IFP_IMPORTANCE = -23`                                            |
| `include/openmc/particle_data.h` | Add `double E_born_` and accessor `E_born()`                                |
| `include/openmc/bank.h`          | Declare `ifp_source_position_bank`, `ifp_source_E_born_bank`, plus fission counterparts |
| `src/bank.cpp`                   | Define those banks; clear them in `free_memory_bank()`                      |
| `include/openmc/settings.h`      | Add `bool ifp_track_phase_space {false}`                                    |
| `src/settings.cpp`               | Default + XML wiring (mirrors `ifp_n_generation`)                           |

The two new banks are **only allocated** when `ifp_track_phase_space` is true,
to keep the existing memory footprint untouched for users not using
`ifp-importance`.

### 4.2 Score plumbing

| File                              | Change                                                              |
| --------------------------------- | ------------------------------------------------------------------- |
| `src/reaction.cpp:205-209`        | Add `{SCORE_IFP_IMPORTANCE, "ifp-importance"}` to score-name table  |
| `src/output.cpp:644-646`          | Add long-name `"IFP importance"`                                    |
| `openmc/lib/tally.py:102-111`     | Add `-23: 'ifp-importance'` to `_SCORES`                            |

### 4.3 Tally activation and validation

| File                              | Change                                                                                 |
| --------------------------------- | -------------------------------------------------------------------------------------- |
| `src/tallies/tally.cpp:194-248`   | Treat `SCORE_IFP_IMPORTANCE` as an IFP score (set `ifp_on`, validate gen, set new flag `ifp_track_phase_space`) |
| `src/tallies/tally.cpp:656-660`   | Force `TallyEstimator::COLLISION` for `SCORE_IFP_IMPORTANCE`                            |
| `src/tallies/tally.cpp:563-573`   | Validate that `ifp-importance` is the **only score** in its tally (filter binning will be done with originator state, which would be wrong for any other score) |

### 4.4 Chain population

| File              | Change                                                                                  |
| ----------------- | --------------------------------------------------------------------------------------- |
| `src/particle.cpp:255-303` (`from_source`) | Set `E_born_ = src->E`                                                  |
| `src/ifp.cpp:31-52` (`ifp`, `resize_simulation_ifp_banks`) | If `ifp_track_phase_space`, also `_ifp()` `(p.r_born(), p.E_born())` into the position / energy banks |
| `src/ifp.cpp:53-63` (`copy_ifp_data_from_fission_banks`) | Copy phase-space chains as well                                |
| `src/ifp.cpp:65-200` (MPI helpers + serial helpers) | Add a parallel set of helpers for the position / energy banks |
| `src/eigenvalue.cpp:200-426` (`synchronize_bank`)   | Allocate temp buffers and call the new helpers when `ifp_track_phase_space` |

### 4.5 Score evaluation

A new function `score_ifp_importance_tally(Particle& p)` is added near
`score_collision_tally` in `tally_scoring.cpp`.  It is invoked from
`score_collision_tally` after the regular tally loop.  Pseudocode:

```cpp
void score_ifp_importance_tally(Particle& p) {
  if (!settings::ifp_on || !settings::ifp_track_phase_space) return;
  if (p.type() != ParticleType::neutron || !p.fission()) return;

  const auto& positions = simulation::ifp_source_position_bank[p.current_work()-1];
  const auto& energies  = simulation::ifp_source_E_born_bank   [p.current_work()-1];
  if (positions.size() != settings::ifp_n_generation) return;

  // Save particle's current state.
  Position saved_r       = p.r();
  Direction saved_u      = p.u();
  double saved_E         = p.E();
  // ... and the localized coordinate stack the cell filter walks

  // Substitute originator state.
  p.r() = positions[0];
  p.E() = energies[0];
  p.r_last() = positions[0];
  p.E_last() = energies[0];
  // Re-find cell so cell / mesh filters see the right cell index.
  exhaustive_find_cell(p);

  // Drive standard filter binning over the substituted state.
  for (auto i_tally : model::active_ifp_importance_tallies) {
      // FilterBinIter + accumulator over score = p.wgt_last()
  }

  // Restore.
  p.r() = saved_r;  p.u() = saved_u;  p.E() = saved_E;
  exhaustive_find_cell(p);   // restore cell stack
}
```

The actual implementation will hold a small POD of saved state and use the
existing `FilterBinIter` with a fresh `filter_matches()` slot.  Re-finding the
cell is the expensive step; for the cell filter it is unavoidable, but for
`MeshFilter` and `EnergyFilter` it is not needed since they use only `r` and
`E`. A fast path for tallies whose filters are all of `{Mesh, Energy, Universe,
Material, Polar/Azimuthal}` skips the cell re-find.

### 4.6 Python API

| File                              | Change                                                                          |
| --------------------------------- | ------------------------------------------------------------------------------- |
| `openmc/tallies.py`               | No change needed (string is opaque; validated in C++)                           |
| `openmc/statepoint.py`            | Optional helper `get_importance_function()` returning the binned `phi†(r,E)`    |
| `openmc/model/model.py`           | Optional `add_ifp_importance_tally(filters=...)` analogous to `add_kinetics_parameters_tallies` |

### 4.7 Documentation

| File                              | Change                                                  |
| --------------------------------- | ------------------------------------------------------- |
| `docs/source/usersguide/kinetics.rst` | Add `ifp-importance` row to the score table        |
| `docs/source/methods/eigenvalue.rst`  | Brief subsection citing Kiedrowski 2017 / M&C 2025 |

## 5. Tally specification (user input)

Python:

```python
mesh = openmc.RegularMesh.from_domain(...)
mesh_filter   = openmc.MeshFilter(mesh)
energy_filter = openmc.EnergyFilter(np.logspace(-5, 7, 21))   # 20 groups

importance_tally = openmc.Tally(name="phi_dagger")
importance_tally.scores  = ["ifp-importance"]              # single score
importance_tally.filters = [mesh_filter, energy_filter]    # any spatial + energy
```

XML:

```xml
<tally id="42">
  <filters>1 2</filters>
  <scores>ifp-importance</scores>
</tally>
```

Validation rules enforced in C++:

1. Run mode must be `EIGENVALUE`.
2. `ifp_n_generation` must be set (or defaults to 10) and `<= n_inactive`.
3. The tally containing `ifp-importance` must contain **only** that score
   (filter binning is on the originator's state).
4. `EnergyoutFilter`, `DelayedGroupFilter`, surface filters are rejected as
   incompatible (these refer to the descendant's outgoing state, not the
   originator's birth state).
5. Allowed filters: `MeshFilter`, `CellFilter`, `EnergyFilter`,
   `UniverseFilter`, `MaterialFilter`, `PolarFilter`, `AzimuthalFilter`,
   `DistribcellFilter`. Phase 1 supports `Mesh + Energy` and `Cell + Energy`.

## 6. HDF5 output schema

The score is accumulated in the standard tally results array, so it is written
by the existing `Tally::write_hdf5_data` path with no changes to file layout:

```
/tallies/tally <id>/
    filters: [mesh, energy]
    scores:  ['ifp-importance']
    results: shape (n_filter_bins, n_nuclides=1, n_scores=1, 3)
             last axis = (sum, sum_sq, n_realizations)
```

In addition, two scalar metadata attributes are written on the tally group when
this score is present:

- `ifp_n_generation` (int)
- `ifp_track_phase_space` (bool)

so postprocessors can verify the asymptotic generation depth that produced the
result.

## 7. Validation strategy

### 7.1 Internal consistency (β_eff cross-check)

For a tally with filters `[CellFilter, EnergyFilter]` plus a second tally
combining `["ifp-beta-numerator", "ifp-denominator"]` with an
`EnergyFilter` on the originator's birth energy is not directly available from
existing scores, so the consistency test is:

```
sum over (cell, E) of  ifp-importance ≈ ifp-denominator
```

That sum must agree to within 1-σ statistical uncertainty.  A test case is
added under `tests/regression_tests/ifp_importance/`.

### 7.2 Adjoint flux validation

Compare against deterministic adjoint computed by an external
discrete-ordinates code (Denovo, MPACT) for:

1. A 1-D slab homogeneous reactor (SHEM-281 group structure).
2. The Godiva HEU sphere (single material, easy mesh).
3. C5G7 (multi-region, energy-dependent).

Acceptance criterion: cosine similarity of normalized `phi†` greater than 0.99
with 5 M-history runs.

### 7.3 Statistical pathology checks

- High-variance tail: bin-by-bin Shannon entropy, FOM stabilisation across
  batches.
- Outlier chain detection: optional per-realisation logging of the maximum
  contribution per bin.

## 8. Complications and decisions deferred

| # | Question                                                                 | Default for Phase 1                              |
| - | ------------------------------------------------------------------------ | ------------------------------------------------ |
| 1 | Should the chain length for `ifp-importance` be configurable separately from `ifp_n_generation`? | No — share the existing setting.                 |
| 2 | What happens to chains shorter than N (early generations / inactive cycle ramp-up)? | Skip (matches existing behaviour).               |
| 3 | How are surface-source / fixed-source modes handled?                     | Reject at tally construction (existing IFP rule).|
| 4 | Memory footprint when N=10, 1 M particles, 3D position + energy?         | ≈ (3 × 8 + 8) × 10 × 1e6 = 320 MB per rank — flag in user guide. Phase 2 may store only filter-bin indices instead of phase-space coordinates. |
| 5 | OpenMP thread safety                                                     | Same as existing scores: per-particle indexing into source bank, score accumulation through existing thread-safe tally results path.|
| 6 | Cell filter performance (re-finding cell for every fission)              | Phase 1: accept the cost. Phase 2: cache cell index in chain. |
| 7 | Should `ifp-importance` be normalised by `k_eff` (like Λ)?              | No — leave normalisation to the user; document the convention. |
| 8 | Re-using the existing `ifp_source_delayed_group_bank` for cell index    | Rejected — keeps the two features orthogonal.    |
| 9 | Naming: `ifp-importance` vs. `ifp-progeny-weight`                        | `ifp-importance` (matches the physics term).     |
| 10 | Outlier capping (e.g. 6-σ truncation as in MCNP6 IFP)                   | Off by default; hook left for future option.     |

## 9. Phase plan

**Phase 1 (this branch).** Minimal end-to-end implementation:
- Plumbing: `SCORE_IFP_IMPORTANCE` enum, name table, Python map.
- Two new global banks gated on `ifp_track_phase_space`.
- `E_born_` field on `Particle`.
- Chain population in `ifp()` and MPI/serial transfer in `synchronize_bank`.
- A single `score_ifp_importance_tally()` function exercised from the
  collision tally path.
- Restricted to `Mesh + Energy` and `Cell + Energy` filter combinations.
- Single-score-per-tally restriction.
- Regression test against `ifp-denominator` summation.

**Phase 2 (future).**
- Filter-index caching at chain birth (memory + speed win for cell filters).
- Configurable outlier capping.
- `add_ifp_importance_tally()` Python helper, statepoint reader.
- Validation suite vs. deterministic adjoint codes.

## 10. Summary diff scope

```
include/openmc/bank.h           ~6 lines  (declarations)
include/openmc/constants.h      ~1 line   (enum)
include/openmc/particle_data.h  ~3 lines  (E_born_ + accessor)
include/openmc/settings.h       ~2 lines  (flag)
include/openmc/ifp.h            ~30 lines (parallel helpers)
src/bank.cpp                    ~8 lines  (def + clear)
src/settings.cpp                ~6 lines  (xml)
src/particle.cpp                ~1 line   (from_source)
src/physics.cpp                 0  lines  (call site reused)
src/ifp.cpp                     ~120 lines (parallel population + MPI)
src/eigenvalue.cpp              ~40 lines (synchronize_bank wiring)
src/reaction.cpp                ~1 line   (name table)
src/output.cpp                  ~1 line   (long name)
src/tallies/tally.cpp           ~30 lines (validation + activation)
src/tallies/tally_scoring.cpp   ~80 lines (score_ifp_importance_tally)
openmc/lib/tally.py             ~1 line   (Python map)
docs/source/usersguide/kinetics.rst ~20 lines
tests/regression_tests/ifp_importance/  ~150 lines (new)
```

End of design document.
