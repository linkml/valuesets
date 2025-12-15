#!/usr/bin/env python3
"""
Script to add consistent metadata to all enums in the valuesets repository.

This script adds the following metadata to each enum:
- title (if missing)
- status: DRAFT (default for batch update)
- contributors: Chris Mungall and Claude Code

Uses ruamel.yaml to preserve formatting and comments.
"""

import sys
from pathlib import Path
from ruamel.yaml import YAML

yaml = YAML()
yaml.preserve_quotes = True
yaml.width = 120

# Default metadata values
DEFAULT_STATUS = "DRAFT"
DEFAULT_CONTRIBUTORS = [
    "orcid:0000-0002-6601-2165",
    "https://github.com/anthropics/claude-code"
]


def generate_title_from_name(enum_name: str) -> str:
    """Generate a human-readable title from enum name."""
    import re
    # Handle CamelCase - insert space before uppercase letters, but not for consecutive uppercase (acronyms)
    # e.g. GOEvidenceCode -> GO Evidence Code, not G O Evidence Code
    result = re.sub(r'([a-z])([A-Z])', r'\1 \2', enum_name)
    result = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1 \2', result)
    # Remove 'Enum' suffix if present
    if result.endswith(' Enum') or result.endswith('Enum'):
        result = re.sub(r'\s*Enum$', '', result)
    return result


def process_schema_file(file_path: Path, dry_run: bool = False) -> tuple[bool, int]:
    """
    Process a single schema file and add metadata to all enums.

    Returns: (modified, enum_count)
    """
    with open(file_path, 'r') as f:
        schema = yaml.load(f)

    if not schema:
        return False, 0

    modified = False
    enum_count = 0

    # Add orcid prefix if needed
    if 'prefixes' in schema:
        if 'orcid' not in schema['prefixes']:
            schema['prefixes']['orcid'] = 'https://orcid.org/'
            modified = True
    else:
        # Check if file imports core (which has orcid prefix)
        imports = schema.get('imports', [])
        imports_core = any('core' in str(i) for i in imports)
        if not imports_core:
            schema['prefixes'] = {'orcid': 'https://orcid.org/'}
            modified = True

    # Process enums
    if 'enums' in schema and schema['enums']:
        for enum_name, enum_def in schema['enums'].items():
            if enum_def is None:
                schema['enums'][enum_name] = {}
                enum_def = schema['enums'][enum_name]

            enum_count += 1

            # Add title if missing
            if 'title' not in enum_def:
                # Insert title at the beginning
                title = generate_title_from_name(enum_name)
                enum_def.insert(0, 'title', title)
                modified = True

            # Add status if missing
            if 'status' not in enum_def:
                # Insert after title/description if present
                insert_pos = 0
                for key in ['title', 'description']:
                    if key in enum_def:
                        insert_pos = list(enum_def.keys()).index(key) + 1
                enum_def.insert(insert_pos, 'status', DEFAULT_STATUS)
                modified = True

            # Add contributors if missing
            if 'contributors' not in enum_def:
                # Insert after status
                insert_pos = 0
                for key in ['title', 'description', 'status']:
                    if key in enum_def:
                        insert_pos = list(enum_def.keys()).index(key) + 1
                enum_def.insert(insert_pos, 'contributors', DEFAULT_CONTRIBUTORS.copy())
                modified = True

    if modified and not dry_run:
        with open(file_path, 'w') as f:
            yaml.dump(schema, f)

    return modified, enum_count


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Add metadata to all enums in valuesets schema')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be changed without modifying files')
    parser.add_argument('--file', type=str, help='Process a single file instead of all files')
    args = parser.parse_args()

    schema_dir = Path(__file__).parent.parent / 'src' / 'valuesets' / 'schema'

    if args.file:
        files = [Path(args.file)]
    else:
        files = list(schema_dir.rglob('*.yaml'))

    total_modified = 0
    total_enums = 0

    for file_path in sorted(files):
        # Skip generated files
        if 'generated' in str(file_path):
            continue

        try:
            modified, enum_count = process_schema_file(file_path, dry_run=args.dry_run)

            if modified:
                total_modified += 1
                print(f"{'Would modify' if args.dry_run else 'Modified'}: {file_path.relative_to(schema_dir)} ({enum_count} enums)")

            total_enums += enum_count
        except Exception as e:
            print(f"Error processing {file_path}: {e}", file=sys.stderr)

    print(f"\nSummary: {'Would modify' if args.dry_run else 'Modified'} {total_modified} files with {total_enums} total enums")


if __name__ == '__main__':
    main()
