"""
valuesets-statistics

Common Data Model Elements: Human and statistics activities

Generated from: statistics.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class PredictionOutcomeType(RichEnum):
    # Enum members
    TP = "TP"
    FP = "FP"
    TN = "TN"
    FN = "FN"

# Set metadata after class creation
PredictionOutcomeType._metadata = {
    "TP": {'description': 'True Positive'},
    "FP": {'description': 'False Positive'},
    "TN": {'description': 'True Negative'},
    "FN": {'description': 'False Negative'},
}

__all__ = [
    "PredictionOutcomeType",
]