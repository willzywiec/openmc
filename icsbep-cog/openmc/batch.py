#!/usr/bin/env python3
"""
Batch runner for OpenMC ICSBEP benchmarks with results collection.

This script runs all OpenMC model.py files in the benchmark directories,
collects k-effective and point kinetics results, and exports to Excel.

Usage:
    python batch.py                    # Generate XML files only (default)
    python batch.py --run              # Generate XML and run OpenMC
    python batch.py --run --parallel 4 # Run with 4 parallel processes
    python batch.py --category pu      # Run only plutonium benchmarks
    python batch.py --benchmark pmf001 # Run specific benchmark
    python batch.py --list             # List all available benchmarks
    python batch.py --run --output results.xlsx  # Specify output file

Results are saved to 'benchmark_results.xlsx' by default.
"""

import os
import sys
import subprocess
import argparse
import time
import re
import json
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor, as_completed
from dataclasses import dataclass, field, asdict
from typing import Optional, List, Dict, Any

# Try to import openpyxl for Excel output
try:
    from openpyxl import Workbook
    from openpyxl.styles import Font, Alignment, PatternFill, Border, Side
    from openpyxl.utils import get_column_letter
    HAS_OPENPYXL = True
except ImportError:
    HAS_OPENPYXL = False
    print("Warning: openpyxl not installed. Excel output disabled.")
    print("Install with: pip install openpyxl")


@dataclass
class BenchmarkResult:
    """Container for benchmark results."""
    name: str
    category: str
    success: bool
    error_message: str = ""
    # Criticality results
    keff: Optional[float] = None
    keff_std: Optional[float] = None
    # Point kinetics results
    beta_eff: Optional[float] = None
    beta_eff_std: Optional[float] = None
    gen_time: Optional[float] = None
    gen_time_std: Optional[float] = None
    # Alpha eigenvalue
    alpha: Optional[float] = None
    alpha_std: Optional[float] = None


def get_benchmark_dirs(base_dir: Path, category: str = None, benchmark: str = None) -> List[Path]:
    """Get list of benchmark directories to process."""
    categories = ['ieu', 'leu', 'mixed', 'pu', 'smf', 'u233']

    if category:
        if category not in categories:
            print(f"Error: Unknown category '{category}'")
            print(f"Available categories: {', '.join(categories)}")
            sys.exit(1)
        categories = [category]

    benchmark_dirs = []

    for cat in categories:
        cat_dir = base_dir / cat
        if not cat_dir.exists():
            continue

        for bench_dir in sorted(cat_dir.iterdir()):
            if not bench_dir.is_dir():
                continue

            model_file = bench_dir / 'model.py'
            if not model_file.exists():
                continue

            if benchmark and bench_dir.name != benchmark:
                continue

            benchmark_dirs.append(bench_dir)

    return benchmark_dirs


def create_kinetics_model(bench_dir: Path) -> bool:
    """Create a modified model with point kinetics enabled.

    This creates a wrapper script that imports the original model,
    adds kinetics tallies, and runs OpenMC.
    """
    kinetics_script = bench_dir / 'run_with_kinetics.py'

    script_content = '''#!/usr/bin/env python3
"""Auto-generated script to run OpenMC with point kinetics."""

import openmc
import os
import sys

# First, run the original model.py to generate base XML files
exec(open('model.py').read())

# Now modify settings for point kinetics
settings = openmc.Settings.from_xml('settings.xml')

# Enable kinetics parameters calculation using IFP method
settings.create_delayed_neutron_data = True

# Re-export settings
settings.export_to_xml()

# Create kinetics tallies for beta-effective and generation time
tallies = openmc.Tallies()

# Try to load existing tallies if any
try:
    existing_tallies = openmc.Tallies.from_xml('tallies.xml')
    for t in existing_tallies:
        tallies.append(t)
except:
    pass

# Add IFP-based kinetics tallies
# These require the adjoint flux which is calculated with create_delayed_neutron_data

# Mesh for tallies (simple global mesh)
mesh = openmc.RegularMesh()
mesh.dimension = [1, 1, 1]
mesh.lower_left = [-1000, -1000, -1000]
mesh.upper_right = [1000, 1000, 1000]

# Tally for delayed neutron fractions
delayed_tally = openmc.Tally(name='delayed_nu_fission')
delayed_tally.scores = ['delayed-nu-fission', 'nu-fission']
tallies.append(delayed_tally)

# Export tallies
tallies.export_to_xml()

print("Kinetics-enabled model generated successfully")
'''

    try:
        with open(kinetics_script, 'w') as f:
            f.write(script_content)
        return True
    except Exception as e:
        print(f"Error creating kinetics script: {e}")
        return False


def parse_openmc_output(output: str, statepoint_path: Path = None) -> Dict[str, Any]:
    """Parse OpenMC output to extract k-effective, kinetics results, and alpha eigenvalue."""
    results = {
        'keff': None,
        'keff_std': None,
        'beta_eff': None,
        'beta_eff_std': None,
        'gen_time': None,
        'gen_time_std': None,
        'alpha': None,
        'alpha_std': None,
    }

    # Parse k-effective from output
    # Look for: "k-effective (Collision)      = X.XXXXX +/- X.XXXXX"
    # Or: "Combined k-effective = X.XXXXX +/- X.XXXXX"
    keff_patterns = [
        r'Combined k-effective\s*=\s*([\d.]+)\s*\+/-\s*([\d.]+)',
        r'k-effective\s*\(Collision\)\s*=\s*([\d.]+)\s*\+/-\s*([\d.]+)',
        r'k-effective\s*=\s*([\d.]+)\s*\+/-\s*([\d.]+)',
    ]

    for pattern in keff_patterns:
        match = re.search(pattern, output, re.IGNORECASE)
        if match:
            results['keff'] = float(match.group(1))
            results['keff_std'] = float(match.group(2))
            break

    # Parse beta-effective if present
    beta_pattern = r'Beta[-_]?eff(?:ective)?\s*[:=]\s*([\d.eE+-]+)\s*(?:\+/-|±)?\s*([\d.eE+-]+)?'
    match = re.search(beta_pattern, output, re.IGNORECASE)
    if match:
        results['beta_eff'] = float(match.group(1))
        if match.group(2):
            results['beta_eff_std'] = float(match.group(2))

    # Parse generation time if present
    gen_time_pattern = r'(?:Generation|Prompt\s+neutron)\s+time\s*[:=]\s*([\d.eE+-]+)\s*(?:\+/-|±)?\s*([\d.eE+-]+)?'
    match = re.search(gen_time_pattern, output, re.IGNORECASE)
    if match:
        results['gen_time'] = float(match.group(1))
        if match.group(2):
            results['gen_time_std'] = float(match.group(2))

    # Parse alpha eigenvalue if present
    # Alpha = (k-1) / (Lambda * k) where Lambda is generation time
    alpha_pattern = r'[Aa]lpha\s*(?:eigenvalue)?\s*[:=]\s*([\d.eE+-]+)\s*(?:\+/-|±)?\s*([\d.eE+-]+)?'
    match = re.search(alpha_pattern, output, re.IGNORECASE)
    if match:
        results['alpha'] = float(match.group(1))
        if match.group(2):
            results['alpha_std'] = float(match.group(2))

    # Try to extract from statepoint file if available
    if statepoint_path and statepoint_path.exists():
        try:
            import openmc
            sp = openmc.StatePoint(str(statepoint_path))

            # Get k-effective
            if hasattr(sp, 'keff'):
                results['keff'] = sp.keff.nominal_value
                results['keff_std'] = sp.keff.std_dev

            # Get kinetics data if available
            if hasattr(sp, 'global_tallies'):
                for name, value in sp.global_tallies.items():
                    if 'beta' in name.lower():
                        results['beta_eff'] = value.nominal_value
                        results['beta_eff_std'] = value.std_dev
                    elif 'generation' in name.lower() or 'lambda' in name.lower():
                        results['gen_time'] = value.nominal_value
                        results['gen_time_std'] = value.std_dev
                    elif 'alpha' in name.lower():
                        results['alpha'] = value.nominal_value
                        results['alpha_std'] = value.std_dev

            sp.close()
        except Exception as e:
            pass  # Silently ignore statepoint parsing errors

    return results


def run_benchmark(bench_dir: Path, run_openmc: bool = False,
                  enable_kinetics: bool = True, openmc_args: list = None) -> BenchmarkResult:
    """Run a single benchmark and collect results.

    Args:
        bench_dir: Path to benchmark directory
        run_openmc: If True, run OpenMC after generating XML
        enable_kinetics: If True, enable point kinetics calculations
        openmc_args: Additional arguments to pass to OpenMC

    Returns:
        BenchmarkResult with all collected data
    """
    bench_name = bench_dir.name
    category = bench_dir.parent.name
    model_file = bench_dir / 'model.py'

    result = BenchmarkResult(name=bench_name, category=category, success=False)

    try:
        # Change to benchmark directory
        original_dir = os.getcwd()
        os.chdir(bench_dir)

        # Run model.py to generate XML files
        proc_result = subprocess.run(
            [sys.executable, str(model_file)],
            capture_output=True,
            text=True,
            timeout=120
        )

        if proc_result.returncode != 0:
            os.chdir(original_dir)
            result.error_message = f"Model generation failed: {proc_result.stderr[:500]}"
            return result

        # Check that XML files were created
        required_files = ['geometry.xml', 'materials.xml', 'settings.xml']
        missing = [f for f in required_files if not (bench_dir / f).exists()]
        if missing:
            os.chdir(original_dir)
            result.error_message = f"Missing XML files: {missing}"
            return result

        # Modify settings for kinetics if requested
        if run_openmc and enable_kinetics:
            try:
                # Read and modify settings.xml to enable kinetics
                settings_file = bench_dir / 'settings.xml'
                with open(settings_file, 'r') as f:
                    settings_content = f.read()

                # Add create_delayed_neutron_data if not present
                if 'delayed_neutron_data' not in settings_content.lower():
                    # Insert before </settings>
                    settings_content = settings_content.replace(
                        '</settings>',
                        '  <create_delayed_neutron_data>true</create_delayed_neutron_data>\n</settings>'
                    )
                    with open(settings_file, 'w') as f:
                        f.write(settings_content)
            except Exception as e:
                # Non-fatal error, continue without kinetics
                pass

        # Run OpenMC if requested
        if run_openmc:
            cmd = ['openmc']
            if openmc_args:
                cmd.extend(openmc_args)

            proc_result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=7200  # 2 hour timeout for OpenMC runs
            )

            # Parse results from output
            full_output = proc_result.stdout + proc_result.stderr

            # Find statepoint file
            statepoint_files = list(bench_dir.glob('statepoint.*.h5'))
            statepoint_path = max(statepoint_files, key=lambda p: p.stat().st_mtime) if statepoint_files else None

            parsed = parse_openmc_output(full_output, statepoint_path)
            result.keff = parsed['keff']
            result.keff_std = parsed['keff_std']
            result.beta_eff = parsed['beta_eff']
            result.beta_eff_std = parsed['beta_eff_std']
            result.gen_time = parsed['gen_time']
            result.gen_time_std = parsed['gen_time_std']
            result.alpha = parsed['alpha']
            result.alpha_std = parsed['alpha_std']

            os.chdir(original_dir)

            if proc_result.returncode != 0:
                result.error_message = f"OpenMC failed: {proc_result.stderr[:500]}"
                # Still mark as partial success if we got k-eff
                if result.keff is not None:
                    result.success = True
                return result

            result.success = True
            return result

        os.chdir(original_dir)
        result.success = True
        return result

    except subprocess.TimeoutExpired:
        os.chdir(original_dir)
        result.error_message = "Timeout"
        return result
    except Exception as e:
        try:
            os.chdir(original_dir)
        except:
            pass
        result.error_message = str(e)[:500]
        return result


def export_results_to_excel(results: List[BenchmarkResult], output_file: Path):
    """Export results to Excel file."""
    if not HAS_OPENPYXL:
        print("Cannot export to Excel: openpyxl not installed")
        # Fall back to CSV
        csv_file = output_file.with_suffix('.csv')
        export_results_to_csv(results, csv_file)
        return

    wb = Workbook()

    # Summary sheet
    ws_summary = wb.active
    ws_summary.title = "Summary"

    # Styles
    header_font = Font(bold=True, color="FFFFFF")
    header_fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
    success_fill = PatternFill(start_color="C6EFCE", end_color="C6EFCE", fill_type="solid")
    fail_fill = PatternFill(start_color="FFC7CE", end_color="FFC7CE", fill_type="solid")
    thin_border = Border(
        left=Side(style='thin'),
        right=Side(style='thin'),
        top=Side(style='thin'),
        bottom=Side(style='thin')
    )

    # Headers
    headers = [
        'Benchmark', 'Category', 'Status',
        'k-eff', 'k-eff Std Dev',
        'Beta-eff', 'Beta-eff Std Dev',
        'Gen Time (s)', 'Gen Time Std Dev',
        'Alpha (1/s)', 'Alpha Std Dev',
        'Error'
    ]

    for col, header in enumerate(headers, 1):
        cell = ws_summary.cell(row=1, column=col, value=header)
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = Alignment(horizontal='center')
        cell.border = thin_border

    # Data rows
    for row_idx, result in enumerate(results, 2):
        data = [
            result.name,
            result.category,
            'Success' if result.success else 'Failed',
            result.keff,
            result.keff_std,
            result.beta_eff,
            result.beta_eff_std,
            result.gen_time,
            result.gen_time_std,
            result.alpha,
            result.alpha_std,
            result.error_message if not result.success else ''
        ]

        for col, value in enumerate(data, 1):
            cell = ws_summary.cell(row=row_idx, column=col, value=value)
            cell.border = thin_border

            # Format numbers
            if isinstance(value, float):
                if col in [4, 5]:  # k-eff columns
                    cell.number_format = '0.00000'
                elif col in [6, 7]:  # beta-eff columns
                    cell.number_format = '0.00000E+00'
                elif col in [8, 9, 10, 11]:  # gen time and alpha columns
                    cell.number_format = '0.00E+00'

            # Color status column
            if col == 3:
                cell.fill = success_fill if result.success else fail_fill

    # Adjust column widths
    column_widths = [15, 10, 10, 12, 12, 12, 12, 12, 12, 12, 12, 50]
    for col, width in enumerate(column_widths, 1):
        ws_summary.column_dimensions[get_column_letter(col)].width = width

    # Create category summary sheets
    categories = set(r.category for r in results)
    for cat in sorted(categories):
        cat_results = [r for r in results if r.category == cat]
        ws = wb.create_sheet(title=cat.upper())

        # Headers
        for col, header in enumerate(headers, 1):
            cell = ws.cell(row=1, column=col, value=header)
            cell.font = header_font
            cell.fill = header_fill
            cell.alignment = Alignment(horizontal='center')
            cell.border = thin_border

        # Data
        for row_idx, result in enumerate(cat_results, 2):
            data = [
                result.name,
                result.category,
                'Success' if result.success else 'Failed',
                result.keff,
                result.keff_std,
                result.beta_eff,
                result.beta_eff_std,
                result.gen_time,
                result.gen_time_std,
                result.alpha,
                result.alpha_std,
                result.error_message if not result.success else ''
            ]

            for col, value in enumerate(data, 1):
                cell = ws.cell(row=row_idx, column=col, value=value)
                cell.border = thin_border

                if isinstance(value, float):
                    if col in [4, 5]:
                        cell.number_format = '0.00000'
                    elif col in [6, 7]:
                        cell.number_format = '0.00000E+00'
                    elif col in [8, 9, 10, 11]:
                        cell.number_format = '0.00E+00'

                if col == 3:
                    cell.fill = success_fill if result.success else fail_fill

        # Adjust column widths
        for col, width in enumerate(column_widths, 1):
            ws.column_dimensions[get_column_letter(col)].width = width

    # Statistics sheet
    ws_stats = wb.create_sheet(title="Statistics")

    # Calculate statistics
    successful = [r for r in results if r.success and r.keff is not None]

    stats_data = [
        ['Metric', 'Value'],
        ['Total Benchmarks', len(results)],
        ['Successful', len([r for r in results if r.success])],
        ['Failed', len([r for r in results if not r.success])],
        ['With k-eff', len([r for r in results if r.keff is not None])],
        ['With Beta-eff', len([r for r in results if r.beta_eff is not None])],
        ['With Gen Time', len([r for r in results if r.gen_time is not None])],
        ['With Alpha', len([r for r in results if r.alpha is not None])],
        ['', ''],
        ['Category Breakdown', ''],
    ]

    for cat in sorted(categories):
        cat_results = [r for r in results if r.category == cat]
        cat_success = len([r for r in cat_results if r.success])
        stats_data.append([f'  {cat.upper()}', f'{cat_success}/{len(cat_results)}'])

    for row_idx, (label, value) in enumerate(stats_data, 1):
        ws_stats.cell(row=row_idx, column=1, value=label)
        ws_stats.cell(row=row_idx, column=2, value=value)

    ws_stats.column_dimensions['A'].width = 20
    ws_stats.column_dimensions['B'].width = 15

    # Save workbook
    wb.save(output_file)
    print(f"Results exported to: {output_file}")


def export_results_to_csv(results: List[BenchmarkResult], output_file: Path):
    """Export results to CSV file (fallback if openpyxl not available)."""
    import csv

    headers = [
        'Benchmark', 'Category', 'Status',
        'k-eff', 'k-eff Std Dev',
        'Beta-eff', 'Beta-eff Std Dev',
        'Gen Time (s)', 'Gen Time Std Dev',
        'Alpha (1/s)', 'Alpha Std Dev',
        'Error'
    ]

    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)

        for result in results:
            writer.writerow([
                result.name,
                result.category,
                'Success' if result.success else 'Failed',
                result.keff,
                result.keff_std,
                result.beta_eff,
                result.beta_eff_std,
                result.gen_time,
                result.gen_time_std,
                result.alpha,
                result.alpha_std,
                result.error_message if not result.success else ''
            ])

    print(f"Results exported to: {output_file}")


def list_benchmarks(base_dir: Path):
    """List all available benchmarks."""
    categories = ['ieu', 'leu', 'mixed', 'pu', 'smf', 'u233']

    total = 0
    for cat in categories:
        cat_dir = base_dir / cat
        if not cat_dir.exists():
            continue

        benchmarks = sorted([d.name for d in cat_dir.iterdir()
                           if d.is_dir() and (d / 'model.py').exists()])

        if benchmarks:
            print(f"\n{cat.upper()} ({len(benchmarks)} benchmarks):")
            print("-" * 40)
            for i, b in enumerate(benchmarks):
                print(f"  {b}", end="")
                if (i + 1) % 5 == 0:
                    print()
            if len(benchmarks) % 5 != 0:
                print()
            total += len(benchmarks)

    print(f"\nTotal: {total} benchmarks")


def main():
    parser = argparse.ArgumentParser(
        description='Batch runner for OpenMC ICSBEP benchmarks with results collection',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )

    parser.add_argument('--run', action='store_true',
                       help='Run OpenMC simulations (default: generate XML only)')
    parser.add_argument('--parallel', '-p', type=int, default=1,
                       help='Number of parallel processes (default: 1)')
    parser.add_argument('--category', '-c', type=str,
                       help='Run only benchmarks in specified category (ieu, leu, mixed, pu, smf, u233)')
    parser.add_argument('--benchmark', '-b', type=str,
                       help='Run only specified benchmark')
    parser.add_argument('--list', '-l', action='store_true',
                       help='List all available benchmarks')
    parser.add_argument('--output', '-o', type=str, default='benchmark_results.xlsx',
                       help='Output file for results (default: benchmark_results.xlsx)')
    parser.add_argument('--openmc-args', type=str, default='',
                       help='Additional arguments to pass to OpenMC (e.g., "-s 4")')
    parser.add_argument('--no-kinetics', action='store_true',
                       help='Disable point kinetics calculations')
    parser.add_argument('--continue-on-error', action='store_true',
                       help='Continue running even if a benchmark fails')

    args = parser.parse_args()

    # Get base directory (where this script is located)
    base_dir = Path(__file__).parent.resolve()

    # List benchmarks if requested
    if args.list:
        list_benchmarks(base_dir)
        return

    # Get benchmark directories
    benchmark_dirs = get_benchmark_dirs(base_dir, args.category, args.benchmark)

    if not benchmark_dirs:
        print("No benchmarks found matching criteria")
        return

    print(f"Found {len(benchmark_dirs)} benchmark(s) to process")
    print(f"Mode: {'Run OpenMC' if args.run else 'Generate XML only'}")
    print(f"Point Kinetics: {'Disabled' if args.no_kinetics else 'Enabled'}")
    if args.parallel > 1:
        print(f"Parallel processes: {args.parallel}")
    print(f"Output file: {args.output}")
    print("-" * 60)

    # Parse OpenMC arguments
    openmc_args = args.openmc_args.split() if args.openmc_args else None
    enable_kinetics = not args.no_kinetics

    start_time = time.time()
    results: List[BenchmarkResult] = []

    if args.parallel > 1 and len(benchmark_dirs) > 1:
        # Parallel execution
        with ProcessPoolExecutor(max_workers=args.parallel) as executor:
            futures = {
                executor.submit(run_benchmark, d, args.run, enable_kinetics, openmc_args): d
                for d in benchmark_dirs
            }

            for future in as_completed(futures):
                result = future.result()
                results.append(result)

                status = "[OK]" if result.success else "[FAIL]"
                keff_str = f"k={result.keff:.5f}" if result.keff else "k=N/A"
                beta_str = f"β={result.beta_eff:.5e}" if result.beta_eff else ""
                alpha_str = f"α={result.alpha:.5e}" if result.alpha else ""

                print(f"{status} {result.category}/{result.name}: {keff_str} {beta_str} {alpha_str}")

                if not result.success and not args.continue_on_error:
                    executor.shutdown(wait=False)
                    break
    else:
        # Sequential execution
        for i, bench_dir in enumerate(benchmark_dirs):
            result = run_benchmark(bench_dir, args.run, enable_kinetics, openmc_args)
            results.append(result)

            status = "[OK]" if result.success else "[FAIL]"
            keff_str = f"k={result.keff:.5f}" if result.keff else "k=N/A"
            beta_str = f"β={result.beta_eff:.5e}" if result.beta_eff else ""
            alpha_str = f"α={result.alpha:.5e}" if result.alpha else ""
            progress = f"[{i+1}/{len(benchmark_dirs)}]"

            print(f"{progress} {status} {result.category}/{result.name}: {keff_str} {beta_str} {alpha_str}")

            if not result.success and not args.continue_on_error:
                print(f"Error: {result.error_message}")
                break

    elapsed = time.time() - start_time

    print("-" * 60)
    print(f"Completed in {elapsed:.1f} seconds")

    successful = len([r for r in results if r.success])
    failed = len([r for r in results if not r.success])
    with_keff = len([r for r in results if r.keff is not None])
    with_beta = len([r for r in results if r.beta_eff is not None])
    with_alpha = len([r for r in results if r.alpha is not None])

    print(f"Successful: {successful}")
    print(f"Failed: {failed}")
    print(f"With k-eff: {with_keff}")
    print(f"With beta-eff: {with_beta}")
    print(f"With alpha: {with_alpha}")

    # Export results
    if results:
        output_path = base_dir / args.output
        if args.output.endswith('.xlsx') and HAS_OPENPYXL:
            export_results_to_excel(results, output_path)
        else:
            csv_path = output_path.with_suffix('.csv')
            export_results_to_csv(results, csv_path)

    if failed > 0:
        sys.exit(1)


if __name__ == '__main__':
    main()
