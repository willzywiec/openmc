"""
Analyze kinetics results from an OpenMC eigenvalue simulation.

Displays:
- k-effective and k-prompt
- Effective delayed neutron fraction (beta_eff)
- Prompt neutron lifetime (ℓ): time from birth to absorption/leakage
- Mean generation time (Λ): time from birth to causing fission
- Alpha eigenvalue: α = (ρ - β_eff) / Λ
"""

import openmc
import warnings

# Suppress the cross sections path warning
warnings.filterwarnings('ignore', message="Path.*does not exist", category=UserWarning)

sp = openmc.StatePoint('statepoint.150.h5')

# Convert units for fast neutron systems
# StatePoint stores values in SI units (seconds), convert to microseconds for display
lifetime_us = sp.prompt_neutron_lifetime.nominal_value * 1e6 if sp.prompt_neutron_lifetime else 0.0
lifetime_std_us = sp.prompt_neutron_lifetime.std_dev * 1e6 if sp.prompt_neutron_lifetime else 0.0

gen_time_us = sp.mean_generation_time.nominal_value * 1e6 if sp.mean_generation_time else 0.0
gen_time_std_us = sp.mean_generation_time.std_dev * 1e6 if sp.mean_generation_time else 0.0

alpha_us = sp.alpha.nominal_value / 1e6 if sp.alpha else 0.0
alpha_std_us = sp.alpha.std_dev / 1e6 if sp.alpha else 0.0

print("\nResults:")
print("=" * 70)
print(f"k-effective:              {sp.keff}")
print(f"k-prompt:                 {sp.k_prompt}")
print(f"Beta-effective:           {sp.beta_eff}")
print(f"Prompt neutron lifetime:  {lifetime_us:.6e}+/-{lifetime_std_us:.6e} us")
print(f"Mean generation time:     {gen_time_us:.6e}+/-{gen_time_std_us:.6e} us")
print(f"Alpha:                    {alpha_us:.6e}+/-{alpha_std_us:.6e} 1/us")

# Expected results for Godiva (from Cullen et al. 2003):
print("\nExpected values for Godiva (UCRL-TR-201506):")
print("  k_eff ≈ 1.0 (near critical)")
print("  beta_eff ≈ 0.0065-0.0070 (0.65-0.70%)")
print("  k_prompt ≈ 0.993-0.994")
print("  Prompt neutron lifetime ≈ 5-10 ns (5e-3 to 1e-2 us for fast systems)")
print("  Mean generation time ≈ similar for bare systems, different for reflected")
print("  Alpha = (rho - beta_eff) / Lambda")
