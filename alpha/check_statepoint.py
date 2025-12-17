#!/usr/bin/env python3
"""Check statepoint for alpha_rate_based field."""
import sys
import h5py

if len(sys.argv) < 2:
    print("Usage: python check_statepoint.py <statepoint.h5>")
    sys.exit(1)

sp_file = sys.argv[1]
print(f"Checking {sp_file}...")

with h5py.File(sp_file, 'r') as f:
    print("\nAlpha-related fields in statepoint:")
    for key in f.keys():
        if 'alpha' in key.lower() or 'prompt' in key.lower() or 'lifetime' in key.lower():
            try:
                val = f[key][()]
                print(f"  {key}: {val}")
            except:
                print(f"  {key}: (group)")

    # Check specifically for alpha_rate_based
    if 'alpha_rate_based' in f:
        val = f['alpha_rate_based'][()]
        print(f"\nalpha_rate_based found: {val}")
    else:
        print("\nalpha_rate_based NOT FOUND in statepoint!")
        print("\nAll root keys:")
        for key in f.keys():
            print(f"  {key}")
