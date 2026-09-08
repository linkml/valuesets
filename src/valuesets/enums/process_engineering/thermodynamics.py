"""
Process Thermodynamics Value Sets

Value sets for the thermodynamic models used in process simulation - equations of state, activity-coefficient (excess Gibbs energy) models, mixing rules, Poynting corrections, and the named property packages that combine them. These cover the thermo_property_package fields (mixture, gamma, phi, PCF) of the PISCES Standard Flowsheet Format, which are otherwise free strings.

Generated from: process_engineering/thermodynamics.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class EquationOfStateModel(RichEnum):
    """
    Equations of state used to compute fugacity coefficients and PVT behavior of fluids in process simulation (the SFF phi method).
    """
    # Enum members
    IDEAL_GAS = "IDEAL_GAS"
    VIRIAL = "VIRIAL"
    REDLICH_KWONG = "REDLICH_KWONG"
    SOAVE_REDLICH_KWONG = "SOAVE_REDLICH_KWONG"
    PENG_ROBINSON = "PENG_ROBINSON"
    PENG_ROBINSON_BOSTON_MATHIAS = "PENG_ROBINSON_BOSTON_MATHIAS"
    SRK_BOSTON_MATHIAS = "SRK_BOSTON_MATHIAS"
    LEE_KESLER_PLOCKER = "LEE_KESLER_PLOCKER"
    BENEDICT_WEBB_RUBIN_STARLING = "BENEDICT_WEBB_RUBIN_STARLING"
    PREDICTIVE_SRK = "PREDICTIVE_SRK"
    PC_SAFT = "PC_SAFT"
    CUBIC_PLUS_ASSOCIATION = "CUBIC_PLUS_ASSOCIATION"
    GERG_2008 = "GERG_2008"
    IAPWS_95 = "IAPWS_95"

# Set metadata after class creation
EquationOfStateModel._metadata = {
    "IDEAL_GAS": {'description': 'Ideal gas law, assuming no intermolecular interactions'},
    "VIRIAL": {'description': 'Virial equation of state expressed as a power series in density or pressure'},
    "REDLICH_KWONG": {'description': 'Redlich-Kwong cubic equation of state', 'annotations': {'abbreviation': 'RK'}},
    "SOAVE_REDLICH_KWONG": {'description': 'Soave modification of the Redlich-Kwong cubic equation of state', 'annotations': {'abbreviation': 'SRK'}},
    "PENG_ROBINSON": {'description': 'Peng-Robinson cubic equation of state', 'annotations': {'abbreviation': 'PR'}},
    "PENG_ROBINSON_BOSTON_MATHIAS": {'description': 'Peng-Robinson with Boston-Mathias alpha function for supercritical extrapolation', 'annotations': {'abbreviation': 'PR-BM'}},
    "SRK_BOSTON_MATHIAS": {'description': 'Soave-Redlich-Kwong with Boston-Mathias alpha function', 'annotations': {'abbreviation': 'SRK-BM'}},
    "LEE_KESLER_PLOCKER": {'description': 'Lee-Kesler-Plocker corresponding-states equation of state', 'annotations': {'abbreviation': 'LKP'}},
    "BENEDICT_WEBB_RUBIN_STARLING": {'description': 'Benedict-Webb-Rubin-Starling equation of state for light hydrocarbons', 'annotations': {'abbreviation': 'BWRS'}},
    "PREDICTIVE_SRK": {'description': 'Predictive SRK combining SRK with a UNIFAC-based mixing rule', 'annotations': {'abbreviation': 'PSRK'}},
    "PC_SAFT": {'description': 'Perturbed-chain statistical associating fluid theory equation of state', 'annotations': {'abbreviation': 'PC-SAFT'}},
    "CUBIC_PLUS_ASSOCIATION": {'description': 'Cubic-plus-association equation of state for associating fluids', 'annotations': {'abbreviation': 'CPA'}},
    "GERG_2008": {'description': 'GERG-2008 reference equation of state for natural gas mixtures'},
    "IAPWS_95": {'description': 'IAPWS-95 reference formulation for the thermodynamic properties of water', 'annotations': {'aliases': 'steam tables'}},
}

class ActivityCoefficientModel(RichEnum):
    """
    Excess Gibbs energy / activity-coefficient models for non-ideal liquid phases (the SFF gamma method).
    """
    # Enum members
    IDEAL = "IDEAL"
    MARGULES = "MARGULES"
    VAN_LAAR = "VAN_LAAR"
    REGULAR_SOLUTION = "REGULAR_SOLUTION"
    WILSON = "WILSON"
    NRTL = "NRTL"
    ELECTROLYTE_NRTL = "ELECTROLYTE_NRTL"
    UNIQUAC = "UNIQUAC"
    UNIFAC = "UNIFAC"
    UNIFAC_DORTMUND = "UNIFAC_DORTMUND"
    FLORY_HUGGINS = "FLORY_HUGGINS"
    PITZER = "PITZER"
    COSMO_SAC = "COSMO_SAC"

# Set metadata after class creation
ActivityCoefficientModel._metadata = {
    "IDEAL": {'description': "Ideal solution, all activity coefficients equal to one (Raoult's law)"},
    "MARGULES": {'description': 'Margules two-parameter activity-coefficient model'},
    "VAN_LAAR": {'description': 'Van Laar activity-coefficient model'},
    "REGULAR_SOLUTION": {'description': 'Scatchard-Hildebrand regular solution model based on solubility parameters'},
    "WILSON": {'description': 'Wilson local-composition activity-coefficient model'},
    "NRTL": {'description': 'Non-random two-liquid local-composition activity-coefficient model'},
    "ELECTROLYTE_NRTL": {'description': 'Electrolyte NRTL model for systems containing ions', 'annotations': {'abbreviation': 'eNRTL'}},
    "UNIQUAC": {'description': 'Universal quasi-chemical activity-coefficient model'},
    "UNIFAC": {'description': 'UNIQUAC functional-group activity-coefficient (group-contribution) model'},
    "UNIFAC_DORTMUND": {'description': 'Modified UNIFAC (Dortmund) group-contribution model'},
    "FLORY_HUGGINS": {'description': 'Flory-Huggins model for polymer solutions'},
    "PITZER": {'description': 'Pitzer model for aqueous electrolyte activity coefficients'},
    "COSMO_SAC": {'description': 'COSMO-based segment activity-coefficient model from quantum chemistry', 'annotations': {'aliases': 'COSMO-RS, COSMO-SAC'}},
}

class ThermodynamicPropertyPackage(RichEnum):
    """
    Named property methods/packages offered by process simulators, typically combining an equation of state and/or an activity-coefficient model. Used where a single package label rather than separate gamma/phi methods is recorded.
    """
    # Enum members
    IDEAL = "IDEAL"
    NRTL = "NRTL"
    NRTL_RK = "NRTL_RK"
    UNIQUAC = "UNIQUAC"
    UNIFAC = "UNIFAC"
    WILSON = "WILSON"
    VAN_LAAR = "VAN_LAAR"
    PENG_ROBINSON = "PENG_ROBINSON"
    SOAVE_REDLICH_KWONG = "SOAVE_REDLICH_KWONG"
    ELECTROLYTE_NRTL = "ELECTROLYTE_NRTL"
    PITZER = "PITZER"
    CHAO_SEADER = "CHAO_SEADER"
    GRAYSON_STREED = "GRAYSON_STREED"
    BRAUN_K10 = "BRAUN_K10"
    PC_SAFT = "PC_SAFT"
    STEAM_TABLES = "STEAM_TABLES"
    API_SOUR = "API_SOUR"

# Set metadata after class creation
ThermodynamicPropertyPackage._metadata = {
    "IDEAL": {'description': "Ideal (Raoult's law) property package"},
    "NRTL": {'description': 'NRTL activity model with ideal or RK vapor phase'},
    "NRTL_RK": {'description': 'NRTL activity model with Redlich-Kwong vapor phase'},
    "UNIQUAC": {'description': 'UNIQUAC activity model property package'},
    "UNIFAC": {'description': 'UNIFAC group-contribution property package'},
    "WILSON": {'description': 'Wilson activity model property package'},
    "VAN_LAAR": {'description': 'Van Laar activity model property package'},
    "PENG_ROBINSON": {'description': 'Peng-Robinson equation-of-state property package'},
    "SOAVE_REDLICH_KWONG": {'description': 'Soave-Redlich-Kwong equation-of-state property package'},
    "ELECTROLYTE_NRTL": {'description': 'Electrolyte NRTL property package for ionic systems'},
    "PITZER": {'description': 'Pitzer property package for aqueous electrolytes'},
    "CHAO_SEADER": {'description': 'Chao-Seader semi-empirical package for hydrocarbon systems'},
    "GRAYSON_STREED": {'description': 'Grayson-Streed package for hydrogen-rich hydrocarbon systems'},
    "BRAUN_K10": {'description': 'Braun K10 package for low-pressure heavy hydrocarbon systems', 'annotations': {'abbreviation': 'BK10'}},
    "PC_SAFT": {'description': 'PC-SAFT equation-of-state property package'},
    "STEAM_TABLES": {'description': 'Steam-table (IAPWS / ASME) property package for water and steam'},
    "API_SOUR": {'description': 'API sour-water package for systems with acid gases and ammonia'},
}

class MixingRuleModel(RichEnum):
    """
    Mixing rules applied to equation-of-state parameters for mixtures (the SFF mixture method).
    """
    # Enum members
    IDEAL = "IDEAL"
    VAN_DER_WAALS = "VAN_DER_WAALS"
    HURON_VIDAL = "HURON_VIDAL"
    MODIFIED_HURON_VIDAL = "MODIFIED_HURON_VIDAL"
    WONG_SANDLER = "WONG_SANDLER"
    PSRK_MIXING = "PSRK_MIXING"

# Set metadata after class creation
MixingRuleModel._metadata = {
    "IDEAL": {'description': 'Ideal mixing, no excess properties'},
    "VAN_DER_WAALS": {'description': 'Classical van der Waals one-fluid mixing rule with binary interaction parameters', 'annotations': {'aliases': 'classical, quadratic mixing rule'}},
    "HURON_VIDAL": {'description': 'Huron-Vidal mixing rule coupling an equation of state to an excess Gibbs energy model'},
    "MODIFIED_HURON_VIDAL": {'description': 'Modified Huron-Vidal first/second order mixing rules', 'annotations': {'aliases': 'MHV1, MHV2'}},
    "WONG_SANDLER": {'description': 'Wong-Sandler mixing rule with correct low- and high-density limits'},
    "PSRK_MIXING": {'description': 'Predictive SRK (PSRK) mixing rule based on UNIFAC'},
}

class PoyntingCorrectionMethod(RichEnum):
    """
    Treatment of the Poynting correction factor accounting for the effect of pressure on liquid fugacity (the SFF PCF method).
    """
    # Enum members
    NONE = "NONE"
    POYNTING = "POYNTING"

# Set metadata after class creation
PoyntingCorrectionMethod._metadata = {
    "NONE": {'description': 'No Poynting correction applied'},
    "POYNTING": {'description': 'Poynting correction factor applied to the liquid fugacity'},
}

__all__ = [
    "EquationOfStateModel",
    "ActivityCoefficientModel",
    "ThermodynamicPropertyPackage",
    "MixingRuleModel",
    "PoyntingCorrectionMethod",
]