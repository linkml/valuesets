"""
Nuclear Reactor Types and Classifications

Classifications of nuclear reactor types based on coolant, moderator, neutron spectrum, and generational designs. Based on World Nuclear Association classifications, IAEA reactor types, and industry standards.

Generated from: energy/nuclear/reactor_types.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class ReactorTypeEnum(RichEnum):
    """
    Nuclear reactor types based on design and operational characteristics
    """
    # Enum members
    PWR = "PWR"
    BWR = "BWR"
    PHWR = "PHWR"
    LWGR = "LWGR"
    AGR = "AGR"
    GCR = "GCR"
    FBR = "FBR"
    HTGR = "HTGR"
    MSR = "MSR"
    SMR = "SMR"
    VHTR = "VHTR"
    SFR = "SFR"
    LFR = "LFR"
    GFR = "GFR"
    SCWR = "SCWR"

# Set metadata after class creation
ReactorTypeEnum._metadata = {
    "PWR": {'description': 'Most common reactor type using light water under pressure', 'annotations': {'coolant': 'light water', 'moderator': 'light water', 'pressure': 'high', 'steam_generation': 'indirect', 'worldwide_count': '~300', 'fuel_enrichment': '3-5%'}, 'aliases': ['Pressurized Water Reactor']},
    "BWR": {'description': 'Light water reactor where water boils directly in core', 'annotations': {'coolant': 'light water', 'moderator': 'light water', 'pressure': 'medium', 'steam_generation': 'direct', 'worldwide_count': '~60', 'fuel_enrichment': '3-5%'}, 'aliases': ['Boiling Water Reactor']},
    "PHWR": {'description': 'Heavy water moderated and cooled reactor (CANDU type)', 'annotations': {'coolant': 'heavy water', 'moderator': 'heavy water', 'pressure': 'high', 'steam_generation': 'indirect', 'worldwide_count': '~47', 'fuel_enrichment': 'natural uranium'}, 'aliases': ['CANDU', 'Pressurized Heavy Water Reactor']},
    "LWGR": {'description': 'Graphite moderated, light water cooled reactor (RBMK type)', 'annotations': {'coolant': 'light water', 'moderator': 'graphite', 'pressure': 'medium', 'steam_generation': 'direct', 'worldwide_count': '~10', 'fuel_enrichment': '1.8-2.4%'}, 'aliases': ['RBMK', 'Light Water Graphite Reactor']},
    "AGR": {'description': 'Graphite moderated, CO2 gas cooled reactor', 'annotations': {'coolant': 'carbon dioxide', 'moderator': 'graphite', 'pressure': 'high', 'steam_generation': 'indirect', 'worldwide_count': '~8', 'fuel_enrichment': '2.5-3.5%'}, 'aliases': ['Advanced Gas-Cooled Reactor']},
    "GCR": {'description': 'Early gas-cooled reactor design (Magnox type)', 'annotations': {'coolant': 'carbon dioxide', 'moderator': 'graphite', 'pressure': 'low', 'fuel_enrichment': 'natural uranium'}, 'aliases': ['Magnox', 'Gas-Cooled Reactor']},
    "FBR": {'description': 'Fast neutron reactor that breeds fissile material', 'annotations': {'coolant': 'liquid metal', 'moderator': 'none', 'neutron_spectrum': 'fast', 'worldwide_count': '~2', 'fuel_enrichment': '15-20%'}, 'aliases': ['Fast Breeder Reactor', 'Liquid Metal Fast Breeder Reactor']},
    "HTGR": {'description': 'Helium-cooled reactor with TRISO fuel', 'annotations': {'coolant': 'helium', 'moderator': 'graphite', 'temperature': 'very high', 'fuel_type': 'TRISO'}, 'aliases': ['High Temperature Gas-Cooled Reactor']},
    "MSR": {'description': 'Reactor using molten salt as coolant and/or fuel', 'annotations': {'coolant': 'molten salt', 'fuel_form': 'liquid', 'generation': 'IV'}, 'aliases': ['Molten Salt Reactor']},
    "SMR": {'description': 'Small reactors designed for modular construction', 'annotations': {'power_output': '<300 MWe', 'modularity': 'high', 'generation': 'III+/IV'}, 'aliases': ['Small Modular Reactor']},
    "VHTR": {'description': 'Generation IV reactor for very high temperature applications', 'annotations': {'temperature': '>950°C', 'generation': 'IV', 'coolant': 'helium'}, 'aliases': ['Very High Temperature Reactor']},
    "SFR": {'description': 'Fast reactor cooled by liquid sodium', 'annotations': {'coolant': 'liquid sodium', 'neutron_spectrum': 'fast', 'generation': 'IV'}, 'aliases': ['Sodium-Cooled Fast Reactor']},
    "LFR": {'description': 'Fast reactor cooled by liquid lead or lead-bismuth', 'annotations': {'coolant': 'liquid lead', 'neutron_spectrum': 'fast', 'generation': 'IV'}, 'aliases': ['Lead-Cooled Fast Reactor']},
    "GFR": {'description': 'Fast reactor with gas cooling', 'annotations': {'coolant': 'helium', 'neutron_spectrum': 'fast', 'generation': 'IV'}, 'aliases': ['Gas-Cooled Fast Reactor']},
    "SCWR": {'description': 'Reactor using supercritical water as coolant', 'annotations': {'coolant': 'supercritical water', 'generation': 'IV'}, 'aliases': ['Supercritical Water-Cooled Reactor']},
}

class ReactorGenerationEnum(RichEnum):
    """
    Nuclear reactor generational classifications
    """
    # Enum members
    GENERATION_I = "GENERATION_I"
    GENERATION_II = "GENERATION_II"
    GENERATION_III = "GENERATION_III"
    GENERATION_III_PLUS = "GENERATION_III_PLUS"
    GENERATION_IV = "GENERATION_IV"

# Set metadata after class creation
ReactorGenerationEnum._metadata = {
    "GENERATION_I": {'description': 'Early commercial reactors (1950s-1960s)', 'annotations': {'period': '1950s-1960s', 'status': 'retired', 'examples': 'Shippingport, Dresden-1'}},
    "GENERATION_II": {'description': 'Current operating commercial reactors', 'annotations': {'period': '1970s-1990s', 'status': 'operating', 'examples': 'PWR, BWR, CANDU', 'design_life': '40 years'}},
    "GENERATION_III": {'description': 'Advanced reactors with enhanced safety', 'annotations': {'period': '1990s-2010s', 'status': 'some operating', 'improvements': 'passive safety, standardization', 'examples': 'AP1000, EPR, ABWR'}},
    "GENERATION_III_PLUS": {'description': 'Evolutionary improvements to Generation III', 'annotations': {'period': '2000s-present', 'status': 'deployment', 'improvements': 'enhanced passive safety', 'examples': 'AP1000, APR1400'}},
    "GENERATION_IV": {'description': 'Next generation advanced reactor concepts', 'annotations': {'period': '2030s and beyond', 'status': 'development', 'goals': 'sustainability, economics, safety, proliferation resistance', 'examples': 'VHTR, SFR, LFR, GFR, SCWR, MSR'}},
}

class ReactorCoolantEnum(RichEnum):
    """
    Primary coolant types used in nuclear reactors
    """
    # Enum members
    LIGHT_WATER = "LIGHT_WATER"
    HEAVY_WATER = "HEAVY_WATER"
    CARBON_DIOXIDE = "CARBON_DIOXIDE"
    HELIUM = "HELIUM"
    LIQUID_SODIUM = "LIQUID_SODIUM"
    LIQUID_LEAD = "LIQUID_LEAD"
    MOLTEN_SALT = "MOLTEN_SALT"
    SUPERCRITICAL_WATER = "SUPERCRITICAL_WATER"

# Set metadata after class creation
ReactorCoolantEnum._metadata = {
    "LIGHT_WATER": {'description': 'Ordinary water as primary coolant', 'annotations': {'chemical_formula': 'H2O', 'density': '1.0 g/cm³', 'neutron_absorption': 'moderate'}},
    "HEAVY_WATER": {'description': 'Deuterium oxide as primary coolant', 'annotations': {'chemical_formula': 'D2O', 'density': '1.1 g/cm³', 'neutron_absorption': 'low'}},
    "CARBON_DIOXIDE": {'description': 'CO2 gas as primary coolant', 'annotations': {'chemical_formula': 'CO2', 'phase': 'gas', 'pressure': 'high'}},
    "HELIUM": {'description': 'Helium gas as primary coolant', 'annotations': {'chemical_formula': 'He', 'phase': 'gas', 'neutron_absorption': 'very low', 'temperature_capability': 'very high'}},
    "LIQUID_SODIUM": {'description': 'Molten sodium metal as coolant', 'annotations': {'chemical_formula': 'Na', 'phase': 'liquid', 'melting_point': '98°C', 'neutron_absorption': 'low'}},
    "LIQUID_LEAD": {'description': 'Molten lead or lead-bismuth as coolant', 'annotations': {'chemical_formula': 'Pb', 'phase': 'liquid', 'melting_point': '327°C', 'neutron_absorption': 'low'}},
    "MOLTEN_SALT": {'description': 'Molten fluoride or chloride salts', 'annotations': {'phase': 'liquid', 'temperature_capability': 'very high', 'neutron_absorption': 'variable'}},
    "SUPERCRITICAL_WATER": {'description': 'Water above critical point', 'annotations': {'chemical_formula': 'H2O', 'pressure': '>221 bar', 'temperature': '>374°C'}},
}

class ReactorModeratorEnum(RichEnum):
    """
    Neutron moderator types used in nuclear reactors
    """
    # Enum members
    LIGHT_WATER = "LIGHT_WATER"
    HEAVY_WATER = "HEAVY_WATER"
    GRAPHITE = "GRAPHITE"
    BERYLLIUM = "BERYLLIUM"
    NONE = "NONE"

# Set metadata after class creation
ReactorModeratorEnum._metadata = {
    "LIGHT_WATER": {'description': 'Ordinary water as neutron moderator', 'annotations': {'chemical_formula': 'H2O', 'moderation_effectiveness': 'good', 'neutron_absorption': 'moderate'}},
    "HEAVY_WATER": {'description': 'Deuterium oxide as neutron moderator', 'annotations': {'chemical_formula': 'D2O', 'moderation_effectiveness': 'excellent', 'neutron_absorption': 'very low'}},
    "GRAPHITE": {'description': 'Carbon graphite as neutron moderator', 'annotations': {'chemical_formula': 'C', 'moderation_effectiveness': 'good', 'neutron_absorption': 'low', 'temperature_resistance': 'high'}},
    "BERYLLIUM": {'description': 'Beryllium metal as neutron moderator', 'annotations': {'chemical_formula': 'Be', 'moderation_effectiveness': 'good', 'neutron_absorption': 'very low'}},
    "NONE": {'description': 'Fast reactors with no neutron moderation', 'annotations': {'neutron_spectrum': 'fast', 'moderation': 'none'}},
}

class ReactorNeutronSpectrumEnum(RichEnum):
    """
    Neutron energy spectrum classifications
    """
    # Enum members
    THERMAL = "THERMAL"
    EPITHERMAL = "EPITHERMAL"
    FAST = "FAST"

# Set metadata after class creation
ReactorNeutronSpectrumEnum._metadata = {
    "THERMAL": {'description': 'Low energy neutrons in thermal equilibrium', 'annotations': {'energy_range': '<1 eV', 'temperature_equivalent': 'room temperature', 'fission_probability': 'high for U-235'}},
    "EPITHERMAL": {'description': 'Intermediate energy neutrons', 'annotations': {'energy_range': '1 eV - 1 keV', 'temperature_equivalent': 'elevated'}},
    "FAST": {'description': 'High energy neutrons from fission', 'annotations': {'energy_range': '>1 keV', 'moderation': 'minimal or none', 'breeding_capability': 'high'}},
}

class ReactorSizeCategoryEnum(RichEnum):
    """
    Nuclear reactor size classifications
    """
    # Enum members
    LARGE = "LARGE"
    MEDIUM = "MEDIUM"
    SMALL = "SMALL"
    MICRO = "MICRO"
    RESEARCH = "RESEARCH"

# Set metadata after class creation
ReactorSizeCategoryEnum._metadata = {
    "LARGE": {'description': 'Traditional large-scale commercial reactors', 'annotations': {'power_output': '>700 MWe', 'construction': 'custom on-site'}},
    "MEDIUM": {'description': 'Mid-scale reactors', 'annotations': {'power_output': '300-700 MWe', 'construction': 'semi-modular'}},
    "SMALL": {'description': 'Small modular reactors', 'annotations': {'power_output': '50-300 MWe', 'construction': 'modular', 'transport': 'potentially transportable'}},
    "MICRO": {'description': 'Very small reactors for remote applications', 'annotations': {'power_output': '<50 MWe', 'construction': 'factory-built', 'transport': 'transportable'}},
    "RESEARCH": {'description': 'Small reactors for research and isotope production', 'annotations': {'power_output': '<100 MWt', 'primary_use': 'research, isotopes, training'}},
}

__all__ = [
    "ReactorTypeEnum",
    "ReactorGenerationEnum",
    "ReactorCoolantEnum",
    "ReactorModeratorEnum",
    "ReactorNeutronSpectrumEnum",
    "ReactorSizeCategoryEnum",
]