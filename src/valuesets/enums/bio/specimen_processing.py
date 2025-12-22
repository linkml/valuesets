"""
Specimen Processing Value Sets

Value sets for specimen and sample processing methods including preservation, fixation, and preparation techniques used in biological research.

Generated from: bio/specimen_processing.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class SpecimenPreparationMethodEnum(RichEnum):
    """
    Methods for preparing and preserving biological specimens for analysis. Sourced from NF-OSI metadata dictionary and Human Cell Atlas standards.
    """
    # Enum members
    FFPE = "FFPE"
    FORMALIN_FIXED = "FORMALIN_FIXED"
    CRYOPRESERVED = "CRYOPRESERVED"
    VIABLY_FROZEN = "VIABLY_FROZEN"
    FLASH_FROZEN = "FLASH_FROZEN"
    FRESH_COLLECTED = "FRESH_COLLECTED"
    OCT_EMBEDDED = "OCT_EMBEDDED"
    RNALATER = "RNALATER"
    ETHANOL_PRESERVED = "ETHANOL_PRESERVED"
    METHANOL_FIXED = "METHANOL_FIXED"
    ACETONE_FIXED = "ACETONE_FIXED"
    PAXGENE_FIXED = "PAXgene_FIXED"
    DRIED = "DRIED"
    LYOPHILIZED = "LYOPHILIZED"

# Set metadata after class creation
SpecimenPreparationMethodEnum._metadata = {
    "FFPE": {'description': 'Formalin-fixed, paraffin-embedded tissue preservation', 'meaning': 'NCIT:C143028', 'annotations': {'fixative': 'formalin', 'embedding': 'paraffin'}, 'aliases': ['Formalin-fixed paraffin-embedded', 'formalin-fixed, paraffin-embedded']},
    "FORMALIN_FIXED": {'description': 'Tissue fixed with formalin without paraffin embedding', 'meaning': 'NCIT:C84516', 'annotations': {'fixative': 'formalin'}, 'aliases': ['formalin-fixed']},
    "CRYOPRESERVED": {'description': 'Specimen preserved by freezing with cryoprotectant', 'meaning': 'NCIT:C16475', 'annotations': {'temperature': 'ultra-low'}, 'aliases': ['Cryopreserved']},
    "VIABLY_FROZEN": {'description': 'Specimen frozen while maintaining cell viability', 'annotations': {'viability': 'preserved'}, 'aliases': ['Viably frozen']},
    "FLASH_FROZEN": {'description': 'Rapid freezing to preserve molecular integrity', 'meaning': 'NCIT:C178955', 'annotations': {'method': 'rapid freezing'}, 'aliases': ['Flash frozen', 'snap frozen']},
    "FRESH_COLLECTED": {'description': 'Freshly collected specimen without preservation', 'annotations': {'preservation': 'none'}, 'aliases': ['Fresh collected', 'fresh']},
    "OCT_EMBEDDED": {'description': 'Tissue embedded in optimal cutting temperature compound', 'meaning': 'OBI:0001472', 'annotations': {'embedding': 'OCT compound', 'purpose': 'cryosectioning'}, 'aliases': ['OCT', 'OCT embedded']},
    "RNALATER": {'description': 'Storage in reagent that stabilizes and protects cellular RNA', 'annotations': {'purpose': 'RNA stabilization', 'manufacturer': 'Thermo Fisher'}, 'aliases': ['RNAlater']},
    "ETHANOL_PRESERVED": {'description': 'Specimen preserved in ethanol', 'annotations': {'preservative': 'ethanol'}, 'aliases': ['ethanol']},
    "METHANOL_FIXED": {'description': 'Specimen fixed with methanol', 'annotations': {'fixative': 'methanol'}, 'aliases': ['methanol']},
    "ACETONE_FIXED": {'description': 'Specimen fixed with acetone', 'annotations': {'fixative': 'acetone'}},
    "PAXGENE_FIXED": {'description': 'Tissue fixed using PAXgene tissue system', 'annotations': {'purpose': 'RNA and DNA preservation'}},
    "DRIED": {'description': 'Air-dried or desiccated specimen', 'aliases': ['air-dried']},
    "LYOPHILIZED": {'description': 'Freeze-dried specimen', 'meaning': 'NCIT:C28175', 'aliases': ['freeze-dried', 'lyophilization']},
}

class TissuePreservationEnum(RichEnum):
    """
    Broader categorization of tissue preservation approaches
    """
    # Enum members
    FROZEN = "FROZEN"
    FIXED = "FIXED"
    FRESH = "FRESH"
    EMBEDDED = "EMBEDDED"

# Set metadata after class creation
TissuePreservationEnum._metadata = {
    "FROZEN": {'description': 'Tissue preserved by freezing', 'meaning': 'NCIT:C70717'},
    "FIXED": {'description': 'Tissue preserved by chemical fixation', 'meaning': 'NCIT:C19328'},
    "FRESH": {'description': 'Fresh unfixed tissue'},
    "EMBEDDED": {'description': 'Tissue embedded in medium (paraffin, OCT, etc.)'},
}

class SpecimenCollectionMethodEnum(RichEnum):
    """
    Methods for collecting biological specimens
    """
    # Enum members
    BIOPSY = "BIOPSY"
    SURGICAL_RESECTION = "SURGICAL_RESECTION"
    AUTOPSY = "AUTOPSY"
    FINE_NEEDLE_ASPIRATE = "FINE_NEEDLE_ASPIRATE"
    CORE_NEEDLE_BIOPSY = "CORE_NEEDLE_BIOPSY"
    PUNCH_BIOPSY = "PUNCH_BIOPSY"
    SWAB = "SWAB"
    VENIPUNCTURE = "VENIPUNCTURE"
    LUMBAR_PUNCTURE = "LUMBAR_PUNCTURE"
    LAVAGE = "LAVAGE"

# Set metadata after class creation
SpecimenCollectionMethodEnum._metadata = {
    "BIOPSY": {'description': 'Tissue sample obtained by biopsy', 'meaning': 'NCIT:C15189'},
    "SURGICAL_RESECTION": {'description': 'Tissue obtained during surgical resection', 'meaning': 'NCIT:C15329'},
    "AUTOPSY": {'description': 'Specimen obtained at autopsy', 'meaning': 'NCIT:C25153'},
    "FINE_NEEDLE_ASPIRATE": {'description': 'Sample obtained by fine needle aspiration', 'meaning': 'NCIT:C15361', 'aliases': ['FNA']},
    "CORE_NEEDLE_BIOPSY": {'description': 'Sample obtained by core needle biopsy', 'meaning': 'NCIT:C15190'},
    "PUNCH_BIOPSY": {'description': 'Sample obtained by punch biopsy', 'meaning': 'NCIT:C15195'},
    "SWAB": {'description': 'Sample collected by swabbing', 'meaning': 'OBI:0002822'},
    "VENIPUNCTURE": {'description': 'Blood sample obtained by venipuncture', 'meaning': 'NCIT:C28221'},
    "LUMBAR_PUNCTURE": {'description': 'CSF sample obtained by lumbar puncture', 'meaning': 'NCIT:C15327', 'aliases': ['spinal tap']},
    "LAVAGE": {'description': 'Sample obtained by lavage (washing)', 'meaning': 'NCIT:C15282'},
}

class SpecimenTypeEnum(RichEnum):
    """
    Types of biological specimens used in research
    """
    # Enum members
    TISSUE = "TISSUE"
    BLOOD = "BLOOD"
    PLASMA = "PLASMA"
    SERUM = "SERUM"
    BUFFY_COAT = "BUFFY_COAT"
    URINE = "URINE"
    SALIVA = "SALIVA"
    STOOL = "STOOL"
    CSF = "CSF"
    SWEAT = "SWEAT"
    MUCUS = "MUCUS"
    BONE_MARROW = "BONE_MARROW"
    PRIMARY_TUMOR = "PRIMARY_TUMOR"
    METASTATIC_TUMOR = "METASTATIC_TUMOR"
    TUMOR_ADJACENT_NORMAL = "TUMOR_ADJACENT_NORMAL"
    ORGANOID = "ORGANOID"
    SPHEROID = "SPHEROID"
    MICROTISSUE = "MICROTISSUE"
    PDX_TISSUE = "PDX_TISSUE"
    CDX_TISSUE = "CDX_TISSUE"

# Set metadata after class creation
SpecimenTypeEnum._metadata = {
    "TISSUE": {'description': 'Solid tissue specimen', 'meaning': 'NCIT:C12801'},
    "BLOOD": {'description': 'Whole blood specimen', 'meaning': 'NCIT:C12434'},
    "PLASMA": {'description': 'Blood plasma specimen', 'meaning': 'NCIT:C13356'},
    "SERUM": {'description': 'Blood serum specimen', 'meaning': 'NCIT:C13325'},
    "BUFFY_COAT": {'description': 'Leukocyte-enriched blood fraction', 'meaning': 'NCIT:C84507'},
    "URINE": {'description': 'Urine specimen', 'meaning': 'NCIT:C13283'},
    "SALIVA": {'description': 'Saliva specimen', 'meaning': 'NCIT:C13275'},
    "STOOL": {'description': 'Stool/fecal specimen', 'meaning': 'NCIT:C13234'},
    "CSF": {'description': 'Cerebrospinal fluid specimen', 'meaning': 'NCIT:C12692', 'aliases': ['cerebrospinal fluid']},
    "SWEAT": {'description': 'Sweat specimen'},
    "MUCUS": {'description': 'Mucus specimen'},
    "BONE_MARROW": {'description': 'Bone marrow specimen', 'meaning': 'NCIT:C12431'},
    "PRIMARY_TUMOR": {'description': 'Primary tumor tissue specimen', 'meaning': 'NCIT:C162622'},
    "METASTATIC_TUMOR": {'description': 'Metastatic tumor tissue specimen'},
    "TUMOR_ADJACENT_NORMAL": {'description': 'Normal tissue adjacent to tumor', 'meaning': 'NCIT:C164032'},
    "ORGANOID": {'description': 'Organoid specimen', 'meaning': 'NCIT:C172259'},
    "SPHEROID": {'description': 'Cell spheroid specimen'},
    "MICROTISSUE": {'description': 'Engineered microtissue specimen'},
    "PDX_TISSUE": {'description': 'Patient-derived xenograft tissue', 'meaning': 'NCIT:C156443', 'aliases': ['PDX tissue']},
    "CDX_TISSUE": {'description': 'Cell line-derived xenograft tissue', 'aliases': ['CDX tissue']},
}

__all__ = [
    "SpecimenPreparationMethodEnum",
    "TissuePreservationEnum",
    "SpecimenCollectionMethodEnum",
    "SpecimenTypeEnum",
]