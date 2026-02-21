"""
Construction and Buildings Value Sets

Value sets for building systems and construction relevant to the DOE Reimagining Construction challenge

Generated from: industry/construction.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class BuildingSystemType(RichEnum):
    """
    Types of building systems for mechanical, electrical, and structural infrastructure
    """
    # Enum members
    HVAC = "HVAC"
    ELECTRICAL = "ELECTRICAL"
    PLUMBING = "PLUMBING"
    STRUCTURAL = "STRUCTURAL"
    BUILDING_ENVELOPE = "BUILDING_ENVELOPE"
    FIRE_PROTECTION = "FIRE_PROTECTION"
    LIGHTING = "LIGHTING"
    BUILDING_AUTOMATION = "BUILDING_AUTOMATION"
    RENEWABLE_ENERGY_INTEGRATION = "RENEWABLE_ENERGY_INTEGRATION"

# Set metadata after class creation
BuildingSystemType._metadata = {
    "HVAC": {'description': 'Heating, ventilation, and air conditioning systems for climate control'},
    "ELECTRICAL": {'description': 'Electrical power distribution and wiring systems within the building'},
    "PLUMBING": {'description': 'Water supply, drainage, and sewage systems'},
    "STRUCTURAL": {'description': 'Load-bearing structural framework including foundations, columns, beams, and slabs'},
    "BUILDING_ENVELOPE": {'description': 'Exterior enclosure system including walls, roof, windows, and insulation', 'meaning': 'ENVO:01000470'},
    "FIRE_PROTECTION": {'description': 'Fire detection, suppression, and alarm systems'},
    "LIGHTING": {'description': 'Interior and exterior lighting systems including controls and fixtures'},
    "BUILDING_AUTOMATION": {'description': 'Integrated control systems for monitoring and managing building operations'},
    "RENEWABLE_ENERGY_INTEGRATION": {'description': 'On-site renewable energy generation systems such as solar panels and wind turbines'},
}

class BuildingEnergyPerformanceLevel(RichEnum):
    """
    Energy performance certification levels and standards for buildings
    """
    # Enum members
    NET_ZERO_ENERGY = "NET_ZERO_ENERGY"
    NET_POSITIVE_ENERGY = "NET_POSITIVE_ENERGY"
    PASSIVE_HOUSE = "PASSIVE_HOUSE"
    LEED_CERTIFIED = "LEED_CERTIFIED"
    LEED_SILVER = "LEED_SILVER"
    LEED_GOLD = "LEED_GOLD"
    LEED_PLATINUM = "LEED_PLATINUM"
    ENERGY_STAR_CERTIFIED = "ENERGY_STAR_CERTIFIED"
    CODE_MINIMUM = "CODE_MINIMUM"

# Set metadata after class creation
BuildingEnergyPerformanceLevel._metadata = {
    "NET_ZERO_ENERGY": {'description': 'Building that produces as much energy as it consumes on an annual basis'},
    "NET_POSITIVE_ENERGY": {'description': 'Building that produces more energy than it consumes on an annual basis'},
    "PASSIVE_HOUSE": {'description': 'Building meeting Passive House Institute standards for ultra-low energy consumption'},
    "LEED_CERTIFIED": {'description': 'LEED Certified rating (40-49 points) from the U.S. Green Building Council'},
    "LEED_SILVER": {'description': 'LEED Silver rating (50-59 points) from the U.S. Green Building Council'},
    "LEED_GOLD": {'description': 'LEED Gold rating (60-79 points) from the U.S. Green Building Council'},
    "LEED_PLATINUM": {'description': 'LEED Platinum rating (80+ points) from the U.S. Green Building Council'},
    "ENERGY_STAR_CERTIFIED": {'description': 'EPA Energy Star certification for buildings performing in top 25% of energy efficiency'},
    "CODE_MINIMUM": {'description': 'Building meeting minimum energy code requirements without additional certification'},
}

__all__ = [
    "BuildingSystemType",
    "BuildingEnergyPerformanceLevel",
]