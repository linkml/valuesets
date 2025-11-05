"""
Earth Science Material Types

Material types for earth samples, based on SESAR (System for Earth Sample Registration) vocabulary

Generated from: earth_science/material_types.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class SESARMaterialType(RichEnum):
    """
    Material types as defined by SESAR (System for Earth Sample Registration). These describe what a sample consists of (e.g., rock, mineral, liquid).
    """
    # Enum members
    BIOLOGY = "BIOLOGY"
    GAS = "GAS"
    ICE = "ICE"
    LIQUID_AQUEOUS = "LIQUID_AQUEOUS"
    LIQUID_ORGANIC = "LIQUID_ORGANIC"
    MINERAL = "MINERAL"
    NOT_APPLICABLE = "NOT_APPLICABLE"
    ORGANIC_MATERIAL = "ORGANIC_MATERIAL"
    OTHER = "OTHER"
    PARTICULATE = "PARTICULATE"
    PLANT_STRUCTURE = "PLANT_STRUCTURE"
    ROCK = "ROCK"
    SEDIMENT = "SEDIMENT"
    SOIL = "SOIL"
    SYNTHETIC = "SYNTHETIC"

# Set metadata after class creation
SESARMaterialType._metadata = {
    "BIOLOGY": {'description': 'Biological material or specimens'},
    "GAS": {'description': 'Gaseous material'},
    "ICE": {'description': 'Frozen water or ice samples', 'meaning': 'ENVO:01001125'},
    "LIQUID_AQUEOUS": {'description': 'Aqueous (water-based) liquid', 'annotations': {'sesar_label': 'Liquid>aqueous'}},
    "LIQUID_ORGANIC": {'description': 'Organic liquid', 'annotations': {'sesar_label': 'Liquid>organic'}},
    "MINERAL": {'description': 'Mineral specimen', 'meaning': 'CHEBI:46662'},
    "NOT_APPLICABLE": {'description': 'Material type not applicable', 'annotations': {'sesar_label': 'NotApplicable'}},
    "ORGANIC_MATERIAL": {'description': 'Organic material (non-living)', 'meaning': 'ENVO:01000155'},
    "OTHER": {'description': 'Other material type not listed'},
    "PARTICULATE": {'description': 'Particulate matter'},
    "PLANT_STRUCTURE": {'description': 'Plant structure or tissue', 'meaning': 'PO:0009011'},
    "ROCK": {'description': 'Rock specimen', 'meaning': 'ENVO:00001995'},
    "SEDIMENT": {'description': 'Sediment sample', 'meaning': 'ENVO:00002007'},
    "SOIL": {'description': 'Soil sample', 'meaning': 'ENVO:00001998'},
    "SYNTHETIC": {'description': 'Synthetic or artificial material'},
}

__all__ = [
    "SESARMaterialType",
]