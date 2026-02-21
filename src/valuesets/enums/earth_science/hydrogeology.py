"""
Hydrogeology Value Sets

Value sets for hydrogeological characterization, aquifer types, and groundwater processes

Generated from: earth_science/hydrogeology.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class AquiferType(RichEnum):
    """
    Classification of aquifer types based on confinement, geology, and hydraulic characteristics.
    """
    # Enum members
    UNCONFINED = "UNCONFINED"
    CONFINED = "CONFINED"
    SEMI_CONFINED = "SEMI_CONFINED"
    PERCHED = "PERCHED"
    ARTESIAN = "ARTESIAN"
    FRACTURED_ROCK = "FRACTURED_ROCK"
    KARST = "KARST"
    ALLUVIAL = "ALLUVIAL"

# Set metadata after class creation
AquiferType._metadata = {
    "UNCONFINED": {'description': 'An aquifer whose upper boundary is the water table, open to atmospheric pressure'},
    "CONFINED": {'description': 'An aquifer bounded above and below by impermeable layers, under pressure greater than atmospheric'},
    "SEMI_CONFINED": {'description': 'An aquifer partially bounded by layers of lower permeability that allow some vertical leakage'},
    "PERCHED": {'description': 'A localized unconfined aquifer above the regional water table, supported by a low-permeability layer'},
    "ARTESIAN": {'description': 'A confined aquifer in which the hydraulic pressure causes water to rise above the top of the aquifer'},
    "FRACTURED_ROCK": {'description': 'An aquifer in which groundwater flows primarily through fractures in otherwise low-permeability rock'},
    "KARST": {'description': 'An aquifer in soluble rock such as limestone where flow occurs through dissolution-enlarged conduits and fractures'},
    "ALLUVIAL": {'description': 'An aquifer composed of unconsolidated alluvial deposits such as sand and gravel deposited by rivers'},
}

class GroundwaterProcessType(RichEnum):
    """
    Types of physical, chemical, and biological processes occurring in groundwater systems.
    """
    # Enum members
    RECHARGE = "RECHARGE"
    DISCHARGE = "DISCHARGE"
    BASEFLOW = "BASEFLOW"
    LATERAL_FLOW = "LATERAL_FLOW"
    VERTICAL_LEAKAGE = "VERTICAL_LEAKAGE"
    SALTWATER_INTRUSION = "SALTWATER_INTRUSION"
    CONTAMINANT_TRANSPORT = "CONTAMINANT_TRANSPORT"
    BIODEGRADATION = "BIODEGRADATION"
    SORPTION = "SORPTION"
    PRECIPITATION_DISSOLUTION = "PRECIPITATION_DISSOLUTION"

# Set metadata after class creation
GroundwaterProcessType._metadata = {
    "RECHARGE": {'description': 'The process by which water enters an aquifer from the surface or from an overlying formation'},
    "DISCHARGE": {'description': 'The process by which groundwater exits an aquifer to the surface or to another formation'},
    "BASEFLOW": {'description': 'The portion of streamflow derived from groundwater discharge into surface water bodies'},
    "LATERAL_FLOW": {'description': 'Horizontal movement of groundwater through an aquifer'},
    "VERTICAL_LEAKAGE": {'description': 'Vertical movement of groundwater between aquifers through semi-confining layers'},
    "SALTWATER_INTRUSION": {'description': 'The movement of saline water into freshwater aquifers, typically in coastal areas'},
    "CONTAMINANT_TRANSPORT": {'description': 'The movement and spreading of dissolved or suspended contaminants through groundwater'},
    "BIODEGRADATION": {'description': 'The biological breakdown of contaminants in groundwater by microbial activity'},
    "SORPTION": {'description': 'The process by which dissolved substances are attached to solid surfaces in the aquifer matrix'},
    "PRECIPITATION_DISSOLUTION": {'description': 'Chemical processes involving the formation or dissolution of mineral phases in groundwater'},
}

class HydrogeologyWellType(RichEnum):
    """
    Classification of wells used for groundwater access, monitoring, and management.
    """
    # Enum members
    MONITORING_WELL = "MONITORING_WELL"
    PRODUCTION_WELL = "PRODUCTION_WELL"
    INJECTION_WELL = "INJECTION_WELL"
    OBSERVATION_WELL = "OBSERVATION_WELL"
    PIEZOMETER = "PIEZOMETER"
    EXTRACTION_WELL = "EXTRACTION_WELL"
    RECHARGE_WELL = "RECHARGE_WELL"
    GEOTHERMAL_WELL = "GEOTHERMAL_WELL"

# Set metadata after class creation
HydrogeologyWellType._metadata = {
    "MONITORING_WELL": {'description': 'A well used to observe and measure groundwater conditions such as water level, quality, and flow'},
    "PRODUCTION_WELL": {'description': 'A well used to extract groundwater for water supply purposes'},
    "INJECTION_WELL": {'description': 'A well used to inject fluids into the subsurface for disposal, storage, or aquifer recharge'},
    "OBSERVATION_WELL": {'description': 'A well used to observe hydrological parameters without significant water extraction'},
    "PIEZOMETER": {'description': 'A device or small-diameter well used to measure hydraulic head at a specific point in the subsurface'},
    "EXTRACTION_WELL": {'description': 'A well used to remove contaminated groundwater as part of remediation activities'},
    "RECHARGE_WELL": {'description': 'A well used to artificially replenish groundwater by injecting treated water into an aquifer'},
    "GEOTHERMAL_WELL": {'description': 'A well drilled to access geothermal resources for energy production or direct use'},
}

__all__ = [
    "AquiferType",
    "GroundwaterProcessType",
    "HydrogeologyWellType",
]