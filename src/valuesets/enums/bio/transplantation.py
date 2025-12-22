"""
Transplantation Value Sets

Value sets for transplantation types and model systems used in biological and medical research, including xenografts and allografts.

Generated from: bio/transplantation.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class TransplantationTypeEnum(RichEnum):
    """
    Classification of transplants based on the genetic relationship between donor and recipient organisms.
    """
    # Enum members
    XENOGRAFT = "XENOGRAFT"
    ALLOGRAFT = "ALLOGRAFT"
    AUTOGRAFT = "AUTOGRAFT"
    ISOGRAFT = "ISOGRAFT"

# Set metadata after class creation
TransplantationTypeEnum._metadata = {
    "XENOGRAFT": {'description': 'Transplantation of cells, tissues, or organs between animals of different species', 'meaning': 'NCIT:C12932', 'annotations': {'donor_recipient': 'different species', 'example': 'human tumor in mouse'}, 'aliases': ['xenotransplant', 'heterograft']},
    "ALLOGRAFT": {'description': 'Transplantation of cells, tissues, or organs between genetically different individuals of the same species', 'meaning': 'SNOMED:7970006', 'annotations': {'donor_recipient': 'same species, different individual', 'example': 'bone marrow transplant'}, 'aliases': ['allogeneic transplant', 'homograft']},
    "AUTOGRAFT": {'description': 'Transplantation of tissue from one body location to another within the same individual', 'meaning': 'NCIT:C40997', 'annotations': {'donor_recipient': 'same individual', 'example': 'skin graft, autologous stem cell transplant'}, 'aliases': ['autologous transplant', 'autotransplant']},
    "ISOGRAFT": {'description': 'Transplantation of cells, tissues, or organs between genetically identical individuals (e.g., identical twins, inbred strains)', 'meaning': 'NCIT:C41000', 'annotations': {'donor_recipient': 'genetically identical', 'example': 'transplant between identical twins'}, 'aliases': ['syngeneic transplant', 'isogeneic transplant']},
}

class XenograftModelEnum(RichEnum):
    """
    Types of xenograft models used in cancer and disease research
    """
    # Enum members
    PDX = "PDX"
    CDX = "CDX"
    PDOX = "PDOX"
    HUMANIZED_MOUSE = "HUMANIZED_MOUSE"

# Set metadata after class creation
XenograftModelEnum._metadata = {
    "PDX": {'description': 'Patient-derived xenograft - tumor tissue directly from patient', 'meaning': 'NCIT:C122738', 'annotations': {'source': 'patient tumor', 'passage': 'primary or passaged'}, 'aliases': ['patient-derived xenograft']},
    "CDX": {'description': 'Cell line-derived xenograft - from established cell lines', 'annotations': {'source': 'cell line'}, 'aliases': ['cell line-derived xenograft']},
    "PDOX": {'description': 'Patient-derived orthotopic xenograft', 'annotations': {'implantation': 'orthotopic site'}, 'aliases': ['patient-derived orthotopic xenograft']},
    "HUMANIZED_MOUSE": {'description': 'Mouse engrafted with human immune cells', 'meaning': 'NCIT:C122961', 'annotations': {'engraftment': 'human immune system'}, 'aliases': ['humanized mouse model']},
}

class ModelSystemTypeEnum(RichEnum):
    """
    Types of model systems used in biological research
    """
    # Enum members
    CELL_LINE = "CELL_LINE"
    PRIMARY_CELLS = "PRIMARY_CELLS"
    ORGANOID = "ORGANOID"
    SPHEROID = "SPHEROID"
    TISSUE_EXPLANT = "TISSUE_EXPLANT"
    ANIMAL_MODEL = "ANIMAL_MODEL"
    TRANSGENIC_MODEL = "TRANSGENIC_MODEL"
    KNOCKOUT_MODEL = "KNOCKOUT_MODEL"
    KNOCKIN_MODEL = "KNOCKIN_MODEL"
    PDX_MODEL = "PDX_MODEL"
    GEMM = "GEMM"
    ZEBRAFISH_MODEL = "ZEBRAFISH_MODEL"
    DROSOPHILA_MODEL = "DROSOPHILA_MODEL"
    C_ELEGANS_MODEL = "C_ELEGANS_MODEL"
    YEAST_MODEL = "YEAST_MODEL"
    IPSC_DERIVED = "IPSC_DERIVED"

# Set metadata after class creation
ModelSystemTypeEnum._metadata = {
    "CELL_LINE": {'description': 'Immortalized or primary cell lines', 'meaning': 'NCIT:C16403'},
    "PRIMARY_CELLS": {'description': 'Primary cells directly from tissue', 'meaning': 'NCIT:C70598'},
    "ORGANOID": {'description': 'Three-dimensional organ-like cultures', 'meaning': 'NCIT:C172259'},
    "SPHEROID": {'description': 'Three-dimensional cell aggregates', 'meaning': 'NCIT:C176153'},
    "TISSUE_EXPLANT": {'description': 'Tissue explant culture', 'meaning': 'NCIT:C127861'},
    "ANIMAL_MODEL": {'description': 'In vivo animal model', 'meaning': 'NCIT:C71164'},
    "TRANSGENIC_MODEL": {'description': 'Genetically engineered transgenic animal', 'meaning': 'NCIT:C14348'},
    "KNOCKOUT_MODEL": {'description': 'Gene knockout animal model', 'meaning': 'NCIT:C14341'},
    "KNOCKIN_MODEL": {'description': 'Gene knock-in animal model'},
    "PDX_MODEL": {'description': 'Patient-derived xenograft model', 'meaning': 'NCIT:C122738'},
    "GEMM": {'description': 'Genetically engineered mouse model', 'aliases': ['genetically engineered mouse model']},
    "ZEBRAFISH_MODEL": {'description': 'Zebrafish disease model'},
    "DROSOPHILA_MODEL": {'description': 'Drosophila (fruit fly) disease model'},
    "C_ELEGANS_MODEL": {'description': 'C. elegans disease model'},
    "YEAST_MODEL": {'description': 'Yeast genetic model'},
    "IPSC_DERIVED": {'description': 'Induced pluripotent stem cell-derived model', 'meaning': 'EFO:0004905', 'aliases': ['iPSC-derived']},
}

__all__ = [
    "TransplantationTypeEnum",
    "XenograftModelEnum",
    "ModelSystemTypeEnum",
]