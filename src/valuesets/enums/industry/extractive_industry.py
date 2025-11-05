"""

Generated from: industry/extractive_industry.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class ExtractiveIndustryFacilityTypeEnum(RichEnum):
    """
    Types of extractive industry facilities
    """
    # Enum members
    MINING_FACILITY = "MINING_FACILITY"
    WELL_FACILITY = "WELL_FACILITY"
    QUARRY_FACILITY = "QUARRY_FACILITY"

# Set metadata after class creation
ExtractiveIndustryFacilityTypeEnum._metadata = {
    "MINING_FACILITY": {'description': 'A facility where mineral resources are extracted'},
    "WELL_FACILITY": {'description': 'A facility where fluid resources are extracted'},
    "QUARRY_FACILITY": {'description': 'A facility where stone, sand, or gravel are extracted'},
}

class ExtractiveIndustryProductTypeEnum(RichEnum):
    """
    Types of products extracted from extractive industry facilities
    """
    # Enum members
    MINERAL = "MINERAL"
    METAL = "METAL"
    COAL = "COAL"
    OIL = "OIL"
    GAS = "GAS"
    STONE = "STONE"
    SAND = "SAND"
    GRAVEL = "GRAVEL"

# Set metadata after class creation
ExtractiveIndustryProductTypeEnum._metadata = {
    "MINERAL": {'description': 'A solid inorganic substance'},
    "METAL": {'description': 'A solid metallic substance'},
    "COAL": {'description': 'A combustible black or brownish-black sedimentary rock'},
    "OIL": {'description': 'A liquid petroleum resource'},
    "GAS": {'description': 'A gaseous petroleum resource'},
    "STONE": {'description': 'A solid aggregate of minerals'},
    "SAND": {'description': 'A granular material composed of finely divided rock and mineral particles'},
    "GRAVEL": {'description': 'A loose aggregation of rock fragments'},
}

class MiningMethodEnum(RichEnum):
    """
    Methods used for extracting minerals from the earth
    """
    # Enum members
    UNDERGROUND = "UNDERGROUND"
    OPEN_PIT = "OPEN_PIT"
    PLACER = "PLACER"
    IN_SITU = "IN_SITU"

# Set metadata after class creation
MiningMethodEnum._metadata = {
    "UNDERGROUND": {'description': "Extraction occurs beneath the earth's surface"},
    "OPEN_PIT": {'description': "Extraction occurs on the earth's surface"},
    "PLACER": {'description': 'Extraction of valuable minerals from alluvial deposits'},
    "IN_SITU": {'description': 'Extraction without removing the ore from its original location'},
}

class WellTypeEnum(RichEnum):
    """
    Types of wells used for extracting fluid resources
    """
    # Enum members
    OIL = "OIL"
    GAS = "GAS"
    WATER = "WATER"
    INJECTION = "INJECTION"

# Set metadata after class creation
WellTypeEnum._metadata = {
    "OIL": {'description': 'A well that primarily extracts crude oil'},
    "GAS": {'description': 'A well that primarily extracts natural gas'},
    "WATER": {'description': 'A well that extracts water for various purposes'},
    "INJECTION": {'description': 'A well used to inject fluids into underground formations'},
}

__all__ = [
    "ExtractiveIndustryFacilityTypeEnum",
    "ExtractiveIndustryProductTypeEnum",
    "MiningMethodEnum",
    "WellTypeEnum",
]