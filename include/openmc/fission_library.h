// SPDX-FileCopyrightText: 2024 Lawrence Livermore National Security, LLC
// SPDX-License-Identifier: MIT
//
// Spriggs 8-group consistent delayed neutron parameters for OpenMC integration.
//
// Reference:
//   G.D. Spriggs, J.M. Campbell, V.M. Piksaikin,
//   "An 8-group delayed neutron model based on a consistent set of half-lives",
//   Progress in Nuclear Energy 41(1-4), 223-251 (2002).
//
// Enabled by: cmake -DOPENMC_USE_FREYA=ON
//
// When OPENMC_USE_FREYA is defined, the delayed neutron emission time in
// sample_fission_neutron() (src/physics.cpp) is sampled from the Spriggs
// 8-group model rather than from the ENDF/B precursor decay constants.
// The group structure (for energy/angle sampling) and beta fraction still
// come from the ENDF/B evaluation; only the emission time is changed.
//
// KEY INSIGHT: The 6-group Keepin model fits both lambda_i AND a_i
// simultaneously, making lambda_i non-unique (different experiments converge
// to different values for the same isotope). The Spriggs model fixes lambda
// to dominant precursor half-lives (Br-87, I-137, Br-88, ...) and fits
// only the per-isotope abundances a_i. This yields consistent, physically
// grounded decay constants across all isotopes and measurement campaigns.

#pragma once

#ifdef OPENMC_USE_FREYA

namespace openmc {
namespace fission_lib {

// ---------------------------------------------------------------------------
// Universal 8-group decay constants  [s^-1]
//
// Derived from dominant precursor half-lives; identical for all isotopes.
// Source: Spriggs et al. (2002) Table V, Piksaikin's half-lives.
//
//   Group | T_1/2 (s) | lambda (s^-1) | Dominant precursor
//   ------|-----------|---------------|--------------------
//     1   |  55.600   |  0.012462     | Br-87
//     2   |  24.500   |  0.028292     | I-137
//     3   |  16.300   |  0.042525     | Br-88
//     4   |   5.210   |  0.133042     |
//     5   |   2.370   |  0.292468     |
//     6   |   1.040   |  0.666490     |
//     7   |   0.424   |  1.634780     |
//     8   |   0.195   |  3.554570     |
// ---------------------------------------------------------------------------
constexpr int NSPRIGGS = 8;

inline constexpr double spriggs_lambda[NSPRIGGS] = {
  0.012462,  // Group 1: T1/2 = 55.6 s  (Br-87)
  0.028292,  // Group 2: T1/2 = 24.5 s  (I-137)
  0.042525,  // Group 3: T1/2 = 16.3 s  (Br-88)
  0.133042,  // Group 4: T1/2 =  5.21 s
  0.292468,  // Group 5: T1/2 =  2.37 s
  0.666490,  // Group 6: T1/2 =  1.04 s
  1.634780,  // Group 7: T1/2 =  0.424 s
  3.554570   // Group 8: T1/2 =  0.195 s
};

// ---------------------------------------------------------------------------
// Per-isotope relative group abundances a_i, normalised so sum(a_i) = 1.
//
// Source: Table VII fast-fission recommended datasets, Spriggs et al. (2002).
// Dataset numbers from Spriggs & Campbell (1999) compilation, LA-UR-98-918.
//
//   ZA    | Source                  | T_mean
//   -------|------------------------|--------
//   92233  | #42 Maksyutenko (1967) | 12.38 s
//   92235  | #88 Piksaikin (1997)   |  9.10 s
//   92238  | #118 Keepin (1957)     |  5.30 s
//   94239  | #207 Besant (1977)     | 10.36 s
//   94241  | #230 Gudkov (1989)     |  7.85 s
// ---------------------------------------------------------------------------
struct SpriggsEntry {
  int ZA;
  double a[NSPRIGGS];
};

inline constexpr SpriggsEntry spriggs_table[] = {
  { 92233, {0.0800, 0.1570, 0.1350, 0.2090, 0.3080, 0.0370, 0.0620, 0.0120} },
  { 92235, {0.0340, 0.1500, 0.0990, 0.2000, 0.3120, 0.0930, 0.0870, 0.0250} },
  { 92238, {0.0080, 0.1040, 0.0380, 0.1370, 0.2940, 0.1980, 0.1280, 0.0930} },
  { 94239, {0.0290, 0.2250, 0.0950, 0.1490, 0.3510, 0.0370, 0.0970, 0.0170} },
  { 94241, {0.0160, 0.1750, 0.0550, 0.1700, 0.2800, 0.1660, 0.1130, 0.0250} },
};

constexpr int N_SPRIGGS_ENTRIES =
  static_cast<int>(sizeof(spriggs_table) / sizeof(spriggs_table[0]));

// ---------------------------------------------------------------------------
// find_entry: look up the SpriggsEntry for a given ZA (1000*Z + A).
// Returns nullptr if the isotope is not tabulated.
// ---------------------------------------------------------------------------
inline const SpriggsEntry* find_entry(int ZA)
{
  for (int i = 0; i < N_SPRIGGS_ENTRIES; ++i) {
    if (spriggs_table[i].ZA == ZA)
      return &spriggs_table[i];
  }
  return nullptr;
}

// ---------------------------------------------------------------------------
// sample_spriggs_group: select a Spriggs group index in [0, NSPRIGGS)
// using the inverse-CDF method on the group abundances.
//
//   entry  -- SpriggsEntry for this isotope (never nullptr; use fallback_entry()
//              before calling if the isotope is not tabulated)
//   xi     -- uniform [0,1) variate consumed for group selection
//
// Returns 0-indexed group number g such that the emission time should be
// sampled as:  t_delay = -log(xi2) / spriggs_lambda[g]
// ---------------------------------------------------------------------------
inline int sample_spriggs_group(const SpriggsEntry* entry, double xi)
{
  double cumul = 0.0;
  for (int g = 0; g < NSPRIGGS - 1; ++g) {
    cumul += entry->a[g];
    if (xi < cumul)
      return g;
  }
  return NSPRIGGS - 1;
}

} // namespace fission_lib
} // namespace openmc

#endif // OPENMC_USE_FREYA
