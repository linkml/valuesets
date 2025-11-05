"""

Generated from: bio/biosafety.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class BiosafetyLevelEnum(RichEnum):
    """
    Biosafety levels (BSL) defining containment requirements for biological agents
    """
    # Enum members
    BSL1 = "BSL1"
    BSL2 = "BSL2"
    BSL3 = "BSL3"
    BSL4 = "BSL4"

# Set metadata after class creation
BiosafetyLevelEnum._metadata = {
    "BSL1": {'description': 'Suitable for well-characterized agents not known to consistently cause disease in healthy adults', 'meaning': 'SNOMED:409600007'},
    "BSL2": {'description': 'Suitable for agents that pose moderate hazards to personnel and the environment', 'meaning': 'SNOMED:409603009'},
    "BSL3": {'description': 'Suitable for indigenous or exotic agents that may cause serious or potentially lethal disease through inhalation', 'meaning': 'SNOMED:409604003'},
    "BSL4": {'description': 'Suitable for dangerous and exotic agents that pose high risk of life-threatening disease', 'meaning': 'SNOMED:409605002'},
}

__all__ = [
    "BiosafetyLevelEnum",
]