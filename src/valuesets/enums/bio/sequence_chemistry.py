"""
Sequence Chemistry Value Sets

Value sets for nucleic acid and protein sequence chemistry, including
standard and extended alphabets, quality encodings, and molecular representations

Generated from: bio/sequence_chemistry.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class IUPACNucleotideCode(RichEnum):
    """
    Complete IUPAC nucleotide codes including ambiguous bases for DNA/RNA sequences.
    Used in FASTA and other sequence formats to represent uncertain nucleotides.
    """
    # Enum members
    A = "A"
    T = "T"
    U = "U"
    G = "G"
    C = "C"
    R = "R"
    Y = "Y"
    S = "S"
    W = "W"
    K = "K"
    M = "M"
    B = "B"
    D = "D"
    H = "H"
    V = "V"
    N = "N"
    GAP = "GAP"

# Set metadata after class creation
IUPACNucleotideCode._metadata = {
    "A": {'description': 'Adenine'},
    "T": {'description': 'Thymine (DNA)'},
    "U": {'description': 'Uracil (RNA)'},
    "G": {'description': 'Guanine'},
    "C": {'description': 'Cytosine'},
    "R": {'description': 'Purine (A or G)'},
    "Y": {'description': 'Pyrimidine (C or T/U)'},
    "S": {'description': 'Strong interaction (G or C)'},
    "W": {'description': 'Weak interaction (A or T/U)'},
    "K": {'description': 'Keto (G or T/U)'},
    "M": {'description': 'Amino (A or C)'},
    "B": {'description': 'Not A (C or G or T/U)'},
    "D": {'description': 'Not C (A or G or T/U)'},
    "H": {'description': 'Not G (A or C or T/U)'},
    "V": {'description': 'Not T/U (A or C or G)'},
    "N": {'description': 'Any nucleotide (A or C or G or T/U)'},
    "GAP": {'description': 'Gap or deletion in alignment'},
}

class StandardAminoAcid(RichEnum):
    """
    The 20 standard proteinogenic amino acids with IUPAC single-letter codes
    """
    # Enum members
    A = "A"
    R = "R"
    N = "N"
    D = "D"
    C = "C"
    E = "E"
    Q = "Q"
    G = "G"
    H = "H"
    I = "I"
    L = "L"
    K = "K"
    M = "M"
    F = "F"
    P = "P"
    S = "S"
    T = "T"
    W = "W"
    Y = "Y"
    V = "V"

# Set metadata after class creation
StandardAminoAcid._metadata = {
    "A": {'description': 'Alanine'},
    "R": {'description': 'Arginine'},
    "N": {'description': 'Asparagine'},
    "D": {'description': 'Aspartic acid'},
    "C": {'description': 'Cysteine'},
    "E": {'description': 'Glutamic acid'},
    "Q": {'description': 'Glutamine'},
    "G": {'description': 'Glycine'},
    "H": {'description': 'Histidine'},
    "I": {'description': 'Isoleucine'},
    "L": {'description': 'Leucine'},
    "K": {'description': 'Lysine'},
    "M": {'description': 'Methionine'},
    "F": {'description': 'Phenylalanine'},
    "P": {'description': 'Proline'},
    "S": {'description': 'Serine'},
    "T": {'description': 'Threonine'},
    "W": {'description': 'Tryptophan'},
    "Y": {'description': 'Tyrosine'},
    "V": {'description': 'Valine'},
}

class IUPACAminoAcidCode(RichEnum):
    """
    Complete IUPAC amino acid codes including standard amino acids,
    rare amino acids, and ambiguity codes
    """
    # Enum members
    A = "A"
    R = "R"
    N = "N"
    D = "D"
    C = "C"
    E = "E"
    Q = "Q"
    G = "G"
    H = "H"
    I = "I"
    L = "L"
    K = "K"
    M = "M"
    F = "F"
    P = "P"
    S = "S"
    T = "T"
    W = "W"
    Y = "Y"
    V = "V"
    U = "U"
    O = "O"
    B = "B"
    Z = "Z"
    J = "J"
    X = "X"
    STOP = "STOP"
    GAP = "GAP"

# Set metadata after class creation
IUPACAminoAcidCode._metadata = {
    "A": {'description': 'Alanine'},
    "R": {'description': 'Arginine'},
    "N": {'description': 'Asparagine'},
    "D": {'description': 'Aspartic acid'},
    "C": {'description': 'Cysteine'},
    "E": {'description': 'Glutamic acid'},
    "Q": {'description': 'Glutamine'},
    "G": {'description': 'Glycine'},
    "H": {'description': 'Histidine'},
    "I": {'description': 'Isoleucine'},
    "L": {'description': 'Leucine'},
    "K": {'description': 'Lysine'},
    "M": {'description': 'Methionine'},
    "F": {'description': 'Phenylalanine'},
    "P": {'description': 'Proline'},
    "S": {'description': 'Serine'},
    "T": {'description': 'Threonine'},
    "W": {'description': 'Tryptophan'},
    "Y": {'description': 'Tyrosine'},
    "V": {'description': 'Valine'},
    "U": {'description': 'Selenocysteine (21st amino acid)', 'aliases': ['Sec']},
    "O": {'description': 'Pyrrolysine (22nd amino acid)', 'aliases': ['Pyl']},
    "B": {'description': 'Asparagine or Aspartic acid (N or D)'},
    "Z": {'description': 'Glutamine or Glutamic acid (Q or E)'},
    "J": {'description': 'Leucine or Isoleucine (L or I)'},
    "X": {'description': 'Any amino acid'},
    "STOP": {'description': 'Translation stop codon'},
    "GAP": {'description': 'Gap or deletion in alignment'},
}

class SequenceAlphabet(RichEnum):
    """
    Types of sequence alphabets used in bioinformatics
    """
    # Enum members
    DNA = "DNA"
    RNA = "RNA"
    PROTEIN = "PROTEIN"
    IUPAC_DNA = "IUPAC_DNA"
    IUPAC_RNA = "IUPAC_RNA"
    IUPAC_PROTEIN = "IUPAC_PROTEIN"
    RESTRICTED_DNA = "RESTRICTED_DNA"
    RESTRICTED_RNA = "RESTRICTED_RNA"
    BINARY = "BINARY"

# Set metadata after class creation
SequenceAlphabet._metadata = {
    "DNA": {'description': 'Deoxyribonucleic acid alphabet (A, T, G, C)'},
    "RNA": {'description': 'Ribonucleic acid alphabet (A, U, G, C)'},
    "PROTEIN": {'description': 'Protein/amino acid alphabet (20 standard AAs)'},
    "IUPAC_DNA": {'description': 'Extended DNA with IUPAC ambiguity codes'},
    "IUPAC_RNA": {'description': 'Extended RNA with IUPAC ambiguity codes'},
    "IUPAC_PROTEIN": {'description': 'Extended protein with ambiguity codes and rare AAs'},
    "RESTRICTED_DNA": {'description': 'Unambiguous DNA bases only (A, T, G, C)'},
    "RESTRICTED_RNA": {'description': 'Unambiguous RNA bases only (A, U, G, C)'},
    "BINARY": {'description': 'Binary encoding of sequences'},
}

class SequenceQualityEncoding(RichEnum):
    """
    Quality score encoding standards used in FASTQ files and sequencing data.
    Different platforms and software versions use different ASCII offsets.
    """
    # Enum members
    SANGER = "SANGER"
    SOLEXA = "SOLEXA"
    ILLUMINA_1_3 = "ILLUMINA_1_3"
    ILLUMINA_1_5 = "ILLUMINA_1_5"
    ILLUMINA_1_8 = "ILLUMINA_1_8"

# Set metadata after class creation
SequenceQualityEncoding._metadata = {
    "SANGER": {'description': 'Sanger/Phred+33 (PHRED scores, ASCII offset 33)', 'annotations': {'ascii_offset': 33, 'score_range': '0-93', 'platforms': 'NCBI SRA, Illumina 1.8+'}},
    "SOLEXA": {'description': 'Solexa+64 (Solexa scores, ASCII offset 64)', 'annotations': {'ascii_offset': 64, 'score_range': '-5-62', 'platforms': 'Early Solexa/Illumina'}},
    "ILLUMINA_1_3": {'description': 'Illumina 1.3+ (PHRED+64, ASCII offset 64)', 'annotations': {'ascii_offset': 64, 'score_range': '0-62', 'platforms': 'Illumina 1.3-1.7'}},
    "ILLUMINA_1_5": {'description': 'Illumina 1.5+ (PHRED+64, special handling for 0-2)', 'annotations': {'ascii_offset': 64, 'score_range': '3-62', 'platforms': 'Illumina 1.5-1.7'}},
    "ILLUMINA_1_8": {'description': 'Illumina 1.8+ (PHRED+33, modern standard)', 'annotations': {'ascii_offset': 33, 'score_range': '0-41', 'platforms': 'Illumina 1.8+, modern sequencers'}},
}

class GeneticCodeTable(RichEnum):
    """
    NCBI genetic code translation tables for different organisms.
    Table 1 is the universal genetic code used by most organisms.
    """
    # Enum members
    TABLE_1 = "TABLE_1"
    TABLE_2 = "TABLE_2"
    TABLE_3 = "TABLE_3"
    TABLE_4 = "TABLE_4"
    TABLE_5 = "TABLE_5"
    TABLE_6 = "TABLE_6"
    TABLE_9 = "TABLE_9"
    TABLE_10 = "TABLE_10"
    TABLE_11 = "TABLE_11"
    TABLE_12 = "TABLE_12"
    TABLE_13 = "TABLE_13"
    TABLE_14 = "TABLE_14"
    TABLE_16 = "TABLE_16"
    TABLE_21 = "TABLE_21"
    TABLE_22 = "TABLE_22"
    TABLE_23 = "TABLE_23"
    TABLE_24 = "TABLE_24"
    TABLE_25 = "TABLE_25"
    TABLE_26 = "TABLE_26"
    TABLE_27 = "TABLE_27"
    TABLE_28 = "TABLE_28"
    TABLE_29 = "TABLE_29"
    TABLE_30 = "TABLE_30"
    TABLE_31 = "TABLE_31"

# Set metadata after class creation
GeneticCodeTable._metadata = {
    "TABLE_1": {'description': 'Standard genetic code (universal)', 'annotations': {'ncbi_id': 1, 'name': 'Standard'}},
    "TABLE_2": {'description': 'Vertebrate mitochondrial code', 'annotations': {'ncbi_id': 2, 'name': 'Vertebrate Mitochondrial'}},
    "TABLE_3": {'description': 'Yeast mitochondrial code', 'annotations': {'ncbi_id': 3, 'name': 'Yeast Mitochondrial'}},
    "TABLE_4": {'description': 'Mold, protozoan, coelenterate mitochondrial', 'annotations': {'ncbi_id': 4, 'name': 'Mold Mitochondrial'}},
    "TABLE_5": {'description': 'Invertebrate mitochondrial code', 'annotations': {'ncbi_id': 5, 'name': 'Invertebrate Mitochondrial'}},
    "TABLE_6": {'description': 'Ciliate, dasycladacean, hexamita nuclear code', 'annotations': {'ncbi_id': 6, 'name': 'Ciliate Nuclear'}},
    "TABLE_9": {'description': 'Echinoderm and flatworm mitochondrial code', 'annotations': {'ncbi_id': 9, 'name': 'Echinoderm Mitochondrial'}},
    "TABLE_10": {'description': 'Euplotid nuclear code', 'annotations': {'ncbi_id': 10, 'name': 'Euplotid Nuclear'}},
    "TABLE_11": {'description': 'Bacterial, archaeal and plant plastid code', 'annotations': {'ncbi_id': 11, 'name': 'Bacterial'}},
    "TABLE_12": {'description': 'Alternative yeast nuclear code', 'annotations': {'ncbi_id': 12, 'name': 'Alternative Yeast Nuclear'}},
    "TABLE_13": {'description': 'Ascidian mitochondrial code', 'annotations': {'ncbi_id': 13, 'name': 'Ascidian Mitochondrial'}},
    "TABLE_14": {'description': 'Alternative flatworm mitochondrial code', 'annotations': {'ncbi_id': 14, 'name': 'Alternative Flatworm Mitochondrial'}},
    "TABLE_16": {'description': 'Chlorophycean mitochondrial code', 'annotations': {'ncbi_id': 16, 'name': 'Chlorophycean Mitochondrial'}},
    "TABLE_21": {'description': 'Trematode mitochondrial code', 'annotations': {'ncbi_id': 21, 'name': 'Trematode Mitochondrial'}},
    "TABLE_22": {'description': 'Scenedesmus obliquus mitochondrial code', 'annotations': {'ncbi_id': 22, 'name': 'Scenedesmus Mitochondrial'}},
    "TABLE_23": {'description': 'Thraustochytrium mitochondrial code', 'annotations': {'ncbi_id': 23, 'name': 'Thraustochytrium Mitochondrial'}},
    "TABLE_24": {'description': 'Rhabdopleuridae mitochondrial code', 'annotations': {'ncbi_id': 24, 'name': 'Rhabdopleuridae Mitochondrial'}},
    "TABLE_25": {'description': 'Candidate division SR1 and gracilibacteria code', 'annotations': {'ncbi_id': 25, 'name': 'Candidate Division SR1'}},
    "TABLE_26": {'description': 'Pachysolen tannophilus nuclear code', 'annotations': {'ncbi_id': 26, 'name': 'Pachysolen Nuclear'}},
    "TABLE_27": {'description': 'Karyorelict nuclear code', 'annotations': {'ncbi_id': 27, 'name': 'Karyorelict Nuclear'}},
    "TABLE_28": {'description': 'Condylostoma nuclear code', 'annotations': {'ncbi_id': 28, 'name': 'Condylostoma Nuclear'}},
    "TABLE_29": {'description': 'Mesodinium nuclear code', 'annotations': {'ncbi_id': 29, 'name': 'Mesodinium Nuclear'}},
    "TABLE_30": {'description': 'Peritrich nuclear code', 'annotations': {'ncbi_id': 30, 'name': 'Peritrich Nuclear'}},
    "TABLE_31": {'description': 'Blastocrithidia nuclear code', 'annotations': {'ncbi_id': 31, 'name': 'Blastocrithidia Nuclear'}},
}

class SequenceStrand(RichEnum):
    """
    Strand orientation for nucleic acid sequences
    """
    # Enum members
    PLUS = "PLUS"
    MINUS = "MINUS"
    BOTH = "BOTH"
    UNKNOWN = "UNKNOWN"

# Set metadata after class creation
SequenceStrand._metadata = {
    "PLUS": {'description': "Plus/forward/sense strand (5' to 3')"},
    "MINUS": {'description': "Minus/reverse/antisense strand (3' to 5')"},
    "BOTH": {'description': 'Both strands'},
    "UNKNOWN": {'description': 'Strand not specified or unknown'},
}

class SequenceTopology(RichEnum):
    """
    Topological structure of nucleic acid molecules
    """
    # Enum members
    LINEAR = "LINEAR"
    CIRCULAR = "CIRCULAR"
    BRANCHED = "BRANCHED"
    UNKNOWN = "UNKNOWN"

# Set metadata after class creation
SequenceTopology._metadata = {
    "LINEAR": {'description': 'Linear sequence molecule', 'meaning': 'SO:0000987'},
    "CIRCULAR": {'description': 'Circular sequence molecule', 'meaning': 'SO:0000988'},
    "BRANCHED": {'description': 'Branched sequence structure'},
    "UNKNOWN": {'description': 'Topology not specified'},
}

class SequenceModality(RichEnum):
    """
    Types of sequence data based on experimental method
    """
    # Enum members
    SINGLE_CELL = "SINGLE_CELL"
    BULK = "BULK"
    SPATIAL = "SPATIAL"
    LONG_READ = "LONG_READ"
    SHORT_READ = "SHORT_READ"
    PAIRED_END = "PAIRED_END"
    SINGLE_END = "SINGLE_END"
    MATE_PAIR = "MATE_PAIR"

# Set metadata after class creation
SequenceModality._metadata = {
    "SINGLE_CELL": {'description': 'Single-cell sequencing data'},
    "BULK": {'description': 'Bulk/population sequencing data'},
    "SPATIAL": {'description': 'Spatially-resolved sequencing'},
    "LONG_READ": {'description': 'Long-read sequencing (PacBio, Oxford Nanopore)'},
    "SHORT_READ": {'description': 'Short-read sequencing (Illumina)'},
    "PAIRED_END": {'description': 'Paired-end sequencing reads'},
    "SINGLE_END": {'description': 'Single-end sequencing reads'},
    "MATE_PAIR": {'description': 'Mate-pair sequencing libraries'},
}

__all__ = [
    "IUPACNucleotideCode",
    "StandardAminoAcid",
    "IUPACAminoAcidCode",
    "SequenceAlphabet",
    "SequenceQualityEncoding",
    "GeneticCodeTable",
    "SequenceStrand",
    "SequenceTopology",
    "SequenceModality",
]