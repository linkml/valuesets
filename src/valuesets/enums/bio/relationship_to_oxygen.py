"""

Generated from: bio/relationship_to_oxygen.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class RelToOxygenEnum(RichEnum):
    """
    Organism's relationship to oxygen for growth and survival
    """
    # Enum members
    AEROBE = "AEROBE"
    ANAEROBE = "ANAEROBE"
    FACULTATIVE = "FACULTATIVE"
    MICROAEROPHILIC = "MICROAEROPHILIC"
    MICROANAEROBE = "MICROANAEROBE"
    OBLIGATE_AEROBE = "OBLIGATE_AEROBE"
    OBLIGATE_ANAEROBE = "OBLIGATE_ANAEROBE"

# Set metadata after class creation
RelToOxygenEnum._metadata = {
    "AEROBE": {'description': 'Organism that can survive and grow in an oxygenated environment', 'meaning': 'ECOCORE:00000173'},
    "ANAEROBE": {'description': 'Organism that does not require oxygen for growth', 'meaning': 'ECOCORE:00000172'},
    "FACULTATIVE": {'description': 'Organism that can grow with or without oxygen', 'meaning': 'ECOCORE:00000177', 'annotations': {'note': 'Maps to facultative anaerobe in ECOCORE'}},
    "MICROAEROPHILIC": {'description': 'Organism that requires oxygen at lower concentrations than atmospheric', 'meaning': 'MICRO:0000515'},
    "MICROANAEROBE": {'description': 'Organism that can tolerate very small amounts of oxygen'},
    "OBLIGATE_AEROBE": {'description': 'Organism that requires oxygen to grow', 'meaning': 'ECOCORE:00000179'},
    "OBLIGATE_ANAEROBE": {'description': 'Organism that cannot grow in the presence of oxygen', 'meaning': 'ECOCORE:00000178'},
}

__all__ = [
    "RelToOxygenEnum",
]