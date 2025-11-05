"""
Energy and Power Value Sets

Value sets for energy sources, units, consumption, and related concepts

Generated from: energy/energy.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class EnergySource(RichEnum):
    """
    Types of energy sources and generation methods
    """
    # Enum members
    SOLAR = "SOLAR"
    WIND = "WIND"
    HYDROELECTRIC = "HYDROELECTRIC"
    GEOTHERMAL = "GEOTHERMAL"
    BIOMASS = "BIOMASS"
    BIOFUEL = "BIOFUEL"
    TIDAL = "TIDAL"
    HYDROGEN = "HYDROGEN"
    COAL = "COAL"
    NATURAL_GAS = "NATURAL_GAS"
    PETROLEUM = "PETROLEUM"
    DIESEL = "DIESEL"
    GASOLINE = "GASOLINE"
    PROPANE = "PROPANE"
    NUCLEAR_FISSION = "NUCLEAR_FISSION"
    NUCLEAR_FUSION = "NUCLEAR_FUSION"
    GRID_MIX = "GRID_MIX"
    BATTERY_STORAGE = "BATTERY_STORAGE"

# Set metadata after class creation
EnergySource._metadata = {
    "SOLAR": {'meaning': 'ENVO:01001862', 'annotations': {'renewable': True, 'emission_free': True}, 'aliases': ['Solar radiation']},
    "WIND": {'annotations': {'renewable': True, 'emission_free': True}, 'aliases': ['wind wave energy']},
    "HYDROELECTRIC": {'annotations': {'renewable': True, 'emission_free': True}, 'aliases': ['hydroelectric dam']},
    "GEOTHERMAL": {'meaning': 'ENVO:2000034', 'annotations': {'renewable': True, 'emission_free': True}, 'aliases': ['geothermal energy']},
    "BIOMASS": {'annotations': {'renewable': True, 'emission_free': False}, 'aliases': ['organic material']},
    "BIOFUEL": {'annotations': {'renewable': True, 'emission_free': False}},
    "TIDAL": {'annotations': {'renewable': True, 'emission_free': True}},
    "HYDROGEN": {'meaning': 'CHEBI:18276', 'annotations': {'renewable': 'depends', 'emission_free': True}, 'aliases': ['dihydrogen']},
    "COAL": {'meaning': 'ENVO:02000091', 'annotations': {'renewable': False, 'emission_free': False, 'fossil_fuel': True}},
    "NATURAL_GAS": {'meaning': 'ENVO:01000552', 'annotations': {'renewable': False, 'emission_free': False, 'fossil_fuel': True}},
    "PETROLEUM": {'meaning': 'ENVO:00002984', 'annotations': {'renewable': False, 'emission_free': False, 'fossil_fuel': True}},
    "DIESEL": {'meaning': 'ENVO:03510006', 'annotations': {'renewable': False, 'emission_free': False, 'fossil_fuel': True}, 'aliases': ['diesel fuel']},
    "GASOLINE": {'annotations': {'renewable': False, 'emission_free': False, 'fossil_fuel': True}, 'aliases': ['fuel oil']},
    "PROPANE": {'meaning': 'ENVO:01000553', 'annotations': {'renewable': False, 'emission_free': False, 'fossil_fuel': True}, 'aliases': ['liquefied petroleum gas']},
    "NUCLEAR_FISSION": {'annotations': {'renewable': False, 'emission_free': True}, 'aliases': ['nuclear energy']},
    "NUCLEAR_FUSION": {'annotations': {'renewable': False, 'emission_free': True}, 'aliases': ['nuclear energy']},
    "GRID_MIX": {'annotations': {'renewable': 'partial'}},
    "BATTERY_STORAGE": {'description': 'Battery storage systems', 'annotations': {'storage': True}},
}

class EnergyUnit(RichEnum):
    """
    Units for measuring energy
    """
    # Enum members
    JOULE = "JOULE"
    KILOJOULE = "KILOJOULE"
    MEGAJOULE = "MEGAJOULE"
    GIGAJOULE = "GIGAJOULE"
    WATT_HOUR = "WATT_HOUR"
    KILOWATT_HOUR = "KILOWATT_HOUR"
    MEGAWATT_HOUR = "MEGAWATT_HOUR"
    GIGAWATT_HOUR = "GIGAWATT_HOUR"
    TERAWATT_HOUR = "TERAWATT_HOUR"
    CALORIE = "CALORIE"
    KILOCALORIE = "KILOCALORIE"
    BTU = "BTU"
    THERM = "THERM"
    ELECTRON_VOLT = "ELECTRON_VOLT"
    TOE = "TOE"
    TCE = "TCE"

# Set metadata after class creation
EnergyUnit._metadata = {
    "JOULE": {'description': 'Joule (J)', 'meaning': 'QUDT:J', 'annotations': {'symbol': 'J', 'ucum': 'J', 'si_base': True}},
    "KILOJOULE": {'description': 'Kilojoule (kJ)', 'meaning': 'QUDT:KiloJ', 'annotations': {'symbol': 'kJ', 'ucum': 'kJ', 'joules': 1000}},
    "MEGAJOULE": {'description': 'Megajoule (MJ)', 'meaning': 'QUDT:MegaJ', 'annotations': {'symbol': 'MJ', 'ucum': 'MJ', 'joules': '1e6'}},
    "GIGAJOULE": {'description': 'Gigajoule (GJ)', 'meaning': 'QUDT:GigaJ', 'annotations': {'symbol': 'GJ', 'ucum': 'GJ', 'joules': '1e9'}},
    "WATT_HOUR": {'description': 'Watt-hour (Wh)', 'meaning': 'QUDT:W-HR', 'annotations': {'symbol': 'Wh', 'ucum': 'W.h', 'joules': 3600}},
    "KILOWATT_HOUR": {'description': 'Kilowatt-hour (kWh)', 'meaning': 'QUDT:KiloW-HR', 'annotations': {'symbol': 'kWh', 'ucum': 'kW.h', 'joules': '3.6e6'}},
    "MEGAWATT_HOUR": {'description': 'Megawatt-hour (MWh)', 'meaning': 'QUDT:MegaW-HR', 'annotations': {'symbol': 'MWh', 'ucum': 'MW.h', 'joules': '3.6e9'}},
    "GIGAWATT_HOUR": {'description': 'Gigawatt-hour (GWh)', 'meaning': 'QUDT:GigaW-HR', 'annotations': {'symbol': 'GWh', 'ucum': 'GW.h', 'joules': '3.6e12'}},
    "TERAWATT_HOUR": {'description': 'Terawatt-hour (TWh)', 'meaning': 'QUDT:TeraW-HR', 'annotations': {'symbol': 'TWh', 'ucum': 'TW.h', 'joules': '3.6e15'}},
    "CALORIE": {'description': 'Calorie (cal)', 'meaning': 'QUDT:CAL', 'annotations': {'symbol': 'cal', 'ucum': 'cal', 'joules': 4.184}},
    "KILOCALORIE": {'description': 'Kilocalorie (kcal)', 'meaning': 'QUDT:KiloCAL', 'annotations': {'symbol': 'kcal', 'ucum': 'kcal', 'joules': 4184}},
    "BTU": {'description': 'British thermal unit', 'meaning': 'QUDT:BTU_IT', 'annotations': {'symbol': 'BTU', 'ucum': '[Btu_IT]', 'joules': 1055.06}},
    "THERM": {'description': 'Therm', 'meaning': 'QUDT:THM_US', 'annotations': {'symbol': 'thm', 'ucum': '[thm_us]', 'joules': '1.055e8'}},
    "ELECTRON_VOLT": {'description': 'Electron volt (eV)', 'meaning': 'QUDT:EV', 'annotations': {'symbol': 'eV', 'ucum': 'eV', 'joules': 1.602e-19}},
    "TOE": {'description': 'Tonne of oil equivalent', 'meaning': 'QUDT:TOE', 'annotations': {'symbol': 'toe', 'ucum': 'toe', 'joules': '4.187e10'}},
    "TCE": {'description': 'Tonne of coal equivalent', 'annotations': {'symbol': 'tce', 'ucum': 'tce', 'joules': '2.93e10'}},
}

class PowerUnit(RichEnum):
    """
    Units for measuring power (energy per time)
    """
    # Enum members
    WATT = "WATT"
    KILOWATT = "KILOWATT"
    MEGAWATT = "MEGAWATT"
    GIGAWATT = "GIGAWATT"
    TERAWATT = "TERAWATT"
    HORSEPOWER = "HORSEPOWER"
    BTU_PER_HOUR = "BTU_PER_HOUR"

# Set metadata after class creation
PowerUnit._metadata = {
    "WATT": {'description': 'Watt (W)', 'meaning': 'QUDT:W', 'annotations': {'symbol': 'W', 'ucum': 'W', 'si_base': True}},
    "KILOWATT": {'description': 'Kilowatt (kW)', 'meaning': 'QUDT:KiloW', 'annotations': {'symbol': 'kW', 'ucum': 'kW', 'watts': 1000}},
    "MEGAWATT": {'description': 'Megawatt (MW)', 'meaning': 'QUDT:MegaW', 'annotations': {'symbol': 'MW', 'ucum': 'MW', 'watts': '1e6'}},
    "GIGAWATT": {'description': 'Gigawatt (GW)', 'meaning': 'QUDT:GigaW', 'annotations': {'symbol': 'GW', 'ucum': 'GW', 'watts': '1e9'}},
    "TERAWATT": {'description': 'Terawatt (TW)', 'meaning': 'QUDT:TeraW', 'annotations': {'symbol': 'TW', 'ucum': 'TW', 'watts': '1e12'}},
    "HORSEPOWER": {'description': 'Horsepower', 'meaning': 'QUDT:HP', 'annotations': {'symbol': 'hp', 'ucum': '[HP]', 'watts': 745.7}},
    "BTU_PER_HOUR": {'description': 'BTU per hour', 'annotations': {'symbol': 'BTU/h', 'ucum': '[Btu_IT]/h', 'watts': 0.293}},
}

class EnergyEfficiencyRating(RichEnum):
    """
    Energy efficiency ratings and standards
    """
    # Enum members
    A_PLUS_PLUS_PLUS = "A_PLUS_PLUS_PLUS"
    A_PLUS_PLUS = "A_PLUS_PLUS"
    A_PLUS = "A_PLUS"
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    E = "E"
    F = "F"
    G = "G"
    ENERGY_STAR = "ENERGY_STAR"
    ENERGY_STAR_MOST_EFFICIENT = "ENERGY_STAR_MOST_EFFICIENT"

# Set metadata after class creation
EnergyEfficiencyRating._metadata = {
    "A_PLUS_PLUS_PLUS": {'description': 'A+++ (highest efficiency)', 'annotations': {'rank': 1, 'region': 'EU'}},
    "A_PLUS_PLUS": {'description': 'A++', 'annotations': {'rank': 2, 'region': 'EU'}},
    "A_PLUS": {'description': 'A+', 'annotations': {'rank': 3, 'region': 'EU'}},
    "A": {'description': 'A', 'annotations': {'rank': 4, 'region': 'EU'}},
    "B": {'description': 'B', 'annotations': {'rank': 5, 'region': 'EU'}},
    "C": {'description': 'C', 'annotations': {'rank': 6, 'region': 'EU'}},
    "D": {'description': 'D', 'annotations': {'rank': 7, 'region': 'EU'}},
    "E": {'description': 'E', 'annotations': {'rank': 8, 'region': 'EU'}},
    "F": {'description': 'F', 'annotations': {'rank': 9, 'region': 'EU'}},
    "G": {'description': 'G (lowest efficiency)', 'annotations': {'rank': 10, 'region': 'EU'}},
    "ENERGY_STAR": {'description': 'Energy Star certified', 'annotations': {'region': 'US'}},
    "ENERGY_STAR_MOST_EFFICIENT": {'description': 'Energy Star Most Efficient', 'annotations': {'region': 'US'}},
}

class BuildingEnergyStandard(RichEnum):
    """
    Building energy efficiency standards and certifications
    """
    # Enum members
    PASSIVE_HOUSE = "PASSIVE_HOUSE"
    LEED_PLATINUM = "LEED_PLATINUM"
    LEED_GOLD = "LEED_GOLD"
    LEED_SILVER = "LEED_SILVER"
    LEED_CERTIFIED = "LEED_CERTIFIED"
    BREEAM_OUTSTANDING = "BREEAM_OUTSTANDING"
    BREEAM_EXCELLENT = "BREEAM_EXCELLENT"
    BREEAM_VERY_GOOD = "BREEAM_VERY_GOOD"
    BREEAM_GOOD = "BREEAM_GOOD"
    BREEAM_PASS = "BREEAM_PASS"
    NET_ZERO = "NET_ZERO"
    ENERGY_POSITIVE = "ENERGY_POSITIVE"
    ZERO_CARBON = "ZERO_CARBON"

# Set metadata after class creation
BuildingEnergyStandard._metadata = {
    "PASSIVE_HOUSE": {'description': 'Passive House (Passivhaus) standard'},
    "LEED_PLATINUM": {'description': 'LEED Platinum certification'},
    "LEED_GOLD": {'description': 'LEED Gold certification'},
    "LEED_SILVER": {'description': 'LEED Silver certification'},
    "LEED_CERTIFIED": {'description': 'LEED Certified'},
    "BREEAM_OUTSTANDING": {'description': 'BREEAM Outstanding'},
    "BREEAM_EXCELLENT": {'description': 'BREEAM Excellent'},
    "BREEAM_VERY_GOOD": {'description': 'BREEAM Very Good'},
    "BREEAM_GOOD": {'description': 'BREEAM Good'},
    "BREEAM_PASS": {'description': 'BREEAM Pass'},
    "NET_ZERO": {'description': 'Net Zero Energy Building'},
    "ENERGY_POSITIVE": {'description': 'Energy Positive Building'},
    "ZERO_CARBON": {'description': 'Zero Carbon Building'},
}

class GridType(RichEnum):
    """
    Types of electrical grid systems
    """
    # Enum members
    MAIN_GRID = "MAIN_GRID"
    MICROGRID = "MICROGRID"
    OFF_GRID = "OFF_GRID"
    SMART_GRID = "SMART_GRID"
    MINI_GRID = "MINI_GRID"
    VIRTUAL_POWER_PLANT = "VIRTUAL_POWER_PLANT"

# Set metadata after class creation
GridType._metadata = {
    "MAIN_GRID": {'description': 'Main utility grid'},
    "MICROGRID": {'description': 'Microgrid'},
    "OFF_GRID": {'description': 'Off-grid/standalone'},
    "SMART_GRID": {'description': 'Smart grid'},
    "MINI_GRID": {'description': 'Mini-grid'},
    "VIRTUAL_POWER_PLANT": {'description': 'Virtual power plant'},
}

class EnergyStorageType(RichEnum):
    """
    Types of energy storage systems
    """
    # Enum members
    LITHIUM_ION_BATTERY = "LITHIUM_ION_BATTERY"
    LEAD_ACID_BATTERY = "LEAD_ACID_BATTERY"
    FLOW_BATTERY = "FLOW_BATTERY"
    SOLID_STATE_BATTERY = "SOLID_STATE_BATTERY"
    SODIUM_ION_BATTERY = "SODIUM_ION_BATTERY"
    PUMPED_HYDRO = "PUMPED_HYDRO"
    COMPRESSED_AIR = "COMPRESSED_AIR"
    FLYWHEEL = "FLYWHEEL"
    GRAVITY_STORAGE = "GRAVITY_STORAGE"
    MOLTEN_SALT = "MOLTEN_SALT"
    ICE_STORAGE = "ICE_STORAGE"
    PHASE_CHANGE = "PHASE_CHANGE"
    HYDROGEN_STORAGE = "HYDROGEN_STORAGE"
    SYNTHETIC_FUEL = "SYNTHETIC_FUEL"
    SUPERCAPACITOR = "SUPERCAPACITOR"
    SUPERCONDUCTING = "SUPERCONDUCTING"

# Set metadata after class creation
EnergyStorageType._metadata = {
    "LITHIUM_ION_BATTERY": {'description': 'Lithium-ion battery', 'annotations': {'category': 'electrochemical'}},
    "LEAD_ACID_BATTERY": {'description': 'Lead-acid battery', 'annotations': {'category': 'electrochemical'}},
    "FLOW_BATTERY": {'description': 'Flow battery (e.g., vanadium redox)', 'annotations': {'category': 'electrochemical'}},
    "SOLID_STATE_BATTERY": {'description': 'Solid-state battery', 'annotations': {'category': 'electrochemical'}},
    "SODIUM_ION_BATTERY": {'description': 'Sodium-ion battery', 'annotations': {'category': 'electrochemical'}},
    "PUMPED_HYDRO": {'description': 'Pumped hydroelectric storage', 'annotations': {'category': 'mechanical'}},
    "COMPRESSED_AIR": {'description': 'Compressed air energy storage (CAES)', 'annotations': {'category': 'mechanical'}},
    "FLYWHEEL": {'description': 'Flywheel energy storage', 'annotations': {'category': 'mechanical'}},
    "GRAVITY_STORAGE": {'description': 'Gravity-based storage', 'annotations': {'category': 'mechanical'}},
    "MOLTEN_SALT": {'description': 'Molten salt thermal storage', 'annotations': {'category': 'thermal'}},
    "ICE_STORAGE": {'description': 'Ice thermal storage', 'annotations': {'category': 'thermal'}},
    "PHASE_CHANGE": {'description': 'Phase change materials', 'annotations': {'category': 'thermal'}},
    "HYDROGEN_STORAGE": {'description': 'Hydrogen storage', 'annotations': {'category': 'chemical'}},
    "SYNTHETIC_FUEL": {'description': 'Synthetic fuel storage', 'annotations': {'category': 'chemical'}},
    "SUPERCAPACITOR": {'description': 'Supercapacitor', 'annotations': {'category': 'electrical'}},
    "SUPERCONDUCTING": {'description': 'Superconducting magnetic energy storage (SMES)', 'annotations': {'category': 'electrical'}},
}

class EmissionScope(RichEnum):
    """
    Greenhouse gas emission scopes (GHG Protocol)
    """
    # Enum members
    SCOPE_1 = "SCOPE_1"
    SCOPE_2 = "SCOPE_2"
    SCOPE_3 = "SCOPE_3"
    SCOPE_3_UPSTREAM = "SCOPE_3_UPSTREAM"
    SCOPE_3_DOWNSTREAM = "SCOPE_3_DOWNSTREAM"

# Set metadata after class creation
EmissionScope._metadata = {
    "SCOPE_1": {'description': 'Direct emissions from owned or controlled sources', 'annotations': {'ghg_protocol': 'Scope 1'}},
    "SCOPE_2": {'description': 'Indirect emissions from purchased energy', 'annotations': {'ghg_protocol': 'Scope 2'}},
    "SCOPE_3": {'description': 'All other indirect emissions in value chain', 'annotations': {'ghg_protocol': 'Scope 3'}},
    "SCOPE_3_UPSTREAM": {'description': 'Upstream Scope 3 emissions', 'annotations': {'ghg_protocol': 'Scope 3'}},
    "SCOPE_3_DOWNSTREAM": {'description': 'Downstream Scope 3 emissions', 'annotations': {'ghg_protocol': 'Scope 3'}},
}

class CarbonIntensity(RichEnum):
    """
    Carbon intensity levels for energy sources
    """
    # Enum members
    ZERO_CARBON = "ZERO_CARBON"
    VERY_LOW_CARBON = "VERY_LOW_CARBON"
    LOW_CARBON = "LOW_CARBON"
    MEDIUM_CARBON = "MEDIUM_CARBON"
    HIGH_CARBON = "HIGH_CARBON"
    VERY_HIGH_CARBON = "VERY_HIGH_CARBON"

# Set metadata after class creation
CarbonIntensity._metadata = {
    "ZERO_CARBON": {'description': 'Zero carbon emissions', 'annotations': {'gCO2_per_kWh': 0}},
    "VERY_LOW_CARBON": {'description': 'Very low carbon (< 50 gCO2/kWh)', 'annotations': {'gCO2_per_kWh': '0-50'}},
    "LOW_CARBON": {'description': 'Low carbon (50-200 gCO2/kWh)', 'annotations': {'gCO2_per_kWh': '50-200'}},
    "MEDIUM_CARBON": {'description': 'Medium carbon (200-500 gCO2/kWh)', 'annotations': {'gCO2_per_kWh': '200-500'}},
    "HIGH_CARBON": {'description': 'High carbon (500-1000 gCO2/kWh)', 'annotations': {'gCO2_per_kWh': '500-1000'}},
    "VERY_HIGH_CARBON": {'description': 'Very high carbon (> 1000 gCO2/kWh)', 'annotations': {'gCO2_per_kWh': '1000+'}},
}

class ElectricityMarket(RichEnum):
    """
    Types of electricity markets and pricing
    """
    # Enum members
    SPOT_MARKET = "SPOT_MARKET"
    DAY_AHEAD = "DAY_AHEAD"
    INTRADAY = "INTRADAY"
    FUTURES = "FUTURES"
    CAPACITY_MARKET = "CAPACITY_MARKET"
    ANCILLARY_SERVICES = "ANCILLARY_SERVICES"
    BILATERAL = "BILATERAL"
    FEED_IN_TARIFF = "FEED_IN_TARIFF"
    NET_METERING = "NET_METERING"
    POWER_PURCHASE_AGREEMENT = "POWER_PURCHASE_AGREEMENT"

# Set metadata after class creation
ElectricityMarket._metadata = {
    "SPOT_MARKET": {'description': 'Spot market/real-time pricing'},
    "DAY_AHEAD": {'description': 'Day-ahead market'},
    "INTRADAY": {'description': 'Intraday market'},
    "FUTURES": {'description': 'Futures market'},
    "CAPACITY_MARKET": {'description': 'Capacity market'},
    "ANCILLARY_SERVICES": {'description': 'Ancillary services market'},
    "BILATERAL": {'description': 'Bilateral contracts'},
    "FEED_IN_TARIFF": {'description': 'Feed-in tariff'},
    "NET_METERING": {'description': 'Net metering'},
    "POWER_PURCHASE_AGREEMENT": {'description': 'Power purchase agreement (PPA)'},
}

__all__ = [
    "EnergySource",
    "EnergyUnit",
    "PowerUnit",
    "EnergyEfficiencyRating",
    "BuildingEnergyStandard",
    "GridType",
    "EnergyStorageType",
    "EmissionScope",
    "CarbonIntensity",
    "ElectricityMarket",
]