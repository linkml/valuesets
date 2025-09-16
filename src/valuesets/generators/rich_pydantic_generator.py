"""
Rich Pydantic Generator for LinkML Schemas

This generator creates Pydantic-compatible Python code from LinkML schemas,
with enhanced enum support that includes metadata (descriptions, meanings, annotations).
"""

import re
from dataclasses import dataclass
from typing import Dict, Any, List, Optional, TextIO
from pathlib import Path

from linkml_runtime.utils.schemaview import SchemaView
from linkml_runtime.linkml_model.meta import (
    SchemaDefinition, EnumDefinition, PermissibleValue, ClassDefinition
)
from linkml.generators.pydanticgen import PydanticGenerator


class RichPydanticGenerator(PydanticGenerator):
    """
    Enhanced Pydantic generator that creates enums with metadata support.

    This generator extends the base PydanticGenerator to create enums that:
    1. Are fully compatible with standard Python enums
    2. Include all metadata from LinkML schemas (descriptions, meanings, annotations)
    3. Provide convenient methods to access metadata
    """

    generatorname = "rich-pydantic"
    generatorversion = "0.1.0"

    def __init__(self, schema: str, **kwargs):
        super().__init__(schema, **kwargs)
        self.schema_view = SchemaView(schema)

    def serialize(self, **kwargs) -> str:
        """Generate the complete Python module."""
        output = []

        # Header and imports
        output.extend(self._generate_header())
        output.extend(self._generate_imports())

        # Base classes and utilities
        output.extend(self._generate_base_classes())

        # Generate all enums with rich metadata
        output.extend(self._generate_rich_enums())

        # Generate classes (reuse base generator logic)
        output.extend(self._generate_classes())

        return "\n".join(output)

    def _generate_header(self) -> List[str]:
        """Generate file header."""
        return [
            '"""',
            'Generated Pydantic models with rich enum support.',
            '',
            'This module was automatically generated from a LinkML schema.',
            'It includes enums with full metadata support (descriptions, meanings, annotations).',
            '"""',
            '',
            'from __future__ import annotations',
            ''
        ]

    def _generate_imports(self) -> List[str]:
        """Generate import statements."""
        return [
            'import re',
            'import sys',
            'from datetime import date, datetime, time',
            'from decimal import Decimal',
            'from enum import Enum',
            'from typing import Any, ClassVar, List, Literal, Dict, Optional, Union',
            '',
            'from pydantic import BaseModel, ConfigDict, Field, RootModel, field_validator',
            '',
            '# Import our rich enum support',
            'from valuesets.generators.rich_enum import RichEnum',
            '',
        ]

    def _generate_base_classes(self) -> List[str]:
        """Generate base configuration classes."""
        return [
            'metamodel_version = "None"',
            'version = "None"',
            '',
            '',
            'class ConfiguredBaseModel(BaseModel):',
            '    model_config = ConfigDict(',
            '        validate_assignment=True,',
            '        validate_default=True,',
            '        extra="forbid",',
            '        arbitrary_types_allowed=True,',
            '        use_enum_values=True,',
            '        strict=False,',
            '    )',
            '    pass',
            '',
            '',
            'class LinkMLMeta(RootModel):',
            '    root: Dict[str, Any] = {}',
            '    model_config = ConfigDict(frozen=True)',
            '',
            '    def __getattr__(self, key: str):',
            '        return getattr(self.root, key)',
            '',
            '    def __getitem__(self, key: str):',
            '        return self.root[key]',
            '',
            '    def __setitem__(self, key: str, value):',
            '        self.root[key] = value',
            '',
            '    def __contains__(self, key: str) -> bool:',
            '        return key in self.root',
            '',
            '',
            f'linkml_meta = LinkMLMeta({self._generate_linkml_meta()})',
            '',
        ]

    def _generate_linkml_meta(self) -> str:
        """Generate the linkml_meta dictionary."""
        schema = self.schema_view.schema
        meta_dict = {
            'default_prefix': schema.default_prefix,
            'description': schema.description,
            'id': schema.id,
            'name': schema.name,
            'title': schema.title,
        }
        return repr(meta_dict)

    def _generate_rich_enums(self) -> List[str]:
        """Generate all enums with metadata support."""
        output = []

        for enum_name in self.schema_view.all_enums():
            enum_def = self.schema_view.get_enum(enum_name)
            if enum_def and enum_def.permissible_values:
                output.extend(self._generate_single_rich_enum(enum_name, enum_def))
                output.append('')  # Add spacing between enums

        return output

    def _generate_single_rich_enum(self, enum_name: str, enum_def: EnumDefinition) -> List[str]:
        """Generate a single rich enum."""
        output = []

        # Class definition
        class_name = self._get_class_name(enum_name)
        output.append(f'class {class_name}(RichEnum):')

        # Class docstring
        if enum_def.description:
            output.append('    """')
            output.append(f'    {enum_def.description}')
            output.append('    """')

        # Enum members
        output.append('    # Enum members')
        for pv_name, pv in enum_def.permissible_values.items():
            member_name = self._get_enum_member_name(pv_name)
            member_value = pv.text if pv.text is not None else pv_name
            output.append(f'    {member_name} = "{member_value}"')

        output.append('')

        # Set metadata after class creation to avoid it becoming an enum member
        output.append(f'# Set metadata after class creation to avoid it becoming an enum member')
        output.append(f'{class_name}._metadata = {{')

        for pv_name, pv in enum_def.permissible_values.items():
            member_name = self._get_enum_member_name(pv_name)
            metadata = self._build_metadata_dict(pv)

            if metadata:  # Only add if there's actual metadata
                output.append(f'    "{member_name}": {repr(metadata)},')

        output.append('}')

        return output

    def _build_metadata_dict(self, pv: PermissibleValue) -> Dict[str, Any]:
        """Build metadata dictionary for a permissible value."""
        metadata = {}

        if pv.description:
            metadata['description'] = pv.description

        if pv.meaning:
            metadata['meaning'] = pv.meaning

        if pv.annotations:
            # Convert annotation objects to simple dictionaries
            annotations_dict = {}
            for key, annotation in pv.annotations.items():
                if hasattr(annotation, 'value'):
                    annotations_dict[key] = annotation.value
                else:
                    annotations_dict[key] = str(annotation)
            metadata['annotations'] = annotations_dict

        # Add other fields if they exist
        if hasattr(pv, 'aliases') and pv.aliases:
            metadata['aliases'] = list(pv.aliases)

        if hasattr(pv, 'deprecated') and pv.deprecated:
            metadata['deprecated'] = pv.deprecated

        return metadata

    def _generate_classes(self) -> List[str]:
        """Generate Pydantic model classes."""
        # For now, we'll use a simplified approach
        # In a full implementation, we'd generate full Pydantic models
        output = []

        for class_name in self.schema_view.all_classes():
            class_def = self.schema_view.get_class(class_name)
            if class_def:
                output.extend(self._generate_single_class(class_name, class_def))
                output.append('')

        return output

    def _generate_single_class(self, class_name: str, class_def: ClassDefinition) -> List[str]:
        """Generate a single Pydantic model class."""
        output = []

        # For now, just create empty classes with docstrings
        pydantic_class_name = self._get_class_name(class_name)
        output.append(f'class {pydantic_class_name}(ConfiguredBaseModel):')

        if class_def.description:
            output.append('    """')
            output.append(f'    {class_def.description}')
            output.append('    """')

        output.append('    pass  # TODO: Implement class slots')

        return output

    def _get_class_name(self, name: str) -> str:
        """Convert a LinkML name to a Python class name with proper CamelCase."""
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
        """Convert a permissible value name to a Python enum member name."""
        # Convert to valid Python identifier in UPPER_CASE
        # Replace invalid characters with underscores
        member_name = re.sub(r'[^a-zA-Z0-9_]', '_', name).upper()

        # Ensure it doesn't start with a digit
        if member_name and member_name[0].isdigit():
            member_name = f'_{member_name}'

        return member_name


def cli():
    """Command line interface for the rich pydantic generator."""
    import argparse

    parser = argparse.ArgumentParser(description='Generate rich Pydantic models from LinkML schema')
    parser.add_argument('schema', help='LinkML schema file')
    parser.add_argument('-o', '--output', help='Output file (default: stdout)')

    args = parser.parse_args()

    generator = RichPydanticGenerator(args.schema)
    output = generator.serialize()

    if args.output:
        with open(args.output, 'w') as f:
            f.write(output)
    else:
        print(output)


if __name__ == '__main__':
    cli()
