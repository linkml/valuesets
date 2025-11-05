"""
Gene Ontology Causality Value Sets

Value sets for GO causal relationships and predicates used in gene ontology annotations and pathway analysis

Generated from: bio/go_causality.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class CausalPredicateEnum(RichEnum):
    """
    A term describing the causal relationship between two activities. All terms are drawn from the "causally upstream or within" (RO:0002418) branch of the Relation Ontology (RO).
    """
    # Enum members
    CONSTITUTIVELY_UPSTREAM_OF = "CONSTITUTIVELY_UPSTREAM_OF"
    PROVIDES_INPUT_FOR = "PROVIDES_INPUT_FOR"
    REMOVES_INPUT_FOR = "REMOVES_INPUT_FOR"
    CAUSALLY_UPSTREAM_OF = "CAUSALLY_UPSTREAM_OF"
    CAUSALLY_UPSTREAM_OF_POSITIVE_EFFECT = "CAUSALLY_UPSTREAM_OF_POSITIVE_EFFECT"
    CAUSALLY_UPSTREAM_OF_NEGATIVE_EFFECT = "CAUSALLY_UPSTREAM_OF_NEGATIVE_EFFECT"
    REGULATES = "REGULATES"
    NEGATIVELY_REGULATES = "NEGATIVELY_REGULATES"
    POSITIVELY_REGULATES = "POSITIVELY_REGULATES"
    DIRECTLY_NEGATIVELY_REGULATES = "DIRECTLY_NEGATIVELY_REGULATES"
    INDIRECTLY_NEGATIVELY_REGULATES = "INDIRECTLY_NEGATIVELY_REGULATES"
    DIRECTLY_POSITIVELY_REGULATES = "DIRECTLY_POSITIVELY_REGULATES"
    INDIRECTLY_POSITIVELY_REGULATES = "INDIRECTLY_POSITIVELY_REGULATES"
    IS_SMALL_MOLECULE_REGULATOR_OF = "IS_SMALL_MOLECULE_REGULATOR_OF"
    IS_SMALL_MOLECULE_ACTIVATOR_OF = "IS_SMALL_MOLECULE_ACTIVATOR_OF"
    IS_SMALL_MOLECULE_INHIBITOR_OF = "IS_SMALL_MOLECULE_INHIBITOR_OF"

# Set metadata after class creation
CausalPredicateEnum._metadata = {
    "CONSTITUTIVELY_UPSTREAM_OF": {'meaning': 'RO:0012009'},
    "PROVIDES_INPUT_FOR": {'meaning': 'RO:0002413'},
    "REMOVES_INPUT_FOR": {'meaning': 'RO:0012010'},
    "CAUSALLY_UPSTREAM_OF": {'meaning': 'RO:0002411', 'aliases': ['undetermined']},
    "CAUSALLY_UPSTREAM_OF_POSITIVE_EFFECT": {'meaning': 'RO:0002304', 'annotations': {'symbol': '+', 'direction': 'POSITIVE'}},
    "CAUSALLY_UPSTREAM_OF_NEGATIVE_EFFECT": {'meaning': 'RO:0002305', 'annotations': {'symbol': '-', 'direction': 'NEGATIVE'}},
    "REGULATES": {'meaning': 'RO:0002211', 'annotations': {'symbol': 'R'}},
    "NEGATIVELY_REGULATES": {'meaning': 'RO:0002212', 'annotations': {'symbol': '-R', 'direction': 'NEGATIVE'}},
    "POSITIVELY_REGULATES": {'meaning': 'RO:0002213', 'annotations': {'symbol': '+R', 'direction': 'POSITIVE'}},
    "DIRECTLY_NEGATIVELY_REGULATES": {'meaning': 'RO:0002630', 'annotations': {'directness': 'DIRECT', 'direction': 'NEGATIVE'}},
    "INDIRECTLY_NEGATIVELY_REGULATES": {'meaning': 'RO:0002409', 'annotations': {'directness': 'INDIRECT', 'direction': 'NEGATIVE'}},
    "DIRECTLY_POSITIVELY_REGULATES": {'meaning': 'RO:0002629', 'annotations': {'directness': 'DIRECT', 'direction': 'POSITIVE'}},
    "INDIRECTLY_POSITIVELY_REGULATES": {'meaning': 'RO:0002407', 'annotations': {'directness': 'INDIRECT', 'direction': 'POSITIVE'}},
    "IS_SMALL_MOLECULE_REGULATOR_OF": {'meaning': 'RO:0012004'},
    "IS_SMALL_MOLECULE_ACTIVATOR_OF": {'meaning': 'RO:0012005', 'annotations': {'direction': 'POSITIVE'}},
    "IS_SMALL_MOLECULE_INHIBITOR_OF": {'meaning': 'RO:0012006', 'annotations': {'direction': 'NEGATIVE'}},
}

__all__ = [
    "CausalPredicateEnum",
]