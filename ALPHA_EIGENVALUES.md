# Alpha Eigenvalue Calculations in OpenMC

This guide explains how to use OpenMC's alpha eigenvalue calculation capability for reactor kinetics analysis.

## Overview

The alpha eigenvalue (α) describes the time-dependent behavior of the neutron population in a nuclear system. OpenMC calculates two alpha values using different methods:

### Static Method (alpha_static)

The static alpha is calculated from the inhour equation:

```
α_static = (ρ - β_eff) / Λ
```

Where:
- **ρ**: Reactivity, ρ = (k - 1) / k
- **β_eff**: Effective delayed neutron fraction
- **Λ**: Mean generation time (mean time from neutron birth to fission)

### Griesheimer Method (alpha_griesheimer)

The Griesheimer alpha uses the same formula:

```
α_griesheimer = (ρ - β_eff) / Λ
```

The difference is the **methodology**, not the formula:
- **Static**: Derive α directly from k-eigenvalue results
- **Griesheimer**: Iteratively add pseudo-absorption α/v to cross sections until k→1

Both methods should converge to the same value.

### Physical Interpretation

| Alpha Value | System State | Behavior |
|-------------|--------------|----------|
| α > 0 | Supercritical | Prompt neutron population growing exponentially |
| α = 0 | Critical | Prompt neutron population stable |
| α < 0 | Subcritical | Prompt neutron population decaying exponentially |

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

# Note: calculate_alpha automatically enables calculate_prompt_k
settings.export_to_xml()

# Run OpenMC
openmc.run()

# Read results from statepoint file
sp = openmc.StatePoint('statepoint.150.h5')

# Access kinetics parameters
print(f"k-effective:           {sp.keff}")
print(f"k-prompt:              {sp.k_prompt}")
print(f"Beta-effective:        {sp.beta_eff}")
print(f"Mean generation time:  {sp.mean_generation_time} seconds")
print(f"Alpha (static):        {sp.alpha_static} 1/seconds")
print(f"Alpha (Griesheimer):   {sp.alpha_griesheimer} 1/seconds")
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

# Mean generation time (in seconds)
gen_time = sp.mean_generation_time
print(f"Λ = {gen_time.nominal_value:.3e} +/- {gen_time.std_dev:.3e} s")

# Alpha eigenvalues (in 1/seconds)
alpha_s = sp.alpha_static
print(f"alpha (static) = {alpha_s.nominal_value:.3e} +/- {alpha_s.std_dev:.3e} 1/s")
alpha_g = sp.alpha_griesheimer
print(f"alpha (Griesheimer) = {alpha_g.nominal_value:.3e} +/- {alpha_g.std_dev:.3e} 1/s")
```

### Converting Units

Alpha eigenvalue is often reported in different units:

```python
sp = openmc.StatePoint('statepoint.150.h5')

# Alpha (static) in 1/seconds (default)
alpha_per_sec = sp.alpha_static.nominal_value

# Alpha in generations per microsecond
alpha_per_us = alpha_per_sec / 1e6

# Alpha in generations per millisecond
alpha_per_ms = alpha_per_sec / 1e3

# Mean generation time in microseconds
gen_time_us = sp.mean_generation_time.nominal_value * 1e6

print(f"Alpha (static): {alpha_per_us:.4f} gen/us")
print(f"Mean generation time: {gen_time_us:.2f} us")
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
print(f"k-effective:        {sp.keff.nominal_value:.5f} +/- {sp.keff.std_dev:.5f}")
print(f"k-prompt:           {sp.k_prompt.nominal_value:.5f} +/- {sp.k_prompt.std_dev:.5f}")
print(f"Beta-effective:     {sp.beta_eff.nominal_value:.5f} +/- {sp.beta_eff.std_dev:.5f}")
print(f"Mean gen time:      {sp.mean_generation_time.nominal_value*1e9:.2f} +/- {sp.mean_generation_time.std_dev*1e9:.2f} ns")
print(f"Alpha (static):     {sp.alpha_static.nominal_value/1e6:.4f} +/- {sp.alpha_static.std_dev/1e6:.4f} gen/us")
print(f"Alpha (Griesheimer):{sp.alpha_griesheimer.nominal_value/1e6:.4f} +/- {sp.alpha_griesheimer.std_dev/1e6:.4f} gen/us")
```

## Output Format

When running OpenMC with alpha calculations enabled, the output will include a kinetics parameters section:

```
 ====================>     RESULTS     <====================

  k-effective (Combined)      = 1.00012 +/- 0.00045
  k-prompt                    = 0.99312 +/- 0.00044
  Beta-effective              = 0.00700 +/- 0.00012
  Mean Generation Time        = 5.70000e-09 +/- 2.50000e-11 seconds
  Alpha (static)              = -1.21500e+06 +/- 1.80000e+04 1/seconds
  Alpha (Griesheimer)         = -1.21500e+06 +/- 1.80000e+04 1/seconds
```

Note: Both alpha values are the same since they use the same formula.

## Internal Tallies

When `calculate_alpha = True`, OpenMC automatically creates internal tallies to track:

- `prompt-chain-fission-time-num`: Numerator for mean generation time (Σ time × ν × weight at fission)
- `prompt-chain-fission-time-denom`: Denominator for mean generation time (Σ ν × weight at fission)
- `prompt-chain-nu-fission-rate`: Fission production rate (diagnostic)
- `prompt-chain-absorption-rate`: Absorption rate (diagnostic)
- `prompt-chain-leakage-rate`: Leakage rate (diagnostic)
- `prompt-chain-population`: Neutron population (diagnostic)

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
