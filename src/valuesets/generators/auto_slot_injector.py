#!/usr/bin/env python3
"""
Automatically inject slot definitions for enums into LinkML schemas.

This script can:
1. Add a slots section to schemas that define enums
2. Generate appropriate slot definitions with correct ranges
3. Optionally create mixin classes that bundle related slots
"""

import yaml
from pathlib import Path
from typing import Dict, Any, List, Optional, Set
import re
import click
from collections import OrderedDict


class SlotInjector:
    """Utility to inject slots for enums into LinkML schemas."""

    @staticmethod
    def camel_to_snake(name: str) -> str:
        """Convert CamelCase to snake_case."""
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

    @staticmethod
    def snake_to_words(name: str) -> str:
        """Convert snake_case to human readable words."""
        return name.replace('_', ' ')

    def generate_slot_name(self, enum_name: str) -> str:
        """Generate slot name from enum name."""
        # Remove common suffixes
        slot_name = enum_name
        for suffix in ['Enum', 'Type', 'Class', 'Code']:
            if slot_name.endswith(suffix):
                slot_name = slot_name[:-len(suffix)]
                break

        return self.camel_to_snake(slot_name)

    def generate_slot_definition(self, enum_name: str,
                                enum_def: Dict[str, Any]) -> Dict[str, Any]:
        """Generate a complete slot definition for an enum."""
        slot_name = self.generate_slot_name(enum_name)

        # Extract description from enum
        enum_desc = enum_def.get('description', '')
        if enum_desc:
            # Clean up multi-line descriptions
            enum_desc = ' '.join(enum_desc.split())
            # Get first sentence
            first_sentence = enum_desc.split('.')[0]
            slot_desc = first_sentence[:1].upper() + first_sentence[1:] if first_sentence else ''
        else:
            # Generate generic description
            readable_name = self.snake_to_words(slot_name)
            slot_desc = f"The {readable_name} classification"

        slot_def = {
            'description': slot_desc,
            'range': enum_name
        }

        # Check if enum has many values (might be multivalued)
        if 'permissible_values' in enum_def:
            num_values = len(enum_def['permissible_values'])
            # If it's a target/feature/metric type enum, might be multivalued
            if any(keyword in slot_name for keyword in ['target', 'feature', 'metric', 'constraint']):
                slot_def['multivalued'] = True
                slot_def['comments'] = [f"Multiple {self.snake_to_words(slot_name)}s may apply"]

        return slot_def

    def inject_slots_into_schema(self, schema_path: Path,
                                output_path: Optional[Path] = None,
                                preserve_existing: bool = True) -> Dict[str, Any]:
        """
        Inject slots into a schema file.

        Args:
            schema_path: Path to the input schema
            output_path: Path to write modified schema (if None, prints to stdout)
            preserve_existing: If True, don't override existing slots

        Returns:
            Dictionary of generated slots
        """
        # Load schema
        with open(schema_path, 'r') as f:
            schema_data = yaml.safe_load(f)

        # Skip if no enums
        if 'enums' not in schema_data:
            return {}

        # Initialize or get existing slots
        if 'slots' not in schema_data:
            schema_data['slots'] = {}

        generated_slots = {}

        # Generate slots for each enum
        for enum_name, enum_def in schema_data['enums'].items():
            slot_name = self.generate_slot_name(enum_name)

            # Skip if exists and preserving
            if preserve_existing and slot_name in schema_data['slots']:
                continue

            slot_def = self.generate_slot_definition(enum_name, enum_def)
            generated_slots[slot_name] = slot_def
            schema_data['slots'][slot_name] = slot_def

        # Write output
        if output_path:
            self.write_schema(schema_data, output_path)
        else:
            # Just return for preview
            return generated_slots

        return generated_slots

    def write_schema(self, schema_data: Dict[str, Any], output_path: Path):
        """Write schema preserving key order."""
        # Define preferred key order
        key_order = [
            'name', 'title', 'description', 'id', 'version', 'status',
            'imports', 'prefixes', 'default_prefix', 'default_curi_maps',
            'slots', 'classes', 'enums'
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

    def generate_typed_slots_schema(self, schema_dir: Path,
                                   output_path: Path) -> None:
        """
        Generate a comprehensive slots schema from all enums in a directory.

        This creates a single schema file with all slot definitions that
        reference the appropriate enums.
        """
        all_slots = {}
        enum_to_module = {}  # Track which module each enum comes from

        # Scan all schema files
        yaml_files = list(schema_dir.rglob("*.yaml"))

        for yaml_file in yaml_files:
            # Skip meta files
            if yaml_file.name in ['linkml-meta.yaml', 'types.yaml', 'slot_mixins.yaml']:
                continue

            try:
                with open(yaml_file, 'r') as f:
                    schema_data = yaml.safe_load(f)

                if 'enums' not in schema_data:
                    continue

                # Get module name from schema
                module_name = schema_data.get('name', yaml_file.stem)

                # Process each enum
                for enum_name, enum_def in schema_data['enums'].items():
                    slot_name = self.generate_slot_name(enum_name)
                    slot_def = self.generate_slot_definition(enum_name, enum_def)

                    # Add module reference
                    slot_def['comments'] = slot_def.get('comments', [])
                    slot_def['comments'].append(f"Defined in module: {module_name}")

                    all_slots[slot_name] = slot_def
                    enum_to_module[enum_name] = module_name

            except Exception as e:
                print(f"Error processing {yaml_file}: {e}")
                continue

        # Create comprehensive slots schema
        slots_schema = {
            'name': 'generated_slots',
            'title': 'Auto-generated Slots for Value Sets',
            'description': 'Automatically generated slot definitions for all enums in the value sets collection.',
            'id': 'https://w3id.org/linkml-common/generated-slots',
            'version': '1.0.0',
            'status': 'release',
            'imports': ['linkml:types'],
            'prefixes': {
                'linkml': 'https://w3id.org/linkml/',
                'cval': 'https://w3id.org/linkml-common/'
            },
            'default_prefix': 'cval',
            'default_curi_maps': ['semweb_context'],
            'slots': all_slots
        }

        # Write the slots schema
        self.write_schema(slots_schema, output_path)
        print(f"Generated {len(all_slots)} slot definitions in {output_path}")


@click.command()
@click.argument('schema_path', type=click.Path(exists=True, path_type=Path))
@click.option('--output', '-o', type=click.Path(path_type=Path),
              help='Output path for modified schema or generated slots file')
@click.option('--mode', '-m',
              type=click.Choice(['inject', 'generate', 'preview']),
              default='preview',
              help='Mode: inject (modify files), generate (create slots file), preview (dry run)')
@click.option('--preserve/--overwrite', default=True,
              help='Preserve existing slots when injecting')
def main(schema_path: Path, output: Optional[Path], mode: str, preserve: bool):
    """
    Generate or inject LinkML slots for enums.

    SCHEMA_PATH: Path to schema file or directory
    """
    injector = SlotInjector()

    if mode == 'inject':
        if schema_path.is_file():
            # Single file injection
            if not output:
                output = schema_path  # In-place modification
            slots = injector.inject_slots_into_schema(
                schema_path, output, preserve_existing=preserve
            )
            print(f"Injected {len(slots)} slots into {output}")
        else:
            print("Inject mode requires a single file. Use generate mode for directories.")

    elif mode == 'generate':
        if schema_path.is_dir():
            # Generate comprehensive slots file
            if not output:
                output = schema_path / 'generated_slots.yaml'
            injector.generate_typed_slots_schema(schema_path, output)
        else:
            print("Generate mode requires a directory.")

    elif mode == 'preview':
        # Preview mode - just show what would be generated
        if schema_path.is_file():
            slots = injector.inject_slots_into_schema(
                schema_path, None, preserve_existing=preserve
            )
            print(f"Would generate {len(slots)} slots:")
            for slot_name, slot_def in slots.items():
                print(f"  - {slot_name}: {slot_def.get('description', 'No description')}")
                print(f"    Range: {slot_def.get('range')}")
                if slot_def.get('multivalued'):
                    print(f"    Multivalued: true")
        else:
            print("Preview mode requires a single file.")


if __name__ == '__main__':
    main()