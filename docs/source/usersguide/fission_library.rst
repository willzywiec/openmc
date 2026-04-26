.. _fission_library:

================================
Correlated Fission (FREYA / GEF)
================================

This fork ships an integration of the LLNL Fission Library — including
the FREYA event generator, GEF spontaneous-fission spectra, and a
Spriggs 8-group delayed-neutron model — for problems where event-by-event
correlations matter (multiplicity counting, NDA/safeguards, Rossi-α and
related coincidence analyses, prompt-α eigenvalue calculations).

The integration is gated at build time by ``OPENMC_USE_FISSION_LIB``.
Without that flag set, OpenMC falls back to its standard ENDF-driven
fission sampling and the FREYA-specific Python settings raise an error
when used.

.. contents:: :local:
   :depth: 2


Build configuration
-------------------

Configure with the option enabled:

.. code-block:: bash

    cmake -DOPENMC_USE_FISSION_LIB=ON ..
    make -j

The FREYA data tables ship with the vendored fission library at
``vendor/fission/data_freya/``. The compiled-in path is set by CMake;
runtime override via ``$FREYA_DATA_PATH``.

Verify a build is FREYA-aware by setting any FREYA-specific Python
setting and running an XML export — the C++ side fatal-errors if the
flag wasn't compiled in.


What's enabled when you build with the flag
-------------------------------------------

==========================================  ========================================================
Capability                                  How to use it
==========================================  ========================================================
Correlated prompt fission (FREYA)           Always on. Replaces ENDF prompt-energy sampling.
Correlated prompt photons (FREYA)           Always on when ``settings.photon_transport = True``.
ENDF MT=460 delayed fission photons         Always on when ``settings.photon_transport = True``.
Spriggs 8-group delayed neutron emission    Always on (replaces 6-group Keepin half-lives).
GEF tabulated SF / induced-fission spectra  Always on (replaces Watt/Maxwellian fallbacks).
ALPHANSO (α,n) source helper                ``openmc.model.alphanso_source(...)`` (Python only)
Full-analog FREYA mode (Phase 4)            ``settings.freya_analog = True``
FREYA-correlated SF source (Phase 5)        ``openmc.FreyaSFSource(...)``
α eigenvalue + IFP-weighted ℓ_p, β_eff      ``settings.calculate_alpha = True``
==========================================  ========================================================


Full-analog FREYA mode
----------------------

In the default integration, FREYA is invoked once per fission-bank slot
and only the *first* of FREYA's :math:`n_n` correlated prompt neutrons
is kept. This preserves OpenMC's population control but discards within-
event correlations.

Set ``settings.freya_analog = True`` to invoke FREYA *once per fission
event* and bank all :math:`n_n` correlated prompt neutrons together,
each with weight :math:`(n_p / n_n) / w` where :math:`n_p` is the
sampled prompt count from ENDF and :math:`w` is the UFS weight. Total
banked weight per fission is unchanged from the default path — only
within-event correlations differ.

.. code-block:: python

    settings = openmc.Settings()
    settings.freya_analog = True
    # ... rest of settings

Use this for n-n correlation problems (multiplicity counting, list-mode
detector simulations) where the joint distribution of neutron energies
and angles within a single fission matters.


FREYA-correlated spontaneous fission source
-------------------------------------------

For fixed-source problems with passive SF emitters (Cf-252 calibration
sources, Pu-bearing material), use :class:`openmc.FreyaSFSource` instead
of an independent Watt spectrum. Each cached site retains its FREYA
event index in ``parent_id`` so within-event correlations are
recoverable post-hoc by grouping detector hits by parent.

.. code-block:: python

    src = openmc.FreyaSFSource(
        za=98252,                  # Cf-252
        position=(0.0, 0.0, 0.0),
        n_events=50000,            # pre-bake count; raise for production
        include_photons=True,      # bank prompt gammas as well
        strength=2.31e6,           # n/s for 1 g of Cf-252
    )
    settings.source = src

Choose ``n_events`` such that the total cached particle count
(:math:`\approx \langle n_n \rangle \cdot n_\mathrm{events}`) exceeds
``settings.particles`` per generation, otherwise particles will be
resampled from the cache and source-bank correlations will be biased.

The ``strength`` parameter is the absolute physical emission rate (e.g.
:math:`\lambda_\mathrm{SF} \cdot N_\mathrm{atoms} \cdot \langle\nu\rangle`
for a passive source). It is not auto-derived from material — you compute
it from the SF half-life, isotopic mass, and FREYA's tabulated mean
multiplicity for the requested isotope.

Supported SF isotopes (from FREYA's ``data_freya/*sf*`` tables):

- 252-Cf, 244-Cm, 238-Pu, 240-Pu, 242-Pu

For other SF emitters, FREYA reverts to its uncorrelated fallback
(see FREYA User Manual v2.0.2 §A.1.7); ``FreyaSFSource`` will fatal-error
if no neutrons are produced after the requested ``n_events`` events.


α eigenvalue calculations
-------------------------

Set ``settings.calculate_alpha = True``. This automatically enables
``calculate_prompt_k`` and the IFP method with sensible defaults. The
statepoint then carries:

- ``alpha_dc_ifp``: delayed-critical α eigenvalue
  (:math:`-\beta_\mathrm{eff} / \ell_p`)
- ``alpha_ifp``: static α at the simulated reactivity
  (:math:`(k_p - 1) / \ell_p`)
- ``lifetime_p_ifp``: IFP-weighted prompt neutron lifetime :math:`\ell_p`
- ``lambda_p_ifp``: IFP-weighted prompt generation time
  :math:`\Lambda_p = \ell_p / k_p` (reported only; not used in α)

See :ref:`methods_alpha_eigenvalue` for the full derivation, and
``Static_Alpha_OpenMC_Zywiec.tex`` at the repo root for the validation
study (21 delayed-critical + 33 subcritical benchmarks).


Approximations and known limitations
------------------------------------

**Delayed neutrons via Spriggs 8-group, not FREYA.** The integration sets
FREYA's delay flag to 0 and uses Spriggs Table-VII abundances + universal
8-group decay constants for delayed-neutron emission times. For isotopes
not in the Spriggs table (anything outside :math:`^{233,235,238}`\ U,
:math:`^{239,241}`\ Pu) the ENDF/B 6-group decay rate is used as a fallback.

**MT=460 delayed photon yields collapsed to thermal.** The ENDF MT=460
delayed-photon-emission tables in the integration use thermal-energy
yields, applied isotope-uniformly across incident energies. This is fine
for thermal/epithermal systems and a known approximation for fast spectra.

**FREYA's :math:`\nu` distribution drives within-event statistics.** OpenMC's
ENDF :math:`\bar\nu` still governs the *mean* fission-bank size per
collision; analog mode rescales FREYA's :math:`n_n` so total banked
weight matches ENDF. The multiplicity *distribution* you observe in
multiplicity-counting tallies comes from FREYA, not ENDF.

**Pre-baked SF source bank.** ``FreyaSFSource`` pre-generates events at
construction. There is no on-demand FREYA call from the per-particle
source sampler. Set ``n_events`` appropriately for your particle count.

**No fission-fragment recoil tracking.** ``getfission_fragment_()`` is
not currently surfaced. For shielding work that needs explicit fragment
transport, this would be a separate addition.


Validating against benchmarks
-----------------------------

The vendored paper ``Static_Alpha_OpenMC_Zywiec.tex`` is the canonical
validation against Rossi-α measurements (21 delayed-critical + 33
subcritical configurations spanning :math:`^{233}`\ U, HEU, IEU, LEU,
and plutonium fuels). Agreement is 1–5 % for thermal solution systems,
5–10 % for fast metal systems.

Repository-side regression coverage:

- ``tests/unit_tests/test_alpha_eigenvalue.py`` — pin-test for the
  α/α_dc/Λ_p formula relationships on a small U-235 sphere.
- ``tests/unit_tests/test_freya_validation.py`` — runtime smoke tests
  for analog FREYA mode and ``FreyaSFSource``. Skipped when
  ``OPENMC_USE_FISSION_LIB`` and ``OPENMC_CROSS_SECTIONS`` env vars are
  not set.

For new validation cases, add tests under ``tests/unit_tests/`` rather
than ``tests/regression_tests/`` until the result-diffing harness is
extended to handle FREYA's stochastic outputs.
