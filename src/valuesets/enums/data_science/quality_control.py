"""

Generated from: data_science/quality_control.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class QualityControlEnum(RichEnum):
    """
    Quality control classification labels
    """
    # Enum members
    PASS = "PASS"
    FAIL = "FAIL"

# Set metadata after class creation
QualityControlEnum._metadata = {
    "PASS": {'description': 'Item meets quality standards', 'meaning': 'NCIT:C81275', 'aliases': ['passed', 'acceptable', 'ok', '1']},
    "FAIL": {'description': 'Item does not meet quality standards', 'meaning': 'NCIT:C44281', 'aliases': ['failed', 'reject', 'defective', '0']},
}

class DefectClassificationEnum(RichEnum):
    """
    Manufacturing defect classification
    """
    # Enum members
    NO_DEFECT = "NO_DEFECT"
    MINOR_DEFECT = "MINOR_DEFECT"
    MAJOR_DEFECT = "MAJOR_DEFECT"
    CRITICAL_DEFECT = "CRITICAL_DEFECT"

# Set metadata after class creation
DefectClassificationEnum._metadata = {
    "NO_DEFECT": {'description': 'No defect detected', 'meaning': 'NCIT:C14165', 'aliases': ['good', 'normal', '0']},
    "MINOR_DEFECT": {'description': "Minor defect that doesn't affect functionality", 'aliases': ['minor', 'cosmetic', '1']},
    "MAJOR_DEFECT": {'description': 'Major defect affecting functionality', 'aliases': ['major', 'functional', '2']},
    "CRITICAL_DEFECT": {'description': 'Critical defect rendering item unusable or unsafe', 'aliases': ['critical', 'severe', '3']},
}

__all__ = [
    "QualityControlEnum",
    "DefectClassificationEnum",
]