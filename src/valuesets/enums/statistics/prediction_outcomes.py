"""

Generated from: statistics/prediction_outcomes.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class OutcomeTypeEnum(RichEnum):
    """
    Types of prediction outcomes for classification tasks
    """
    # Enum members
    TP = "TP"
    FP = "FP"
    TN = "TN"
    FN = "FN"

# Set metadata after class creation
OutcomeTypeEnum._metadata = {
    "TP": {'description': 'True Positive'},
    "FP": {'description': 'False Positive'},
    "TN": {'description': 'True Negative'},
    "FN": {'description': 'False Negative'},
}

__all__ = [
    "OutcomeTypeEnum",
]