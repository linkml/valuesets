# Dynamic Value Sets and Validation

Dynamic value sets are a powerful feature in LinkML that allows enums to be populated dynamically from ontologies rather than having hardcoded permissible values. This enables validation against large, evolving controlled vocabularies without manually maintaining enum lists.

## What are Dynamic Value Sets?

Dynamic value sets use the `reachable_from` specification to define enums that are populated from ontology terms. Instead of listing every possible value, you specify:

- **Source ontology**: The ontology to query
- **Source nodes**: Root terms to start from  
- **Relationship types**: How to traverse the ontology (e.g., subClassOf)
- **Include self**: Whether to include the root terms themselves

## Available Dynamic Value Sets

The `valuesets` repository contains numerous dynamic value sets across different domains:

### Biological Entities (`bio/bio_entities.yaml`)

#### Cell Types
```yaml
CellType:
  description: Any cell type from the Cell Ontology (CL)
  reachable_from:
    source_ontology: obo:cl
    source_nodes:
      - CL:0000000  # cell
    include_self: true
    relationship_types:
      - rdfs:subClassOf
```

#### Diseases
```yaml
Disease:
  description: Human diseases from the Mondo Disease Ontology
  reachable_from:
    source_ontology: obo:mondo
    source_nodes:
      - MONDO:0000001  # disease
    include_self: true
    relationship_types:
      - rdfs:subClassOf
```

#### Chemical Entities
```yaml
ChemicalEntity:
  description: Any chemical entity from ChEBI ontology
  reachable_from:
    source_ontology: obo:chebi
    source_nodes:
      - CHEBI:24431  # chemical entity
    include_self: true
    relationship_types:
      - rdfs:subClassOf
```

### Anatomical Structures
```yaml
MetazoanAnatomicalStructure:
  description: Any anatomical structure found in metazoan organisms
  reachable_from:
    source_ontology: obo:uberon
    source_nodes:
      - UBERON:0000061  # anatomical structure
    include_self: true
    relationship_types:
      - rdfs:subClassOf
```

### Taxonomy (`bio/taxonomy.yaml`)
```yaml
OrganismTaxonEnum:
  description: All organism taxa from NCBI Taxonomy
  reachable_from:
    source_nodes:
      - NCBITaxon:1  # root
    is_direct: false
    relationship_types:
      - rdfs:subClassOf
```

### Investigation Protocols (`investigation.yaml`)
```yaml
StudyDesignEnum:
  description: Study design classifications from OBI
  reachable_from:
    source_nodes:
      - OBI:0500000  # study design
    is_direct: false
    relationship_types:
      - rdfs:subClassOf
```

## Using Dynamic Value Sets in Schemas

### Basic Usage
```yaml
# In your schema file
slots:
  cell_type:
    description: Type of cell being studied
    range: CellType  # References the dynamic enum

  disease:
    description: Disease under investigation  
    range: Disease   # References the dynamic enum
```

### Instance Data Validation
```yaml
# Example instance data
person:
  cell_type: CL:0000540  # neuron
  disease: MONDO:0005148  # type 2 diabetes mellitus
```

## Validation Approaches

### 1. Static Validation
Current LinkML validators can check that values match the ontology prefix patterns:

```python
from linkml.validators.jsonschemavalidator import JsonSchemaValidator

# Validate that cell type follows CL: pattern
validator = JsonSchemaValidator(schema="path/to/schema.yaml")
report = validator.validate(instance_data)
```

### 2. Ontology-based Validation

For full dynamic validation, you can use ontology access tools:

```python
from oaklib import get_adapter
from linkml_runtime.utils.schemaview import SchemaView

# Load ontology adapter
cl_adapter = get_adapter("obo:cl")

# Check if a term is a valid cell type
def validate_cell_type(term_id: str) -> bool:
    """Validate that term_id is a subclass of cell (CL:0000000)"""
    return cl_adapter.is_subclass_of(term_id, "CL:0000000")

# Example usage
is_valid = validate_cell_type("CL:0000540")  # True - neuron is a cell
```

### 3. Batch Validation with OAK

```python
from oaklib import get_adapter

def validate_disease_terms(term_ids: list[str]) -> dict[str, bool]:
    """Validate multiple disease terms against MONDO"""
    mondo_adapter = get_adapter("obo:mondo")
    results = {}
    
    for term_id in term_ids:
        try:
            # Check if term exists and is a disease
            is_valid = mondo_adapter.is_subclass_of(term_id, "MONDO:0000001")
            results[term_id] = is_valid
        except Exception:
            results[term_id] = False
            
    return results

# Example usage
disease_terms = ["MONDO:0005148", "MONDO:0004992", "INVALID:123"]
validation_results = validate_disease_terms(disease_terms)
```

## Practical Examples

### Example 1: Cell Biology Study

```yaml
# Schema definition
classes:
  CellExperiment:
    attributes:
      cell_type:
        range: CellType
        required: true
      treatment_compound:
        range: ChemicalEntity
        required: false

# Instance data
experiment_1:
  cell_type: CL:0000540      # neuron
  treatment_compound: CHEBI:15377  # water

experiment_2:  
  cell_type: CL:0000136      # fat cell
  treatment_compound: CHEBI:27732  # caffeine
```

### Example 2: Disease Research

```yaml
# Schema definition  
classes:
  DiseaseStudy:
    attributes:
      primary_disease:
        range: Disease
        required: true
      comorbidities:
        range: Disease
        multivalued: true
      affected_anatomy:
        range: MetazoanAnatomicalStructure
        multivalued: true

# Instance data
diabetes_study:
  primary_disease: MONDO:0005148        # type 2 diabetes
  comorbidities:
    - MONDO:0005267                     # heart disease  
    - MONDO:0005147                     # type 1 diabetes
  affected_anatomy:
    - UBERON:0001264                    # pancreas
    - UBERON:0004535                    # cardiovascular system
```

### Example 3: Taxonomic Classification

```yaml
# Schema definition
classes:
  OrganismSample:
    attributes:
      species:
        range: OrganismTaxonEnum  
        required: true
      genus:
        range: OrganismTaxonEnum
        required: false
        
# Instance data
mouse_sample:
  species: NCBITaxon:10090     # Mus musculus (house mouse)
  genus: NCBITaxon:10088       # Mus (mouse genus)

human_sample:
  species: NCBITaxon:9606      # Homo sapiens
  genus: NCBITaxon:9605        # Homo
```

## Validation Tools and Libraries

### OAK (Ontology Access Kit)
The primary tool for working with ontologies in the LinkML ecosystem:

```bash
# Install OAK
pip install oaklib

# Basic ontology queries
runoak -i obo:cl descendants CL:0000000  # All cell types
runoak -i obo:mondo info MONDO:0005148   # Diabetes info  
runoak -i obo:chebi ancestors CHEBI:15377 # Water ancestors
```

### Custom Validation Functions

```python
from oaklib import get_adapter
from typing import Dict, List, Optional

class DynamicEnumValidator:
    """Validator for dynamic enums using ontology lookup"""
    
    def __init__(self):
        self.adapters = {
            'cl': get_adapter('obo:cl'),
            'mondo': get_adapter('obo:mondo'), 
            'chebi': get_adapter('obo:chebi'),
            'uberon': get_adapter('obo:uberon'),
            'ncbitaxon': get_adapter('obo:ncbitaxon')
        }
    
    def validate_term(self, term_id: str, root_term: str) -> bool:
        """Validate that term_id is reachable from root_term"""
        prefix = term_id.split(':')[0].lower()
        if prefix not in self.adapters:
            return False
            
        adapter = self.adapters[prefix]
        try:
            return adapter.is_subclass_of(term_id, root_term)
        except Exception:
            return False
    
    def validate_cell_type(self, term_id: str) -> bool:
        """Validate cell type against CL:0000000"""
        return self.validate_term(term_id, "CL:0000000")
    
    def validate_disease(self, term_id: str) -> bool:
        """Validate disease against MONDO:0000001"""
        return self.validate_term(term_id, "MONDO:0000001")
        
    def validate_chemical(self, term_id: str) -> bool:
        """Validate chemical against CHEBI:24431"""
        return self.validate_term(term_id, "CHEBI:24431")

# Usage example
validator = DynamicEnumValidator()
print(validator.validate_cell_type("CL:0000540"))    # True
print(validator.validate_disease("MONDO:0005148"))   # True  
print(validator.validate_chemical("CHEBI:15377"))    # True
```

## Best Practices

### 1. Choose Appropriate Root Terms
- Use specific enough root terms to avoid overly broad value sets
- For cell types, consider using specific cell lineages rather than the root "cell" term
- For diseases, use disease categories (infectious, genetic, etc.) when appropriate

### 2. Include Ontology Prefixes in Schema
```yaml
prefixes:
  CL: http://purl.obolibrary.org/obo/CL_
  MONDO: http://purl.obolibrary.org/obo/MONDO_ 
  CHEBI: http://purl.obolibrary.org/obo/CHEBI_
  UBERON: http://purl.obolibrary.org/obo/UBERON_
```

### 3. Validate During Development
- Test dynamic enums with representative data during schema development
- Use OAK to explore ontology hierarchies before choosing root terms
- Document expected term formats and validation requirements

### 4. Handle Validation Errors Gracefully
```python
def safe_validate_term(term_id: str, validator_func) -> Optional[bool]:
    """Safely validate a term with error handling"""
    try:
        return validator_func(term_id)
    except Exception as e:
        print(f"Validation error for {term_id}: {e}")
        return None
```

## Limitations and Considerations

### Current Limitations
- Runtime enum expansion is still under development
- Some ontology adapters may require internet connectivity
- Large ontologies can make validation slow
- Not all ontologies may be available through OAK

### Performance Considerations  
- Cache ontology adapters when validating multiple terms
- Consider using local ontology files for better performance
- Batch validation calls when possible

### Future Developments
- Automated enum materialization from ontologies
- Better integration with LinkML validators
- Support for more relationship types and boolean combinations
- Subset filtering capabilities

## Additional Resources

- [LinkML Dynamic Enums Documentation](https://linkml.io/linkml/schemas/enums.html#dynamic-enums)
- [OAK (Ontology Access Kit) Documentation](https://incatools.github.io/ontology-access-kit/)
- [LinkML GitHub Discussion on Dynamic Enums](https://github.com/orgs/linkml/discussions/2300)
- [BioPortal Ontology Repository](https://bioportal.bioontology.org/)
- [OBO Foundry Ontologies](http://www.obofoundry.org/)

---

*This documentation covers the current state of dynamic value set validation in LinkML. As the framework continues to evolve, some features may become available that aren't yet implemented.*