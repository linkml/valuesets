"""
Nuclear Fuel Cycle Value Sets

Value sets for nuclear fuel cycle processes and stages

Generated from: energy/nuclear/nuclear_fuel_cycle.yaml
"""

from __future__ import annotations

from typing import Dict, Any, Optional
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
    "MINING": {'description': 'Uranium ore mining and extraction', 'meaning': 'CVS:nuclear_fuel_cycle_mining'},
    "MILLING": {'description': 'Processing uranium ore into yellowcake (U3O8)', 'meaning': 'CVS:nuclear_fuel_cycle_milling'},
    "CONVERSION": {'description': 'Converting yellowcake to uranium hexafluoride (UF6)', 'meaning': 'CVS:nuclear_fuel_cycle_conversion'},
    "ENRICHMENT": {'description': 'Increasing U-235 concentration in uranium', 'meaning': 'CVS:nuclear_fuel_cycle_enrichment'},
    "FUEL_FABRICATION": {'description': 'Manufacturing nuclear fuel assemblies', 'meaning': 'CVS:nuclear_fuel_cycle_fuel_fabrication'},
    "REACTOR_OPERATION": {'description': 'Nuclear fission in reactor core', 'meaning': 'CVS:nuclear_fuel_cycle_reactor_operation'},
    "INTERIM_STORAGE": {'description': 'Temporary storage of spent nuclear fuel', 'meaning': 'CVS:nuclear_fuel_cycle_interim_storage'},
    "REPROCESSING": {'description': 'Chemical separation of useful materials from spent fuel', 'meaning': 'CVS:nuclear_fuel_cycle_reprocessing'},
    "FINAL_DISPOSAL": {'description': 'Permanent disposal of nuclear waste', 'meaning': 'CVS:nuclear_fuel_cycle_final_disposal'},
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
    "URANIUM_ORE": {'description': 'Natural uranium ore containing uranium minerals', 'meaning': 'CVS:nuclear_fuel_uranium_ore'},
    "YELLOWCAKE": {'description': 'Uranium oxide concentrate (U3O8)', 'meaning': 'CVS:nuclear_fuel_yellowcake'},
    "URANIUM_HEXAFLUORIDE": {'description': 'Gaseous uranium compound (UF6) used for enrichment', 'meaning': 'CVS:nuclear_fuel_uranium_hexafluoride'},
    "ENRICHED_URANIUM": {'description': 'Uranium with increased U-235 concentration', 'meaning': 'CVS:nuclear_fuel_enriched_uranium'},
    "URANIUM_DIOXIDE": {'description': 'Ceramic uranium fuel pellets (UO2)', 'meaning': 'CVS:nuclear_fuel_uranium_dioxide'},
    "FUEL_PELLETS": {'description': 'Sintered uranium dioxide pellets', 'meaning': 'CVS:nuclear_fuel_pellets'},
    "FUEL_RODS": {'description': 'Zircaloy tubes containing fuel pellets', 'meaning': 'CVS:nuclear_fuel_rods'},
    "FUEL_ASSEMBLIES": {'description': 'Bundled fuel rods ready for reactor loading', 'meaning': 'CVS:nuclear_fuel_assemblies'},
    "SPENT_FUEL": {'description': 'Used nuclear fuel removed from reactor', 'meaning': 'CVS:nuclear_fuel_spent'},
    "MIXED_OXIDE_FUEL": {'description': 'MOX fuel containing plutonium and uranium oxides', 'meaning': 'CVS:nuclear_fuel_mox'},
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
    "GAS_DIFFUSION": {'description': 'Gaseous diffusion enrichment process', 'meaning': 'CVS:enrichment_gas_diffusion'},
    "GAS_CENTRIFUGE": {'description': 'Gas centrifuge enrichment process', 'meaning': 'CVS:enrichment_gas_centrifuge'},
    "LASER_ISOTOPE_SEPARATION": {'description': 'Laser-based uranium isotope separation', 'meaning': 'CVS:enrichment_laser_isotope_separation'},
    "ELECTROMAGNETIC_SEPARATION": {'description': 'Electromagnetic isotope separation (EMIS)', 'meaning': 'CVS:enrichment_electromagnetic_separation'},
    "AERODYNAMIC_SEPARATION": {'description': 'Aerodynamic enrichment processes', 'meaning': 'CVS:enrichment_aerodynamic_separation'},
}

__all__ = [
    "NuclearFuelCycleStageEnum",
    "NuclearFuelFormEnum",
    "EnrichmentProcessEnum",
]