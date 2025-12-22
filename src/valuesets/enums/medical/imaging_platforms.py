"""
Medical Imaging Platform Value Sets

Value sets for medical imaging platforms and instruments including MRI scanners, microscopy systems, and other imaging devices. Organized by manufacturer and field strength where applicable.

Generated from: medical/imaging_platforms.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class MRIPlatformEnum(RichEnum):
    """
    Specific MRI scanner models from major manufacturers. Includes field strength information (1.5T, 3T, 7T) for proper data interpretation.
    """
    # Enum members
    SIEMENS_AVANTO_1_5T = "SIEMENS_AVANTO_1_5T"
    SIEMENS_AVANTO_FIT_1_5T = "SIEMENS_AVANTO_FIT_1_5T"
    SIEMENS_AERA_1_5T = "SIEMENS_AERA_1_5T"
    SIEMENS_ESPREE_1_5T = "SIEMENS_ESPREE_1_5T"
    SIEMENS_TRIO_3T = "SIEMENS_TRIO_3T"
    SIEMENS_VERIO_3T = "SIEMENS_VERIO_3T"
    SIEMENS_SKYRA_3T = "SIEMENS_SKYRA_3T"
    SIEMENS_PRISMA_3T = "SIEMENS_PRISMA_3T"
    SIEMENS_PRISMA_FIT_3T = "SIEMENS_PRISMA_FIT_3T"
    GE_SIGNA_EXCITE_1_5T = "GE_SIGNA_EXCITE_1_5T"
    GE_SIGNA_GENESIS_1_5T = "GE_SIGNA_GENESIS_1_5T"
    GE_SIGNA_HDXT_1_5T = "GE_SIGNA_HDXT_1_5T"
    GE_OPTIMA_MR450W_1_5T = "GE_OPTIMA_MR450W_1_5T"
    GE_SIGNA_HDXT_3T = "GE_SIGNA_HDXT_3T"
    GE_DISCOVERY_MR750_3T = "GE_DISCOVERY_MR750_3T"
    GE_SIGNA_PREMIER_3T = "GE_SIGNA_PREMIER_3T"
    PHILIPS_PANORAMA_1_0T = "PHILIPS_PANORAMA_1_0T"
    PHILIPS_ACHIEVA_1_5T = "PHILIPS_ACHIEVA_1_5T"
    PHILIPS_INGENIA_1_5T = "PHILIPS_INGENIA_1_5T"
    PHILIPS_ACHIEVA_3T = "PHILIPS_ACHIEVA_3T"
    PHILIPS_INTERA_ACHIEVA_3T = "PHILIPS_INTERA_ACHIEVA_3T"
    PHILIPS_INGENIA_3T = "PHILIPS_INGENIA_3T"
    HITACHI_ECHELON_1_5T = "HITACHI_ECHELON_1_5T"
    HITACHI_OASIS_1_2T = "HITACHI_OASIS_1_2T"
    TOSHIBA_VANTAGE_TITAN_1_5T = "TOSHIBA_VANTAGE_TITAN_1_5T"
    BRUKER_BIOSPEC_7T = "BRUKER_BIOSPEC_7T"

# Set metadata after class creation
MRIPlatformEnum._metadata = {
    "SIEMENS_AVANTO_1_5T": {'description': 'Siemens Magnetom Avanto 1.5T MRI scanner', 'annotations': {'manufacturer': 'Siemens', 'field_strength': '1.5T'}, 'aliases': ['Siemens Avanto 1.5T']},
    "SIEMENS_AVANTO_FIT_1_5T": {'description': 'Siemens Magnetom Avanto Fit 1.5T MRI scanner', 'annotations': {'manufacturer': 'Siemens', 'field_strength': '1.5T'}, 'aliases': ['Siemens Avanto Fit 1.5T']},
    "SIEMENS_AERA_1_5T": {'description': 'Siemens Magnetom Aera 1.5T MRI scanner', 'annotations': {'manufacturer': 'Siemens', 'field_strength': '1.5T'}, 'aliases': ['Siemens Magnetom Aera 1.5T']},
    "SIEMENS_ESPREE_1_5T": {'description': 'Siemens Magnetom Espree 1.5T MRI scanner', 'annotations': {'manufacturer': 'Siemens', 'field_strength': '1.5T'}, 'aliases': ['Siemens Magnetom Espree 1.5T']},
    "SIEMENS_TRIO_3T": {'description': 'Siemens Magnetom Trio 3T MRI scanner', 'annotations': {'manufacturer': 'Siemens', 'field_strength': '3T'}, 'aliases': ['Siemens Magnetom Trio 3T']},
    "SIEMENS_VERIO_3T": {'description': 'Siemens Magnetom Verio 3T MRI scanner', 'annotations': {'manufacturer': 'Siemens', 'field_strength': '3T'}, 'aliases': ['Siemens Magnetom Verio 3T']},
    "SIEMENS_SKYRA_3T": {'description': 'Siemens Magnetom Skyra 3T MRI scanner', 'annotations': {'manufacturer': 'Siemens', 'field_strength': '3T'}, 'aliases': ['Siemens Magnetom Skyra 3T']},
    "SIEMENS_PRISMA_3T": {'description': 'Siemens Magnetom Prisma 3T MRI scanner', 'annotations': {'manufacturer': 'Siemens', 'field_strength': '3T'}, 'aliases': ['Siemens Magnetom Prisma 3T']},
    "SIEMENS_PRISMA_FIT_3T": {'description': 'Siemens Magnetom Prisma Fit 3T MRI scanner', 'annotations': {'manufacturer': 'Siemens', 'field_strength': '3T'}, 'aliases': ['Siemens Magnetom Prisma Fit 3T']},
    "GE_SIGNA_EXCITE_1_5T": {'description': 'GE Signa Excite 1.5T MRI scanner', 'annotations': {'manufacturer': 'GE Healthcare', 'field_strength': '1.5T'}, 'aliases': ['GE Signa Excite 1.5T']},
    "GE_SIGNA_GENESIS_1_5T": {'description': 'GE Signa Genesis 1.5T MRI scanner', 'annotations': {'manufacturer': 'GE Healthcare', 'field_strength': '1.5T'}, 'aliases': ['GE Signa Genesis 1.5T']},
    "GE_SIGNA_HDXT_1_5T": {'description': 'GE Signa HDxt 1.5T MRI scanner', 'annotations': {'manufacturer': 'GE Healthcare', 'field_strength': '1.5T'}, 'aliases': ['GE Signa HDxt 1.5T']},
    "GE_OPTIMA_MR450W_1_5T": {'description': 'GE Optima MR450W 1.5T MRI scanner', 'annotations': {'manufacturer': 'GE Healthcare', 'field_strength': '1.5T'}, 'aliases': ['GE Optima MR450W 1.5T']},
    "GE_SIGNA_HDXT_3T": {'description': 'GE Signa HDxt 3T MRI scanner', 'annotations': {'manufacturer': 'GE Healthcare', 'field_strength': '3T'}, 'aliases': ['GE Signa HDxt 3T']},
    "GE_DISCOVERY_MR750_3T": {'description': 'GE Discovery MR750 3T MRI scanner', 'annotations': {'manufacturer': 'GE Healthcare', 'field_strength': '3T'}, 'aliases': ['GE Discovery MR750 3T']},
    "GE_SIGNA_PREMIER_3T": {'description': 'GE Signa Premier 3T MRI scanner', 'annotations': {'manufacturer': 'GE Healthcare', 'field_strength': '3T'}, 'aliases': ['GE Signa Premier 3T']},
    "PHILIPS_PANORAMA_1_0T": {'description': 'Philips Panorama 1.0T MRI scanner', 'annotations': {'manufacturer': 'Philips Healthcare', 'field_strength': '1.0T'}, 'aliases': ['Philips Panorama 1.0T']},
    "PHILIPS_ACHIEVA_1_5T": {'description': 'Philips Achieva 1.5T MRI scanner', 'annotations': {'manufacturer': 'Philips Healthcare', 'field_strength': '1.5T'}, 'aliases': ['Philips Achieva 1.5T']},
    "PHILIPS_INGENIA_1_5T": {'description': 'Philips Ingenia 1.5T MRI scanner', 'annotations': {'manufacturer': 'Philips Healthcare', 'field_strength': '1.5T'}, 'aliases': ['Philips Ingenia 1.5T']},
    "PHILIPS_ACHIEVA_3T": {'description': 'Philips Achieva 3T MRI scanner', 'annotations': {'manufacturer': 'Philips Healthcare', 'field_strength': '3T'}, 'aliases': ['Philips Achieva 3T']},
    "PHILIPS_INTERA_ACHIEVA_3T": {'description': 'Philips Intera Achieva 3T MRI scanner', 'annotations': {'manufacturer': 'Philips Healthcare', 'field_strength': '3T'}, 'aliases': ['Philips Intera Achieva 3T']},
    "PHILIPS_INGENIA_3T": {'description': 'Philips Ingenia 3T MRI scanner', 'annotations': {'manufacturer': 'Philips Healthcare', 'field_strength': '3T'}, 'aliases': ['Philips Ingenia 3T']},
    "HITACHI_ECHELON_1_5T": {'description': 'Hitachi Echelon 1.5T MRI scanner', 'annotations': {'manufacturer': 'Hitachi', 'field_strength': '1.5T'}, 'aliases': ['Hitachi Echelon 1.5T']},
    "HITACHI_OASIS_1_2T": {'description': 'Hitachi Oasis 1.2T MRI scanner', 'annotations': {'manufacturer': 'Hitachi', 'field_strength': '1.2T'}, 'aliases': ['Hitachi Oasis 1.2T']},
    "TOSHIBA_VANTAGE_TITAN_1_5T": {'description': 'Toshiba Vantage Titan 1.5T MRI scanner', 'annotations': {'manufacturer': 'Toshiba/Canon', 'field_strength': '1.5T'}, 'aliases': ['Toshiba Vantage Titan 1.5T']},
    "BRUKER_BIOSPEC_7T": {'description': 'Bruker Biospec 7T research MRI scanner', 'annotations': {'manufacturer': 'Bruker', 'field_strength': '7T', 'type': 'research'}, 'aliases': ['7T Bruker Biospec']},
}

class MicroscopyPlatformEnum(RichEnum):
    """
    Microscopy imaging systems and platforms
    """
    # Enum members
    ZEISS_LSM_700 = "ZEISS_LSM_700"
    ZEISS_LSM_980 = "ZEISS_LSM_980"
    ZEISS_LSM = "ZEISS_LSM"
    LEICA_APERIO_AT2 = "LEICA_APERIO_AT2"
    APERIO_CS2 = "APERIO_CS2"
    LEICA_MZ16 = "LEICA_MZ16"
    LEICA_S9 = "LEICA_S9"
    OLYMPUS_IX73 = "OLYMPUS_IX73"
    OLYMPUS_DP80 = "OLYMPUS_DP80"
    PANNORAMIC_250_FLASH = "PANNORAMIC_250_FLASH"
    PHILIPS_FEI_TECNAI_12 = "PHILIPS_FEI_TECNAI_12"
    ECHO_CONFOCAL = "ECHO_CONFOCAL"

# Set metadata after class creation
MicroscopyPlatformEnum._metadata = {
    "ZEISS_LSM_700": {'description': 'Zeiss LSM 700 confocal microscope', 'annotations': {'manufacturer': 'Zeiss', 'type': 'confocal'}, 'aliases': ['Zeiss LSM 700']},
    "ZEISS_LSM_980": {'description': 'Zeiss LSM 980 confocal microscope', 'annotations': {'manufacturer': 'Zeiss', 'type': 'confocal'}, 'aliases': ['Zeiss LSM 980']},
    "ZEISS_LSM": {'description': 'Zeiss LSM confocal microscope (general)', 'annotations': {'manufacturer': 'Zeiss', 'type': 'confocal'}, 'aliases': ['Zeiss LSM']},
    "LEICA_APERIO_AT2": {'description': 'Leica Aperio AT2 whole slide scanner', 'annotations': {'manufacturer': 'Leica', 'type': 'slide scanner'}, 'aliases': ['Leica Aperio AT2']},
    "APERIO_CS2": {'description': 'Aperio CS2 slide scanner', 'annotations': {'manufacturer': 'Leica', 'type': 'slide scanner'}, 'aliases': ['Aperio CS2']},
    "LEICA_MZ16": {'description': 'Leica MZ16 stereomicroscope', 'annotations': {'manufacturer': 'Leica', 'type': 'stereomicroscope'}, 'aliases': ['Leica MZ16']},
    "LEICA_S9": {'description': 'Leica S9 stereomicroscope', 'annotations': {'manufacturer': 'Leica', 'type': 'stereomicroscope'}, 'aliases': ['Leica S9 Stereomicroscope']},
    "OLYMPUS_IX73": {'description': 'Olympus IX73 inverted microscope', 'annotations': {'manufacturer': 'Olympus', 'type': 'inverted fluorescence'}, 'aliases': ['Olympus IX73']},
    "OLYMPUS_DP80": {'description': 'Olympus DP80 camera system', 'annotations': {'manufacturer': 'Olympus', 'type': 'camera'}, 'aliases': ['Olympus DP80']},
    "PANNORAMIC_250_FLASH": {'description': '3DHISTECH Pannoramic 250 Flash slide scanner', 'annotations': {'manufacturer': '3DHISTECH', 'type': 'slide scanner'}, 'aliases': ['Pannoramic 250 Flash']},
    "PHILIPS_FEI_TECNAI_12": {'description': 'Philips FEI Tecnai 12 electron microscope', 'annotations': {'manufacturer': 'FEI/Thermo Fisher', 'type': 'TEM'}, 'aliases': ['Philips FEI Tecnai 12']},
    "ECHO_CONFOCAL": {'description': 'ECHO confocal imaging system', 'annotations': {'type': 'confocal'}, 'aliases': ['ECHO Confocal']},
}

class ImagingSystemPlatformEnum(RichEnum):
    """
    Other imaging systems including plate readers, flow cytometers, and specialized systems
    """
    # Enum members
    ENVISION_MULTIPLATE_READER = "ENVISION_MULTIPLATE_READER"
    SPECTRAMAX_M_SERIES = "SPECTRAMAX_M_SERIES"
    VARIOSKAN_LUX = "VARIOSKAN_LUX"
    PROMEGA_GLOMAX_DISCOVER = "PROMEGA_GLOMAX_DISCOVER"
    BD_FACS_CALIBUR = "BD_FACS_CALIBUR"
    BD_FACSSYMPHONY = "BD_FACSSYMPHONY"
    IVIS_SPECTRUM = "IVIS_SPECTRUM"
    NANOSTRING_COSMX = "NANOSTRING_COSMX"
    NANOSTRING_GEOMX = "NANOSTRING_GEOMX"
    VISIUM_10X = "VISIUM_10X"
    VEVO_3100 = "VEVO_3100"
    VENTANA_BENCHMARK_XT = "VENTANA_BENCHMARK_XT"
    VECTRA_H1 = "VECTRA_H1"
    XF24_EXTRACELLULAR_FLUX = "XF24_EXTRACELLULAR_FLUX"
    LICOR_ODYSSEY_CLX = "LICOR_ODYSSEY_CLX"
    BIORAD_CHEMIDOC_MP = "BIORAD_CHEMIDOC_MP"

# Set metadata after class creation
ImagingSystemPlatformEnum._metadata = {
    "ENVISION_MULTIPLATE_READER": {'description': 'PerkinElmer EnVision 2103 Multiplate Reader', 'annotations': {'manufacturer': 'PerkinElmer', 'type': 'plate reader'}, 'aliases': ['EnVision 2103 Multiplate Reader']},
    "SPECTRAMAX_M_SERIES": {'description': 'Molecular Devices SpectraMax M Series', 'annotations': {'manufacturer': 'Molecular Devices', 'type': 'plate reader'}, 'aliases': ['Spectramax M Series']},
    "VARIOSKAN_LUX": {'description': 'Thermo Scientific Varioskan LUX', 'annotations': {'manufacturer': 'Thermo Fisher', 'type': 'plate reader'}, 'aliases': ['Varioskan LUX']},
    "PROMEGA_GLOMAX_DISCOVER": {'description': 'Promega GloMax Discover', 'annotations': {'manufacturer': 'Promega', 'type': 'plate reader'}, 'aliases': ['Promega GloMax Discover']},
    "BD_FACS_CALIBUR": {'description': 'BD FACS Calibur flow cytometer', 'annotations': {'manufacturer': 'BD Biosciences', 'type': 'flow cytometer'}, 'aliases': ['BD FACS Calibur']},
    "BD_FACSSYMPHONY": {'description': 'BD FACSymphony flow cytometer', 'annotations': {'manufacturer': 'BD Biosciences', 'type': 'flow cytometer'}, 'aliases': ['BD FACSymphony']},
    "IVIS_SPECTRUM": {'description': 'PerkinElmer IVIS Spectrum In Vivo Imaging System', 'annotations': {'manufacturer': 'PerkinElmer', 'type': 'in vivo bioluminescence'}, 'aliases': ['IVIS Spectrum In Vivo Imaging System']},
    "NANOSTRING_COSMX": {'description': 'NanoString CosMx Spatial Molecular Imager', 'annotations': {'manufacturer': 'NanoString', 'type': 'spatial transcriptomics'}, 'aliases': ['Nanostring CosMx']},
    "NANOSTRING_GEOMX": {'description': 'NanoString GeoMx Digital Spatial Profiler', 'annotations': {'manufacturer': 'NanoString', 'type': 'spatial profiling'}, 'aliases': ['Nanostring GeoMx']},
    "VISIUM_10X": {'description': '10x Genomics Visium Spatial Gene Expression', 'annotations': {'manufacturer': '10x Genomics', 'type': 'spatial transcriptomics'}, 'aliases': ['10x Visium Spatial Gene Expression']},
    "VEVO_3100": {'description': 'Vevo 3100 Imaging System (ultrasound)', 'annotations': {'manufacturer': 'FUJIFILM VisualSonics', 'type': 'ultrasound'}, 'aliases': ['Vevo 3100 Imaging System']},
    "VENTANA_BENCHMARK_XT": {'description': 'Ventana Benchmark XT automated staining', 'annotations': {'manufacturer': 'Roche', 'type': 'automated IHC stainer'}, 'aliases': ['Ventana Benchmark XT']},
    "VECTRA_H1": {'description': 'Vectra H1 3D Imaging System (Perkin Elmer)', 'annotations': {'manufacturer': 'PerkinElmer', 'type': 'multispectral imaging'}, 'aliases': ['Vectra H1 3D Imaging System']},
    "XF24_EXTRACELLULAR_FLUX": {'description': 'Agilent XF24 Extracellular Flux Analyzer', 'annotations': {'manufacturer': 'Agilent/Seahorse', 'type': 'metabolic analyzer'}, 'aliases': ['XF24 Extracellular Flux Analyzer']},
    "LICOR_ODYSSEY_CLX": {'description': 'LI-COR Odyssey CLx Imaging System', 'annotations': {'manufacturer': 'LI-COR', 'type': 'western blot imager'}, 'aliases': ['LI-COR Odyssey CLx']},
    "BIORAD_CHEMIDOC_MP": {'description': 'BioRad ChemiDoc MP Imaging System', 'annotations': {'manufacturer': 'BioRad', 'type': 'gel/western imager'}, 'aliases': ['BioRad ChemiDoc MP Imaging System']},
}

__all__ = [
    "MRIPlatformEnum",
    "MicroscopyPlatformEnum",
    "ImagingSystemPlatformEnum",
]