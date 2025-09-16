"""

Generated from: social/person_status.yaml
"""

from __future__ import annotations

from typing import Dict, Any, Optional
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

class MaritalStatusEnum(RichEnum):
    """
    Marital or civil status of a person
    """
    # Enum members
    SINGLE = "SINGLE"
    MARRIED = "MARRIED"
    DIVORCED = "DIVORCED"
    WIDOWED = "WIDOWED"
    SEPARATED = "SEPARATED"
    DOMESTIC_PARTNERSHIP = "DOMESTIC_PARTNERSHIP"
    CIVIL_UNION = "CIVIL_UNION"
    UNKNOWN = "UNKNOWN"
    PREFER_NOT_TO_SAY = "PREFER_NOT_TO_SAY"

# Set metadata after class creation
MaritalStatusEnum._metadata = {
    "SINGLE": {'description': 'Never married', 'meaning': 'NCIT:C51774'},
    "MARRIED": {'description': 'Currently married or in civil partnership', 'meaning': 'NCIT:C51773'},
    "DIVORCED": {'description': 'Marriage legally dissolved', 'meaning': 'NCIT:C51776'},
    "WIDOWED": {'description': 'Marriage ended due to death of spouse', 'meaning': 'NCIT:C51775'},
    "SEPARATED": {'description': 'Living apart from spouse', 'meaning': 'NCIT:C51777'},
    "DOMESTIC_PARTNERSHIP": {'description': 'In a domestic partnership', 'meaning': 'NCIT:C53262'},
    "CIVIL_UNION": {'description': 'In a civil union', 'meaning': 'NCIT:C25188'},
    "UNKNOWN": {'description': 'Marital status not known', 'meaning': 'NCIT:C17998'},
    "PREFER_NOT_TO_SAY": {'description': 'Prefers not to disclose marital status', 'meaning': 'NCIT:C150742'},
}

class EmploymentStatusEnum(RichEnum):
    """
    Employment status of a person
    """
    # Enum members
    EMPLOYED_FULL_TIME = "EMPLOYED_FULL_TIME"
    EMPLOYED_PART_TIME = "EMPLOYED_PART_TIME"
    SELF_EMPLOYED = "SELF_EMPLOYED"
    UNEMPLOYED = "UNEMPLOYED"
    STUDENT = "STUDENT"
    RETIRED = "RETIRED"
    HOMEMAKER = "HOMEMAKER"
    DISABLED = "DISABLED"
    OTHER = "OTHER"
    UNKNOWN = "UNKNOWN"

# Set metadata after class creation
EmploymentStatusEnum._metadata = {
    "EMPLOYED_FULL_TIME": {'description': 'Employed full-time', 'meaning': 'NCIT:C52658'},
    "EMPLOYED_PART_TIME": {'description': 'Employed part-time', 'meaning': 'NCIT:C75562'},
    "SELF_EMPLOYED": {'description': 'Self-employed', 'meaning': 'NCIT:C116000'},
    "UNEMPLOYED": {'description': 'Unemployed', 'meaning': 'NCIT:C75563'},
    "STUDENT": {'description': 'Student', 'meaning': 'NCIT:C75561'},
    "RETIRED": {'description': 'Retired', 'meaning': 'NCIT:C148257'},
    "HOMEMAKER": {'description': 'Homemaker', 'meaning': 'NCIT:C75560'},
    "DISABLED": {'description': 'Unable to work due to disability', 'meaning': 'NCIT:C63367'},
    "OTHER": {'description': 'Other employment status', 'meaning': 'NCIT:C25172'},
    "UNKNOWN": {'description': 'Employment status not known', 'meaning': 'NCIT:C17998'},
}

__all__ = [
    "PersonStatusEnum",
    "MaritalStatusEnum",
    "EmploymentStatusEnum",
]