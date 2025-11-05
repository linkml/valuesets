"""

Generated from: materials_science/crystal_structures.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class CrystalSystemEnum(RichEnum):
    """
    The seven crystal systems in crystallography
    """
    # Enum members
    TRICLINIC = "TRICLINIC"
    MONOCLINIC = "MONOCLINIC"
    ORTHORHOMBIC = "ORTHORHOMBIC"
    TETRAGONAL = "TETRAGONAL"
    TRIGONAL = "TRIGONAL"
    HEXAGONAL = "HEXAGONAL"
    CUBIC = "CUBIC"

# Set metadata after class creation
CrystalSystemEnum._metadata = {
    "TRICLINIC": {'description': 'Crystal system with no symmetry constraints (a≠b≠c, α≠β≠γ≠90°)', 'meaning': 'ENM:9000022', 'aliases': ['anorthic']},
    "MONOCLINIC": {'description': 'Crystal system with one twofold axis of symmetry (a≠b≠c, α=γ=90°≠β)', 'meaning': 'ENM:9000029'},
    "ORTHORHOMBIC": {'description': 'Crystal system with three mutually perpendicular axes (a≠b≠c, α=β=γ=90°)', 'meaning': 'ENM:9000031', 'aliases': ['rhombic']},
    "TETRAGONAL": {'description': 'Crystal system with one fourfold axis (a=b≠c, α=β=γ=90°)', 'meaning': 'ENM:9000032'},
    "TRIGONAL": {'description': 'Crystal system with one threefold axis (a=b=c, α=β=γ≠90°)', 'meaning': 'ENM:9000054', 'aliases': ['rhombohedral']},
    "HEXAGONAL": {'description': 'Crystal system with one sixfold axis (a=b≠c, α=β=90°, γ=120°)', 'meaning': 'PATO:0002509'},
    "CUBIC": {'description': 'Crystal system with four threefold axes (a=b=c, α=β=γ=90°)', 'meaning': 'ENM:9000035', 'aliases': ['isometric']},
}

class BravaisLatticeEnum(RichEnum):
    """
    The 14 Bravais lattices describing all possible crystal lattices
    """
    # Enum members
    PRIMITIVE_TRICLINIC = "PRIMITIVE_TRICLINIC"
    PRIMITIVE_MONOCLINIC = "PRIMITIVE_MONOCLINIC"
    BASE_CENTERED_MONOCLINIC = "BASE_CENTERED_MONOCLINIC"
    PRIMITIVE_ORTHORHOMBIC = "PRIMITIVE_ORTHORHOMBIC"
    BASE_CENTERED_ORTHORHOMBIC = "BASE_CENTERED_ORTHORHOMBIC"
    BODY_CENTERED_ORTHORHOMBIC = "BODY_CENTERED_ORTHORHOMBIC"
    FACE_CENTERED_ORTHORHOMBIC = "FACE_CENTERED_ORTHORHOMBIC"
    PRIMITIVE_TETRAGONAL = "PRIMITIVE_TETRAGONAL"
    BODY_CENTERED_TETRAGONAL = "BODY_CENTERED_TETRAGONAL"
    PRIMITIVE_TRIGONAL = "PRIMITIVE_TRIGONAL"
    PRIMITIVE_HEXAGONAL = "PRIMITIVE_HEXAGONAL"
    PRIMITIVE_CUBIC = "PRIMITIVE_CUBIC"
    BODY_CENTERED_CUBIC = "BODY_CENTERED_CUBIC"
    FACE_CENTERED_CUBIC = "FACE_CENTERED_CUBIC"

# Set metadata after class creation
BravaisLatticeEnum._metadata = {
    "PRIMITIVE_TRICLINIC": {'description': 'Primitive triclinic lattice (aP)', 'aliases': ['aP']},
    "PRIMITIVE_MONOCLINIC": {'description': 'Primitive monoclinic lattice (mP)', 'aliases': ['mP']},
    "BASE_CENTERED_MONOCLINIC": {'description': 'Base-centered monoclinic lattice (mC)', 'aliases': ['mC', 'mS']},
    "PRIMITIVE_ORTHORHOMBIC": {'description': 'Primitive orthorhombic lattice (oP)', 'aliases': ['oP']},
    "BASE_CENTERED_ORTHORHOMBIC": {'description': 'Base-centered orthorhombic lattice (oC)', 'aliases': ['oC', 'oS']},
    "BODY_CENTERED_ORTHORHOMBIC": {'description': 'Body-centered orthorhombic lattice (oI)', 'aliases': ['oI']},
    "FACE_CENTERED_ORTHORHOMBIC": {'description': 'Face-centered orthorhombic lattice (oF)', 'aliases': ['oF']},
    "PRIMITIVE_TETRAGONAL": {'description': 'Primitive tetragonal lattice (tP)', 'aliases': ['tP']},
    "BODY_CENTERED_TETRAGONAL": {'description': 'Body-centered tetragonal lattice (tI)', 'aliases': ['tI']},
    "PRIMITIVE_TRIGONAL": {'description': 'Primitive trigonal/rhombohedral lattice (hR)', 'aliases': ['hR']},
    "PRIMITIVE_HEXAGONAL": {'description': 'Primitive hexagonal lattice (hP)', 'aliases': ['hP']},
    "PRIMITIVE_CUBIC": {'description': 'Simple cubic lattice (cP)', 'aliases': ['cP', 'SC']},
    "BODY_CENTERED_CUBIC": {'description': 'Body-centered cubic lattice (cI)', 'aliases': ['cI', 'BCC']},
    "FACE_CENTERED_CUBIC": {'description': 'Face-centered cubic lattice (cF)', 'aliases': ['cF', 'FCC']},
}

__all__ = [
    "CrystalSystemEnum",
    "BravaisLatticeEnum",
]