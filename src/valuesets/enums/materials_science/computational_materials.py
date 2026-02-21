"""
Computational Materials Science Value Sets

Value sets for computational materials methods and property prediction relevant to the DOE Materials Discovery and Design challenges

Generated from: materials_science/computational_materials.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class MaterialsSimulationType(RichEnum):
    """
    Computational simulation methods used in materials science for predicting structure, properties, and behavior of materials
    """
    # Enum members
    DENSITY_FUNCTIONAL_THEORY = "DENSITY_FUNCTIONAL_THEORY"
    MOLECULAR_DYNAMICS = "MOLECULAR_DYNAMICS"
    MONTE_CARLO = "MONTE_CARLO"
    PHASE_FIELD_MODELING = "PHASE_FIELD_MODELING"
    FINITE_ELEMENT_ANALYSIS = "FINITE_ELEMENT_ANALYSIS"
    CONTINUUM_MECHANICS = "CONTINUUM_MECHANICS"
    TIGHT_BINDING = "TIGHT_BINDING"
    AB_INITIO_MOLECULAR_DYNAMICS = "AB_INITIO_MOLECULAR_DYNAMICS"
    MACHINE_LEARNING_POTENTIAL = "MACHINE_LEARNING_POTENTIAL"
    COARSE_GRAINED_SIMULATION = "COARSE_GRAINED_SIMULATION"

# Set metadata after class creation
MaterialsSimulationType._metadata = {
    "DENSITY_FUNCTIONAL_THEORY": {'description': 'Quantum mechanical method for computing electronic structure based on electron density functionals'},
    "MOLECULAR_DYNAMICS": {'description': 'Simulation of atomic and molecular motion by numerically integrating equations of motion', 'meaning': 'NCIT:C18097'},
    "MONTE_CARLO": {'description': 'Stochastic simulation method using random sampling to explore configuration space', 'meaning': 'SWO:4000008'},
    "PHASE_FIELD_MODELING": {'description': 'Continuum method for simulating microstructure evolution using order parameter fields'},
    "FINITE_ELEMENT_ANALYSIS": {'description': 'Numerical method for solving partial differential equations by dividing a domain into discrete elements'},
    "CONTINUUM_MECHANICS": {'description': 'Modeling material behavior at the macroscopic scale using continuous field equations'},
    "TIGHT_BINDING": {'description': 'Semi-empirical quantum mechanical method using parameterized Hamiltonian matrices'},
    "AB_INITIO_MOLECULAR_DYNAMICS": {'description': 'Molecular dynamics with forces computed from first-principles electronic structure calculations'},
    "MACHINE_LEARNING_POTENTIAL": {'description': 'Interatomic potentials trained on quantum mechanical data using machine learning methods'},
    "COARSE_GRAINED_SIMULATION": {'description': 'Simulation using simplified representations that group atoms into larger effective interaction sites'},
}

class MaterialPropertyPredictionType(RichEnum):
    """
    Material properties that are commonly targeted for computational prediction in materials discovery and design
    """
    # Enum members
    BAND_GAP = "BAND_GAP"
    ELASTIC_MODULUS = "ELASTIC_MODULUS"
    THERMAL_CONDUCTIVITY = "THERMAL_CONDUCTIVITY"
    DIELECTRIC_CONSTANT = "DIELECTRIC_CONSTANT"
    MAGNETIC_MOMENT = "MAGNETIC_MOMENT"
    FORMATION_ENERGY = "FORMATION_ENERGY"
    SURFACE_ENERGY = "SURFACE_ENERGY"
    DEFECT_ENERGY = "DEFECT_ENERGY"
    PHASE_STABILITY = "PHASE_STABILITY"
    MECHANICAL_STRENGTH = "MECHANICAL_STRENGTH"

# Set metadata after class creation
MaterialPropertyPredictionType._metadata = {
    "BAND_GAP": {'description': 'Energy difference between the valence band and conduction band in a semiconductor or insulator'},
    "ELASTIC_MODULUS": {'description': 'Measure of material stiffness defined as the ratio of stress to strain in the elastic regime'},
    "THERMAL_CONDUCTIVITY": {'description': 'Ability of a material to conduct heat, measured in watts per meter-kelvin', 'meaning': 'PATO:0001756'},
    "DIELECTRIC_CONSTANT": {'description': 'Ratio of the permittivity of a material to the permittivity of free space'},
    "MAGNETIC_MOMENT": {'description': 'Magnetic dipole moment of a material arising from electron spin and orbital contributions'},
    "FORMATION_ENERGY": {'description': 'Energy required to form a compound from its constituent elements in their standard states'},
    "SURFACE_ENERGY": {'description': 'Excess energy at the surface of a material relative to its bulk'},
    "DEFECT_ENERGY": {'description': 'Energy associated with the formation or migration of point defects and dislocations'},
    "PHASE_STABILITY": {'description': 'Thermodynamic stability of a material phase relative to competing phases'},
    "MECHANICAL_STRENGTH": {'description': 'Maximum stress a material can withstand before failure under applied load'},
}

__all__ = [
    "MaterialsSimulationType",
    "MaterialPropertyPredictionType",
]