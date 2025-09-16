# Custom Pydantic Templates

This directory contains custom Jinja2 templates for the LinkML Pydantic generator.

## Overview

The LinkML pydantic generator allows customization through Jinja2 templates. We've created custom templates to enhance the generated Python enums with metadata support.

## Current Status

### What Works
- ✅ Custom enum template that generates metadata classes for enum descriptions
- ✅ Methods to access enum descriptions at runtime
- ✅ Clean enum representation with `__repr__` method

### Current Limitations
- ❌ **Ontology meanings (e.g., BSPO:0000000) are not currently included**
- ❌ **Annotations are not currently included**

The reason is that the LinkML pydantic generator's `EnumValue` class only passes through:
- `label`: The enum member name
- `value`: The enum member value  
- `description`: The description text

It does NOT pass through:
- `meaning`: Ontology term mappings
- `annotations`: Additional metadata

## Usage

To use these custom templates, the pydantic generator is configured with:

```bash
uv run gen-pydantic --template-dir templates/pydantic schema.yaml
```

This is configured in `config.public.mk`:
```makefile
LINKML_GENERATORS_PYDANTIC_ARGS=--template-dir templates/pydantic
```

## Template Structure

### `pydantic/enum.py.jinja`

This template generates:

1. **Metadata Class** (when descriptions exist):
   - `{EnumName}Meta` class with static dictionaries
   - `_descriptions` dictionary mapping member names to descriptions
   - Class methods to access metadata

2. **Enhanced Enum Class**:
   - Standard Python enum with string values
   - Instance methods to access metadata:
     - `get_description()`: Get description for the enum value
     - `get_metadata()`: Get all available metadata
   - Class methods:
     - `get_member_metadata(name)`: Get metadata by member name
   - Custom `__repr__` for better debugging

## Example Generated Code

```python
class DataAbsentEnumMeta:
    """Metadata holder for DataAbsentEnum enum values"""
    
    _descriptions = {
        "Unknown": "The value is expected to exist but is not known.",
        # ... more descriptions
    }
    
    @classmethod
    def description(cls, member: "DataAbsentEnum") -> Optional[str]:
        """Get description for enum member"""
        return cls._descriptions.get(member.name, None)

class DataAbsentEnum(str, Enum):
    """Used to specify why content is missing."""
    
    # Enum members
    Unknown = "unknown"
    
    # Metadata access methods
    def get_description(self) -> Optional[str]:
        """Get description for this enum value"""
        return DataAbsentEnumMeta.description(self)
```

## Future Improvements

To fully support ontology meanings and annotations, we would need to either:

1. **Extend the LinkML pydantic generator** to pass these fields through to templates
2. **Create a custom generator** that inherits from PydanticGenerator
3. **Post-process** the generated files to inject metadata from the schema
4. **Generate a separate metadata module** that can be imported alongside the enums

### Proposed Solution

The most maintainable approach would be to contribute back to LinkML to enhance the `EnumValue` class:

```python
@dataclass
class EnumValue:
    label: str
    value: str  
    description: Optional[str] = None
    meaning: Optional[str] = None  # Add this
    annotations: Optional[Dict[str, Any]] = None  # Add this
```

This would allow templates to access all enum metadata and generate richer Python enums.

## Files

- `pydantic/enum.py.jinja`: Custom enum template with metadata support
- Additional templates can be added as needed (class.py.jinja, etc.)