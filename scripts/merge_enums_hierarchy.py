#!/usr/bin/env python3
"""
Utility to merge all LinkML YAML schemas into a single hierarchical structure.
Creates an is_a hierarchy: Domain -> Schema -> Enum
"""

import yaml
import os
from pathlib import Path
from typing import Dict, Any, List
import re
from collections import defaultdict

def snake_to_pascal(name: str) -> str:
    """Convert snake_case to PascalCase."""
    components = name.split('_')
    return ''.join(x.title() for x in components)


def create_domain_enum_name(domain: str) -> str:
    """Create a domain-level enum name."""
    domain_pascal = snake_to_pascal(domain)
    return f"{domain_pascal}DomainEnum"

def create_schema_enum_name(domain: str, schema_name: str) -> str:
    """Create a schema-level enum name."""
    # Just use the schema name directly, no need to prefix with domain
    schema_pascal = snake_to_pascal(schema_name.replace('.yaml', '').replace('.yml', ''))
    return f"{schema_pascal}SchemaEnum"

def load_yaml_file(file_path: Path) -> Dict[str, Any]:
    """Load a YAML file."""
    with open(file_path, 'r') as f:
        return yaml.safe_load(f)

def collect_all_schemas(schema_dir: Path) -> Dict[str, List[Path]]:
    """Collect all schema files organized by domain."""
    schemas_by_domain = defaultdict(list)

    # Process root-level schemas
    for yaml_file in schema_dir.glob('*.yaml'):
        # Skip meta files and our own output
        if yaml_file.name not in ['valuesets.yaml', 'types.yaml', 'merged_hierarchy.yaml']:
            schemas_by_domain['root'].append(yaml_file)

    # Process domain-specific schemas
    for domain_dir in schema_dir.iterdir():
        if domain_dir.is_dir():
            domain_name = domain_dir.name
            # Skip the merged directory to avoid recursion
            if domain_name == 'merged':
                continue
            for yaml_file in domain_dir.glob('*.yaml'):
                schemas_by_domain[domain_name].append(yaml_file)

    return dict(schemas_by_domain)

def extract_prefixes(schema_data: Dict[str, Any]) -> Dict[str, str]:
    """Extract prefixes from a schema."""
    return schema_data.get('prefixes', {})

def merge_prefixes(*prefix_dicts: Dict[str, str]) -> Dict[str, str]:
    """Merge multiple prefix dictionaries, handling conflicts."""
    merged = {}
    for prefix_dict in prefix_dicts:
        for key, value in prefix_dict.items():
            if key in merged and merged[key] != value:
                # Keep the first occurrence for consistency
                continue
            merged[key] = value
    return merged

def process_enum(enum_name: str, enum_data: Dict[str, Any], parent_enum: str) -> Dict[str, Any]:
    """Process a single enum and add is_a relationship."""
    processed_enum = enum_data.copy()
    processed_enum['is_a'] = parent_enum

    # Ensure enum has a description
    if 'description' not in processed_enum:
        processed_enum['description'] = f"Enum: {enum_name}"

    return processed_enum

def build_hierarchical_schema(schema_dir: Path) -> Dict[str, Any]:
    """Build the complete hierarchical schema."""
    schemas_by_domain = collect_all_schemas(schema_dir)

    # Initialize the merged schema
    merged_schema = {
        'id': 'https://w3id.org/linkml/valuesets/merged',
        'name': 'valuesets_merged_hierarchy',
        'title': 'Merged Value Sets with Hierarchical Structure',
        'description': 'All value sets merged into a single hierarchical structure with is_a relationships',
        'license': 'MIT',
        'prefixes': {
            'linkml': 'https://w3id.org/linkml/',
            'valuesets': 'https://w3id.org/linkml/valuesets/',
        },
        'default_prefix': 'valuesets',
        'imports': ['linkml:types'],
        'enums': {}
    }

    # Create root enum
    root_enum_name = 'ValueSetEnum'
    merged_schema['enums'][root_enum_name] = {
        'description': 'Root enum for all value sets',
        'abstract': True
    }

    all_prefixes = {}

    # Process each domain
    for domain, schema_files in sorted(schemas_by_domain.items()):
        if not schema_files:
            continue

        # Create domain-level enum
        if domain == 'root':
            domain_enum_name = 'RootDomainEnum'
        else:
            domain_enum_name = create_domain_enum_name(domain)

        merged_schema['enums'][domain_enum_name] = {
            'description': f'Domain-level enum for {domain} value sets',
            'is_a': root_enum_name,
            'abstract': True
        }

        # Process each schema file in the domain
        for schema_file in sorted(schema_files):
            try:
                schema_data = load_yaml_file(schema_file)

                # Collect prefixes
                schema_prefixes = extract_prefixes(schema_data)
                all_prefixes = merge_prefixes(all_prefixes, schema_prefixes)

                # Skip if no enums
                if 'enums' not in schema_data or not schema_data['enums']:
                    continue

                # Create schema-level enum
                schema_name = schema_file.stem
                schema_enum_name = create_schema_enum_name(domain, schema_name)

                merged_schema['enums'][schema_enum_name] = {
                    'description': f'Schema-level enum for {schema_name} in {domain}',
                    'is_a': domain_enum_name,
                    'abstract': True,
                    'annotations': {
                        'source_file': str(schema_file.relative_to(schema_dir))
                    }
                }

                # Process each enum in the schema
                for enum_name, enum_data in schema_data['enums'].items():
                    # Just use the original enum name - assume uniqueness
                    unique_enum_name = enum_name

                    # Process and add the enum
                    merged_schema['enums'][unique_enum_name] = process_enum(
                        unique_enum_name,
                        enum_data,
                        schema_enum_name
                    )

                    # Add source annotations
                    if 'annotations' not in merged_schema['enums'][unique_enum_name]:
                        merged_schema['enums'][unique_enum_name]['annotations'] = {}
                    merged_schema['enums'][unique_enum_name]['annotations']['source_domain'] = domain
                    merged_schema['enums'][unique_enum_name]['annotations']['source_schema'] = schema_name

            except Exception as e:
                print(f"Error processing {schema_file}: {e}")
                continue

    # Merge all collected prefixes
    merged_schema['prefixes'] = merge_prefixes(merged_schema['prefixes'], all_prefixes)

    return merged_schema

def write_merged_schema(merged_schema: Dict[str, Any], output_file: Path):
    """Write the merged schema to a YAML file."""
    with open(output_file, 'w') as f:
        yaml.dump(merged_schema, f,
                 default_flow_style=False,
                 sort_keys=False,
                 allow_unicode=True,
                 width=120)
    print(f"Merged schema written to {output_file}")

    # Print statistics
    enum_count = len(merged_schema['enums'])
    domain_count = sum(1 for e in merged_schema['enums'].values()
                      if e.get('description', '').startswith('Domain-level enum'))
    schema_count = sum(1 for e in merged_schema['enums'].values()
                      if e.get('description', '').startswith('Schema-level enum'))
    concrete_count = enum_count - domain_count - schema_count - 1  # -1 for root

    print(f"\nStatistics:")
    print(f"  Total enums: {enum_count}")
    print(f"  Domain-level enums: {domain_count}")
    print(f"  Schema-level enums: {schema_count}")
    print(f"  Concrete enums: {concrete_count}")

    # Count prefixes
    prefix_count = len(merged_schema.get('prefixes', {}))
    print(f"  Prefixes: {prefix_count}")

def main():
    """Main function."""
    import argparse

    # Set up argument parser
    parser = argparse.ArgumentParser(description='Merge LinkML schemas into hierarchical structure')
    parser.add_argument('--output', '-o', type=str,
                       help='Output file path (default: src/valuesets/merged/merged_hierarchy.yaml)')
    args = parser.parse_args()

    # Get the project root
    script_dir = Path(__file__).parent
    project_root = script_dir.parent

    # Define paths
    schema_dir = project_root / 'src' / 'valuesets' / 'schema'

    # Use provided output path or default
    if args.output:
        output_file = Path(args.output)
        # Make absolute if relative
        if not output_file.is_absolute():
            output_file = project_root / output_file
    else:
        output_file = project_root / 'src' / 'valuesets' / 'merged' / 'merged_hierarchy.yaml'

    # Ensure output directory exists
    output_file.parent.mkdir(parents=True, exist_ok=True)

    # Check if schema directory exists
    if not schema_dir.exists():
        print(f"Schema directory not found: {schema_dir}")
        return 1

    print(f"Processing schemas from: {schema_dir}")
    print(f"Output will be written to: {output_file}")

    # Build and write the merged schema
    merged_schema = build_hierarchical_schema(schema_dir)
    write_merged_schema(merged_schema, output_file)

    return 0

if __name__ == '__main__':
    exit(main())