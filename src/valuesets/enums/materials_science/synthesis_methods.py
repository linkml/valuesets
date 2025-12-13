"""

Generated from: materials_science/synthesis_methods.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class SynthesisMethodEnum(RichEnum):
    """
    Common material synthesis and processing methods
    """
    # Enum members
    SOL_GEL = "SOL_GEL"
    HYDROTHERMAL = "HYDROTHERMAL"
    SOLVOTHERMAL = "SOLVOTHERMAL"
    CVD = "CVD"
    PVD = "PVD"
    ALD = "ALD"
    ELECTRODEPOSITION = "ELECTRODEPOSITION"
    BALL_MILLING = "BALL_MILLING"
    PRECIPITATION = "PRECIPITATION"
    SINTERING = "SINTERING"
    MELT_PROCESSING = "MELT_PROCESSING"
    SOLUTION_CASTING = "SOLUTION_CASTING"
    SPIN_COATING = "SPIN_COATING"
    DIP_COATING = "DIP_COATING"
    SPRAY_COATING = "SPRAY_COATING"

# Set metadata after class creation
SynthesisMethodEnum._metadata = {
    "SOL_GEL": {'description': 'Synthesis from solution through gel formation', 'aliases': ['sol-gel process']},
    "HYDROTHERMAL": {'description': 'Synthesis using high temperature aqueous solutions', 'aliases': ['hydrothermal synthesis']},
    "SOLVOTHERMAL": {'description': 'Synthesis using non-aqueous solvents at high temperature/pressure'},
    "CVD": {'description': 'Chemical Vapor Deposition', 'meaning': 'CHMO:0001314', 'aliases': ['Chemical Vapor Deposition', 'CVD']},
    "PVD": {'description': 'Physical Vapor Deposition', 'meaning': 'CHMO:0001356', 'aliases': ['Physical Vapor Deposition', 'PVD']},
    "ALD": {'description': 'Atomic Layer Deposition', 'aliases': ['Atomic Layer Deposition']},
    "ELECTRODEPOSITION": {'description': 'Deposition using electric current', 'meaning': 'CHMO:0001331', 'aliases': ['electroplating', 'Electrodeposition', 'ELECTRODEPOSITION']},
    "BALL_MILLING": {'description': 'Mechanical alloying using ball mill', 'aliases': ['mechanical alloying']},
    "PRECIPITATION": {'description': 'Formation of solid from solution', 'meaning': 'CHMO:0001688', 'aliases': ['Precipitation', 'PRECIPITATION']},
    "SINTERING": {'description': 'Compacting and forming solid mass by heat/pressure'},
    "MELT_PROCESSING": {'description': 'Processing from molten state', 'aliases': ['melt casting']},
    "SOLUTION_CASTING": {'description': 'Casting from solution'},
    "SPIN_COATING": {'description': 'Coating by spinning substrate', 'meaning': 'CHMO:0001472'},
    "DIP_COATING": {'description': 'Coating by dipping in solution', 'meaning': 'CHMO:0001471'},
    "SPRAY_COATING": {'description': 'Coating by spraying'},
}

class CrystalGrowthMethodEnum(RichEnum):
    """
    Methods for growing single crystals
    """
    # Enum members
    CZOCHRALSKI = "CZOCHRALSKI"
    BRIDGMAN = "BRIDGMAN"
    FLOAT_ZONE = "FLOAT_ZONE"
    FLUX_GROWTH = "FLUX_GROWTH"
    VAPOR_TRANSPORT = "VAPOR_TRANSPORT"
    HYDROTHERMAL_GROWTH = "HYDROTHERMAL_GROWTH"
    LPE = "LPE"
    MBE = "MBE"
    MOCVD = "MOCVD"

# Set metadata after class creation
CrystalGrowthMethodEnum._metadata = {
    "CZOCHRALSKI": {'description': 'Crystal pulling from melt', 'aliases': ['CZ', 'crystal pulling']},
    "BRIDGMAN": {'description': 'Directional solidification method', 'aliases': ['Bridgman-Stockbarger']},
    "FLOAT_ZONE": {'description': 'Zone melting without crucible', 'aliases': ['FZ', 'zone refining']},
    "FLUX_GROWTH": {'description': 'Crystal growth from high temperature solution'},
    "VAPOR_TRANSPORT": {'description': 'Crystal growth via vapor phase transport', 'aliases': ['CVT']},
    "HYDROTHERMAL_GROWTH": {'description': 'Crystal growth in aqueous solution under pressure'},
    "LPE": {'description': 'Liquid Phase Epitaxy', 'aliases': ['Liquid Phase Epitaxy']},
    "MBE": {'description': 'Molecular Beam Epitaxy', 'meaning': 'CHMO:0001341', 'aliases': ['Molecular Beam Epitaxy', 'MBE']},
    "MOCVD": {'description': 'Metal-Organic Chemical Vapor Deposition', 'aliases': ['MOVPE']},
}

class AdditiveManufacturingEnum(RichEnum):
    """
    3D printing and additive manufacturing methods
    """
    # Enum members
    FDM = "FDM"
    SLA = "SLA"
    SLS = "SLS"
    SLM = "SLM"
    EBM = "EBM"
    BINDER_JETTING = "BINDER_JETTING"
    MATERIAL_JETTING = "MATERIAL_JETTING"
    DED = "DED"

# Set metadata after class creation
AdditiveManufacturingEnum._metadata = {
    "FDM": {'description': 'Fused Deposition Modeling', 'aliases': ['FFF', 'Fused Filament Fabrication']},
    "SLA": {'description': 'Stereolithography', 'aliases': ['Stereolithography']},
    "SLS": {'description': 'Selective Laser Sintering', 'aliases': ['Selective Laser Sintering']},
    "SLM": {'description': 'Selective Laser Melting', 'aliases': ['Selective Laser Melting']},
    "EBM": {'description': 'Electron Beam Melting', 'aliases': ['Electron Beam Melting']},
    "BINDER_JETTING": {'description': 'Powder bed with liquid binder'},
    "MATERIAL_JETTING": {'description': 'Droplet deposition of materials', 'aliases': ['PolyJet']},
    "DED": {'description': 'Directed Energy Deposition', 'aliases': ['Directed Energy Deposition']},
}

__all__ = [
    "SynthesisMethodEnum",
    "CrystalGrowthMethodEnum",
    "AdditiveManufacturingEnum",
]