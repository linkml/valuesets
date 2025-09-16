# Rich Enums - Default Python Generation

This project uses **Rich Enums** as the DEFAULT form for Python code generation. Rich enums provide full metadata support while maintaining complete compatibility with standard Python enums.

## Features

- ✅ **Full Python enum compatibility** - Works anywhere a standard enum is expected
- ✅ **Rich metadata** - Preserves descriptions, ontology mappings (meanings), and annotations from LinkML schemas
- ✅ **Ontology lookups** - Find enum members by their ontology terms (e.g., `EnumClass.from_meaning("BSPO:0000055")`)
- ✅ **JSON serializable** - Serializes as strings, just like standard enums
- ✅ **Type safe** - Full Pydantic and type checking support

## Usage

### Generate Python with Rich Enums

```bash
# Generate Python models with rich enum support (DEFAULT)
just gen-python

# Generate entire project with rich Python enums (DEFAULT)
just gen-project

# Run all generation including docs
just site

# If you need the dataclass version for some reason
just gen-python-dataclass
```

### Using Generated Rich Enums

```python
from valuesets.datamodel.valuesets import AnatomicalSide

# Use like a normal enum
left = AnatomicalSide.LEFT
print(left)  # "LEFT"
print(left == "LEFT")  # True

# Access rich metadata
print(left.get_description())  # "Left side of a bilaterally symmetric organism"
print(left.get_meaning())  # "BSPO:0000000"
print(left.get_annotations())  # {...}

# Lookup by ontology term
anterior = AnatomicalSide.from_meaning("BSPO:0000055")
print(anterior)  # AnatomicalSide.ANTERIOR

# Get all ontology mappings
meanings = AnatomicalSide.get_all_meanings()
# {"LEFT": "BSPO:0000000", "RIGHT": "BSPO:0000007", ...}
```

## Implementation

The rich enum system consists of:

1. **`RichEnum` base class** (`src/valuesets/generators/rich_enum.py`)
   - Uses `__init_subclass__` for clean metadata handling
   - Provides metadata access methods

2. **Custom LinkML generator** (`src/valuesets/generators/rich_pydantic_generator.py`)
   - Generates Pydantic models with rich enum support
   - Preserves all LinkML metadata

3. **Build integration** (`project.justfile`)
   - `gen-python` - Generate Python with rich enums (DEFAULT)
   - `gen-project` - Generate full project with rich enums (DEFAULT)
   - `gen-python-dataclass` - Generate dataclass version if needed

## Compatibility

Rich enums are 100% compatible with standard Python enums. They:
- Inherit from `str` and `Enum`
- Support all enum operations (iteration, comparison, etc.)
- Serialize to JSON as strings
- Work with Pydantic models
- Pass all type checks

The metadata is stored separately and accessed through methods, so it doesn't interfere with normal enum behavior.
