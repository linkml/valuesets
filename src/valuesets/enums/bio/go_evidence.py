"""
Gene Ontology Evidence Codes

Value sets for Gene Ontology evidence codes and electronic annotation methods

Generated from: bio/go_evidence.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class GOEvidenceCode(RichEnum):
    """
    Gene Ontology evidence codes used to describe the type of support for GO annotations. Each code maps to the Evidence and Conclusion Ontology (ECO). Evidence codes are categorized by whether they represent experimental evidence, computational analysis, phylogenetic inference, author statements, or electronic annotation. All codes except IEA represent manual curation.
    """
    # Enum members
    EXP = "EXP"
    IDA = "IDA"
    IPI = "IPI"
    IMP = "IMP"
    IGI = "IGI"
    IEP = "IEP"
    HTP = "HTP"
    HDA = "HDA"
    HMP = "HMP"
    HGI = "HGI"
    HEP = "HEP"
    IBA = "IBA"
    IBD = "IBD"
    IKR = "IKR"
    IRD = "IRD"
    ISS = "ISS"
    ISO = "ISO"
    ISA = "ISA"
    ISM = "ISM"
    IGC = "IGC"
    RCA = "RCA"
    TAS = "TAS"
    NAS = "NAS"
    IC = "IC"
    ND = "ND"
    IEA = "IEA"

# Set metadata after class creation
GOEvidenceCode._metadata = {
    "EXP": {'description': 'General experimental evidence supporting a GO annotation', 'meaning': 'ECO:0000269', 'annotations': {'is_experimental': True, 'is_manual': True, 'is_high_throughput': False}, 'aliases': ['experimental evidence used in manual assertion']},
    "IDA": {'description': 'Evidence from a direct assay for the presence or activity of a gene product', 'meaning': 'ECO:0000314', 'annotations': {'is_experimental': True, 'is_manual': True, 'is_high_throughput': False}, 'aliases': ['direct assay evidence used in manual assertion']},
    "IPI": {'description': 'Evidence from physical interaction between gene products', 'meaning': 'ECO:0000353', 'annotations': {'is_experimental': True, 'is_manual': True, 'is_high_throughput': False}, 'aliases': ['physical interaction evidence used in manual assertion']},
    "IMP": {'description': 'Evidence from the phenotype of a mutant allele', 'meaning': 'ECO:0000315', 'annotations': {'is_experimental': True, 'is_manual': True, 'is_high_throughput': False}, 'aliases': ['mutant phenotype evidence used in manual assertion']},
    "IGI": {'description': 'Evidence from genetic interaction between genes', 'meaning': 'ECO:0000316', 'annotations': {'is_experimental': True, 'is_manual': True, 'is_high_throughput': False}, 'aliases': ['genetic interaction evidence used in manual assertion']},
    "IEP": {'description': 'Evidence from gene expression pattern data', 'meaning': 'ECO:0000270', 'annotations': {'is_experimental': True, 'is_manual': True, 'is_high_throughput': False}, 'aliases': ['expression pattern evidence used in manual assertion']},
    "HTP": {'description': 'Evidence from high-throughput experimental methods', 'meaning': 'ECO:0006056', 'annotations': {'is_experimental': True, 'is_manual': True, 'is_high_throughput': True}, 'aliases': ['high throughput evidence used in manual assertion']},
    "HDA": {'description': 'Evidence from high-throughput direct assay experiments', 'meaning': 'ECO:0007005', 'annotations': {'is_experimental': True, 'is_manual': True, 'is_high_throughput': True}, 'aliases': ['high throughput direct assay evidence used in manual assertion']},
    "HMP": {'description': 'Evidence from high-throughput mutant phenotype screening', 'meaning': 'ECO:0007001', 'annotations': {'is_experimental': True, 'is_manual': True, 'is_high_throughput': True}, 'aliases': ['high throughput mutant phenotypic evidence used in manual assertion']},
    "HGI": {'description': 'Evidence from high-throughput genetic interaction screening', 'meaning': 'ECO:0007003', 'annotations': {'is_experimental': True, 'is_manual': True, 'is_high_throughput': True}, 'aliases': ['high throughput genetic interaction phenotypic evidence used in manual assertion']},
    "HEP": {'description': 'Evidence from high-throughput expression profiling', 'meaning': 'ECO:0007007', 'annotations': {'is_experimental': True, 'is_manual': True, 'is_high_throughput': True}, 'aliases': ['high throughput expression pattern evidence used in manual assertion']},
    "IBA": {'description': 'Evidence from conservation of biological aspect in an ancestral sequence', 'meaning': 'ECO:0000318', 'annotations': {'is_experimental': False, 'is_manual': True, 'is_high_throughput': False, 'is_phylogenetic': True}, 'aliases': ['biological aspect of ancestor evidence used in manual assertion']},
    "IBD": {'description': 'Evidence from conservation of biological aspect in a descendant sequence', 'meaning': 'ECO:0000319', 'annotations': {'is_experimental': False, 'is_manual': True, 'is_high_throughput': False, 'is_phylogenetic': True}, 'aliases': ['biological aspect of descendant evidence used in manual assertion']},
    "IKR": {'description': 'Evidence from phylogenetic analysis showing loss of key residues', 'meaning': 'ECO:0000320', 'annotations': {'is_experimental': False, 'is_manual': True, 'is_high_throughput': False, 'is_phylogenetic': True}, 'aliases': ['phylogenetic determination of loss of key residues evidence used in manual assertion']},
    "IRD": {'description': 'Evidence from rapid divergence from ancestral sequence', 'meaning': 'ECO:0000321', 'annotations': {'is_experimental': False, 'is_manual': True, 'is_high_throughput': False, 'is_phylogenetic': True}, 'aliases': ['rapid divergence from ancestral sequence evidence used in manual assertion']},
    "ISS": {'description': 'Evidence from sequence or structural similarity to another annotated gene product', 'meaning': 'ECO:0000250', 'annotations': {'is_experimental': False, 'is_manual': True, 'is_high_throughput': False, 'is_computational': True}, 'aliases': ['sequence similarity evidence used in manual assertion']},
    "ISO": {'description': 'Evidence from orthology to an experimentally characterized gene product', 'meaning': 'ECO:0000266', 'annotations': {'is_experimental': False, 'is_manual': True, 'is_high_throughput': False, 'is_computational': True}, 'aliases': ['sequence orthology evidence used in manual assertion']},
    "ISA": {'description': 'Evidence from sequence alignment to an annotated gene product', 'meaning': 'ECO:0000247', 'annotations': {'is_experimental': False, 'is_manual': True, 'is_high_throughput': False, 'is_computational': True}, 'aliases': ['sequence alignment evidence used in manual assertion']},
    "ISM": {'description': 'Evidence from match to a sequence model (e.g., HMM, profile)', 'meaning': 'ECO:0000255', 'annotations': {'is_experimental': False, 'is_manual': True, 'is_high_throughput': False, 'is_computational': True}, 'aliases': ['match to sequence model evidence used in manual assertion']},
    "IGC": {'description': 'Evidence from genomic context such as synteny or gene neighborhood', 'meaning': 'ECO:0000317', 'annotations': {'is_experimental': False, 'is_manual': True, 'is_high_throughput': False, 'is_computational': True}, 'aliases': ['genomic context evidence used in manual assertion']},
    "RCA": {'description': 'Evidence from computational analysis that has been reviewed by a curator', 'meaning': 'ECO:0000245', 'annotations': {'is_experimental': False, 'is_manual': True, 'is_high_throughput': False, 'is_computational': True}, 'aliases': ['automatically integrated combinatorial evidence used in manual assertion']},
    "TAS": {'description': 'Evidence from an author statement in a published paper that can be traced to the original source', 'meaning': 'ECO:0000304', 'annotations': {'is_experimental': False, 'is_manual': True, 'is_high_throughput': False, 'is_author_statement': True}, 'aliases': ['author statement supported by traceable reference used in manual assertion']},
    "NAS": {'description': 'Evidence from an author statement that cannot be traced to the experimental source', 'meaning': 'ECO:0000303', 'annotations': {'is_experimental': False, 'is_manual': True, 'is_high_throughput': False, 'is_author_statement': True}, 'aliases': ['author statement without traceable support used in manual assertion']},
    "IC": {'description': 'Evidence inferred by a curator based on existing annotations and biological knowledge', 'meaning': 'ECO:0000305', 'annotations': {'is_experimental': False, 'is_manual': True, 'is_high_throughput': False, 'is_curator_inference': True}, 'aliases': ['curator inference used in manual assertion']},
    "ND": {'description': 'Indicates that no biological data is available to support an annotation', 'meaning': 'ECO:0000307', 'annotations': {'is_experimental': False, 'is_manual': True, 'is_high_throughput': False}, 'aliases': ['no evidence data found used in manual assertion']},
    "IEA": {'description': 'Evidence from automated electronic annotation pipelines without manual curation', 'meaning': 'ECO:0000501', 'annotations': {'is_experimental': False, 'is_manual': False, 'is_high_throughput': False, 'is_electronic': True}, 'aliases': ['evidence used in automatic assertion']},
}

class GOElectronicMethods(RichEnum):
    """
    Electronic annotation methods used in Gene Ontology, identified by GO_REF codes
    """
    # Enum members
    INTERPRO2GO = "INTERPRO2GO"
    EC2GO = "EC2GO"
    UNIPROTKB_KW2GO = "UNIPROTKB_KW2GO"
    UNIPROTKB_SUBCELL2GO = "UNIPROTKB_SUBCELL2GO"
    HAMAP_RULE2GO = "HAMAP_RULE2GO"
    UNIPATHWAY2GO = "UNIPATHWAY2GO"
    UNIRULE2GO = "UNIRULE2GO"
    RHEA2GO = "RHEA2GO"
    ENSEMBL_COMPARA = "ENSEMBL_COMPARA"
    PANTHER = "PANTHER"
    REACTOME = "REACTOME"
    RFAM2GO = "RFAM2GO"
    DICTYBASE = "DICTYBASE"
    MGI = "MGI"
    ZFIN = "ZFIN"
    FLYBASE = "FLYBASE"
    WORMBASE = "WORMBASE"
    SGD = "SGD"
    POMBASE = "POMBASE"
    METACYC2GO = "METACYC2GO"

# Set metadata after class creation
GOElectronicMethods._metadata = {
    "INTERPRO2GO": {'meaning': 'GO_REF:0000002'},
    "EC2GO": {'meaning': 'GO_REF:0000003'},
    "UNIPROTKB_KW2GO": {'meaning': 'GO_REF:0000004'},
    "UNIPROTKB_SUBCELL2GO": {'meaning': 'GO_REF:0000023'},
    "HAMAP_RULE2GO": {'meaning': 'GO_REF:0000020'},
    "UNIPATHWAY2GO": {'meaning': 'GO_REF:0000041'},
    "UNIRULE2GO": {'meaning': 'GO_REF:0000104'},
    "RHEA2GO": {'meaning': 'GO_REF:0000116'},
    "ENSEMBL_COMPARA": {'meaning': 'GO_REF:0000107'},
    "PANTHER": {'meaning': 'GO_REF:0000033'},
    "REACTOME": {'meaning': 'GO_REF:0000018'},
    "RFAM2GO": {'meaning': 'GO_REF:0000115'},
    "DICTYBASE": {'meaning': 'GO_REF:0000015'},
    "MGI": {'meaning': 'GO_REF:0000096'},
    "ZFIN": {'meaning': 'GO_REF:0000031'},
    "FLYBASE": {'meaning': 'GO_REF:0000047'},
    "WORMBASE": {'meaning': 'GO_REF:0000003'},
    "SGD": {'meaning': 'GO_REF:0000100'},
    "POMBASE": {'meaning': 'GO_REF:0000024'},
    "METACYC2GO": {'meaning': 'GO_REF:0000112'},
}

__all__ = [
    "GOEvidenceCode",
    "GOElectronicMethods",
]