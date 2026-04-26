"""Unit tests for the MT=460 delayed fission photon sampling logic.

The full Python ENDF parser (openmc.data.reaction._get_delayed_photons_mt460)
requires a valid ENDF file to exercise. These tests instead mirror the C++
sampling algorithm in pure Python and verify the statistical properties:
  - mean number of photons per fission converges to sum(yields)
  - photon energies are sampled from `energies` weighted by `yields`
  - emission delay times follow exponential with the per-line lambda

This is the same algorithm implemented in
src/physics.cpp::sample_mt460_delayed_photons. Keep them in sync.
"""

import math

import numpy as np
import pytest


# ---------------------------------------------------------------------------
# Reference data: a small synthetic MT=460 spectrum.
# Three photon lines with different energies, decay constants, yields.
# Total expected delayed photons / fission = 0.10 + 0.05 + 0.20 = 0.35
# ---------------------------------------------------------------------------
ENERGIES_eV       = np.array([4.0e5, 1.2e6, 2.0e6])
DECAY_CONSTANTS_S = np.array([1.0e-3, 5.0e-3, 1.0e-1])
YIELDS            = np.array([0.10,   0.05,   0.20])

TOTAL_EXPECTED = float(YIELDS.sum())   # 0.35


def _sample_n_photons(rng):
    """Knuth's Poisson algorithm — mirror of the C++ inner loop."""
    L = math.exp(-TOTAL_EXPECTED)
    k = 0
    q = 1.0
    while True:
        k += 1
        q *= rng.random()
        if q <= L:
            break
        if k >= 1000:
            break
    return k - 1


def _sample_one_photon(rng):
    """Single (line, time) sample mirroring the C++ inverse-CDF loop."""
    xi = rng.random() * TOTAL_EXPECTED
    cumul = 0.0
    sel = len(YIELDS) - 1
    for l, y in enumerate(YIELDS):
        cumul += y
        if xi <= cumul:
            sel = l
            break
    t_delay = -math.log(rng.random()) / DECAY_CONSTANTS_S[sel]
    return ENERGIES_eV[sel], t_delay, sel


# ---------------------------------------------------------------------------
# Test 1: Mean photon multiplicity converges to sum(yields).
# ---------------------------------------------------------------------------
def test_mean_multiplicity():
    rng = np.random.default_rng(seed=0xC461)
    n_fiss = 100_000
    counts = [_sample_n_photons(rng) for _ in range(n_fiss)]
    mean = np.mean(counts)
    # sigma/mean for Poisson ≈ 1/sqrt(N*mu) → tolerance 5%
    rel_err = abs(mean - TOTAL_EXPECTED) / TOTAL_EXPECTED
    assert rel_err < 0.05, (
        f'mean photon multiplicity {mean:.5f} '
        f'expected {TOTAL_EXPECTED:.5f}  (rel err {rel_err:.3f})'
    )


# ---------------------------------------------------------------------------
# Test 2: Per-line emission probability matches yields[l] / sum(yields).
# ---------------------------------------------------------------------------
def test_line_selection_distribution():
    rng = np.random.default_rng(seed=0xC462)
    n = 200_000
    line_counts = np.zeros(len(YIELDS), dtype=int)
    for _ in range(n):
        _, _, sel = _sample_one_photon(rng)
        line_counts[sel] += 1
    expected = YIELDS / TOTAL_EXPECTED
    observed = line_counts / n
    for l in range(len(YIELDS)):
        rel_err = abs(observed[l] - expected[l]) / expected[l]
        assert rel_err < 0.02, (
            f'line {l}: observed prob {observed[l]:.4f} '
            f'expected {expected[l]:.4f}  (rel err {rel_err:.3f})'
        )


# ---------------------------------------------------------------------------
# Test 3: Conditional emission-time distribution per line is exponential
# with the line's decay constant.
# ---------------------------------------------------------------------------
@pytest.mark.parametrize('line_idx', [0, 1, 2])
def test_emission_time_per_line(line_idx):
    rng = np.random.default_rng(seed=0xC463 + line_idx)
    times = []
    while len(times) < 100_000:
        _, t, sel = _sample_one_photon(rng)
        if sel == line_idx:
            times.append(t)
    mean_t   = np.mean(times)
    expected = 1.0 / DECAY_CONSTANTS_S[line_idx]
    rel_err = abs(mean_t - expected) / expected
    assert rel_err < 0.02, (
        f'line {line_idx}: <t>={mean_t:.4e} s  '
        f'expected 1/lambda={expected:.4e} s  (rel err {rel_err:.3f})'
    )


# ---------------------------------------------------------------------------
# Test 4: Energy sample mean matches the yield-weighted average.
# ---------------------------------------------------------------------------
def test_mean_photon_energy():
    rng = np.random.default_rng(seed=0xC464)
    n = 200_000
    energies = []
    for _ in range(n):
        E, _, _ = _sample_one_photon(rng)
        energies.append(E)
    mean_E   = np.mean(energies)
    expected = float((YIELDS * ENERGIES_eV).sum() / TOTAL_EXPECTED)
    rel_err  = abs(mean_E - expected) / expected
    assert rel_err < 0.01, (
        f'<E>={mean_E:.4e} eV  expected {expected:.4e} eV '
        f'(rel err {rel_err:.4f})'
    )
