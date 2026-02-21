"""
Water Resources Value Sets

Value sets for water resource types, water use categories, and water quality relevant to the DOE 'Predicting U.S. Water for Energy' challenge

Generated from: earth_science/water_resources.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class WaterResourceType(RichEnum):
    """
    Classification of water resources by source, quality, and origin.
    """
    # Enum members
    SURFACE_WATER = "SURFACE_WATER"
    GROUNDWATER = "GROUNDWATER"
    PRODUCED_WATER = "PRODUCED_WATER"
    BRACKISH_WATER = "BRACKISH_WATER"
    SEAWATER = "SEAWATER"
    STORMWATER = "STORMWATER"
    WASTEWATER = "WASTEWATER"
    RECLAIMED_WATER = "RECLAIMED_WATER"
    GLACIAL_MELTWATER = "GLACIAL_MELTWATER"

# Set metadata after class creation
WaterResourceType._metadata = {
    "SURFACE_WATER": {'description': 'Water found on the surface of the Earth in rivers, lakes, reservoirs, and wetlands', 'meaning': 'ENVO:00002042'},
    "GROUNDWATER": {'description': 'Underground water located in pore spaces of rock or unconsolidated deposits', 'meaning': 'ENVO:01001004'},
    "PRODUCED_WATER": {'description': 'Water brought to the surface during oil, gas, or geothermal extraction operations'},
    "BRACKISH_WATER": {'description': 'Water with salinity between freshwater and seawater', 'meaning': 'ENVO:00002019'},
    "SEAWATER": {'description': 'Water from the ocean or sea with characteristic salinity levels'},
    "STORMWATER": {'description': 'Water that accumulates on surfaces during precipitation events and snow or ice melt', 'meaning': 'ENVO:01001267'},
    "WASTEWATER": {'description': 'Water that has been adversely affected in quality by anthropogenic influence'},
    "RECLAIMED_WATER": {'description': 'Wastewater that has been treated to a level suitable for beneficial reuse'},
    "GLACIAL_MELTWATER": {'description': 'Water released by the melting of glacial ice, ice sheets, or ice shelves'},
}

class WaterUseCategoryType(RichEnum):
    """
    Classification of water use categories relevant to the water-energy nexus and national water resource planning.
    """
    # Enum members
    AGRICULTURAL_IRRIGATION = "AGRICULTURAL_IRRIGATION"
    INDUSTRIAL_COOLING = "INDUSTRIAL_COOLING"
    MUNICIPAL_SUPPLY = "MUNICIPAL_SUPPLY"
    THERMOELECTRIC_POWER = "THERMOELECTRIC_POWER"
    HYDROELECTRIC = "HYDROELECTRIC"
    MINING = "MINING"
    LIVESTOCK = "LIVESTOCK"
    AQUACULTURE = "AQUACULTURE"
    ENVIRONMENTAL_FLOW = "ENVIRONMENTAL_FLOW"

# Set metadata after class creation
WaterUseCategoryType._metadata = {
    "AGRICULTURAL_IRRIGATION": {'description': 'Water used for irrigation of crops and agricultural land'},
    "INDUSTRIAL_COOLING": {'description': 'Water used for cooling processes in industrial facilities'},
    "MUNICIPAL_SUPPLY": {'description': 'Water supplied for domestic, commercial, and public use by a municipal system'},
    "THERMOELECTRIC_POWER": {'description': 'Water used in thermoelectric power generation for steam production and cooling'},
    "HYDROELECTRIC": {'description': 'Water used for hydroelectric power generation'},
    "MINING": {'description': 'Water used in mining operations for extraction, processing, and dust suppression'},
    "LIVESTOCK": {'description': 'Water used for livestock watering, feedlots, and dairy operations'},
    "AQUACULTURE": {'description': 'Water used for farming aquatic organisms including fish, shellfish, and plants'},
    "ENVIRONMENTAL_FLOW": {'description': 'Water allocated to maintain or restore ecological health of rivers, wetlands, and other water-dependent ecosystems'},
}

class WaterQualityParameterType(RichEnum):
    """
    Physical, chemical, and biological parameters used to assess water quality for various applications.
    """
    # Enum members
    PH = "PH"
    DISSOLVED_OXYGEN = "DISSOLVED_OXYGEN"
    TOTAL_DISSOLVED_SOLIDS = "TOTAL_DISSOLVED_SOLIDS"
    TURBIDITY = "TURBIDITY"
    CONDUCTIVITY = "CONDUCTIVITY"
    BIOLOGICAL_OXYGEN_DEMAND = "BIOLOGICAL_OXYGEN_DEMAND"
    CHEMICAL_OXYGEN_DEMAND = "CHEMICAL_OXYGEN_DEMAND"
    NITRATE = "NITRATE"
    PHOSPHATE = "PHOSPHATE"
    HEAVY_METALS = "HEAVY_METALS"
    COLIFORM_BACTERIA = "COLIFORM_BACTERIA"
    TEMPERATURE = "TEMPERATURE"

# Set metadata after class creation
WaterQualityParameterType._metadata = {
    "PH": {'description': 'A measure of the hydrogen ion concentration indicating the acidity or alkalinity of water'},
    "DISSOLVED_OXYGEN": {'description': 'The concentration of molecular oxygen dissolved in water'},
    "TOTAL_DISSOLVED_SOLIDS": {'description': 'The total concentration of dissolved inorganic and organic substances in water'},
    "TURBIDITY": {'description': 'A measure of the degree to which water loses its transparency due to suspended particulates'},
    "CONDUCTIVITY": {'description': 'The ability of water to conduct an electrical current, related to the concentration of dissolved ions'},
    "BIOLOGICAL_OXYGEN_DEMAND": {'description': 'The amount of dissolved oxygen consumed by biological organisms during the decomposition of organic matter'},
    "CHEMICAL_OXYGEN_DEMAND": {'description': 'The amount of oxygen required to chemically oxidize organic and inorganic matter in water'},
    "NITRATE": {'description': 'The concentration of nitrate ions in water, an indicator of nutrient loading', 'meaning': 'CHEBI:17632'},
    "PHOSPHATE": {'description': 'The concentration of phosphate in water, an indicator of nutrient loading and eutrophication potential', 'meaning': 'CHEBI:26020'},
    "HEAVY_METALS": {'description': 'The concentration of heavy metals in water, including lead, mercury, cadmium, and arsenic'},
    "COLIFORM_BACTERIA": {'description': 'The presence and concentration of coliform bacteria as indicators of microbial contamination'},
    "TEMPERATURE": {'description': 'The thermal energy of the water, affecting dissolved oxygen levels and biological activity', 'meaning': 'PATO:0000146'},
}

__all__ = [
    "WaterResourceType",
    "WaterUseCategoryType",
    "WaterQualityParameterType",
]