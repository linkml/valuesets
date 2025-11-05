"""
Ontology and Semantic Web Value Sets

Value sets for ontologies, semantic web standards, and knowledge representation.


Generated from: computing/ontologies.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class OWLProfileEnum(RichEnum):
    """
    OWL 2 profiles that provide different tradeoffs between expressiveness and computational complexity
    """
    # Enum members
    OWL_2_EL = "OWL_2_EL"
    OWL_2_QL = "OWL_2_QL"
    OWL_2_RL = "OWL_2_RL"
    OWL_2_DL = "OWL_2_DL"
    OWL_2_FULL = "OWL_2_FULL"

# Set metadata after class creation
OWLProfileEnum._metadata = {
    "OWL_2_EL": {'description': 'OWL 2 EL (Existential Language) - optimized for applications using very large ontologies with basic relationships. Provides polynomial time reasoning.', 'annotations': {'complexity': 'polynomial time', 'use_case': 'large biomedical ontologies, SNOMED CT'}},
    "OWL_2_QL": {'description': 'OWL 2 QL (Query Language) - optimized for query answering over large data repositories. Based on DL-Lite family.', 'annotations': {'complexity': 'LogSpace data complexity', 'use_case': 'ontology-based data access, database integration'}},
    "OWL_2_RL": {'description': 'OWL 2 RL (Rule Language) - optimized for rule-based reasoning and can be implemented using rule engines. Compatible with RDF Schema.', 'annotations': {'complexity': 'polynomial time', 'use_case': 'business rules, policy systems'}},
    "OWL_2_DL": {'description': 'OWL 2 DL (Description Logic) - full expressiveness while maintaining computational completeness and decidability. Maximum expressiveness without sacrificing decidability.', 'annotations': {'complexity': 'NExpTime', 'use_case': 'general purpose ontologies requiring high expressiveness'}},
    "OWL_2_FULL": {'description': 'OWL 2 Full - maximum expressiveness with no restrictions, but reasoning is undecidable. Allows full RDF capabilities.', 'annotations': {'complexity': 'undecidable', 'use_case': 'maximum flexibility, no guaranteed reasoning'}},
}

__all__ = [
    "OWLProfileEnum",
]