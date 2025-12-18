# Alpha Eigenvalue Calculation in OpenMC

## Overview

The alpha eigenvalue (α) represents the time rate of change of the neutron population in a nuclear system. OpenMC calculates alpha using the IFP (Iterated Fission Probability) method:

**Formula:**
```
α = (k - 1) / Λ_eff
```

**Definitions:**
- **k** = effective multiplication factor (k-effective)
- **Λ_eff** = IFP-weighted effective generation time

---

## Physical Meaning

The alpha eigenvalue describes population dynamics:
- **α > 0**: Supercritical (k > 1) → population growing exponentially
- **α = 0**: Critical (k = 1) → population stable
- **α < 0**: Subcritical (k < 1) → population decaying exponentially

### Effective Generation Time (Λ_eff)

The effective generation time is computed using the IFP method, which provides adjoint-weighted quantities:

```
Λ_eff = ifp-time-numerator / (ifp-denominator × k_eff)
```

The IFP method properly accounts for the importance of neutrons at different energies and positions, giving physically meaningful results for reactor kinetics.

---

## Implementation

### 1. IFP Infrastructure

OpenMC's existing IFP (Iterated Fission Probability) infrastructure is used for alpha calculations. The same scores used for beta-effective calculations provide the generation time:

- `ifp-time-numerator`: IFP-weighted time to fission
- `ifp-denominator`: IFP normalization factor

### 2. Tally Setup

During initialization, if `calculate_alpha = True`, OpenMC creates an internal tally:

```cpp
void setup_kinetics_tallies()
{
  if (!settings::calculate_alpha || !settings::ifp_on)
    return;

  auto* tally = Tally::create();
  tally->set_writable(false);  // Internal use only

  vector<std::string> scores;
  scores.push_back("ifp-time-numerator");
  scores.push_back("ifp-denominator");

  tally->set_scores(scores);
  tally->set_filters({});  // Tally over entire geometry
}
```

### 3. Calculation During Active Batches

For each active generation, `calculate_kinetics_parameters()` computes:

#### Step 1: Effective Generation Time

```cpp
// Get IFP tally results
double ifp_time_num = ifp_tally_results(IFP_TIME_NUM);
double ifp_denom = ifp_tally_results(IFP_DENOM);

// Calculate effective generation time
// Λ_eff = ifp-time-numerator / (ifp-denominator × k_eff)
lambda_eff_ifp = ifp_time_num / (ifp_denom * keff);
```

#### Step 2: Alpha Eigenvalue

```cpp
// α = (k - 1) / Λ_eff
alpha_ifp = (keff - 1.0) / lambda_eff_ifp;
```

### 4. Uncertainty Propagation

Standard deviations are calculated using error propagation:

**For Λ_eff:**
```
σ_Λ² ≈ (∂Λ/∂num)² σ_num² + (∂Λ/∂denom)² σ_denom² + (∂Λ/∂k)² σ_k²
```

**For α = (k - 1) / Λ_eff:**
```
σ_α² ≈ (∂α/∂k)² σ_k² + (∂α/∂Λ)² σ_Λ²
```

where:
- ∂α/∂k = 1/Λ_eff
- ∂α/∂Λ = -(k - 1)/Λ_eff²

---

## Example Calculation

For a typical fast system (Godiva):

**Given:**
- k = 1.0001
- Λ_eff (IFP-weighted) = 5.7 × 10⁻⁹ seconds

**Calculate:**
```
α = (k - 1) / Λ_eff = (1.0001 - 1.0) / 5.7e-9 = 1.75e4 s⁻¹
```

The positive alpha means the neutron population grows at ~17,500 per second for this slightly supercritical system.

---

## Output

OpenMC prints alpha results in the summary:

```
 k-prompt                   = 0.99300 +/- 0.00045
 Beta-effective             = 0.00700 +/- 0.00010
 Lambda_eff (IFP)           = 5.70000e-09 +/- 2.50000e-11 seconds
 Alpha (IFP)                = 1.75000e+04 +/- 1.80000e+02 1/seconds
```

The values are also written to statepoint files for post-processing via:
- `sp.lambda_eff_ifp` - IFP-weighted effective generation time
- `sp.alpha_ifp` - IFP-weighted alpha eigenvalue

---

## Code Location

- **Setup**: `openmc/src/eigenvalue.cpp::setup_kinetics_tallies()`
- **IFP Scoring**: `openmc/src/ifp.cpp`
- **Alpha Calculation**: `openmc/src/eigenvalue.cpp::calculate_kinetics_parameters()`
- **Output**: `openmc/src/output.cpp::print_results()`

---

## References

The alpha calculation uses the fundamental relationship α = (k - 1) / Λ_eff from reactor kinetics theory. The IFP method provides adjoint-weighted generation times that correctly account for neutron importance, making it suitable for heterogeneous reactor calculations.
