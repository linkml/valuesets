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
    "FFPE": {'description': 'Formalin-fixed, paraffin-embedded tissue preservation', 'meaning': 'NCIT:C143028', 'annotations': {'fixative': 'formalin', 'embedding': 'paraffin'}, 'aliases': ['Formalin-fixed paraffin-embedded', 'formalin-fixed, paraffin-embedded', 'FFPE Tissue Block']},
    "FORMALIN_FIXED": {'description': 'Tissue fixed with formalin without paraffin embedding', 'annotations': {'fixative': 'formalin'}, 'aliases': ['formalin-fixed']},
    "CRYOPRESERVED": {'description': 'Specimen preserved by freezing with cryoprotectant', 'meaning': 'NCIT:C16475', 'annotations': {'temperature': 'ultra-low'}, 'aliases': ['Cryopreserved', 'Cryopreservation']},
    "VIABLY_FROZEN": {'description': 'Specimen frozen while maintaining cell viability', 'annotations': {'viability': 'preserved'}, 'aliases': ['Viably frozen']},
    "FLASH_FROZEN": {'description': 'Rapid freezing to preserve molecular integrity', 'annotations': {'method': 'rapid freezing'}, 'aliases': ['Flash frozen', 'snap frozen']},
    "FRESH_COLLECTED": {'description': 'Freshly collected specimen without preservation', 'annotations': {'preservation': 'none'}, 'aliases': ['Fresh collected', 'fresh']},
    "OCT_EMBEDDED": {'description': 'Tissue embedded in optimal cutting temperature compound', 'annotations': {'embedding': 'OCT compound', 'purpose': 'cryosectioning'}, 'aliases': ['OCT', 'OCT embedded']},
    "RNALATER": {'description': 'Storage in reagent that stabilizes and protects cellular RNA', 'annotations': {'purpose': 'RNA stabilization', 'manufacturer': 'Thermo Fisher'}, 'aliases': ['RNAlater']},
    "ETHANOL_PRESERVED": {'description': 'Specimen preserved in ethanol', 'annotations': {'preservative': 'ethanol'}, 'aliases': ['ethanol']},
    "METHANOL_FIXED": {'description': 'Specimen fixed with methanol', 'annotations': {'fixative': 'methanol'}, 'aliases': ['methanol']},
    "ACETONE_FIXED": {'description': 'Specimen fixed with acetone', 'annotations': {'fixative': 'acetone'}},
    "PAXGENE_FIXED": {'description': 'Tissue fixed using PAXgene tissue system', 'annotations': {'purpose': 'RNA and DNA preservation'}},
    "DRIED": {'description': 'Air-dried or desiccated specimen', 'aliases': ['air-dried']},
    "LYOPHILIZED": {'description': 'Freeze-dried specimen', 'meaning': 'NCIT:C28150', 'aliases': ['freeze-dried', 'lyophilization', 'Freeze-Drying']},
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
    "FROZEN": {'description': 'Tissue preserved by freezing', 'meaning': 'NCIT:C70717', 'aliases': ['Frozen Specimen']},
    "FIXED": {'description': 'Tissue preserved by chemical fixation', 'meaning': 'NCIT:C25219', 'aliases': ['Fixation']},
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
    "BIOPSY": {'description': 'Tissue sample obtained by biopsy', 'meaning': 'NCIT:C15189', 'aliases': ['Biopsy Procedure']},
    "SURGICAL_RESECTION": {'description': 'Tissue obtained during surgical resection', 'meaning': 'NCIT:C15329', 'aliases': ['Surgical Procedure']},
    "AUTOPSY": {'description': 'Specimen obtained at autopsy', 'meaning': 'NCIT:C25153', 'aliases': ['Autopsy']},
    "FINE_NEEDLE_ASPIRATE": {'description': 'Sample obtained by fine needle aspiration', 'meaning': 'NCIT:C15361', 'aliases': ['FNA', 'Fine-Needle Aspiration']},
    "CORE_NEEDLE_BIOPSY": {'description': 'Sample obtained by core needle biopsy', 'meaning': 'NCIT:C15190', 'aliases': ['Needle Biopsy']},
    "PUNCH_BIOPSY": {'description': 'Sample obtained by punch biopsy'},
    "SWAB": {'description': 'Sample collected by swabbing'},
    "VENIPUNCTURE": {'description': 'Blood sample obtained by venipuncture', 'meaning': 'NCIT:C28221', 'aliases': ['Phlebotomy']},
    "LUMBAR_PUNCTURE": {'description': 'CSF sample obtained by lumbar puncture', 'meaning': 'NCIT:C15327', 'aliases': ['spinal tap', 'Lumbar Puncture']},
    "LAVAGE": {'description': 'Sample obtained by lavage (washing)'},
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
    "TISSUE": {'description': 'Solid tissue specimen', 'meaning': 'NCIT:C12801', 'aliases': ['Tissue']},
    "BLOOD": {'description': 'Whole blood specimen', 'meaning': 'NCIT:C12434', 'aliases': ['Blood']},
    "PLASMA": {'description': 'Blood plasma specimen', 'meaning': 'NCIT:C13356', 'aliases': ['Plasma']},
    "SERUM": {'description': 'Blood serum specimen', 'meaning': 'NCIT:C13325', 'aliases': ['Serum']},
    "BUFFY_COAT": {'description': 'Leukocyte-enriched blood fraction', 'meaning': 'NCIT:C84507', 'aliases': ['Buffy Coat']},
    "URINE": {'description': 'Urine specimen', 'meaning': 'NCIT:C13283', 'aliases': ['Urine']},
    "SALIVA": {'description': 'Saliva specimen', 'meaning': 'NCIT:C13275', 'aliases': ['Saliva']},
    "STOOL": {'description': 'Stool/fecal specimen', 'meaning': 'NCIT:C13234', 'aliases': ['Feces', 'fecal']},
    "CSF": {'description': 'Cerebrospinal fluid specimen', 'meaning': 'NCIT:C12692', 'aliases': ['cerebrospinal fluid', 'Cerebrospinal Fluid']},
    "SWEAT": {'description': 'Sweat specimen'},
    "MUCUS": {'description': 'Mucus specimen'},
    "BONE_MARROW": {'description': 'Bone marrow specimen', 'meaning': 'NCIT:C12431', 'aliases': ['Bone Marrow']},
    "PRIMARY_TUMOR": {'description': 'Primary tumor tissue specimen', 'meaning': 'NCIT:C8509', 'aliases': ['Primary Neoplasm']},
    "METASTATIC_TUMOR": {'description': 'Metastatic tumor tissue specimen', 'meaning': 'NCIT:C3261', 'aliases': ['Metastatic Neoplasm']},
    "TUMOR_ADJACENT_NORMAL": {'description': 'Normal tissue adjacent to tumor', 'meaning': 'NCIT:C164032', 'aliases': ['Tumor-Adjacent Normal Specimen']},
    "ORGANOID": {'description': 'Organoid specimen', 'meaning': 'NCIT:C172259', 'aliases': ['Organoid']},
    "SPHEROID": {'description': 'Cell spheroid specimen'},
    "MICROTISSUE": {'description': 'Engineered microtissue specimen'},
    "PDX_TISSUE": {'description': 'Patient-derived xenograft tissue', 'meaning': 'NCIT:C122936', 'aliases': ['PDX tissue', 'Patient Derived Xenograft']},
    "CDX_TISSUE": {'description': 'Cell line-derived xenograft tissue', 'aliases': ['CDX tissue']},
}

class AnalyteTypeEnum(RichEnum):
    """
    Types of analytes that can be extracted from biological specimens for molecular analysis.
    """
    # Enum members
    DNA = "DNA"
    RNA = "RNA"
    TOTAL_RNA = "TOTAL_RNA"
    FFPE_DNA = "FFPE_DNA"
    FFPE_RNA = "FFPE_RNA"
    CFDNA = "cfDNA"
    PROTEIN = "PROTEIN"
    NUCLEI_RNA = "NUCLEI_RNA"
    REPLI_G_DNA = "REPLI_G_DNA"
    REPLI_G_X_DNA = "REPLI_G_X_DNA"
    REPLI_G_POOLED_DNA = "REPLI_G_POOLED_DNA"
    GENOMEPLEX_DNA = "GENOMEPLEX_DNA"
    EBV_IMMORTALIZED = "EBV_IMMORTALIZED"

# Set metadata after class creation
AnalyteTypeEnum._metadata = {
    "DNA": {'description': 'Deoxyribonucleic acid', 'meaning': 'NCIT:C198567', 'aliases': ['DNA Specimen']},
    "RNA": {'description': 'Ribonucleic acid', 'meaning': 'NCIT:C198568', 'aliases': ['RNA Specimen']},
    "TOTAL_RNA": {'description': 'Total RNA including all RNA species'},
    "FFPE_DNA": {'description': 'DNA extracted from formalin-fixed paraffin-embedded tissue', 'aliases': ['Formalin-Fixed Paraffin-Embedded DNA']},
    "FFPE_RNA": {'description': 'RNA extracted from formalin-fixed paraffin-embedded tissue', 'aliases': ['Formalin-Fixed Paraffin-Embedded RNA']},
    "CFDNA": {'description': 'Cell-free DNA found in blood plasma', 'meaning': 'NCIT:C128274', 'aliases': ['Circulating Cell-Free DNA', 'cell-free DNA']},
    "PROTEIN": {'description': 'Protein analyte', 'meaning': 'NCIT:C17021', 'aliases': ['Protein']},
    "NUCLEI_RNA": {'description': 'RNA isolated from cell nuclei'},
    "REPLI_G_DNA": {'description': 'Whole genome amplified DNA using Repli-G technology', 'aliases': ['Repli-G (Qiagen) DNA']},
    "REPLI_G_X_DNA": {'description': 'Whole genome amplified DNA using Repli-G X technology', 'aliases': ['Repli-G X (Qiagen) DNA']},
    "REPLI_G_POOLED_DNA": {'description': 'Pooled whole genome amplified DNA using Repli-G', 'aliases': ['Repli-G Pooled (Qiagen) DNA']},
    "GENOMEPLEX_DNA": {'description': 'Whole genome amplified DNA using GenomePlex technology', 'aliases': ['GenomePlex (Rubicon) Amplified DNA']},
    "EBV_IMMORTALIZED": {'description': 'DNA/cells from EBV immortalized cell lines', 'aliases': ['EBV Immortalized Normal']},
}

class SourceMaterialTypeEnum(RichEnum):
    """
    Types of source materials from which specimens are derived, particularly relevant for cancer and tissue banking research.
    """
    # Enum members
    PRIMARY_TUMOR = "PRIMARY_TUMOR"
    METASTATIC = "METASTATIC"
    RECURRENT_TUMOR = "RECURRENT_TUMOR"
    BLOOD_DERIVED_NORMAL = "BLOOD_DERIVED_NORMAL"
    BLOOD_DERIVED_CANCER_PERIPHERAL_BLOOD = "BLOOD_DERIVED_CANCER_PERIPHERAL_BLOOD"
    BLOOD_DERIVED_CANCER_BONE_MARROW = "BLOOD_DERIVED_CANCER_BONE_MARROW"
    BONE_MARROW_NORMAL = "BONE_MARROW_NORMAL"
    SOLID_TISSUE_NORMAL = "SOLID_TISSUE_NORMAL"
    BUCCAL_CELL_NORMAL = "BUCCAL_CELL_NORMAL"
    NORMAL_ADJACENT_TISSUE = "NORMAL_ADJACENT_TISSUE"
    CELL_LINES = "CELL_LINES"
    PRIMARY_XENOGRAFT_TISSUE = "PRIMARY_XENOGRAFT_TISSUE"
    XENOGRAFT_TISSUE = "XENOGRAFT_TISSUE"
    NEXT_GENERATION_CANCER_MODEL = "NEXT_GENERATION_CANCER_MODEL"
    PLEURAL_EFFUSION = "PLEURAL_EFFUSION"
    SALIVA = "SALIVA"
    GRANULOCYTES = "GRANULOCYTES"
    EBV_IMMORTALIZED_NORMAL = "EBV_IMMORTALIZED_NORMAL"
    CONTROL_ANALYTE = "CONTROL_ANALYTE"
    FFPE_SCROLLS = "FFPE_SCROLLS"
    FFPE_RECURRENT = "FFPE_RECURRENT"
    NOT_REPORTED = "NOT_REPORTED"
    UNKNOWN = "UNKNOWN"

# Set metadata after class creation
SourceMaterialTypeEnum._metadata = {
    "PRIMARY_TUMOR": {'description': 'Primary tumor tissue', 'meaning': 'NCIT:C8509', 'aliases': ['Primary Neoplasm']},
    "METASTATIC": {'description': 'Metastatic tumor tissue', 'meaning': 'NCIT:C3261', 'aliases': ['Metastatic Neoplasm']},
    "RECURRENT_TUMOR": {'description': 'Recurrent tumor tissue', 'meaning': 'NCIT:C4798', 'aliases': ['Recurrent Neoplasm']},
    "BLOOD_DERIVED_NORMAL": {'description': 'Normal cells derived from blood'},
    "BLOOD_DERIVED_CANCER_PERIPHERAL_BLOOD": {'description': 'Cancer cells from peripheral blood'},
    "BLOOD_DERIVED_CANCER_BONE_MARROW": {'description': 'Cancer cells from bone marrow'},
    "BONE_MARROW_NORMAL": {'description': 'Normal bone marrow cells'},
    "SOLID_TISSUE_NORMAL": {'description': 'Normal solid tissue'},
    "BUCCAL_CELL_NORMAL": {'description': 'Normal buccal (cheek) cells'},
    "NORMAL_ADJACENT_TISSUE": {'description': 'Normal tissue adjacent to tumor', 'meaning': 'NCIT:C164032', 'aliases': ['Tumor-Adjacent Normal Specimen']},
    "CELL_LINES": {'description': 'Established cell lines', 'meaning': 'NCIT:C16403', 'aliases': ['Cell Line']},
    "PRIMARY_XENOGRAFT_TISSUE": {'description': 'Tissue from primary xenograft'},
    "XENOGRAFT_TISSUE": {'description': 'Tissue derived from xenograft models'},
    "NEXT_GENERATION_CANCER_MODEL": {'description': 'Tissue from next-generation cancer models'},
    "PLEURAL_EFFUSION": {'description': 'Fluid from pleural effusion', 'meaning': 'NCIT:C3331', 'aliases': ['Pleural Effusion']},
    "SALIVA": {'description': 'Saliva specimen', 'meaning': 'NCIT:C13275', 'aliases': ['Saliva']},
    "GRANULOCYTES": {'description': 'Granulocyte cells', 'meaning': 'NCIT:C12530', 'aliases': ['Granulocyte']},
    "EBV_IMMORTALIZED_NORMAL": {'description': 'EBV immortalized normal cells'},
    "CONTROL_ANALYTE": {'description': 'Control analyte material'},
    "FFPE_SCROLLS": {'description': 'FFPE tissue scrolls'},
    "FFPE_RECURRENT": {'description': 'FFPE tissue from recurrent tumor'},
    "NOT_REPORTED": {'description': 'Source material type not reported'},
    "UNKNOWN": {'description': 'Unknown source material type', 'meaning': 'NCIT:C17998', 'aliases': ['Unknown']},
}

class SpecimenCreationActivityTypeEnum(RichEnum):
    """
    High-level types of activities through which specimens are generated, either by collection from source or derivation from existing specimens.
    """
    # Enum members
    COLLECTION_FROM_SOURCE = "COLLECTION_FROM_SOURCE"
    DERIVATION_FROM_SPECIMEN = "DERIVATION_FROM_SPECIMEN"

# Set metadata after class creation
SpecimenCreationActivityTypeEnum._metadata = {
    "COLLECTION_FROM_SOURCE": {'description': 'Activity that collects an initial sample directly from a subject or source', 'meaning': 'OBI:0000659', 'aliases': ['specimen collection process']},
    "DERIVATION_FROM_SPECIMEN": {'description': 'Activity that derives a new specimen from an existing one', 'meaning': 'OBI:0000094', 'aliases': ['material processing']},
}

class SpecimenProcessingActivityTypeEnum(RichEnum):
    """
    High-level types of specimen processing activities
    """
    # Enum members
    FIXATION = "FIXATION"
    FREEZING = "FREEZING"
    MOUNTING = "MOUNTING"
    PRESERVATION = "PRESERVATION"

# Set metadata after class creation
SpecimenProcessingActivityTypeEnum._metadata = {
    "FIXATION": {'description': 'Chemical preservation to maintain structural and molecular features', 'meaning': 'NCIT:C25219', 'aliases': ['Fixation']},
    "FREEZING": {'description': 'Processing activity that freezes a specimen', 'meaning': 'NCIT:C70717', 'aliases': ['Frozen Specimen']},
    "MOUNTING": {'description': 'Securing a specimen in place for examination'},
    "PRESERVATION": {'description': 'Processing activity that preserves a specimen for storage'},
}

class SpecimenQualityObservationTypeEnum(RichEnum):
    """
    Types of measurements that reflect specimen quality or suitability for use
    """
    # Enum members
    A260_A280_RATIO = "A260_A280_RATIO"
    RIBOSOMAL_RNA_28S_16S_RATIO = "RIBOSOMAL_RNA_28S_16S_RATIO"

# Set metadata after class creation
SpecimenQualityObservationTypeEnum._metadata = {
    "A260_A280_RATIO": {'description': 'Ratio of absorbance at 260nm to 280nm wavelength for nucleic acid purity'},
    "RIBOSOMAL_RNA_28S_16S_RATIO": {'description': 'Ratio of 28S to 16S ribosomal RNA for RNA integrity'},
}

class SpecimenQualityObservationMethodEnum(RichEnum):
    """
    Methods used for determining specimen quality
    """
    # Enum members
    UV_SPEC = "UV_SPEC"
    PICO_GREEN = "PICO_GREEN"

# Set metadata after class creation
SpecimenQualityObservationMethodEnum._metadata = {
    "UV_SPEC": {'description': 'UV-Vis spectrophotometry measuring absorbance across UV and visible ranges', 'meaning': 'NCIT:C116701', 'aliases': ['Spectrophotometry']},
    "PICO_GREEN": {'description': 'Fluorescent dye assay for quantifying double-stranded DNA'},
}

class SpecimenQuantityObservationTypeEnum(RichEnum):
    """
    Types of quantity measurements for specimens
    """
    # Enum members
    WEIGHT = "WEIGHT"
    VOLUME = "VOLUME"
    CONCENTRATION = "CONCENTRATION"

# Set metadata after class creation
SpecimenQuantityObservationTypeEnum._metadata = {
    "WEIGHT": {'description': 'Current weight of the specimen', 'meaning': 'NCIT:C25208', 'aliases': ['Weight']},
    "VOLUME": {'description': 'Current volume of the specimen', 'meaning': 'NCIT:C25335', 'aliases': ['Volume']},
    "CONCENTRATION": {'description': 'Concentration of extracted analyte in specimen', 'meaning': 'NCIT:C41185', 'aliases': ['Concentration']},
}

class SectionLocationEnum(RichEnum):
    """
    Location in a parent specimen from which a section was excised
    """
    # Enum members
    TOP = "TOP"
    BOTTOM = "BOTTOM"
    UNKNOWN = "UNKNOWN"

# Set metadata after class creation
SectionLocationEnum._metadata = {
    "TOP": {'description': 'The top portion of a specimen per orientation criteria'},
    "BOTTOM": {'description': 'The bottom portion of a specimen per orientation criteria'},
    "UNKNOWN": {'description': 'Unknown location on a specimen', 'meaning': 'NCIT:C17998', 'aliases': ['Unknown']},
}

__all__ = [
    "SpecimenPreparationMethodEnum",
    "TissuePreservationEnum",
    "SpecimenCollectionMethodEnum",
    "SpecimenTypeEnum",
    "AnalyteTypeEnum",
    "SourceMaterialTypeEnum",
    "SpecimenCreationActivityTypeEnum",
    "SpecimenProcessingActivityTypeEnum",
    "SpecimenQualityObservationTypeEnum",
    "SpecimenQualityObservationMethodEnum",
    "SpecimenQuantityObservationTypeEnum",
    "SectionLocationEnum",
]