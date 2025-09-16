"""
Enhanced Pydantic Generator that includes metadata (meanings, annotations) for enum values.

This custom generator extends the LinkML PydanticGenerator to pass additional
metadata fields to the templates, enabling rich enum generation with ontology
mappings and annotations.
"""

from typing import Dict, Any, Optional
from dataclasses import dataclass
from linkml.generators.pydanticgen import PydanticGenerator
from linkml.generators.pydanticgen.template import PydanticEnum, EnumValue
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue


@dataclass
class EnhancedEnumValue(EnumValue):
    """Extended EnumValue that includes meaning and annotations fields."""
    meaning: Optional[str] = None
    annotations: Optional[Dict[str, Any]] = None


class EnhancedPydanticGenerator(PydanticGenerator):
    """
    Enhanced Pydantic generator that preserves enum metadata.
    
    This generator extends the base PydanticGenerator to include
    meaning (ontology mappings) and annotations in the enum template context.
    """
    
    def generate_enums(self) -> None:
        """Generate enums with enhanced metadata."""
        enums = self.schemaview.all_enums()
        
        for enum_name, enum_def in enums.items():
            if enum_def.permissible_values:
                # Create enhanced enum values with metadata
                enum_values = {}
                for pv_name, pv in enum_def.permissible_values.items():
                    # Convert permissible value to enhanced enum value
                    label = self._get_enum_label(pv_name, pv)
                    value = pv.text if pv.text is not None else pv_name
                    
                    # Create enhanced enum value with all metadata
                    enhanced_value = EnhancedEnumValue(
                        label=label,
                        value=value,
                        description=pv.description,
                        meaning=pv.meaning,
                        annotations=dict(pv.annotations) if pv.annotations else None
                    )
                    enum_values[pv_name] = enhanced_value
                
                # Create the enum with enhanced values
                enum_model = PydanticEnum(
                    name=self._get_class_name(enum_name),
                    description=enum_def.description,
                    values=enum_values
                )
                
                # Add to the module's enums
                self.enums[enum_name] = enum_model
    
    def _get_enum_label(self, pv_name: str, pv: PermissibleValue) -> str:
        """Get the label for an enum value."""
        # Use the same logic as the base generator
        if hasattr(self, 'camelcase_enums') and self.camelcase_enums:
            from linkml.utils.formatutils import camelcase
            return camelcase(pv_name)
        else:
            # Convert to valid Python identifier
            import re
            label = re.sub(r'[^a-zA-Z0-9_]', '_', pv_name)
            if label[0].isdigit():
                label = f'_{label}'
            return label
    
    def _get_class_name(self, name: str) -> str:
        """Get the class name for an enum."""
        # Use the base generator's logic if available
        if hasattr(super(), '_get_class_name'):
            return super()._get_class_name(name)
        else:
            # Default: just return the name as-is
            return name


def generate_enhanced_pydantic(schema_path: str, **kwargs) -> str:
    """
    Generate enhanced Pydantic models with metadata-rich enums.
    
    Args:
        schema_path: Path to the LinkML schema file
        **kwargs: Additional arguments to pass to the generator
        
    Returns:
        Generated Python code as a string
    """
    generator = EnhancedPydanticGenerator(schema_path, **kwargs)
    return generator.serialize()