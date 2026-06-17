# Alpha Eigenvalue Calculation in OpenMC

## Overview

The alpha eigenvalue (α) represents the time rate of change of the neutron population in a nuclear system. OpenMC calculates two forms of the alpha eigenvalue directly from the IFP-weighted prompt neutron lifetime ℓ_p:

**Delayed critical alpha** (assumes ρ = 0, i.e., k_eff = 1):
```
α_dc = −β_eff / ℓ_p
```

**Static alpha** (uses actual reactivity state):
```
α = (k_p − 1) / ℓ_p
```

**Definitions:**
- **k_eff** = effective multiplication factor
- **k_p** = prompt multiplication factor = k_eff · (1 − β_eff)
- **β_eff** = effective delayed neutron fraction (from k-prompt)
- **ℓ_p** = IFP-weighted prompt neutron lifetime
- **Λ_p** = IFP-weighted prompt generation time = ℓ_p / k_p (reported only; not used in α)

---

## Physical Meaning

The alpha eigenvalue describes prompt neutron population dynamics:
- **α < 0**: Subcritical (ρ < β_eff) → prompt neutrons decaying
- **α = 0**: Prompt critical (ρ = β_eff) → prompt neutron population stable
- **α > 0**: Prompt supercritical (ρ > β_eff) → prompt neutrons growing exponentially

### Kinetics Parameters

The kinetics parameters are computed using two methods:

```
β_eff = (k - k_prompt) / k                                          (from k-prompt)
Λ_eff = ifp-time-numerator        / (ifp-denominator × k_eff)        (from IFP)
ℓ_p   = ifp-prompt-time-numerator /  ifp-prompt-denominator          (from IFP)
Λ_p   = ℓ_p / k_p                                                    (reported only)
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

#### Step 2: Generation Time and Prompt Neutron Lifetime

```cpp
// Λ_eff = ifp-time-numerator / (ifp-denominator × k_eff)
lambda_eff_ifp = ifp_time_num / (ifp_denom * keff);

// ℓ_p = ifp-prompt-time-numerator / ifp-prompt-denominator
double lp = ifp_prompt_time_num / ifp_prompt_denom;
lifetime_p_ifp = lp;

// Λ_p = ℓ_p / k_p (reported only; not used in α)
lambda_p_ifp = lp / kp;
```

#### Step 3: Alpha Eigenvalues

```cpp
// k_p = k_eff · (1 − β_eff)
double kp = k * (1.0 - beta);

// Delayed critical: α_dc = −β_eff / ℓ_p
alpha_dc_ifp = -beta / lp;

// Static: α = (k_p − 1) / ℓ_p
alpha_ifp = (kp - 1.0) / lp;
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

**For α_dc = −β_eff / ℓ_p:**
```
σ_α_dc² ≈ (1/ℓ_p)² σ_β² + (β_eff/ℓ_p²)² σ_ℓp²
```

**For α = (k_p − 1) / ℓ_p, with k_p = k_eff · (1 − β_eff):**
```
σ_α² ≈ ((1 − β_eff)/ℓ_p)² σ_k²
     + (k_eff/ℓ_p)²        σ_β²
     + ((k_p − 1)/ℓ_p²)²    σ_ℓp²
```

---

## Example Calculation

For a typical fast system (Godiva) near critical:

**Given:**
- k = 1.0001
- β_eff = 0.0065
- ℓ_p = 5.66 × 10⁻⁹ seconds
- k_p = k · (1 − β_eff) = 1.0001 × 0.9935 ≈ 0.99360
- Λ_p = ℓ_p / k_p ≈ 5.70 × 10⁻⁹ seconds

**Calculate:**
```
α_dc = −β_eff / ℓ_p   = −0.0065      / 5.66e-9 ≈ −1.15e6 s⁻¹

α    = (k_p − 1) / ℓ_p = (0.99360 − 1) / 5.66e-9 ≈ −1.13e6 s⁻¹
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
