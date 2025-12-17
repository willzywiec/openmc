#!/usr/bin/env python3
"""
Alpha Eigenvalue Batch Runner for ICSBEP Benchmarks
====================================================
Runs ICSBEP benchmarks matching the examples/alpha folder with alpha eigenvalue
calculations enabled. Saves all results (alpha, keff, k-prompt, beta-effective,
prompt neutron lifetime, generation time derived, generation time direct) to a
single .xlsx file.

Generation time is measured two ways:
  - Derived: Λ = ℓ/k (from lifetime and k-effective)
  - Direct: Birth-to-fission time weighted by ν (neutrons produced)

The alpha eigenvalue uses the direct generation time: α = (k - 1) / Λ

Usage:
    python batch.py              # Run all benchmarks
    python batch.py --dry-run    # List benchmarks without running
    python batch.py --quick      # Quick run with fewer particles
"""

import os
import sys
import shutil
import subprocess
import time
import xml.etree.ElementTree as ET
from pathlib import Path
from datetime import datetime

# Mapping of alpha example names to ICSBEP benchmark paths
# Format: (short_name, icsbep_path_relative_to_icsbep_dir)
BENCHMARK_MAP = [
    ("hmf001", "heu-met-fast-001/openmc/case-1"),
    ("hmf028", "heu-met-fast-028/openmc"),
    ("hmi006-1", "heu-met-inter-006/openmc/case-1"),
    ("imf007-4", "ieu-met-fast-007/openmc/case-4"),
    ("imf010-1", "ieu-met-fast-010/openmc"),
    ("lst001-1", "leu-sol-therm-001/openmc"),
    ("pmf001", "pu-met-fast-001/openmc"),
    ("pmf008-1", "pu-met-fast-008/openmc/case-1"),
    ("pmi002", "pu-met-inter-002/openmc"),
    ("umf001-1", "u233-met-fast-001/openmc"),
    ("umf006-1", "u233-met-fast-006/openmc"),
]


def get_script_dir():
    """Get the directory containing this script."""
    return Path(__file__).parent.absolute()


def get_icsbep_dir():
    """Get the icsbep directory path."""
    return get_script_dir().parent / "icsbep"


def fix_materials(materials_path: Path):
    """
    Fix materials.xml to replace problematic nuclide names.

    Replaces:
    - C0 (natural carbon) with C12/C13 at natural abundances (98.93%/1.07%)
    - Other X0 nuclides that may not be in the library
    """
    tree = ET.parse(materials_path)
    root = tree.getroot()

    # Natural abundances for carbon
    C12_FRAC = 0.9893
    C13_FRAC = 0.0107

    modified = False

    for material in root.findall('.//material'):
        nuclides_to_remove = []
        nuclides_to_add = []

        for nuclide in material.findall('nuclide'):
            name = nuclide.get('name')
            ao = nuclide.get('ao')

            if name == 'C0':
                # Replace C0 with C12 and C13
                nuclides_to_remove.append(nuclide)
                ao_val = float(ao)
                nuclides_to_add.append(('C12', ao_val * C12_FRAC))
                nuclides_to_add.append(('C13', ao_val * C13_FRAC))
                modified = True

        # Remove old nuclides
        for nuclide in nuclides_to_remove:
            material.remove(nuclide)

        # Add new nuclides
        for name, ao_val in nuclides_to_add:
            new_nuclide = ET.SubElement(material, 'nuclide')
            new_nuclide.set('ao', str(ao_val))
            new_nuclide.set('name', name)

    if modified:
        tree.write(materials_path, xml_declaration=True, encoding='utf-8')
        return True
    return False


def modify_settings_for_alpha(settings_path: Path, quick_mode: bool = False):
    """
    Modify settings.xml to enable alpha eigenvalue calculation.

    Sets:
    - calculate_alpha = true (under <kinetics> element)
    - calculate_prompt_k = true (automatically enabled by calculate_alpha)
    - Optionally reduces particles/batches for quick mode
    """
    tree = ET.parse(settings_path)
    root = tree.getroot()

    # Find or create kinetics element (required by OpenMC C++ code)
    kinetics = root.find('kinetics')
    if kinetics is None:
        kinetics = ET.SubElement(root, 'kinetics')

    # Add or update calculate_alpha under kinetics
    calc_alpha = kinetics.find('calculate_alpha')
    if calc_alpha is None:
        calc_alpha = ET.SubElement(kinetics, 'calculate_alpha')
    calc_alpha.text = 'true'

    # Add or update calculate_prompt_k under kinetics
    calc_prompt_k = kinetics.find('calculate_prompt_k')
    if calc_prompt_k is None:
        calc_prompt_k = ET.SubElement(kinetics, 'calculate_prompt_k')
    calc_prompt_k.text = 'true'

    if quick_mode:
        # Reduce particles and batches for quick testing
        particles = root.find('particles')
        if particles is not None:
            particles.text = '5000'

        batches = root.find('batches')
        if batches is not None:
            batches.text = '50'

        inactive = root.find('inactive')
        if inactive is not None:
            inactive.text = '10'

    tree.write(settings_path, xml_declaration=True, encoding='utf-8')
    print(f"  Enabled: calculate_alpha = true")


def setup_benchmark(name: str, icsbep_path: str, run_dir: Path, quick_mode: bool = False) -> bool:
    """
    Set up a benchmark run directory by copying XML files and modifying settings.

    Returns True if successful, False otherwise.
    """
    icsbep_dir = get_icsbep_dir()
    source_dir = icsbep_dir / icsbep_path

    if not source_dir.exists():
        print(f"  Warning: Source directory not found: {source_dir}")
        return False

    # Create run directory
    run_dir.mkdir(parents=True, exist_ok=True)

    # Copy XML files
    for xml_file in ['materials.xml', 'geometry.xml', 'settings.xml']:
        src = source_dir / xml_file
        dst = run_dir / xml_file
        if src.exists():
            shutil.copy2(src, dst)
        else:
            print(f"  Warning: Missing {xml_file} in {source_dir}")
            return False

    # Fix materials (replace C0 with C12/C13, etc.)
    materials_path = run_dir / 'materials.xml'
    if fix_materials(materials_path):
        print(f"  Fixed materials.xml (replaced C0 with C12/C13)")

    # Modify settings for alpha calculation
    settings_path = run_dir / 'settings.xml'
    modify_settings_for_alpha(settings_path, quick_mode)

    return True


def run_benchmark(name: str, run_dir: Path) -> dict:
    """
    Run OpenMC for a single benchmark.

    Returns dict with results.
    """
    result = {
        "benchmark": name,
        "success": False,
        "runtime": 0.0,
        "error": None,
        "keff": None,
        "keff_unc": None,
        "k_prompt": None,
        "k_prompt_unc": None,
        "alpha": None,
        "alpha_unc": None,
        "beta_eff": None,
        "beta_eff_unc": None,
        "lifetime": None,
        "lifetime_unc": None,
        "gen_time": None,
        "gen_time_unc": None,
        "gen_time_direct": None,
        "gen_time_direct_unc": None,
    }

    start_time = time.time()

    try:
        # Run OpenMC
        proc = subprocess.run(
            ['openmc'],
            cwd=str(run_dir),
            capture_output=True,
            text=True
        )

        result["runtime"] = time.time() - start_time

        if proc.returncode == 0:
            result["success"] = True

            # Extract results from statepoint
            extracted = extract_results(run_dir, name)
            result.update(extracted)

        else:
            result["error"] = proc.stderr if proc.stderr else proc.stdout

            # Write error log
            error_file = run_dir / f"{name}_error.log"
            with open(error_file, 'w') as f:
                f.write(f"=== STDOUT ===\n{proc.stdout}\n")
                f.write(f"=== STDERR ===\n{proc.stderr}\n")

    except Exception as e:
        result["runtime"] = time.time() - start_time
        result["error"] = str(e)

    return result


def extract_results(run_dir: Path, name: str) -> dict:
    """
    Extract kinetics parameters from the statepoint file.
    """
    results = {}

    # Find statepoint file
    statepoints = sorted(run_dir.glob("statepoint.*.h5"))
    if not statepoints:
        return results

    sp_file = statepoints[-1]

    try:
        import openmc
        sp = openmc.StatePoint(str(sp_file))

        # k-effective
        if hasattr(sp, 'keff') and sp.keff is not None:
            results["keff"] = sp.keff.nominal_value
            results["keff_unc"] = sp.keff.std_dev

        # Prompt k-effective
        if hasattr(sp, 'k_prompt') and sp.k_prompt is not None:
            results["k_prompt"] = sp.k_prompt.nominal_value
            results["k_prompt_unc"] = sp.k_prompt.std_dev

        # Beta effective
        if hasattr(sp, 'beta_eff') and sp.beta_eff is not None:
            results["beta_eff"] = sp.beta_eff.nominal_value
            results["beta_eff_unc"] = sp.beta_eff.std_dev

        # Prompt neutron lifetime
        if hasattr(sp, 'prompt_lifetime') and sp.prompt_lifetime is not None:
            results["lifetime"] = sp.prompt_lifetime.nominal_value
            results["lifetime_unc"] = sp.prompt_lifetime.std_dev

        # Prompt generation time (derived from lifetime)
        if hasattr(sp, 'prompt_gen_time') and sp.prompt_gen_time is not None:
            results["gen_time"] = sp.prompt_gen_time.nominal_value
            results["gen_time_unc"] = sp.prompt_gen_time.std_dev

        # Prompt generation time (direct measurement)
        if hasattr(sp, 'prompt_gen_time_direct') and sp.prompt_gen_time_direct is not None:
            results["gen_time_direct"] = sp.prompt_gen_time_direct.nominal_value
            results["gen_time_direct_unc"] = sp.prompt_gen_time_direct.std_dev

        # Alpha eigenvalue
        if hasattr(sp, 'alpha_k_based') and sp.alpha_k_based is not None:
            results["alpha"] = sp.alpha_k_based.nominal_value
            results["alpha_unc"] = sp.alpha_k_based.std_dev

    except Exception as e:
        print(f"  Warning: Could not read statepoint: {e}")

    return results


def write_results_xlsx(results: list, output_file: Path):
    """Write all results to an Excel file."""
    try:
        import openpyxl
        from openpyxl.styles import Font, Alignment, Border, Side, PatternFill
    except ImportError:
        print("Warning: openpyxl not installed. Installing...")
        subprocess.run([sys.executable, '-m', 'pip', 'install', 'openpyxl'], check=True)
        import openpyxl
        from openpyxl.styles import Font, Alignment, Border, Side, PatternFill

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Alpha Eigenvalue Results"

    # Define styles
    header_font = Font(bold=True)
    header_fill = PatternFill(start_color="CCCCCC", end_color="CCCCCC", fill_type="solid")
    thin_border = Border(
        left=Side(style='thin'),
        right=Side(style='thin'),
        top=Side(style='thin'),
        bottom=Side(style='thin')
    )

    # Headers
    headers = [
        "Benchmark",
        "k-eff", "k-eff unc",
        "k-prompt", "k-prompt unc",
        "Alpha (1/s)", "Alpha unc",
        "Beta-eff", "Beta-eff unc",
        "Lifetime (s)", "Lifetime unc",
        "Gen Time Derived (s)", "Gen Time Derived unc",
        "Gen Time Direct (s)", "Gen Time Direct unc",
        "Runtime (s)", "Status"
    ]

    for col, header in enumerate(headers, 1):
        cell = ws.cell(row=1, column=col, value=header)
        cell.font = header_font
        cell.fill = header_fill
        cell.border = thin_border
        cell.alignment = Alignment(horizontal='center')

    # Data rows
    for row_idx, r in enumerate(results, 2):
        data = [
            r.get("benchmark", ""),
            r.get("keff"),
            r.get("keff_unc"),
            r.get("k_prompt"),
            r.get("k_prompt_unc"),
            r.get("alpha"),
            r.get("alpha_unc"),
            r.get("beta_eff"),
            r.get("beta_eff_unc"),
            r.get("lifetime"),
            r.get("lifetime_unc"),
            r.get("gen_time"),
            r.get("gen_time_unc"),
            r.get("gen_time_direct"),
            r.get("gen_time_direct_unc"),
            r.get("runtime"),
            "OK" if r.get("success") else "FAILED"
        ]

        for col, value in enumerate(data, 1):
            cell = ws.cell(row=row_idx, column=col, value=value)
            cell.border = thin_border

            # Format numbers
            if isinstance(value, float):
                # Alpha, lifetime, gen time (derived), gen time (direct) - scientific notation
                if col in [6, 7, 10, 11, 12, 13, 14, 15]:
                    cell.number_format = '0.00E+00'
                else:
                    cell.number_format = '0.000000'

    # Adjust column widths
    column_widths = [15, 12, 12, 12, 12, 14, 14, 12, 12, 14, 14, 14, 14, 14, 14, 12, 10]
    for col, width in enumerate(column_widths, 1):
        ws.column_dimensions[openpyxl.utils.get_column_letter(col)].width = width

    # Add summary section
    ws_summary = wb.create_sheet("Summary")
    ws_summary['A1'] = "Alpha Eigenvalue Benchmark Results"
    ws_summary['A1'].font = Font(bold=True, size=14)

    ws_summary['A3'] = "Generated:"
    ws_summary['B3'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    successful = sum(1 for r in results if r.get("success"))
    ws_summary['A4'] = "Total benchmarks:"
    ws_summary['B4'] = len(results)
    ws_summary['A5'] = "Successful:"
    ws_summary['B5'] = successful
    ws_summary['A6'] = "Failed:"
    ws_summary['B6'] = len(results) - successful
    ws_summary['A7'] = "Total runtime:"
    ws_summary['B7'] = f"{sum(r.get('runtime', 0) for r in results):.1f} s"

    wb.save(output_file)


def run_all_benchmarks(dry_run: bool = False, quick_mode: bool = False):
    """Run all ICSBEP benchmarks with alpha eigenvalue calculations."""
    script_dir = get_script_dir()
    icsbep_dir = get_icsbep_dir()

    print("=" * 70)
    print("Alpha Eigenvalue Batch Runner for ICSBEP Benchmarks")
    print("=" * 70)
    print(f"Script directory: {script_dir}")
    print(f"ICSBEP directory: {icsbep_dir}")
    print(f"Mode: {'DRY RUN' if dry_run else ('QUICK' if quick_mode else 'FULL')}")
    print()

    # Check which benchmarks exist
    available_benchmarks = []
    for name, path in BENCHMARK_MAP:
        full_path = icsbep_dir / path
        if full_path.exists():
            available_benchmarks.append((name, path))
            print(f"  [OK] {name}: {path}")
        else:
            print(f"  [--] {name}: {path} (not found)")

    print(f"\nFound {len(available_benchmarks)} available benchmark(s)")

    if dry_run:
        print("\n[DRY RUN - not executing]")
        return

    # Create output directory
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = script_dir / f"runs_{timestamp}"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"\nOutput directory: {output_dir}")
    print(f"Starting batch run at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    results = []
    total_start = time.time()

    for i, (name, icsbep_path) in enumerate(available_benchmarks, 1):
        print(f"\n{'='*70}")
        print(f"[{i}/{len(available_benchmarks)}] Running: {name}")
        print(f"{'='*70}")

        run_dir = output_dir / name

        # Set up benchmark
        if not setup_benchmark(name, icsbep_path, run_dir, quick_mode):
            results.append({
                "benchmark": name,
                "success": False,
                "error": "Failed to set up benchmark",
                "runtime": 0.0
            })
            continue

        # Run benchmark
        result = run_benchmark(name, run_dir)
        results.append(result)

        # Print results
        if result["success"]:
            print(f"  Completed in {result['runtime']:.1f}s")
            # Always show all parameters
            keff = f"{result['keff']:.6f} +/- {result['keff_unc']:.6f}" if result.get("keff") else "N/A"
            k_prompt = f"{result['k_prompt']:.6f} +/- {result['k_prompt_unc']:.6f}" if result.get("k_prompt") else "N/A"
            alpha = f"{result['alpha']:.4e} +/- {result['alpha_unc']:.4e} 1/s" if result.get("alpha") else "N/A"
            beta_eff = f"{result['beta_eff']:.6f} +/- {result['beta_eff_unc']:.6f}" if result.get("beta_eff") else "N/A"
            lifetime = f"{result['lifetime']:.4e} +/- {result['lifetime_unc']:.4e} s" if result.get("lifetime") else "N/A"
            gen_time = f"{result['gen_time']:.4e} +/- {result['gen_time_unc']:.4e} s" if result.get("gen_time") else "N/A"
            gen_time_direct = f"{result['gen_time_direct']:.4e} +/- {result['gen_time_direct_unc']:.4e} s" if result.get("gen_time_direct") else "N/A"

            print(f"  k-eff                = {keff}")
            print(f"  k-prompt             = {k_prompt}")
            print(f"  alpha                = {alpha}")
            print(f"  beta-eff             = {beta_eff}")
            print(f"  prompt lifetime      = {lifetime}")
            print(f"  gen time (derived)   = {gen_time}")
            print(f"  gen time (direct)    = {gen_time_direct}")

            # Warn if kinetics parameters are missing
            if not result.get("k_prompt"):
                print("  WARNING: Kinetics parameters not found - check that OpenMC was built with alpha eigenvalue support")
        else:
            print(f"  FAILED: {result.get('error', 'Unknown error')[:200]}")

    total_time = time.time() - total_start

    # Write results to xlsx
    xlsx_file = output_dir / "alpha_results.xlsx"
    write_results_xlsx(results, xlsx_file)

    # Summary
    print("\n")
    print("=" * 70)
    print("BATCH RUN COMPLETE")
    print("=" * 70)

    successful = [r for r in results if r.get("success")]
    failed = [r for r in results if not r.get("success")]

    print(f"Total benchmarks:  {len(results)}")
    print(f"Successful:        {len(successful)}")
    print(f"Failed:            {len(failed)}")
    print(f"Total runtime:     {total_time:.1f}s")
    print()
    print(f"Results file:      {xlsx_file}")

    if failed:
        print(f"\nFailed benchmarks:")
        for r in failed:
            print(f"  - {r['benchmark']}")

    return results


if __name__ == "__main__":
    dry_run = "--dry-run" in sys.argv
    quick_mode = "--quick" in sys.argv

    if "--help" in sys.argv or "-h" in sys.argv:
        print(__doc__)
        sys.exit(0)

    run_all_benchmarks(dry_run=dry_run, quick_mode=quick_mode)
