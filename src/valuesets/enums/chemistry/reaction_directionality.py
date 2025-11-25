"""
Reaction Directionality

Directionality of chemical reactions and processes

Generated from: chemistry/reaction_directionality.yaml
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

class ReactionDirectionality(RichEnum):
    """
    The directionality of a chemical reaction or process
    """
    # Enum members
    LEFT_TO_RIGHT = "LEFT_TO_RIGHT"
    RIGHT_TO_LEFT = "RIGHT_TO_LEFT"
    BIDIRECTIONAL = "BIDIRECTIONAL"
    AGNOSTIC = "AGNOSTIC"
    IRREVERSIBLE_LEFT_TO_RIGHT = "IRREVERSIBLE_LEFT_TO_RIGHT"
    IRREVERSIBLE_RIGHT_TO_LEFT = "IRREVERSIBLE_RIGHT_TO_LEFT"

# Set metadata after class creation
ReactionDirectionality._metadata = {
    "LEFT_TO_RIGHT": {'description': 'Reaction proceeds from left to right (forward direction)', 'aliases': ['LR', 'forward', '-->']},
    "RIGHT_TO_LEFT": {'description': 'Reaction proceeds from right to left (reverse direction)', 'aliases': ['RL', 'reverse', 'backward', '<--']},
    "BIDIRECTIONAL": {'description': 'Reaction can proceed in both directions', 'aliases': ['BIDI', 'reversible', '<-->']},
    "AGNOSTIC": {'description': 'Direction is unknown or not specified', 'aliases': ['unknown', 'unspecified']},
    "IRREVERSIBLE_LEFT_TO_RIGHT": {'description': 'Reaction proceeds only from left to right and cannot be reversed', 'aliases': ['irreversible forward', '->>']},
    "IRREVERSIBLE_RIGHT_TO_LEFT": {'description': 'Reaction proceeds only from right to left and cannot be reversed', 'aliases': ['irreversible reverse', '<<-']},
}

__all__ = [
    "RelativeTimeEnum",
    "PresenceEnum",
    "ReactionDirectionality",
]