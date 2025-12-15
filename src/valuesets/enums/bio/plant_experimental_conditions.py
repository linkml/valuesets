"""
Plant Experimental Conditions Value Sets

Value sets based on the Plant Experimental Conditions Ontology (PECO), including plant exposures and study conditions.

Generated from: bio/plant_experimental_conditions.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class PlantStudyConditionEnum(RichEnum):
    """
    The type of plant growth facility used in an experiment, describing whether plants were grown in a field, greenhouse, growth chamber, or laboratory.
    """
    # Enum members
    FIELD_STUDY = "FIELD_STUDY"
    GREENHOUSE_STUDY = "GREENHOUSE_STUDY"
    GROWTH_CHAMBER_STUDY = "GROWTH_CHAMBER_STUDY"
    LABORATORY_STUDY = "LABORATORY_STUDY"

# Set metadata after class creation
PlantStudyConditionEnum._metadata = {
    "FIELD_STUDY": {'description': 'Plants were grown outdoors under field conditions', 'meaning': 'PECO:0007256'},
    "GREENHOUSE_STUDY": {'description': 'Plants were grown under greenhouse conditions', 'meaning': 'PECO:0007248'},
    "GROWTH_CHAMBER_STUDY": {'description': 'Plants were grown in growth chambers under controlled light and temperature conditions', 'meaning': 'PECO:0007269'},
    "LABORATORY_STUDY": {'description': 'Plants were grown under in vitro growth conditions in a laboratory', 'meaning': 'PECO:0007255'},
}

class SeasonalEnvironmentExposureEnum(RichEnum):
    """
    Seasonal conditions during plant growth, including standard seasons and regional agricultural seasons (e.g., kharif, rabi in South Asia).
    """
    # Enum members
    SPRING_SEASON = "SPRING_SEASON"
    SUMMER_SEASON = "SUMMER_SEASON"
    AUTUMN_SEASON = "AUTUMN_SEASON"
    WINTER_SEASON = "WINTER_SEASON"
    DRY_SEASON = "DRY_SEASON"
    RAINY_SEASON = "RAINY_SEASON"
    KHARIF_SEASON = "KHARIF_SEASON"
    RABI_SEASON = "RABI_SEASON"

# Set metadata after class creation
SeasonalEnvironmentExposureEnum._metadata = {
    "SPRING_SEASON": {'description': 'Growth during the spring season', 'meaning': 'PECO:0007037'},
    "SUMMER_SEASON": {'description': 'Growth during the summer season', 'meaning': 'PECO:0007036'},
    "AUTUMN_SEASON": {'description': 'Growth during the autumn season', 'meaning': 'PECO:0007038'},
    "WINTER_SEASON": {'description': 'Growth during the winter season', 'meaning': 'PECO:0007035'},
    "DRY_SEASON": {'description': 'Growth during the dry season', 'meaning': 'PECO:0007286'},
    "RAINY_SEASON": {'description': 'Growth during the wet or rainy season', 'meaning': 'PECO:0007285'},
    "KHARIF_SEASON": {'description': 'Growth during the kharif crop season (May-October) as practiced in South Asia', 'meaning': 'PECO:0007034'},
    "RABI_SEASON": {'description': 'Growth during the rabi crop season (October-March) as practiced in South Asia', 'meaning': 'PECO:0007033'},
}

class EcologicalEnvironmentExposureEnum(RichEnum):
    """
    Ecological or geographical environment conditions during plant growth, including climate zones, altitude, atmospheric pressure, and land characteristics.
    """
    # Enum members
    ALTITUDE = "ALTITUDE"
    ATMOSPHERIC_PRESSURE = "ATMOSPHERIC_PRESSURE"
    TROPICAL_REGION = "TROPICAL_REGION"
    SUB_TROPICAL_REGION = "SUB_TROPICAL_REGION"
    TEMPERATE_REGION = "TEMPERATE_REGION"
    DESERT_LIKE_REGION = "DESERT_LIKE_REGION"
    SEMIARID_REGION = "SEMIARID_REGION"
    LOWLAND_REGION = "LOWLAND_REGION"
    UPLAND_REGION = "UPLAND_REGION"
    FLOOD_PRONE_REGION = "FLOOD_PRONE_REGION"
    IRRIGATED_LAND_REGION = "IRRIGATED_LAND_REGION"

# Set metadata after class creation
EcologicalEnvironmentExposureEnum._metadata = {
    "ALTITUDE": {'description': 'Growth at a given elevation or height above sea level', 'meaning': 'PECO:0007176'},
    "ATMOSPHERIC_PRESSURE": {'description': 'Growth at a given air pressure', 'meaning': 'PECO:0007178'},
    "TROPICAL_REGION": {'description': 'Growth in the geographical region between the Tropics of Cancer and Capricorn', 'meaning': 'PECO:0007061'},
    "SUB_TROPICAL_REGION": {'description': 'Growth in regions adjacent to the tropics (roughly 25-40 degrees latitude)', 'meaning': 'PECO:0007398'},
    "TEMPERATE_REGION": {'description': 'Growth in regions with temperate climate, characterized by roughly equal winters and summers', 'meaning': 'PECO:0007003'},
    "DESERT_LIKE_REGION": {'description': 'Growth in biome characterized by low moisture and infrequent precipitation', 'meaning': 'PECO:0007394'},
    "SEMIARID_REGION": {'description': 'Growth in regions with 25-50cm (10-20 inches) annual rainfall', 'meaning': 'PECO:0007401'},
    "LOWLAND_REGION": {'description': 'Growth in slightly steep regions with noncontinuous flooding and alternating aerobic/anaerobic soil', 'meaning': 'PECO:0007391'},
    "UPLAND_REGION": {'description': 'Growth in steep regions that are rarely flooded with aerobic soil', 'meaning': 'PECO:0007392'},
    "FLOOD_PRONE_REGION": {'description': 'Growth in conditions susceptible to inundation by water', 'meaning': 'PECO:0007396'},
    "IRRIGATED_LAND_REGION": {'description': 'Growth in leveled land with water control and shallow flooding', 'meaning': 'PECO:0007385'},
}

class PlantGrowthMediumExposureEnum(RichEnum):
    """
    The type of growth medium or substrate used for plant cultivation, including soil, hydroponic, aeroponic, and in vitro media.
    """
    # Enum members
    SOIL_ENVIRONMENT = "SOIL_ENVIRONMENT"
    HYDROPONIC_CULTURE = "HYDROPONIC_CULTURE"
    AEROPONIC_GROWTH = "AEROPONIC_GROWTH"
    IN_VITRO_GROWTH_MEDIUM = "IN_VITRO_GROWTH_MEDIUM"

# Set metadata after class creation
PlantGrowthMediumExposureEnum._metadata = {
    "SOIL_ENVIRONMENT": {'description': 'Growing plants in soil growth media with varying contents', 'meaning': 'PECO:0007049'},
    "HYDROPONIC_CULTURE": {'description': 'Growing plants in liquid growth media', 'meaning': 'PECO:0007067'},
    "AEROPONIC_GROWTH": {'description': 'Growing plants in air and/or mist environment without soil or aggregate medium', 'meaning': 'PECO:0001073'},
    "IN_VITRO_GROWTH_MEDIUM": {'description': 'In vitro culture using solid or liquid substrate with nutrients and amendments', 'meaning': 'PECO:0007266'},
}

__all__ = [
    "PlantStudyConditionEnum",
    "SeasonalEnvironmentExposureEnum",
    "EcologicalEnvironmentExposureEnum",
    "PlantGrowthMediumExposureEnum",
]