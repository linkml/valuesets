"""

Generated from: data_science/binary_classification.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class BinaryClassificationEnum(RichEnum):
    """
    Generic binary classification labels
    """
    # Enum members
    POSITIVE = "POSITIVE"
    NEGATIVE = "NEGATIVE"

# Set metadata after class creation
BinaryClassificationEnum._metadata = {
    "POSITIVE": {'description': 'Positive class', 'meaning': 'NCIT:C38758', 'aliases': ['1', 'true', 'yes', 'T']},
    "NEGATIVE": {'description': 'Negative class', 'meaning': 'NCIT:C35681', 'aliases': ['0', 'false', 'no', 'F']},
}

class SpamClassificationEnum(RichEnum):
    """
    Standard labels for spam/ham email classification
    """
    # Enum members
    SPAM = "SPAM"
    HAM = "HAM"

# Set metadata after class creation
SpamClassificationEnum._metadata = {
    "SPAM": {'description': 'Unwanted or unsolicited message', 'annotations': {'note': 'No appropriate ontology term found for spam concept'}, 'aliases': ['junk', '1']},
    "HAM": {'description': 'Legitimate, wanted message', 'annotations': {'note': 'No appropriate ontology term found for ham concept'}, 'aliases': ['not_spam', 'legitimate', '0']},
}

class AnomalyDetectionEnum(RichEnum):
    """
    Labels for anomaly detection tasks
    """
    # Enum members
    NORMAL = "NORMAL"
    ANOMALY = "ANOMALY"

# Set metadata after class creation
AnomalyDetectionEnum._metadata = {
    "NORMAL": {'description': 'Normal, expected behavior or pattern', 'meaning': 'NCIT:C14165', 'aliases': ['inlier', 'regular', '0']},
    "ANOMALY": {'description': 'Abnormal, unexpected behavior or pattern', 'meaning': 'STATO:0000036', 'aliases': ['outlier', 'abnormal', 'irregular', '1']},
}

class ChurnClassificationEnum(RichEnum):
    """
    Customer churn prediction labels
    """
    # Enum members
    RETAINED = "RETAINED"
    CHURNED = "CHURNED"

# Set metadata after class creation
ChurnClassificationEnum._metadata = {
    "RETAINED": {'description': 'Customer continues using the service', 'annotations': {'note': 'No appropriate ontology term found for customer retention'}, 'aliases': ['active', 'staying', '0']},
    "CHURNED": {'description': 'Customer stopped using the service', 'annotations': {'note': 'No appropriate ontology term found for customer churn'}, 'aliases': ['lost', 'inactive', 'attrited', '1']},
}

class FraudDetectionEnum(RichEnum):
    """
    Fraud detection classification labels
    """
    # Enum members
    LEGITIMATE = "LEGITIMATE"
    FRAUDULENT = "FRAUDULENT"

# Set metadata after class creation
FraudDetectionEnum._metadata = {
    "LEGITIMATE": {'description': 'Legitimate, non-fraudulent transaction or activity', 'meaning': 'NCIT:C14165', 'aliases': ['genuine', 'valid', '0']},
    "FRAUDULENT": {'description': 'Fraudulent transaction or activity', 'meaning': 'NCIT:C121839', 'aliases': ['fraud', 'invalid', '1']},
}

__all__ = [
    "BinaryClassificationEnum",
    "SpamClassificationEnum",
    "AnomalyDetectionEnum",
    "ChurnClassificationEnum",
    "FraudDetectionEnum",
]