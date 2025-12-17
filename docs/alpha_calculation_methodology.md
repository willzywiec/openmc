# Alpha Eigenvalue Calculation in OpenMC

## Overview

The alpha eigenvalue (α) represents the time rate of change of the neutron population in a nuclear system. OpenMC calculates alpha using kinetics parameters derived from prompt neutron chain tallies during normal eigenvalue iterations.

**Formula:**
```
α = (k_prompt - 1) / Λ
```

where:
- **k_prompt** = prompt neutron multiplication factor (excluding delayed neutrons)
- **Λ** = prompt generation time (mean time from birth-to-birth of fission chain)

---

## Physical Meaning

The alpha eigenvalue describes population dynamics:
- **α > 0**: Supercritical (k_prompt > 1) → population growing exponentially
- **α = 0**: Critical (k_prompt = 1) → population stable
- **α < 0**: Subcritical (k_prompt < 1) → population decaying exponentially

### Generation Time vs Lifetime

The alpha eigenvalue is fundamentally a function of **generation time** (Λ), not lifetime (ℓ):

- **Prompt neutron lifetime (ℓ)**: Average time from birth to removal (absorption or leakage)
- **Prompt generation time (Λ)**: Mean time from birth-to-birth of the fission chain

These are related by:
```
Λ = ℓ / k
```

The generation time formulation is more natural because α describes the exponential growth/decay rate of the fission chain, and the chain progresses in generations, not individual neutron lifetimes.

While alpha can be expressed in terms of lifetime as `α = k(k-1)/ℓ`, this is a derived form. The direct relationship `α = (k-1)/Λ` is preferred.

---

## Implementation

### 1. Tally Setup

During initialization, if `calculate_alpha = True`, OpenMC creates an internal tally with prompt-chain scores:

```cpp
void setup_kinetics_tallies()
{
  auto* tally = Tally::create();
  tally->set_writable(false);  // Internal use only

  vector<std::string> scores;
  scores.push_back("prompt-chain-gen-time-num");    // Numerator: Σ(lifetime × weight)
  scores.push_back("prompt-chain-gen-time-denom");  // Denominator: Σ(weight)
  scores.push_back("prompt-chain-nu-fission-rate"); // For diagnostics
  scores.push_back("prompt-chain-absorption-rate"); // For diagnostics
  scores.push_back("prompt-chain-leakage-rate");    // For diagnostics
  scores.push_back("prompt-chain-population");      // For diagnostics

  tally->set_scores(scores);
  tally->set_filters({});  // Tally over entire geometry
}
```

### 2. Calculation During Active Batches

For each active generation, `calculate_kinetics_parameters()` computes:

#### Step 1: Prompt Neutron Lifetime

The prompt neutron lifetime calculation includes both absorption and leakage as removal mechanisms.

```cpp
// Extract tally results (accumulated over active batches)
double gen_time_num = results(0, 0, SUM) / n_active;
double gen_time_denom = results(0, 1, SUM) / n_active;

// Calculate prompt neutron lifetime: ℓ = Σ(lifetime × weight) / Σ(weight)
prompt_lifetime = gen_time_num / gen_time_denom
```

#### Step 2: Prompt Generation Time

```cpp
// Calculate generation time from lifetime: Λ = ℓ / k
prompt_gen_time = prompt_lifetime / keff_prompt
```

#### Step 3: Alpha Eigenvalue

```cpp
// α = (k - 1) / Λ
alpha = (keff_prompt - 1.0) / prompt_gen_time
```

### 3. Uncertainty Propagation

Standard deviations are calculated using error propagation:

**For lifetime ℓ:**
```
σ_ℓ² ≈ (∂ℓ/∂num)² σ_num² + (∂ℓ/∂denom)² σ_denom²
```

**For generation time Λ = ℓ/k:**
```
σ_Λ² ≈ (1/k)² σ_ℓ² + (ℓ/k²)² σ_k²
```

**For α = (k-1)/Λ:**
```
σ_α² ≈ (1/Λ)² σ_k² + ((k-1)/Λ²)² σ_Λ²
```

---

## Tally Scores Explained

### Active Scores (Used in Calculation)

| Index | Score | Description |
|-------|-------|-------------|
| 0 | `prompt-chain-gen-time-num` | Σ(lifetime × weight) - numerator for ℓ |
| 1 | `prompt-chain-gen-time-denom` | Σ(weight) - denominator for ℓ |

### Diagnostic Scores (Not Currently Used)

| Index | Score | Description |
|-------|-------|-------------|
| 2 | `prompt-chain-nu-fission-rate` | Fission production rate |
| 3 | `prompt-chain-absorption-rate` | Total absorption rate |
| 4 | `prompt-chain-leakage-rate` | Leakage rate |
| 5 | `prompt-chain-population` | Prompt neutron population |

---

## Example Calculation

For a typical fast system (Godiva):

**Given:**
- k_prompt = 0.993
- ℓ (lifetime) = 5.66 × 10⁻⁶ seconds

**Calculate:**
```
Λ = ℓ / k = 5.66e-6 / 0.993 = 5.70e-6 seconds

α = (k - 1) / Λ = (0.993 - 1.0) / 5.70e-6 = -1.23e6 s⁻¹
```

This means the prompt neutron population decays at ~1.23 million per second, requiring delayed neutrons to sustain criticality.

---

## Output

OpenMC prints alpha results in the summary:

```
 k-prompt                   = 0.99300 +/- 0.00045
 Beta-effective             = 0.00700 +/- 0.00010
 Prompt Lifetime            = 5.66000e-06 +/- 2.50000e-08 seconds
 Prompt Generation Time     = 5.70000e-06 +/- 2.52000e-08 seconds
 Alpha Eigenvalue           = -1.23000e+06 +/- 1.80000e+04 1/seconds
```

The values are also written to statepoint files for post-processing.

---

## Code Location

- **Setup**: `openmc/src/eigenvalue.cpp::setup_kinetics_tallies()`
- **Scoring (Absorption)**: `openmc/src/tallies/tally_scoring.cpp::score_analog_tally_ce()`
- **Scoring (Leakage)**: `openmc/src/particle.cpp::cross_vacuum_bc()`
- **Calculation**: `openmc/src/eigenvalue.cpp::calculate_kinetics_parameters()`
- **Output**: `openmc/src/output.cpp::print_results()`

---

## References

The relationship α = (k - 1) / Λ is derived from reactor kinetics theory and represents the fundamental mode decay constant for the prompt neutron population. The generation time formulation captures the birth-to-birth behavior of the fission chain, which is what α describes physically.
