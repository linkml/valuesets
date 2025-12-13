"""

Generated from: data_science/priority_severity.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class PriorityLevelEnum(RichEnum):
    """
    Standard priority levels for task/issue classification
    """
    # Enum members
    CRITICAL = "CRITICAL"
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"
    TRIVIAL = "TRIVIAL"

# Set metadata after class creation
PriorityLevelEnum._metadata = {
    "CRITICAL": {'description': 'Highest priority, requires immediate attention', 'aliases': ['P0', 'urgent', 'blocker', '1']},
    "HIGH": {'description': 'High priority, should be addressed soon', 'aliases': ['P1', 'important', '2']},
    "MEDIUM": {'description': 'Medium priority, normal workflow', 'aliases': ['P2', 'normal', '3']},
    "LOW": {'description': 'Low priority, can be deferred', 'aliases': ['P3', 'minor', '4']},
    "TRIVIAL": {'description': 'Lowest priority, nice to have', 'aliases': ['P4', 'cosmetic', '5']},
}

class SeverityLevelEnum(RichEnum):
    """
    Severity levels for incident/bug classification
    """
    # Enum members
    CRITICAL = "CRITICAL"
    MAJOR = "MAJOR"
    MINOR = "MINOR"
    TRIVIAL = "TRIVIAL"

# Set metadata after class creation
SeverityLevelEnum._metadata = {
    "CRITICAL": {'description': 'System is unusable, data loss possible', 'aliases': ['S1', 'blocker', 'showstopper']},
    "MAJOR": {'description': 'Major functionality impaired', 'aliases': ['S2', 'severe', 'high']},
    "MINOR": {'description': 'Minor functionality impaired', 'aliases': ['S3', 'moderate', 'medium']},
    "TRIVIAL": {'description': 'Cosmetic issue, minimal impact', 'aliases': ['S4', 'cosmetic', 'low']},
}

class ConfidenceLevelEnum(RichEnum):
    """
    Confidence levels for predictions and classifications
    """
    # Enum members
    VERY_HIGH = "VERY_HIGH"
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"
    VERY_LOW = "VERY_LOW"

# Set metadata after class creation
ConfidenceLevelEnum._metadata = {
    "VERY_HIGH": {'description': 'Very high confidence (>95%)', 'aliases': ['certain', '5']},
    "HIGH": {'description': 'High confidence (80-95%)', 'aliases': ['confident', '4']},
    "MEDIUM": {'description': 'Medium confidence (60-80%)', 'aliases': ['moderate', '3']},
    "LOW": {'description': 'Low confidence (40-60%)', 'aliases': ['uncertain', '2']},
    "VERY_LOW": {'description': 'Very low confidence (<40%)', 'aliases': ['guess', '1']},
}

__all__ = [
    "PriorityLevelEnum",
    "SeverityLevelEnum",
    "ConfidenceLevelEnum",
]