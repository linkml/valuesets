"""

Generated from: social/person_status.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class PersonStatusEnum(RichEnum):
    """
    Vital status of a person (living or deceased)
    """
    # Enum members
    ALIVE = "ALIVE"
    DEAD = "DEAD"
    UNKNOWN = "UNKNOWN"

# Set metadata after class creation
PersonStatusEnum._metadata = {
    "ALIVE": {'description': 'The person is living', 'meaning': 'PATO:0001421'},
    "DEAD": {'description': 'The person is deceased', 'meaning': 'PATO:0001422'},
    "UNKNOWN": {'description': 'The vital status is not known', 'meaning': 'NCIT:C17998'},
}

__all__ = [
    "PersonStatusEnum",
]