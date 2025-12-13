"""

Generated from: bio/insdc_missing_values.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class InsdcMissingValueEnum(RichEnum):
    """
    INSDC (International Nucleotide Sequence Database Collaboration) controlled vocabulary for missing values in sequence records
    """
    # Enum members
    NOT_APPLICABLE = "NOT_APPLICABLE"
    MISSING = "MISSING"
    NOT_COLLECTED = "NOT_COLLECTED"
    NOT_PROVIDED = "NOT_PROVIDED"
    RESTRICTED_ACCESS = "RESTRICTED_ACCESS"
    MISSING_CONTROL_SAMPLE = "MISSING_CONTROL_SAMPLE"
    MISSING_SAMPLE_GROUP = "MISSING_SAMPLE_GROUP"
    MISSING_SYNTHETIC_CONSTRUCT = "MISSING_SYNTHETIC_CONSTRUCT"
    MISSING_LAB_STOCK = "MISSING_LAB_STOCK"
    MISSING_THIRD_PARTY_DATA = "MISSING_THIRD_PARTY_DATA"
    MISSING_DATA_AGREEMENT_ESTABLISHED_PRE_2023 = "MISSING_DATA_AGREEMENT_ESTABLISHED_PRE_2023"
    MISSING_ENDANGERED_SPECIES = "MISSING_ENDANGERED_SPECIES"
    MISSING_HUMAN_IDENTIFIABLE = "MISSING_HUMAN_IDENTIFIABLE"

# Set metadata after class creation
InsdcMissingValueEnum._metadata = {
    "NOT_APPLICABLE": {'description': 'Information is inappropriate to report, can indicate that the standard itself fails to model or represent the information appropriately', 'meaning': 'NCIT:C48660'},
    "MISSING": {'description': 'Not stated explicitly or implied by any other means', 'meaning': 'NCIT:C54031'},
    "NOT_COLLECTED": {'description': 'Information of an expected format was not given because it has never been collected', 'meaning': 'NCIT:C142610', 'annotations': {'note': 'NCIT:C142610 represents Missing Data which encompasses data not collected'}},
    "NOT_PROVIDED": {'description': 'Information of an expected format was not given, a value may be given at the later stage', 'meaning': 'NCIT:C126101', 'annotations': {'note': 'Using NCIT:C126101 (Not Available) as a general term for data not provided'}},
    "RESTRICTED_ACCESS": {'description': 'Information exists but cannot be released openly because of privacy concerns', 'meaning': 'NCIT:C67110', 'annotations': {'note': 'NCIT:C67110 represents Data Not Releasable due to confidentiality'}},
    "MISSING_CONTROL_SAMPLE": {'description': 'Information is not applicable to control samples, negative control samples (e.g. blank sample or clear sample)', 'annotations': {'note': 'No specific ontology term found for missing control sample data'}},
    "MISSING_SAMPLE_GROUP": {'description': 'Information can not be provided for a sample group where a selection of samples is used to represent a species, location or some other attribute/metric', 'annotations': {'note': 'No specific ontology term found for missing sample group data'}},
    "MISSING_SYNTHETIC_CONSTRUCT": {'description': 'Information does not exist for a synthetic construct', 'annotations': {'note': 'No specific ontology term found for missing synthetic construct data'}},
    "MISSING_LAB_STOCK": {'description': 'Information is not collected for a lab stock and its cultivation, e.g. stock centers, culture collections, seed banks', 'annotations': {'note': 'No specific ontology term found for missing lab stock data'}},
    "MISSING_THIRD_PARTY_DATA": {'description': 'Information has not been revealed by another party', 'meaning': 'NCIT:C67329', 'annotations': {'note': 'NCIT:C67329 represents Source Data Not Available'}},
    "MISSING_DATA_AGREEMENT_ESTABLISHED_PRE_2023": {'description': 'Information can not be reported due to a data agreement established before metadata standards were introduced in 2023', 'annotations': {'note': 'No specific ontology term for data missing due to pre-2023 agreements'}},
    "MISSING_ENDANGERED_SPECIES": {'description': 'Information can not be reported due to endangered species concerns', 'annotations': {'note': 'No specific ontology term for data withheld due to endangered species'}},
    "MISSING_HUMAN_IDENTIFIABLE": {'description': 'Information can not be reported due to identifiable human data concerns', 'annotations': {'note': 'No specific ontology term for data withheld due to human identifiability'}},
}

__all__ = [
    "InsdcMissingValueEnum",
]