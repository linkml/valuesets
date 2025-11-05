"""
Biological Color Value Sets

Color value sets for biological traits including eye colors, hair colors, flower colors, and other phenotypic color characteristics.


Generated from: bio/biological_colors.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class EyeColorEnum(RichEnum):
    """
    Human eye color phenotypes
    """
    # Enum members
    BROWN = "BROWN"
    BLUE = "BLUE"
    GREEN = "GREEN"
    HAZEL = "HAZEL"
    AMBER = "AMBER"
    GRAY = "GRAY"
    HETEROCHROMIA = "HETEROCHROMIA"
    RED_PINK = "RED_PINK"
    VIOLET = "VIOLET"

# Set metadata after class creation
EyeColorEnum._metadata = {
    "BROWN": {'description': 'Brown eyes', 'annotations': {'hex_range': '663300-8B4513', 'prevalence': '79% worldwide'}},
    "BLUE": {'description': 'Blue eyes', 'meaning': 'HP:0000635', 'annotations': {'hex_range': '4169E1-87CEEB', 'prevalence': '8-10% worldwide'}},
    "GREEN": {'description': 'Green eyes', 'annotations': {'hex_range': '2E8B57-90EE90', 'prevalence': '2% worldwide'}},
    "HAZEL": {'description': 'Hazel eyes (brown-green mix)', 'annotations': {'hex_range': '8B7355-C9A878', 'prevalence': '5% worldwide'}},
    "AMBER": {'description': 'Amber/golden eyes', 'annotations': {'hex_range': 'FFBF00-FFB300', 'prevalence': 'rare'}},
    "GRAY": {'description': 'Gray eyes', 'meaning': 'HP:0007730', 'annotations': {'hex_range': '778899-C0C0C0', 'prevalence': '<1% worldwide'}},
    "HETEROCHROMIA": {'description': 'Different colored eyes', 'meaning': 'HP:0001100', 'annotations': {'note': 'complete or sectoral heterochromia'}},
    "RED_PINK": {'description': 'Red/pink eyes (albinism)', 'annotations': {'condition': 'associated with albinism'}},
    "VIOLET": {'description': 'Violet eyes (extremely rare)', 'annotations': {'hex_range': '8B7AB8-9370DB', 'prevalence': 'extremely rare'}},
}

class HairColorEnum(RichEnum):
    """
    Human hair color phenotypes
    """
    # Enum members
    BLACK = "BLACK"
    BROWN = "BROWN"
    DARK_BROWN = "DARK_BROWN"
    LIGHT_BROWN = "LIGHT_BROWN"
    BLONDE = "BLONDE"
    DARK_BLONDE = "DARK_BLONDE"
    LIGHT_BLONDE = "LIGHT_BLONDE"
    PLATINUM_BLONDE = "PLATINUM_BLONDE"
    STRAWBERRY_BLONDE = "STRAWBERRY_BLONDE"
    RED = "RED"
    AUBURN = "AUBURN"
    GINGER = "GINGER"
    GRAY = "GRAY"
    WHITE = "WHITE"
    SILVER = "SILVER"

# Set metadata after class creation
HairColorEnum._metadata = {
    "BLACK": {'description': 'Black hair', 'annotations': {'hex': '000000', 'prevalence': 'most common worldwide'}},
    "BROWN": {'description': 'Brown hair', 'annotations': {'hex_range': '654321-8B4513'}},
    "DARK_BROWN": {'description': 'Dark brown hair', 'annotations': {'hex': '3B2F2F'}},
    "LIGHT_BROWN": {'description': 'Light brown hair', 'annotations': {'hex': '977961'}},
    "BLONDE": {'description': 'Blonde/blond hair', 'meaning': 'HP:0002286', 'annotations': {'hex_range': 'FAF0BE-FFF8DC'}},
    "DARK_BLONDE": {'description': 'Dark blonde hair', 'annotations': {'hex': '9F8F71'}},
    "LIGHT_BLONDE": {'description': 'Light blonde hair', 'annotations': {'hex': 'FFF8DC'}},
    "PLATINUM_BLONDE": {'description': 'Platinum blonde hair', 'annotations': {'hex': 'E5E5E5'}},
    "STRAWBERRY_BLONDE": {'description': 'Strawberry blonde hair', 'annotations': {'hex': 'FF9966'}},
    "RED": {'description': 'Red hair', 'meaning': 'HP:0002297', 'annotations': {'hex_range': '922724-FF4500', 'prevalence': '1-2% worldwide'}},
    "AUBURN": {'description': 'Auburn hair (reddish-brown)', 'annotations': {'hex': 'A52A2A'}},
    "GINGER": {'description': 'Ginger hair (orange-red)', 'annotations': {'hex': 'FF6600'}},
    "GRAY": {'description': 'Gray hair', 'meaning': 'HP:0002216', 'annotations': {'hex_range': '808080-C0C0C0'}},
    "WHITE": {'description': 'White hair', 'meaning': 'HP:0011364', 'annotations': {'hex': 'FFFFFF'}},
    "SILVER": {'description': 'Silver hair', 'annotations': {'hex': 'C0C0C0'}},
}

class FlowerColorEnum(RichEnum):
    """
    Common flower colors
    """
    # Enum members
    RED = "RED"
    PINK = "PINK"
    ORANGE = "ORANGE"
    YELLOW = "YELLOW"
    WHITE = "WHITE"
    PURPLE = "PURPLE"
    VIOLET = "VIOLET"
    BLUE = "BLUE"
    LAVENDER = "LAVENDER"
    MAGENTA = "MAGENTA"
    BURGUNDY = "BURGUNDY"
    CORAL = "CORAL"
    PEACH = "PEACH"
    CREAM = "CREAM"
    BICOLOR = "BICOLOR"
    MULTICOLOR = "MULTICOLOR"

# Set metadata after class creation
FlowerColorEnum._metadata = {
    "RED": {'description': 'Red flowers', 'annotations': {'hex': 'FF0000', 'examples': 'roses, tulips, poppies'}},
    "PINK": {'description': 'Pink flowers', 'annotations': {'hex': 'FFC0CB', 'examples': 'peonies, cherry blossoms'}},
    "ORANGE": {'description': 'Orange flowers', 'annotations': {'hex': 'FFA500', 'examples': 'marigolds, zinnias'}},
    "YELLOW": {'description': 'Yellow flowers', 'annotations': {'hex': 'FFFF00', 'examples': 'sunflowers, daffodils'}},
    "WHITE": {'description': 'White flowers', 'annotations': {'hex': 'FFFFFF', 'examples': 'lilies, daisies'}},
    "PURPLE": {'description': 'Purple flowers', 'annotations': {'hex': '800080', 'examples': 'lavender, violets'}},
    "VIOLET": {'description': 'Violet flowers', 'annotations': {'hex': '7F00FF', 'examples': 'violets, pansies'}},
    "BLUE": {'description': 'Blue flowers', 'annotations': {'hex': '0000FF', 'examples': 'forget-me-nots, cornflowers'}},
    "LAVENDER": {'description': 'Lavender flowers', 'annotations': {'hex': 'E6E6FA', 'examples': 'lavender, wisteria'}},
    "MAGENTA": {'description': 'Magenta flowers', 'annotations': {'hex': 'FF00FF', 'examples': 'fuchsias, bougainvillea'}},
    "BURGUNDY": {'description': 'Burgundy/deep red flowers', 'annotations': {'hex': '800020', 'examples': 'dahlias, chrysanthemums'}},
    "CORAL": {'description': 'Coral flowers', 'annotations': {'hex': 'FF7F50', 'examples': 'coral bells, begonias'}},
    "PEACH": {'description': 'Peach flowers', 'annotations': {'hex': 'FFDAB9', 'examples': 'roses, dahlias'}},
    "CREAM": {'description': 'Cream flowers', 'annotations': {'hex': 'FFFDD0', 'examples': 'roses, tulips'}},
    "BICOLOR": {'description': 'Two-colored flowers', 'annotations': {'note': 'flowers with two distinct colors'}},
    "MULTICOLOR": {'description': 'Multi-colored flowers', 'annotations': {'note': 'flowers with more than two colors'}},
}

class AnimalCoatColorEnum(RichEnum):
    """
    Animal coat/fur colors
    """
    # Enum members
    BLACK = "BLACK"
    WHITE = "WHITE"
    BROWN = "BROWN"
    TAN = "TAN"
    CREAM = "CREAM"
    GRAY = "GRAY"
    RED = "RED"
    GOLDEN = "GOLDEN"
    FAWN = "FAWN"
    BRINDLE = "BRINDLE"
    SPOTTED = "SPOTTED"
    MERLE = "MERLE"
    PIEBALD = "PIEBALD"
    CALICO = "CALICO"
    TABBY = "TABBY"
    TORTOISESHELL = "TORTOISESHELL"
    ROAN = "ROAN"
    PALOMINO = "PALOMINO"
    CHESTNUT = "CHESTNUT"
    BAY = "BAY"

# Set metadata after class creation
AnimalCoatColorEnum._metadata = {
    "BLACK": {'description': 'Black coat', 'annotations': {'hex': '000000'}},
    "WHITE": {'description': 'White coat', 'annotations': {'hex': 'FFFFFF'}},
    "BROWN": {'description': 'Brown coat', 'annotations': {'hex': '964B00'}},
    "TAN": {'description': 'Tan coat', 'annotations': {'hex': 'D2B48C'}},
    "CREAM": {'description': 'Cream coat', 'annotations': {'hex': 'FFFDD0'}},
    "GRAY": {'description': 'Gray coat', 'annotations': {'hex': '808080'}},
    "RED": {'description': 'Red/rust coat', 'annotations': {'hex': 'B22222'}},
    "GOLDEN": {'description': 'Golden coat', 'annotations': {'hex': 'FFD700'}},
    "FAWN": {'description': 'Fawn coat', 'annotations': {'hex': 'E5AA70'}},
    "BRINDLE": {'description': 'Brindle pattern (striped)', 'annotations': {'pattern': 'striped mixture of colors'}},
    "SPOTTED": {'description': 'Spotted pattern', 'annotations': {'pattern': 'spots on base color'}},
    "MERLE": {'description': 'Merle pattern (mottled)', 'annotations': {'pattern': 'mottled patches'}},
    "PIEBALD": {'description': 'Piebald pattern (patches)', 'annotations': {'pattern': 'irregular patches'}},
    "CALICO": {'description': 'Calico pattern (tri-color)', 'annotations': {'pattern': 'tri-color patches', 'species': 'primarily cats'}},
    "TABBY": {'description': 'Tabby pattern (striped)', 'annotations': {'pattern': 'striped or spotted', 'species': 'primarily cats'}},
    "TORTOISESHELL": {'description': 'Tortoiseshell pattern', 'annotations': {'pattern': 'mottled orange and black', 'species': 'primarily cats'}},
    "ROAN": {'description': 'Roan pattern (mixed white)', 'annotations': {'pattern': 'white mixed with base color', 'species': 'primarily horses'}},
    "PALOMINO": {'description': 'Palomino (golden with white mane)', 'annotations': {'hex': 'DEC05F', 'species': 'horses'}},
    "CHESTNUT": {'description': 'Chestnut/sorrel', 'annotations': {'hex': 'CD5C5C', 'species': 'horses'}},
    "BAY": {'description': 'Bay (brown with black points)', 'annotations': {'species': 'horses'}},
}

class SkinToneEnum(RichEnum):
    """
    Human skin tone classifications (Fitzpatrick scale based)
    """
    # Enum members
    TYPE_I = "TYPE_I"
    TYPE_II = "TYPE_II"
    TYPE_III = "TYPE_III"
    TYPE_IV = "TYPE_IV"
    TYPE_V = "TYPE_V"
    TYPE_VI = "TYPE_VI"

# Set metadata after class creation
SkinToneEnum._metadata = {
    "TYPE_I": {'description': 'Very pale white skin', 'annotations': {'fitzpatrick': 'Type I', 'hex_range': 'FFE0BD-FFDFC4', 'sun_reaction': 'always burns, never tans'}},
    "TYPE_II": {'description': 'Fair white skin', 'annotations': {'fitzpatrick': 'Type II', 'hex_range': 'F0D5BE-E8C5A0', 'sun_reaction': 'burns easily, tans minimally'}},
    "TYPE_III": {'description': 'Light brown skin', 'annotations': {'fitzpatrick': 'Type III', 'hex_range': 'DDA582-CD9766', 'sun_reaction': 'burns moderately, tans gradually'}},
    "TYPE_IV": {'description': 'Moderate brown skin', 'annotations': {'fitzpatrick': 'Type IV', 'hex_range': 'B87659-A47148', 'sun_reaction': 'burns minimally, tans easily'}},
    "TYPE_V": {'description': 'Dark brown skin', 'annotations': {'fitzpatrick': 'Type V', 'hex_range': '935D37-7C4E2A', 'sun_reaction': 'rarely burns, tans darkly'}},
    "TYPE_VI": {'description': 'Very dark brown to black skin', 'annotations': {'fitzpatrick': 'Type VI', 'hex_range': '5C3A1E-3D2314', 'sun_reaction': 'never burns, always tans darkly'}},
}

class PlantLeafColorEnum(RichEnum):
    """
    Plant leaf colors (including seasonal changes)
    """
    # Enum members
    GREEN = "GREEN"
    DARK_GREEN = "DARK_GREEN"
    LIGHT_GREEN = "LIGHT_GREEN"
    YELLOW_GREEN = "YELLOW_GREEN"
    YELLOW = "YELLOW"
    ORANGE = "ORANGE"
    RED = "RED"
    PURPLE = "PURPLE"
    BRONZE = "BRONZE"
    SILVER = "SILVER"
    VARIEGATED = "VARIEGATED"
    BROWN = "BROWN"

# Set metadata after class creation
PlantLeafColorEnum._metadata = {
    "GREEN": {'description': 'Green leaves (healthy/summer)', 'meaning': 'PATO:0000320', 'annotations': {'hex_range': '228B22-90EE90', 'season': 'spring/summer'}},
    "DARK_GREEN": {'description': 'Dark green leaves', 'annotations': {'hex': '006400'}},
    "LIGHT_GREEN": {'description': 'Light green leaves', 'annotations': {'hex': '90EE90'}},
    "YELLOW_GREEN": {'description': 'Yellow-green leaves', 'annotations': {'hex': '9ACD32', 'condition': 'new growth or nutrient deficiency'}},
    "YELLOW": {'description': 'Yellow leaves (autumn or chlorosis)', 'meaning': 'PATO:0000324', 'annotations': {'hex': 'FFD700', 'season': 'autumn'}},
    "ORANGE": {'description': 'Orange leaves (autumn)', 'annotations': {'hex': 'FF8C00', 'season': 'autumn'}},
    "RED": {'description': 'Red leaves (autumn or certain species)', 'meaning': 'PATO:0000322', 'annotations': {'hex': 'DC143C', 'season': 'autumn'}},
    "PURPLE": {'description': 'Purple leaves (certain species)', 'annotations': {'hex': '800080', 'examples': 'purple basil, Japanese maple'}},
    "BRONZE": {'description': 'Bronze leaves', 'annotations': {'hex': 'CD7F32'}},
    "SILVER": {'description': 'Silver/gray leaves', 'annotations': {'hex': 'C0C0C0', 'examples': 'dusty miller, artemisia'}},
    "VARIEGATED": {'description': 'Variegated leaves (multiple colors)', 'annotations': {'pattern': 'mixed colors/patterns'}},
    "BROWN": {'description': 'Brown leaves (dead/dying)', 'annotations': {'hex': '964B00', 'condition': 'senescent or dead'}},
}

__all__ = [
    "EyeColorEnum",
    "HairColorEnum",
    "FlowerColorEnum",
    "AnimalCoatColorEnum",
    "SkinToneEnum",
    "PlantLeafColorEnum",
]