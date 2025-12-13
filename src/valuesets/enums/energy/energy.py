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
    "SOLAR": {'meaning': 'ENVO:01001862', 'annotations': {'renewable': True, 'emission_free': True, 'oeo_label': 'solar energy', 'brick_label': 'Solar Thermal Collector'}, 'aliases': ['Solar radiation']},
    "WIND": {'annotations': {'renewable': True, 'emission_free': True, 'oeo_label': 'wind energy'}, 'aliases': ['wind wave energy']},
    "HYDROELECTRIC": {'annotations': {'renewable': True, 'emission_free': True, 'oeo_label': 'hydro energy'}, 'aliases': ['hydroelectric dam']},
    "GEOTHERMAL": {'meaning': 'ENVO:2000034', 'annotations': {'renewable': True, 'emission_free': True, 'oeo_label': 'geothermal energy'}, 'aliases': ['geothermal energy']},
    "BIOMASS": {'annotations': {'renewable': True, 'emission_free': False, 'oeo_label': 'bioenergy'}, 'aliases': ['organic material']},
    "BIOFUEL": {'annotations': {'renewable': True, 'emission_free': False, 'oeo_label': 'biofuel'}},
    "TIDAL": {'annotations': {'renewable': True, 'emission_free': True, 'oeo_label': 'marine tidal energy, marine wave energy'}},
    "HYDROGEN": {'meaning': 'CHEBI:18276', 'annotations': {'renewable': 'depends', 'emission_free': True, 'oeo_label': 'hydrogen'}, 'aliases': ['dihydrogen']},
    "COAL": {'meaning': 'ENVO:02000091', 'annotations': {'renewable': False, 'emission_free': False, 'fossil_fuel': True, 'oeo_label': 'coal'}},
    "NATURAL_GAS": {'meaning': 'ENVO:01000552', 'annotations': {'renewable': False, 'emission_free': False, 'fossil_fuel': True, 'oeo_label': 'natural gas'}},
    "PETROLEUM": {'meaning': 'ENVO:00002984', 'annotations': {'renewable': False, 'emission_free': False, 'fossil_fuel': True, 'oeo_label': 'crude oil'}},
    "DIESEL": {'meaning': 'ENVO:03510006', 'annotations': {'renewable': False, 'emission_free': False, 'fossil_fuel': True, 'oeo_label': 'diesel fuel'}, 'aliases': ['diesel fuel']},
    "GASOLINE": {'annotations': {'renewable': False, 'emission_free': False, 'fossil_fuel': True, 'oeo_label': 'gasoline fuel'}, 'aliases': ['fuel oil']},
    "PROPANE": {'meaning': 'ENVO:01000553', 'annotations': {'renewable': False, 'emission_free': False, 'fossil_fuel': True}, 'aliases': ['liquefied petroleum gas']},
    "NUCLEAR_FISSION": {'annotations': {'renewable': False, 'emission_free': True, 'oeo_label': 'nuclear fuel'}, 'aliases': ['nuclear energy']},
    "NUCLEAR_FUSION": {'annotations': {'renewable': False, 'emission_free': True}, 'aliases': ['nuclear energy']},
    "GRID_MIX": {'annotations': {'renewable': 'partial', 'oeo_label': 'supply grid'}},
    "BATTERY_STORAGE": {'description': 'Battery storage systems', 'annotations': {'storage': True, 'oeo_label': 'battery'}},
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
    "MAIN_GRID": {'description': 'Main utility grid', 'annotations': {'oeo_label': 'supply grid'}},
    "MICROGRID": {'description': 'Microgrid'},
    "OFF_GRID": {'description': 'Off-grid/standalone'},
    "SMART_GRID": {'description': 'Smart grid'},
    "MINI_GRID": {'description': 'Mini-grid'},
    "VIRTUAL_POWER_PLANT": {'description': 'Virtual power plant'},
}

class BatteryType(RichEnum):
    """
    Types of battery technologies for energy storage
    """
    # Enum members
    LITHIUM_ION = "LITHIUM_ION"
    LITHIUM_IRON_PHOSPHATE = "LITHIUM_IRON_PHOSPHATE"
    LITHIUM_POLYMER = "LITHIUM_POLYMER"
    LEAD_ACID = "LEAD_ACID"
    NICKEL_METAL_HYDRIDE = "NICKEL_METAL_HYDRIDE"
    NICKEL_CADMIUM = "NICKEL_CADMIUM"
    SODIUM_ION = "SODIUM_ION"
    SOLID_STATE = "SOLID_STATE"
    VANADIUM_REDOX_FLOW = "VANADIUM_REDOX_FLOW"
    ZINC_BROMINE_FLOW = "ZINC_BROMINE_FLOW"
    IRON_AIR = "IRON_AIR"
    ZINC_AIR = "ZINC_AIR"

# Set metadata after class creation
BatteryType._metadata = {
    "LITHIUM_ION": {'description': 'Lithium-ion battery', 'annotations': {'chemistry': 'lithium'}, 'aliases': ['Li-ion', 'LIB']},
    "LITHIUM_IRON_PHOSPHATE": {'description': 'Lithium iron phosphate (LFP) battery', 'annotations': {'chemistry': 'lithium'}, 'aliases': ['LFP', 'LiFePO4']},
    "LITHIUM_POLYMER": {'description': 'Lithium polymer battery', 'annotations': {'chemistry': 'lithium'}, 'aliases': ['LiPo']},
    "LEAD_ACID": {'description': 'Lead-acid battery', 'annotations': {'chemistry': 'lead'}, 'aliases': ['Pb-acid']},
    "NICKEL_METAL_HYDRIDE": {'description': 'Nickel-metal hydride battery', 'annotations': {'chemistry': 'nickel'}, 'aliases': ['NiMH']},
    "NICKEL_CADMIUM": {'description': 'Nickel-cadmium battery', 'annotations': {'chemistry': 'nickel'}, 'aliases': ['NiCd']},
    "SODIUM_ION": {'description': 'Sodium-ion battery', 'annotations': {'chemistry': 'sodium'}, 'aliases': ['Na-ion']},
    "SOLID_STATE": {'description': 'Solid-state battery', 'annotations': {'chemistry': 'various'}},
    "VANADIUM_REDOX_FLOW": {'description': 'Vanadium redox flow battery', 'annotations': {'chemistry': 'vanadium', 'type': 'flow'}, 'aliases': ['VRB', 'VRFB']},
    "ZINC_BROMINE_FLOW": {'description': 'Zinc-bromine flow battery', 'annotations': {'chemistry': 'zinc', 'type': 'flow'}, 'aliases': ['ZnBr']},
    "IRON_AIR": {'description': 'Iron-air battery', 'annotations': {'chemistry': 'iron'}},
    "ZINC_AIR": {'description': 'Zinc-air battery', 'annotations': {'chemistry': 'zinc'}},
}

class PVCellType(RichEnum):
    """
    Types of photovoltaic cell technologies
    """
    # Enum members
    MONOCRYSTALLINE_SILICON = "MONOCRYSTALLINE_SILICON"
    POLYCRYSTALLINE_SILICON = "POLYCRYSTALLINE_SILICON"
    PASSIVATED_EMITTER_REAR_CELL = "PASSIVATED_EMITTER_REAR_CELL"
    HETEROJUNCTION = "HETEROJUNCTION"
    TUNNEL_OXIDE_PASSIVATED_CONTACT = "TUNNEL_OXIDE_PASSIVATED_CONTACT"
    INTERDIGITATED_BACK_CONTACT = "INTERDIGITATED_BACK_CONTACT"
    CADMIUM_TELLURIDE = "CADMIUM_TELLURIDE"
    COPPER_INDIUM_GALLIUM_SELENIDE = "COPPER_INDIUM_GALLIUM_SELENIDE"
    AMORPHOUS_SILICON = "AMORPHOUS_SILICON"
    GALLIUM_ARSENIDE = "GALLIUM_ARSENIDE"
    PEROVSKITE = "PEROVSKITE"
    ORGANIC = "ORGANIC"
    TANDEM = "TANDEM"

# Set metadata after class creation
PVCellType._metadata = {
    "MONOCRYSTALLINE_SILICON": {'description': 'Monocrystalline silicon (mono-Si) cells', 'annotations': {'material': 'silicon', 'efficiency_range': '17-22%'}, 'aliases': ['mono-Si', 'single-crystal silicon']},
    "POLYCRYSTALLINE_SILICON": {'description': 'Polycrystalline silicon (poly-Si) cells', 'annotations': {'material': 'silicon', 'efficiency_range': '15-17%'}, 'aliases': ['poly-Si', 'multi-crystalline silicon']},
    "PASSIVATED_EMITTER_REAR_CELL": {'description': 'Passivated Emitter and Rear Cell (PERC)', 'annotations': {'material': 'silicon', 'efficiency_range': '19-22%'}, 'aliases': ['PERC']},
    "HETEROJUNCTION": {'description': 'Heterojunction (HJT) cells', 'annotations': {'material': 'silicon', 'efficiency_range': '21-24%'}, 'aliases': ['HJT', 'HIT']},
    "TUNNEL_OXIDE_PASSIVATED_CONTACT": {'description': 'Tunnel Oxide Passivated Contact (TOPCon) cells', 'annotations': {'material': 'silicon', 'efficiency_range': '22-24%'}, 'aliases': ['TOPCon']},
    "INTERDIGITATED_BACK_CONTACT": {'description': 'Interdigitated Back Contact (IBC) cells', 'annotations': {'material': 'silicon', 'efficiency_range': '22-24%'}, 'aliases': ['IBC']},
    "CADMIUM_TELLURIDE": {'description': 'Cadmium telluride (CdTe) thin-film cells', 'annotations': {'material': 'cadmium_telluride', 'type': 'thin-film', 'efficiency_range': '16-18%'}, 'aliases': ['CdTe']},
    "COPPER_INDIUM_GALLIUM_SELENIDE": {'description': 'Copper indium gallium selenide (CIGS) thin-film cells', 'annotations': {'material': 'CIGS', 'type': 'thin-film', 'efficiency_range': '15-20%'}, 'aliases': ['CIGS', 'CIS']},
    "AMORPHOUS_SILICON": {'description': 'Amorphous silicon (a-Si) thin-film cells', 'annotations': {'material': 'silicon', 'type': 'thin-film', 'efficiency_range': '6-8%'}, 'aliases': ['a-Si']},
    "GALLIUM_ARSENIDE": {'description': 'Gallium arsenide (GaAs) cells', 'annotations': {'material': 'gallium_arsenide', 'efficiency_range': '25-30%', 'application': 'space, concentrator'}, 'aliases': ['GaAs']},
    "PEROVSKITE": {'description': 'Perovskite solar cells', 'annotations': {'material': 'perovskite', 'efficiency_range': '20-25%', 'status': 'emerging'}},
    "ORGANIC": {'description': 'Organic photovoltaic (OPV) cells', 'annotations': {'material': 'organic', 'type': 'thin-film', 'efficiency_range': '10-15%', 'status': 'emerging'}, 'aliases': ['OPV']},
    "TANDEM": {'description': 'Tandem/multi-junction cells', 'annotations': {'efficiency_range': '25-35%'}, 'aliases': ['multi-junction']},
}

class PVSystemType(RichEnum):
    """
    Types of photovoltaic system installations
    """
    # Enum members
    ROOFTOP_RESIDENTIAL = "ROOFTOP_RESIDENTIAL"
    ROOFTOP_COMMERCIAL = "ROOFTOP_COMMERCIAL"
    GROUND_MOUNTED = "GROUND_MOUNTED"
    FLOATING = "FLOATING"
    BUILDING_INTEGRATED = "BUILDING_INTEGRATED"
    AGRIVOLTAICS = "AGRIVOLTAICS"
    CARPORT = "CARPORT"
    TRACKER_SINGLE_AXIS = "TRACKER_SINGLE_AXIS"
    TRACKER_DUAL_AXIS = "TRACKER_DUAL_AXIS"
    CONCENTRATING = "CONCENTRATING"

# Set metadata after class creation
PVSystemType._metadata = {
    "ROOFTOP_RESIDENTIAL": {'description': 'Residential rooftop PV system', 'annotations': {'scale': 'residential', 'mounting': 'rooftop'}},
    "ROOFTOP_COMMERCIAL": {'description': 'Commercial/industrial rooftop PV system', 'annotations': {'scale': 'commercial', 'mounting': 'rooftop'}},
    "GROUND_MOUNTED": {'description': 'Ground-mounted utility-scale PV system', 'annotations': {'scale': 'utility', 'mounting': 'ground'}},
    "FLOATING": {'description': 'Floating PV system (floatovoltaics)', 'annotations': {'scale': 'utility', 'mounting': 'floating'}, 'aliases': ['floatovoltaics', 'FPV']},
    "BUILDING_INTEGRATED": {'description': 'Building-integrated PV (BIPV)', 'annotations': {'mounting': 'integrated'}, 'aliases': ['BIPV']},
    "AGRIVOLTAICS": {'description': 'Agrivoltaic system (dual-use with agriculture)', 'annotations': {'scale': 'utility', 'dual_use': 'agriculture'}, 'aliases': ['agrophotovoltaics', 'APV']},
    "CARPORT": {'description': 'Solar carport/parking canopy', 'annotations': {'mounting': 'canopy', 'dual_use': 'parking'}},
    "TRACKER_SINGLE_AXIS": {'description': 'Single-axis tracking system', 'annotations': {'tracking': 'single_axis'}},
    "TRACKER_DUAL_AXIS": {'description': 'Dual-axis tracking system', 'annotations': {'tracking': 'dual_axis'}},
    "CONCENTRATING": {'description': 'Concentrating PV (CPV) system', 'annotations': {'type': 'concentrating'}, 'aliases': ['CPV']},
}

class EnergyStorageType(RichEnum):
    """
    Types of energy storage systems (categories)
    """
    # Enum members
    BATTERY = "BATTERY"
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
    "BATTERY": {'description': 'Battery storage (see BatteryType for specific chemistries)', 'annotations': {'category': 'electrochemical'}},
    "PUMPED_HYDRO": {'description': 'Pumped hydroelectric storage', 'annotations': {'category': 'mechanical', 'oeo_label': 'pumped hydro storage power plant'}},
    "COMPRESSED_AIR": {'description': 'Compressed air energy storage (CAES)', 'annotations': {'category': 'mechanical', 'oeo_label': 'compressed air'}},
    "FLYWHEEL": {'description': 'Flywheel energy storage', 'annotations': {'category': 'mechanical'}},
    "GRAVITY_STORAGE": {'description': 'Gravity-based storage', 'annotations': {'category': 'mechanical'}},
    "MOLTEN_SALT": {'description': 'Molten salt thermal storage', 'annotations': {'category': 'thermal'}},
    "ICE_STORAGE": {'description': 'Ice thermal storage', 'annotations': {'category': 'thermal'}},
    "PHASE_CHANGE": {'description': 'Phase change materials', 'annotations': {'category': 'thermal'}},
    "HYDROGEN_STORAGE": {'description': 'Hydrogen storage', 'annotations': {'category': 'chemical', 'oeo_label': 'hydrogen'}},
    "SYNTHETIC_FUEL": {'description': 'Synthetic fuel storage', 'annotations': {'category': 'chemical', 'oeo_label': 'synthetic fuel'}},
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
    "SCOPE_1": {'description': 'Direct emissions from owned or controlled sources', 'annotations': {'ghg_protocol': 'Scope 1', 'oeo_label': 'greenhouse gas emission'}},
    "SCOPE_2": {'description': 'Indirect emissions from purchased energy', 'annotations': {'ghg_protocol': 'Scope 2', 'oeo_label': 'greenhouse gas emission'}},
    "SCOPE_3": {'description': 'All other indirect emissions in value chain', 'annotations': {'ghg_protocol': 'Scope 3', 'oeo_label': 'greenhouse gas emission'}},
    "SCOPE_3_UPSTREAM": {'description': 'Upstream Scope 3 emissions', 'annotations': {'ghg_protocol': 'Scope 3', 'oeo_label': 'greenhouse gas emission'}},
    "SCOPE_3_DOWNSTREAM": {'description': 'Downstream Scope 3 emissions', 'annotations': {'ghg_protocol': 'Scope 3', 'oeo_label': 'greenhouse gas emission'}},
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

class CapabilityStatus(RichEnum):
    """
    Operational status of a capability, facility, or infrastructure. Applicable to energy facilities, research capabilities, and other infrastructure throughout their lifecycle.
    """
    # Enum members
    OPERATIONAL = "OPERATIONAL"
    COMING_ONLINE = "COMING_ONLINE"
    PILOT = "PILOT"
    UNDER_DEVELOPMENT = "UNDER_DEVELOPMENT"
    DECOMMISSIONED = "DECOMMISSIONED"

# Set metadata after class creation
CapabilityStatus._metadata = {
    "OPERATIONAL": {'description': 'Fully operational and available to users', 'annotations': {'wikidata_label': 'in use', 'lifecycle_phase': 'operation'}},
    "COMING_ONLINE": {'description': 'Being commissioned, coming online soon', 'annotations': {'wikidata_label': 'building process', 'lifecycle_phase': 'commissioning', 'iaea_equivalent': 'commissioning'}},
    "PILOT": {'description': 'In pilot phase with limited access', 'annotations': {'availability': 'limited', 'lifecycle_phase': 'testing'}},
    "UNDER_DEVELOPMENT": {'description': 'Under development, not yet available', 'annotations': {'wikidata_label': 'proposed building or structure', 'lifecycle_phase': 'planning/construction'}},
    "DECOMMISSIONED": {'description': 'No longer available, permanently shut down', 'annotations': {'lifecycle_phase': 'end-of-life', 'iaea_equivalent': 'decommissioned'}},
}

__all__ = [
    "EnergySource",
    "EnergyUnit",
    "PowerUnit",
    "EnergyEfficiencyRating",
    "BuildingEnergyStandard",
    "GridType",
    "BatteryType",
    "PVCellType",
    "PVSystemType",
    "EnergyStorageType",
    "EmissionScope",
    "CarbonIntensity",
    "ElectricityMarket",
    "CapabilityStatus",
]