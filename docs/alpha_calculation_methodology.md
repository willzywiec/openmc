# Alpha Eigenvalue Calculation in OpenMC

## Overview

The alpha eigenvalue (α) represents the time rate of change of the neutron population in a nuclear system. OpenMC calculates alpha using two methods:

### Static Method (alpha_static)

**Formula:**
```
α_static = (ρ - β_eff) / Λ
```

This is derived from the inhour equation, accounting for delayed neutrons.

### Griesheimer Method (alpha_griesheimer)

**Formula:**
```
α_griesheimer = (ρ - β_eff) / Λ
```

This is the same formula as the static method. The difference is the **methodology**:
- Static: Derive α directly from k-eigenvalue results
- Griesheimer: Iteratively add pseudo-absorption α/v to cross sections until k→1

**Common definitions:**
- **ρ** = (k - 1) / k is reactivity
- **β_eff** = effective delayed neutron fraction = (k - k_prompt) / k
- **Λ** = mean generation time (mean time from neutron birth to fission)

---

## Physical Meaning

The alpha eigenvalue describes population dynamics:
- **α > 0**: Supercritical (k > 1 + β_eff) → population growing exponentially
- **α = 0**: Delayed critical → population stable
- **α < 0**: Subcritical or prompt subcritical → population decaying exponentially

### Mean Generation Time (Λ)

The mean generation time is the average time from neutron birth to fission (production of the next generation). This is measured directly by scoring at fission events:

```
Λ = Σ(time × ν × weight) / Σ(ν × weight)
```

where the sums are taken over all fission events, and ν is the number of neutrons produced.

**Important**: Mean generation time is NOT the same as prompt neutron lifetime. The lifetime (ℓ) is the average time to any removal (absorption or leakage), while generation time (Λ) is specifically the time to fission. These are related but distinct quantities.

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
  // Mean generation time scores (at fission events only)
  scores.push_back("prompt-chain-fission-time-num");   // Σ(time × ν × weight)
  scores.push_back("prompt-chain-fission-time-denom"); // Σ(ν × weight)
  // Diagnostic scores
  scores.push_back("prompt-chain-nu-fission-rate");
  scores.push_back("prompt-chain-absorption-rate");
  scores.push_back("prompt-chain-leakage-rate");
  scores.push_back("prompt-chain-population");

  tally->set_scores(scores);
  tally->set_filters({});  // Tally over entire geometry
}
```

### 2. Scoring at Fission Events

The mean generation time is calculated from scores accumulated at fission events:

```cpp
// At each fission event for prompt neutrons:
// Numerator: time since birth × number of neutrons produced × weight
fission_time_num += lifetime * nu * weight;
// Denominator: number of neutrons produced × weight
fission_time_denom += nu * weight;
```

### 3. Calculation During Active Batches

For each active generation, `calculate_kinetics_parameters()` computes:

#### Step 1: Mean Generation Time

```cpp
// Extract tally results (accumulated over active batches)
double fission_time_num = results(0, 0, SUM) / n_active;
double fission_time_denom = results(0, 1, SUM) / n_active;

// Calculate mean generation time: Λ = Σ(t × ν × w) / Σ(ν × w)
mean_generation_time = fission_time_num / fission_time_denom;
```

#### Step 2: Static Alpha Eigenvalue

```cpp
// Calculate reactivity
double rho = (keff - 1.0) / keff;

// α_static = (ρ - β_eff) / Λ
alpha_static = (rho - beta_eff) / mean_generation_time;
```

#### Step 3: Griesheimer Alpha Eigenvalue (Iterative Method)

After main eigenvalue batches complete, runs additional iterations with pseudo-absorption:

```cpp
// Initialize with static alpha as guess
alpha_current = alpha_static;

// Iteration loop
for (int iter = 1; iter <= max_iterations; ++iter) {
  // Run batches with pseudo-absorption α/v added to cross sections
  // ... transport with modified cross sections ...

  // Check convergence
  if (|k - 1| < tolerance) {
    alpha_griesheimer = alpha_current;
    break;
  }

  // Update alpha: α_new = α_old + (k - 1) / (k × Λ)
  alpha_current += (k - 1.0) / (k * mean_generation_time);
}
```

### 4. Uncertainty Propagation

Standard deviations are calculated using error propagation:

**For mean generation time Λ:**
```
σ_Λ² ≈ (∂Λ/∂num)² σ_num² + (∂Λ/∂denom)² σ_denom²
```

**For α_static = (ρ - β)/Λ:**
```
σ_α² ≈ (∂α/∂k)² σ_k² + (∂α/∂β)² σ_β² + (∂α/∂Λ)² σ_Λ²
```

where:
- ∂α/∂k = 1/(k²Λ)
- ∂α/∂β = -1/Λ
- ∂α/∂Λ = -(ρ - β)/Λ²

**For α_griesheimer:**

Uncertainty is estimated from the iterative convergence. Currently uses the same uncertainty as α_static as an approximation.

---

## Tally Scores Explained

### Active Scores (Used in Calculation)

| Index | Score | Description |
|-------|-------|-------------|
| 0 | `prompt-chain-fission-time-num` | Σ(time × ν × weight) at fission events |
| 1 | `prompt-chain-fission-time-denom` | Σ(ν × weight) at fission events |

### Diagnostic Scores

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
- k = 1.0001
- k_prompt = 0.993
- Λ (mean generation time) = 5.7 × 10⁻⁹ seconds

**Calculate:**
```
ρ = (k - 1) / k = (1.0001 - 1.0) / 1.0001 = 0.0001

β_eff = (k - k_prompt) / k = (1.0001 - 0.993) / 1.0001 = 0.0071

α = (ρ - β_eff) / Λ = (0.0001 - 0.0071) / 5.7e-9 = -1.23e6 s⁻¹
```

Both α_static and α_griesheimer use this same formula. The negative alpha means the prompt neutron population decays at ~1.23 million per second, requiring delayed neutrons to sustain criticality.

---

## Output

OpenMC prints alpha results in the summary:

```
 k-prompt                   = 0.99300 +/- 0.00045
 Beta-effective             = 0.00700 +/- 0.00010
 Mean Generation Time       = 5.70000e-09 +/- 2.50000e-11 seconds
 Alpha (static)             = -1.23000e+06 +/- 1.80000e+04 1/seconds
 Alpha (Griesheimer)        = -1.23000e+06 +/- 1.80000e+04 1/seconds
```

After the main results, Griesheimer iterations are shown:

```
 ====================>     GRIESHEIMER ALPHA ITERATIONS     <====================

 Starting iterative pseudo-absorption method
 Initial alpha guess (from static): -1.23000e+06 1/s
 Convergence tolerance: |k - 1| < 0.0010

 Iteration  1: alpha = -1.23000e+06 1/s
             k = 1.00012 +/- 0.00045, |k-1| = 0.00012

 Griesheimer method converged after 1 iterations
 Final alpha (Griesheimer) = -1.23000e+06 1/s
```

The values are also written to statepoint files for post-processing.

---

## Code Location

- **Setup**: `openmc/src/eigenvalue.cpp::setup_kinetics_tallies()`
- **Scoring (Fission)**: `openmc/src/tallies/tally_scoring.cpp::score_analog_tally_ce()`
- **Static Alpha Calculation**: `openmc/src/eigenvalue.cpp::calculate_kinetics_parameters()`
- **Griesheimer Alpha Calculation**: `openmc/src/eigenvalue.cpp::run_alpha_iterations()`
- **Pseudo-absorption**: `openmc/src/material.cpp::calculate_neutron_xs()`
- **Output**: `openmc/src/output.cpp::print_results()`

---

## References

Both static and Griesheimer methods use the same fundamental equation α = (ρ - β_eff) / Λ from reactor kinetics theory (the inhour equation). The mean generation time Λ is measured directly as the ν-weighted time-to-fission, which correctly captures the birth-to-birth behavior of the fission chain.

The Griesheimer method differs in methodology, not formula. It adds pseudo-absorption α/v to cross sections and iterates until k converges to 1, providing an independent verification of the alpha eigenvalue.
