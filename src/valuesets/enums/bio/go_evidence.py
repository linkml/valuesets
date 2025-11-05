"""
Gene Ontology Evidence Codes

Value sets for Gene Ontology evidence codes and electronic annotation methods

Generated from: bio/go_evidence.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class GOEvidenceCode(RichEnum):
    """
    Gene Ontology evidence codes mapped to Evidence and Conclusion Ontology (ECO) terms
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
    "EXP": {'meaning': 'ECO:0000269', 'aliases': ['experimental evidence used in manual assertion']},
    "IDA": {'meaning': 'ECO:0000314', 'aliases': ['direct assay evidence used in manual assertion']},
    "IPI": {'meaning': 'ECO:0000353', 'aliases': ['physical interaction evidence used in manual assertion']},
    "IMP": {'meaning': 'ECO:0000315', 'aliases': ['mutant phenotype evidence used in manual assertion']},
    "IGI": {'meaning': 'ECO:0000316', 'aliases': ['genetic interaction evidence used in manual assertion']},
    "IEP": {'meaning': 'ECO:0000270', 'aliases': ['expression pattern evidence used in manual assertion']},
    "HTP": {'meaning': 'ECO:0006056', 'aliases': ['high throughput evidence used in manual assertion']},
    "HDA": {'meaning': 'ECO:0007005', 'aliases': ['high throughput direct assay evidence used in manual assertion']},
    "HMP": {'meaning': 'ECO:0007001', 'aliases': ['high throughput mutant phenotypic evidence used in manual assertion']},
    "HGI": {'meaning': 'ECO:0007003', 'aliases': ['high throughput genetic interaction phenotypic evidence used in manual assertion']},
    "HEP": {'meaning': 'ECO:0007007', 'aliases': ['high throughput expression pattern evidence used in manual assertion']},
    "IBA": {'meaning': 'ECO:0000318', 'aliases': ['biological aspect of ancestor evidence used in manual assertion']},
    "IBD": {'meaning': 'ECO:0000319', 'aliases': ['biological aspect of descendant evidence used in manual assertion']},
    "IKR": {'meaning': 'ECO:0000320', 'aliases': ['phylogenetic determination of loss of key residues evidence used in manual assertion']},
    "IRD": {'meaning': 'ECO:0000321', 'aliases': ['rapid divergence from ancestral sequence evidence used in manual assertion']},
    "ISS": {'meaning': 'ECO:0000250', 'aliases': ['sequence similarity evidence used in manual assertion']},
    "ISO": {'meaning': 'ECO:0000266', 'aliases': ['sequence orthology evidence used in manual assertion']},
    "ISA": {'meaning': 'ECO:0000247', 'aliases': ['sequence alignment evidence used in manual assertion']},
    "ISM": {'meaning': 'ECO:0000255', 'aliases': ['match to sequence model evidence used in manual assertion']},
    "IGC": {'meaning': 'ECO:0000317', 'aliases': ['genomic context evidence used in manual assertion']},
    "RCA": {'meaning': 'ECO:0000245', 'aliases': ['automatically integrated combinatorial evidence used in manual assertion']},
    "TAS": {'meaning': 'ECO:0000304', 'aliases': ['author statement supported by traceable reference used in manual assertion']},
    "NAS": {'meaning': 'ECO:0000303', 'aliases': ['author statement without traceable support used in manual assertion']},
    "IC": {'meaning': 'ECO:0000305', 'aliases': ['curator inference used in manual assertion']},
    "ND": {'meaning': 'ECO:0000307', 'aliases': ['no evidence data found used in manual assertion']},
    "IEA": {'meaning': 'ECO:0000501', 'aliases': ['evidence used in automatic assertion']},
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