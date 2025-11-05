"""
Nuclear Fuel Cycle Value Sets

Value sets for nuclear fuel cycle processes and stages

Generated from: energy/nuclear/nuclear_fuel_cycle.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class NuclearFuelCycleStageEnum(RichEnum):
    """
    Stages in the nuclear fuel cycle from mining to disposal
    """
    # Enum members
    MINING = "MINING"
    MILLING = "MILLING"
    CONVERSION = "CONVERSION"
    ENRICHMENT = "ENRICHMENT"
    FUEL_FABRICATION = "FUEL_FABRICATION"
    REACTOR_OPERATION = "REACTOR_OPERATION"
    INTERIM_STORAGE = "INTERIM_STORAGE"
    REPROCESSING = "REPROCESSING"
    FINAL_DISPOSAL = "FINAL_DISPOSAL"

# Set metadata after class creation
NuclearFuelCycleStageEnum._metadata = {
    "MINING": {'description': 'Uranium ore mining and extraction'},
    "MILLING": {'description': 'Processing uranium ore into yellowcake (U3O8)'},
    "CONVERSION": {'description': 'Converting yellowcake to uranium hexafluoride (UF6)'},
    "ENRICHMENT": {'description': 'Increasing U-235 concentration in uranium'},
    "FUEL_FABRICATION": {'description': 'Manufacturing nuclear fuel assemblies'},
    "REACTOR_OPERATION": {'description': 'Nuclear fission in reactor core'},
    "INTERIM_STORAGE": {'description': 'Temporary storage of spent nuclear fuel'},
    "REPROCESSING": {'description': 'Chemical separation of useful materials from spent fuel'},
    "FINAL_DISPOSAL": {'description': 'Permanent disposal of nuclear waste'},
}

class NuclearFuelFormEnum(RichEnum):
    """
    Different forms of nuclear fuel throughout the cycle
    """
    # Enum members
    URANIUM_ORE = "URANIUM_ORE"
    YELLOWCAKE = "YELLOWCAKE"
    URANIUM_HEXAFLUORIDE = "URANIUM_HEXAFLUORIDE"
    ENRICHED_URANIUM = "ENRICHED_URANIUM"
    URANIUM_DIOXIDE = "URANIUM_DIOXIDE"
    FUEL_PELLETS = "FUEL_PELLETS"
    FUEL_RODS = "FUEL_RODS"
    FUEL_ASSEMBLIES = "FUEL_ASSEMBLIES"
    SPENT_FUEL = "SPENT_FUEL"
    MIXED_OXIDE_FUEL = "MIXED_OXIDE_FUEL"

# Set metadata after class creation
NuclearFuelFormEnum._metadata = {
    "URANIUM_ORE": {'description': 'Natural uranium ore containing uranium minerals'},
    "YELLOWCAKE": {'description': 'Uranium oxide concentrate (U3O8)'},
    "URANIUM_HEXAFLUORIDE": {'description': 'Gaseous uranium compound (UF6) used for enrichment'},
    "ENRICHED_URANIUM": {'description': 'Uranium with increased U-235 concentration'},
    "URANIUM_DIOXIDE": {'description': 'Ceramic uranium fuel pellets (UO2)'},
    "FUEL_PELLETS": {'description': 'Sintered uranium dioxide pellets'},
    "FUEL_RODS": {'description': 'Zircaloy tubes containing fuel pellets'},
    "FUEL_ASSEMBLIES": {'description': 'Bundled fuel rods ready for reactor loading'},
    "SPENT_FUEL": {'description': 'Used nuclear fuel removed from reactor'},
    "MIXED_OXIDE_FUEL": {'description': 'MOX fuel containing plutonium and uranium oxides'},
}

class EnrichmentProcessEnum(RichEnum):
    """
    Methods for enriching uranium to increase U-235 concentration
    """
    # Enum members
    GAS_DIFFUSION = "GAS_DIFFUSION"
    GAS_CENTRIFUGE = "GAS_CENTRIFUGE"
    LASER_ISOTOPE_SEPARATION = "LASER_ISOTOPE_SEPARATION"
    ELECTROMAGNETIC_SEPARATION = "ELECTROMAGNETIC_SEPARATION"
    AERODYNAMIC_SEPARATION = "AERODYNAMIC_SEPARATION"

# Set metadata after class creation
EnrichmentProcessEnum._metadata = {
    "GAS_DIFFUSION": {'description': 'Gaseous diffusion enrichment process'},
    "GAS_CENTRIFUGE": {'description': 'Gas centrifuge enrichment process'},
    "LASER_ISOTOPE_SEPARATION": {'description': 'Laser-based uranium isotope separation'},
    "ELECTROMAGNETIC_SEPARATION": {'description': 'Electromagnetic isotope separation (EMIS)'},
    "AERODYNAMIC_SEPARATION": {'description': 'Aerodynamic enrichment processes'},
}

__all__ = [
    "NuclearFuelCycleStageEnum",
    "NuclearFuelFormEnum",
    "EnrichmentProcessEnum",
]