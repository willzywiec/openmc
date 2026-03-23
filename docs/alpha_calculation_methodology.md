# Alpha Eigenvalue Calculation in OpenMC

## Overview

The alpha eigenvalue (α) represents the time rate of change of the neutron population in a nuclear system. OpenMC calculates two forms of the alpha eigenvalue using the IFP (Iterated Fission Probability) method:

**Delayed critical alpha** (assumes ρ = 0):
```
α_dc = −β_eff · k_eff / Λ_p
```

**Static alpha** (uses actual reactivity state):
```
α = (k_eff − 1 − β_eff · k_eff) / Λ_p
```

**Definitions:**
- **k_eff** = effective multiplication factor
- **β_eff** = effective delayed neutron fraction (from k-prompt)
- **Λ_p** = IFP-weighted prompt generation time

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
Λ_p = ifp-prompt-time-numerator / (ifp-prompt-denominator × k_eff)   (from IFP)
```

The β_eff is calculated from the difference between total k-effective and prompt k-effective. The Λ_eff and Λ_p use the IFP (Iterated Fission Probability) method which properly accounts for the importance of neutrons at different energies and positions.

---

## Implementation

### 1. IFP Infrastructure

OpenMC's IFP (Iterated Fission Probability) infrastructure is used for generation time calculations:

- `ifp-time-numerator`: IFP-weighted time to fission
- `ifp-prompt-time-numerator`: IFP-weighted prompt time to fission
- `ifp-denominator`: IFP normalization factor
- `ifp-prompt-denominator`: IFP prompt normalization factor

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
  scores.push_back("ifp-time-numerator");          // Index 0
  scores.push_back("ifp-prompt-time-numerator");   // Index 1
  scores.push_back("ifp-denominator");             // Index 2
  scores.push_back("ifp-prompt-denominator");      // Index 3

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

#### Step 2: Generation Times

```cpp
// Λ_eff = ifp-time-numerator / (ifp-denominator × k_eff)
lambda_eff_ifp = ifp_time_num / (ifp_denom * keff);

// Λ_p = ifp-prompt-time-numerator / (ifp-prompt-denominator × k_eff)
lambda_p_ifp = ifp_prompt_time_num / (ifp_prompt_denom * keff);
```

#### Step 3: Alpha Eigenvalues

```cpp
// Delayed critical: α_dc = −β_eff · k_eff / Λ_p
alpha_dc_ifp = -beta * k / Lp;

// Static: α = (k_eff − 1 − β_eff · k_eff) / Λ_p
alpha_ifp = (k - 1.0 - beta * k) / Lp;
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

**For α_dc = −β_eff · k_eff / Λ_p (using equivalent form α = (k_p − k) / Λ_p):**
```
σ_α² ≈ (1/Λ_p)² σ_kp² + (−1/Λ_p)² σ_k² + ((k_p − k)/Λ_p²)² σ_Λp²
```

**For α = (k − 1 − β · k) / Λ_p:**
```
σ_α² ≈ ((1−β)/Λ_p)² σ_k² + (−k/Λ_p)² σ_β² + (−α/Λ_p)² σ_Λp²
```

---

## Example Calculation

For a typical fast system (Godiva) near critical:

**Given:**
- k = 1.0001
- β_eff = 0.0065
- Λ_p = 5.7 × 10⁻⁹ seconds

**Calculate:**
```
α_dc = −β_eff · k / Λ_p = −0.0065 × 1.0001 / 5.7e-9 ≈ −1.14e6 s⁻¹

α = (k − 1 − β · k) / Λ_p = (1.0001 − 1.0 − 0.0065 × 1.0001) / 5.7e-9 ≈ −1.12e6 s⁻¹
```

The negative alpha (with ρ < β_eff) indicates the system is subcritical on the prompt timescale - prompt neutrons decay, but delayed neutrons sustain the chain reaction.

---

## Output

OpenMC prints alpha results in the summary:

```
 k-prompt                   = 0.99350 +/- 0.00045
 Beta-effective             = 0.00650 +/- 0.00010
 Lambda-effective (IFP)     = 5.70000e-09 +/- 2.50000e-11 seconds
 Lambda-prompt (IFP)        = 5.60000e-09 +/- 2.40000e-11 seconds
 Alpha (Delayed Critical)    = -1.14000e+06 +/- 1.80000e+04 1/seconds
 Alpha (Static)              = -1.12000e+06 +/- 1.80000e+04 1/seconds
```

The values are also written to statepoint files for post-processing via:
- `sp.beta_eff` - effective delayed neutron fraction (from k-prompt)
- `sp.lambda_eff_ifp` - IFP-weighted effective generation time
- `sp.lambda_p_ifp` - IFP-weighted prompt generation time
- `sp.alpha_dc_ifp` - delayed critical alpha eigenvalue
- `sp.alpha_ifp` - static alpha eigenvalue

---

## Code Location

- **Setup**: `openmc/src/eigenvalue.cpp::setup_kinetics_tallies()`
- **IFP Scoring**: `openmc/src/ifp.cpp`
- **Kinetics Calculation**: `openmc/src/eigenvalue.cpp::calculate_kinetics_parameters()`
- **Output**: `openmc/src/output.cpp::print_results()`

---

## References

The alpha calculation uses standard reactor kinetics theory. The IFP method provides adjoint-weighted quantities that correctly account for neutron importance, making it suitable for heterogeneous reactor calculations.
