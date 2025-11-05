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

__all__ = [
    "CaseOrControlEnum",
]