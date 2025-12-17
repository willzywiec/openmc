# Alpha Eigenvalue Calculations in OpenMC

This guide explains how to use OpenMC's alpha eigenvalue calculation capability for reactor kinetics analysis.

## Overview

The alpha eigenvalue (α) describes the time-dependent behavior of the prompt neutron population in a nuclear system. It is calculated using the formula:

```
α = (k_prompt - 1) / l_prompt
```

Where:
- **k_prompt**: Prompt multiplication factor (excluding delayed neutrons)
- **l_prompt**: Prompt neutron generation time (lifetime)

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
print(f"Prompt lifetime:       {sp.prompt_gen_time} seconds")
print(f"Alpha eigenvalue:      {sp.alpha_k_based} 1/seconds")
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

# Prompt neutron generation time (in seconds)
lifetime = sp.prompt_gen_time
print(f"l-prompt = {lifetime.nominal_value:.3e} +/- {lifetime.std_dev:.3e} s")

# Alpha eigenvalue (in 1/seconds)
alpha = sp.alpha_k_based
print(f"alpha = {alpha.nominal_value:.3e} +/- {alpha.std_dev:.3e} 1/s")

# Alternative name for alpha (same value)
alpha_static = sp.alpha_static
```

### Converting Units

Alpha eigenvalue is often reported in different units:

```python
sp = openmc.StatePoint('statepoint.150.h5')

# Alpha in 1/seconds (default)
alpha_per_sec = sp.alpha_k_based.nominal_value

# Alpha in generations per microsecond
alpha_per_us = alpha_per_sec / 1e6

# Alpha in generations per millisecond
alpha_per_ms = alpha_per_sec / 1e3

# Prompt lifetime in microseconds
lifetime_us = sp.prompt_gen_time.nominal_value * 1e6

print(f"Alpha: {alpha_per_us:.4f} gen/us")
print(f"Prompt lifetime: {lifetime_us:.2f} us")
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
print(f"Prompt lifetime:    {sp.prompt_gen_time.nominal_value*1e9:.2f} +/- {sp.prompt_gen_time.std_dev*1e9:.2f} ns")
print(f"Alpha eigenvalue:   {sp.alpha_k_based.nominal_value/1e6:.4f} +/- {sp.alpha_k_based.std_dev/1e6:.4f} gen/us")
```

## Output Format

When running OpenMC with alpha calculations enabled, the output will include a kinetics parameters section:

```
 ====================>     DELAYED NEUTRON KINETICS     <====================

 Delayed Neutron Kinetics Parameters:
  k-effective                = 1.00012 +/- 0.00045
  k-prompt                   = 0.99312 +/- 0.00044
  Beta-effective             = 0.00700 +/- 0.00012
  Prompt Neutron Lifetime    = 5.66000e-09 +/- 2.50000e-11 seconds
  Alpha Eigenvalue           = -1.21500e+06 +/- 1.80000e+04 1/seconds
```

## Internal Tallies

When `calculate_alpha = True`, OpenMC automatically creates internal tallies to track:

- `prompt-chain-gen-time-num`: Numerator for lifetime calculation (Σ lifetime × weight)
- `prompt-chain-gen-time-denom`: Denominator for lifetime calculation (Σ weight)
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
