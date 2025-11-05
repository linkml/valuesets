"""

Generated from: energy/fossil_fuels.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class FossilFuelTypeEnum(RichEnum):
    """
    Types of fossil fuels used for energy generation
    """
    # Enum members
    COAL = "COAL"
    NATURAL_GAS = "NATURAL_GAS"
    PETROLEUM = "PETROLEUM"

# Set metadata after class creation
FossilFuelTypeEnum._metadata = {
    "COAL": {'description': 'Coal', 'meaning': 'ENVO:02000091'},
    "NATURAL_GAS": {'description': 'Natural gas', 'meaning': 'ENVO:01000552'},
    "PETROLEUM": {'description': 'Petroleum', 'meaning': 'ENVO:00002984'},
}

__all__ = [
    "FossilFuelTypeEnum",
]