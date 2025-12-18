# Alpha Eigenvalue Calculation in OpenMC

## Overview

The alpha eigenvalue (α) represents the time rate of change of the neutron population in a nuclear system. OpenMC calculates alpha using the IFP (Iterated Fission Probability) method:

**Formula:**
```
α = (ρ - β_eff) / Λ_eff
```

**Definitions:**
- **ρ** = reactivity = (k - 1) / k
- **β_eff** = effective delayed neutron fraction (from k-prompt)
- **Λ_eff** = IFP-weighted effective generation time

---

## Physical Meaning

The alpha eigenvalue describes prompt neutron population dynamics:
- **α < 0**: Subcritical (ρ < β_eff) → prompt neutrons decaying
- **α = 0**: Prompt critical (ρ = β_eff) → prompt neutron population stable
- **α > 0**: Prompt supercritical (ρ > β_eff) → prompt neutrons growing exponentially

### Kinetics Parameters

The kinetics parameters are computed using two methods:

```
β_eff = (k - k_prompt) / k          (from k-prompt)
Λ_eff = ifp-time-numerator / (ifp-denominator × k_eff)   (from IFP)
```

The β_eff is calculated from the difference between total k-effective and prompt k-effective. The Λ_eff uses the IFP (Iterated Fission Probability) method which properly accounts for the importance of neutrons at different energies and positions.

---

## Implementation

### 1. IFP Infrastructure

OpenMC's IFP (Iterated Fission Probability) infrastructure is used for generation time calculations:

- `ifp-time-numerator`: IFP-weighted time to fission
- `ifp-denominator`: IFP normalization factor

β_eff is calculated separately from k-prompt (no IFP tally needed).

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

  tally->set_scores(scores);
  tally->set_filters({});  // Tally over entire geometry
}
```

### 3. Calculation During Active Batches

For each active generation, `calculate_kinetics_parameters()` computes:

#### Step 1: Effective Delayed Neutron Fraction

```cpp
// β_eff = (k - k_prompt) / k
beta_eff = (keff - keff_prompt) / keff;
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

// α = (ρ - β_eff) / Λ_eff
alpha_ifp = (rho - beta_eff) / lambda_eff_ifp;
```

### 4. Uncertainty Propagation

Standard deviations are calculated using error propagation:

**For β_eff = (k - k_prompt) / k:**
```
σ_β² ≈ (1/k)² σ_k_prompt² + (k_prompt/k²)² σ_k²
```

**For Λ_eff:**
```
σ_Λ² ≈ (∂Λ/∂num)² σ_num² + (∂Λ/∂denom)² σ_denom² + (∂Λ/∂k)² σ_k²
```

**For α = (ρ - β) / Λ:**
```
σ_α² ≈ (∂α/∂β)² σ_β² + (∂α/∂k)² σ_k² + (∂α/∂Λ)² σ_Λ²
```

where:
- ∂α/∂β = -1/Λ
- ∂α/∂k = 1/(k²Λ)
- ∂α/∂Λ = -(ρ - β)/Λ²

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

α = (ρ - β_eff) / Λ_eff = (0.0001 - 0.0065) / 5.7e-9 ≈ -1.12e6 s⁻¹
```

The negative alpha (with ρ < β_eff) indicates the system is subcritical on the prompt timescale - prompt neutrons decay, but delayed neutrons sustain the chain reaction.

---

## Output

OpenMC prints alpha results in the summary:

```
 k-prompt                   = 0.99350 +/- 0.00045
 Beta-effective             = 0.00650 +/- 0.00010
 Lambda_eff (IFP)           = 5.70000e-09 +/- 2.50000e-11 seconds
 Alpha (IFP)                = -1.12000e+06 +/- 1.80000e+04 1/seconds
```

The values are also written to statepoint files for post-processing via:
- `sp.beta_eff` - effective delayed neutron fraction (from k-prompt)
- `sp.lambda_eff_ifp` - IFP-weighted effective generation time
- `sp.alpha_ifp` - alpha eigenvalue

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
α = (ρ - β_eff) / Λ_eff
```

The IFP method provides adjoint-weighted quantities that correctly account for neutron importance, making it suitable for heterogeneous reactor calculations.
