"""
Biological Sequence Alphabet Value Sets

Alphabets for biological sequences including DNA, RNA, and protein sequences. Includes standard alphabets and extended versions with ambiguity codes following IUPAC nomenclature and common bioinformatics standards.


Generated from: bio/sequence_alphabets.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class DNABaseEnum(RichEnum):
    """
    Standard DNA nucleotide bases (canonical)
    """
    # Enum members
    A = "A"
    C = "C"
    G = "G"
    T = "T"

# Set metadata after class creation
DNABaseEnum._metadata = {
    "A": {'meaning': 'CHEBI:16708', 'annotations': {'complement': 'T', 'purine': 'true', 'chemical_formula': 'C5H5N5'}, 'aliases': ['adenine']},
    "C": {'meaning': 'CHEBI:16040', 'annotations': {'complement': 'G', 'pyrimidine': 'true', 'chemical_formula': 'C4H5N3O'}, 'aliases': ['cytosine']},
    "G": {'meaning': 'CHEBI:16235', 'annotations': {'complement': 'C', 'purine': 'true', 'chemical_formula': 'C5H5N5O'}, 'aliases': ['guanine']},
    "T": {'meaning': 'CHEBI:17821', 'annotations': {'complement': 'A', 'pyrimidine': 'true', 'chemical_formula': 'C5H6N2O2'}, 'aliases': ['thymine']},
}

class DNABaseExtendedEnum(RichEnum):
    """
    Extended DNA alphabet with IUPAC ambiguity codes
    """
    # Enum members
    A = "A"
    C = "C"
    G = "G"
    T = "T"
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
DNABaseExtendedEnum._metadata = {
    "A": {'meaning': 'CHEBI:16708', 'annotations': {'represents': 'A'}, 'aliases': ['adenine']},
    "C": {'meaning': 'CHEBI:16040', 'annotations': {'represents': 'C'}, 'aliases': ['cytosine']},
    "G": {'meaning': 'CHEBI:16235', 'annotations': {'represents': 'G'}, 'aliases': ['guanine']},
    "T": {'meaning': 'CHEBI:17821', 'annotations': {'represents': 'T'}, 'aliases': ['thymine']},
    "R": {'annotations': {'represents': 'A,G', 'iupac': 'true'}},
    "Y": {'annotations': {'represents': 'C,T', 'iupac': 'true'}},
    "S": {'annotations': {'represents': 'G,C', 'iupac': 'true', 'bond_strength': 'strong (3 H-bonds)'}},
    "W": {'annotations': {'represents': 'A,T', 'iupac': 'true', 'bond_strength': 'weak (2 H-bonds)'}},
    "K": {'annotations': {'represents': 'G,T', 'iupac': 'true'}},
    "M": {'annotations': {'represents': 'A,C', 'iupac': 'true'}},
    "B": {'annotations': {'represents': 'C,G,T', 'iupac': 'true'}},
    "D": {'annotations': {'represents': 'A,G,T', 'iupac': 'true'}},
    "H": {'annotations': {'represents': 'A,C,T', 'iupac': 'true'}},
    "V": {'annotations': {'represents': 'A,C,G', 'iupac': 'true'}},
    "N": {'annotations': {'represents': 'A,C,G,T', 'iupac': 'true'}},
    "GAP": {'annotations': {'symbol': '-', 'represents': 'gap'}},
}

class RNABaseEnum(RichEnum):
    """
    Standard RNA nucleotide bases (canonical)
    """
    # Enum members
    A = "A"
    C = "C"
    G = "G"
    U = "U"

# Set metadata after class creation
RNABaseEnum._metadata = {
    "A": {'meaning': 'CHEBI:16708', 'annotations': {'complement': 'U', 'purine': 'true', 'chemical_formula': 'C5H5N5'}, 'aliases': ['adenine']},
    "C": {'meaning': 'CHEBI:16040', 'annotations': {'complement': 'G', 'pyrimidine': 'true', 'chemical_formula': 'C4H5N3O'}, 'aliases': ['cytosine']},
    "G": {'meaning': 'CHEBI:16235', 'annotations': {'complement': 'C', 'purine': 'true', 'chemical_formula': 'C5H5N5O'}, 'aliases': ['guanine']},
    "U": {'meaning': 'CHEBI:17568', 'annotations': {'complement': 'A', 'pyrimidine': 'true', 'chemical_formula': 'C4H4N2O2'}, 'aliases': ['uracil']},
}

class RNABaseExtendedEnum(RichEnum):
    """
    Extended RNA alphabet with IUPAC ambiguity codes
    """
    # Enum members
    A = "A"
    C = "C"
    G = "G"
    U = "U"
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
RNABaseExtendedEnum._metadata = {
    "A": {'meaning': 'CHEBI:16708', 'annotations': {'represents': 'A'}, 'aliases': ['adenine']},
    "C": {'meaning': 'CHEBI:16040', 'annotations': {'represents': 'C'}, 'aliases': ['cytosine']},
    "G": {'meaning': 'CHEBI:16235', 'annotations': {'represents': 'G'}, 'aliases': ['guanine']},
    "U": {'meaning': 'CHEBI:17568', 'annotations': {'represents': 'U'}, 'aliases': ['uracil']},
    "R": {'annotations': {'represents': 'A,G', 'iupac': 'true'}},
    "Y": {'annotations': {'represents': 'C,U', 'iupac': 'true'}},
    "S": {'annotations': {'represents': 'G,C', 'iupac': 'true'}},
    "W": {'annotations': {'represents': 'A,U', 'iupac': 'true'}},
    "K": {'annotations': {'represents': 'G,U', 'iupac': 'true'}},
    "M": {'annotations': {'represents': 'A,C', 'iupac': 'true'}},
    "B": {'annotations': {'represents': 'C,G,U', 'iupac': 'true'}},
    "D": {'annotations': {'represents': 'A,G,U', 'iupac': 'true'}},
    "H": {'annotations': {'represents': 'A,C,U', 'iupac': 'true'}},
    "V": {'annotations': {'represents': 'A,C,G', 'iupac': 'true'}},
    "N": {'annotations': {'represents': 'A,C,G,U', 'iupac': 'true'}},
    "GAP": {'annotations': {'symbol': '-', 'represents': 'gap'}},
}

class AminoAcidEnum(RichEnum):
    """
    Standard amino acid single letter codes
    """
    # Enum members
    A = "A"
    C = "C"
    D = "D"
    E = "E"
    F = "F"
    G = "G"
    H = "H"
    I = "I"
    K = "K"
    L = "L"
    M = "M"
    N = "N"
    P = "P"
    Q = "Q"
    R = "R"
    S = "S"
    T = "T"
    V = "V"
    W = "W"
    Y = "Y"

# Set metadata after class creation
AminoAcidEnum._metadata = {
    "A": {'meaning': 'CHEBI:16449', 'annotations': {'three_letter': 'Ala', 'polarity': 'nonpolar', 'essential': 'false', 'molecular_weight': '89.09'}, 'aliases': ['alanine']},
    "C": {'meaning': 'CHEBI:17561', 'annotations': {'three_letter': 'Cys', 'polarity': 'polar', 'essential': 'false', 'molecular_weight': '121.15', 'special': 'forms disulfide bonds'}, 'aliases': ['L-cysteine']},
    "D": {'meaning': 'CHEBI:17053', 'annotations': {'three_letter': 'Asp', 'polarity': 'acidic', 'essential': 'false', 'molecular_weight': '133.10', 'charge': 'negative'}, 'aliases': ['L-aspartic acid']},
    "E": {'meaning': 'CHEBI:16015', 'annotations': {'three_letter': 'Glu', 'polarity': 'acidic', 'essential': 'false', 'molecular_weight': '147.13', 'charge': 'negative'}, 'aliases': ['L-glutamic acid']},
    "F": {'meaning': 'CHEBI:17295', 'annotations': {'three_letter': 'Phe', 'polarity': 'nonpolar', 'essential': 'true', 'molecular_weight': '165.19', 'aromatic': 'true'}, 'aliases': ['L-phenylalanine']},
    "G": {'meaning': 'CHEBI:15428', 'annotations': {'three_letter': 'Gly', 'polarity': 'nonpolar', 'essential': 'false', 'molecular_weight': '75.07', 'special': 'smallest, most flexible'}, 'aliases': ['glycine']},
    "H": {'meaning': 'CHEBI:15971', 'annotations': {'three_letter': 'His', 'polarity': 'basic', 'essential': 'true', 'molecular_weight': '155.16', 'charge': 'positive'}, 'aliases': ['L-histidine']},
    "I": {'meaning': 'CHEBI:17191', 'annotations': {'three_letter': 'Ile', 'polarity': 'nonpolar', 'essential': 'true', 'molecular_weight': '131.17', 'branched': 'true'}, 'aliases': ['L-isoleucine']},
    "K": {'meaning': 'CHEBI:18019', 'annotations': {'three_letter': 'Lys', 'polarity': 'basic', 'essential': 'true', 'molecular_weight': '146.19', 'charge': 'positive'}, 'aliases': ['L-lysine']},
    "L": {'meaning': 'CHEBI:15603', 'annotations': {'three_letter': 'Leu', 'polarity': 'nonpolar', 'essential': 'true', 'molecular_weight': '131.17', 'branched': 'true'}, 'aliases': ['L-leucine']},
    "M": {'meaning': 'CHEBI:16643', 'annotations': {'three_letter': 'Met', 'polarity': 'nonpolar', 'essential': 'true', 'molecular_weight': '149.21', 'special': 'start codon'}, 'aliases': ['L-methionine']},
    "N": {'meaning': 'CHEBI:17196', 'annotations': {'three_letter': 'Asn', 'polarity': 'polar', 'essential': 'false', 'molecular_weight': '132.12'}, 'aliases': ['L-asparagine']},
    "P": {'meaning': 'CHEBI:17203', 'annotations': {'three_letter': 'Pro', 'polarity': 'nonpolar', 'essential': 'false', 'molecular_weight': '115.13', 'special': 'helix breaker, rigid'}, 'aliases': ['L-proline']},
    "Q": {'meaning': 'CHEBI:18050', 'annotations': {'three_letter': 'Gln', 'polarity': 'polar', 'essential': 'false', 'molecular_weight': '146.15'}, 'aliases': ['L-glutamine']},
    "R": {'meaning': 'CHEBI:16467', 'annotations': {'three_letter': 'Arg', 'polarity': 'basic', 'essential': 'false', 'molecular_weight': '174.20', 'charge': 'positive'}, 'aliases': ['L-arginine']},
    "S": {'meaning': 'CHEBI:17115', 'annotations': {'three_letter': 'Ser', 'polarity': 'polar', 'essential': 'false', 'molecular_weight': '105.09', 'hydroxyl': 'true'}, 'aliases': ['L-serine']},
    "T": {'meaning': 'CHEBI:16857', 'annotations': {'three_letter': 'Thr', 'polarity': 'polar', 'essential': 'true', 'molecular_weight': '119.12', 'hydroxyl': 'true'}, 'aliases': ['L-threonine']},
    "V": {'meaning': 'CHEBI:16414', 'annotations': {'three_letter': 'Val', 'polarity': 'nonpolar', 'essential': 'true', 'molecular_weight': '117.15', 'branched': 'true'}, 'aliases': ['L-valine']},
    "W": {'meaning': 'CHEBI:16828', 'annotations': {'three_letter': 'Trp', 'polarity': 'nonpolar', 'essential': 'true', 'molecular_weight': '204.23', 'aromatic': 'true', 'special': 'largest'}, 'aliases': ['L-tryptophan']},
    "Y": {'meaning': 'CHEBI:17895', 'annotations': {'three_letter': 'Tyr', 'polarity': 'polar', 'essential': 'false', 'molecular_weight': '181.19', 'aromatic': 'true', 'hydroxyl': 'true'}, 'aliases': ['L-tyrosine']},
}

class AminoAcidExtendedEnum(RichEnum):
    """
    Extended amino acid alphabet with ambiguity codes and special characters
    """
    # Enum members
    A = "A"
    C = "C"
    D = "D"
    E = "E"
    F = "F"
    G = "G"
    H = "H"
    I = "I"
    K = "K"
    L = "L"
    M = "M"
    N = "N"
    P = "P"
    Q = "Q"
    R = "R"
    S = "S"
    T = "T"
    V = "V"
    W = "W"
    Y = "Y"
    B = "B"
    Z = "Z"
    J = "J"
    X = "X"
    STOP = "STOP"
    GAP = "GAP"
    U = "U"
    O = "O"

# Set metadata after class creation
AminoAcidExtendedEnum._metadata = {
    "A": {'meaning': 'CHEBI:16449', 'annotations': {'three_letter': 'Ala'}, 'aliases': ['alanine']},
    "C": {'meaning': 'CHEBI:17561', 'annotations': {'three_letter': 'Cys'}, 'aliases': ['L-cysteine']},
    "D": {'meaning': 'CHEBI:17053', 'annotations': {'three_letter': 'Asp'}, 'aliases': ['L-aspartic acid']},
    "E": {'meaning': 'CHEBI:16015', 'annotations': {'three_letter': 'Glu'}, 'aliases': ['L-glutamic acid']},
    "F": {'meaning': 'CHEBI:17295', 'annotations': {'three_letter': 'Phe'}, 'aliases': ['L-phenylalanine']},
    "G": {'meaning': 'CHEBI:15428', 'annotations': {'three_letter': 'Gly'}, 'aliases': ['glycine']},
    "H": {'meaning': 'CHEBI:15971', 'annotations': {'three_letter': 'His'}, 'aliases': ['L-histidine']},
    "I": {'meaning': 'CHEBI:17191', 'annotations': {'three_letter': 'Ile'}, 'aliases': ['L-isoleucine']},
    "K": {'meaning': 'CHEBI:18019', 'annotations': {'three_letter': 'Lys'}, 'aliases': ['L-lysine']},
    "L": {'meaning': 'CHEBI:15603', 'annotations': {'three_letter': 'Leu'}, 'aliases': ['L-leucine']},
    "M": {'meaning': 'CHEBI:16643', 'annotations': {'three_letter': 'Met'}, 'aliases': ['L-methionine']},
    "N": {'meaning': 'CHEBI:17196', 'annotations': {'three_letter': 'Asn'}, 'aliases': ['L-asparagine']},
    "P": {'meaning': 'CHEBI:17203', 'annotations': {'three_letter': 'Pro'}, 'aliases': ['L-proline']},
    "Q": {'meaning': 'CHEBI:18050', 'annotations': {'three_letter': 'Gln'}, 'aliases': ['L-glutamine']},
    "R": {'meaning': 'CHEBI:16467', 'annotations': {'three_letter': 'Arg'}, 'aliases': ['L-arginine']},
    "S": {'meaning': 'CHEBI:17115', 'annotations': {'three_letter': 'Ser'}, 'aliases': ['L-serine']},
    "T": {'meaning': 'CHEBI:16857', 'annotations': {'three_letter': 'Thr'}, 'aliases': ['L-threonine']},
    "V": {'meaning': 'CHEBI:16414', 'annotations': {'three_letter': 'Val'}, 'aliases': ['L-valine']},
    "W": {'meaning': 'CHEBI:16828', 'annotations': {'three_letter': 'Trp'}, 'aliases': ['L-tryptophan']},
    "Y": {'meaning': 'CHEBI:17895', 'annotations': {'three_letter': 'Tyr'}, 'aliases': ['L-tyrosine']},
    "B": {'annotations': {'three_letter': 'Asx', 'represents': 'D,N', 'ambiguity': 'true'}, 'aliases': ['L-aspartic acid or Asparagine (D or N)']},
    "Z": {'annotations': {'three_letter': 'Glx', 'represents': 'E,Q', 'ambiguity': 'true'}, 'aliases': ['L-glutamic acid or Glutamine (E or Q)']},
    "J": {'annotations': {'three_letter': 'Xle', 'represents': 'L,I', 'ambiguity': 'true'}, 'aliases': ['L-leucine or Isoleucine (L or I)']},
    "X": {'annotations': {'three_letter': 'Xaa', 'represents': 'any', 'ambiguity': 'true'}},
    "STOP": {'annotations': {'symbol': '*', 'three_letter': 'Ter', 'represents': 'stop codon'}},
    "GAP": {'annotations': {'symbol': '-', 'represents': 'gap'}},
    "U": {'meaning': 'CHEBI:16633', 'annotations': {'three_letter': 'Sec', 'special': '21st amino acid', 'codon': 'UGA with SECIS element'}, 'aliases': ['L-selenocysteine']},
    "O": {'meaning': 'CHEBI:21860', 'annotations': {'three_letter': 'Pyl', 'special': '22nd amino acid', 'codon': 'UAG in certain archaea/bacteria'}, 'aliases': ['L-pyrrolysine']},
}

class CodonEnum(RichEnum):
    """
    Standard genetic code codons (DNA)
    """
    # Enum members
    TTT = "TTT"
    TTC = "TTC"
    TTA = "TTA"
    TTG = "TTG"
    CTT = "CTT"
    CTC = "CTC"
    CTA = "CTA"
    CTG = "CTG"
    ATT = "ATT"
    ATC = "ATC"
    ATA = "ATA"
    ATG = "ATG"
    GTT = "GTT"
    GTC = "GTC"
    GTA = "GTA"
    GTG = "GTG"
    TCT = "TCT"
    TCC = "TCC"
    TCA = "TCA"
    TCG = "TCG"
    AGT = "AGT"
    AGC = "AGC"
    CCT = "CCT"
    CCC = "CCC"
    CCA = "CCA"
    CCG = "CCG"
    ACT = "ACT"
    ACC = "ACC"
    ACA = "ACA"
    ACG = "ACG"
    GCT = "GCT"
    GCC = "GCC"
    GCA = "GCA"
    GCG = "GCG"
    TAT = "TAT"
    TAC = "TAC"
    TAA = "TAA"
    TAG = "TAG"
    TGA = "TGA"
    CAT = "CAT"
    CAC = "CAC"
    CAA = "CAA"
    CAG = "CAG"
    AAT = "AAT"
    AAC = "AAC"
    AAA = "AAA"
    AAG = "AAG"
    GAT = "GAT"
    GAC = "GAC"
    GAA = "GAA"
    GAG = "GAG"
    TGT = "TGT"
    TGC = "TGC"
    TGG = "TGG"
    CGT = "CGT"
    CGC = "CGC"
    CGA = "CGA"
    CGG = "CGG"
    AGA = "AGA"
    AGG = "AGG"
    GGT = "GGT"
    GGC = "GGC"
    GGA = "GGA"
    GGG = "GGG"

# Set metadata after class creation
CodonEnum._metadata = {
    "TTT": {'annotations': {'amino_acid': 'F', 'amino_acid_name': 'Phenylalanine'}},
    "TTC": {'annotations': {'amino_acid': 'F', 'amino_acid_name': 'Phenylalanine'}},
    "TTA": {'annotations': {'amino_acid': 'L', 'amino_acid_name': 'Leucine'}},
    "TTG": {'annotations': {'amino_acid': 'L', 'amino_acid_name': 'Leucine'}},
    "CTT": {'annotations': {'amino_acid': 'L', 'amino_acid_name': 'Leucine'}},
    "CTC": {'annotations': {'amino_acid': 'L', 'amino_acid_name': 'Leucine'}},
    "CTA": {'annotations': {'amino_acid': 'L', 'amino_acid_name': 'Leucine'}},
    "CTG": {'annotations': {'amino_acid': 'L', 'amino_acid_name': 'Leucine'}},
    "ATT": {'annotations': {'amino_acid': 'I', 'amino_acid_name': 'Isoleucine'}},
    "ATC": {'annotations': {'amino_acid': 'I', 'amino_acid_name': 'Isoleucine'}},
    "ATA": {'annotations': {'amino_acid': 'I', 'amino_acid_name': 'Isoleucine'}},
    "ATG": {'annotations': {'amino_acid': 'M', 'amino_acid_name': 'Methionine', 'special': 'start codon'}},
    "GTT": {'annotations': {'amino_acid': 'V', 'amino_acid_name': 'Valine'}},
    "GTC": {'annotations': {'amino_acid': 'V', 'amino_acid_name': 'Valine'}},
    "GTA": {'annotations': {'amino_acid': 'V', 'amino_acid_name': 'Valine'}},
    "GTG": {'annotations': {'amino_acid': 'V', 'amino_acid_name': 'Valine'}},
    "TCT": {'annotations': {'amino_acid': 'S', 'amino_acid_name': 'Serine'}},
    "TCC": {'annotations': {'amino_acid': 'S', 'amino_acid_name': 'Serine'}},
    "TCA": {'annotations': {'amino_acid': 'S', 'amino_acid_name': 'Serine'}},
    "TCG": {'annotations': {'amino_acid': 'S', 'amino_acid_name': 'Serine'}},
    "AGT": {'annotations': {'amino_acid': 'S', 'amino_acid_name': 'Serine'}},
    "AGC": {'annotations': {'amino_acid': 'S', 'amino_acid_name': 'Serine'}},
    "CCT": {'annotations': {'amino_acid': 'P', 'amino_acid_name': 'Proline'}},
    "CCC": {'annotations': {'amino_acid': 'P', 'amino_acid_name': 'Proline'}},
    "CCA": {'annotations': {'amino_acid': 'P', 'amino_acid_name': 'Proline'}},
    "CCG": {'annotations': {'amino_acid': 'P', 'amino_acid_name': 'Proline'}},
    "ACT": {'annotations': {'amino_acid': 'T', 'amino_acid_name': 'Threonine'}},
    "ACC": {'annotations': {'amino_acid': 'T', 'amino_acid_name': 'Threonine'}},
    "ACA": {'annotations': {'amino_acid': 'T', 'amino_acid_name': 'Threonine'}},
    "ACG": {'annotations': {'amino_acid': 'T', 'amino_acid_name': 'Threonine'}},
    "GCT": {'annotations': {'amino_acid': 'A', 'amino_acid_name': 'Alanine'}},
    "GCC": {'annotations': {'amino_acid': 'A', 'amino_acid_name': 'Alanine'}},
    "GCA": {'annotations': {'amino_acid': 'A', 'amino_acid_name': 'Alanine'}},
    "GCG": {'annotations': {'amino_acid': 'A', 'amino_acid_name': 'Alanine'}},
    "TAT": {'annotations': {'amino_acid': 'Y', 'amino_acid_name': 'Tyrosine'}},
    "TAC": {'annotations': {'amino_acid': 'Y', 'amino_acid_name': 'Tyrosine'}},
    "TAA": {'annotations': {'amino_acid': '*', 'name': 'ochre', 'special': 'stop codon'}},
    "TAG": {'annotations': {'amino_acid': '*', 'name': 'amber', 'special': 'stop codon'}},
    "TGA": {'annotations': {'amino_acid': '*', 'name': 'opal', 'special': 'stop codon or selenocysteine'}},
    "CAT": {'annotations': {'amino_acid': 'H', 'amino_acid_name': 'Histidine'}},
    "CAC": {'annotations': {'amino_acid': 'H', 'amino_acid_name': 'Histidine'}},
    "CAA": {'annotations': {'amino_acid': 'Q', 'amino_acid_name': 'Glutamine'}},
    "CAG": {'annotations': {'amino_acid': 'Q', 'amino_acid_name': 'Glutamine'}},
    "AAT": {'annotations': {'amino_acid': 'N', 'amino_acid_name': 'Asparagine'}},
    "AAC": {'annotations': {'amino_acid': 'N', 'amino_acid_name': 'Asparagine'}},
    "AAA": {'annotations': {'amino_acid': 'K', 'amino_acid_name': 'Lysine'}},
    "AAG": {'annotations': {'amino_acid': 'K', 'amino_acid_name': 'Lysine'}},
    "GAT": {'annotations': {'amino_acid': 'D', 'amino_acid_name': 'Aspartic acid'}},
    "GAC": {'annotations': {'amino_acid': 'D', 'amino_acid_name': 'Aspartic acid'}},
    "GAA": {'annotations': {'amino_acid': 'E', 'amino_acid_name': 'Glutamic acid'}},
    "GAG": {'annotations': {'amino_acid': 'E', 'amino_acid_name': 'Glutamic acid'}},
    "TGT": {'annotations': {'amino_acid': 'C', 'amino_acid_name': 'Cysteine'}},
    "TGC": {'annotations': {'amino_acid': 'C', 'amino_acid_name': 'Cysteine'}},
    "TGG": {'annotations': {'amino_acid': 'W', 'amino_acid_name': 'Tryptophan'}},
    "CGT": {'annotations': {'amino_acid': 'R', 'amino_acid_name': 'Arginine'}},
    "CGC": {'annotations': {'amino_acid': 'R', 'amino_acid_name': 'Arginine'}},
    "CGA": {'annotations': {'amino_acid': 'R', 'amino_acid_name': 'Arginine'}},
    "CGG": {'annotations': {'amino_acid': 'R', 'amino_acid_name': 'Arginine'}},
    "AGA": {'annotations': {'amino_acid': 'R', 'amino_acid_name': 'Arginine'}},
    "AGG": {'annotations': {'amino_acid': 'R', 'amino_acid_name': 'Arginine'}},
    "GGT": {'annotations': {'amino_acid': 'G', 'amino_acid_name': 'Glycine'}},
    "GGC": {'annotations': {'amino_acid': 'G', 'amino_acid_name': 'Glycine'}},
    "GGA": {'annotations': {'amino_acid': 'G', 'amino_acid_name': 'Glycine'}},
    "GGG": {'annotations': {'amino_acid': 'G', 'amino_acid_name': 'Glycine'}},
}

class NucleotideModificationEnum(RichEnum):
    """
    Common nucleotide modifications
    """
    # Enum members
    FIVE_METHYL_C = "FIVE_METHYL_C"
    SIX_METHYL_A = "SIX_METHYL_A"
    PSEUDOURIDINE = "PSEUDOURIDINE"
    INOSINE = "INOSINE"
    DIHYDROURIDINE = "DIHYDROURIDINE"
    SEVEN_METHYL_G = "SEVEN_METHYL_G"
    FIVE_HYDROXY_METHYL_C = "FIVE_HYDROXY_METHYL_C"
    EIGHT_OXO_G = "EIGHT_OXO_G"

# Set metadata after class creation
NucleotideModificationEnum._metadata = {
    "FIVE_METHYL_C": {'description': '5-methylcytosine', 'meaning': 'CHEBI:27551', 'annotations': {'symbol': 'm5C', 'type': 'DNA methylation', 'function': 'gene regulation'}},
    "SIX_METHYL_A": {'description': 'N6-methyladenosine', 'meaning': 'CHEBI:21891', 'annotations': {'symbol': 'm6A', 'type': 'RNA modification', 'function': 'RNA stability, translation'}},
    "PSEUDOURIDINE": {'description': 'Pseudouridine', 'meaning': 'CHEBI:17802', 'annotations': {'symbol': 'Ψ', 'type': 'RNA modification', 'function': 'RNA stability'}},
    "INOSINE": {'description': 'Inosine', 'meaning': 'CHEBI:17596', 'annotations': {'symbol': 'I', 'type': 'RNA editing', 'pairs_with': 'A, C, U'}},
    "DIHYDROURIDINE": {'description': 'Dihydrouridine', 'meaning': 'CHEBI:23774', 'annotations': {'symbol': 'D', 'type': 'tRNA modification'}},
    "SEVEN_METHYL_G": {'description': '7-methylguanosine', 'meaning': 'CHEBI:20794', 'annotations': {'symbol': 'm7G', 'type': 'mRNA cap', 'function': 'translation initiation'}},
    "FIVE_HYDROXY_METHYL_C": {'description': '5-hydroxymethylcytosine', 'meaning': 'CHEBI:76792', 'annotations': {'symbol': 'hmC', 'type': 'DNA modification', 'function': 'demethylation intermediate'}},
    "EIGHT_OXO_G": {'description': '8-oxoguanine', 'meaning': 'CHEBI:44605', 'annotations': {'symbol': '8-oxoG', 'type': 'oxidative damage', 'pairs_with': 'A or C'}},
}

class SequenceQualityEnum(RichEnum):
    """
    Sequence quality indicators (Phred scores)
    """
    # Enum members
    Q0 = "Q0"
    Q10 = "Q10"
    Q20 = "Q20"
    Q30 = "Q30"
    Q40 = "Q40"
    Q50 = "Q50"
    Q60 = "Q60"

# Set metadata after class creation
SequenceQualityEnum._metadata = {
    "Q0": {'description': 'Phred quality 0 (100% error probability)', 'annotations': {'phred_score': '0', 'error_probability': '1.0', 'ascii_char': '!'}},
    "Q10": {'description': 'Phred quality 10 (10% error probability)', 'annotations': {'phred_score': '10', 'error_probability': '0.1', 'ascii_char': '+'}},
    "Q20": {'description': 'Phred quality 20 (1% error probability)', 'annotations': {'phred_score': '20', 'error_probability': '0.01', 'ascii_char': '5'}},
    "Q30": {'description': 'Phred quality 30 (0.1% error probability)', 'annotations': {'phred_score': '30', 'error_probability': '0.001', 'ascii_char': '?'}},
    "Q40": {'description': 'Phred quality 40 (0.01% error probability)', 'annotations': {'phred_score': '40', 'error_probability': '0.0001', 'ascii_char': 'I'}},
    "Q50": {'description': 'Phred quality 50 (0.001% error probability)', 'annotations': {'phred_score': '50', 'error_probability': '0.00001', 'ascii_char': 'S'}},
    "Q60": {'description': 'Phred quality 60 (0.0001% error probability)', 'annotations': {'phred_score': '60', 'error_probability': '0.000001', 'ascii_char': ']'}},
}

__all__ = [
    "DNABaseEnum",
    "DNABaseExtendedEnum",
    "RNABaseEnum",
    "RNABaseExtendedEnum",
    "AminoAcidEnum",
    "AminoAcidExtendedEnum",
    "CodonEnum",
    "NucleotideModificationEnum",
    "SequenceQualityEnum",
]