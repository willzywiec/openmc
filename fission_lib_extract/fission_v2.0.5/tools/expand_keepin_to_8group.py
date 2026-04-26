#!/usr/bin/env python3
"""
Spriggs NNLS expansion: convert Keepin/Brady-England 6-group fast-fission
parameters to the Spriggs 8-group consistent half-life basis.

Method: G.D. Spriggs, J.M. Campbell, V.M. Piksaikin,
  "An 8-group delayed neutron model based on a consistent set of half-lives",
  Progress in Nuclear Energy 41(1-4), 223-251 (2002).

The 6-group decay curve f(t) = sum a_i * exp(-lambda_i * t) is re-expressed
in the 8-group fixed-lambda basis using non-negative least squares (NNLS) on
a 200-point log-spaced time grid from 0.001 to 300 s, with a normalization
constraint row appended at high weight.  Mean half-life is conserved to
< 0.02%; RMS curve error < 0.025% for all isotopes.

Usage:
  python3 expand_keepin_to_8group.py

Output:
  C array initializers for pasting into keepin_table[] in SmpDelayed.cc.

Dependencies: numpy, scipy  (pip install numpy scipy)
"""
import numpy as np
from scipy.optimize import nnls

# Spriggs 8-group fixed half-lives (seconds) and lambda values (s^-1)
T8 = np.array([55.6, 24.5, 16.3, 5.21, 2.37, 1.04, 0.424, 0.195])
L8 = np.log(2) / T8

DATASETS = [
    # (ZA, label, ftype, nu_d, [a_i x 6], [lambda_i x 6])
    (92233, "U-233  fast  Keepin-1965",   1, 0.00733,
     [0.0860, 0.2740, 0.2270, 0.3170, 0.0730, 0.0230],
     [0.01260, 0.03370, 0.13900, 0.32500, 1.13000, 2.50000]),
    (92235, "U-235  fast  Keepin-1965",   1, 0.01585,
     [0.0330, 0.2190, 0.1960, 0.3950, 0.1150, 0.0420],
     [0.01240, 0.03050, 0.11100, 0.30100, 1.14000, 3.01000]),
    (92238, "U-238  fast  Brady-England", 1, 0.04300,
     [0.0130, 0.1370, 0.1620, 0.3880, 0.2250, 0.0750],
     [0.01320, 0.03210, 0.13900, 0.35800, 1.41600, 4.02000]),
    (94239, "Pu-239 fast  Keepin-1965",   1, 0.00622,
     [0.0350, 0.2980, 0.2110, 0.3260, 0.0930, 0.0370],
     [0.01290, 0.03110, 0.13400, 0.33100, 1.26000, 3.21000]),
    (94241, "Pu-241 fast  Brady-England", 1, 0.01600,
     [0.0100, 0.2290, 0.1730, 0.3900, 0.1480, 0.0500],
     [0.01282, 0.02990, 0.12400, 0.35200, 1.61000, 3.47000]),
    (98252, "Cf-252 SF    literature",    0, 0.00978,
     [0.0200, 0.1920, 0.2330, 0.3410, 0.1580, 0.0560],
     [0.01330, 0.03250, 0.12400, 0.34800, 1.38000, 3.97000]),
]


def expand(a6, lam6):
    a6, lam6 = np.array(a6), np.array(lam6)
    t = np.logspace(-3, np.log10(300), 200)
    f = (a6 * np.exp(-lam6[:, None] * t[None, :])).sum(axis=0)
    B = np.exp(-L8[:, None] * t[None, :]).T
    w = 200.0
    B = np.vstack([B, np.ones((1, 8)) * w])
    f = np.append(f, w)
    A8, _ = nnls(B, f)
    A8 /= A8.sum()
    t_chk = np.logspace(-3, np.log10(300), 1000)
    f6 = (a6 * np.exp(-lam6[:, None] * t_chk[None, :])).sum(axis=0)
    f8 = (A8  * np.exp(-L8[:, None]  * t_chk[None, :])).sum(axis=0)
    rms = np.sqrt(np.mean((f8 - f6) ** 2)) / f6.max() * 100
    T6m = (a6  * np.log(2) / lam6).sum()
    T8m = (A8  * T8).sum()
    return A8, T6m, T8m, rms


print("/* Spriggs 8-group NNLS expansion of Keepin/Brady-England 6-group data */")
print(f"/* Fixed lambda: {', '.join(f'{l:.6f}' for l in L8)} */")
print()
for (za, label, ft, nu_d, a6, lam6) in DATASETS:
    A8, T6m, T8m, rms = expand(a6, lam6)
    a_str = ', '.join(f'{x:.4f}' for x in A8)
    print(f"   /* {label}  nu_d={nu_d}  T_mean={T8m:.2f}s  RMS={rms:.3f}% */")
    print(f"   {{ {za}, {ft}, {nu_d},")
    print(f"     {{{a_str}}} }},")
    print()
