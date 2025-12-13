"""
Genomics Value Sets

Value sets related to genomics and sequencing

Generated from: bio/genomics.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class CdsPhaseType(RichEnum):
    """
    For features of type CDS (coding sequence), the phase indicates where the feature begins with reference to the reading frame. The phase is one of the integers 0, 1, or 2, indicating the number of bases that should be removed from the beginning of this feature to reach the first base of the next codon.
    """
    # Enum members
    PHASE_0 = "PHASE_0"
    PHASE_1 = "PHASE_1"
    PHASE_2 = "PHASE_2"

# Set metadata after class creation
CdsPhaseType._metadata = {
    "PHASE_0": {'description': 'Zero bases from reading frame to feature start.'},
    "PHASE_1": {'description': 'One base from reading frame to feature start.'},
    "PHASE_2": {'description': 'Two bases from reading frame to feature start.'},
}

class ContigCollectionType(RichEnum):
    """
    The type of the contig set; the type of the 'omics data set. Terms are taken from the Genomics Standards Consortium where possible. See the GSC checklists at https://genomicsstandardsconsortium.github.io/mixs/ for the controlled vocabularies used.
    """
    # Enum members
    ISOLATE = "ISOLATE"
    MAG = "MAG"
    METAGENOME = "METAGENOME"
    METATRANSCRIPTOME = "METATRANSCRIPTOME"
    SAG = "SAG"
    VIRUS = "VIRUS"
    MARKER = "MARKER"

# Set metadata after class creation
ContigCollectionType._metadata = {
    "ISOLATE": {'description': 'Sequences assembled from DNA of isolated organism. Bacteria/Archaea: https://genomicsstandardsconsortium.github.io/mixs/0010003/ Euk: https://genomicsstandardsconsortium.github.io/mixs/0010002/ Virus: https://genomicsstandardsconsortium.github.io/mixs/0010005/ Organelle: https://genomicsstandardsconsortium.github.io/mixs/0010006/ Plasmid: https://genomicsstandardsconsortium.github.io/mixs/0010004/'},
    "MAG": {'description': 'Sequences assembled from DNA of mixed community and binned. MAGs are likely to represent a single taxonomic origin. See checkm2 scores for quality assessment.', 'meaning': 'mixs:0010011', 'aliases': ['Metagenome-Assembled Genome']},
    "METAGENOME": {'description': 'Sequences assembled from DNA of mixed community.', 'meaning': 'mixs:0010007'},
    "METATRANSCRIPTOME": {'description': 'Sequences assembled from RNA of mixed community. Currently not represented by GSC.'},
    "SAG": {'description': 'Sequences assembled from DNA of single cell.', 'meaning': 'mixs:0010010', 'aliases': ['Single Amplified Genome']},
    "VIRUS": {'description': 'Sequences assembled from uncultivated virus genome (DNA/RNA).', 'meaning': 'mixs:0010012'},
    "MARKER": {'description': 'Sequences from targeted region of DNA; see protocol for information on targeted region. specimen: https://genomicsstandardsconsortium.github.io/mixs/0010009/ survey: https://genomicsstandardsconsortium.github.io/mixs/0010008/'},
}

class StrandType(RichEnum):
    """
    The strand that a feature appears on relative to a landmark. Also encompasses unknown or irrelevant strandedness.
    """
    # Enum members
    NEGATIVE = "NEGATIVE"
    POSITIVE = "POSITIVE"
    UNKNOWN = "UNKNOWN"
    UNSTRANDED = "UNSTRANDED"

# Set metadata after class creation
StrandType._metadata = {
    "NEGATIVE": {'description': 'Represented by "-" in a GFF file; the strand is negative wrt the landmark.'},
    "POSITIVE": {'description': 'Represented by "+" in a GFF file; the strand is positive with relation to the landmark.'},
    "UNKNOWN": {'description': 'Represented by "?" in a GFF file. The strandedness is relevant but unknown.'},
    "UNSTRANDED": {'description': 'Represented by "." in a GFF file; the feature is not stranded.'},
}

class SequenceType(RichEnum):
    """
    The type of sequence being represented.
    """
    # Enum members
    NUCLEIC_ACID = "NUCLEIC_ACID"
    AMINO_ACID = "AMINO_ACID"

# Set metadata after class creation
SequenceType._metadata = {
    "NUCLEIC_ACID": {'description': 'A nucleic acid sequence, as found in an FNA file.'},
    "AMINO_ACID": {'description': 'An amino acid sequence, as would be found in an FAA file.'},
}

__all__ = [
    "CdsPhaseType",
    "ContigCollectionType",
    "StrandType",
    "SequenceType",
]