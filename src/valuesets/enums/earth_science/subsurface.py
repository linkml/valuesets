"""
Subsurface Science Value Sets

Value sets for subsurface characterization, geophysical methods, and formation types relevant to the DOE GEO-AI lighthouse and subsurface energy programs

Generated from: earth_science/subsurface.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class SubsurfaceFormationType(RichEnum):
    """
    Classification of subsurface geological formations relevant to energy exploration, carbon storage, geothermal systems, and groundwater resources.
    """
    # Enum members
    AQUIFER = "AQUIFER"
    AQUITARD = "AQUITARD"
    RESERVOIR_ROCK = "RESERVOIR_ROCK"
    CAPROCK = "CAPROCK"
    FAULT_ZONE = "FAULT_ZONE"
    KARST = "KARST"
    PERMAFROST = "PERMAFROST"
    UNCONSOLIDATED_SEDIMENT = "UNCONSOLIDATED_SEDIMENT"
    FRACTURED_BEDROCK = "FRACTURED_BEDROCK"
    COAL_SEAM = "COAL_SEAM"
    SALT_DOME = "SALT_DOME"
    SHALE = "SHALE"

# Set metadata after class creation
SubsurfaceFormationType._metadata = {
    "AQUIFER": {'description': 'An underground layer of water-bearing permeable rock or unconsolidated materials from which groundwater can be extracted', 'meaning': 'ENVO:00012408'},
    "AQUITARD": {'description': 'A zone within the earth that restricts the flow of groundwater from one aquifer to another'},
    "RESERVOIR_ROCK": {'description': 'A porous and permeable rock formation capable of storing and transmitting fluids such as oil, gas, or water'},
    "CAPROCK": {'description': 'An impermeable rock layer overlying a reservoir that prevents upward migration of fluids'},
    "FAULT_ZONE": {'description': 'A zone of fracturing and deformation along a geological fault'},
    "KARST": {'description': 'A landscape formed from dissolution of soluble rocks such as limestone, dolomite, and gypsum, characterized by sinkholes, caves, and underground drainage', 'meaning': 'ENVO:00000175'},
    "PERMAFROST": {'description': 'Soil or rock that remains at or below freezing for two or more consecutive years', 'meaning': 'ENVO:00000134'},
    "UNCONSOLIDATED_SEDIMENT": {'description': 'Loose, uncemented sedimentary material such as gravel, sand, silt, or clay'},
    "FRACTURED_BEDROCK": {'description': 'Bedrock containing natural fractures that may serve as pathways for fluid flow'},
    "COAL_SEAM": {'description': 'A stratum of coal within a sedimentary rock sequence'},
    "SALT_DOME": {'description': 'A dome-shaped intrusion of evaporite minerals formed by upward movement of a salt body through overlying rock', 'meaning': 'ENVO:01000505'},
    "SHALE": {'description': 'A fine-grained sedimentary rock formed from compacted clay or mud, often serving as a seal or source rock', 'meaning': 'ENVO:00002056'},
}

class GeophysicalMethodType(RichEnum):
    """
    Types of geophysical investigation methods used for subsurface characterization, resource exploration, and environmental monitoring.
    """
    # Enum members
    SEISMIC_REFLECTION = "SEISMIC_REFLECTION"
    SEISMIC_REFRACTION = "SEISMIC_REFRACTION"
    GROUND_PENETRATING_RADAR = "GROUND_PENETRATING_RADAR"
    ELECTRICAL_RESISTIVITY_TOMOGRAPHY = "ELECTRICAL_RESISTIVITY_TOMOGRAPHY"
    MAGNETOTELLURICS = "MAGNETOTELLURICS"
    GRAVITY_SURVEY = "GRAVITY_SURVEY"
    MAGNETIC_SURVEY = "MAGNETIC_SURVEY"
    WELL_LOGGING = "WELL_LOGGING"
    DISTRIBUTED_ACOUSTIC_SENSING = "DISTRIBUTED_ACOUSTIC_SENSING"
    DISTRIBUTED_TEMPERATURE_SENSING = "DISTRIBUTED_TEMPERATURE_SENSING"
    CROSSWELL_TOMOGRAPHY = "CROSSWELL_TOMOGRAPHY"

# Set metadata after class creation
GeophysicalMethodType._metadata = {
    "SEISMIC_REFLECTION": {'description': 'A geophysical method using reflected seismic waves to image subsurface geological structures'},
    "SEISMIC_REFRACTION": {'description': 'A geophysical method using refracted seismic waves to determine subsurface velocity structure and layer boundaries'},
    "GROUND_PENETRATING_RADAR": {'description': 'A geophysical method using radar pulses to image the shallow subsurface'},
    "ELECTRICAL_RESISTIVITY_TOMOGRAPHY": {'description': 'A geophysical imaging technique that measures the electrical resistivity distribution of the subsurface'},
    "MAGNETOTELLURICS": {'description': 'A geophysical method using natural electromagnetic fields to investigate the subsurface electrical conductivity structure'},
    "GRAVITY_SURVEY": {'description': 'A geophysical method measuring variations in the gravitational field to infer subsurface density distribution'},
    "MAGNETIC_SURVEY": {'description': 'A geophysical method measuring variations in the magnetic field to detect subsurface magnetic anomalies'},
    "WELL_LOGGING": {'description': 'Measurement of physical properties of rock formations traversed by a borehole using downhole instruments'},
    "DISTRIBUTED_ACOUSTIC_SENSING": {'description': 'A monitoring technique using fiber optic cables to measure acoustic signals along a borehole or surface deployment'},
    "DISTRIBUTED_TEMPERATURE_SENSING": {'description': 'A monitoring technique using fiber optic cables to measure temperature profiles along a borehole or surface deployment'},
    "CROSSWELL_TOMOGRAPHY": {'description': 'A geophysical imaging method using sources and receivers in separate boreholes to image the intervening subsurface'},
}

class SubsurfacePropertyType(RichEnum):
    """
    Physical and hydraulic properties of subsurface formations relevant to resource characterization and reservoir modeling.
    """
    # Enum members
    POROSITY = "POROSITY"
    PERMEABILITY = "PERMEABILITY"
    THERMAL_CONDUCTIVITY = "THERMAL_CONDUCTIVITY"
    SPECIFIC_HEAT_CAPACITY = "SPECIFIC_HEAT_CAPACITY"
    BULK_DENSITY = "BULK_DENSITY"
    FLUID_SATURATION = "FLUID_SATURATION"
    PORE_PRESSURE = "PORE_PRESSURE"
    GEOTHERMAL_GRADIENT = "GEOTHERMAL_GRADIENT"
    HYDRAULIC_CONDUCTIVITY = "HYDRAULIC_CONDUCTIVITY"
    ELASTIC_MODULUS = "ELASTIC_MODULUS"
    SEISMIC_VELOCITY = "SEISMIC_VELOCITY"

# Set metadata after class creation
SubsurfacePropertyType._metadata = {
    "POROSITY": {'description': 'The fraction of void space in a rock or sediment relative to its total volume', 'meaning': 'PATO:0000973'},
    "PERMEABILITY": {'description': 'The ability of a porous material to allow fluids to pass through it', 'meaning': 'PATO:0000970'},
    "THERMAL_CONDUCTIVITY": {'description': 'The rate at which heat is transferred through a material per unit area per unit temperature gradient'},
    "SPECIFIC_HEAT_CAPACITY": {'description': 'The amount of heat energy required to raise the temperature of a unit mass of material by one degree'},
    "BULK_DENSITY": {'description': 'The mass of a material divided by its total volume, including pore spaces'},
    "FLUID_SATURATION": {'description': 'The fraction of pore space occupied by a specific fluid phase'},
    "PORE_PRESSURE": {'description': 'The pressure of fluids within the pore spaces of rock or sediment'},
    "GEOTHERMAL_GRADIENT": {'description': "The rate of temperature increase with depth in the Earth's subsurface"},
    "HYDRAULIC_CONDUCTIVITY": {'description': 'A measure of the ease with which water can move through a porous medium under a hydraulic gradient'},
    "ELASTIC_MODULUS": {'description': 'A measure of the stiffness of a material, defined as the ratio of stress to strain'},
    "SEISMIC_VELOCITY": {'description': 'The speed at which seismic waves propagate through a subsurface material'},
}

__all__ = [
    "SubsurfaceFormationType",
    "GeophysicalMethodType",
    "SubsurfacePropertyType",
]