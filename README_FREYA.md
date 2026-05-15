# FREYA in OpenMC — Integration Notes

**Audience:** Tony Nelson (LLNL), and anyone else from the Fission Library
team looking at how FREYA is wired into a host transport code.

**Status:** Experimental fork of [openmc-dev/openmc](https://github.com/openmc-dev/openmc).
Not upstreamed. Branch of record: `freya-fork-seed`.

**Maintainer (fork):** William Zywiec — `willzywiec@gmail.com`

---

## Why this fork exists

OpenMC's stock fission model samples prompt neutrons one at a time from
ENDF/B `χ(E)` with an ENDF/B `ν̄(E)` mean and treats the within-event
joint distribution as independent. That's fine for `k_eff`, but it
washes out the n–n correlations needed for:

- Multiplicity counting / NDA / safeguards
- Rossi-α and Feynman-Y coincidence analyses
- Prompt-α eigenvalue work that depends on FREYA-quality `ν` variance
- List-mode detector simulations

This fork drops FREYA in as the prompt-fission event generator so OpenMC
can be used for those problems without leaving the OpenMC ecosystem
(Python API, depletion, statepoints, tallies).

The fork also picks up the rest of the LLNL Fission Library while we're
in there: GEF SF/induced-fission energy spectra, the Spriggs 8-group
delayed-neutron timing model, and an MT=460 delayed-photon path.

---

## How FREYA is vendored

```
vendor/fission/                  ← unmodified LLNL Fission Library drop
    src/                         ← Fission.cc, SmpFreya.cc, SmpDelayed.cc, …
    data_freya/                  ← FREYA data tables (*.TKE-Af, *.Y-Af, …)
    include/                     ← Fission.h, Fission.hh
    COPYRIGHT_FREYA.TXT
    …
```

We pull the library source in as-shipped — no patches to the FREYA core.
The OpenMC build vendors it as a CMake subproject and links against
`FissionLib::Fission`. The data tables ship next to the source; the
default search path is baked in at configure time, with runtime override
through `$FREYA_DATA_PATH`.

The intent is that bumping FREYA versions is `git rm -rf vendor/fission`
+ drop in the new tarball + rebuild. Nothing in the OpenMC tree should
need to know about FREYA's internals.

---

## Build switch

Everything FREYA-related is gated by a single CMake option:

```bash
cmake -DOPENMC_USE_FISSION_LIB=ON ..
make -j
```

Or via the fork's setup script:

```bash
./setup.sh --with-fission-lib
```

With the flag **off**, OpenMC builds and runs exactly as upstream
(stock ENDF prompt sampling, 6-group Keepin delays, Watt/Maxwellian SF).
The FREYA-specific Python settings raise `OpenMCError` so users can't
silently get a non-FREYA result when they asked for FREYA. With the flag
**on**, every code path described below activates.

The flag name has churned (`OPENMC_USE_FREYA` → `OPENMC_USE_FRIGGA` →
`OPENMC_USE_FISSION_LIB`) — the current name reflects that the build
also brings in GEF and Spriggs, not just FREYA.

---

## The OpenMC ↔ FREYA seam

There's one C++ file that owns the FREYA boundary:

- `include/openmc/freya_interface.h`
- `src/freya_interface.cpp`

Everything else in OpenMC calls through this header. It exposes three
functions in `openmc::freya`:

| Function           | Role |
|--------------------|------|
| `init(data_path)`  | One-shot FREYA init, `std::call_once`. Resolves data dir from arg → `$FREYA_DATA_PATH` → compile-time default. |
| `set_seed(uint64_t*)` | Points FREYA's RNG callback at the current OpenMC particle's LCG seed, so FREYA samples advance the same RNG stream OpenMC is using. |
| `is_initialized()` | Diagnostic. |

The header includes a comment that's worth restating: **FREYA is not
thread-safe.** The global `fissionEvent` pointer plus the
generate-then-retrieve API means every FREYA call has to happen under a
lock. We use `#pragma omp critical(freya_event)` around the
`set_seed → genfissevtdir_ → retrieve` sequence in
`src/physics.cpp:301`. If FREYA ever grows a per-thread event object,
the critical section drops away cleanly.

The RNG callback hookup is the most OpenMC-specific bit. FREYA expects a
function pointer that returns a `double` in `[0,1)`; we register one
that pulls from OpenMC's own LCG using the seed pointer stashed by
`set_seed`. This is what makes FREYA samples deterministic w.r.t.
OpenMC's master seed, and what makes parallel runs reproducible at fixed
thread count.

---

## Where FREYA is called from in OpenMC

Three call sites, all gated by `#ifdef OPENMC_USE_FISSION_LIB`:

1. **`src/physics.cpp`** — induced-fission prompt-neutron sampling.
   Default path keeps one of FREYA's `n_n` neutrons per fission-bank
   slot (population control preserved). Analog path
   (`settings.freya_analog = True`) calls FREYA once per fission event
   and banks all `n_n` correlated neutrons with reweighted statistical
   weights so total banked weight per fission matches ENDF `ν̄`.
   Within-event correlations are what's preserved.

2. **`src/source.cpp`** — `FreyaSFSource`, the correlated SF source.
   Pre-bakes `n_events` calls to `genspfissevt_` at problem
   initialization, caches the resulting prompt particles tagged with a
   FREYA event index, and serves them as a fixed source. The event
   index is carried on `parent_id` so post-hoc coincidence grouping is
   trivial in user analysis code.

3. **Prompt-photon path** — when `settings.photon_transport = True`,
   FREYA prompt γ's are banked alongside the prompt neutrons from both
   call sites above.

That's the entire C++ surface. There's no FREYA call from any hot inner
loop other than the per-fission boundary; the lock granularity matches
the per-event cost.

---

## Where Spriggs and GEF live

Sibling modules to FREYA, all in the same vendored library:

- **Spriggs 8-group delayed neutrons** — `SmpDelayed.cc`. Replaces
  OpenMC's 6-group Keepin half-lives in the delayed-neutron sampling
  path. FREYA's own delay flag is set to 0; we drive delayed timing
  ourselves so the prompt and delayed sides stay decoupled. For isotopes
  outside the Spriggs table (²³³⁻²³⁵⁻²³⁸U, ²³⁹⁻²⁴¹Pu) we fall back to
  the ENDF/B 6-group decay rates.

- **GEF spectra** — `SmpFreya.cc` / `SmpGEng.cc`. GEF tabulated
  energy spectra replace Watt/Maxwellian fallbacks for both SF and
  induced fission, applied per-isotope.

These are quieter integrations than FREYA itself — they're spectrum
swaps, not event-correlation changes — but they live behind the same
build flag because the data ships together.

---

## Python-side surface

Everything FREYA-specific that a user touches:

```python
import openmc

# Analog (correlated) induced-fission mode
settings = openmc.Settings()
settings.freya_analog = True

# Correlated spontaneous-fission source
src = openmc.FreyaSFSource(
    za=98252,                  # Cf-252
    position=(0.0, 0.0, 0.0),
    n_events=50_000,
    include_photons=True,
    strength=2.31e6,           # n/s for 1 g of Cf-252
)
settings.source = src

# (α,n) source helper (uses ALPHANSO; orthogonal to FREYA but in the
# same fork because it's the other half of a passive-source workflow)
settings.source = openmc.model.alphanso_source(...)

# Static α / IFP-weighted ℓ_p, β_eff
settings.calculate_alpha = True
```

These all serialize to XML and round-trip. The Python API enforces that
calling them without `-DOPENMC_USE_FISSION_LIB=ON` will fatal-error
inside the C++ side at problem init.

Supported SF isotopes (gated by what's in `data_freya/*sf*`):
²³⁸U, ²³⁸Pu, ²⁴⁰Pu, ²⁴²Pu, ²⁴⁴Cm, ²⁵²Cf. Anything outside this set uses
FREYA's uncorrelated fallback per FREYA User Manual v2.0.2 §A.1.7.

---

## What we picked from the FREYA API

The functions we actually call:

| FREYA symbol            | OpenMC use |
|-------------------------|------------|
| `genfissevtdir_`        | Induced fission, neutrons + photons + directional sampling |
| `genspfissevt_`         | SF source pre-bake |
| `getnumberneutrons_`    | `n_n` per event |
| `getnumberphotons_`     | `n_γ` per event |
| `getneutron_`, `getphoton_` | Retrieve banked particles |
| Spriggs delayed-timing entry points | Through `SmpDelayed.cc` |

We do **not** currently surface `getfission_fragment_()` — fragment
recoil tracking isn't wired up. That's the obvious next addition if a
shielding application asks for it.

---

## Validation status

- **Rossi-α benchmark suite**: 21 delayed-critical + 33 subcritical
  configs (²³³U, HEU, IEU, LEU, plutonium fuels). Agreement is 1–5 % for
  thermal solution systems, 5–10 % for fast metal systems. Writeup:
  Zywiec, *"Rossi-α Benchmark Validation of a Static Alpha Eigenvalue
  Capability in OpenMC"* (2026), included in `docs/`.

- **Regression coverage** (`tests/unit_tests/`):
  - `test_freya_analog.py` — analog-mode prompt-fission sampling
  - `test_freya_sf_source.py` — SF source pre-bake / banking
  - `test_freya_validation.py` — runtime smoke tests, skipped when the
    build flag or `OPENMC_CROSS_SECTIONS` are absent
  - `test_alpha_eigenvalue.py` — α / α_dc / Λ_p formula consistency

- **End-to-end demo**: `examples/godiva_full_pipeline.py` exercises
  every Phase-1–8 capability on bare HEU.

---

## Known approximations

These are the ones we'd want you to be aware of, in case any of them are
wrong by your reading of the library:

1. **FREYA `ν` distribution drives within-event statistics, ENDF `ν̄`
   drives total banked weight.** In analog mode we rescale FREYA's
   sampled `n_n` so the mean banked weight per collision matches ENDF.
   Distribution shape comes from FREYA; first moment comes from ENDF.

2. **Delayed neutrons come from Spriggs, not FREYA.** We set FREYA's
   delay flag to 0. This is deliberate — we wanted the Spriggs 8-group
   model with universal decay constants — but it's worth flagging
   because FREYA *can* produce delays itself.

3. **MT=460 delayed-photon yields collapsed to thermal.** Thermal-energy
   yields applied isotope-uniformly across incident energies. Fine for
   thermal/epithermal, known approximation for fast.

4. **`FreyaSFSource` is pre-baked, not on-demand.** All FREYA SF calls
   happen at problem init; the source sampler then draws from the
   cache. Users have to size `n_events` to exceed the per-generation
   particle count.

5. **No fission-fragment transport** (see above).

If any of these conflict with how the Fission Library is supposed to be
driven, we'd love to know.

---

## Repo layout pointers

| Path | What's there |
|------|--------------|
| `vendor/fission/` | Unmodified LLNL Fission Library |
| `include/openmc/freya_interface.h` | C++ seam declaration |
| `src/freya_interface.cpp` | C++ seam implementation, RNG callback |
| `src/physics.cpp` | Induced-fission call site (analog + default) |
| `src/source.cpp` | `FreyaSFSource` C++ side |
| `openmc/source.py` | `FreyaSFSource` Python class |
| `openmc/settings.py` | `freya_analog`, `calculate_alpha` settings |
| `openmc/model/alphanso_source.py` | (α,n) source helper |
| `docs/source/usersguide/fission_library.rst` | User-facing doc page |
| `examples/godiva_full_pipeline.py` | End-to-end demo |
| `tests/unit_tests/test_freya_*.py` | FREYA-specific tests |
| `setup.sh` | `--with-fission-lib` build shortcut |

The git log on the `freya-fork-seed` branch reads as Phase 1 through
Phase 8 commits, each scoped to one capability (delayed neutrons,
FREYA prompt fission, prompt photons + ALPHANSO, MT=460 photons,
analog mode, `FreyaSFSource`, validation tests, docs).

---

## Questions for LLNL / Tony

The bits we'd most like a second opinion on:

1. **Is the OMP-critical wrapping the right granularity?** Per-event
   feels coarse enough that the lock overhead is negligible compared
   to a FREYA event cost, but we haven't profiled at scale.

2. **Is delegating delayed timing to Spriggs (FREYA delay flag = 0) the
   intended use?** Or are we leaving FREYA capability on the table?

3. **Pre-baking `genspfissevt_` calls at init vs. calling on-demand
   from the source sampler** — any reason to prefer one over the
   other? On-demand would require pushing the FREYA critical section
   into the source-sampling hot path, which is why we picked pre-bake.

4. **Fission-fragment recoil** — is `getfission_fragment_()` something
   you'd expect a host code to use, or is it more of a diagnostic?

Happy to walk through any of this on a call.

---

*Generated from the `freya-fork-seed` branch state. If something in the
description doesn't match the source, the source wins — let us know.*
