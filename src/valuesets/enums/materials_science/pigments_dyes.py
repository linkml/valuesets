"""
Pigments and Dyes Color Value Sets

Color value sets for pigments, dyes, paints, and other colorant materials used in art, industry, and manufacturing.


Generated from: materials_science/pigments_dyes.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class TraditionalPigmentEnum(RichEnum):
    """
    Traditional artist pigments and their colors
    """
    # Enum members
    TITANIUM_WHITE = "TITANIUM_WHITE"
    ZINC_WHITE = "ZINC_WHITE"
    LEAD_WHITE = "LEAD_WHITE"
    CADMIUM_YELLOW = "CADMIUM_YELLOW"
    CHROME_YELLOW = "CHROME_YELLOW"
    NAPLES_YELLOW = "NAPLES_YELLOW"
    YELLOW_OCHRE = "YELLOW_OCHRE"
    CADMIUM_ORANGE = "CADMIUM_ORANGE"
    CADMIUM_RED = "CADMIUM_RED"
    VERMILION = "VERMILION"
    ALIZARIN_CRIMSON = "ALIZARIN_CRIMSON"
    CARMINE = "CARMINE"
    BURNT_SIENNA = "BURNT_SIENNA"
    RAW_SIENNA = "RAW_SIENNA"
    BURNT_UMBER = "BURNT_UMBER"
    RAW_UMBER = "RAW_UMBER"
    VAN_DYKE_BROWN = "VAN_DYKE_BROWN"
    PRUSSIAN_BLUE = "PRUSSIAN_BLUE"
    ULTRAMARINE = "ULTRAMARINE"
    COBALT_BLUE = "COBALT_BLUE"
    CERULEAN_BLUE = "CERULEAN_BLUE"
    PHTHALO_BLUE = "PHTHALO_BLUE"
    VIRIDIAN = "VIRIDIAN"
    CHROME_GREEN = "CHROME_GREEN"
    PHTHALO_GREEN = "PHTHALO_GREEN"
    TERRE_VERTE = "TERRE_VERTE"
    TYRIAN_PURPLE = "TYRIAN_PURPLE"
    MANGANESE_VIOLET = "MANGANESE_VIOLET"
    MARS_BLACK = "MARS_BLACK"
    IVORY_BLACK = "IVORY_BLACK"
    LAMP_BLACK = "LAMP_BLACK"

# Set metadata after class creation
TraditionalPigmentEnum._metadata = {
    "TITANIUM_WHITE": {'description': 'Titanium white (Titanium dioxide)', 'meaning': 'CHEBI:51050', 'annotations': {'hex': 'FFFFFF', 'chemical': 'TiO2', 'discovered': '1916'}},
    "ZINC_WHITE": {'description': 'Zinc white (Zinc oxide)', 'meaning': 'CHEBI:36560', 'annotations': {'hex': 'FEFEFE', 'chemical': 'ZnO'}},
    "LEAD_WHITE": {'description': 'Lead white (Basic lead carbonate) - toxic', 'annotations': {'hex': 'F8F8F8', 'chemical': '2PbCO3·Pb(OH)2', 'warning': 'highly toxic, historical use'}},
    "CADMIUM_YELLOW": {'description': 'Cadmium yellow (Cadmium sulfide)', 'meaning': 'CHEBI:50834', 'annotations': {'hex': 'FFF600', 'chemical': 'CdS', 'warning': 'toxic'}},
    "CHROME_YELLOW": {'description': 'Chrome yellow (Lead chromate) - toxic', 'annotations': {'hex': 'FFC200', 'chemical': 'PbCrO4', 'warning': 'highly toxic'}},
    "NAPLES_YELLOW": {'description': 'Naples yellow (Lead antimonate)', 'annotations': {'hex': 'FDD5B1', 'chemical': 'Pb(SbO3)2', 'historical': 'ancient pigment'}},
    "YELLOW_OCHRE": {'description': 'Yellow ochre (Iron oxide hydroxide)', 'annotations': {'hex': 'CC7722', 'chemical': 'FeO(OH)·nH2O', 'natural': 'earth pigment'}},
    "CADMIUM_ORANGE": {'description': 'Cadmium orange (Cadmium selenide)', 'annotations': {'hex': 'FF6600', 'chemical': 'CdS·CdSe', 'warning': 'toxic'}},
    "CADMIUM_RED": {'description': 'Cadmium red (Cadmium selenide)', 'meaning': 'CHEBI:50835', 'annotations': {'hex': 'E30022', 'chemical': 'CdSe', 'warning': 'toxic'}},
    "VERMILION": {'description': 'Vermilion/Cinnabar (Mercury sulfide)', 'annotations': {'hex': 'E34234', 'chemical': 'HgS', 'warning': 'highly toxic'}},
    "ALIZARIN_CRIMSON": {'description': 'Alizarin crimson (synthetic)', 'meaning': 'CHEBI:16866', 'annotations': {'hex': 'E32636', 'chemical': 'C14H8O4', 'organic': 'synthetic organic'}},
    "CARMINE": {'description': 'Carmine (from cochineal insects)', 'annotations': {'hex': '960018', 'source': 'cochineal insects', 'natural': 'organic pigment'}},
    "BURNT_SIENNA": {'description': 'Burnt sienna (heated iron oxide)', 'annotations': {'hex': 'E97451', 'chemical': 'Fe2O3', 'process': 'calcined raw sienna'}},
    "RAW_SIENNA": {'description': 'Raw sienna (Iron oxide with clay)', 'annotations': {'hex': 'C69D52', 'chemical': 'Fe2O3 with clay', 'natural': 'earth pigment'}},
    "BURNT_UMBER": {'description': 'Burnt umber (heated iron/manganese oxide)', 'annotations': {'hex': '8B4513', 'chemical': 'Fe2O3 + MnO2', 'process': 'calcined raw umber'}},
    "RAW_UMBER": {'description': 'Raw umber (Iron/manganese oxide)', 'annotations': {'hex': '734A12', 'chemical': 'Fe2O3 + MnO2', 'natural': 'earth pigment'}},
    "VAN_DYKE_BROWN": {'description': 'Van Dyke brown (organic earth)', 'annotations': {'hex': '664228', 'source': 'peat, lignite', 'warning': 'fugitive color'}},
    "PRUSSIAN_BLUE": {'description': 'Prussian blue (Ferric ferrocyanide)', 'meaning': 'CHEBI:30069', 'annotations': {'hex': '003153', 'chemical': 'Fe4[Fe(CN)6]3', 'discovered': '1706'}},
    "ULTRAMARINE": {'description': 'Ultramarine blue (originally lapis lazuli)', 'annotations': {'hex': '120A8F', 'chemical': 'Na8[Al6Si6O24]Sn', 'historical': 'most expensive pigment'}},
    "COBALT_BLUE": {'description': 'Cobalt blue (Cobalt aluminate)', 'annotations': {'hex': '0047AB', 'chemical': 'CoAl2O4'}},
    "CERULEAN_BLUE": {'description': 'Cerulean blue (Cobalt stannate)', 'annotations': {'hex': '2A52BE', 'chemical': 'Co2SnO4'}},
    "PHTHALO_BLUE": {'description': 'Phthalocyanine blue', 'annotations': {'hex': '000F89', 'chemical': 'C32H16CuN8', 'modern': 'synthetic organic'}},
    "VIRIDIAN": {'description': 'Viridian (Chromium oxide green)', 'annotations': {'hex': '40826D', 'chemical': 'Cr2O3·2H2O'}},
    "CHROME_GREEN": {'description': 'Chrome oxide green', 'annotations': {'hex': '2E5E26', 'chemical': 'Cr2O3'}},
    "PHTHALO_GREEN": {'description': 'Phthalocyanine green', 'annotations': {'hex': '123524', 'chemical': 'C32H16ClCuN8', 'modern': 'synthetic organic'}},
    "TERRE_VERTE": {'description': 'Terre verte/Green earth', 'annotations': {'hex': '6B7F59', 'chemical': 'complex silicate', 'natural': 'earth pigment'}},
    "TYRIAN_PURPLE": {'description': 'Tyrian purple (from murex snails)', 'annotations': {'hex': '66023C', 'source': 'murex snails', 'historical': 'ancient royal purple'}},
    "MANGANESE_VIOLET": {'description': 'Manganese violet', 'annotations': {'hex': '8B3E5F', 'chemical': 'NH4MnP2O7'}},
    "MARS_BLACK": {'description': 'Mars black (Synthetic iron oxide)', 'annotations': {'hex': '010101', 'chemical': 'Fe3O4', 'synthetic': 'iron oxide'}},
    "IVORY_BLACK": {'description': 'Ivory black (Bone char)', 'annotations': {'hex': '1B1B1B', 'source': 'charred bones'}},
    "LAMP_BLACK": {'description': 'Lamp black (Carbon black)', 'annotations': {'hex': '2B2B2B', 'chemical': 'C', 'source': 'soot'}},
}

class IndustrialDyeEnum(RichEnum):
    """
    Industrial and textile dyes
    """
    # Enum members
    INDIGO = "INDIGO"
    ANILINE_BLACK = "ANILINE_BLACK"
    METHYLENE_BLUE = "METHYLENE_BLUE"
    CONGO_RED = "CONGO_RED"
    MALACHITE_GREEN = "MALACHITE_GREEN"
    CRYSTAL_VIOLET = "CRYSTAL_VIOLET"
    EOSIN = "EOSIN"
    SAFRANIN = "SAFRANIN"
    ACID_ORANGE_7 = "ACID_ORANGE_7"
    REACTIVE_BLACK_5 = "REACTIVE_BLACK_5"
    DISPERSE_BLUE_1 = "DISPERSE_BLUE_1"
    VAT_BLUE_1 = "VAT_BLUE_1"

# Set metadata after class creation
IndustrialDyeEnum._metadata = {
    "INDIGO": {'description': 'Indigo dye', 'annotations': {'hex': '4B0082', 'source': 'originally plant-based, now synthetic', 'use': 'denim, textiles'}},
    "ANILINE_BLACK": {'description': 'Aniline black', 'annotations': {'hex': '000000', 'chemical': 'polyaniline', 'use': 'cotton dyeing'}},
    "METHYLENE_BLUE": {'description': 'Methylene blue', 'annotations': {'hex': '1E90FF', 'chemical': 'C16H18ClN3S', 'use': 'biological stain, medical'}},
    "CONGO_RED": {'description': 'Congo red', 'meaning': 'CHEBI:34653', 'annotations': {'hex': 'CC0000', 'chemical': 'C32H22N6Na2O6S2', 'use': 'pH indicator, textile'}},
    "MALACHITE_GREEN": {'description': 'Malachite green', 'meaning': 'CHEBI:72449', 'annotations': {'hex': '0BDA51', 'chemical': 'C23H25ClN2', 'use': 'biological stain'}},
    "CRYSTAL_VIOLET": {'description': 'Crystal violet/Gentian violet', 'meaning': 'CHEBI:41688', 'annotations': {'hex': '9400D3', 'chemical': 'C25H30ClN3', 'use': 'gram staining'}},
    "EOSIN": {'description': 'Eosin Y', 'meaning': 'CHEBI:52053', 'annotations': {'hex': 'FF6B6B', 'chemical': 'C20H6Br4Na2O5', 'use': 'histology stain'}, 'aliases': ['eosin YS dye']},
    "SAFRANIN": {'description': 'Safranin O', 'annotations': {'hex': 'FF0066', 'chemical': 'C20H19ClN4', 'use': 'biological stain'}},
    "ACID_ORANGE_7": {'description': 'Acid Orange 7 (Orange II)', 'annotations': {'hex': 'FF7F00', 'chemical': 'C16H11N2NaO4S', 'use': 'wool, silk dyeing'}},
    "REACTIVE_BLACK_5": {'description': 'Reactive Black 5', 'annotations': {'hex': '000000', 'use': 'cotton reactive dye'}},
    "DISPERSE_BLUE_1": {'description': 'Disperse Blue 1', 'annotations': {'hex': '1560BD', 'use': 'polyester dyeing'}},
    "VAT_BLUE_1": {'description': 'Vat Blue 1 (Indanthrene blue)', 'annotations': {'hex': '002F5C', 'use': 'cotton vat dyeing'}},
}

class FoodColoringEnum(RichEnum):
    """
    Food coloring and natural food dyes
    """
    # Enum members
    FD_C_RED_40 = "FD_C_RED_40"
    FD_C_YELLOW_5 = "FD_C_YELLOW_5"
    FD_C_YELLOW_6 = "FD_C_YELLOW_6"
    FD_C_BLUE_1 = "FD_C_BLUE_1"
    FD_C_BLUE_2 = "FD_C_BLUE_2"
    FD_C_GREEN_3 = "FD_C_GREEN_3"
    CARAMEL_COLOR = "CARAMEL_COLOR"
    ANNATTO = "ANNATTO"
    TURMERIC = "TURMERIC"
    BEETROOT_RED = "BEETROOT_RED"
    CHLOROPHYLL = "CHLOROPHYLL"
    ANTHOCYANINS = "ANTHOCYANINS"
    PAPRIKA_EXTRACT = "PAPRIKA_EXTRACT"
    SPIRULINA_BLUE = "SPIRULINA_BLUE"

# Set metadata after class creation
FoodColoringEnum._metadata = {
    "FD_C_RED_40": {'description': 'FD&C Red No. 40 (Allura Red)', 'annotations': {'hex': 'E40000', 'E_number': 'E129', 'use': 'beverages, candies'}},
    "FD_C_YELLOW_5": {'description': 'FD&C Yellow No. 5 (Tartrazine)', 'annotations': {'hex': 'FFFF00', 'E_number': 'E102', 'use': 'beverages, desserts'}},
    "FD_C_YELLOW_6": {'description': 'FD&C Yellow No. 6 (Sunset Yellow)', 'annotations': {'hex': 'FFA500', 'E_number': 'E110', 'use': 'snacks, beverages'}},
    "FD_C_BLUE_1": {'description': 'FD&C Blue No. 1 (Brilliant Blue)', 'meaning': 'CHEBI:82411', 'annotations': {'hex': '0033FF', 'E_number': 'E133', 'use': 'beverages, candies'}},
    "FD_C_BLUE_2": {'description': 'FD&C Blue No. 2 (Indigo Carmine)', 'annotations': {'hex': '4B0082', 'E_number': 'E132', 'use': 'beverages, confections'}},
    "FD_C_GREEN_3": {'description': 'FD&C Green No. 3 (Fast Green)', 'annotations': {'hex': '00FF00', 'E_number': 'E143', 'use': 'beverages, desserts'}},
    "CARAMEL_COLOR": {'description': 'Caramel coloring', 'annotations': {'hex': '8B4513', 'E_number': 'E150', 'use': 'cola, sauces'}},
    "ANNATTO": {'description': 'Annatto (natural orange)', 'meaning': 'CHEBI:3136', 'annotations': {'hex': 'FF6600', 'E_number': 'E160b', 'source': 'achiote seeds'}, 'aliases': ['bixin']},
    "TURMERIC": {'description': 'Turmeric/Curcumin (natural yellow)', 'meaning': 'CHEBI:3962', 'annotations': {'hex': 'F0E442', 'E_number': 'E100', 'source': 'turmeric root'}},
    "BEETROOT_RED": {'description': 'Beetroot red/Betanin', 'meaning': 'CHEBI:3080', 'annotations': {'hex': 'BC2A4D', 'E_number': 'E162', 'source': 'beets'}, 'aliases': ['Betanin']},
    "CHLOROPHYLL": {'description': 'Chlorophyll (natural green)', 'meaning': 'CHEBI:28966', 'annotations': {'hex': '4D7C0F', 'E_number': 'E140', 'source': 'plants'}},
    "ANTHOCYANINS": {'description': 'Anthocyanins (natural purple/red)', 'annotations': {'hex': '6B3AA0', 'E_number': 'E163', 'source': 'berries, grapes'}},
    "PAPRIKA_EXTRACT": {'description': 'Paprika extract', 'annotations': {'hex': 'E85D00', 'E_number': 'E160c', 'source': 'paprika peppers'}},
    "SPIRULINA_BLUE": {'description': 'Spirulina extract (phycocyanin)', 'annotations': {'hex': '1E88E5', 'source': 'spirulina algae', 'natural': 'true'}},
}

class AutomobilePaintColorEnum(RichEnum):
    """
    Common automobile paint colors
    """
    # Enum members
    ARCTIC_WHITE = "ARCTIC_WHITE"
    MIDNIGHT_BLACK = "MIDNIGHT_BLACK"
    SILVER_METALLIC = "SILVER_METALLIC"
    GUNMETAL_GRAY = "GUNMETAL_GRAY"
    RACING_RED = "RACING_RED"
    CANDY_APPLE_RED = "CANDY_APPLE_RED"
    ELECTRIC_BLUE = "ELECTRIC_BLUE"
    BRITISH_RACING_GREEN = "BRITISH_RACING_GREEN"
    PEARL_WHITE = "PEARL_WHITE"
    CHAMPAGNE_GOLD = "CHAMPAGNE_GOLD"
    COPPER_BRONZE = "COPPER_BRONZE"
    MIAMI_BLUE = "MIAMI_BLUE"

# Set metadata after class creation
AutomobilePaintColorEnum._metadata = {
    "ARCTIC_WHITE": {'description': 'Arctic White', 'meaning': 'HEX:FFFFFF', 'annotations': {'type': 'solid'}},
    "MIDNIGHT_BLACK": {'description': 'Midnight Black', 'meaning': 'HEX:000000', 'annotations': {'type': 'metallic'}},
    "SILVER_METALLIC": {'description': 'Silver Metallic', 'meaning': 'HEX:C0C0C0', 'annotations': {'type': 'metallic'}},
    "GUNMETAL_GRAY": {'description': 'Gunmetal Gray', 'meaning': 'HEX:2A3439', 'annotations': {'type': 'metallic'}},
    "RACING_RED": {'description': 'Racing Red', 'meaning': 'HEX:CE1620', 'annotations': {'type': 'solid'}},
    "CANDY_APPLE_RED": {'description': 'Candy Apple Red', 'meaning': 'HEX:FF0800', 'annotations': {'type': 'metallic'}},
    "ELECTRIC_BLUE": {'description': 'Electric Blue', 'meaning': 'HEX:7DF9FF', 'annotations': {'type': 'metallic'}},
    "BRITISH_RACING_GREEN": {'description': 'British Racing Green', 'meaning': 'HEX:004225', 'annotations': {'type': 'solid', 'historical': 'British racing color'}},
    "PEARL_WHITE": {'description': 'Pearl White', 'meaning': 'HEX:F8F8FF', 'annotations': {'type': 'pearl', 'finish': 'pearlescent'}},
    "CHAMPAGNE_GOLD": {'description': 'Champagne Gold', 'meaning': 'HEX:D4AF37', 'annotations': {'type': 'metallic'}},
    "COPPER_BRONZE": {'description': 'Copper Bronze', 'meaning': 'HEX:B87333', 'annotations': {'type': 'metallic'}},
    "MIAMI_BLUE": {'description': 'Miami Blue', 'meaning': 'HEX:00BFFF', 'annotations': {'type': 'metallic', 'brand': 'Porsche'}},
}

__all__ = [
    "TraditionalPigmentEnum",
    "IndustrialDyeEnum",
    "FoodColoringEnum",
    "AutomobilePaintColorEnum",
]