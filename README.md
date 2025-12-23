# Common Value Sets

[![PyPI version](https://badge.fury.io/py/valuesets.svg)](https://badge.fury.io/py/valuesets)
[![LinkML](https://img.shields.io/badge/LinkML-1.9+-orange.svg)](https://linkml.io/)
[![Documentation](https://img.shields.io/badge/docs-linkml.io-green.svg)](https://linkml.io/valuesets/)
[![OWL/RDF](https://img.shields.io/badge/OWL-RDF-purple.svg)](https://w3id.org/valuesets/valuesets.owl.ttl)
[![BioPortal](https://img.shields.io/badge/BioPortal-VALUESETS-blue.svg)](https://bioportal.bioontology.org/ontologies/VALUESETS)

A comprehensive collection of standardized enumerations and value sets for data science, bioinformatics, materials science, and beyond.

## 🎯 Why Common Value Sets?

Data standardization is hard. Every project reinvents the wheel with custom enums, inconsistent naming, and no semantic meaning.  
**Common Value Sets** solves this by providing:

- 📚 **Rich, standardized enumerations** – Pre-defined value sets across multiple domains  
- 🧬 **Semantic meaning** – Every value is linked to ontology terms (when possible)  
- 🐍 **Python-first convenience** – Work with simple enums, get semantics for free  
- 🌐 **Multi-language support** – Generate JSON Schema, TypeScript, and more  
- 🔗 **Interoperability** – Built on LinkML standards for maximum compatibility  

---

### 🔍 A Simple Example

Different datasets often represent the same concept in incompatible ways:

- `M` / `F`  
- `male` / `female`  
- `1` / `2`  

They all mean the same thing, but they don’t interoperate.  
With **Common Value Sets**, you can instead use a shared enum:

```python
from valuesets.enums.core import SexEnum

s = SexEnum.MALE
print(s.value)            # "MALE"
print(s.get_meaning())    # "NCIT:C20197"
print(s.get_description())# "Male sex"
```

## ⚡ Quick Start

### For Python Developers

```python
from valuesets.enums.bio.structural_biology import StructuralBiologyTechnique
from valuesets.enums.spatial.spatial_qualifiers import AnatomicalSide

# Rich enums with metadata and ontology mappings
technique = StructuralBiologyTechnique.CRYO_EM
print(technique.value)  # "CRYO_EM"
print(technique.get_description())  # "Cryo-electron microscopy"
print(technique.get_meaning())  # "CHMO:0002413" (Chemical Methods Ontology)
print(technique.get_annotations())  # {'resolution_range': '2-30 Å typical', ...}

# Spatial relationships with BSPO mappings
side = AnatomicalSide.LEFT
print(side.get_meaning())  # "BSPO:0000000" (Biological Spatial Ontology)

# Look up enums by their ontology terms
found = AnatomicalSide.from_meaning("BSPO:0000000")  # Returns LEFT
```

### For Data Scientists

```python
from valuesets.enums.statistics import StatisticalTest, PValueThreshold
from valuesets.enums.data_science import DatasetSplitType, ModelType

# Standardized statistical tests with STATO ontology mappings
test = StatisticalTest.STUDENTS_T_TEST
print(test.get_meaning())  # "STATO:0000176"
print(test.get_description())  # "Student's t-test for comparing means"

# ML pipeline with standard splits
split = DatasetSplitType.TRAIN
model = ModelType.RANDOM_FOREST

# P-value thresholds with clear semantics
threshold = PValueThreshold.SIGNIFICANT
print(threshold.get_annotations())  # {'value': 0.05, 'symbol': '*'}
```

### For Bioinformaticians

```python
from valuesets.enums.bio.taxonomy import CommonOrganismTaxaEnum, BiologicalKingdom
from valuesets.enums.bio.cell_biology import CellCyclePhase, CellType

# Model organisms with NCBI Taxonomy IDs
human = CommonOrganismTaxaEnum.HUMAN
print(human.get_meaning())  # "NCBITaxon:9606"
print(human.get_description())  # "Homo sapiens (human)"

# Cell biology with CL and GO mappings
phase = CellCyclePhase.S_PHASE
print(phase.get_meaning())  # "GO:0000084"

neuron = CellType.NEURON
print(neuron.get_meaning())  # "CL:0000540"

# Get all organisms at a specific taxonomic level
mammals = [org for org in CommonOrganismTaxaEnum
           if 'MAMMALIA' in str(org)]
```

## 🏗️ Available Domains

### Core Domains (Most Mature)
- **🧬 Biology**:
  - **Structural Biology**: Cryo-EM techniques, crystallization methods, detectors
  - **Cell Biology**: Cell types, cell cycle phases, organelles
  - **Taxonomy**: Model organisms (all with NCBI Taxonomy IDs)
- **📍 Spatial**: Anatomical directions, planes, relationships (BSPO mapped)
- **📊 Statistics**: Statistical tests (STATO mapped), p-value thresholds

### Expanding Domains
- **🧪 Data Science**: ML model types, dataset splits, metrics
- **⚗️ Materials Science**: Crystal structures, characterization methods
- **🏥 Clinical/Medical**: Blood types (SNOMED), vital status
- **🌍 Environmental**: Exposure routes, pollutants
- **⚡ Energy**: Sources, storage methods, efficiency ratings

### Coming Soon
- **🧭 Geography**: Country codes (ISO), time zones, coordinate systems
- **⏰ Time**: Temporal relationships, periods, frequencies
- **💼 Academic**: Publication types, research roles, funding sources
- **🏭 Industrial**: Manufacturing processes, quality standards

## 🔄 Multiple Use Cases

### 1. **LinkML Standards** (YAML schemas)
Use the raw LinkML schemas for data modeling, validation, and documentation:
```yaml
# Direct schema usage
Person:
  attributes:
    vital_status:
      range: VitalStatusEnum  # ALIVE, DECEASED, UNKNOWN
```

### 2. **Python Programming** (Rich Enums)
Get Python enums with full IDE support, type checking, and semantic metadata:
```python
# Type-safe enums with ontology mappings
status = VitalStatusEnum.ALIVE  
print(status.meaning)  # "NCIT:C37987"
```

### 3. **"Stealth Semantics"**
Write simple code, get semantic meaning automatically:
```python
# Example: Different systems use different names for the same concept
from valuesets.enums.medical import BloodTypeEnum
from external_system import PatientBloodType  # Third-party enum

# Even though the enum values might be named differently:
# BloodTypeEnum.A_POSITIVE vs PatientBloodType.A_POS
# They map to the same SNOMED code: SNOMED:278149003

if blood_type.get_meaning() == patient_blood.get_meaning():
    # Semantic interoperability - works across different naming conventions
    process_compatible_blood_type()

# Or use the utility function
if same_meaning_as(blood_type, patient_blood):
    process_compatible_blood_type()
```

### 4. **Multi-language Interoperability**
Generate schemas and types for any language:

```bash
# Generate JSON Schema for web apps
gen-jsonschema schema.yaml

# Generate TypeScript definitions  
gen-typescript schema.yaml -t typescript

# Generate JSON-LD
gen-jsonld schema.yaml
```

### 5. **Integration & Tooling**
- **Excel/Google Sheets**: Generate dropdown validation lists
- **Web forms**: Auto-generate select options with descriptions
- **APIs**: Standardized response codes and classifications
- **Databases**: Consistent foreign key constraints

## 🛠️ Advanced Features

### Hierarchical Relationships

```python
# Some enums support hierarchical is_a relationships
from valuesets.enums import ViralGenomeTypeEnum

# Baltimore classification with hierarchy
positive_rna = ViralGenomeTypeEnum.SSRNA_POSITIVE  # Group IV
# inherits from SSRNA (single-stranded RNA)
```

### Rich Metadata

```python
from valuesets.enums.bio.structural_biology import CryoEMGridType

grid = CryoEMGridType.QUANTIFOIL
metadata = grid.get_metadata()
print(metadata)
# {
#   'name': 'QUANTIFOIL',
#   'value': 'QUANTIFOIL',
#   'description': 'Quantifoil holey carbon grid',
#   'annotations': {
#     'hole_sizes': '1.2/1.3, 2/1, 2/2 μm common',
#     'manufacturer': 'Quantifoil'
#   }
# }

# Get all grid types with their descriptions at once
all_grids = CryoEMGridType.get_all_descriptions()
# {'C_FLAT': 'C-flat holey carbon grid', 'QUANTIFOIL': ...}
```

### Utility Functions

```python
from valuesets.enums.spatial import AnatomicalPlane

# Get all ontology mappings for an enum
mappings = AnatomicalPlane.get_all_meanings()
print(mappings)
# {'SAGITTAL': 'BSPO:0000417', 'CORONAL': 'BSPO:0000019', ...}

# List all metadata for every value in an enum
all_metadata = AnatomicalPlane.list_metadata()
for name, meta in all_metadata.items():
    print(f"{name}: {meta.get('description', 'No description')}")

# Find enum by ontology term (useful for data integration)
plane = AnatomicalPlane.from_meaning("BSPO:0000417")  # Returns SAGITTAL
```

### Dynamic Enums

Some enums in this collection are **dynamic enums** that can be expanded at runtime by querying ontologies. This uses LinkML's [Dynamic Enum](https://linkml.io/linkml/schemas/enums.html#dynamic-enums) feature.

```yaml
# Example: A dynamic enum that pulls values from an ontology
CellTypeEnum:
  # Dynamic expansion from Cell Ontology
  reachable_from:
    source_ontology: obo:cl
    source_nodes:
      - CL:0000540  # neuron
    include_self: false
    relationship_types:
      - rdfs:subClassOf
```

**Note**: Runtime expansion support is coming soon! Currently, dynamic enums provide:
- ✅ Static values with ontology mappings
- ✅ Metadata and descriptions
- 🚧 Runtime expansion from ontologies (coming in next release)

When runtime expansion is available, you'll be able to:
```python
# Future: Dynamically expand enum with all neuron subtypes
cell_types = CellTypeEnum.expand_from_ontology()
# Would add: MOTOR_NEURON, SENSORY_NEURON, INTERNEURON, etc.
```

## 📖 Documentation

[**Full Documentation Website →**](https://linkml.io/valuesets/)

### OWL/RDF Representation

The value sets are also available as an OWL ontology for semantic web applications and ontology browsers:

- **Direct Download**: [https://w3id.org/valuesets/valuesets.owl.ttl](https://w3id.org/valuesets/valuesets.owl.ttl)
- **BioPortal**: Available at [BioPortal](https://bioportal.bioontology.org/ontologies/VALUESETS)
- **Ontology Lookup Service (OLS)**: Submission planned for [OLS](https://www.ebi.ac.uk/ols/)

The OWL representation allows you to:
- Browse value sets in ontology browsers
- Perform SPARQL queries
- Integrate with semantic web applications
- Link to other biomedical ontologies

## 🚀 Future Directions

### Maturity Levels
We plan to add maturity level metadata to each enum to help users understand their readiness:

- **🟢 Stable**: Production-ready, well-tested, unlikely to change
- **🟡 Beta**: Usable but may have minor changes
- **🔴 Draft**: Under development, expect changes

```python
# Future: Check maturity before use
if enum_def.maturity_level == MaturityLevel.STABLE:
    use_in_production()
```

### Modularization
Split the package into domain-specific modules for lighter installs:

```bash
# Future: Install only what you need
pip install valuesets-core        # Core functionality
pip install valuesets-bio         # Biological domains
pip install valuesets-materials   # Materials science
pip install valuesets-clinical    # Clinical/medical
```

### Community Extensions
- **Domain Packages**: Community-maintained domain-specific value sets
- **Organization Standards**: Company/institution-specific enums that extend base sets
- **Mapping Tables**: Cross-ontology and cross-standard mappings

### Advanced Features
- **🤖 AI/LLM Integration**: Semantic annotations optimized for language models
- **📊 Usage Analytics**: Track which enums are most used, identify gaps
- **🔄 Version Management**: Handle enum evolution with deprecation warnings
- **🌐 Multi-ontology Support**: Map single values to multiple ontologies
- **🔍 Fuzzy Matching**: Find enums by approximate string matching

## 🏗️ Development

### Installation
```bash
git clone https://github.com/linkml/valuesets
cd valuesets
uv install
```

### Available Commands
```bash
just --list  # Show all available commands
just test    # Run tests  
just doctest # Run doctests
just lint    # Run linting
just site    # Build documentation site
```

## 🤝 Contributing

We welcome contributions! Whether you're adding new domains, improving existing enums, or fixing bugs:

1. **Domain Experts**: Contribute standardized value sets for your field
2. **Developers**: Add utility functions, improve tooling, fix issues  
3. **Users**: Report missing enums, suggest improvements, share use cases

## 📁 Repository Structure

```
├── src/valuesets/
│   ├── schema/              # 📝 LinkML YAML schemas (source of truth)
│   │   ├── bio/            # Biological domains
│   │   │   ├── cell_biology.yaml
│   │   │   ├── structural_biology.yaml
│   │   │   └── taxonomy.yaml
│   │   ├── spatial/        # Spatial and anatomical
│   │   │   └── spatial_qualifiers.yaml
│   │   ├── statistics.yaml
│   │   └── core.yaml
│   ├── enums/              # 🐍 Generated Python enums
│   │   └── <auto-generated from schemas>
│   ├── generators/         # 🔧 Rich enum generator
│   │   └── rich_enum.py
│   └── validators/         # ✓ Ontology validation
│       └── enum_evaluator.py
├── docs/                   # 📚 Documentation
└── tests/                  # 🧪 Test cases
    ├── test_rich_enums.py  # Rich enum functionality
    └── validators/         # Ontology validation tests
```

## 📜 Credits

Built with [LinkML](https://linkml.io/) and the [linkml-project-copier](https://github.com/dalito/linkml-project-copier) template.

---

*Making data standardization simple, semantic, and scalable* 🚀
