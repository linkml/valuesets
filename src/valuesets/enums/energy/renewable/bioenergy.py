"""
Bioenergy and Biofuels Value Sets

Value sets for bioenergy feedstocks, biofuels, and conversion processes. Based on DOE Bioenergy Technologies Office terminology and glossary.

Generated from: energy/renewable/bioenergy.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class BiomassFeedstockType(RichEnum):
    """
    Types of biomass materials used as feedstocks for bioenergy production. Includes dedicated energy crops, agricultural residues, forest residues, and waste streams.
    """
    # Enum members
    CORN_STOVER = "CORN_STOVER"
    WHEAT_STRAW = "WHEAT_STRAW"
    RICE_STRAW = "RICE_STRAW"
    SWITCHGRASS = "SWITCHGRASS"
    MISCANTHUS = "MISCANTHUS"
    ENERGY_CANE = "ENERGY_CANE"
    SWEET_SORGHUM = "SWEET_SORGHUM"
    POPLAR = "POPLAR"
    WILLOW = "WILLOW"
    FOREST_RESIDUE = "FOREST_RESIDUE"
    WOOD_PROCESSING_RESIDUE = "WOOD_PROCESSING_RESIDUE"
    MUNICIPAL_SOLID_WASTE = "MUNICIPAL_SOLID_WASTE"
    FOOD_WASTE = "FOOD_WASTE"
    ANIMAL_MANURE = "ANIMAL_MANURE"
    ALGAE = "ALGAE"
    USED_COOKING_OIL = "USED_COOKING_OIL"
    SOYBEAN_OIL = "SOYBEAN_OIL"
    CORN_GRAIN = "CORN_GRAIN"
    SUGARCANE = "SUGARCANE"

# Set metadata after class creation
BiomassFeedstockType._metadata = {
    "CORN_STOVER": {'description': 'Agricultural residue consisting of leaves, stalks, and cobs remaining after corn grain harvest.', 'annotations': {'category': 'agricultural_residue', 'lignocellulosic': True}, 'aliases': ['Corn Residue']},
    "WHEAT_STRAW": {'description': 'Agricultural residue remaining after wheat grain harvest.', 'annotations': {'category': 'agricultural_residue', 'lignocellulosic': True}},
    "RICE_STRAW": {'description': 'Agricultural residue remaining after rice grain harvest.', 'annotations': {'category': 'agricultural_residue', 'lignocellulosic': True}},
    "SWITCHGRASS": {'description': 'Perennial warm-season grass native to North America, cultivated as dedicated energy crop for cellulosic biofuel production.', 'annotations': {'category': 'energy_crop', 'lignocellulosic': True, 'perennial': True}},
    "MISCANTHUS": {'description': 'High-yielding perennial grass cultivated as dedicated energy crop.', 'annotations': {'category': 'energy_crop', 'lignocellulosic': True, 'perennial': True}, 'aliases': ['Elephant Grass']},
    "ENERGY_CANE": {'description': 'High-fiber sugarcane varieties bred for biomass production rather than sugar content.', 'annotations': {'category': 'energy_crop', 'lignocellulosic': True}},
    "SWEET_SORGHUM": {'description': 'Sorghum variety with high sugar content in stalks, suitable for both sugar and lignocellulosic conversion.', 'annotations': {'category': 'energy_crop', 'sugar_crop': True}},
    "POPLAR": {'description': 'Fast-growing hardwood tree cultivated as short-rotation woody crop for biomass.', 'annotations': {'category': 'woody_crop', 'lignocellulosic': True}, 'aliases': ['Hybrid Poplar']},
    "WILLOW": {'description': 'Fast-growing shrub cultivated as short-rotation woody crop.', 'annotations': {'category': 'woody_crop', 'lignocellulosic': True}, 'aliases': ['Shrub Willow']},
    "FOREST_RESIDUE": {'description': 'Biomass from forest operations including logging residues, thinning material, and salvage timber.', 'annotations': {'category': 'forestry_residue', 'lignocellulosic': True}, 'aliases': ['Logging Residue']},
    "WOOD_PROCESSING_RESIDUE": {'description': 'Byproducts from wood processing including sawdust, bark, shavings, and wood chips.', 'annotations': {'category': 'processing_residue', 'lignocellulosic': True}, 'aliases': ['Mill Residue']},
    "MUNICIPAL_SOLID_WASTE": {'description': 'Organic portion of municipal solid waste suitable for bioenergy conversion.', 'annotations': {'category': 'waste'}, 'aliases': ['MSW']},
    "FOOD_WASTE": {'description': 'Waste food from residential, commercial, and industrial sources.', 'annotations': {'category': 'wet_waste'}},
    "ANIMAL_MANURE": {'description': 'Livestock waste including cattle, swine, and poultry manure.', 'annotations': {'category': 'wet_waste', 'biogas_suitable': True}},
    "ALGAE": {'description': 'Microalgae or macroalgae cultivated for lipid or carbohydrate content for biofuel production.', 'annotations': {'category': 'aquatic_biomass', 'lipid_rich': True}, 'aliases': ['Microalgae']},
    "USED_COOKING_OIL": {'description': 'Waste vegetable oils from food preparation.', 'annotations': {'category': 'waste', 'lipid_rich': True}, 'aliases': ['UCO', 'Waste Vegetable Oil']},
    "SOYBEAN_OIL": {'description': 'Vegetable oil from soybean seeds, used for biodiesel.', 'meaning': 'CHEBI:166975', 'annotations': {'category': 'oil_crop', 'lipid_rich': True}},
    "CORN_GRAIN": {'description': 'Corn kernels used for starch-based ethanol production.', 'annotations': {'category': 'grain', 'starch_crop': True}},
    "SUGARCANE": {'description': 'Sugar-rich crop used for first-generation ethanol production.', 'annotations': {'category': 'sugar_crop'}},
}

class BiofuelType(RichEnum):
    """
    Types of fuels produced from biomass feedstocks.
    """
    # Enum members
    ETHANOL = "ETHANOL"
    BIODIESEL = "BIODIESEL"
    RENEWABLE_DIESEL = "RENEWABLE_DIESEL"
    SUSTAINABLE_AVIATION_FUEL = "SUSTAINABLE_AVIATION_FUEL"
    BIOGAS = "BIOGAS"
    BIOMETHANE = "BIOMETHANE"
    BIO_OIL = "BIO_OIL"
    SYNGAS = "SYNGAS"
    BUTANOL = "BUTANOL"
    METHANOL = "METHANOL"
    DIMETHYL_ETHER = "DIMETHYL_ETHER"

# Set metadata after class creation
BiofuelType._metadata = {
    "ETHANOL": {'description': 'Alcohol biofuel (C2H5OH) produced by fermentation of sugars or starches, or from cellulosic biomass.', 'meaning': 'CHEBI:16236', 'annotations': {'chemical_formula': 'C2H5OH'}, 'aliases': ['Fuel Ethanol', 'Bioethanol']},
    "BIODIESEL": {'description': 'Fatty acid methyl esters (FAME) produced by transesterification of vegetable oils or animal fats.', 'annotations': {'production_method': 'transesterification'}, 'aliases': ['FAME']},
    "RENEWABLE_DIESEL": {'description': 'Hydrocarbon diesel produced by hydrotreating lipids. Chemically identical to petroleum diesel.', 'annotations': {'drop_in_fuel': True}, 'aliases': ['Green Diesel', 'HVO', 'Hydrotreated Vegetable Oil']},
    "SUSTAINABLE_AVIATION_FUEL": {'description': 'Jet fuel produced from biomass or waste, meeting aviation fuel specifications.', 'annotations': {'drop_in_fuel': True}, 'aliases': ['SAF', 'Biojet']},
    "BIOGAS": {'description': 'Gaseous mixture of methane and CO2 produced by anaerobic digestion of organic matter.', 'annotations': {'methane_content_percent': '50-70'}, 'aliases': ['Raw Biogas']},
    "BIOMETHANE": {'description': 'Purified biogas upgraded to natural gas quality (>95% methane).', 'annotations': {'methane_content_percent': '95+', 'pipeline_quality': True}, 'aliases': ['Renewable Natural Gas', 'RNG']},
    "BIO_OIL": {'description': 'Liquid intermediate produced by pyrolysis or hydrothermal liquefaction of biomass.', 'annotations': {'intermediate': True}, 'aliases': ['Pyrolysis Oil']},
    "SYNGAS": {'description': 'Synthesis gas (CO + H2) produced by gasification of biomass.', 'annotations': {'intermediate': True}, 'aliases': ['Synthesis Gas', 'gasification']},
    "BUTANOL": {'description': 'Four-carbon alcohol biofuel with higher energy density than ethanol.', 'meaning': 'CHEBI:28885', 'annotations': {'chemical_formula': 'C4H9OH'}, 'aliases': ['Biobutanol']},
    "METHANOL": {'description': 'Methanol produced from biomass-derived syngas.', 'meaning': 'CHEBI:17790', 'annotations': {'chemical_formula': 'CH3OH'}},
    "DIMETHYL_ETHER": {'description': 'Dimethyl ether produced from biomass, usable as diesel substitute.', 'meaning': 'CHEBI:28887', 'aliases': ['DME']},
}

class BiofuelGeneration(RichEnum):
    """
    Classification of biofuels by feedstock source and technology generation.
    """
    # Enum members
    FIRST_GENERATION = "FIRST_GENERATION"
    SECOND_GENERATION = "SECOND_GENERATION"
    THIRD_GENERATION = "THIRD_GENERATION"
    FOURTH_GENERATION = "FOURTH_GENERATION"

# Set metadata after class creation
BiofuelGeneration._metadata = {
    "FIRST_GENERATION": {'description': 'Biofuels produced from food crops (sugar, starch, vegetable oils) using conventional conversion technologies.', 'annotations': {'feedstock': 'food_crops', 'examples': 'corn_ethanol,soy_biodiesel'}, 'aliases': ['1G Biofuel', 'Conventional Biofuel']},
    "SECOND_GENERATION": {'description': 'Biofuels produced from lignocellulosic biomass (non-food) using advanced conversion technologies.', 'annotations': {'feedstock': 'lignocellulosic', 'examples': 'cellulosic_ethanol,wood_diesel'}, 'aliases': ['2G Biofuel', 'Cellulosic Biofuel', 'Advanced Biofuel']},
    "THIRD_GENERATION": {'description': 'Biofuels produced from algae or other photosynthetic microorganisms.', 'annotations': {'feedstock': 'algae'}, 'aliases': ['3G Biofuel', 'Algal Biofuel']},
    "FOURTH_GENERATION": {'description': 'Biofuels from genetically engineered organisms designed for carbon capture and enhanced fuel production.', 'annotations': {'feedstock': 'engineered_organisms', 'carbon_negative': True}, 'aliases': ['4G Biofuel']},
}

class BioconversionProcess(RichEnum):
    """
    Processes for converting biomass feedstocks into biofuels and bioproducts.
    """
    # Enum members
    FERMENTATION = "FERMENTATION"
    ANAEROBIC_DIGESTION = "ANAEROBIC_DIGESTION"
    TRANSESTERIFICATION = "TRANSESTERIFICATION"
    HYDROTREATING = "HYDROTREATING"
    PYROLYSIS = "PYROLYSIS"
    GASIFICATION = "GASIFICATION"
    HYDROTHERMAL_LIQUEFACTION = "HYDROTHERMAL_LIQUEFACTION"
    ENZYMATIC_HYDROLYSIS = "ENZYMATIC_HYDROLYSIS"
    ACID_HYDROLYSIS = "ACID_HYDROLYSIS"
    FISCHER_TROPSCH = "FISCHER_TROPSCH"
    ALCOHOL_TO_JET = "ALCOHOL_TO_JET"

# Set metadata after class creation
BioconversionProcess._metadata = {
    "FERMENTATION": {'description': 'Biological conversion of sugars to alcohols using yeast or bacteria.', 'annotations': {'category': 'biochemical', 'products': 'ethanol,butanol'}},
    "ANAEROBIC_DIGESTION": {'description': 'Biological breakdown of organic matter by microorganisms in the absence of oxygen, producing biogas.', 'annotations': {'category': 'biochemical', 'products': 'biogas'}},
    "TRANSESTERIFICATION": {'description': 'Chemical reaction of triglycerides with alcohol to produce fatty acid esters (biodiesel) and glycerol.', 'annotations': {'category': 'chemical', 'products': 'biodiesel'}},
    "HYDROTREATING": {'description': 'Catalytic reaction of lipids with hydrogen to produce hydrocarbon fuels.', 'annotations': {'category': 'thermochemical', 'products': 'renewable_diesel,SAF'}, 'aliases': ['Hydroprocessing']},
    "PYROLYSIS": {'description': 'Thermal decomposition of biomass in the absence of oxygen to produce bio-oil, syngas, and biochar.', 'annotations': {'category': 'thermochemical', 'temperature_c': '400-600', 'products': 'bio_oil,syngas,biochar'}},
    "GASIFICATION": {'description': 'High-temperature conversion of carbonaceous materials to syngas using controlled oxygen and/or steam.', 'meaning': 'CHMO:0001501', 'annotations': {'category': 'thermochemical', 'temperature_c': '700-1500', 'products': 'syngas'}},
    "HYDROTHERMAL_LIQUEFACTION": {'description': 'Conversion of wet biomass to bio-crude using high temperature and pressure water.', 'annotations': {'category': 'thermochemical', 'temperature_c': '250-400', 'pressure_bar': '100-200', 'wet_feedstock': True}, 'aliases': ['HTL']},
    "ENZYMATIC_HYDROLYSIS": {'description': 'Breakdown of cellulose and hemicellulose to fermentable sugars using enzymes.', 'annotations': {'category': 'biochemical', 'pretreatment_step': True}},
    "ACID_HYDROLYSIS": {'description': 'Chemical breakdown of cellulose to sugars using dilute or concentrated acid.', 'annotations': {'category': 'chemical', 'pretreatment_step': True}},
    "FISCHER_TROPSCH": {'description': 'Catalytic conversion of syngas to liquid hydrocarbons.', 'annotations': {'category': 'thermochemical', 'feedstock': 'syngas', 'products': 'FT_diesel,FT_jet'}, 'aliases': ['FT Synthesis']},
    "ALCOHOL_TO_JET": {'description': 'Conversion of alcohols (ethanol, isobutanol) to jet fuel through dehydration, oligomerization, and hydrogenation.', 'annotations': {'category': 'chemical', 'products': 'SAF'}, 'aliases': ['ATJ']},
}

__all__ = [
    "BiomassFeedstockType",
    "BiofuelType",
    "BiofuelGeneration",
    "BioconversionProcess",
]