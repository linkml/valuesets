"""
Gene Perturbation Value Sets

Value sets for genetic perturbation and modification methods used in functional genomics, gene therapy, and molecular biology research.

Generated from: bio/gene_perturbation.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class GenePerturbationMethodEnum(RichEnum):
    """
    Methods for perturbing or modifying gene expression and function. Includes gene editing, silencing, and overexpression approaches.
    """
    # Enum members
    CRISPR = "CRISPR"
    CRISPR_ACTIVATION = "CRISPR_ACTIVATION"
    CRISPR_INTERFERENCE = "CRISPR_INTERFERENCE"
    CRISPR_BASE_EDITING = "CRISPR_BASE_EDITING"
    CRISPR_PRIME_EDITING = "CRISPR_PRIME_EDITING"
    CRAFT = "CRAFT"
    RNAI = "RNAI"
    SIRNA = "SIRNA"
    SHRNA = "SHRNA"
    ANTISENSE_OLIGONUCLEOTIDE = "ANTISENSE_OLIGONUCLEOTIDE"
    MORPHOLINO = "MORPHOLINO"
    CRE_RECOMBINASE = "CRE_RECOMBINASE"
    FLPE_RECOMBINASE = "FLPE_RECOMBINASE"
    TALEN = "TALEN"
    ZINC_FINGER_NUCLEASE = "ZINC_FINGER_NUCLEASE"
    TRANSPOSON_MUTAGENESIS = "TRANSPOSON_MUTAGENESIS"
    CHEMICAL_MUTAGENESIS = "CHEMICAL_MUTAGENESIS"
    OVEREXPRESSION = "OVEREXPRESSION"

# Set metadata after class creation
GenePerturbationMethodEnum._metadata = {
    "CRISPR": {'description': 'CRISPR/Cas9 gene editing technology', 'meaning': 'BAO:0010249', 'annotations': {'mechanism': 'DNA cleavage and repair'}, 'aliases': ['CRISPR/Cas9', 'CRISPR-Cas9']},
    "CRISPR_ACTIVATION": {'description': 'CRISPR activation (CRISPRa) for gene upregulation', 'annotations': {'mechanism': 'transcriptional activation', 'effect': 'overexpression'}, 'aliases': ['CRISPRa']},
    "CRISPR_INTERFERENCE": {'description': 'CRISPR interference (CRISPRi) for gene silencing', 'annotations': {'mechanism': 'transcriptional repression', 'effect': 'knockdown'}, 'aliases': ['CRISPRi']},
    "CRISPR_BASE_EDITING": {'description': 'CRISPR base editing for precise nucleotide changes', 'annotations': {'mechanism': 'nucleotide conversion'}, 'aliases': ['base editing']},
    "CRISPR_PRIME_EDITING": {'description': 'CRISPR prime editing for versatile sequence changes', 'annotations': {'mechanism': 'search-and-replace'}, 'aliases': ['prime editing']},
    "CRAFT": {'description': 'CRISPR Assisted mRNA Fragment Trans-splicing', 'annotations': {'mechanism': 'RNA trans-splicing'}, 'aliases': ['CRISPR Assisted mRNA Fragment Trans-splicing']},
    "RNAI": {'description': 'RNA interference for post-transcriptional gene silencing', 'meaning': 'NCIT:C20153', 'annotations': {'mechanism': 'mRNA degradation', 'effect': 'knockdown'}, 'aliases': ['RNAi', 'RNA interference']},
    "SIRNA": {'description': 'Small interfering RNA for transient gene silencing', 'meaning': 'NCIT:C2191', 'annotations': {'duration': 'transient', 'delivery': 'transfection'}, 'aliases': ['siRNA']},
    "SHRNA": {'description': 'Short hairpin RNA for stable gene silencing', 'meaning': 'NCIT:C111906', 'annotations': {'duration': 'stable', 'delivery': 'viral transduction'}, 'aliases': ['shRNA']},
    "ANTISENSE_OLIGONUCLEOTIDE": {'description': 'Antisense oligonucleotides for gene silencing', 'meaning': 'NCIT:C1653', 'annotations': {'mechanism': 'RNase H activation or steric blocking'}, 'aliases': ['ASO', 'antisense']},
    "MORPHOLINO": {'description': 'Morpholino oligomers for gene knockdown', 'meaning': 'NCIT:C96280', 'annotations': {'mechanism': 'steric blocking', 'use': 'developmental biology'}},
    "CRE_RECOMBINASE": {'description': 'Cre-lox recombination system for conditional gene modification', 'meaning': 'NCIT:C17285', 'annotations': {'mechanism': 'site-specific recombination', 'use': 'conditional knockout'}, 'aliases': ['Cre-lox', 'CRE Recombinase']},
    "FLPE_RECOMBINASE": {'description': 'Flp-FRT recombination system', 'annotations': {'mechanism': 'site-specific recombination'}, 'aliases': ['Flp-FRT']},
    "TALEN": {'description': 'Transcription Activator-Like Effector Nucleases', 'meaning': 'NCIT:C111903', 'annotations': {'mechanism': 'DNA cleavage'}, 'aliases': ['TALENs']},
    "ZINC_FINGER_NUCLEASE": {'description': 'Zinc finger nucleases for gene editing', 'meaning': 'NCIT:C111904', 'annotations': {'mechanism': 'DNA cleavage'}, 'aliases': ['ZFN']},
    "TRANSPOSON_MUTAGENESIS": {'description': 'Transposon-mediated insertional mutagenesis', 'meaning': 'OBI:0001187', 'annotations': {'mechanism': 'random insertion'}, 'aliases': ['transposon insertion']},
    "CHEMICAL_MUTAGENESIS": {'description': 'Chemical mutagen-induced mutagenesis', 'meaning': 'OBI:0001183', 'annotations': {'mechanism': 'base modification'}, 'aliases': ['ENU mutagenesis', 'EMS mutagenesis']},
    "OVEREXPRESSION": {'description': 'Transgene overexpression', 'meaning': 'OBI:0002452', 'annotations': {'effect': 'gain of function'}, 'aliases': ['transgene expression']},
}

class GeneKnockoutMethodEnum(RichEnum):
    """
    Specific methods for creating gene knockouts in model systems
    """
    # Enum members
    HOMOLOGOUS_RECOMBINATION = "HOMOLOGOUS_RECOMBINATION"
    CRISPR_KNOCKOUT = "CRISPR_KNOCKOUT"
    CONDITIONAL_KNOCKOUT = "CONDITIONAL_KNOCKOUT"
    CONSTITUTIVE_KNOCKOUT = "CONSTITUTIVE_KNOCKOUT"
    TISSUE_SPECIFIC_KNOCKOUT = "TISSUE_SPECIFIC_KNOCKOUT"
    INDUCIBLE_KNOCKOUT = "INDUCIBLE_KNOCKOUT"

# Set metadata after class creation
GeneKnockoutMethodEnum._metadata = {
    "HOMOLOGOUS_RECOMBINATION": {'description': 'Traditional homologous recombination-based knockout', 'meaning': 'OBI:0001186', 'annotations': {'use': 'ES cell targeting'}},
    "CRISPR_KNOCKOUT": {'description': 'CRISPR-mediated gene knockout', 'annotations': {'mechanism': 'indel formation'}, 'aliases': ['CRISPR KO']},
    "CONDITIONAL_KNOCKOUT": {'description': 'Conditional/inducible gene knockout (Cre-lox or similar)', 'annotations': {'mechanism': 'Cre-lox recombination'}, 'aliases': ['cKO', 'floxed']},
    "CONSTITUTIVE_KNOCKOUT": {'description': 'Constitutive whole-body gene knockout', 'aliases': ['germline knockout']},
    "TISSUE_SPECIFIC_KNOCKOUT": {'description': 'Tissue or cell type-specific gene knockout', 'annotations': {'mechanism': 'tissue-specific Cre'}},
    "INDUCIBLE_KNOCKOUT": {'description': 'Temporally inducible gene knockout', 'annotations': {'mechanism': 'CreERT2'}, 'aliases': ['tamoxifen-inducible']},
}

class GenotypeEnum(RichEnum):
    """
    Allelic states for genotype description
    """
    # Enum members
    HOMOZYGOUS_WILDTYPE = "HOMOZYGOUS_WILDTYPE"
    HETEROZYGOUS = "HETEROZYGOUS"
    HOMOZYGOUS_MUTANT = "HOMOZYGOUS_MUTANT"
    HEMIZYGOUS = "HEMIZYGOUS"
    COMPOUND_HETEROZYGOUS = "COMPOUND_HETEROZYGOUS"

# Set metadata after class creation
GenotypeEnum._metadata = {
    "HOMOZYGOUS_WILDTYPE": {'description': 'Homozygous wild-type alleles', 'aliases': ['+/+', 'wild-type', 'WT']},
    "HETEROZYGOUS": {'description': 'Heterozygous for mutation or deletion', 'aliases': ['+/-', 'het']},
    "HOMOZYGOUS_MUTANT": {'description': 'Homozygous for mutation or deletion', 'aliases': ['-/-', 'None', 'KO']},
    "HEMIZYGOUS": {'description': 'Hemizygous (single allele, X-linked or deletion)', 'aliases': ['-/Y']},
    "COMPOUND_HETEROZYGOUS": {'description': 'Compound heterozygous (two different mutant alleles)', 'aliases': ['compound het']},
}

class VectorTypeEnum(RichEnum):
    """
    Types of vectors used for gene delivery in research
    """
    # Enum members
    LENTIVIRAL = "LENTIVIRAL"
    RETROVIRAL = "RETROVIRAL"
    ADENOVIRAL = "ADENOVIRAL"
    AAV = "AAV"
    PLASMID = "PLASMID"
    MRNA = "MRNA"
    LNP = "LNP"
    ELECTROPORATION = "ELECTROPORATION"

# Set metadata after class creation
VectorTypeEnum._metadata = {
    "LENTIVIRAL": {'description': 'Lentiviral vector', 'meaning': 'NCIT:C73481', 'annotations': {'integration': 'integrating'}},
    "RETROVIRAL": {'description': 'Retroviral vector (gamma-retrovirus)', 'meaning': 'NCIT:C16886', 'annotations': {'integration': 'integrating'}},
    "ADENOVIRAL": {'description': 'Adenoviral vector', 'meaning': 'NCIT:C73475', 'annotations': {'integration': 'non-integrating'}},
    "AAV": {'description': 'Adeno-associated viral vector', 'meaning': 'NCIT:C73476', 'annotations': {'integration': 'non-integrating (episomal)'}, 'aliases': ['adeno-associated virus']},
    "PLASMID": {'description': 'Plasmid DNA vector', 'meaning': 'NCIT:C730', 'annotations': {'delivery': 'transfection', 'duration': 'transient'}},
    "MRNA": {'description': 'mRNA delivery', 'meaning': 'NCIT:C813', 'annotations': {'duration': 'transient'}},
    "LNP": {'description': 'Lipid nanoparticle delivery', 'annotations': {'cargo': 'mRNA, siRNA'}, 'aliases': ['lipid nanoparticle']},
    "ELECTROPORATION": {'description': 'Electroporation-based delivery', 'meaning': 'OBI:0001937', 'annotations': {'method': 'physical'}},
}

__all__ = [
    "GenePerturbationMethodEnum",
    "GeneKnockoutMethodEnum",
    "GenotypeEnum",
    "VectorTypeEnum",
]