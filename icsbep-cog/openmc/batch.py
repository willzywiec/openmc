#!/usr/bin/env python3
"""
Batch runner for OpenMC ICSBEP benchmarks with results collection.

This script runs all OpenMC model.py files in the benchmark directories,
collects k-effective and point kinetics results, and exports to CSV.

Usage:
    python batch.py                    # Generate XML files only (default)
    python batch.py --run              # Generate XML and run OpenMC
    python batch.py --run --parallel 4 # Run with 4 parallel processes
    python batch.py --category pu      # Run only plutonium benchmarks
    python batch.py --benchmark pmf001 # Run specific benchmark
    python batch.py --list             # List all available benchmarks
    python batch.py --run --output results.csv  # Specify output file

Results are saved to 'benchmark_results.csv' by default.
Results are written incrementally as each benchmark completes.
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

            # Get k-effective from statepoint
            if hasattr(sp, 'keff'):
                results['keff'] = sp.keff.nominal_value
                results['keff_std'] = sp.keff.std_dev

            # Get kinetics data from statepoint
            # OpenMC stores delayed neutron data when create_delayed_neutron_data=true

            # Try to get beta-effective (sum of delayed neutron fractions)
            if hasattr(sp, 'k_combined') and hasattr(sp.k_combined, 'nominal_value'):
                k_eff = sp.k_combined.nominal_value
            elif results['keff']:
                k_eff = results['keff']
            else:
                k_eff = None

            # Check for kinetics tallies to extract beta-effective
            if hasattr(sp, 'tallies'):
                for tally_id, tally in sp.tallies.items():
                    try:
                        scores = tally.scores if hasattr(tally, 'scores') else []
                        score_strs = [str(s).lower() for s in scores]

                        # Check if this tally has both delayed-nu-fission and nu-fission
                        delayed_idx = None
                        total_idx = None
                        for i, s in enumerate(score_strs):
                            if 'delayed' in s and 'nu' in s:
                                delayed_idx = i
                            elif 'nu-fission' in s or 'nu_fission' in s:
                                if 'delayed' not in s:
                                    total_idx = i

                        if delayed_idx is not None and total_idx is not None:
                            # Get mean values for each score
                            mean = tally.mean
                            std_dev = tally.std_dev

                            # mean shape is typically (filters, nuclides, scores)
                            # For a simple tally it's (1, 1, num_scores)
                            delayed_mean = mean.flat[delayed_idx]
                            delayed_std = std_dev.flat[delayed_idx]
                            total_mean = mean.flat[total_idx]
                            total_std = std_dev.flat[total_idx]

                            if total_mean > 0:
                                beta = delayed_mean / total_mean
                                results['beta_eff'] = float(beta)
                                # Propagate uncertainty
                                if delayed_mean > 0 and (delayed_std > 0 or total_std > 0):
                                    rel_err = ((delayed_std/delayed_mean)**2 +
                                               (total_std/total_mean)**2) ** 0.5
                                    results['beta_eff_std'] = float(beta * rel_err)
                    except Exception:
                        pass  # Continue if this tally can't be parsed

            # Calculate alpha eigenvalue if we have k-eff and generation time
            if results['keff'] and results['gen_time'] and results['alpha'] is None:
                k = results['keff']
                gen_time = results['gen_time']
                if gen_time > 0 and k > 0:
                    results['alpha'] = (k - 1.0) / (gen_time * k)
                    if results['keff_std'] and results['gen_time_std']:
                        # Propagate uncertainty (simplified)
                        dk = results['keff_std']
                        dl = results['gen_time_std']
                        results['alpha_std'] = abs(results['alpha']) * ((dk/k)**2 + (dl/gen_time)**2)**0.5

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

        # Modify settings and add kinetics tallies if requested
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

                # Create kinetics tallies for beta-effective calculation
                tallies_file = bench_dir / 'tallies.xml'
                # Only add if tallies.xml doesn't exist or doesn't have delayed-nu-fission
                add_kinetics_tally = True
                if tallies_file.exists():
                    with open(tallies_file, 'r') as f:
                        if 'delayed-nu-fission' in f.read():
                            add_kinetics_tally = False

                if add_kinetics_tally:
                    tallies_content = '''<?xml version='1.0' encoding='utf-8'?>
<tallies>
  <tally id="1" name="kinetics">
    <scores>delayed-nu-fission nu-fission</scores>
  </tally>
</tallies>
'''
                    with open(tallies_file, 'w') as f:
                        f.write(tallies_content)
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


def export_results_to_csv(results: List[BenchmarkResult], output_file: Path):
    """Export results to CSV file."""
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


def init_csv_file(output_file: Path):
    """Initialize CSV file with headers for incremental writing."""
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


def append_result_to_csv(result: BenchmarkResult, output_file: Path):
    """Append a single result to CSV file (for incremental updates)."""
    import csv

    with open(output_file, 'a', newline='') as f:
        writer = csv.writer(f)
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
    parser.add_argument('--output', '-o', type=str, default='benchmark_results.csv',
                       help='Output file for results (default: benchmark_results.csv)')
    parser.add_argument('--openmc-args', type=str, default='',
                       help='Additional arguments to pass to OpenMC (e.g., "-s 4")')
    parser.add_argument('--no-kinetics', action='store_true',
                       help='Disable point kinetics calculations')
    parser.add_argument('--stop-on-error', action='store_true',
                       help='Stop running if a benchmark fails (default: continue)')

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

    # Set up output paths
    output_path = base_dir / args.output
    csv_path = output_path.with_suffix('.csv')

    # Initialize CSV file for incremental writing
    init_csv_file(csv_path)
    print(f"Writing results incrementally to: {csv_path}")

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

                # Write result to CSV immediately
                append_result_to_csv(result, csv_path)

                status = "[OK]" if result.success else "[FAIL]"
                keff_str = f"k={result.keff:.5f}" if result.keff else "k=N/A"
                beta_str = f"β={result.beta_eff:.5e}" if result.beta_eff else ""
                alpha_str = f"α={result.alpha:.5e}" if result.alpha else ""

                print(f"{status} {result.category}/{result.name}: {keff_str} {beta_str} {alpha_str}")

                if not result.success and args.stop_on_error:
                    executor.shutdown(wait=False)
                    break
    else:
        # Sequential execution
        for i, bench_dir in enumerate(benchmark_dirs):
            result = run_benchmark(bench_dir, args.run, enable_kinetics, openmc_args)
            results.append(result)

            # Write result to CSV immediately
            append_result_to_csv(result, csv_path)

            status = "[OK]" if result.success else "[FAIL]"
            keff_str = f"k={result.keff:.5f}" if result.keff else "k=N/A"
            beta_str = f"β={result.beta_eff:.5e}" if result.beta_eff else ""
            alpha_str = f"α={result.alpha:.5e}" if result.alpha else ""
            progress = f"[{i+1}/{len(benchmark_dirs)}]"

            print(f"{progress} {status} {result.category}/{result.name}: {keff_str} {beta_str} {alpha_str}")

            if not result.success and args.stop_on_error:
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

    # CSV was already written incrementally
    print(f"Results saved to: {csv_path}")

    if failed > 0:
        sys.exit(1)


if __name__ == '__main__':
    main()
