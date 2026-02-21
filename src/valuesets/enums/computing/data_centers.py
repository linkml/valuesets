"""
Data Center Value Sets

Value sets for data center infrastructure relevant to the DOE Securing U.S. Leadership in Data Centers challenge

Generated from: computing/data_centers.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class DataCenterCoolingType(RichEnum):
    """
    Types of cooling systems used in data center facilities
    """
    # Enum members
    AIR_COOLING = "AIR_COOLING"
    LIQUID_COOLING = "LIQUID_COOLING"
    IMMERSION_COOLING = "IMMERSION_COOLING"
    REAR_DOOR_HEAT_EXCHANGER = "REAR_DOOR_HEAT_EXCHANGER"
    EVAPORATIVE_COOLING = "EVAPORATIVE_COOLING"
    GEOTHERMAL_COOLING = "GEOTHERMAL_COOLING"
    FREE_AIR_COOLING = "FREE_AIR_COOLING"
    DIRECT_TO_CHIP_LIQUID_COOLING = "DIRECT_TO_CHIP_LIQUID_COOLING"

# Set metadata after class creation
DataCenterCoolingType._metadata = {
    "AIR_COOLING": {'description': 'Traditional air-based cooling using computer room air conditioning (CRAC) or air handling units'},
    "LIQUID_COOLING": {'description': 'Cooling using liquid coolant circulated through heat exchangers near server components'},
    "IMMERSION_COOLING": {'description': 'Cooling by submerging server hardware in a thermally conductive dielectric liquid'},
    "REAR_DOOR_HEAT_EXCHANGER": {'description': 'Liquid-to-air heat exchanger mounted on the rear door of server racks'},
    "EVAPORATIVE_COOLING": {'description': 'Cooling that uses water evaporation to reduce air temperature'},
    "GEOTHERMAL_COOLING": {'description': 'Cooling that leverages underground temperature stability for heat dissipation'},
    "FREE_AIR_COOLING": {'description': 'Cooling using outside ambient air when conditions permit, reducing mechanical cooling load'},
    "DIRECT_TO_CHIP_LIQUID_COOLING": {'description': 'Liquid cooling with cold plates attached directly to processors and other heat-generating components'},
}

class DataCenterTierLevel(RichEnum):
    """
    Uptime Institute data center tier classification levels defining infrastructure reliability
    """
    # Enum members
    TIER_I = "TIER_I"
    TIER_II = "TIER_II"
    TIER_III = "TIER_III"
    TIER_IV = "TIER_IV"

# Set metadata after class creation
DataCenterTierLevel._metadata = {
    "TIER_I": {'description': 'Basic capacity - single non-redundant distribution path with no redundancy', 'annotations': {'uptime_guarantee': '99.671%', 'classification': 'Basic'}},
    "TIER_II": {'description': 'Redundant capacity components - single non-redundant distribution path with redundant components', 'annotations': {'uptime_guarantee': '99.741%', 'classification': 'Redundant Components'}},
    "TIER_III": {'description': 'Concurrently maintainable - multiple independent distribution paths with redundant components', 'annotations': {'uptime_guarantee': '99.982%', 'classification': 'Concurrently Maintainable'}},
    "TIER_IV": {'description': 'Fault tolerant - multiple independent distribution paths with redundant components, fault tolerant', 'annotations': {'uptime_guarantee': '99.995%', 'classification': 'Fault Tolerant'}},
}

__all__ = [
    "DataCenterCoolingType",
    "DataCenterTierLevel",
]