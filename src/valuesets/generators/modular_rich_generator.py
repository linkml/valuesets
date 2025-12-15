"""
Modular Rich Enum Generator for LinkML Schemas

This generator creates modular Python enum files from LinkML schemas,
maintaining the directory structure and generating one Python module per schema file.
"""

import os
import re
from pathlib import Path
from typing import Dict, Any, List, Optional, Set
from linkml_runtime.utils.schemaview import SchemaView
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ModularRichEnumGenerator:
    """
    Generate modular Python enum files with rich metadata support.
    """

    def __init__(self, schema_dir: str, output_dir: str):
        self.schema_dir = Path(schema_dir)
        self.output_dir = Path(output_dir)
        self.generated_modules = {}  # Track what we generate for __init__.py

    def generate_all(self):
        """Process all schema files and generate corresponding Python modules."""
        # Find all YAML schema files
        schema_files = list(self.schema_dir.rglob("*.yaml"))

        # Skip the main valuesets.yaml
        schema_files = [f for f in schema_files if f.name != "valuesets.yaml"]

        logger.info(f"Found {len(schema_files)} schema files to process")

        for schema_file in schema_files:
            self.process_schema_file(schema_file)

        # Generate top-level __init__.py
        self.generate_init_file()

    def process_schema_file(self, schema_path: Path):
        """Process a single schema file and generate corresponding Python module."""
        # Calculate relative path from schema dir
        relative_path = schema_path.relative_to(self.schema_dir)

        # Create corresponding output path
        output_path = self.output_dir / relative_path.with_suffix('.py')

        logger.info(f"Processing {relative_path} -> {output_path.relative_to(self.output_dir.parent.parent)}")

        try:
            # Load schema
            schema_view = SchemaView(str(schema_path))

            # Generate Python module
            module_content = self.generate_module(schema_view, relative_path)

            if module_content:
                # Ensure output directory exists
                output_path.parent.mkdir(parents=True, exist_ok=True)

                # Write module
                with open(output_path, 'w') as f:
                    f.write(module_content)

                # Track for __init__.py generation
                module_key = str(relative_path.with_suffix('')).replace('/', '.')
                self.generated_modules[module_key] = {
                    'path': relative_path,
                    'enums': self._get_enum_names(schema_view)
                }

                # Also create __init__.py for subdirectories
                self._ensure_package_structure(output_path.parent)

        except Exception as e:
            logger.error(f"Error processing {schema_path}: {e}")

    def generate_module(self, schema_view: SchemaView, relative_path: Path) -> Optional[str]:
        """Generate Python module content for a schema."""
        output = []

        # Header
        output.append('"""')
        if schema_view.schema.title:
            output.append(f'{schema_view.schema.title}')
        if schema_view.schema.description:
            output.append('')
            output.append(schema_view.schema.description)
        output.append('')
        output.append(f'Generated from: {relative_path}')
        output.append('"""')
        output.append('')
        output.append('from __future__ import annotations')
        output.append('')
        output.append('from valuesets.generators.rich_enum import RichEnum')
        output.append('')

        # Get all enums in this schema
        enum_names = schema_view.all_enums()

        if not enum_names:
            logger.info(f"No enums found in {relative_path}")
            return None

        # Generate each enum and track which ones we actually generated
        generated_enums = []
        for enum_name in enum_names:
            enum_def = schema_view.get_enum(enum_name)
            if enum_def:
                # Skip dynamic enums
                if hasattr(enum_def, 'reachable_from') and enum_def.reachable_from:
                    continue
                if enum_def.permissible_values:
                    output.extend(self._generate_enum(enum_name, enum_def))
                    output.append('')
                    generated_enums.append(self._get_class_name(enum_name))

        # Add __all__ export for generated enums only
        if generated_enums:
            output.append('__all__ = [')
            for class_name in generated_enums:
                output.append(f'    "{class_name}",')
            output.append(']')
        else:
            # No enums generated for this module
            return None

        return '\n'.join(output)

    def _generate_enum(self, enum_name: str, enum_def: EnumDefinition) -> List[str]:
        """Generate a single enum class."""
        output = []

        class_name = self._get_class_name(enum_name)

        # Check if this is a dynamic enum
        is_dynamic = hasattr(enum_def, 'reachable_from') and enum_def.reachable_from

        if is_dynamic:
            # For dynamic enums, generate a placeholder comment
            output.append(f'# {class_name} is a dynamic enum')
            output.append(f'# It would be populated from: {enum_def.reachable_from}')
            output.append(f'# Skipping generation for dynamic enum')
            return []  # Don't generate this enum

        output.append(f'class {class_name}(RichEnum):')

        # Add docstring
        if enum_def.description:
            output.append('    """')
            # Handle multi-line descriptions
            for line in enum_def.description.split('\n'):
                output.append(f'    {line}')
            output.append('    """')

        # Generate enum members
        output.append('    # Enum members')

        if not enum_def.permissible_values:
            # Empty enum - add pass statement
            output.append('    pass')
            output.append('')
            return output

        for pv_name, pv in enum_def.permissible_values.items():
            member_name = self._get_enum_member_name(pv_name)
            member_value = pv.text if pv.text is not None else pv_name
            output.append(f'    {member_name} = "{member_value}"')

        output.append('')

        # Generate metadata
        output.append(f'# Set metadata after class creation')
        output.append(f'{class_name}._metadata = {{')

        for pv_name, pv in enum_def.permissible_values.items():
            member_name = self._get_enum_member_name(pv_name)
            metadata = self._build_metadata(pv)

            if metadata:
                output.append(f'    "{member_name}": {repr(metadata)},')

        output.append('}')

        return output

    def _build_metadata(self, pv: PermissibleValue) -> Dict[str, Any]:
        """Build metadata dictionary for a permissible value."""
        metadata = {}

        if pv.description:
            metadata['description'] = pv.description

        if pv.meaning:
            metadata['meaning'] = pv.meaning

        if hasattr(pv, 'rank') and pv.rank is not None:
            metadata['rank'] = pv.rank

        if pv.annotations:
            annotations_dict = {}
            for key, annotation in pv.annotations.items():
                if hasattr(annotation, 'value'):
                    annotations_dict[key] = annotation.value
                else:
                    annotations_dict[key] = str(annotation)
            metadata['annotations'] = annotations_dict

        if hasattr(pv, 'aliases') and pv.aliases:
            metadata['aliases'] = list(pv.aliases)

        if hasattr(pv, 'deprecated') and pv.deprecated:
            metadata['deprecated'] = pv.deprecated

        return metadata

    def _get_enum_names(self, schema_view: SchemaView) -> List[str]:
        """Get list of enum class names from schema (excluding dynamic enums)."""
        result = []
        for enum_name in schema_view.all_enums():
            enum_def = schema_view.get_enum(enum_name)
            # Skip dynamic enums
            if enum_def and not (hasattr(enum_def, 'reachable_from') and enum_def.reachable_from):
                result.append(self._get_class_name(enum_name))
        return result

    def _ensure_package_structure(self, directory: Path):
        """Ensure __init__.py files exist for package structure."""
        current = directory
        while current != self.output_dir and current != current.parent:
            init_file = current / '__init__.py'
            if not init_file.exists():
                init_file.write_text('"""Auto-generated package."""\n')
            current = current.parent

    def generate_init_file(self):
        """Generate top-level __init__.py for convenient imports."""
        output = []

        output.append('"""')
        output.append('Common Value Sets - Rich Enum Collection')
        output.append('')
        output.append('This module provides convenient access to all enum definitions.')
        output.append('Each enum includes rich metadata (descriptions, ontology mappings, annotations)')
        output.append('while maintaining full Python enum compatibility.')
        output.append('')
        output.append('Usage:')
        output.append('    from valuesets.enums import Presenceenum, AnatomicalSide')
        output.append('    ')
        output.append('    # Or import everything')
        output.append('    from valuesets.enums import *')
        output.append('"""')
        output.append('')
        output.append('# flake8: noqa')
        output.append('')

        # Collect all enums from all modules
        all_enums = []
        imports_by_module = {}

        for module_key, info in sorted(self.generated_modules.items()):
            if info['enums']:
                module_path = module_key.replace('/', '.')
                imports_by_module[module_path] = info['enums']
                all_enums.extend(info['enums'])

        # Generate imports grouped by domain
        domains = {}
        for module_path, enums in imports_by_module.items():
            parts = module_path.split('.')
            domain = parts[0] if len(parts) > 1 else 'core'
            if domain not in domains:
                domains[domain] = {}
            domains[domain][module_path] = enums

        # Write imports organized by domain
        for domain in sorted(domains.keys()):
            output.append(f'# {domain.title()} domain')
            for module_path, enums in sorted(domains[domain].items()):
                if enums:
                    enum_list = ', '.join(enums)
                    output.append(f'from .{module_path} import {enum_list}')
            output.append('')

        # Generate __all__
        output.append('__all__ = [')
        for enum in sorted(set(all_enums)):
            output.append(f'    "{enum}",')
        output.append(']')

        # Write the init file
        init_path = self.output_dir / '__init__.py'
        init_path.parent.mkdir(parents=True, exist_ok=True)
        with open(init_path, 'w') as f:
            f.write('\n'.join(output))

        logger.info(f"Generated {init_path} with {len(all_enums)} enum exports")

    def _get_class_name(self, name: str) -> str:
        """Convert LinkML name to Python class name with proper CamelCase."""
        # Handle already CamelCase names
        if not any(c in name for c in ['_', '-', ' ']):
            # If it's already in some form of CamelCase, preserve it
            # Just ensure first letter is capitalized
            return name[0].upper() + name[1:] if name else ''

        # Convert snake_case, kebab-case, or space-separated to CamelCase
        words = re.split(r'[_\s-]+', name)

        # Properly capitalize each word, preserving existing caps when appropriate
        result = []
        for word in words:
            if word:
                if word.isupper():
                    # If the word is all caps (like "ISO"), keep it that way
                    result.append(word)
                elif word[0].isupper() and len(word) > 1:
                    # If already starts with capital, preserve the casing
                    result.append(word)
                else:
                    # Otherwise, capitalize first letter
                    result.append(word[0].upper() + word[1:].lower())

        return ''.join(result)

    def _get_enum_member_name(self, name: str) -> str:
        """Convert permissible value name to Python enum member name."""
        member_name = re.sub(r'[^a-zA-Z0-9_]', '_', name).upper()
        if member_name and member_name[0].isdigit():
            member_name = f'_{member_name}'
        return member_name


def main():
    """CLI entry point."""
    import argparse

    parser = argparse.ArgumentParser(description='Generate modular rich enums from LinkML schemas')
    parser.add_argument('schema_dir', help='Directory containing LinkML schema files')
    parser.add_argument('-o', '--output-dir', required=True, help='Output directory for Python modules')

    args = parser.parse_args()

    generator = ModularRichEnumGenerator(args.schema_dir, args.output_dir)
    generator.generate_all()


if __name__ == '__main__':
    main()
