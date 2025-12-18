# Alpha Eigenvalue Calculation in OpenMC

## Overview

The alpha eigenvalue (α) represents the time rate of change of the neutron population in a nuclear system. OpenMC calculates alpha using the IFP (Iterated Fission Probability) method:

**Formula:**
```
α = (β_eff - ρ) / Λ_eff
```

**Definitions:**
- **β_eff** = effective delayed neutron fraction (IFP-weighted)
- **ρ** = reactivity = (k - 1) / k
- **Λ_eff** = IFP-weighted effective generation time

---

## Physical Meaning

The alpha eigenvalue describes prompt neutron population dynamics:
- **α > 0**: Subcritical on prompt timescale (ρ < β_eff) → prompt neutrons decaying
- **α = 0**: Delayed critical (ρ = β_eff) → prompt neutron population stable
- **α < 0**: Prompt supercritical (ρ > β_eff) → prompt neutrons growing exponentially

### IFP-Weighted Quantities

All kinetics parameters are computed using IFP adjoint weighting:

```
β_eff = ifp-beta-numerator / ifp-denominator
Λ_eff = ifp-time-numerator / (ifp-denominator × k_eff)
```

The IFP method properly accounts for the importance of neutrons at different energies and positions, giving physically meaningful results for reactor kinetics.

---

## Implementation

### 1. IFP Infrastructure

OpenMC's existing IFP (Iterated Fission Probability) infrastructure is used for all kinetics calculations:

- `ifp-time-numerator`: IFP-weighted time to fission
- `ifp-beta-numerator`: IFP-weighted delayed neutron fraction numerator
- `ifp-denominator`: IFP normalization factor (common denominator)

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
  scores.push_back("ifp-time-numerator");   // Index 0
  scores.push_back("ifp-denominator");      // Index 1
  scores.push_back("ifp-beta-numerator");   // Index 2

  tally->set_scores(scores);
  tally->set_filters({});  // Tally over entire geometry
}
```

### 3. Calculation During Active Batches

For each active generation, `calculate_kinetics_parameters()` computes:

#### Step 1: Effective Delayed Neutron Fraction

```cpp
// β_eff = ifp-beta-numerator / ifp-denominator
beta_eff = ifp_beta_num / ifp_denom;
```

#### Step 2: Effective Generation Time

```cpp
// Λ_eff = ifp-time-numerator / (ifp-denominator × k_eff)
lambda_eff_ifp = ifp_time_num / (ifp_denom * keff);
```

#### Step 3: Alpha Eigenvalue

```cpp
// ρ = (k - 1) / k
double rho = (keff - 1.0) / keff;

// α = (β_eff - ρ) / Λ_eff
alpha_ifp = (beta_eff - rho) / lambda_eff_ifp;
```

### 4. Uncertainty Propagation

Standard deviations are calculated using error propagation:

**For β_eff = beta_num / denom:**
```
σ_β² ≈ (∂β/∂num)² σ_num² + (∂β/∂denom)² σ_denom²
```

**For Λ_eff:**
```
σ_Λ² ≈ (∂Λ/∂num)² σ_num² + (∂Λ/∂denom)² σ_denom² + (∂Λ/∂k)² σ_k²
```

**For α = (β - ρ) / Λ:**
```
σ_α² ≈ (∂α/∂β)² σ_β² + (∂α/∂k)² σ_k² + (∂α/∂Λ)² σ_Λ²
```

where:
- ∂α/∂β = 1/Λ
- ∂α/∂k = -1/(k²Λ)
- ∂α/∂Λ = -(β - ρ)/Λ²

---

## Example Calculation

For a typical fast system (Godiva) near critical:

**Given:**
- k = 1.0001
- β_eff = 0.0065
- Λ_eff = 5.7 × 10⁻⁹ seconds

**Calculate:**
```
ρ = (k - 1) / k = (1.0001 - 1.0) / 1.0001 ≈ 0.0001

α = (β_eff - ρ) / Λ_eff = (0.0065 - 0.0001) / 5.7e-9 ≈ 1.12e6 s⁻¹
```

The positive alpha (with β_eff > ρ) indicates the system is subcritical on the prompt timescale - prompt neutrons decay but delayed neutrons sustain the chain reaction.

---

## Output

OpenMC prints alpha results in the summary:

```
 k-prompt                   = 0.99350 +/- 0.00045
 Beta-effective             = 0.00650 +/- 0.00010
 Lambda_eff (IFP)           = 5.70000e-09 +/- 2.50000e-11 seconds
 Alpha (IFP)                = 1.12000e+06 +/- 1.80000e+04 1/seconds
```

The values are also written to statepoint files for post-processing via:
- `sp.beta_eff` - IFP-weighted effective delayed neutron fraction
- `sp.lambda_eff_ifp` - IFP-weighted effective generation time
- `sp.alpha_ifp` - IFP-weighted alpha eigenvalue

---

## Code Location

- **Setup**: `openmc/src/eigenvalue.cpp::setup_kinetics_tallies()`
- **IFP Scoring**: `openmc/src/ifp.cpp`
- **Kinetics Calculation**: `openmc/src/eigenvalue.cpp::calculate_kinetics_parameters()`
- **Output**: `openmc/src/output.cpp::print_results()`

---

## References

The alpha calculation uses the inhour equation from reactor kinetics theory:
```
α = (β_eff - ρ) / Λ_eff
```

The IFP method provides adjoint-weighted quantities that correctly account for neutron importance, making it suitable for heterogeneous reactor calculations.
