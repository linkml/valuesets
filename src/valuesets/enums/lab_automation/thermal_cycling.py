"""

Generated from: lab_automation/thermal_cycling.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class ThermalCyclerTypeEnum(RichEnum):
    """
    Types of thermal cycling instruments
    """
    # Enum members
    STANDARD_THERMAL_CYCLER = "STANDARD_THERMAL_CYCLER"
    REAL_TIME_PCR = "REAL_TIME_PCR"
    DIGITAL_PCR = "DIGITAL_PCR"
    GRADIENT_THERMAL_CYCLER = "GRADIENT_THERMAL_CYCLER"
    FAST_THERMAL_CYCLER = "FAST_THERMAL_CYCLER"
    AUTOMATED_THERMAL_CYCLER = "AUTOMATED_THERMAL_CYCLER"
    IN_SITU_THERMAL_CYCLER = "IN_SITU_THERMAL_CYCLER"

# Set metadata after class creation
ThermalCyclerTypeEnum._metadata = {
    "STANDARD_THERMAL_CYCLER": {'description': 'Standard thermal cycler for endpoint PCR'},
    "REAL_TIME_PCR": {'description': 'Thermal cycler with real-time fluorescence detection', 'annotations': {'abbreviation': 'qPCR'}},
    "DIGITAL_PCR": {'description': 'Thermal cycler for digital PCR applications', 'annotations': {'abbreviation': 'dPCR'}},
    "GRADIENT_THERMAL_CYCLER": {'description': 'Thermal cycler capable of running temperature gradients across the block'},
    "FAST_THERMAL_CYCLER": {'description': 'Thermal cycler optimized for rapid cycling'},
    "AUTOMATED_THERMAL_CYCLER": {'description': 'Thermal cycler with integrated automation for high-throughput applications', 'annotations': {'example': 'Biometra TRobot II'}},
    "IN_SITU_THERMAL_CYCLER": {'description': 'Thermal cycler designed for in situ PCR applications'},
}

class PCROperationTypeEnum(RichEnum):
    """
    Types of PCR operations and techniques
    """
    # Enum members
    STANDARD_PCR = "STANDARD_PCR"
    QUANTITATIVE_PCR = "QUANTITATIVE_PCR"
    REVERSE_TRANSCRIPTION_PCR = "REVERSE_TRANSCRIPTION_PCR"
    RT_QPCR = "RT_QPCR"
    MULTIPLEX_PCR = "MULTIPLEX_PCR"
    NESTED_PCR = "NESTED_PCR"
    TOUCHDOWN_PCR = "TOUCHDOWN_PCR"
    HOT_START_PCR = "HOT_START_PCR"
    LONG_RANGE_PCR = "LONG_RANGE_PCR"
    COLONY_PCR = "COLONY_PCR"
    HIGH_FIDELITY_PCR = "HIGH_FIDELITY_PCR"
    DIGITAL_PCR = "DIGITAL_PCR"

# Set metadata after class creation
PCROperationTypeEnum._metadata = {
    "STANDARD_PCR": {'description': 'Standard endpoint PCR amplification'},
    "QUANTITATIVE_PCR": {'description': 'Real-time quantitative PCR', 'annotations': {'abbreviation': 'qPCR'}},
    "REVERSE_TRANSCRIPTION_PCR": {'description': 'PCR with reverse transcription step for RNA amplification', 'annotations': {'abbreviation': 'RT-PCR'}},
    "RT_QPCR": {'description': 'Real-time quantitative RT-PCR'},
    "MULTIPLEX_PCR": {'description': 'PCR amplifying multiple targets simultaneously'},
    "NESTED_PCR": {'description': 'Two-stage PCR for increased specificity'},
    "TOUCHDOWN_PCR": {'description': 'PCR with decreasing annealing temperature'},
    "HOT_START_PCR": {'description': 'PCR with heat-activated polymerase'},
    "LONG_RANGE_PCR": {'description': 'PCR optimized for amplifying long DNA fragments'},
    "COLONY_PCR": {'description': 'PCR directly from bacterial colonies'},
    "HIGH_FIDELITY_PCR": {'description': 'PCR using proofreading polymerases'},
    "DIGITAL_PCR": {'description': 'Absolute quantification PCR using partitioning'},
}

class DetectionModeEnum(RichEnum):
    """
    Detection modes for real-time PCR instruments
    """
    # Enum members
    SYBR_GREEN = "SYBR_GREEN"
    TAQMAN = "TAQMAN"
    MOLECULAR_BEACON = "MOLECULAR_BEACON"
    FRET = "FRET"
    SCORPION = "SCORPION"
    HYBRIDIZATION_PROBE = "HYBRIDIZATION_PROBE"
    MULTI_CHANNEL = "MULTI_CHANNEL"

# Set metadata after class creation
DetectionModeEnum._metadata = {
    "SYBR_GREEN": {'description': 'DNA-binding dye detection'},
    "TAQMAN": {'description': 'Hydrolysis probe-based detection'},
    "MOLECULAR_BEACON": {'description': 'Hairpin probe-based detection'},
    "FRET": {'description': 'Fluorescence resonance energy transfer detection', 'annotations': {'full_name': 'Fluorescence Resonance Energy Transfer'}},
    "SCORPION": {'description': 'Unimolecular probe-based detection'},
    "HYBRIDIZATION_PROBE": {'description': 'Two-probe FRET-based detection'},
    "MULTI_CHANNEL": {'description': 'Multi-channel fluorescence detection'},
}

class PCRPlateTypeEnum(RichEnum):
    """
    Types of plates used for PCR applications
    """
    # Enum members
    PCR_96_WELL = "PCR_96_WELL"
    PCR_384_WELL = "PCR_384_WELL"
    PCR_TUBE_STRIP = "PCR_TUBE_STRIP"
    INDIVIDUAL_PCR_TUBE = "INDIVIDUAL_PCR_TUBE"
    LOW_PROFILE_PLATE = "LOW_PROFILE_PLATE"
    SKIRTED_PLATE = "SKIRTED_PLATE"
    SEMI_SKIRTED_PLATE = "SEMI_SKIRTED_PLATE"

# Set metadata after class creation
PCRPlateTypeEnum._metadata = {
    "PCR_96_WELL": {'description': '96-well plate for PCR'},
    "PCR_384_WELL": {'description': '384-well plate for PCR'},
    "PCR_TUBE_STRIP": {'description': 'Strip of 8 or 12 PCR tubes'},
    "INDIVIDUAL_PCR_TUBE": {'description': 'Individual PCR tube'},
    "LOW_PROFILE_PLATE": {'description': 'Low-profile PCR plate for automated systems'},
    "SKIRTED_PLATE": {'description': 'PCR plate with skirted base for stability'},
    "SEMI_SKIRTED_PLATE": {'description': 'PCR plate with partial skirt'},
}

class ThermalCyclingStepEnum(RichEnum):
    """
    Steps in thermal cycling protocols
    """
    # Enum members
    INITIAL_DENATURATION = "INITIAL_DENATURATION"
    DENATURATION = "DENATURATION"
    ANNEALING = "ANNEALING"
    EXTENSION = "EXTENSION"
    FINAL_EXTENSION = "FINAL_EXTENSION"
    HOLD = "HOLD"
    MELT_CURVE = "MELT_CURVE"
    GRADIENT = "GRADIENT"

# Set metadata after class creation
ThermalCyclingStepEnum._metadata = {
    "INITIAL_DENATURATION": {'description': 'Initial high-temperature step to denature template DNA'},
    "DENATURATION": {'description': 'High-temperature step to separate DNA strands'},
    "ANNEALING": {'description': 'Cooling step to allow primer binding'},
    "EXTENSION": {'description': 'Temperature-optimized step for polymerase activity'},
    "FINAL_EXTENSION": {'description': 'Extended final extension step'},
    "HOLD": {'description': 'Temperature hold step'},
    "MELT_CURVE": {'description': 'Gradual temperature increase for melt curve analysis'},
    "GRADIENT": {'description': 'Temperature gradient across block'},
}

__all__ = [
    "ThermalCyclerTypeEnum",
    "PCROperationTypeEnum",
    "DetectionModeEnum",
    "PCRPlateTypeEnum",
    "ThermalCyclingStepEnum",
]