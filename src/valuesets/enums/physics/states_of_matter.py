"""
valuesets-physics-states-of-matter

Physics-related value sets for states of matter

Generated from: physics/states_of_matter.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class StateOfMatterEnum(RichEnum):
    """
    The physical state or phase of matter
    """
    # Enum members
    SOLID = "SOLID"
    LIQUID = "LIQUID"
    GAS = "GAS"
    PLASMA = "PLASMA"
    BOSE_EINSTEIN_CONDENSATE = "BOSE_EINSTEIN_CONDENSATE"
    FERMIONIC_CONDENSATE = "FERMIONIC_CONDENSATE"
    SUPERCRITICAL_FLUID = "SUPERCRITICAL_FLUID"
    SUPERFLUID = "SUPERFLUID"
    SUPERSOLID = "SUPERSOLID"
    QUARK_GLUON_PLASMA = "QUARK_GLUON_PLASMA"

# Set metadata after class creation
StateOfMatterEnum._metadata = {
    "SOLID": {'description': 'A state of matter where particles are closely packed together with fixed positions', 'meaning': 'AFO:AFQ_0000112'},
    "LIQUID": {'description': 'A nearly incompressible fluid that conforms to the shape of its container', 'meaning': 'AFO:AFQ_0000113'},
    "GAS": {'description': 'A compressible fluid that expands to fill its container', 'meaning': 'AFO:AFQ_0000114'},
    "PLASMA": {'description': 'An ionized gas with freely moving charged particles', 'meaning': 'AFO:AFQ_0000115'},
    "BOSE_EINSTEIN_CONDENSATE": {'description': 'A state of matter formed at extremely low temperatures where particles occupy the same quantum state'},
    "FERMIONIC_CONDENSATE": {'description': 'A superfluid phase formed by fermionic particles at extremely low temperatures'},
    "SUPERCRITICAL_FLUID": {'description': 'A state where distinct liquid and gas phases do not exist'},
    "SUPERFLUID": {'description': 'A phase of matter with zero viscosity'},
    "SUPERSOLID": {'description': 'A spatially ordered material with superfluid properties'},
    "QUARK_GLUON_PLASMA": {'description': 'An extremely hot phase where quarks and gluons are not confined'},
}

__all__ = [
    "StateOfMatterEnum",
]