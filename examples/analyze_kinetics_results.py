"""
Analyze kinetics results from an OpenMC eigenvalue simulation.

Displays:
- k-effective and k-prompt
- Effective delayed neutron fraction (beta_eff)
- IFP-weighted effective generation time (Lambda_eff)
- IFP-weighted alpha eigenvalues: α_dc and α (static)
"""

import openmc
import warnings

# Suppress the cross sections path warning
warnings.filterwarnings('ignore', message="Path.*does not exist", category=UserWarning)

sp = openmc.StatePoint('statepoint.150.h5')

# Convert units for fast neutron systems
# StatePoint stores values in SI units (seconds), convert to microseconds for display
gen_time_us = sp.lambda_eff_ifp.nominal_value * 1e6 if sp.lambda_eff_ifp else 0.0
gen_time_std_us = sp.lambda_eff_ifp.std_dev * 1e6 if sp.lambda_eff_ifp else 0.0

alpha_dc_us = sp.alpha_dc_ifp.nominal_value / 1e6 if sp.alpha_dc_ifp else 0.0
alpha_dc_std_us = sp.alpha_dc_ifp.std_dev / 1e6 if sp.alpha_dc_ifp else 0.0

alpha_us = sp.alpha_ifp.nominal_value / 1e6 if sp.alpha_ifp else 0.0
alpha_std_us = sp.alpha_ifp.std_dev / 1e6 if sp.alpha_ifp else 0.0

print("\nResults:")
print("=" * 70)
print(f"k-effective:              {sp.keff}")
print(f"k-prompt:                 {sp.k_prompt}")
print(f"Beta-effective:           {sp.beta_eff}")
print(f"Lambda-effective (IFP):   {gen_time_us:.6e}+/-{gen_time_std_us:.6e} us")
print(f"Alpha (Delayed Critical): {alpha_dc_us:.6e}+/-{alpha_dc_std_us:.6e} 1/us")
print(f"Alpha (Static):           {alpha_us:.6e}+/-{alpha_std_us:.6e} 1/us")

# Expected results for Godiva (from Cullen et al. 2003):
print("\nExpected values for Godiva (UCRL-TR-201506):")
print("  k_eff ≈ 1.0 (near critical)")
print("  beta_eff ≈ 0.0065-0.0070 (0.65-0.70%)")
print("  k_prompt ≈ 0.993-0.994")
print("  Lambda_eff ≈ 5-10 ns for bare fast systems")
print("  Alpha = (k - 1) / Lambda_eff")
