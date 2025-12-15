"""
valuesets-investigation

Common Data Model Elements: Human and investigation activities

Generated from: investigation.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class CaseOrControlEnum(RichEnum):
    # Enum members
    CASE = "CASE"
    CONTROL = "CONTROL"

# Set metadata after class creation
CaseOrControlEnum._metadata = {
    "CASE": {'meaning': 'OBI:0002492'},
    "CONTROL": {'meaning': 'OBI:0002493'},
}

class PlannedProcessCompletionStatus(RichEnum):
    """
    The completion status of a planned process, indicating whether the process was successfully executed or failed. Based on COB (Core Ontology for Biology) planned process hierarchy.
    """
    # Enum members
    COMPLETELY_EXECUTED = "COMPLETELY_EXECUTED"
    FAILED = "FAILED"

# Set metadata after class creation
PlannedProcessCompletionStatus._metadata = {
    "COMPLETELY_EXECUTED": {'description': 'A planned process that was successfully completed as intended', 'meaning': 'COB:0000035'},
    "FAILED": {'description': 'A planned process that did not complete successfully', 'meaning': 'COB:0000083'},
}

__all__ = [
    "CaseOrControlEnum",
    "PlannedProcessCompletionStatus",
]