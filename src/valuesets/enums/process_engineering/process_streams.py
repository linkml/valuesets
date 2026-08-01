"""
Process Engineering Stream Value Sets

Value sets describing process streams - the material and energy flows that connect unit operations in a process flowsheet (the edges of a process graph, e.g. in the PISCES Standard Flowsheet Format). Covers the role a stream plays in the process, its physical (phase) state, and common plant utility types.

Generated from: process_engineering/process_streams.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class ProcessStreamRole(RichEnum):
    """
    The functional role of a stream within a process flowsheet, independent of its chemical composition.
    """
    # Enum members
    FEED = "FEED"
    RAW_MATERIAL = "RAW_MATERIAL"
    PRODUCT = "PRODUCT"
    BYPRODUCT = "BYPRODUCT"
    INTERMEDIATE = "INTERMEDIATE"
    RECYCLE = "RECYCLE"
    PURGE = "PURGE"
    BLEED = "BLEED"
    MAKEUP = "MAKEUP"
    WASTE = "WASTE"
    EFFLUENT = "EFFLUENT"
    EMISSION = "EMISSION"
    UTILITY = "UTILITY"

# Set metadata after class creation
ProcessStreamRole._metadata = {
    "FEED": {'description': 'A stream entering the process or a unit operation as input'},
    "RAW_MATERIAL": {'description': 'A fresh raw material or reactant stream entering the process battery limits'},
    "PRODUCT": {'description': 'A primary product stream of commercial value leaving the process'},
    "BYPRODUCT": {'description': 'A secondary saleable or usable product produced alongside the main product'},
    "INTERMEDIATE": {'description': 'A stream flowing between unit operations within the process'},
    "RECYCLE": {'description': 'A stream returned to an upstream point for reprocessing'},
    "PURGE": {'description': 'A stream withdrawn from a recycle loop to prevent accumulation of inerts or impurities'},
    "BLEED": {'description': 'A small continuous stream withdrawn to control composition or level'},
    "MAKEUP": {'description': 'A stream added to replenish material lost from a circulating loop'},
    "WASTE": {'description': 'A stream with no further use that must be treated or disposed of'},
    "EFFLUENT": {'description': 'A liquid waste stream discharged from the process'},
    "EMISSION": {'description': 'A gaseous stream released to the atmosphere'},
    "UTILITY": {'description': 'A service stream (e.g. steam, cooling water) supplied to a unit operation'},
}

class ProcessStreamPhase(RichEnum):
    """
    The physical phase or phase combination of a process stream. For single-phase fundamental states see also StateOfMatterEnum in the physics module; this enum adds the multiphase combinations common in process engineering.
    """
    # Enum members
    GAS = "GAS"
    LIQUID = "LIQUID"
    SOLID = "SOLID"
    SUPERCRITICAL = "SUPERCRITICAL"
    VAPOR_LIQUID = "VAPOR_LIQUID"
    LIQUID_LIQUID = "LIQUID_LIQUID"
    VAPOR_LIQUID_LIQUID = "VAPOR_LIQUID_LIQUID"
    SLURRY = "SLURRY"
    GAS_SOLID = "GAS_SOLID"
    MULTIPHASE = "MULTIPHASE"

# Set metadata after class creation
ProcessStreamPhase._metadata = {
    "GAS": {'description': 'A single gas or vapor phase', 'annotations': {'sff_phase_code': 'g'}},
    "LIQUID": {'description': 'A single liquid phase', 'annotations': {'sff_phase_code': 'l'}},
    "SOLID": {'description': 'A single solid phase', 'annotations': {'sff_phase_code': 's'}},
    "SUPERCRITICAL": {'description': 'A supercritical fluid above its critical temperature and pressure'},
    "VAPOR_LIQUID": {'description': 'A two-phase mixture of vapor and liquid'},
    "LIQUID_LIQUID": {'description': 'A two-phase mixture of two immiscible liquids'},
    "VAPOR_LIQUID_LIQUID": {'description': 'A three-phase mixture of a vapor and two immiscible liquids'},
    "SLURRY": {'description': 'A suspension of solids in a liquid'},
    "GAS_SOLID": {'description': 'A two-phase mixture of gas and entrained or fluidized solids'},
    "MULTIPHASE": {'description': 'A stream containing more than one phase, of mixed or unspecified composition'},
}

class UtilityType(RichEnum):
    """
    Common plant utilities consumed or produced by process unit operations, used for energy and mass balance accounting on a flowsheet.
    """
    # Enum members
    STEAM = "STEAM"
    LOW_PRESSURE_STEAM = "LOW_PRESSURE_STEAM"
    MEDIUM_PRESSURE_STEAM = "MEDIUM_PRESSURE_STEAM"
    HIGH_PRESSURE_STEAM = "HIGH_PRESSURE_STEAM"
    COOLING_WATER = "COOLING_WATER"
    CHILLED_WATER = "CHILLED_WATER"
    REFRIGERANT = "REFRIGERANT"
    HOT_OIL = "HOT_OIL"
    BRINE = "BRINE"
    ELECTRICITY = "ELECTRICITY"
    PROCESS_WATER = "PROCESS_WATER"
    DEMINERALIZED_WATER = "DEMINERALIZED_WATER"
    NATURAL_GAS = "NATURAL_GAS"
    FUEL_GAS = "FUEL_GAS"
    COMPRESSED_AIR = "COMPRESSED_AIR"
    INSTRUMENT_AIR = "INSTRUMENT_AIR"
    NITROGEN = "NITROGEN"
    FLARE = "FLARE"

# Set metadata after class creation
UtilityType._metadata = {
    "STEAM": {'description': 'Process steam used for heating or stripping', 'annotations': {'utility_category': 'HEAT'}},
    "LOW_PRESSURE_STEAM": {'description': 'Low-pressure steam utility', 'annotations': {'utility_category': 'HEAT', 'typical_range': '<3 barg'}},
    "MEDIUM_PRESSURE_STEAM": {'description': 'Medium-pressure steam utility', 'annotations': {'utility_category': 'HEAT', 'typical_range': '3-20 barg'}},
    "HIGH_PRESSURE_STEAM": {'description': 'High-pressure steam utility', 'annotations': {'utility_category': 'HEAT', 'typical_range': '>20 barg'}},
    "COOLING_WATER": {'description': 'Recirculated cooling water for heat rejection', 'annotations': {'utility_category': 'HEAT'}},
    "CHILLED_WATER": {'description': 'Refrigerated water for below-ambient cooling', 'annotations': {'utility_category': 'HEAT'}},
    "REFRIGERANT": {'description': 'Refrigerant fluid for low-temperature cooling duty', 'annotations': {'utility_category': 'HEAT'}},
    "HOT_OIL": {'description': 'Thermal oil heat-transfer fluid for high-temperature heating', 'annotations': {'utility_category': 'HEAT'}},
    "BRINE": {'description': 'Chilled brine used as a low-temperature coolant', 'annotations': {'utility_category': 'HEAT'}},
    "ELECTRICITY": {'description': 'Electrical power supplied to drivers and equipment', 'annotations': {'utility_category': 'POWER'}},
    "PROCESS_WATER": {'description': 'Treated water used as a process input', 'annotations': {'utility_category': 'OTHER'}},
    "DEMINERALIZED_WATER": {'description': 'High-purity demineralized water utility', 'annotations': {'utility_category': 'OTHER'}},
    "NATURAL_GAS": {'description': 'Natural gas supplied as fuel or feedstock', 'annotations': {'utility_category': 'OTHER'}},
    "FUEL_GAS": {'description': 'Fuel gas burned in fired heaters and boilers', 'annotations': {'utility_category': 'OTHER'}},
    "COMPRESSED_AIR": {'description': 'Compressed air utility for process or actuation use', 'annotations': {'utility_category': 'OTHER'}},
    "INSTRUMENT_AIR": {'description': 'Clean dry compressed air for instrumentation', 'annotations': {'utility_category': 'OTHER'}},
    "NITROGEN": {'description': 'Nitrogen used for inerting, blanketing, or purging', 'annotations': {'utility_category': 'OTHER'}},
    "FLARE": {'description': 'Flare system for safe combustion of relieved gases', 'annotations': {'utility_category': 'OTHER'}},
}

__all__ = [
    "ProcessStreamRole",
    "ProcessStreamPhase",
    "UtilityType",
]