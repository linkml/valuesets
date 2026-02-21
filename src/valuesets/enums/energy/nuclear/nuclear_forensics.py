"""
Nuclear Forensics Value Sets

Value sets for nuclear forensics and attribution relevant to the DOE Nuclear Threat Assessment and Attribution challenges

Generated from: energy/nuclear/nuclear_forensics.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class NuclearForensicsMethodType(RichEnum):
    """
    Analytical methods used in nuclear forensics for material characterization and attribution
    """
    # Enum members
    ISOTOPE_RATIO_ANALYSIS = "ISOTOPE_RATIO_ANALYSIS"
    MASS_SPECTROMETRY = "MASS_SPECTROMETRY"
    GAMMA_SPECTROSCOPY = "GAMMA_SPECTROSCOPY"
    ALPHA_SPECTROSCOPY = "ALPHA_SPECTROSCOPY"
    NEUTRON_ACTIVATION_ANALYSIS = "NEUTRON_ACTIVATION_ANALYSIS"
    RADIOCHEMICAL_SEPARATION = "RADIOCHEMICAL_SEPARATION"
    ELECTRON_MICROSCOPY = "ELECTRON_MICROSCOPY"
    X_RAY_FLUORESCENCE = "X_RAY_FLUORESCENCE"
    AGE_DATING = "AGE_DATING"

# Set metadata after class creation
NuclearForensicsMethodType._metadata = {
    "ISOTOPE_RATIO_ANALYSIS": {'description': 'Measurement of relative abundances of isotopes to determine material origin and processing history', 'meaning': 'CHMO:0000506'},
    "MASS_SPECTROMETRY": {'description': 'Analytical technique measuring mass-to-charge ratios for elemental and isotopic composition', 'meaning': 'CHMO:0000470'},
    "GAMMA_SPECTROSCOPY": {'description': 'Measurement of gamma-ray energies emitted by radioactive materials for isotope identification', 'meaning': 'CHMO:0000414'},
    "ALPHA_SPECTROSCOPY": {'description': 'Measurement of alpha particle energies for characterizing alpha-emitting radionuclides', 'meaning': 'CHMO:0000230'},
    "NEUTRON_ACTIVATION_ANALYSIS": {'description': 'Elemental analysis by irradiating samples with neutrons and measuring induced radioactivity', 'meaning': 'CHMO:0000782'},
    "RADIOCHEMICAL_SEPARATION": {'description': 'Chemical separation of radionuclides from a sample matrix for individual measurement'},
    "ELECTRON_MICROSCOPY": {'description': 'Microscopic imaging and analysis of nuclear material morphology and microstructure', 'meaning': 'CHMO:0000068'},
    "X_RAY_FLUORESCENCE": {'description': 'Elemental analysis by measuring characteristic X-rays emitted after X-ray excitation', 'meaning': 'CHMO:0000307'},
    "AGE_DATING": {'description': 'Determination of the time since last chemical purification of nuclear material using parent-daughter ratios'},
}

class NuclearThreatCategoryType(RichEnum):
    """
    Categories of nuclear and radiological threat scenarios for security assessment
    """
    # Enum members
    IMPROVISED_NUCLEAR_DEVICE = "IMPROVISED_NUCLEAR_DEVICE"
    RADIOLOGICAL_DISPERSAL_DEVICE = "RADIOLOGICAL_DISPERSAL_DEVICE"
    NUCLEAR_FACILITY_SABOTAGE = "NUCLEAR_FACILITY_SABOTAGE"
    NUCLEAR_MATERIAL_THEFT = "NUCLEAR_MATERIAL_THEFT"
    NUCLEAR_SMUGGLING = "NUCLEAR_SMUGGLING"
    ENVIRONMENTAL_RELEASE = "ENVIRONMENTAL_RELEASE"

# Set metadata after class creation
NuclearThreatCategoryType._metadata = {
    "IMPROVISED_NUCLEAR_DEVICE": {'description': 'A crude nuclear weapon constructed from diverted or stolen fissile material', 'meaning': 'NCIT:C120576'},
    "RADIOLOGICAL_DISPERSAL_DEVICE": {'description': 'A device that disperses radioactive material using conventional explosives or other means', 'meaning': 'NCIT:C120580'},
    "NUCLEAR_FACILITY_SABOTAGE": {'description': 'Deliberate sabotage of a nuclear facility to cause radiological release'},
    "NUCLEAR_MATERIAL_THEFT": {'description': 'Theft or diversion of nuclear or radioactive material from authorized control'},
    "NUCLEAR_SMUGGLING": {'description': 'Illicit trafficking and transport of nuclear or radioactive materials across borders'},
    "ENVIRONMENTAL_RELEASE": {'description': 'Unauthorized or accidental release of radioactive material into the environment'},
}

__all__ = [
    "NuclearForensicsMethodType",
    "NuclearThreatCategoryType",
]