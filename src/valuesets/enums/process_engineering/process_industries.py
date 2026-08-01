"""
Process Industry Value Sets

Value sets categorizing process industries and process operation modes. The process industry categories generalize the top-level process categories used by the PISCES Standard Flowsheet Format (Biofuel, Chemical, Energy, Pharmaceutical, Food Product) into a more comprehensive set of process manufacturing sectors.

Generated from: process_engineering/process_industries.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class ProcessIndustryCategory(RichEnum):
    """
    Sectors of the process (continuous and batch) manufacturing industries. The pisces_category annotation records the corresponding top-level category in the PISCES Standard Flowsheet Format where one exists.
    """
    # Enum members
    PETROLEUM_REFINING = "PETROLEUM_REFINING"
    PETROCHEMICAL = "PETROCHEMICAL"
    BULK_CHEMICAL = "BULK_CHEMICAL"
    SPECIALTY_CHEMICAL = "SPECIALTY_CHEMICAL"
    AGROCHEMICAL = "AGROCHEMICAL"
    POLYMER_AND_PLASTICS = "POLYMER_AND_PLASTICS"
    PHARMACEUTICAL = "PHARMACEUTICAL"
    BIOTECHNOLOGY = "BIOTECHNOLOGY"
    BIOFUEL = "BIOFUEL"
    FOOD_AND_BEVERAGE = "FOOD_AND_BEVERAGE"
    PULP_AND_PAPER = "PULP_AND_PAPER"
    METALS_AND_MINING = "METALS_AND_MINING"
    WATER_AND_WASTEWATER_TREATMENT = "WATER_AND_WASTEWATER_TREATMENT"
    POWER_GENERATION = "POWER_GENERATION"
    GAS_PROCESSING = "GAS_PROCESSING"
    CEMENT_AND_CONSTRUCTION_MATERIALS = "CEMENT_AND_CONSTRUCTION_MATERIALS"
    GLASS_AND_CERAMICS = "GLASS_AND_CERAMICS"
    TEXTILE = "TEXTILE"
    COSMETICS_AND_PERSONAL_CARE = "COSMETICS_AND_PERSONAL_CARE"
    NUCLEAR_FUEL = "NUCLEAR_FUEL"
    SEMICONDUCTOR = "SEMICONDUCTOR"

# Set metadata after class creation
ProcessIndustryCategory._metadata = {
    "PETROLEUM_REFINING": {'description': 'Refining of crude oil into fuels and feedstocks', 'annotations': {'pisces_category': 'Energy'}},
    "PETROCHEMICAL": {'description': 'Production of chemicals derived from petroleum and natural gas', 'annotations': {'pisces_category': 'Chemical'}},
    "BULK_CHEMICAL": {'description': 'Large-volume production of commodity chemicals', 'annotations': {'pisces_category': 'Chemical'}},
    "SPECIALTY_CHEMICAL": {'description': 'Production of lower-volume, high-value performance chemicals', 'annotations': {'pisces_category': 'Chemical'}},
    "AGROCHEMICAL": {'description': 'Production of fertilizers, pesticides, and other agricultural chemicals', 'annotations': {'pisces_category': 'Chemical'}},
    "POLYMER_AND_PLASTICS": {'description': 'Production of polymers, resins, and plastic materials', 'annotations': {'pisces_category': 'Chemical'}},
    "PHARMACEUTICAL": {'description': 'Manufacture of active pharmaceutical ingredients and drug products', 'annotations': {'pisces_category': 'Pharmaceutical'}},
    "BIOTECHNOLOGY": {'description': 'Manufacture of products using biological systems and fermentation', 'annotations': {'pisces_category': 'Pharmaceutical'}},
    "BIOFUEL": {'description': 'Production of biologically derived fuels such as ethanol and biodiesel', 'annotations': {'pisces_category': 'Biofuel'}},
    "FOOD_AND_BEVERAGE": {'description': 'Processing and manufacture of food and beverage products', 'annotations': {'pisces_category': 'Food Product'}},
    "PULP_AND_PAPER": {'description': 'Production of pulp, paper, and board from fiber'},
    "METALS_AND_MINING": {'description': 'Extraction and processing of metals and minerals'},
    "WATER_AND_WASTEWATER_TREATMENT": {'description': 'Treatment of water and wastewater streams'},
    "POWER_GENERATION": {'description': 'Generation of electrical power and process heat', 'annotations': {'pisces_category': 'Energy'}},
    "GAS_PROCESSING": {'description': 'Processing and separation of natural gas and industrial gases', 'annotations': {'pisces_category': 'Energy'}},
    "CEMENT_AND_CONSTRUCTION_MATERIALS": {'description': 'Production of cement, lime, and construction materials'},
    "GLASS_AND_CERAMICS": {'description': 'Manufacture of glass and ceramic products'},
    "TEXTILE": {'description': 'Production and finishing of textile fibers and fabrics'},
    "COSMETICS_AND_PERSONAL_CARE": {'description': 'Manufacture of cosmetics and personal care products'},
    "NUCLEAR_FUEL": {'description': 'Processing of nuclear fuel materials', 'annotations': {'pisces_category': 'Energy'}},
    "SEMICONDUCTOR": {'description': 'Fabrication of semiconductor and microelectronic materials'},
}

class ProcessOperationMode(RichEnum):
    """
    The temporal mode in which a process or unit operation is run.
    """
    # Enum members
    BATCH = "BATCH"
    CONTINUOUS = "CONTINUOUS"
    SEMI_BATCH = "SEMI_BATCH"
    SEMI_CONTINUOUS = "SEMI_CONTINUOUS"

# Set metadata after class creation
ProcessOperationMode._metadata = {
    "BATCH": {'description': 'Material is charged, processed, and discharged in discrete batches'},
    "CONTINUOUS": {'description': 'Material flows through the process steadily without interruption'},
    "SEMI_BATCH": {'description': 'A hybrid mode where some streams are continuous while others are batch-wise'},
    "SEMI_CONTINUOUS": {'description': 'Process alternates between continuous operation and periodic interruptions'},
}

__all__ = [
    "ProcessIndustryCategory",
    "ProcessOperationMode",
]