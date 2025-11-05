"""
Contributor Value Sets

Value sets related to contributors and their roles

Generated from: contributor.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class ContributorType(RichEnum):
    """
    The type of contributor being represented.
    """
    # Enum members
    PERSON = "PERSON"
    ORGANIZATION = "ORGANIZATION"

# Set metadata after class creation
ContributorType._metadata = {
    "PERSON": {'description': 'A person.', 'meaning': 'NCIT:C25190'},
    "ORGANIZATION": {'description': 'An organization.', 'meaning': 'NCIT:C41206', 'aliases': ['Institution']},
}

__all__ = [
    "ContributorType",
]