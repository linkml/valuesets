#!/usr/bin/env python3
"""
Script to fix poorly-generated enum titles (e.g. "G O Evidence Code" -> "GO Evidence Code").
"""

import re
from pathlib import Path
from ruamel.yaml import YAML

yaml = YAML()
yaml.preserve_quotes = True
yaml.width = 120


def fix_title(title: str) -> str:
    """Fix titles with separated acronym letters."""
    # Pattern to find single letters followed by space and another single letter
    # e.g., "G O Evidence Code" -> "GO Evidence Code"

    # Join consecutive single uppercase letters that are separated by spaces
    def join_acronyms(match):
        letters = match.group(0).replace(' ', '')
        return letters

    # Match sequences of "X Y Z" where X, Y, Z are single uppercase letters
    # This handles things like "G O Evidence" -> "GO Evidence"
    result = re.sub(r'\b([A-Z])(?: ([A-Z]))+\b', join_acronyms, title)

    # Also handle cases where acronym is partially joined with digit
    # e.g., "IS O2" should stay as found, but "IS O639" should become "ISO639"
    # Actually, let's handle specific known patterns:

    # Fix specific known patterns
    known_fixes = {
        'IS O2': 'ISO2',
        'IS O3': 'ISO3',
        'IS O639_1': 'ISO639_1',
        'IS O4217': 'ISO4217',
        'OM B1997': 'OMB1997',
    }
    for old, new in known_fixes.items():
        result = result.replace(old, new)

    return result


def process_schema_file(file_path: Path, dry_run: bool = False) -> tuple[bool, int]:
    """Fix titles in a single schema file."""
    with open(file_path, 'r') as f:
        schema = yaml.load(f)

    if not schema:
        return False, 0

    modified = False
    fix_count = 0

    # Process enums
    if 'enums' in schema and schema['enums']:
        for enum_name, enum_def in schema['enums'].items():
            if enum_def is None:
                continue

            if 'title' in enum_def:
                old_title = enum_def['title']
                new_title = fix_title(old_title)
                if old_title != new_title:
                    enum_def['title'] = new_title
                    modified = True
                    fix_count += 1
                    print(f"  Fixed: '{old_title}' -> '{new_title}'")

    if modified and not dry_run:
        with open(file_path, 'w') as f:
            yaml.dump(schema, f)

    return modified, fix_count


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Fix enum titles in valuesets schema')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be changed without modifying files')
    args = parser.parse_args()

    schema_dir = Path(__file__).parent.parent / 'src' / 'valuesets' / 'schema'
    files = list(schema_dir.rglob('*.yaml'))

    total_modified = 0
    total_fixes = 0

    for file_path in sorted(files):
        if 'generated' in str(file_path):
            continue

        modified, fix_count = process_schema_file(file_path, dry_run=args.dry_run)

        if modified:
            total_modified += 1

        total_fixes += fix_count

    print(f"\nSummary: {'Would fix' if args.dry_run else 'Fixed'} {total_fixes} titles in {total_modified} files")


if __name__ == '__main__':
    main()
