#!/usr/bin/env python3
"""
Batch runner for OpenMC ICSBEP benchmarks.

This script runs all OpenMC model.py files in the benchmark directories.
It can generate XML files only or run full OpenMC simulations.

Usage:
    python batch.py                    # Generate XML files only (default)
    python batch.py --run              # Generate XML and run OpenMC
    python batch.py --run --parallel 4 # Run with 4 parallel processes
    python batch.py --category pu      # Run only plutonium benchmarks
    python batch.py --benchmark pmf001 # Run specific benchmark
    python batch.py --list             # List all available benchmarks
"""

import os
import sys
import subprocess
import argparse
import time
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor, as_completed


def get_benchmark_dirs(base_dir: Path, category: str = None, benchmark: str = None):
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


def run_benchmark(bench_dir: Path, run_openmc: bool = False, openmc_args: list = None):
    """Run a single benchmark.

    Args:
        bench_dir: Path to benchmark directory
        run_openmc: If True, run OpenMC after generating XML
        openmc_args: Additional arguments to pass to OpenMC

    Returns:
        Tuple of (benchmark_name, success, message)
    """
    bench_name = f"{bench_dir.parent.name}/{bench_dir.name}"
    model_file = bench_dir / 'model.py'

    try:
        # Change to benchmark directory
        original_dir = os.getcwd()
        os.chdir(bench_dir)

        # Run model.py to generate XML files
        result = subprocess.run(
            [sys.executable, str(model_file)],
            capture_output=True,
            text=True,
            timeout=60
        )

        if result.returncode != 0:
            os.chdir(original_dir)
            return (bench_name, False, f"Model generation failed: {result.stderr[:200]}")

        # Check that XML files were created
        required_files = ['geometry.xml', 'materials.xml', 'settings.xml']
        missing = [f for f in required_files if not (bench_dir / f).exists()]
        if missing:
            os.chdir(original_dir)
            return (bench_name, False, f"Missing XML files: {missing}")

        # Run OpenMC if requested
        if run_openmc:
            cmd = ['openmc']
            if openmc_args:
                cmd.extend(openmc_args)

            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=3600  # 1 hour timeout for OpenMC runs
            )

            os.chdir(original_dir)

            if result.returncode != 0:
                return (bench_name, False, f"OpenMC failed: {result.stderr[:200]}")

            # Extract k-effective from output
            keff_line = None
            for line in result.stdout.split('\n'):
                if 'k-effective' in line.lower() and 'combined' in line.lower():
                    keff_line = line.strip()
                    break

            return (bench_name, True, keff_line or "OpenMC completed")

        os.chdir(original_dir)
        return (bench_name, True, "XML files generated")

    except subprocess.TimeoutExpired:
        os.chdir(original_dir)
        return (bench_name, False, "Timeout")
    except Exception as e:
        os.chdir(original_dir)
        return (bench_name, False, str(e)[:200])


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
        description='Batch runner for OpenMC ICSBEP benchmarks',
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
    parser.add_argument('--openmc-args', type=str, default='',
                       help='Additional arguments to pass to OpenMC (e.g., "-s 4")')
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
    if args.parallel > 1:
        print(f"Parallel processes: {args.parallel}")
    print("-" * 60)

    # Parse OpenMC arguments
    openmc_args = args.openmc_args.split() if args.openmc_args else None

    start_time = time.time()
    successful = 0
    failed = 0
    results = []

    if args.parallel > 1 and len(benchmark_dirs) > 1:
        # Parallel execution
        with ProcessPoolExecutor(max_workers=args.parallel) as executor:
            futures = {
                executor.submit(run_benchmark, d, args.run, openmc_args): d
                for d in benchmark_dirs
            }

            for future in as_completed(futures):
                bench_name, success, message = future.result()
                results.append((bench_name, success, message))

                if success:
                    successful += 1
                    print(f"[OK] {bench_name}: {message}")
                else:
                    failed += 1
                    print(f"[FAIL] {bench_name}: {message}")
                    if not args.continue_on_error:
                        executor.shutdown(wait=False)
                        break
    else:
        # Sequential execution
        for bench_dir in benchmark_dirs:
            bench_name, success, message = run_benchmark(bench_dir, args.run, openmc_args)
            results.append((bench_name, success, message))

            if success:
                successful += 1
                print(f"[OK] {bench_name}: {message}")
            else:
                failed += 1
                print(f"[FAIL] {bench_name}: {message}")
                if not args.continue_on_error:
                    break

    elapsed = time.time() - start_time

    print("-" * 60)
    print(f"Completed in {elapsed:.1f} seconds")
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")

    if failed > 0:
        sys.exit(1)


if __name__ == '__main__':
    main()
