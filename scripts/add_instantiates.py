#!/usr/bin/env python3
"""
Script to add instantiates references to all enums in the valuesets repository.

This adds references to the valuesets_meta metaclasses based on the metadata
present in each enum:
- ValueSetEnumDefinition: base metaclass for all enums
- ValueSetEnumDefinitionWithSource: for enums with source
- ValueSetEnumDefinitionWithConformance: for enums with source + conforms_to
- ReferenceEnumDefinition: for reference enums (maturity_levels)
"""

import sys
from pathlib import Path
from ruamel.yaml import YAML

yaml = YAML()
yaml.preserve_quotes = True
yaml.width = 120

# Metaclass URIs
BASE_METACLASS = "valuesets_meta:ValueSetEnumDefinition"
SOURCE_METACLASS = "valuesets_meta:ValueSetEnumDefinitionWithSource"
CONFORMANCE_METACLASS = "valuesets_meta:ValueSetEnumDefinitionWithConformance"
REFERENCE_METACLASS = "valuesets_meta:ReferenceEnumDefinition"

# Files containing reference enums (these define values used by other parts of schema)
REFERENCE_ENUM_FILES = [
    "computing/maturity_levels.yaml",
]


def determine_metaclass(enum_def: dict, file_rel_path: str) -> str:
    """Determine the appropriate metaclass based on enum metadata."""
    # Check if this is a reference enum file
    for ref_file in REFERENCE_ENUM_FILES:
        if file_rel_path.endswith(ref_file):
            return REFERENCE_METACLASS

    # Check for conformance (requires source + conforms_to)
    if enum_def.get('source') and enum_def.get('conforms_to'):
        return CONFORMANCE_METACLASS

    # Check for source only
    if enum_def.get('source'):
        return SOURCE_METACLASS

    # Default to base metaclass
    return BASE_METACLASS


def process_schema_file(file_path: Path, schema_dir: Path, dry_run: bool = False) -> tuple[bool, int]:
    """
    Process a single schema file and add instantiates to all enums.

    Returns: (modified, enum_count)
    """
    with open(file_path, 'r') as f:
        schema = yaml.load(f)

    if not schema:
        return False, 0

    modified = False
    enum_count = 0

    # Add valuesets_meta prefix if needed
    if 'prefixes' in schema:
        if 'valuesets_meta' not in schema['prefixes']:
            schema['prefixes']['valuesets_meta'] = 'https://w3id.org/valuesets/meta/'
            modified = True
    else:
        # Check if file imports something that might have the prefix
        # For safety, add it anyway
        schema['prefixes'] = {'valuesets_meta': 'https://w3id.org/valuesets/meta/'}
        modified = True

    # Get relative path for determining metaclass
    try:
        file_rel_path = str(file_path.relative_to(schema_dir))
    except ValueError:
        file_rel_path = str(file_path)

    # Process enums
    if 'enums' in schema and schema['enums']:
        for enum_name, enum_def in schema['enums'].items():
            if enum_def is None:
                continue

            enum_count += 1

            # Determine appropriate metaclass
            metaclass = determine_metaclass(enum_def, file_rel_path)

            # Add instantiates if not present or update if different
            current_instantiates = enum_def.get('instantiates', [])
            if isinstance(current_instantiates, str):
                current_instantiates = [current_instantiates]

            # Check if any valuesets_meta class is already present
            has_meta_ref = any('valuesets_meta:' in str(i) for i in current_instantiates)

            if not has_meta_ref:
                # Add the metaclass reference
                if 'instantiates' not in enum_def:
                    # Insert after contributors or status
                    insert_pos = 0
                    for key in ['title', 'description', 'status', 'contributors']:
                        if key in enum_def:
                            insert_pos = list(enum_def.keys()).index(key) + 1
                    enum_def.insert(insert_pos, 'instantiates', [metaclass])
                else:
                    # Append to existing list
                    if isinstance(enum_def['instantiates'], list):
                        enum_def['instantiates'].append(metaclass)
                    else:
                        enum_def['instantiates'] = [enum_def['instantiates'], metaclass]
                modified = True

    if modified and not dry_run:
        with open(file_path, 'w') as f:
            yaml.dump(schema, f)

    return modified, enum_count


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Add instantiates references to all enums')
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
        # Skip generated files and metamodel
        if 'generated' in str(file_path) or 'metamodel' in str(file_path):
            continue

        try:
            modified, enum_count = process_schema_file(file_path, schema_dir, dry_run=args.dry_run)

            if modified:
                total_modified += 1
                print(f"{'Would modify' if args.dry_run else 'Modified'}: {file_path.relative_to(schema_dir)} ({enum_count} enums)")

            total_enums += enum_count
        except Exception as e:
            print(f"Error processing {file_path}: {e}", file=sys.stderr)

    print(f"\nSummary: {'Would modify' if args.dry_run else 'Modified'} {total_modified} files with {total_enums} total enums")


if __name__ == '__main__':
    main()
