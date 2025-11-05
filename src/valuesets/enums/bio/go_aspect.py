"""
Gene Ontology Aspects

The three main aspects of Gene Ontology - Molecular Function, Biological Process, and Cellular Component

Generated from: bio/go_aspect.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class GOAspect(RichEnum):
    """
    The three main aspects (namespaces) of Gene Ontology
    """
    # Enum members
    F = "F"
    P = "P"
    C = "C"

# Set metadata after class creation
GOAspect._metadata = {
    "F": {'description': 'The activities that occur at the molecular level, such as catalysis or binding', 'meaning': 'GO:0003674', 'aliases': ['molecular_function', 'MF']},
    "P": {'description': 'The larger processes accomplished by multiple molecular activities', 'meaning': 'GO:0008150', 'aliases': ['biological_process', 'BP']},
    "C": {'description': 'The locations relative to cellular structures in which a gene product performs a function', 'meaning': 'GO:0005575', 'aliases': ['cellular_component', 'CC']},
}

__all__ = [
    "GOAspect",
]