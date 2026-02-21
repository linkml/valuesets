"""
Subsurface Energy Value Sets

Value sets for subsurface energy resources and storage technologies relevant to the DOE Unleashing Subsurface Strategic Energy Assets challenge

Generated from: energy/subsurface_energy.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class SubsurfaceEnergyResourceType(RichEnum):
    """
    Types of subsurface energy resources including geothermal, hydrocarbon, and other geological energy assets
    """
    # Enum members
    GEOTHERMAL_RESERVOIR = "GEOTHERMAL_RESERVOIR"
    ENHANCED_GEOTHERMAL_SYSTEM = "ENHANCED_GEOTHERMAL_SYSTEM"
    OIL_RESERVOIR = "OIL_RESERVOIR"
    NATURAL_GAS_RESERVOIR = "NATURAL_GAS_RESERVOIR"
    COALBED_METHANE = "COALBED_METHANE"
    GAS_HYDRATE = "GAS_HYDRATE"
    HOT_DRY_ROCK = "HOT_DRY_ROCK"
    SEDIMENTARY_BASIN = "SEDIMENTARY_BASIN"
    VOLCANIC_SYSTEM = "VOLCANIC_SYSTEM"

# Set metadata after class creation
SubsurfaceEnergyResourceType._metadata = {
    "GEOTHERMAL_RESERVOIR": {'description': 'Natural subsurface reservoir containing hot water or steam suitable for geothermal energy extraction', 'annotations': {'temperature_range': '90-350 C', 'resource_type': 'renewable'}},
    "ENHANCED_GEOTHERMAL_SYSTEM": {'description': 'Engineered subsurface reservoir created by hydraulic stimulation of hot dry rock for geothermal energy', 'annotations': {'abbreviation': 'EGS', 'resource_type': 'renewable'}},
    "OIL_RESERVOIR": {'description': 'Subsurface formation containing fluid hydrocarbons in porous or fractured rock', 'meaning': 'ENVO:00002185'},
    "NATURAL_GAS_RESERVOIR": {'description': 'Subsurface formation containing natural gas trapped in porous or fractured rock', 'annotations': {'resource_type': 'fossil fuel'}},
    "COALBED_METHANE": {'description': 'Methane gas adsorbed in coal seams that can be extracted as an energy resource', 'annotations': {'abbreviation': 'CBM', 'resource_type': 'fossil fuel'}},
    "GAS_HYDRATE": {'description': 'Crystalline ice-like structures containing methane trapped in water molecule cages, found in ocean sediments and permafrost regions', 'meaning': 'ENVO:01000851'},
    "HOT_DRY_ROCK": {'description': 'Deep crystalline basement rock with high temperature but low natural permeability, targeted for enhanced geothermal systems', 'annotations': {'typical_depth': '>3 km', 'temperature': '>150 C'}},
    "SEDIMENTARY_BASIN": {'description': 'Large-scale geological depression filled with sedimentary rocks that may contain energy resources', 'annotations': {'resource_potential': 'hydrocarbons, geothermal, CO2 storage'}},
    "VOLCANIC_SYSTEM": {'description': 'Volcanic geological system with high geothermal gradients suitable for energy extraction', 'meaning': 'ENVO:00000354'},
}

class SubsurfaceStorageType(RichEnum):
    """
    Types of subsurface energy and material storage technologies utilizing geological formations
    """
    # Enum members
    CARBON_CAPTURE_AND_STORAGE = "CARBON_CAPTURE_AND_STORAGE"
    HYDROGEN_STORAGE = "HYDROGEN_STORAGE"
    COMPRESSED_AIR_ENERGY_STORAGE = "COMPRESSED_AIR_ENERGY_STORAGE"
    NATURAL_GAS_STORAGE = "NATURAL_GAS_STORAGE"
    THERMAL_ENERGY_STORAGE = "THERMAL_ENERGY_STORAGE"
    NUCLEAR_WASTE_REPOSITORY = "NUCLEAR_WASTE_REPOSITORY"

# Set metadata after class creation
SubsurfaceStorageType._metadata = {
    "CARBON_CAPTURE_AND_STORAGE": {'description': 'Capture of CO2 from industrial sources and injection into deep geological formations for permanent storage', 'annotations': {'abbreviation': 'CCS', 'target_formations': 'saline aquifers, depleted reservoirs'}},
    "HYDROGEN_STORAGE": {'description': 'Underground storage of hydrogen gas in geological formations such as salt caverns or depleted reservoirs', 'annotations': {'formations': 'salt caverns, depleted gas fields, aquifers'}},
    "COMPRESSED_AIR_ENERGY_STORAGE": {'description': 'Storage of compressed air in underground caverns for later electricity generation', 'annotations': {'abbreviation': 'CAES', 'formations': 'salt caverns, hard rock caverns'}},
    "NATURAL_GAS_STORAGE": {'description': 'Underground storage of natural gas in geological formations for seasonal demand management', 'annotations': {'formations': 'depleted reservoirs, aquifers, salt caverns'}},
    "THERMAL_ENERGY_STORAGE": {'description': 'Storage of thermal energy in subsurface formations for heating and cooling applications', 'annotations': {'types': 'aquifer thermal energy storage, borehole thermal energy storage'}},
    "NUCLEAR_WASTE_REPOSITORY": {'description': 'Deep geological repository for permanent disposal of high-level nuclear waste', 'annotations': {'formations': 'crystalline rock, clay, salt', 'depth': '>300 m'}},
}

class ReservoirCharacterizationMethodType(RichEnum):
    """
    Methods and techniques used to characterize subsurface reservoirs for energy extraction and storage applications
    """
    # Enum members
    WELL_TEST_ANALYSIS = "WELL_TEST_ANALYSIS"
    SEISMIC_INTERPRETATION = "SEISMIC_INTERPRETATION"
    CORE_ANALYSIS = "CORE_ANALYSIS"
    WIRELINE_LOGGING = "WIRELINE_LOGGING"
    TRACER_TEST = "TRACER_TEST"
    PRESSURE_TRANSIENT_ANALYSIS = "PRESSURE_TRANSIENT_ANALYSIS"
    PRODUCTION_HISTORY_MATCHING = "PRODUCTION_HISTORY_MATCHING"
    GEOSTATISTICAL_MODELING = "GEOSTATISTICAL_MODELING"

# Set metadata after class creation
ReservoirCharacterizationMethodType._metadata = {
    "WELL_TEST_ANALYSIS": {'description': 'Analysis of pressure and flow rate data from well tests to determine reservoir properties', 'annotations': {'parameters': 'permeability, skin factor, reservoir boundaries'}},
    "SEISMIC_INTERPRETATION": {'description': 'Interpretation of seismic survey data to map subsurface geological structures and properties', 'annotations': {'types': '2D seismic, 3D seismic, 4D time-lapse'}},
    "CORE_ANALYSIS": {'description': 'Laboratory analysis of rock core samples to determine petrophysical and geomechanical properties', 'annotations': {'measurements': 'porosity, permeability, saturation, mechanical strength'}},
    "WIRELINE_LOGGING": {'description': 'Measurement of formation properties using instruments lowered into a wellbore on a wireline', 'annotations': {'logs': 'gamma ray, resistivity, neutron, density, sonic'}},
    "TRACER_TEST": {'description': 'Injection and monitoring of chemical or radioactive tracers to characterize fluid flow paths', 'annotations': {'purpose': 'flow path identification, residence time distribution'}},
    "PRESSURE_TRANSIENT_ANALYSIS": {'description': 'Analysis of pressure changes over time during well operations to infer reservoir characteristics', 'annotations': {'tests': 'drawdown, buildup, interference'}},
    "PRODUCTION_HISTORY_MATCHING": {'description': 'Calibration of reservoir simulation models by matching historical production data', 'annotations': {'approach': 'inverse modeling, parameter estimation'}},
    "GEOSTATISTICAL_MODELING": {'description': 'Statistical methods for spatial interpolation and uncertainty quantification of reservoir properties', 'annotations': {'methods': 'kriging, sequential Gaussian simulation, multiple-point statistics'}},
}

__all__ = [
    "SubsurfaceEnergyResourceType",
    "SubsurfaceStorageType",
    "ReservoirCharacterizationMethodType",
]