"""
Process Modeling Value Sets

Value sets describing how process flowsheets and unit operations are modeled and solved - unit-operation design/simulation methods, flowsheet solution approaches, and process simulator software. These cover the design_simulation_method and process_simulator fields of the PISCES Standard Flowsheet Format, which are otherwise free strings.

Generated from: process_engineering/process_modeling.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class DesignSimulationMethod(RichEnum):
    """
    Methods used to design or simulate unit operations, particularly separation columns - ranging from graphical and shortcut methods to rigorous stage-by-stage and rate-based models.
    """
    # Enum members
    MCCABE_THIELE = "MCCABE_THIELE"
    PONCHON_SAVARIT = "PONCHON_SAVARIT"
    FENSKE_UNDERWOOD_GILLILAND = "FENSKE_UNDERWOOD_GILLILAND"
    KREMSER = "KREMSER"
    MESH = "MESH"
    INSIDE_OUT = "INSIDE_OUT"
    RATE_BASED = "RATE_BASED"
    EQUILIBRIUM_STAGE = "EQUILIBRIUM_STAGE"
    SHORTCUT = "SHORTCUT"
    RIGOROUS = "RIGOROUS"
    PINCH_ANALYSIS = "PINCH_ANALYSIS"

# Set metadata after class creation
DesignSimulationMethod._metadata = {
    "MCCABE_THIELE": {'description': 'McCabe-Thiele graphical method for binary distillation', 'annotations': {'method_class': 'GRAPHICAL'}},
    "PONCHON_SAVARIT": {'description': 'Ponchon-Savarit enthalpy-composition graphical method for binary distillation', 'annotations': {'method_class': 'GRAPHICAL'}},
    "FENSKE_UNDERWOOD_GILLILAND": {'description': 'Fenske-Underwood-Gilliland shortcut method for multicomponent distillation', 'annotations': {'method_class': 'SHORTCUT', 'abbreviation': 'FUG'}},
    "KREMSER": {'description': 'Kremser shortcut method for absorber and stripper design', 'annotations': {'method_class': 'SHORTCUT'}},
    "MESH": {'description': 'Rigorous equilibrium-stage solution of the Material, Equilibrium, Summation and Heat (enthalpy) equations', 'annotations': {'method_class': 'RIGOROUS_EQUILIBRIUM'}},
    "INSIDE_OUT": {'description': 'Inside-out algorithm for rigorous equilibrium-stage column convergence', 'annotations': {'method_class': 'RIGOROUS_EQUILIBRIUM'}},
    "RATE_BASED": {'description': 'Rate-based (nonequilibrium) model accounting for mass and heat transfer rates', 'annotations': {'method_class': 'RATE_BASED'}},
    "EQUILIBRIUM_STAGE": {'description': 'Generic equilibrium-stage model assuming each stage reaches phase equilibrium', 'annotations': {'method_class': 'RIGOROUS_EQUILIBRIUM'}},
    "SHORTCUT": {'description': 'Generic shortcut / approximate design method', 'annotations': {'method_class': 'SHORTCUT'}},
    "RIGOROUS": {'description': 'Generic rigorous design method', 'annotations': {'method_class': 'RIGOROUS_EQUILIBRIUM'}},
    "PINCH_ANALYSIS": {'description': 'Pinch analysis for heat-exchanger network and energy integration', 'annotations': {'method_class': 'ENERGY_INTEGRATION'}},
}

class FlowsheetSolutionApproach(RichEnum):
    """
    The overall computational strategy used to converge a process flowsheet.
    """
    # Enum members
    SEQUENTIAL_MODULAR = "SEQUENTIAL_MODULAR"
    EQUATION_ORIENTED = "EQUATION_ORIENTED"
    SIMULTANEOUS_MODULAR = "SIMULTANEOUS_MODULAR"

# Set metadata after class creation
FlowsheetSolutionApproach._metadata = {
    "SEQUENTIAL_MODULAR": {'description': 'Units solved one at a time in sequence, iterating on recycle tear streams'},
    "EQUATION_ORIENTED": {'description': 'All model equations assembled and solved simultaneously'},
    "SIMULTANEOUS_MODULAR": {'description': 'Hybrid approach combining modular unit models with a simultaneous convergence layer'},
}

class ProcessSimulator(RichEnum):
    """
    Process simulation software packages used to model chemical and biochemical process flowsheets.
    """
    # Enum members
    ASPEN_PLUS = "ASPEN_PLUS"
    ASPEN_HYSYS = "ASPEN_HYSYS"
    ASPEN_CUSTOM_MODELER = "ASPEN_CUSTOM_MODELER"
    UNISIM_DESIGN = "UNISIM_DESIGN"
    PRO_II = "PRO_II"
    AVEVA_PROCESS_SIMULATION = "AVEVA_PROCESS_SIMULATION"
    CHEMCAD = "CHEMCAD"
    DWSIM = "DWSIM"
    COCO_SIMULATOR = "COCO_SIMULATOR"
    GPROMS = "GPROMS"
    PROSIMPLUS = "PROSIMPLUS"
    PETRO_SIM = "PETRO_SIM"
    BIOSTEAM = "BIOSTEAM"
    SUPERPRO_DESIGNER = "SUPERPRO_DESIGNER"
    IDAES = "IDAES"
    CAPE_OPEN = "CAPE_OPEN"

# Set metadata after class creation
ProcessSimulator._metadata = {
    "ASPEN_PLUS": {'description': 'Aspen Plus steady-state process simulator (AspenTech)'},
    "ASPEN_HYSYS": {'description': 'Aspen HYSYS process simulator (AspenTech)'},
    "ASPEN_CUSTOM_MODELER": {'description': 'Aspen Custom Modeler for user-defined unit operation models (AspenTech)'},
    "UNISIM_DESIGN": {'description': 'Honeywell UniSim Design process simulator'},
    "PRO_II": {'description': 'AVEVA Pro/II (formerly SimSci Pro/II) process simulator'},
    "AVEVA_PROCESS_SIMULATION": {'description': 'AVEVA Process Simulation (formerly SimCentral)'},
    "CHEMCAD": {'description': 'ChemCAD process simulator (Chemstations)'},
    "DWSIM": {'description': 'DWSIM open-source CAPE-OPEN process simulator'},
    "COCO_SIMULATOR": {'description': 'COCO/COFE free CAPE-OPEN flowsheeting environment'},
    "GPROMS": {'description': 'gPROMS equation-oriented process modeling environment (Siemens / PSE)'},
    "PROSIMPLUS": {'description': 'ProSimPlus steady-state process simulator (ProSim)'},
    "PETRO_SIM": {'description': 'KBC Petro-SIM process simulator'},
    "BIOSTEAM": {'description': 'BioSTEAM open-source biorefinery simulation and techno-economic analysis package'},
    "SUPERPRO_DESIGNER": {'description': 'SuperPro Designer batch and bioprocess simulator (Intelligen)'},
    "IDAES": {'description': 'IDAES open-source equation-oriented process systems engineering platform (US DOE)'},
    "CAPE_OPEN": {'description': 'A CAPE-OPEN compliant simulator or unit (interoperability standard, simulator unspecified)'},
}

__all__ = [
    "DesignSimulationMethod",
    "FlowsheetSolutionApproach",
    "ProcessSimulator",
]