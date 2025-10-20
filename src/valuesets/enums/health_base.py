"""
valuesets-health

General health-related value sets

Generated from: health.yaml
"""

from __future__ import annotations

from typing import Dict, Any, Optional
from valuesets.generators.rich_enum import RichEnum

class VitalStatusEnum(RichEnum):
    """
    The vital status of a person or organism
    """
    # Enum members
    ALIVE = "ALIVE"
    DECEASED = "DECEASED"
    UNKNOWN = "UNKNOWN"
    PRESUMED_ALIVE = "PRESUMED_ALIVE"
    PRESUMED_DECEASED = "PRESUMED_DECEASED"

# Set metadata after class creation
VitalStatusEnum._metadata = {
    "ALIVE": {'description': 'The person is living', 'meaning': 'NCIT:C37987'},
    "DECEASED": {'description': 'The person has died', 'meaning': 'NCIT:C28554'},
    "UNKNOWN": {'description': 'The vital status is not known', 'meaning': 'NCIT:C17998'},
    "PRESUMED_ALIVE": {'description': 'The person is presumed to be alive based on available information'},
    "PRESUMED_DECEASED": {'description': 'The person is presumed to be deceased based on available information'},
}

__all__ = [
    "VitalStatusEnum",
]