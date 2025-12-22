"""
Geothermal Energy Value Sets

Value sets for geothermal energy systems, reservoir types, well types, and technologies. Based on DOE Geothermal Technologies Office terminology and the Geothermal Data Repository standards.

Generated from: energy/renewable/geothermal.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class GeothermalSystemType(RichEnum):
    """
    Types of geothermal energy systems, including conventional hydrothermal and enhanced/engineered geothermal systems.
    """
    # Enum members
    HYDROTHERMAL = "HYDROTHERMAL"
    ENHANCED_GEOTHERMAL_SYSTEM = "ENHANCED_GEOTHERMAL_SYSTEM"
    ADVANCED_GEOTHERMAL_SYSTEM = "ADVANCED_GEOTHERMAL_SYSTEM"
    HOT_DRY_ROCK = "HOT_DRY_ROCK"
    GEOPRESSURED = "GEOPRESSURED"
    SUPERCRITICAL = "SUPERCRITICAL"
    GROUND_SOURCE_HEAT_PUMP = "GROUND_SOURCE_HEAT_PUMP"

# Set metadata after class creation
GeothermalSystemType._metadata = {
    "HYDROTHERMAL": {'description': 'Naturally occurring geothermal system with heat, fluid, and permeability sufficient for energy extraction without stimulation.', 'annotations': {'conventional': True}},
    "ENHANCED_GEOTHERMAL_SYSTEM": {'description': 'Engineered reservoirs created to extract heat from low permeability geothermal resources through stimulation methods.', 'annotations': {'requires_stimulation': True}, 'aliases': ['EGS', 'Engineered Geothermal System']},
    "ADVANCED_GEOTHERMAL_SYSTEM": {'description': 'Closed-loop geothermal systems that circulate working fluid through wellbores to extract heat conductively without reservoir stimulation.', 'annotations': {'closed_loop': True}, 'aliases': ['AGS', 'Closed-Loop Geothermal']},
    "HOT_DRY_ROCK": {'description': 'Geothermal system targeting hot basement rock lacking natural fluid or permeability, requiring artificial reservoir creation.', 'aliases': ['HDR']},
    "GEOPRESSURED": {'description': 'Deep sedimentary formations with abnormally high fluid pressure containing hot brine and dissolved methane.', 'annotations': {'methane_recovery': True}},
    "SUPERCRITICAL": {'description': 'Very high temperature systems (>374C) where water exists above its critical point, offering higher energy density.', 'annotations': {'temperature_min_c': 374}},
    "GROUND_SOURCE_HEAT_PUMP": {'description': 'Shallow geothermal system using stable ground temperatures for heating and cooling buildings.', 'annotations': {'direct_use': True}, 'aliases': ['GSHP', 'Geothermal Heat Pump']},
}

class GeothermalReservoirType(RichEnum):
    """
    Classification of geothermal reservoirs by geological setting and characteristics.
    """
    # Enum members
    VOLCANIC = "VOLCANIC"
    SEDIMENTARY = "SEDIMENTARY"
    FRACTURED_BASEMENT = "FRACTURED_BASEMENT"
    FAULT_CONTROLLED = "FAULT_CONTROLLED"
    MAGMATIC = "MAGMATIC"
    CONDUCTION_DOMINATED = "CONDUCTION_DOMINATED"

# Set metadata after class creation
GeothermalReservoirType._metadata = {
    "VOLCANIC": {'description': 'Reservoir associated with volcanic activity, typically in active volcanic regions with magma heat sources.'},
    "SEDIMENTARY": {'description': 'Reservoir in sedimentary formations with elevated temperatures due to depth or regional heat flow.'},
    "FRACTURED_BASEMENT": {'description': 'Reservoir in fractured crystalline basement rocks, typically granitic or metamorphic.', 'aliases': ['Hot Fractured Rock']},
    "FAULT_CONTROLLED": {'description': 'Reservoir where fluid flow is controlled by fault systems providing permeability pathways.'},
    "MAGMATIC": {'description': 'Very high temperature reservoir near or in contact with magma bodies or recent intrusions.'},
    "CONDUCTION_DOMINATED": {'description': 'Low permeability reservoir where heat transfer is primarily through conduction rather than convection.'},
}

class GeothermalWellType(RichEnum):
    """
    Types of wells used in geothermal energy development and production.
    """
    # Enum members
    PRODUCTION_WELL = "PRODUCTION_WELL"
    INJECTION_WELL = "INJECTION_WELL"
    EXPLORATION_WELL = "EXPLORATION_WELL"
    OBSERVATION_WELL = "OBSERVATION_WELL"
    SLIM_HOLE = "SLIM_HOLE"
    DIRECTIONAL_WELL = "DIRECTIONAL_WELL"

# Set metadata after class creation
GeothermalWellType._metadata = {
    "PRODUCTION_WELL": {'description': 'Well used to extract geothermal fluids or steam from the reservoir.'},
    "INJECTION_WELL": {'description': 'Well used to return cooled geothermal fluids to the reservoir to maintain pressure and sustainability.', 'aliases': ['Reinjection Well']},
    "EXPLORATION_WELL": {'description': 'Well drilled to evaluate geothermal resource characteristics.', 'aliases': ['Wildcat Well']},
    "OBSERVATION_WELL": {'description': 'Well used to monitor reservoir conditions and pressure.', 'aliases': ['Monitoring Well']},
    "SLIM_HOLE": {'description': 'Smaller diameter well used for initial exploration and temperature gradient measurement.'},
    "DIRECTIONAL_WELL": {'description': 'Well drilled at an angle to access reservoir from offset surface location or increase reservoir contact.'},
}

class GeothermalApplication(RichEnum):
    """
    Applications and uses of geothermal energy.
    """
    # Enum members
    ELECTRICITY_GENERATION = "ELECTRICITY_GENERATION"
    DIRECT_USE_HEATING = "DIRECT_USE_HEATING"
    GREENHOUSE_HEATING = "GREENHOUSE_HEATING"
    AQUACULTURE = "AQUACULTURE"
    INDUSTRIAL_PROCESS_HEAT = "INDUSTRIAL_PROCESS_HEAT"
    FOOD_PROCESSING = "FOOD_PROCESSING"
    BATHING_RECREATION = "BATHING_RECREATION"
    LITHIUM_EXTRACTION = "LITHIUM_EXTRACTION"

# Set metadata after class creation
GeothermalApplication._metadata = {
    "ELECTRICITY_GENERATION": {'description': 'Use of geothermal resources for power generation through steam turbines or binary cycle plants.'},
    "DIRECT_USE_HEATING": {'description': 'Direct use of geothermal heat for space heating, district heating, or industrial processes.'},
    "GREENHOUSE_HEATING": {'description': 'Use of geothermal heat for agricultural greenhouses.'},
    "AQUACULTURE": {'description': 'Use of geothermal heat for fish farming and aquaculture.'},
    "INDUSTRIAL_PROCESS_HEAT": {'description': 'Use of geothermal heat for industrial manufacturing processes.'},
    "FOOD_PROCESSING": {'description': 'Use of geothermal heat for food drying, pasteurization, and processing.'},
    "BATHING_RECREATION": {'description': 'Use of geothermal waters for spas, pools, and recreation.'},
    "LITHIUM_EXTRACTION": {'description': 'Extraction of lithium and other minerals from geothermal brines as a co-product of energy production.', 'annotations': {'co_production': True}},
}

class GeothermalResourceTemperature(RichEnum):
    """
    Classification of geothermal resources by temperature range.
    """
    # Enum members
    LOW_TEMPERATURE = "LOW_TEMPERATURE"
    MODERATE_TEMPERATURE = "MODERATE_TEMPERATURE"
    HIGH_TEMPERATURE = "HIGH_TEMPERATURE"
    SUPERCRITICAL = "SUPERCRITICAL"

# Set metadata after class creation
GeothermalResourceTemperature._metadata = {
    "LOW_TEMPERATURE": {'description': 'Geothermal resource below 90C, suitable for direct use applications.', 'annotations': {'temperature_max_c': 90}},
    "MODERATE_TEMPERATURE": {'description': 'Geothermal resource 90-150C, suitable for binary power generation.', 'annotations': {'temperature_min_c': 90, 'temperature_max_c': 150}},
    "HIGH_TEMPERATURE": {'description': 'Geothermal resource above 150C, suitable for flash steam power generation.', 'annotations': {'temperature_min_c': 150}},
    "SUPERCRITICAL": {'description': 'Very high temperature resource above 374C where water exists in supercritical state.', 'annotations': {'temperature_min_c': 374}},
}

__all__ = [
    "GeothermalSystemType",
    "GeothermalReservoirType",
    "GeothermalWellType",
    "GeothermalApplication",
    "GeothermalResourceTemperature",
]