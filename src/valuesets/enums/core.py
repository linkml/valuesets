"""
comet-core

Common Observational Model: Core

Generated from: core.yaml
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

__all__ = [
    "RelativeTimeEnum",
    "PresenceEnum",
]