"""
Confidence Level Value Sets

Value sets for expressing levels of confidence, certainty, and evidence strength in various contexts including research, clinical, and data quality assessments.

Generated from: confidence_levels.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class RelativeTimeEnum(RichEnum):
    """
    Temporal relationships between events or time points
    """
    # Enum members
    BEFORE = "BEFORE"
    AFTER = "AFTER"
    AT_SAME_TIME_AS = "AT_SAME_TIME_AS"

# Set metadata after class creation
RelativeTimeEnum._metadata = {
    "BEFORE": {'description': 'Occurs before the reference time point'},
    "AFTER": {'description': 'Occurs after the reference time point'},
    "AT_SAME_TIME_AS": {'description': 'Occurs at the same time as the reference time point'},
}

class PresenceEnum(RichEnum):
    """
    Classification of whether an entity is present, absent, or at detection limits
    """
    # Enum members
    PRESENT = "PRESENT"
    ABSENT = "ABSENT"
    BELOW_DETECTION_LIMIT = "BELOW_DETECTION_LIMIT"
    ABOVE_DETECTION_LIMIT = "ABOVE_DETECTION_LIMIT"

# Set metadata after class creation
PresenceEnum._metadata = {
    "PRESENT": {'description': 'The entity is present'},
    "ABSENT": {'description': 'The entity is absent'},
    "BELOW_DETECTION_LIMIT": {'description': 'The entity is below the detection limit'},
    "ABOVE_DETECTION_LIMIT": {'description': 'The entity is above the detection limit'},
}

class ConfidenceLevel(RichEnum):
    """
    Standard confidence levels based on NCIT (NCI Thesaurus) definitions. Used to express the degree of confidence in evidence, data, or assertions.
    """
    # Enum members
    HIGH_CONFIDENCE = "HIGH_CONFIDENCE"
    MODERATE_CONFIDENCE = "MODERATE_CONFIDENCE"
    LOW_CONFIDENCE = "LOW_CONFIDENCE"
    VERY_LOW_OR_NO_CONFIDENCE = "VERY_LOW_OR_NO_CONFIDENCE"

# Set metadata after class creation
ConfidenceLevel._metadata = {
    "HIGH_CONFIDENCE": {'description': 'A response indicating a high level of confidence.', 'meaning': 'NCIT:C129479'},
    "MODERATE_CONFIDENCE": {'description': 'A response indicating a moderate level of confidence.', 'meaning': 'NCIT:C129480'},
    "LOW_CONFIDENCE": {'description': 'A response indicating a low level of confidence.', 'meaning': 'NCIT:C129481'},
    "VERY_LOW_OR_NO_CONFIDENCE": {'description': 'A response indicating a very low level of confidence or an absence.', 'meaning': 'NCIT:C129482', 'aliases': ['Very Low Confidence or No Confidence']},
}

class CIOConfidenceLevel(RichEnum):
    """
    Confidence levels from the Confidence Information Ontology (CIO), representing different levels of trust in evidence.
    """
    # Enum members
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"

# Set metadata after class creation
CIOConfidenceLevel._metadata = {
    "HIGH": {'description': 'A confidence level representing a high trust in an evidence.', 'meaning': 'CIO:0000029', 'aliases': ['high confidence level']},
    "MEDIUM": {'description': 'A confidence level representing a moderate trust in an evidence.', 'meaning': 'CIO:0000030', 'aliases': ['medium confidence level']},
    "LOW": {'description': 'A confidence level representing an absence of trust in an evidence.', 'meaning': 'CIO:0000031', 'aliases': ['low confidence level']},
}

class OBCSCertaintyLevel(RichEnum):
    """
    Certainty levels from the Ontology of Biological and Clinical Statistics (OBCS). These terms are used to express degrees of certainty in statistical and clinical contexts.
    """
    # Enum members
    DEFINITIVE = "DEFINITIVE"
    HIGH = "HIGH"
    INTERMEDIATE = "INTERMEDIATE"

# Set metadata after class creation
OBCSCertaintyLevel._metadata = {
    "DEFINITIVE": {'description': 'Definitive certainty level - the highest degree of certainty.', 'meaning': 'OBCS:0000368', 'aliases': ['definitive certainty level']},
    "HIGH": {'description': 'High certainty level - strong confidence but not absolute.', 'meaning': 'OBCS:0000369', 'aliases': ['high certainty level']},
    "INTERMEDIATE": {'description': 'Intermediate certainty level - moderate degree of certainty.', 'meaning': 'OBCS:0000370', 'aliases': ['intermediate certainty level']},
}

class IPCCLikelihoodScale(RichEnum):
    """
    IPCC (Intergovernmental Panel on Climate Change) standardized likelihood scale used to communicate the assessed probability of an outcome or result. Widely used in climate science and environmental assessments.
    """
    # Enum members
    VIRTUALLY_CERTAIN = "VIRTUALLY_CERTAIN"
    EXTREMELY_LIKELY = "EXTREMELY_LIKELY"
    VERY_LIKELY = "VERY_LIKELY"
    LIKELY = "LIKELY"
    MORE_LIKELY_THAN_NOT = "MORE_LIKELY_THAN_NOT"
    ABOUT_AS_LIKELY_AS_NOT = "ABOUT_AS_LIKELY_AS_NOT"
    UNLIKELY = "UNLIKELY"
    VERY_UNLIKELY = "VERY_UNLIKELY"
    EXTREMELY_UNLIKELY = "EXTREMELY_UNLIKELY"
    EXCEPTIONALLY_UNLIKELY = "EXCEPTIONALLY_UNLIKELY"

# Set metadata after class creation
IPCCLikelihoodScale._metadata = {
    "VIRTUALLY_CERTAIN": {'description': '99-100% probability of occurrence/truth.', 'annotations': {'probability_range': '0.99-1.00'}},
    "EXTREMELY_LIKELY": {'description': '95-100% probability of occurrence/truth.', 'annotations': {'probability_range': '0.95-1.00'}},
    "VERY_LIKELY": {'description': '90-100% probability of occurrence/truth.', 'annotations': {'probability_range': '0.90-1.00'}},
    "LIKELY": {'description': '66-100% probability of occurrence/truth.', 'annotations': {'probability_range': '0.66-1.00'}},
    "MORE_LIKELY_THAN_NOT": {'description': 'Greater than 50% to 100% probability of occurrence/truth.', 'annotations': {'probability_range': '0.50-1.00'}},
    "ABOUT_AS_LIKELY_AS_NOT": {'description': '33-66% probability of occurrence/truth.', 'annotations': {'probability_range': '0.33-0.66'}},
    "UNLIKELY": {'description': '0-33% probability of occurrence/truth.', 'annotations': {'probability_range': '0.00-0.33'}},
    "VERY_UNLIKELY": {'description': '0-10% probability of occurrence/truth.', 'annotations': {'probability_range': '0.00-0.10'}},
    "EXTREMELY_UNLIKELY": {'description': '0-5% probability of occurrence/truth.', 'annotations': {'probability_range': '0.00-0.05'}},
    "EXCEPTIONALLY_UNLIKELY": {'description': '0-1% probability of occurrence/truth.', 'annotations': {'probability_range': '0.00-0.01'}},
}

class IPCCConfidenceLevel(RichEnum):
    """
    IPCC confidence qualifiers used to express the degree of confidence in a finding based on the type, amount, quality, and consistency of evidence and the degree of agreement.
    """
    # Enum members
    VERY_HIGH_CONFIDENCE = "VERY_HIGH_CONFIDENCE"
    HIGH_CONFIDENCE = "HIGH_CONFIDENCE"
    MEDIUM_CONFIDENCE = "MEDIUM_CONFIDENCE"
    LOW_CONFIDENCE = "LOW_CONFIDENCE"
    VERY_LOW_CONFIDENCE = "VERY_LOW_CONFIDENCE"

# Set metadata after class creation
IPCCConfidenceLevel._metadata = {
    "VERY_HIGH_CONFIDENCE": {'description': 'Very high confidence in the validity of a finding.'},
    "HIGH_CONFIDENCE": {'description': 'High confidence in the validity of a finding.'},
    "MEDIUM_CONFIDENCE": {'description': 'Medium confidence in the validity of a finding.'},
    "LOW_CONFIDENCE": {'description': 'Low confidence in the validity of a finding.'},
    "VERY_LOW_CONFIDENCE": {'description': 'Very low confidence in the validity of a finding.'},
}

class NCITFivePointConfidenceScale(RichEnum):
    """
    NCIT 5-point subjective confidence scale ranging from "Not at all confident" (1) to "Very confident" (5). Used in clinical assessments and questionnaires.
    """
    # Enum members
    NOT_AT_ALL_CONFIDENT = "NOT_AT_ALL_CONFIDENT"
    SLIGHTLY_CONFIDENT = "SLIGHTLY_CONFIDENT"
    SOMEWHAT_CONFIDENT = "SOMEWHAT_CONFIDENT"
    MODERATELY_CONFIDENT = "MODERATELY_CONFIDENT"
    VERY_CONFIDENT = "VERY_CONFIDENT"

# Set metadata after class creation
NCITFivePointConfidenceScale._metadata = {
    "NOT_AT_ALL_CONFIDENT": {'description': 'A subjective score of 1 - Not at all confident.', 'meaning': 'NCIT:C153491', 'aliases': ['Confidence 1']},
    "SLIGHTLY_CONFIDENT": {'description': 'A subjective score of 2 - Slightly confident.', 'meaning': 'NCIT:C153492', 'aliases': ['Confidence 2']},
    "SOMEWHAT_CONFIDENT": {'description': 'A subjective score of 3 - Somewhat confident.', 'meaning': 'NCIT:C153493', 'aliases': ['Confidence 3']},
    "MODERATELY_CONFIDENT": {'description': 'A subjective score of 4 - Moderately confident.', 'meaning': 'NCIT:C153494', 'aliases': ['Confidence 4']},
    "VERY_CONFIDENT": {'description': 'A subjective score of 5 - Very confident.', 'meaning': 'NCIT:C153495', 'aliases': ['Confidence 5']},
}

__all__ = [
    "RelativeTimeEnum",
    "PresenceEnum",
    "ConfidenceLevel",
    "CIOConfidenceLevel",
    "OBCSCertaintyLevel",
    "IPCCLikelihoodScale",
    "IPCCConfidenceLevel",
    "NCITFivePointConfidenceScale",
]