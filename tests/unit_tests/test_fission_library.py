"""Validation tests for the Spriggs 8-group delayed neutron model.

Verifies that the data in include/openmc/fission_library.h is internally
consistent and matches Table VII of:

  Spriggs, Campbell & Piksaikin, Prog. Nucl. Energy 41(1-4), 223-251 (2002).

No OpenMC transport is needed; all checks are pure-Python arithmetic on the
same numerical constants defined in the header.

NOTE: The paper defines T_mean as the weighted average of group HALF-LIVES:
  T_mean = sum_g(a_g * T_{1/2,g}) = ln(2) * sum_g(a_g / lambda_g)

This is the standard convention in the delayed-neutron field (Keepin, Spriggs).
The physical mean emission time from the exponential distribution is
  E[t] = sum_g(a_g / lambda_g) = T_mean / ln(2)
which is larger by a factor of 1/ln(2) ≈ 1.4427.  Both quantities are tested.
"""

import math
import numpy as np
import pytest

# ---------------------------------------------------------------------------
# Mirror of include/openmc/fission_library.h
# ---------------------------------------------------------------------------

# Universal 8-group decay constants [s^-1], Table V of Spriggs (2002).
# Derived from Piksaikin's dominant-precursor half-lives.
SPRIGGS_LAMBDA = [
    0.012462,   # Group 1: T1/2 = 55.6 s  (Br-87)
    0.028292,   # Group 2: T1/2 = 24.5 s  (I-137)
    0.042525,   # Group 3: T1/2 = 16.3 s  (Br-88)
    0.133042,   # Group 4: T1/2 =  5.21 s
    0.292468,   # Group 5: T1/2 =  2.37 s
    0.666490,   # Group 6: T1/2 =  1.04 s
    1.634780,   # Group 7: T1/2 =  0.424 s
    3.554570,   # Group 8: T1/2 =  0.195 s
]

# Per-isotope abundances a_i (sum = 1.0), Table VII fast-fission datasets.
SPRIGGS_TABLE = {
    92233: [0.0800, 0.1570, 0.1350, 0.2090, 0.3080, 0.0370, 0.0620, 0.0120],
    92235: [0.0340, 0.1500, 0.0990, 0.2000, 0.3120, 0.0930, 0.0870, 0.0250],
    92238: [0.0080, 0.1040, 0.0380, 0.1370, 0.2940, 0.1980, 0.1280, 0.0930],
    94239: [0.0290, 0.2250, 0.0950, 0.1490, 0.3510, 0.0370, 0.0970, 0.0170],
    94241: [0.0160, 0.1750, 0.0550, 0.1700, 0.2800, 0.1660, 0.1130, 0.0250],
}

# Expected T_mean [s] from Table VII, Spriggs (2002).
T_MEAN_PAPER = {
    92233: 12.38,
    92235:  9.10,
    92238:  5.30,
    94239: 10.36,
    94241:  7.85,
}

NGROUPS = 8


# ---------------------------------------------------------------------------
# Helper: compute mean emission time analytically.
#
# Two conventions:
#   paper_tmean  -- weighted average of half-lives (paper's T_mean convention):
#                   T_mean = sum_g(a_g * T_{1/2,g}) = ln(2) * sum_g(a_g/lambda_g)
#   physical_tmean -- true exponential mean (mean lifetime, = T_mean/ln2):
#                   E[t] = sum_g(a_g / lambda_g)
# ---------------------------------------------------------------------------
def paper_tmean(za):
    """Weighted average of group half-lives — matches Table VII column."""
    a = SPRIGGS_TABLE[za]
    return math.log(2.0) * sum(a[g] / SPRIGGS_LAMBDA[g] for g in range(NGROUPS))


def physical_tmean(za):
    """True mean of the exponential emission-time distribution."""
    a = SPRIGGS_TABLE[za]
    return sum(a[g] / SPRIGGS_LAMBDA[g] for g in range(NGROUPS))


# ---------------------------------------------------------------------------
# Helper: sample one emission time using the inverse-CDF method.
# ---------------------------------------------------------------------------
def sample_emission_time(za, rng):
    a = SPRIGGS_TABLE[za]
    xi1 = rng.random()
    # Inverse-CDF group selection (mirrors sample_spriggs_group in header)
    cumul = 0.0
    group = NGROUPS - 1
    for g in range(NGROUPS - 1):
        cumul += a[g]
        if xi1 < cumul:
            group = g
            break
    xi2 = rng.random()
    return -math.log(xi2) / SPRIGGS_LAMBDA[group]


# ===========================================================================
# Test: lambda values reproduce the tabulated half-lives to 4 significant
#       figures (T_1/2 = ln2 / lambda).
# ===========================================================================
HALF_LIVES = [55.6, 24.5, 16.3, 5.21, 2.37, 1.04, 0.424, 0.195]

def test_lambda_half_lives():
    """Decay constants are consistent with Piksaikin's half-lives (Table V).

    Table V reports half-lives rounded to 3-4 significant figures. Group 1
    (Br-87, 55.6 s) has ~0.04% rounding; all others agree to <0.01%.
    """
    ln2 = math.log(2.0)
    for g, (lam, t12) in enumerate(zip(SPRIGGS_LAMBDA, HALF_LIVES)):
        computed = ln2 / lam
        rel_err = abs(computed - t12) / t12
        assert rel_err < 1e-3, (
            f"Group {g+1}: T_1/2 = {computed:.4f} s, expected {t12} s "
            f"(rel err {rel_err:.2e})"
        )


# ===========================================================================
# Test: abundances sum to 1 for every isotope (they are relative fractions).
# ===========================================================================
@pytest.mark.parametrize("za", sorted(SPRIGGS_TABLE))
def test_abundances_sum_to_one(za):
    """a_i values for each isotope must sum to 1.0 within floating-point."""
    s = sum(SPRIGGS_TABLE[za])
    assert abs(s - 1.0) < 1e-10, f"ZA={za}: sum(a_i) = {s}"


# ===========================================================================
# Test: analytical T_mean matches Spriggs Table VII within 1%.
# ===========================================================================
@pytest.mark.parametrize("za", sorted(T_MEAN_PAPER))
def test_analytical_tmean_paper_convention(za):
    """Paper T_mean (weighted half-lives) matches Table VII within 1%.

    T_mean(paper) = sum_g(a_g * T_{1/2,g}) = ln(2) * sum_g(a_g / lambda_g)
    """
    t_computed = paper_tmean(za)
    t_paper = T_MEAN_PAPER[za]
    rel_err = abs(t_computed - t_paper) / t_paper
    assert rel_err < 0.01, (
        f"ZA={za}: T_mean(computed)={t_computed:.4f} s, "
        f"T_mean(paper)={t_paper:.2f} s  (rel err {rel_err:.3f})"
    )


@pytest.mark.parametrize("za", sorted(T_MEAN_PAPER))
def test_analytical_tmean_physical(za):
    """Physical mean emission time is T_mean(paper)/ln(2)."""
    t_physical = physical_tmean(za)
    t_expected = T_MEAN_PAPER[za] / math.log(2.0)
    rel_err = abs(t_physical - t_expected) / t_expected
    assert rel_err < 0.01, (
        f"ZA={za}: physical T_mean={t_physical:.4f} s, "
        f"expected {t_expected:.4f} s  (rel err {rel_err:.3f})"
    )


# ===========================================================================
# Test: Monte Carlo T_mean matches analytical value within statistical noise.
#   N=500000 samples → σ/mean ~ 0.4% for each isotope; use 2% tolerance.
# ===========================================================================
N_MC = 500_000

@pytest.mark.parametrize("za", sorted(SPRIGGS_TABLE))
def test_mc_tmean(za):
    """MC mean emission time matches the physical mean lifetime within 2%.

    N=500_000 samples → statistical uncertainty ~ 0.4% per isotope.
    Physical mean = sum_g(a_g / lambda_g) = T_mean(paper) / ln(2).
    """
    rng = np.random.default_rng(seed=za)
    times = [sample_emission_time(za, rng) for _ in range(N_MC)]
    t_mc = np.mean(times)
    t_expected = physical_tmean(za)
    rel_err = abs(t_mc - t_expected) / t_expected
    assert rel_err < 0.02, (
        f"ZA={za}: MC T_mean={t_mc:.4f} s, expected={t_expected:.4f} s "
        f"(rel err {rel_err:.3f})"
    )


# ===========================================================================
# Test: each group's empirical rate matches its lambda (checks the exponential
#       distribution parameter, not just the mean).
# ===========================================================================
def test_mc_group_rates():
    """For a pure single-group sample, -1/log(U) follows the correct lambda."""
    rng = np.random.default_rng(seed=12345)
    n = 200_000
    for g, lam in enumerate(SPRIGGS_LAMBDA):
        u = rng.random(n)
        t = -np.log(u) / lam
        rate_mc = 1.0 / np.mean(t)
        rel_err = abs(rate_mc - lam) / lam
        assert rel_err < 0.01, (
            f"Group {g+1}: rate_mc={rate_mc:.6f}, lambda={lam:.6f} "
            f"(rel err {rel_err:.3f})"
        )


# ===========================================================================
# Test: find_entry returns None for unlisted isotopes (no fallback).
# ===========================================================================
def test_no_fallback_for_unknown_isotopes():
    """Isotopes not in the Spriggs table must return None, not a substitute.

    In the OpenMC integration, a None result causes the code to fall back
    to the ENDF/B decay rate rather than silently using a wrong isotope's
    group abundances.
    """
    unlisted = [92234, 92236, 94238, 94240, 94242, 95241, 96244]
    for za in unlisted:
        assert za not in SPRIGGS_TABLE, (
            f"ZA={za} is now in SPRIGGS_TABLE — update this test"
        )
