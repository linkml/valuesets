"""
Currency Chemicals Value Sets

Value sets for metabolic currency molecules and cofactors used in energy transfer and redox reactions

Generated from: bio/currency_chemicals.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class CurrencyChemical(RichEnum):
    """
    Common metabolic currency molecules and cofactors that serve as energy carriers, electron donors/acceptors, and group transfer agents in cellular metabolism.
    """
    # Enum members
    ATP = "ATP"
    ADP = "ADP"
    AMP = "AMP"
    GTP = "GTP"
    GDP = "GDP"
    NAD_PLUS = "NAD_PLUS"
    NADH = "NADH"
    NADP_PLUS = "NADP_PLUS"
    NADPH = "NADPH"
    FAD = "FAD"
    FADH2 = "FADH2"
    COA = "COA"
    ACETYL_COA = "ACETYL_COA"

# Set metadata after class creation
CurrencyChemical._metadata = {
    "ATP": {'description': 'Adenosine triphosphate - primary energy currency molecule in cells', 'meaning': 'CHEBI:15422'},
    "ADP": {'description': 'Adenosine diphosphate - product of ATP hydrolysis, energy acceptor', 'meaning': 'CHEBI:16761'},
    "AMP": {'description': 'Adenosine monophosphate - nucleotide, product of ADP hydrolysis', 'meaning': 'CHEBI:16027', 'aliases': ["adenosine 5'-monophosphate"]},
    "GTP": {'description': 'Guanosine triphosphate - energy molecule, protein synthesis and signaling', 'meaning': 'CHEBI:15996'},
    "GDP": {'description': 'Guanosine diphosphate - product of GTP hydrolysis', 'meaning': 'CHEBI:17552'},
    "NAD_PLUS": {'description': 'Nicotinamide adenine dinucleotide (oxidized) - electron acceptor in catabolism', 'meaning': 'CHEBI:15846'},
    "NADH": {'description': 'Nicotinamide adenine dinucleotide (reduced) - electron donor, reducing agent', 'meaning': 'CHEBI:16908'},
    "NADP_PLUS": {'description': 'Nicotinamide adenine dinucleotide phosphate (oxidized) - electron acceptor', 'meaning': 'CHEBI:18009'},
    "NADPH": {'description': 'Nicotinamide adenine dinucleotide phosphate (reduced) - anabolic reducing agent', 'meaning': 'CHEBI:16474'},
    "FAD": {'description': 'Flavin adenine dinucleotide (oxidized) - electron acceptor in oxidation reactions', 'meaning': 'CHEBI:16238'},
    "FADH2": {'description': 'Flavin adenine dinucleotide (reduced) - electron donor in electron transport chain', 'meaning': 'CHEBI:17877'},
    "COA": {'description': 'Coenzyme A - acyl group carrier in fatty acid metabolism', 'meaning': 'CHEBI:15346', 'aliases': ['coenzyme A']},
    "ACETYL_COA": {'description': 'Acetyl coenzyme A - central metabolic intermediate, links glycolysis to citric acid cycle', 'meaning': 'CHEBI:15351'},
}

__all__ = [
    "CurrencyChemical",
]