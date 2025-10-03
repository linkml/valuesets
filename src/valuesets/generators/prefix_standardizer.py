#!/usr/bin/env python3
"""
Standardize prefixes across all LinkML schemas to use consistent valuesets prefix.

Sets:
- default_prefix: valuesets
- valuesets: https://w3id.org/valuesets/

Updates schemas in place with consistent prefixing.
"""

import yaml
from pathlib import Path
from typing import Dict, Any
import click
from collections import OrderedDict


class PrefixStandardizer:
    """Utility to standardize prefixes across LinkML schemas."""

    def __init__(self, target_prefix: str = "valuesets",
                 target_uri: str = "https://w3id.org/valuesets/"):
        self.target_prefix = target_prefix
        self.target_uri = target_uri

    def standardize_schema_prefixes(self, schema_path: Path, dry_run: bool = False) -> Dict[str, Any]:
        """
        Standardize prefixes in a schema file.

        Args:
            schema_path: Path to the schema file
            dry_run: If True, only show what would be changed

        Returns:
            Summary of changes made
        """
        # Load schema
        with open(schema_path, 'r') as f:
            schema_data = yaml.safe_load(f)

        changes = []

        # Ensure prefixes section exists
        if 'prefixes' not in schema_data:
            schema_data['prefixes'] = {}

        # Update/add the target prefix
        current_valuesets_uri = schema_data['prefixes'].get(self.target_prefix)
        if current_valuesets_uri != self.target_uri:
            old_uri = current_valuesets_uri or "not defined"
            schema_data['prefixes'][self.target_prefix] = self.target_uri
            changes.append(f"Updated {self.target_prefix} prefix: {old_uri} → {self.target_uri}")

        # Update default_prefix
        current_default = schema_data.get('default_prefix')
        if current_default != self.target_prefix:
            old_default = current_default or "not defined"
            schema_data['default_prefix'] = self.target_prefix
            changes.append(f"Updated default_prefix: {old_default} → {self.target_prefix}")

        # Write changes if not dry run
        if not dry_run and changes:
            self.write_schema(schema_data, schema_path)

        return {
            'file': schema_path.name,
            'changes': changes,
            'modified': len(changes) > 0
        }

    def write_schema(self, schema_data: Dict[str, Any], output_path: Path):
        """Write schema preserving key order and formatting."""
        # Define preferred key order
        key_order = [
            'name', 'title', 'description', 'id', 'version', 'status',
            'imports', 'prefixes', 'default_prefix', 'default_curi_maps',
            'slots', 'classes', 'enums', 'types', 'subsets', 'license', 'see_also'
        ]

        # Create ordered dict
        ordered_data = OrderedDict()

        # Add keys in preferred order
        for key in key_order:
            if key in schema_data:
                ordered_data[key] = schema_data[key]

        # Add any remaining keys
        for key in schema_data:
            if key not in ordered_data:
                ordered_data[key] = schema_data[key]

        # Write with nice formatting
        with open(output_path, 'w') as f:
            yaml.dump(dict(ordered_data), f,
                     default_flow_style=False,
                     sort_keys=False,
                     allow_unicode=True,
                     width=120)

    def standardize_directory(self, schema_dir: Path, dry_run: bool = False) -> None:
        """
        Standardize prefixes for all schemas in a directory.

        Args:
            schema_dir: Directory containing LinkML schema files
            dry_run: If True, only show what would be changed
        """
        # Find all YAML files
        yaml_files = list(schema_dir.rglob("*.yaml"))

        print(f"{'DRY RUN - ' if dry_run else ''}Standardizing prefixes in {len(yaml_files)} files")
        print(f"Target: {self.target_prefix}: {self.target_uri}")
        print()

        total_modified = 0
        total_changes = 0

        for yaml_file in yaml_files:
            # Skip certain files
            if yaml_file.name in ['linkml-meta.yaml', 'meta.yaml']:
                continue

            try:
                result = self.standardize_schema_prefixes(yaml_file, dry_run=dry_run)

                if result['changes']:
                    total_modified += 1
                    total_changes += len(result['changes'])

                    print(f"{'[DRY RUN] ' if dry_run else ''}{result['file']}:")
                    for change in result['changes']:
                        print(f"  - {change}")
                    print()

            except Exception as e:
                print(f"Error processing {yaml_file}: {e}")

        print(f"{'='*50}")
        print(f"{'DRY RUN - ' if dry_run else ''}Summary:")
        print(f"  Files modified: {total_modified}")
        print(f"  Total changes: {total_changes}")


@click.command()
@click.argument('schema_path', type=click.Path(exists=True, path_type=Path))
@click.option('--dry-run', '-n', is_flag=True,
              help='Preview changes without modifying files')
@click.option('--prefix', '-p', default='valuesets',
              help='Target prefix name (default: valuesets)')
@click.option('--uri', '-u', default='https://w3id.org/valuesets/',
              help='Target prefix URI (default: https://w3id.org/valuesets/)')
@click.option('--single-file', '-s', is_flag=True,
              help='Process single file instead of directory')
def main(schema_path: Path, dry_run: bool, prefix: str, uri: str, single_file: bool):
    """
    Standardize prefixes across LinkML schemas.

    SCHEMA_PATH: Path to schema file or directory

    Examples:

    \b
    # Preview changes for all schemas
    prefix_standardizer.py src/valuesets/schema --dry-run

    \b
    # Standardize all schemas
    prefix_standardizer.py src/valuesets/schema

    \b
    # Single file
    prefix_standardizer.py schema.yaml --single-file

    \b
    # Custom prefix
    prefix_standardizer.py src/valuesets/schema --prefix cval --uri https://w3id.org/linkml-common/
    """
    standardizer = PrefixStandardizer(target_prefix=prefix, target_uri=uri)

    if single_file or schema_path.is_file():
        # Process single file
        result = standardizer.standardize_schema_prefixes(schema_path, dry_run=dry_run)

        print(f"{'DRY RUN - ' if dry_run else ''}Results for {result['file']}:")
        if result['changes']:
            for change in result['changes']:
                print(f"  - {change}")
        else:
            print("  No changes needed")
    else:
        # Process directory
        standardizer.standardize_directory(schema_path, dry_run=dry_run)


if __name__ == '__main__':
    main()