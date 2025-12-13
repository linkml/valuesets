"""

Generated from: materials_science/characterization_methods.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class MicroscopyMethodEnum(RichEnum):
    """
    Microscopy techniques for material characterization
    """
    # Enum members
    SEM = "SEM"
    TEM = "TEM"
    STEM = "STEM"
    AFM = "AFM"
    STM = "STM"
    OPTICAL = "OPTICAL"
    CONFOCAL = "CONFOCAL"

# Set metadata after class creation
MicroscopyMethodEnum._metadata = {
    "SEM": {'description': 'Scanning Electron Microscopy', 'meaning': 'CHMO:0000073', 'aliases': ['Scanning Electron Microscopy', 'SEM']},
    "TEM": {'description': 'Transmission Electron Microscopy', 'meaning': 'CHMO:0000080', 'aliases': ['Transmission Electron Microscopy', 'TEM']},
    "STEM": {'description': 'Scanning Transmission Electron Microscopy', 'aliases': ['Scanning Transmission Electron Microscopy']},
    "AFM": {'description': 'Atomic Force Microscopy', 'meaning': 'CHMO:0000113', 'aliases': ['Atomic Force Microscopy', 'AFM']},
    "STM": {'description': 'Scanning Tunneling Microscopy', 'meaning': 'CHMO:0000132', 'aliases': ['Scanning Tunneling Microscopy', 'STM']},
    "OPTICAL": {'description': 'Optical/Light Microscopy', 'meaning': 'CHMO:0000102', 'aliases': ['Light Microscopy', 'Optical Microscopy', 'OPTICAL']},
    "CONFOCAL": {'description': 'Confocal Laser Scanning Microscopy', 'meaning': 'CHMO:0000089', 'aliases': ['CLSM', 'CONFOCAL', 'Confocal']},
}

class SpectroscopyMethodEnum(RichEnum):
    """
    Spectroscopy techniques for material analysis
    """
    # Enum members
    XRD = "XRD"
    XPS = "XPS"
    EDS = "EDS"
    FTIR = "FTIR"
    RAMAN = "RAMAN"
    UV_VIS = "UV_VIS"
    NMR = "NMR"
    XRF = "XRF"

# Set metadata after class creation
SpectroscopyMethodEnum._metadata = {
    "XRD": {'description': 'X-ray Diffraction', 'meaning': 'CHMO:0000156', 'aliases': ['X-ray Diffraction']},
    "XPS": {'description': 'X-ray Photoelectron Spectroscopy', 'meaning': 'CHMO:0000404', 'aliases': ['ESCA', 'X-ray Photoelectron Spectroscopy']},
    "EDS": {'description': 'Energy Dispersive X-ray Spectroscopy', 'meaning': 'CHMO:0000309', 'aliases': ['EDX', 'EDXS', 'EDS']},
    "FTIR": {'description': 'Fourier Transform Infrared Spectroscopy', 'meaning': 'CHMO:0000636', 'aliases': ['FT-IR', 'FTIR']},
    "RAMAN": {'description': 'Raman Spectroscopy', 'meaning': 'CHMO:0000656', 'aliases': ['Raman Spectroscopy']},
    "UV_VIS": {'description': 'Ultraviolet-Visible Spectroscopy', 'meaning': 'CHMO:0000292', 'aliases': ['UV-Visible', 'UV-Vis', 'UV_VIS']},
    "NMR": {'description': 'Nuclear Magnetic Resonance Spectroscopy', 'meaning': 'CHMO:0000591', 'aliases': ['Nuclear Magnetic Resonance', 'NMR']},
    "XRF": {'description': 'X-ray Fluorescence Spectroscopy', 'meaning': 'CHMO:0000307', 'aliases': ['X-ray Fluorescence', 'XRF']},
}

class ThermalAnalysisMethodEnum(RichEnum):
    """
    Thermal analysis techniques
    """
    # Enum members
    DSC = "DSC"
    TGA = "TGA"
    DTA = "DTA"
    TMA = "TMA"
    DMTA = "DMTA"

# Set metadata after class creation
ThermalAnalysisMethodEnum._metadata = {
    "DSC": {'description': 'Differential Scanning Calorimetry', 'meaning': 'CHMO:0000684', 'aliases': ['Differential Scanning Calorimetry']},
    "TGA": {'description': 'Thermogravimetric Analysis', 'meaning': 'CHMO:0000690', 'aliases': ['Thermogravimetric Analysis', 'TGA']},
    "DTA": {'description': 'Differential Thermal Analysis', 'meaning': 'CHMO:0000687', 'aliases': ['Differential Thermal Analysis']},
    "TMA": {'description': 'Thermomechanical Analysis', 'aliases': ['Thermomechanical Analysis']},
    "DMTA": {'description': 'Dynamic Mechanical Thermal Analysis', 'aliases': ['DMA', 'Dynamic Mechanical Analysis']},
}

class MechanicalTestingMethodEnum(RichEnum):
    """
    Mechanical testing methods
    """
    # Enum members
    TENSILE = "TENSILE"
    COMPRESSION = "COMPRESSION"
    HARDNESS = "HARDNESS"
    IMPACT = "IMPACT"
    FATIGUE = "FATIGUE"
    CREEP = "CREEP"
    FRACTURE_TOUGHNESS = "FRACTURE_TOUGHNESS"
    NANOINDENTATION = "NANOINDENTATION"

# Set metadata after class creation
MechanicalTestingMethodEnum._metadata = {
    "TENSILE": {'description': 'Tensile strength testing'},
    "COMPRESSION": {'description': 'Compression strength testing'},
    "HARDNESS": {'description': 'Hardness testing (Vickers, Rockwell, Brinell)'},
    "IMPACT": {'description': 'Impact resistance testing (Charpy, Izod)'},
    "FATIGUE": {'description': 'Fatigue testing under cyclic loading'},
    "CREEP": {'description': 'Creep testing under sustained load'},
    "FRACTURE_TOUGHNESS": {'description': 'Fracture toughness testing'},
    "NANOINDENTATION": {'description': 'Nanoindentation for nanoscale mechanical properties'},
}

__all__ = [
    "MicroscopyMethodEnum",
    "SpectroscopyMethodEnum",
    "ThermalAnalysisMethodEnum",
    "MechanicalTestingMethodEnum",
]