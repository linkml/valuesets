"""

Generated from: bio/viral_genome_types.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class ViralGenomeTypeEnum(RichEnum):
    """
    Types of viral genomes based on Baltimore classification
    """
    # Enum members
    DNA = "DNA"
    DSDNA = "DSDNA"
    SSDNA = "SSDNA"
    RNA = "RNA"
    DSRNA = "DSRNA"
    SSRNA = "SSRNA"
    SSRNA_POSITIVE = "SSRNA_POSITIVE"
    SSRNA_NEGATIVE = "SSRNA_NEGATIVE"
    SSRNA_RT = "SSRNA_RT"
    DSDNA_RT = "DSDNA_RT"
    MIXED = "MIXED"
    UNCHARACTERIZED = "UNCHARACTERIZED"

# Set metadata after class creation
ViralGenomeTypeEnum._metadata = {
    "DNA": {'description': 'Viral genome composed of DNA', 'meaning': 'CHEBI:16991'},
    "DSDNA": {'description': 'Double-stranded DNA viral genome', 'meaning': 'NCIT:C14348', 'aliases': ['Baltimore Group I', 'Group I']},
    "SSDNA": {'description': 'Single-stranded DNA viral genome', 'meaning': 'NCIT:C14350', 'aliases': ['Baltimore Group II', 'Group II']},
    "RNA": {'description': 'Viral genome composed of RNA', 'meaning': 'CHEBI:33697'},
    "DSRNA": {'description': 'Double-stranded RNA viral genome', 'meaning': 'NCIT:C28518', 'aliases': ['Baltimore Group III', 'Group III']},
    "SSRNA": {'description': 'Single-stranded RNA viral genome', 'meaning': 'NCIT:C95939'},
    "SSRNA_POSITIVE": {'description': 'Positive-sense single-stranded RNA viral genome', 'meaning': 'NCIT:C14351', 'aliases': ['Baltimore Group IV', 'Group IV', '(+)ssRNA']},
    "SSRNA_NEGATIVE": {'description': 'Negative-sense single-stranded RNA viral genome', 'meaning': 'NCIT:C14346', 'aliases': ['Baltimore Group V', 'Group V', '(-)ssRNA']},
    "SSRNA_RT": {'description': 'Single-stranded RNA viruses that replicate through a DNA intermediate (retroviruses)', 'meaning': 'NCIT:C14347', 'aliases': ['Baltimore Group VI', 'Group VI', 'Retroviruses']},
    "DSDNA_RT": {'description': 'Double-stranded DNA viruses that replicate through a single-stranded RNA intermediate (pararetroviruses)', 'meaning': 'NCIT:C14349', 'aliases': ['Baltimore Group VII', 'Group VII', 'Pararetroviruses']},
    "MIXED": {'description': 'Mixed or hybrid viral genome type', 'meaning': 'NCIT:C128790'},
    "UNCHARACTERIZED": {'description': 'Viral genome type not yet characterized', 'meaning': 'NCIT:C17998'},
}

__all__ = [
    "ViralGenomeTypeEnum",
]