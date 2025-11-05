"""

Generated from: materials_science/material_types.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class MaterialClassEnum(RichEnum):
    """
    Major classes of materials
    """
    # Enum members
    METAL = "METAL"
    CERAMIC = "CERAMIC"
    POLYMER = "POLYMER"
    COMPOSITE = "COMPOSITE"
    SEMICONDUCTOR = "SEMICONDUCTOR"
    BIOMATERIAL = "BIOMATERIAL"
    NANOMATERIAL = "NANOMATERIAL"

# Set metadata after class creation
MaterialClassEnum._metadata = {
    "METAL": {'description': 'Metallic materials with metallic bonding', 'meaning': 'ENVO:01001069', 'aliases': ['Metal', 'METAL']},
    "CERAMIC": {'description': 'Inorganic non-metallic materials', 'meaning': 'ENVO:03501307'},
    "POLYMER": {'description': 'Large molecules composed of repeating units', 'meaning': 'CHEBI:60027'},
    "COMPOSITE": {'description': 'Materials made from two or more constituent materials', 'meaning': 'NCIT:C61520'},
    "SEMICONDUCTOR": {'description': 'Materials with electrical conductivity between conductors and insulators', 'meaning': 'NCIT:C172788'},
    "BIOMATERIAL": {'description': 'Materials designed to interact with biological systems', 'meaning': 'NCIT:C16338', 'aliases': ['Biomaterial', 'BIOMATERIAL']},
    "NANOMATERIAL": {'description': 'Materials with at least one dimension in nanoscale (1-100 nm)', 'meaning': 'NCIT:C62371'},
}

class PolymerTypeEnum(RichEnum):
    """
    Types of polymer materials
    """
    # Enum members
    THERMOPLASTIC = "THERMOPLASTIC"
    THERMOSET = "THERMOSET"
    ELASTOMER = "ELASTOMER"
    BIOPOLYMER = "BIOPOLYMER"
    CONDUCTING_POLYMER = "CONDUCTING_POLYMER"

# Set metadata after class creation
PolymerTypeEnum._metadata = {
    "THERMOPLASTIC": {'description': 'Polymer that becomes moldable above specific temperature', 'meaning': 'PATO:0040070'},
    "THERMOSET": {'description': 'Polymer that irreversibly hardens when cured', 'meaning': 'ENVO:06105005', 'aliases': ['thermosetting polymer', 'Thermoset', 'THERMOSET']},
    "ELASTOMER": {'description': 'Polymer with elastic properties', 'meaning': 'SNOMED:261777007', 'aliases': ['rubber']},
    "BIOPOLYMER": {'description': 'Polymer produced by living organisms', 'meaning': 'NCIT:C73478'},
    "CONDUCTING_POLYMER": {'description': 'Polymer that conducts electricity', 'aliases': ['conducting polymer']},
}

class MetalTypeEnum(RichEnum):
    """
    Types of metallic materials
    """
    # Enum members
    FERROUS = "FERROUS"
    NON_FERROUS = "NON_FERROUS"
    NOBLE_METAL = "NOBLE_METAL"
    REFRACTORY_METAL = "REFRACTORY_METAL"
    LIGHT_METAL = "LIGHT_METAL"
    HEAVY_METAL = "HEAVY_METAL"

# Set metadata after class creation
MetalTypeEnum._metadata = {
    "FERROUS": {'description': 'Iron-based metals and alloys', 'meaning': 'SNOMED:264354006', 'aliases': ['iron-based']},
    "NON_FERROUS": {'description': 'Metals and alloys not containing iron', 'meaning': 'SNOMED:264879001'},
    "NOBLE_METAL": {'description': 'Metals resistant to corrosion and oxidation'},
    "REFRACTORY_METAL": {'description': 'Metals with very high melting points (>2000°C)'},
    "LIGHT_METAL": {'description': 'Low density metals (density < 5 g/cm³)', 'meaning': 'SNOMED:65436002'},
    "HEAVY_METAL": {'description': 'High density metals (density > 5 g/cm³)', 'meaning': 'CHEBI:5631'},
}

class CompositeTypeEnum(RichEnum):
    """
    Types of composite materials
    """
    # Enum members
    FIBER_REINFORCED = "FIBER_REINFORCED"
    PARTICLE_REINFORCED = "PARTICLE_REINFORCED"
    LAMINAR_COMPOSITE = "LAMINAR_COMPOSITE"
    METAL_MATRIX_COMPOSITE = "METAL_MATRIX_COMPOSITE"
    CERAMIC_MATRIX_COMPOSITE = "CERAMIC_MATRIX_COMPOSITE"
    POLYMER_MATRIX_COMPOSITE = "POLYMER_MATRIX_COMPOSITE"

# Set metadata after class creation
CompositeTypeEnum._metadata = {
    "FIBER_REINFORCED": {'description': 'Composite with fiber reinforcement', 'aliases': ['FRC']},
    "PARTICLE_REINFORCED": {'description': 'Composite with particle reinforcement'},
    "LAMINAR_COMPOSITE": {'description': 'Composite with layered structure', 'aliases': ['laminate']},
    "METAL_MATRIX_COMPOSITE": {'description': 'Composite with metal matrix', 'aliases': ['MMC']},
    "CERAMIC_MATRIX_COMPOSITE": {'description': 'Composite with ceramic matrix', 'aliases': ['CMC']},
    "POLYMER_MATRIX_COMPOSITE": {'description': 'Composite with polymer matrix', 'aliases': ['PMC']},
}

__all__ = [
    "MaterialClassEnum",
    "PolymerTypeEnum",
    "MetalTypeEnum",
    "CompositeTypeEnum",
]