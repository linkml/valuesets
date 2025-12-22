"""
Hydrogen Energy Value Sets

Value sets for hydrogen production, storage, and utilization. Includes the color-coded hydrogen classification system used by industry. Based on DOE Hydrogen and Fuel Cell Technologies Office terminology.

Generated from: energy/renewable/hydrogen.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class HydrogenType(RichEnum):
    """
    Color-coded classification of hydrogen based on production method and carbon intensity. This informal industry taxonomy differentiates hydrogen by its carbon footprint and energy source.
    """
    # Enum members
    GREEN_HYDROGEN = "GREEN_HYDROGEN"
    BLUE_HYDROGEN = "BLUE_HYDROGEN"
    GREY_HYDROGEN = "GREY_HYDROGEN"
    BROWN_HYDROGEN = "BROWN_HYDROGEN"
    BLACK_HYDROGEN = "BLACK_HYDROGEN"
    PINK_HYDROGEN = "PINK_HYDROGEN"
    TURQUOISE_HYDROGEN = "TURQUOISE_HYDROGEN"
    WHITE_HYDROGEN = "WHITE_HYDROGEN"
    YELLOW_HYDROGEN = "YELLOW_HYDROGEN"
    ORANGE_HYDROGEN = "ORANGE_HYDROGEN"

# Set metadata after class creation
HydrogenType._metadata = {
    "GREEN_HYDROGEN": {'description': 'Hydrogen produced via electrolysis powered by renewable energy sources (solar, wind, hydro). Zero carbon emissions during production.', 'annotations': {'production_method': 'electrolysis', 'energy_source': 'renewable', 'carbon_intensity': 'zero'}, 'aliases': ['Renewable Hydrogen']},
    "BLUE_HYDROGEN": {'description': 'Hydrogen produced from natural gas via steam methane reforming (SMR) with carbon capture and storage (CCS). Low carbon intensity.', 'annotations': {'production_method': 'steam_methane_reforming', 'energy_source': 'natural_gas', 'carbon_intensity': 'low', 'requires_ccs': True}},
    "GREY_HYDROGEN": {'description': 'Hydrogen produced from natural gas via steam methane reforming without carbon capture. Most common production method currently.', 'annotations': {'production_method': 'steam_methane_reforming', 'energy_source': 'natural_gas', 'carbon_intensity': 'high', 'co2_per_kg_h2': '9-12'}, 'aliases': ['Gray Hydrogen']},
    "BROWN_HYDROGEN": {'description': 'Hydrogen produced from brown coal (lignite) gasification without carbon capture. High carbon intensity.', 'annotations': {'production_method': 'coal_gasification', 'energy_source': 'lignite', 'carbon_intensity': 'very_high'}},
    "BLACK_HYDROGEN": {'description': 'Hydrogen produced from black coal (bituminous) gasification without carbon capture. High carbon intensity.', 'annotations': {'production_method': 'coal_gasification', 'energy_source': 'bituminous_coal', 'carbon_intensity': 'very_high'}},
    "PINK_HYDROGEN": {'description': 'Hydrogen produced via electrolysis powered by nuclear energy. Zero carbon emissions during production.', 'annotations': {'production_method': 'electrolysis', 'energy_source': 'nuclear', 'carbon_intensity': 'zero'}, 'aliases': ['Purple Hydrogen', 'Red Hydrogen']},
    "TURQUOISE_HYDROGEN": {'description': 'Hydrogen produced via methane pyrolysis, producing solid carbon instead of CO2. Lower carbon intensity than grey hydrogen.', 'annotations': {'production_method': 'methane_pyrolysis', 'energy_source': 'natural_gas', 'carbon_intensity': 'low', 'byproduct': 'solid_carbon'}},
    "WHITE_HYDROGEN": {'description': 'Naturally occurring geological hydrogen found in underground deposits. Zero production emissions.', 'annotations': {'production_method': 'geological_extraction', 'energy_source': 'natural', 'carbon_intensity': 'zero'}, 'aliases': ['Natural Hydrogen', 'Geological Hydrogen', 'Gold Hydrogen']},
    "YELLOW_HYDROGEN": {'description': 'Hydrogen produced via electrolysis powered by solar energy specifically. A subset of green hydrogen.', 'annotations': {'production_method': 'electrolysis', 'energy_source': 'solar', 'carbon_intensity': 'zero'}},
    "ORANGE_HYDROGEN": {'description': 'Hydrogen produced from plastic waste gasification or pyrolysis. Emerging technology addressing both energy and waste challenges.', 'annotations': {'production_method': 'waste_gasification', 'energy_source': 'plastic_waste', 'carbon_intensity': 'varies'}},
}

class HydrogenProductionMethod(RichEnum):
    """
    Methods and processes for producing hydrogen.
    """
    # Enum members
    STEAM_METHANE_REFORMING = "STEAM_METHANE_REFORMING"
    AUTOTHERMAL_REFORMING = "AUTOTHERMAL_REFORMING"
    PARTIAL_OXIDATION = "PARTIAL_OXIDATION"
    COAL_GASIFICATION = "COAL_GASIFICATION"
    WATER_ELECTROLYSIS = "WATER_ELECTROLYSIS"
    ALKALINE_ELECTROLYSIS = "ALKALINE_ELECTROLYSIS"
    PEM_ELECTROLYSIS = "PEM_ELECTROLYSIS"
    SOLID_OXIDE_ELECTROLYSIS = "SOLID_OXIDE_ELECTROLYSIS"
    METHANE_PYROLYSIS = "METHANE_PYROLYSIS"
    BIOMASS_GASIFICATION = "BIOMASS_GASIFICATION"
    BIOLOGICAL_PRODUCTION = "BIOLOGICAL_PRODUCTION"
    THERMOCHEMICAL_WATER_SPLITTING = "THERMOCHEMICAL_WATER_SPLITTING"
    PHOTOELECTROCHEMICAL = "PHOTOELECTROCHEMICAL"

# Set metadata after class creation
HydrogenProductionMethod._metadata = {
    "STEAM_METHANE_REFORMING": {'description': 'High temperature steam reacts with methane to produce hydrogen, carbon monoxide, and carbon dioxide.', 'annotations': {'feedstock': 'natural_gas', 'temperature_c': '700-1000', 'dominant_method': True}, 'aliases': ['SMR']},
    "AUTOTHERMAL_REFORMING": {'description': 'Combines steam reforming and partial oxidation using oxygen and steam to produce hydrogen from hydrocarbons.', 'aliases': ['ATR']},
    "PARTIAL_OXIDATION": {'description': 'Exothermic process reacting hydrocarbons with limited oxygen to produce hydrogen and carbon monoxide.', 'aliases': ['POX']},
    "COAL_GASIFICATION": {'description': 'Conversion of coal to syngas (hydrogen and carbon monoxide) using high temperature and steam.', 'meaning': 'CHMO:0001501'},
    "WATER_ELECTROLYSIS": {'description': 'Splitting water into hydrogen and oxygen using electrical current. Can be powered by various energy sources.', 'aliases': ['Electrolysis']},
    "ALKALINE_ELECTROLYSIS": {'description': 'Electrolysis using alkaline solution (typically KOH) as electrolyte. Mature commercial technology.', 'annotations': {'electrolyte': 'alkaline', 'maturity': 'commercial'}, 'aliases': ['AEL']},
    "PEM_ELECTROLYSIS": {'description': 'Proton Exchange Membrane electrolysis using solid polymer electrolyte. Higher efficiency, faster response.', 'annotations': {'electrolyte': 'polymer_membrane', 'maturity': 'commercial'}, 'aliases': ['PEMEC', 'Polymer Electrolyte Membrane Electrolysis']},
    "SOLID_OXIDE_ELECTROLYSIS": {'description': 'High temperature electrolysis using solid ceramic electrolyte. Higher efficiency when waste heat is available.', 'annotations': {'electrolyte': 'solid_oxide', 'temperature_c': '700-850', 'maturity': 'emerging'}, 'aliases': ['SOEC']},
    "METHANE_PYROLYSIS": {'description': 'Thermal decomposition of methane into hydrogen and solid carbon without oxygen. Produces no direct CO2.', 'annotations': {'feedstock': 'natural_gas', 'byproduct': 'solid_carbon'}, 'aliases': ['Thermal Cracking']},
    "BIOMASS_GASIFICATION": {'description': 'Thermochemical conversion of biomass to hydrogen-rich syngas at high temperatures.', 'annotations': {'feedstock': 'biomass', 'renewable': True}},
    "BIOLOGICAL_PRODUCTION": {'description': 'Production of hydrogen by microorganisms through photosynthesis, fermentation, or other biological processes.', 'annotations': {'renewable': True, 'maturity': 'research'}, 'aliases': ['Biohydrogen']},
    "THERMOCHEMICAL_WATER_SPLITTING": {'description': 'Using high temperatures from concentrated solar or nuclear to drive chemical cycles that split water.', 'annotations': {'temperature_c': '500-2000', 'maturity': 'research'}},
    "PHOTOELECTROCHEMICAL": {'description': 'Direct conversion of sunlight to hydrogen using specialized semiconductor materials in contact with water.', 'annotations': {'maturity': 'research'}, 'aliases': ['PEC']},
}

class HydrogenStorageMethod(RichEnum):
    """
    Methods for storing hydrogen for later use or transport.
    """
    # Enum members
    COMPRESSED_GAS = "COMPRESSED_GAS"
    LIQUID_HYDROGEN = "LIQUID_HYDROGEN"
    METAL_HYDRIDE = "METAL_HYDRIDE"
    CHEMICAL_HYDRIDE = "CHEMICAL_HYDRIDE"
    UNDERGROUND_STORAGE = "UNDERGROUND_STORAGE"
    CRYO_COMPRESSED = "CRYO_COMPRESSED"

# Set metadata after class creation
HydrogenStorageMethod._metadata = {
    "COMPRESSED_GAS": {'description': 'Storage of hydrogen as compressed gas at high pressure (350-700 bar) in pressure vessels.', 'annotations': {'pressure_bar': '350-700', 'maturity': 'commercial'}, 'aliases': ['CGH2']},
    "LIQUID_HYDROGEN": {'description': 'Storage of hydrogen in liquid form at cryogenic temperatures (-253C). Higher energy density but requires insulation.', 'annotations': {'temperature_c': -253, 'maturity': 'commercial'}, 'aliases': ['LH2']},
    "METAL_HYDRIDE": {'description': 'Storage of hydrogen absorbed into metal alloys forming metal hydrides. Safer but heavier than compressed gas.', 'annotations': {'maturity': 'commercial'}},
    "CHEMICAL_HYDRIDE": {'description': 'Storage as chemical compounds (ammonia, methanol, LOHC) that release hydrogen when processed.', 'aliases': ['LOHC', 'Liquid Organic Hydrogen Carrier']},
    "UNDERGROUND_STORAGE": {'description': 'Large-scale storage in salt caverns, depleted gas fields, or aquifers for grid-scale applications.', 'annotations': {'scale': 'utility'}, 'aliases': ['Geological Storage']},
    "CRYO_COMPRESSED": {'description': 'Hybrid approach combining cryogenic cooling with high pressure for improved density.', 'annotations': {'maturity': 'emerging'}, 'aliases': ['CcH2']},
}

class HydrogenApplication(RichEnum):
    """
    End-use applications for hydrogen.
    """
    # Enum members
    FUEL_CELL_VEHICLE = "FUEL_CELL_VEHICLE"
    FUEL_CELL_STATIONARY = "FUEL_CELL_STATIONARY"
    INDUSTRIAL_FEEDSTOCK = "INDUSTRIAL_FEEDSTOCK"
    STEEL_PRODUCTION = "STEEL_PRODUCTION"
    AMMONIA_SYNTHESIS = "AMMONIA_SYNTHESIS"
    METHANOL_SYNTHESIS = "METHANOL_SYNTHESIS"
    POWER_TO_GAS = "POWER_TO_GAS"
    BLENDING_NATURAL_GAS = "BLENDING_NATURAL_GAS"
    SYNTHETIC_FUELS = "SYNTHETIC_FUELS"

# Set metadata after class creation
HydrogenApplication._metadata = {
    "FUEL_CELL_VEHICLE": {'description': 'Use of hydrogen in fuel cells for transportation (cars, trucks, buses).', 'aliases': ['FCEV']},
    "FUEL_CELL_STATIONARY": {'description': 'Use of hydrogen in stationary fuel cells for power generation.'},
    "INDUSTRIAL_FEEDSTOCK": {'description': 'Use of hydrogen as chemical feedstock for ammonia production, petroleum refining, and chemical synthesis.'},
    "STEEL_PRODUCTION": {'description': 'Use of hydrogen to reduce iron ore in steelmaking, replacing coal.', 'aliases': ['Green Steel']},
    "AMMONIA_SYNTHESIS": {'description': 'Use of hydrogen with nitrogen to produce ammonia for fertilizers.'},
    "METHANOL_SYNTHESIS": {'description': 'Use of hydrogen with CO2 to produce methanol.'},
    "POWER_TO_GAS": {'description': 'Conversion of excess renewable electricity to hydrogen for grid balancing and energy storage.', 'aliases': ['P2G']},
    "BLENDING_NATURAL_GAS": {'description': 'Blending hydrogen into natural gas pipelines for decarbonization of heating.'},
    "SYNTHETIC_FUELS": {'description': 'Use of hydrogen with captured CO2 to produce synthetic hydrocarbons (e-fuels, SAF).', 'aliases': ['E-Fuels', 'Power-to-Liquid']},
}

__all__ = [
    "HydrogenType",
    "HydrogenProductionMethod",
    "HydrogenStorageMethod",
    "HydrogenApplication",
]