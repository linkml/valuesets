"""
Microelectronics Value Sets

Value sets for semiconductor and microelectronics types relevant to the DOE Recentering Microelectronics challenge

Generated from: computing/microelectronics.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class SemiconductorMaterialType(RichEnum):
    """
    Types of semiconductor materials used in microelectronics fabrication
    """
    # Enum members
    SILICON = "SILICON"
    GALLIUM_ARSENIDE = "GALLIUM_ARSENIDE"
    SILICON_CARBIDE = "SILICON_CARBIDE"
    GALLIUM_NITRIDE = "GALLIUM_NITRIDE"
    INDIUM_PHOSPHIDE = "INDIUM_PHOSPHIDE"
    GERMANIUM = "GERMANIUM"
    SILICON_GERMANIUM = "SILICON_GERMANIUM"
    DIAMOND = "DIAMOND"

# Set metadata after class creation
SemiconductorMaterialType._metadata = {
    "SILICON": {'description': 'Elemental silicon, the most widely used semiconductor material', 'meaning': 'CHEBI:27573'},
    "GALLIUM_ARSENIDE": {'description': 'Gallium arsenide (GaAs) compound semiconductor for high-frequency applications'},
    "SILICON_CARBIDE": {'description': 'Silicon carbide (SiC) wide-bandgap semiconductor for high-power applications', 'meaning': 'CHEBI:29390'},
    "GALLIUM_NITRIDE": {'description': 'Gallium nitride (GaN) wide-bandgap semiconductor for power electronics and LEDs'},
    "INDIUM_PHOSPHIDE": {'description': 'Indium phosphide (InP) compound semiconductor for optoelectronics and fiber communications', 'meaning': 'CHEBI:82281'},
    "GERMANIUM": {'description': 'Elemental germanium semiconductor used in high-speed transistors and detectors', 'meaning': 'CHEBI:30441'},
    "SILICON_GERMANIUM": {'description': 'Silicon-germanium (SiGe) alloy semiconductor for heterojunction bipolar transistors'},
    "DIAMOND": {'description': 'Diamond as an ultra-wide-bandgap semiconductor for extreme environment electronics', 'meaning': 'CHEBI:33417'},
}

class ChipFabricationNodeType(RichEnum):
    """
    Semiconductor fabrication process node sizes defining transistor feature dimensions
    """
    # Enum members
    NODE_3NM = "NODE_3NM"
    NODE_5NM = "NODE_5NM"
    NODE_7NM = "NODE_7NM"
    NODE_10NM = "NODE_10NM"
    NODE_14NM = "NODE_14NM"
    NODE_22NM = "NODE_22NM"
    NODE_28NM = "NODE_28NM"
    NODE_45NM = "NODE_45NM"
    MATURE_NODE = "MATURE_NODE"

# Set metadata after class creation
ChipFabricationNodeType._metadata = {
    "NODE_3NM": {'description': '3 nanometer process node', 'annotations': {'feature_size': '3nm'}},
    "NODE_5NM": {'description': '5 nanometer process node', 'annotations': {'feature_size': '5nm'}},
    "NODE_7NM": {'description': '7 nanometer process node', 'annotations': {'feature_size': '7nm'}},
    "NODE_10NM": {'description': '10 nanometer process node', 'annotations': {'feature_size': '10nm'}},
    "NODE_14NM": {'description': '14 nanometer process node', 'annotations': {'feature_size': '14nm'}},
    "NODE_22NM": {'description': '22 nanometer process node', 'annotations': {'feature_size': '22nm'}},
    "NODE_28NM": {'description': '28 nanometer process node', 'annotations': {'feature_size': '28nm'}},
    "NODE_45NM": {'description': '45 nanometer process node', 'annotations': {'feature_size': '45nm'}},
    "MATURE_NODE": {'description': 'Mature fabrication node (65nm and larger) for legacy and specialty applications', 'annotations': {'feature_size': '65nm+'}},
}

__all__ = [
    "SemiconductorMaterialType",
    "ChipFabricationNodeType",
]