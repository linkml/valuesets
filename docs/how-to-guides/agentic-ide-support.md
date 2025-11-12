# Using Common Value Sets with Agentic IDE Support via Context7 MCP

This guide shows you how to leverage Context7 MCP (Model Context Protocol) for enhanced agentic support when working with Common Value Sets in your IDE.

## 🤖 What is Agentic IDE Support?

Agentic IDE support refers to AI assistants that can:
- Access up-to-date documentation in real-time
- Understand your specific codebase context
- Provide accurate code suggestions with proper valuesets
- Execute complex workflows with domain-specific knowledge

Context7 MCP enables this by dynamically fetching current documentation and injecting it into your AI assistant's context.

## 🛠️ Prerequisites

- **Node.js** v18.0.0 or higher
- **Compatible IDE/Editor** with MCP support:
  - Claude Desktop
  - Cursor
  - VS Code with appropriate extensions
  - Windsurf
  - Zed
- **Common Value Sets** installed in your project

## 📦 Installation & Setup

### 1. Install Context7 MCP Server

#### Option A: Using Smithery CLI (Recommended for Claude Desktop)
```bash
npx -y @smithery/cli install @upstash/context7-mcp --client claude
```

#### Option B: Manual Configuration

For **Claude Desktop**, add to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp@latest"]
    }
  }
}
```

For **Cursor**, add to your MCP configuration:
```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp@latest"]
    }
  }
}
```

For **VS Code**, configure in your settings.json:
```json
{
  "mcp.servers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp@latest"]
    }
  }
}
```

### 2. Install Common Value Sets

```bash
pip install valuesets
```

Or add to your requirements:
```txt
valuesets>=0.1.0
```

## 🚀 Usage Patterns

### Basic Pattern: Context-Aware Code Generation

Use the `use context7` directive to get up-to-date valuesets documentation:

**Prompt:**
```
Create a data validation function using Common Value Sets for binary classification. use context7
```

**AI Response will include:**
- Current API documentation for Common Value Sets
- Accurate enum imports and usage
- Proper semantic meaning access
- Version-specific examples

### Advanced Pattern: Domain-Specific Workflows

**Prompt:**
```
Build a bioinformatics pipeline using Common Value Sets for organism taxonomy and experimental techniques. Include validation and semantic mapping. use context7
```

**Expected AI capabilities:**
- Access to current LinkML schema documentation
- Knowledge of available biological enumerations
- Proper ontology term usage (NCBITaxon, OBO terms)
- Integration patterns with semantic web standards

## 🎯 Practical Examples

### Example 1: Data Science Classification

**Prompt:**
```python
# Create a machine learning model validator using Common Value Sets
# Include binary classification, anomaly detection, and fraud detection enums
# use context7
```

**AI will generate:**
```python
from valuesets.enums.data_science.binary_classification import (
    BinaryClassificationEnum,
    AnomalyDetectionEnum,
    FraudDetectionEnum
)
from typing import Union, Dict, Any
import pandas as pd

def validate_predictions(
    predictions: pd.Series,
    task_type: str
) -> Dict[str, Any]:
    """
    Validate model predictions against Common Value Sets standards.
    """
    validation_enums = {
        'binary': BinaryClassificationEnum,
        'anomaly': AnomalyDetectionEnum,
        'fraud': FraudDetectionEnum
    }

    if task_type not in validation_enums:
        raise ValueError(f"Unknown task type: {task_type}")

    enum_class = validation_enums[task_type]
    valid_values = {item.value for item in enum_class}

    # Validate predictions
    invalid_predictions = predictions[~predictions.isin(valid_values)]

    return {
        'valid_count': len(predictions) - len(invalid_predictions),
        'invalid_count': len(invalid_predictions),
        'invalid_values': invalid_predictions.unique().tolist(),
        'expected_values': list(valid_values),
        'semantic_mappings': {
            item.value: item.get_meaning() if hasattr(item, 'get_meaning') else None
            for item in enum_class
        }
    }

# Example usage
predictions = pd.Series(['POSITIVE', 'NEGATIVE', 'MAYBE'])  # 'MAYBE' is invalid
result = validate_predictions(predictions, 'binary')
print(f"Validation result: {result}")
```

### Example 2: Bioinformatics Integration

**Prompt:**
```
Create a sample metadata validator for genomics experiments using Common Value Sets. Include organism taxonomy, experimental techniques, and cell cycle phases. use context7
```

**AI will generate:**
```python
from valuesets.enums.bio.taxonomy import CommonOrganismTaxaEnum
from valuesets.enums.bio.cell_cycle import CellCyclePhase
from valuesets.enums.bio.structural_biology import StructuralBiologyTechnique
from dataclasses import dataclass
from typing import Optional, List, Dict

@dataclass
class GenomicsExperiment:
    """
    Standardized genomics experiment metadata using Common Value Sets.
    """
    organism: CommonOrganismTaxaEnum
    technique: StructuralBiologyTechnique
    cell_phase: Optional[CellCyclePhase] = None

    def validate(self) -> Dict[str, any]:
        """Validate experiment metadata and return semantic information."""
        return {
            'organism': {
                'value': self.organism.value,
                'meaning': self.organism.get_meaning(),
                'description': self.organism.get_description()
            },
            'technique': {
                'value': self.technique.value,
                'meaning': self.technique.get_meaning(),
                'description': self.technique.get_description()
            },
            'cell_phase': {
                'value': self.cell_phase.value if self.cell_phase else None,
                'meaning': self.cell_phase.get_meaning() if self.cell_phase else None,
                'description': self.cell_phase.get_description() if self.cell_phase else None
            } if self.cell_phase else None
        }

    def to_rdf_triples(self) -> List[str]:
        """Convert to RDF triples for semantic web integration."""
        triples = []
        base_uri = "http://example.org/experiment/"

        # Organism triple
        if hasattr(self.organism, 'get_meaning') and self.organism.get_meaning():
            triples.append(f"<{base_uri}organism> <http://purl.obolibrary.org/obo/RO_0002162> <{self.organism.get_meaning()}> .")

        # Technique triple
        if hasattr(self.technique, 'get_meaning') and self.technique.get_meaning():
            triples.append(f"<{base_uri}technique> <http://purl.obolibrary.org/obo/BFO_0000051> <{self.technique.get_meaning()}> .")

        return triples

# Example usage
experiment = GenomicsExperiment(
    organism=CommonOrganismTaxaEnum.MOUSE,
    technique=StructuralBiologyTechnique.CRYO_EM,
    cell_phase=CellCyclePhase.G1
)

print("Validation:", experiment.validate())
print("RDF Triples:", experiment.to_rdf_triples())
```

## 🎪 Advanced Agentic Workflows

### Multi-Step Data Harmonization

**Prompt:**
```
Create an intelligent data harmonization system that:
1. Detects data types in CSV files
2. Maps values to appropriate Common Value Sets enums
3. Suggests ontology alignments
4. Generates standardized output with semantic annotations
use context7
```

With Context7, the AI will have access to:
- Current schema documentation
- All available enum categories
- Ontology mapping patterns
- Best practices for LinkML integration

### Semantic Query Generation

**Prompt:**
```
Build a SPARQL query generator that uses Common Value Sets semantic mappings to create complex biological queries. Include support for GO terms, taxonomy, and experimental conditions. use context7
```

The AI will generate code that properly leverages the ontology term mappings embedded in Common Value Sets.

## 🔧 Configuration Tips

### Optimize Context7 for ValueSets

1. **Custom Documentation Sources**: Configure Context7 to prioritize LinkML and Common Value Sets documentation
2. **Version Pinning**: Ensure Context7 fetches documentation for your specific valuesets version
3. **Domain Focus**: Use domain-specific prompts to get targeted documentation

### IDE-Specific Optimizations

#### For Cursor:
- Enable auto-completion for enum imports
- Configure semantic highlighting for ontology terms
- Set up code actions for value validation

#### For Claude Desktop:
- Use conversation memory for complex workflows
- Leverage file upload for schema validation
- Enable multi-turn planning for data harmonization

#### For VS Code:
- Install LinkML extension for schema validation
- Configure Python language server for enum type hints
- Set up debugging for semantic mapping functions

## 🔍 Troubleshooting

### Common Issues

1. **Context7 not responding**
   - Check Node.js version (≥18.0.0)
   - Verify MCP configuration syntax
   - Restart your IDE

2. **Outdated documentation**
   - Clear Context7 cache
   - Update to latest Context7 version
   - Check internet connectivity

3. **Import errors with valuesets**
   - Ensure valuesets is installed in correct environment
   - Check Python path configuration
   - Verify package version compatibility

### Performance Optimization

- Use specific enum imports rather than wildcard imports
- Cache semantic mappings for repeated lookups
- Batch validation operations when possible

## 🌟 Best Practices

1. **Prompt Engineering**
   - Always include "use context7" for up-to-date information
   - Be specific about the valuesets domain you're working with
   - Ask for semantic mappings when working with ontology integration

2. **Code Organization**
   - Group related enums by domain
   - Use type hints for better IDE support
   - Document semantic mappings in your code

3. **Validation Patterns**
   - Validate inputs against enum values
   - Leverage semantic meanings for data integration
   - Provide clear error messages with valid options

4. **Semantic Integration**
   - Use ontology terms for data interoperability
   - Generate RDF when needed for knowledge graphs
   - Preserve provenance information

## 🚀 Next Steps

- Explore the [Common Value Sets documentation](https://linkml.github.io/valuesets/)
- Learn about [LinkML schemas](https://linkml.io/)
- Check out [Model Context Protocol](https://modelcontextprotocol.io/)
- Contribute new enumerations to the Common Value Sets project

With Context7 MCP and Common Value Sets, you can build intelligent, semantically-aware applications with unprecedented ease and accuracy. The AI assistant becomes your domain expert, providing up-to-date, accurate guidance for standardized data representation across scientific domains.