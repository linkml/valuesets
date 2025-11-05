"""

Generated from: materials_science/material_properties.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class ElectricalConductivityEnum(RichEnum):
    """
    Classification of materials by electrical conductivity
    """
    # Enum members
    CONDUCTOR = "CONDUCTOR"
    SEMICONDUCTOR = "SEMICONDUCTOR"
    INSULATOR = "INSULATOR"
    SUPERCONDUCTOR = "SUPERCONDUCTOR"

# Set metadata after class creation
ElectricalConductivityEnum._metadata = {
    "CONDUCTOR": {'description': 'Material with high electrical conductivity (resistivity < 10^-5 Ω·m)', 'aliases': ['metal']},
    "SEMICONDUCTOR": {'description': 'Material with intermediate electrical conductivity (10^-5 to 10^8 Ω·m)', 'meaning': 'NCIT:C172788', 'aliases': ['semi']},
    "INSULATOR": {'description': 'Material with very low electrical conductivity (resistivity > 10^8 Ω·m)', 'aliases': ['dielectric']},
    "SUPERCONDUCTOR": {'description': 'Material with zero electrical resistance below critical temperature'},
}

class MagneticPropertyEnum(RichEnum):
    """
    Classification of materials by magnetic properties
    """
    # Enum members
    DIAMAGNETIC = "DIAMAGNETIC"
    PARAMAGNETIC = "PARAMAGNETIC"
    FERROMAGNETIC = "FERROMAGNETIC"
    FERRIMAGNETIC = "FERRIMAGNETIC"
    ANTIFERROMAGNETIC = "ANTIFERROMAGNETIC"

# Set metadata after class creation
MagneticPropertyEnum._metadata = {
    "DIAMAGNETIC": {'description': 'Weakly repelled by magnetic fields'},
    "PARAMAGNETIC": {'description': 'Weakly attracted to magnetic fields'},
    "FERROMAGNETIC": {'description': 'Strongly attracted to magnetic fields, can be permanently magnetized'},
    "FERRIMAGNETIC": {'description': 'Similar to ferromagnetic but with opposing magnetic moments'},
    "ANTIFERROMAGNETIC": {'description': 'Adjacent magnetic moments cancel each other'},
}

class OpticalPropertyEnum(RichEnum):
    """
    Optical properties of materials
    """
    # Enum members
    TRANSPARENT = "TRANSPARENT"
    TRANSLUCENT = "TRANSLUCENT"
    OPAQUE = "OPAQUE"
    REFLECTIVE = "REFLECTIVE"
    ABSORBING = "ABSORBING"
    FLUORESCENT = "FLUORESCENT"
    PHOSPHORESCENT = "PHOSPHORESCENT"

# Set metadata after class creation
OpticalPropertyEnum._metadata = {
    "TRANSPARENT": {'description': 'Allows light to pass through with minimal scattering', 'meaning': 'PATO:0000964'},
    "TRANSLUCENT": {'description': 'Allows light to pass through but with significant scattering'},
    "OPAQUE": {'description': 'Does not allow light to pass through', 'meaning': 'PATO:0000963'},
    "REFLECTIVE": {'description': 'Reflects most incident light'},
    "ABSORBING": {'description': 'Absorbs most incident light'},
    "FLUORESCENT": {'description': 'Emits light when excited by radiation'},
    "PHOSPHORESCENT": {'description': 'Continues to emit light after excitation stops'},
}

class ThermalConductivityEnum(RichEnum):
    """
    Classification by thermal conductivity
    """
    # Enum members
    HIGH_THERMAL_CONDUCTOR = "HIGH_THERMAL_CONDUCTOR"
    MODERATE_THERMAL_CONDUCTOR = "MODERATE_THERMAL_CONDUCTOR"
    THERMAL_INSULATOR = "THERMAL_INSULATOR"

# Set metadata after class creation
ThermalConductivityEnum._metadata = {
    "HIGH_THERMAL_CONDUCTOR": {'description': 'High thermal conductivity (>100 W/m·K)', 'aliases': ['thermal conductor']},
    "MODERATE_THERMAL_CONDUCTOR": {'description': 'Moderate thermal conductivity (1-100 W/m·K)'},
    "THERMAL_INSULATOR": {'description': 'Low thermal conductivity (<1 W/m·K)', 'aliases': ['thermal barrier']},
}

class MechanicalBehaviorEnum(RichEnum):
    """
    Mechanical behavior of materials under stress
    """
    # Enum members
    ELASTIC = "ELASTIC"
    PLASTIC = "PLASTIC"
    BRITTLE = "BRITTLE"
    DUCTILE = "DUCTILE"
    MALLEABLE = "MALLEABLE"
    TOUGH = "TOUGH"
    VISCOELASTIC = "VISCOELASTIC"

# Set metadata after class creation
MechanicalBehaviorEnum._metadata = {
    "ELASTIC": {'description': 'Returns to original shape after stress removal', 'meaning': 'PATO:0001171'},
    "PLASTIC": {'description': 'Undergoes permanent deformation under stress', 'meaning': 'PATO:0001172'},
    "BRITTLE": {'description': 'Breaks without significant plastic deformation', 'meaning': 'PATO:0002477'},
    "DUCTILE": {'description': 'Can be drawn into wires, undergoes large plastic deformation'},
    "MALLEABLE": {'description': 'Can be hammered into sheets'},
    "TOUGH": {'description': 'High resistance to fracture'},
    "VISCOELASTIC": {'description': 'Exhibits both viscous and elastic characteristics'},
}

__all__ = [
    "ElectricalConductivityEnum",
    "MagneticPropertyEnum",
    "OpticalPropertyEnum",
    "ThermalConductivityEnum",
    "MechanicalBehaviorEnum",
]