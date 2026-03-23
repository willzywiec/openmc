# Alpha Eigenvalue Calculations in OpenMC

This guide explains how to use OpenMC's alpha eigenvalue calculation capability for reactor kinetics analysis.

## Overview

The alpha eigenvalue (α) describes the time-dependent behavior of the neutron population in a nuclear system. OpenMC calculates two forms of the alpha eigenvalue using the prompt generation time Λ_p from the IFP method:

**Delayed critical alpha** (assumes the system is exactly delayed critical, i.e., ρ = 0):
```
α_dc = −β_eff · k_eff / Λ_p
```

**Actual alpha** (uses the system's actual reactivity state):
```
α = (k_eff − 1 − β_eff · k_eff) / Λ_p
```

Where:
- **k_eff**: Effective multiplication factor
- **β_eff**: Effective delayed neutron fraction (from k-prompt)
- **Λ_p**: IFP-weighted prompt generation time

The kinetics parameters are computed as:
```
β_eff = (k - k_prompt) / k
Λ_eff = ifp-time-numerator / (ifp-denominator × k_eff)
Λ_p = ifp-prompt-time-numerator / (ifp-prompt-denominator × k_eff)
```

### Physical Interpretation

| Alpha Value | System State | Behavior |
|-------------|--------------|----------|
| α < 0 | Subcritical (ρ < β_eff) | Prompt neutrons decaying |
| α = 0 | Prompt critical (ρ = β_eff) | Prompt neutron population stable |
| α > 0 | Prompt supercritical (ρ > β_eff) | Prompt neutron population growing exponentially |

## Quick Start

### Basic Example

```python
import openmc

# Create your geometry and materials (not shown)
# ...

# Configure settings for alpha calculation
settings = openmc.Settings()
settings.batches = 150
settings.inactive = 50
settings.particles = 10000
settings.calculate_alpha = True  # Enable alpha eigenvalue calculation

# Note: calculate_alpha automatically enables:
# - calculate_prompt_k
# - IFP (Iterated Fission Probability) with 10 generations by default
# IFP is used to calculate β_eff, Λ_p, and α
settings.export_to_xml()

# Run OpenMC
openmc.run()

# Read results from statepoint file
sp = openmc.StatePoint('statepoint.150.h5')

# Access kinetics parameters
print(f"k-effective:              {sp.keff}")
print(f"k-prompt:                 {sp.k_prompt}")
print(f"Beta-effective:           {sp.beta_eff}")
print(f"Lambda-effective (IFP):   {sp.lambda_eff_ifp} seconds")
print(f"Lambda-prompt (IFP):      {sp.lambda_p_ifp} seconds")
print(f"Alpha (Delayed Critical): {sp.alpha_dc_ifp} 1/seconds")
print(f"Alpha (Static):           {sp.alpha_ifp} 1/seconds")
```

## Detailed Usage

### Settings Configuration

```python
settings = openmc.Settings()

# Required for alpha calculation
settings.calculate_alpha = True

# Optional: explicitly enable prompt k calculation (automatically enabled by calculate_alpha)
settings.calculate_prompt_k = True

# Recommended settings for good statistics
settings.batches = 150          # Total batches
settings.inactive = 50          # Inactive batches for source convergence
settings.particles = 10000      # Particles per batch
```

### Reading Results

The `StatePoint` class provides several properties for accessing kinetics results:

```python
sp = openmc.StatePoint('statepoint.150.h5')

# All values are returned as ufloat objects with uncertainty
# Access nominal value with .nominal_value and uncertainty with .std_dev

# k-effective (total)
keff = sp.keff
print(f"k-eff = {keff.nominal_value:.5f} +/- {keff.std_dev:.5f}")

# Prompt k-effective
k_prompt = sp.k_prompt
print(f"k-prompt = {k_prompt.nominal_value:.5f} +/- {k_prompt.std_dev:.5f}")

# Effective delayed neutron fraction
beta = sp.beta_eff
print(f"beta-eff = {beta.nominal_value:.5f} +/- {beta.std_dev:.5f}")

# IFP-weighted effective generation time (in seconds)
lambda_eff = sp.lambda_eff_ifp
print(f"Λ_eff = {lambda_eff.nominal_value:.3e} +/- {lambda_eff.std_dev:.3e} s")

# IFP-weighted prompt generation time (in seconds)
lambda_p = sp.lambda_p_ifp
print(f"Λ_p = {lambda_p.nominal_value:.3e} +/- {lambda_p.std_dev:.3e} s")

# Alpha eigenvalue at delayed critical (in 1/seconds)
alpha_dc = sp.alpha_dc_ifp
print(f"alpha_dc = {alpha_dc.nominal_value:.3e} +/- {alpha_dc.std_dev:.3e} 1/s")

# Alpha eigenvalue at actual reactivity (in 1/seconds)
alpha = sp.alpha_ifp
print(f"alpha = {alpha.nominal_value:.3e} +/- {alpha.std_dev:.3e} 1/s")
```

### Converting Units

Alpha eigenvalue is often reported in different units:

```python
sp = openmc.StatePoint('statepoint.150.h5')

# Alpha in 1/seconds (default)
alpha_per_sec = sp.alpha_ifp.nominal_value

# Alpha in generations per microsecond
alpha_per_us = alpha_per_sec / 1e6

# Alpha in generations per millisecond
alpha_per_ms = alpha_per_sec / 1e3

# Effective generation time in microseconds
lambda_eff_us = sp.lambda_eff_ifp.nominal_value * 1e6

print(f"Alpha: {alpha_per_us:.4f} gen/us")
print(f"Lambda_eff: {lambda_eff_us:.2f} us")
```

## Complete Example: Godiva Benchmark

This example models the Godiva bare HEU sphere, a standard benchmark for kinetics calculations:

```python
import openmc

# Materials
heu = openmc.Material(name='HEU')
heu.add_nuclide('U235', 0.9406, 'ao')
heu.add_nuclide('U238', 0.0536, 'ao')
heu.add_nuclide('U234', 0.0058, 'ao')
heu.set_density('g/cm3', 18.74)

materials = openmc.Materials([heu])
materials.export_to_xml()

# Geometry - bare sphere
sphere = openmc.Sphere(r=8.7407, boundary_type='vacuum')
cell = openmc.Cell(fill=heu, region=-sphere)
universe = openmc.Universe(cells=[cell])
geometry = openmc.Geometry(universe)
geometry.export_to_xml()

# Settings
settings = openmc.Settings()
settings.batches = 200
settings.inactive = 50
settings.particles = 20000
settings.calculate_alpha = True

# Initial source
settings.source = openmc.IndependentSource(
    space=openmc.stats.Point((0, 0, 0))
)
settings.export_to_xml()

# Run
openmc.run()

# Analyze results
sp = openmc.StatePoint('statepoint.200.h5')

print("=" * 50)
print("Godiva Kinetics Parameters")
print("=" * 50)
print(f"k-effective:              {sp.keff.nominal_value:.5f} +/- {sp.keff.std_dev:.5f}")
print(f"k-prompt:                 {sp.k_prompt.nominal_value:.5f} +/- {sp.k_prompt.std_dev:.5f}")
print(f"Beta-effective:           {sp.beta_eff.nominal_value:.5f} +/- {sp.beta_eff.std_dev:.5f}")
print(f"Lambda-effective (IFP):   {sp.lambda_eff_ifp.nominal_value*1e9:.2f} +/- {sp.lambda_eff_ifp.std_dev*1e9:.2f} ns")
print(f"Lambda-prompt (IFP):      {sp.lambda_p_ifp.nominal_value*1e9:.2f} +/- {sp.lambda_p_ifp.std_dev*1e9:.2f} ns")
print(f"Alpha (Delayed Critical): {sp.alpha_dc_ifp.nominal_value/1e6:.4f} +/- {sp.alpha_dc_ifp.std_dev/1e6:.4f} gen/us")
print(f"Alpha (Static):           {sp.alpha_ifp.nominal_value/1e6:.4f} +/- {sp.alpha_ifp.std_dev/1e6:.4f} gen/us")
```

## Output Format

When running OpenMC with alpha calculations enabled, the output will include a kinetics parameters section:

```
 ====================>     RESULTS     <====================

  k-effective (Combined)      = 1.00012 +/- 0.00045
  k-prompt                    = 0.99312 +/- 0.00044
  Beta-effective              = 0.00700 +/- 0.00012
  Lambda-effective (IFP)      = 5.70000e-09 +/- 2.50000e-11 seconds
  Lambda-prompt (IFP)         = 5.60000e-09 +/- 2.40000e-11 seconds
  Alpha (Delayed Critical)    = -1.25000e+06 +/- 1.80000e+04 1/seconds
  Alpha (Static)              = 1.75000e+04 +/- 1.80000e+02 1/seconds
```

## Implementation Details

### Calculation Methods

**β_eff (Effective Delayed Neutron Fraction)**: Calculated from k-prompt using the formula β_eff = (k - k_prompt) / k. This approach uses the difference between total k-effective and prompt k-effective to determine the delayed neutron fraction.

**Λ_eff (Effective Generation Time)**: Calculated using OpenMC's Iterated Fission Probability (IFP) infrastructure. IFP provides adjoint-weighted quantities that properly account for the importance of neutrons at different energies and positions:
```
Λ_eff = ifp-time-numerator / (ifp-denominator × k_eff)
```

**Λ_p (Prompt Generation Time)**: Also calculated using IFP, but using prompt-only scores:
```
Λ_p = ifp-prompt-time-numerator / (ifp-prompt-denominator × k_eff)
```

**α_dc (Delayed Critical Alpha)**: Assumes the system is exactly delayed critical (ρ = 0):
```
α_dc = −β_eff · k_eff / Λ_p
```

**α (Actual Alpha)**: Uses the system's actual reactivity:
```
α = (k_eff − 1 − β_eff · k_eff) / Λ_p
```

IFP scores used:
- `ifp-time-numerator`: IFP-weighted time to fission
- `ifp-prompt-time-numerator`: IFP-weighted prompt time to fission
- `ifp-denominator`: IFP normalization factor
- `ifp-prompt-denominator`: IFP prompt normalization factor

### Internal Tallies

When `calculate_alpha = True`, OpenMC automatically creates an internal tally with:
- `ifp-time-numerator`
- `ifp-prompt-time-numerator`
- `ifp-denominator`
- `ifp-prompt-denominator`

These tallies are managed internally and do not need to be created by the user.

## Tips for Accurate Results

1. **Use sufficient particles**: Alpha calculations require good statistics. Use at least 10,000 particles per batch.

2. **Allow source convergence**: Use enough inactive batches (typically 50+) to ensure the fission source has converged.

3. **Run enough active batches**: More batches reduce statistical uncertainty. 100+ active batches recommended.

4. **Check uncertainties**: Always examine the reported uncertainties to ensure results are statistically meaningful.

5. **Validate with benchmarks**: Compare results against known benchmarks (like Godiva) to verify your methodology.

## XML Configuration

If you prefer to configure via XML directly:

```xml
<?xml version='1.0' encoding='utf-8'?>
<settings>
  <run_mode>eigenvalue</run_mode>
  <particles>10000</particles>
  <batches>150</batches>
  <inactive>50</inactive>
  <calculate_alpha>true</calculate_alpha>
  <calculate_prompt_k>true</calculate_prompt_k>
</settings>
```

## See Also

- `openmc.Settings` - Settings class documentation
- `openmc.StatePoint` - StatePoint class for reading results
- `examples/` directory for additional examples
