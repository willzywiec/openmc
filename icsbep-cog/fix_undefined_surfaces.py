#!/usr/bin/env python3
"""
Fix script to remove undefined surface references from model.py files.

This script scans model.py files for region expressions that reference
surfaces not defined in the file, and removes those invalid references.
"""

import re
import sys
from pathlib import Path


def extract_defined_surfaces(content: str) -> set:
    """Extract all surface variable names that are defined in the file."""
    defined = set()

    # Match surface variable definitions like: surf1 = openmc.ZCylinder(...)
    # Also match prism plane definitions like: surf5_0 = openmc.Plane(...)
    pattern = r'^(surf\d+(?:_\d+)?)\s*='

    for line in content.split('\n'):
        match = re.match(pattern, line.strip())
        if match:
            defined.add(match.group(1))

    return defined


def extract_region_references(region_expr: str) -> set:
    """Extract all surface variable names referenced in a region expression."""
    # Match surface references like: -surf10, +surf12
    pattern = r'[+-]?(surf\d+(?:_\d+)?)'
    return set(re.findall(pattern, region_expr))


def fix_region_expression(region_expr: str, defined_surfaces: set) -> str:
    """
    Fix a region expression by removing references to undefined surfaces.
    Also removes contradictory terms like -surfX & +surfX.
    """
    # Split by & operator
    parts = [p.strip() for p in region_expr.split('&')]

    fixed_parts = []
    seen_surfaces = {}  # Track sign of each surface

    for part in parts:
        if not part:
            continue

        # Handle parenthesized expressions (prism regions)
        if '(' in part:
            # For now, keep prism expressions as-is if they have prism planes
            fixed_parts.append(part)
            continue

        # Check if this part references a valid surface
        match = re.match(r'([+-])(surf\d+(?:_\d+)?)', part.strip())
        if match:
            sign = match.group(1)
            surf_name = match.group(2)

            # Skip if surface is not defined
            if surf_name not in defined_surfaces:
                continue

            # Check for contradictory terms
            if surf_name in seen_surfaces:
                if seen_surfaces[surf_name] != sign:
                    # Contradictory - remove both by skipping this one
                    # and remove the previous one
                    fixed_parts = [p for p in fixed_parts if surf_name not in p]
                    continue
                else:
                    # Duplicate - skip
                    continue

            seen_surfaces[surf_name] = sign
            fixed_parts.append(part.strip())
        else:
            # Keep other expressions
            fixed_parts.append(part.strip())

    return ' & '.join(fixed_parts)


def fix_model_file(filepath: Path) -> tuple:
    """
    Fix a model.py file by removing undefined surface references and contradictory terms.
    Returns (was_modified, num_fixes).
    """
    with open(filepath, 'r') as f:
        content = f.read()

    original_content = content

    # Extract defined surfaces
    defined_surfaces = extract_defined_surfaces(content)

    # Find and fix region assignments
    num_fixes = 0

    # Pattern to match full region assignment lines
    region_pattern = r'^(\s*\w+\.region\s*=\s*)([^#\n]*)$'

    def fix_region_match(match):
        nonlocal num_fixes
        prefix = match.group(1)
        region_expr = match.group(2).strip()

        # Always try to fix (handles undefined refs and contradictory terms)
        fixed_expr = fix_region_expression(region_expr, defined_surfaces)
        if fixed_expr != region_expr:
            num_fixes += 1
            # If fixed expression is empty, remove the entire line
            if not fixed_expr:
                return ''
            return prefix + fixed_expr

        return match.group(0)

    content = re.sub(region_pattern, fix_region_match, content, flags=re.MULTILINE)

    if content != original_content:
        with open(filepath, 'w') as f:
            f.write(content)
        return True, num_fixes

    return False, 0


def main():
    # Get base directory
    if len(sys.argv) > 1:
        base_dir = Path(sys.argv[1])
    else:
        base_dir = Path(__file__).parent / 'openmc'

    if not base_dir.exists():
        print(f"Error: Directory {base_dir} does not exist")
        sys.exit(1)

    # Find all model.py files
    model_files = list(base_dir.rglob('model.py'))
    print(f"Found {len(model_files)} model.py files")

    modified_count = 0
    total_fixes = 0

    for filepath in sorted(model_files):
        was_modified, num_fixes = fix_model_file(filepath)
        if was_modified:
            modified_count += 1
            total_fixes += num_fixes
            print(f"Fixed {filepath.relative_to(base_dir.parent)}: {num_fixes} region(s)")

    print(f"\nSummary: Modified {modified_count} files with {total_fixes} region fixes")


if __name__ == '__main__':
    main()
