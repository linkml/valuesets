#!/usr/bin/env python3
"""
Utility to generate LinkML slots for each enum in a schema.

For each enum, creates a corresponding slot with:
- Slot name: enum name (removing 'Enum' suffix if present)
- Range: the enum itself
- Description: auto-generated from enum description
"""

import yaml
from pathlib import Path
from typing import Dict, Any, List, Optional
import re
import click
from linkml_runtime.utils.schemaview import SchemaView
from linkml_runtime.linkml_model import SchemaDefinition


def camel_to_snake(name: str) -> str:
    """Convert CamelCase to snake_case."""
    # Insert underscore before uppercase letters that follow lowercase letters
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    # Insert underscore before uppercase letters that follow lowercase or uppercase letters
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def generate_slot_name(enum_name: str) -> str:
    """
    Generate a slot name from an enum name.

    Rules:
    - Remove 'Enum' suffix if present
    - Remove 'Type' suffix if present
    - Convert to snake_case
    """
    # Remove common suffixes
    slot_name = enum_name
    if slot_name.endswith('Enum'):
        slot_name = slot_name[:-4]
    elif slot_name.endswith('Type'):
        slot_name = slot_name[:-4]

    # Convert to snake_case
    return camel_to_snake(slot_name)


def generate_slot_description(enum_name: str, enum_desc: Optional[str]) -> str:
    """Generate a description for the slot based on the enum."""
    if enum_desc:
        # Use first sentence of enum description
        first_sentence = enum_desc.split('.')[0]
        return f"The {generate_slot_name(enum_name).replace('_', ' ')} classification"
    else:
        return f"The {generate_slot_name(enum_name).replace('_', ' ')} for this entity"


def generate_slots_for_schema(schema_path: Path, in_place: bool = False,
                            output_path: Optional[Path] = None) -> Dict[str, Any]:
    """
    Generate slots for all enums in a schema.

    Args:
        schema_path: Path to the LinkML schema YAML file
        in_place: If True, modify the schema file in place
        output_path: If provided, write to this path instead

    Returns:
        Dictionary of generated slots
    """
    # Load schema
    with open(schema_path, 'r') as f:
        schema_data = yaml.safe_load(f)

    # Check if schema has enums
    if 'enums' not in schema_data or not schema_data['enums']:
        print(f"No enums found in {schema_path}")
        return {}

    # Initialize slots section if not present
    if 'slots' not in schema_data:
        schema_data['slots'] = {}

    generated_slots = {}

    # Generate slot for each enum
    for enum_name, enum_def in schema_data['enums'].items():
        slot_name = generate_slot_name(enum_name)

        # Skip if slot already exists
        if slot_name in schema_data['slots']:
            print(f"  Slot '{slot_name}' already exists, skipping")
            continue

        # Create slot definition
        slot_def = {
            'description': generate_slot_description(enum_name, enum_def.get('description')),
            'range': enum_name
        }

        # Add optional fields if useful
        if enum_def.get('description'):
            # Add a more detailed description if available
            slot_def['comments'] = [f"Value set: {enum_name}"]

        generated_slots[slot_name] = slot_def
        schema_data['slots'][slot_name] = slot_def
        print(f"  Generated slot '{slot_name}' for enum '{enum_name}'")

    # Write output if requested
    if in_place or output_path:
        output_file = schema_path if in_place else output_path

        # Preserve order and formatting as much as possible
        with open(output_file, 'w') as f:
            yaml.dump(schema_data, f,
                     default_flow_style=False,
                     sort_keys=False,
                     allow_unicode=True,
                     width=120)
        print(f"Updated schema written to {output_file}")

    return generated_slots


def process_directory(schema_dir: Path, in_place: bool = False,
                     output_dir: Optional[Path] = None) -> None:
    """
    Process all schema files in a directory.

    Args:
        schema_dir: Directory containing LinkML schema files
        in_place: If True, modify files in place
        output_dir: If provided, write modified schemas to this directory
    """
    # Find all YAML files
    yaml_files = list(schema_dir.rglob("*.yaml")) + list(schema_dir.rglob("*.yml"))

    print(f"Found {len(yaml_files)} YAML files in {schema_dir}")

    total_slots = 0
    processed_files = 0

    for yaml_file in yaml_files:
        # Skip certain files
        if yaml_file.name in ['linkml-meta.yaml', 'meta.yaml', 'types.yaml']:
            continue

        print(f"\nProcessing {yaml_file.relative_to(schema_dir)}...")

        try:
            # Determine output path
            output_path = None
            if output_dir and not in_place:
                # Maintain directory structure in output
                rel_path = yaml_file.relative_to(schema_dir)
                output_path = output_dir / rel_path
                output_path.parent.mkdir(parents=True, exist_ok=True)

            # Generate slots
            slots = generate_slots_for_schema(yaml_file, in_place=in_place,
                                            output_path=output_path)

            if slots:
                total_slots += len(slots)
                processed_files += 1

        except Exception as e:
            print(f"  Error processing {yaml_file}: {e}")

    print(f"\n{'='*50}")
    print(f"Summary: Generated {total_slots} slots across {processed_files} files")


@click.command()
@click.argument('schema_path', type=click.Path(exists=True, path_type=Path))
@click.option('--in-place', '-i', is_flag=True,
              help='Modify schema files in place')
@click.option('--output', '-o', type=click.Path(path_type=Path),
              help='Output directory for modified schemas')
@click.option('--single-file', '-s', is_flag=True,
              help='Process single file instead of directory')
def main(schema_path: Path, in_place: bool, output: Optional[Path], single_file: bool):
    """
    Generate LinkML slots for enums in schema files.

    SCHEMA_PATH: Path to schema file or directory
    """
    if single_file or schema_path.is_file():
        # Process single file
        print(f"Processing single file: {schema_path}")
        slots = generate_slots_for_schema(schema_path, in_place=in_place,
                                         output_path=output)
        print(f"Generated {len(slots)} slots")
    else:
        # Process directory
        process_directory(schema_path, in_place=in_place, output_dir=output)


if __name__ == '__main__':
    main()