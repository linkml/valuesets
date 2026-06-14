"""
Cloud Laboratory Protocol Value Sets

Controlled vocabularies for cloud-laboratory research protocols, modeled on the operational taxonomy exposed by remote/cloud labs such as Emerald Cloud Lab (ECL) and its Symbolic Lab Language (SLL). Two complementary layers are captured: (1) LabUnitOperationEnum -- the composable sample-manipulation primitives ("unit operations") that make up a sample-preparation protocol; and (2) CloudLabExperimentEnum -- the higher-level experiment/assay functions that a protocol invokes. The experiment layer is cross-referenced to the assay value sets under bio/assays/ (OBIAssayEnum, BAOBioassayEnum) and to analytical-chemistry vocabularies; OBI/CHMO/MMO terms are used for `meaning:` where an equivalent ontology class exists. These vocabularies use neutral ontology mappings rather than vendor-specific identifiers; ECL function names are used only as an input checklist for completeness.

Generated from: lab_automation/cloud_lab.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class RelativeTimeEnum(RichEnum):
    """
    Temporal relationships between events or time points
    """
    # Enum members
    BEFORE = "BEFORE"
    AFTER = "AFTER"
    AT_SAME_TIME_AS = "AT_SAME_TIME_AS"

# Set metadata after class creation
RelativeTimeEnum._metadata = {
    "BEFORE": {'description': 'Occurs before the reference time point'},
    "AFTER": {'description': 'Occurs after the reference time point'},
    "AT_SAME_TIME_AS": {'description': 'Occurs at the same time as the reference time point'},
}

class PresenceEnum(RichEnum):
    """
    Classification of whether an entity is present, absent, or at detection limits
    """
    # Enum members
    PRESENT = "PRESENT"
    ABSENT = "ABSENT"
    BELOW_DETECTION_LIMIT = "BELOW_DETECTION_LIMIT"
    ABOVE_DETECTION_LIMIT = "ABOVE_DETECTION_LIMIT"

# Set metadata after class creation
PresenceEnum._metadata = {
    "PRESENT": {'description': 'The entity is present'},
    "ABSENT": {'description': 'The entity is absent'},
    "BELOW_DETECTION_LIMIT": {'description': 'The entity is below the detection limit'},
    "ABOVE_DETECTION_LIMIT": {'description': 'The entity is above the detection limit'},
}

class LabUnitOperationEnum(RichEnum):
    """
    Composable sample-manipulation primitives ("unit operations") used to build sample-preparation protocols in a cloud laboratory. Modeled on the ECL Symbolic Lab Language sample-preparation unit operations (Transfer, Aliquot, Mix, Incubate, Filter, Centrifuge, Pellet, Resuspend, etc.). Complements the lower level LiquidHandlingOperationEnum and SampleProcessingOperationEnum in lab_automation/operations.
    """
    # Enum members
    DEFINE = "DEFINE"
    LABEL_SAMPLE = "LABEL_SAMPLE"
    LABEL_CONTAINER = "LABEL_CONTAINER"
    TRANSFER = "TRANSFER"
    ALIQUOT = "ALIQUOT"
    CONSOLIDATE = "CONSOLIDATE"
    DILUTE = "DILUTE"
    SERIAL_DILUTE = "SERIAL_DILUTE"
    FILL_TO_VOLUME = "FILL_TO_VOLUME"
    RESUSPEND = "RESUSPEND"
    PREPARE_STOCK_SOLUTION = "PREPARE_STOCK_SOLUTION"
    ADJUST_PH = "ADJUST_PH"
    MIX = "MIX"
    INCUBATE = "INCUBATE"
    WAIT = "WAIT"
    CENTRIFUGE = "CENTRIFUGE"
    PELLET = "PELLET"
    FILTER = "FILTER"
    MAGNETIC_BEAD_SEPARATION = "MAGNETIC_BEAD_SEPARATION"
    MOVE_TO_MAGNET = "MOVE_TO_MAGNET"
    REMOVE_FROM_MAGNET = "REMOVE_FROM_MAGNET"
    COVER = "COVER"
    UNCOVER = "UNCOVER"
    DEGAS = "DEGAS"
    DESICCATE = "DESICCATE"
    EVAPORATE = "EVAPORATE"
    LYOPHILIZE = "LYOPHILIZE"
    FLASH_FREEZE = "FLASH_FREEZE"
    AUTOCLAVE = "AUTOCLAVE"
    GRIND = "GRIND"
    MICROWAVE_DIGESTION = "MICROWAVE_DIGESTION"

# Set metadata after class creation
LabUnitOperationEnum._metadata = {
    "DEFINE": {'description': 'Declare a new sample, container, or model and assign it a label for later reference in the protocol'},
    "LABEL_SAMPLE": {'description': 'Assign a human-readable label to a sample so it can be referenced by later unit operations'},
    "LABEL_CONTAINER": {'description': 'Assign a human-readable label to a container so it can be referenced by later unit operations'},
    "TRANSFER": {'description': 'Move a specified amount of sample from one source to one or more destinations'},
    "ALIQUOT": {'description': 'Distribute a sample into multiple equal portions in separate containers'},
    "CONSOLIDATE": {'description': 'Combine multiple source samples into a single destination container'},
    "DILUTE": {'description': 'Reduce the concentration of a sample by adding diluent to a target volume or concentration'},
    "SERIAL_DILUTE": {'description': 'Create a stepwise series of dilutions by repeatedly transferring and diluting a sample'},
    "FILL_TO_VOLUME": {'description': 'Add solvent to a sample until a specified total volume is reached'},
    "RESUSPEND": {'description': 'Dissolve or re-disperse a solid or pellet in a specified volume of solvent'},
    "PREPARE_STOCK_SOLUTION": {'description': 'Prepare a solution of defined composition from components and solvent'},
    "ADJUST_PH": {'description': 'Add titrant to bring a sample to a target pH'},
    "MIX": {'description': 'Homogenize a sample by pipetting, inversion, vortexing, stirring, sonication, or related agitation', 'meaning': 'CHMO:0001685', 'aliases': ['mixing']},
    "INCUBATE": {'description': 'Hold a sample at controlled temperature (and optionally mixing) for a specified duration'},
    "WAIT": {'description': 'Pause the protocol for a specified duration without other manipulation'},
    "CENTRIFUGE": {'description': 'Apply centrifugal force to a sample to separate components by density', 'meaning': 'OBI:0302886', 'aliases': ['centrifugation']},
    "PELLET": {'description': 'Centrifuge to precipitate solids, optionally aspirate the supernatant, and optionally resuspend the pellet'},
    "FILTER": {'description': 'Pass a sample through a filter to separate particulates or to sterilize', 'meaning': 'CHMO:0001640', 'aliases': ['filtration']},
    "MAGNETIC_BEAD_SEPARATION": {'description': 'Isolate target analytes bound to magnetic beads using a magnetic field'},
    "MOVE_TO_MAGNET": {'description': 'Place a container on a magnetic rack to immobilize magnetic beads'},
    "REMOVE_FROM_MAGNET": {'description': 'Remove a container from a magnetic rack to release magnetic beads'},
    "COVER": {'description': 'Apply a lid, cap, or seal to a container'},
    "UNCOVER": {'description': 'Remove a lid, cap, or seal from a container'},
    "DEGAS": {'description': 'Remove dissolved gases from a liquid sample', 'meaning': 'CHMO:0002772', 'aliases': ['degassing']},
    "DESICCATE": {'description': 'Remove moisture from a sample using a desiccant or controlled-humidity chamber'},
    "EVAPORATE": {'description': 'Remove solvent from a sample by evaporation, optionally under reduced pressure', 'meaning': 'CHMO:0001574', 'aliases': ['evaporation']},
    "LYOPHILIZE": {'description': 'Freeze-dry a sample to remove solvent by sublimation under vacuum', 'meaning': 'CHMO:0001553', 'aliases': ['freeze drying']},
    "FLASH_FREEZE": {'description': 'Rapidly freeze a sample, typically in liquid nitrogen'},
    "AUTOCLAVE": {'description': 'Sterilize a sample or labware using pressurized saturated steam'},
    "GRIND": {'description': 'Mechanically reduce a solid sample to smaller particles or powder', 'meaning': 'CHMO:0001652', 'aliases': ['grinding']},
    "MICROWAVE_DIGESTION": {'description': 'Digest a sample in acid under microwave heating to bring analytes into solution'},
}

class CloudLabExperimentEnum(RichEnum):
    """
    Higher-level experiment and assay functions offered as protocols by a cloud laboratory, modeled on the ECL Symbolic Lab Language experiment functions and grouped by category (synthesis, separations/chromatography, spectroscopy, mass spectrometry, bioassays, crystallography, property measurement, cellular). Cross-referenced to the assay value sets in bio/assays/ (OBIAssayEnum, BAOBioassayEnum) and to analytical_chemistry vocabularies; `meaning:` maps to OBI/CHMO classes where an equivalent assay or analytical method exists.
    """
    # Enum members
    DNA_SYNTHESIS = "DNA_SYNTHESIS"
    RNA_SYNTHESIS = "RNA_SYNTHESIS"
    PNA_SYNTHESIS = "PNA_SYNTHESIS"
    PEPTIDE_SYNTHESIS = "PEPTIDE_SYNTHESIS"
    PCR = "PCR"
    BIOCONJUGATION = "BIOCONJUGATION"
    HPLC = "HPLC"
    FPLC = "FPLC"
    FLASH_CHROMATOGRAPHY = "FLASH_CHROMATOGRAPHY"
    GAS_CHROMATOGRAPHY = "GAS_CHROMATOGRAPHY"
    ION_CHROMATOGRAPHY = "ION_CHROMATOGRAPHY"
    SUPERCRITICAL_FLUID_CHROMATOGRAPHY = "SUPERCRITICAL_FLUID_CHROMATOGRAPHY"
    SOLID_PHASE_EXTRACTION = "SOLID_PHASE_EXTRACTION"
    LIQUID_LIQUID_EXTRACTION = "LIQUID_LIQUID_EXTRACTION"
    CROSS_FLOW_FILTRATION = "CROSS_FLOW_FILTRATION"
    DIALYSIS = "DIALYSIS"
    AGAROSE_GEL_ELECTROPHORESIS = "AGAROSE_GEL_ELECTROPHORESIS"
    PAGE = "PAGE"
    CAPILLARY_GEL_ELECTROPHORESIS_SDS = "CAPILLARY_GEL_ELECTROPHORESIS_SDS"
    CAPILLARY_ISOELECTRIC_FOCUSING = "CAPILLARY_ISOELECTRIC_FOCUSING"
    WESTERN_BLOT = "WESTERN_BLOT"
    NMR = "NMR"
    NMR_2D = "NMR_2D"
    ABSORBANCE_SPECTROSCOPY = "ABSORBANCE_SPECTROSCOPY"
    ABSORBANCE_INTENSITY = "ABSORBANCE_INTENSITY"
    ABSORBANCE_KINETICS = "ABSORBANCE_KINETICS"
    FLUORESCENCE_SPECTROSCOPY = "FLUORESCENCE_SPECTROSCOPY"
    FLUORESCENCE_INTENSITY = "FLUORESCENCE_INTENSITY"
    FLUORESCENCE_KINETICS = "FLUORESCENCE_KINETICS"
    FLUORESCENCE_POLARIZATION = "FLUORESCENCE_POLARIZATION"
    LUMINESCENCE_SPECTROSCOPY = "LUMINESCENCE_SPECTROSCOPY"
    LUMINESCENCE_INTENSITY = "LUMINESCENCE_INTENSITY"
    LUMINESCENCE_KINETICS = "LUMINESCENCE_KINETICS"
    IR_SPECTROSCOPY = "IR_SPECTROSCOPY"
    RAMAN_SPECTROSCOPY = "RAMAN_SPECTROSCOPY"
    CIRCULAR_DICHROISM = "CIRCULAR_DICHROISM"
    DYNAMIC_LIGHT_SCATTERING = "DYNAMIC_LIGHT_SCATTERING"
    NEPHELOMETRY = "NEPHELOMETRY"
    THERMAL_SHIFT = "THERMAL_SHIFT"
    UV_MELTING = "UV_MELTING"
    MASS_SPECTROMETRY = "MASS_SPECTROMETRY"
    LCMS = "LCMS"
    GCMS = "GCMS"
    ICPMS = "ICPMS"
    ELISA = "ELISA"
    CAPILLARY_ELISA = "CAPILLARY_ELISA"
    ALPHASCREEN = "ALPHASCREEN"
    BIOLAYER_INTERFEROMETRY = "BIOLAYER_INTERFEROMETRY"
    QPCR = "QPCR"
    DNA_SEQUENCING = "DNA_SEQUENCING"
    TOTAL_PROTEIN_QUANTIFICATION = "TOTAL_PROTEIN_QUANTIFICATION"
    TOTAL_PROTEIN_DETECTION = "TOTAL_PROTEIN_DETECTION"
    DIFFERENTIAL_SCANNING_CALORIMETRY = "DIFFERENTIAL_SCANNING_CALORIMETRY"
    GROW_CRYSTAL = "GROW_CRYSTAL"
    POWDER_XRD = "POWDER_XRD"
    MEASURE_PH = "MEASURE_PH"
    MEASURE_CONDUCTIVITY = "MEASURE_CONDUCTIVITY"
    MEASURE_DENSITY = "MEASURE_DENSITY"
    MEASURE_VISCOSITY = "MEASURE_VISCOSITY"
    MEASURE_OSMOLALITY = "MEASURE_OSMOLALITY"
    MEASURE_REFRACTIVE_INDEX = "MEASURE_REFRACTIVE_INDEX"
    MEASURE_SURFACE_TENSION = "MEASURE_SURFACE_TENSION"
    MEASURE_CONTACT_ANGLE = "MEASURE_CONTACT_ANGLE"
    MEASURE_DISSOLVED_OXYGEN = "MEASURE_DISSOLVED_OXYGEN"
    MEASURE_MELTING_POINT = "MEASURE_MELTING_POINT"
    MEASURE_WEIGHT = "MEASURE_WEIGHT"
    MEASURE_VOLUME = "MEASURE_VOLUME"
    MEASURE_COUNT = "MEASURE_COUNT"
    COUNT_LIQUID_PARTICLES = "COUNT_LIQUID_PARTICLES"
    COULTER_COUNT = "COULTER_COUNT"
    CYCLIC_VOLTAMMETRY = "CYCLIC_VOLTAMMETRY"
    KARL_FISCHER_TITRATION = "KARL_FISCHER_TITRATION"
    DISSOLUTION = "DISSOLUTION"
    DYNAMIC_FOAM_ANALYSIS = "DYNAMIC_FOAM_ANALYSIS"
    VISUAL_INSPECTION = "VISUAL_INSPECTION"
    IMAGE_SAMPLE = "IMAGE_SAMPLE"
    IMAGE_CELLS = "IMAGE_CELLS"
    IMAGE_COLONIES = "IMAGE_COLONIES"
    QUANTIFY_COLONIES = "QUANTIFY_COLONIES"
    LYSE_CELLS = "LYSE_CELLS"
    FREEZE_CELLS = "FREEZE_CELLS"

# Set metadata after class creation
CloudLabExperimentEnum._metadata = {
    "DNA_SYNTHESIS": {'description': 'Solid-phase chemical synthesis of DNA oligonucleotides'},
    "RNA_SYNTHESIS": {'description': 'Solid-phase chemical synthesis of RNA oligonucleotides'},
    "PNA_SYNTHESIS": {'description': 'Solid-phase chemical synthesis of peptide nucleic acid oligomers'},
    "PEPTIDE_SYNTHESIS": {'description': 'Solid-phase chemical synthesis of peptides'},
    "PCR": {'description': 'Polymerase chain reaction amplification of nucleic acids', 'meaning': 'OBI:0000415', 'aliases': ['polymerase chain reaction']},
    "BIOCONJUGATION": {'description': 'Covalent coupling of biomolecules or labels to a target molecule'},
    "HPLC": {'description': 'High-performance liquid chromatography separation', 'meaning': 'CHMO:0001009', 'aliases': ['high-performance liquid chromatography']},
    "FPLC": {'description': 'Fast protein liquid chromatography separation'},
    "FLASH_CHROMATOGRAPHY": {'description': 'Medium-pressure flash column chromatography separation', 'meaning': 'CHMO:0002582'},
    "GAS_CHROMATOGRAPHY": {'description': 'Gas chromatography separation of volatile analytes', 'meaning': 'CHMO:0001002'},
    "ION_CHROMATOGRAPHY": {'description': 'Chromatographic separation of ionic species', 'meaning': 'CHMO:0002874'},
    "SUPERCRITICAL_FLUID_CHROMATOGRAPHY": {'description': 'Chromatographic separation using a supercritical fluid mobile phase'},
    "SOLID_PHASE_EXTRACTION": {'description': 'Sample cleanup or enrichment by selective retention on a solid sorbent'},
    "LIQUID_LIQUID_EXTRACTION": {'description': 'Separation of analytes between two immiscible liquid phases', 'meaning': 'CHMO:0001600', 'aliases': ['liquid–liquid extraction']},
    "CROSS_FLOW_FILTRATION": {'description': 'Tangential-flow filtration for concentration or buffer exchange'},
    "DIALYSIS": {'description': 'Separation of molecules by size across a semipermeable membrane', 'meaning': 'CHMO:0001522'},
    "AGAROSE_GEL_ELECTROPHORESIS": {'description': 'Size-based separation of nucleic acids in an agarose gel', 'meaning': 'CHMO:0001022'},
    "PAGE": {'description': 'Polyacrylamide gel electrophoresis separation of biomolecules', 'meaning': 'CHMO:0001023', 'aliases': ['polyacrylamide gel electrophoresis']},
    "CAPILLARY_GEL_ELECTROPHORESIS_SDS": {'description': 'SDS capillary gel electrophoresis sizing of proteins'},
    "CAPILLARY_ISOELECTRIC_FOCUSING": {'description': 'Separation of proteins by isoelectric point in a capillary', 'meaning': 'CHMO:0001033'},
    "WESTERN_BLOT": {'description': 'Immunodetection of proteins separated by electrophoresis', 'meaning': 'OBI:0000854', 'aliases': ['western blot assay']},
    "NMR": {'description': 'One-dimensional nuclear magnetic resonance spectroscopy', 'meaning': 'CHMO:0000591', 'aliases': ['nuclear magnetic resonance spectroscopy']},
    "NMR_2D": {'description': 'Two-dimensional nuclear magnetic resonance spectroscopy', 'meaning': 'CHMO:0000598', 'aliases': ['two-dimensional nuclear magnetic resonance spectroscopy']},
    "ABSORBANCE_SPECTROSCOPY": {'description': 'Measurement of absorbance across a wavelength range'},
    "ABSORBANCE_INTENSITY": {'description': 'Measurement of absorbance at one or more discrete wavelengths'},
    "ABSORBANCE_KINETICS": {'description': 'Time-resolved measurement of absorbance'},
    "FLUORESCENCE_SPECTROSCOPY": {'description': 'Measurement of fluorescence emission across a wavelength range', 'meaning': 'CHMO:0000287'},
    "FLUORESCENCE_INTENSITY": {'description': 'Measurement of fluorescence intensity at discrete wavelengths'},
    "FLUORESCENCE_KINETICS": {'description': 'Time-resolved measurement of fluorescence intensity'},
    "FLUORESCENCE_POLARIZATION": {'description': 'Measurement of fluorescence polarization/anisotropy'},
    "LUMINESCENCE_SPECTROSCOPY": {'description': 'Measurement of luminescence emission across a wavelength range', 'meaning': 'CHMO:0002415'},
    "LUMINESCENCE_INTENSITY": {'description': 'Measurement of luminescence intensity at discrete wavelengths'},
    "LUMINESCENCE_KINETICS": {'description': 'Time-resolved measurement of luminescence intensity'},
    "IR_SPECTROSCOPY": {'description': 'Infrared absorption spectroscopy', 'meaning': 'CHMO:0000630', 'aliases': ['infrared absorption spectroscopy']},
    "RAMAN_SPECTROSCOPY": {'description': 'Raman scattering spectroscopy', 'meaning': 'CHMO:0000656'},
    "CIRCULAR_DICHROISM": {'description': 'Measurement of differential absorption of circularly polarized light'},
    "DYNAMIC_LIGHT_SCATTERING": {'description': 'Measurement of particle size distribution from scattered-light fluctuations', 'meaning': 'CHMO:0000167'},
    "NEPHELOMETRY": {'description': 'Measurement of turbidity by scattered light'},
    "THERMAL_SHIFT": {'description': 'Measurement of protein thermal stability via a fluorescent thermal shift assay'},
    "UV_MELTING": {'description': 'Measurement of nucleic acid or protein melting curves by UV absorbance'},
    "MASS_SPECTROMETRY": {'description': 'Determination of mass-to-charge ratios of ionized analytes', 'meaning': 'CHMO:0000470'},
    "LCMS": {'description': 'Liquid chromatography coupled to mass spectrometry', 'meaning': 'CHMO:0000524', 'aliases': ['liquid chromatography-mass spectrometry']},
    "GCMS": {'description': 'Gas chromatography coupled to mass spectrometry', 'meaning': 'CHMO:0000497', 'aliases': ['gas chromatography-mass spectrometry']},
    "ICPMS": {'description': 'Inductively coupled plasma mass spectrometry for elemental analysis', 'meaning': 'CHMO:0000538', 'aliases': ['inductively coupled plasma mass spectrometry']},
    "ELISA": {'description': 'Enzyme-linked immunosorbent assay', 'meaning': 'OBI:0000661', 'aliases': ['enzyme-linked immunosorbent assay']},
    "CAPILLARY_ELISA": {'description': 'Automated capillary-based enzyme-linked immunosorbent assay'},
    "ALPHASCREEN": {'description': 'Bead-based amplified luminescent proximity homogeneous assay'},
    "BIOLAYER_INTERFEROMETRY": {'description': 'Label-free measurement of biomolecular binding kinetics by interferometry', 'meaning': 'OBI:0002107', 'aliases': ['bio-layer interferometry assay']},
    "QPCR": {'description': 'Quantitative real-time polymerase chain reaction', 'meaning': 'OBI:0000893', 'aliases': ['real time polymerase chain reaction assay']},
    "DNA_SEQUENCING": {'description': 'Determination of nucleotide sequence of DNA (Sanger/capillary)', 'meaning': 'OBI:0000626', 'aliases': ['DNA sequencing assay']},
    "TOTAL_PROTEIN_QUANTIFICATION": {'description': 'Colorimetric or fluorometric quantification of total protein'},
    "TOTAL_PROTEIN_DETECTION": {'description': 'Capillary-based detection and sizing of total protein'},
    "DIFFERENTIAL_SCANNING_CALORIMETRY": {'description': 'Measurement of heat flow associated with thermal transitions', 'meaning': 'CHMO:0000684'},
    "GROW_CRYSTAL": {'description': 'Crystallization of a compound or macromolecule for structural analysis', 'meaning': 'CHMO:0001477', 'aliases': ['crystallisation']},
    "POWDER_XRD": {'description': 'Powder X-ray diffraction analysis of crystalline solids', 'meaning': 'CHMO:0000158', 'aliases': ['powder X-ray diffraction']},
    "MEASURE_PH": {'description': 'Measurement of sample pH'},
    "MEASURE_CONDUCTIVITY": {'description': 'Measurement of electrical conductivity of a solution'},
    "MEASURE_DENSITY": {'description': 'Measurement of sample density'},
    "MEASURE_VISCOSITY": {'description': 'Measurement of sample viscosity'},
    "MEASURE_OSMOLALITY": {'description': 'Measurement of solute concentration as osmolality'},
    "MEASURE_REFRACTIVE_INDEX": {'description': 'Measurement of the refractive index of a sample'},
    "MEASURE_SURFACE_TENSION": {'description': 'Measurement of liquid surface tension'},
    "MEASURE_CONTACT_ANGLE": {'description': 'Measurement of the contact angle of a liquid on a surface'},
    "MEASURE_DISSOLVED_OXYGEN": {'description': 'Measurement of dissolved oxygen concentration in a liquid'},
    "MEASURE_MELTING_POINT": {'description': 'Determination of the melting point of a solid'},
    "MEASURE_WEIGHT": {'description': 'Gravimetric measurement of sample mass'},
    "MEASURE_VOLUME": {'description': 'Measurement of sample volume'},
    "MEASURE_COUNT": {'description': 'Counting of discrete objects (e.g. particles, colonies, cells)'},
    "COUNT_LIQUID_PARTICLES": {'description': 'Counting and sizing of particles suspended in a liquid'},
    "COULTER_COUNT": {'description': 'Counting and sizing of particles or cells by electrical impedance'},
    "CYCLIC_VOLTAMMETRY": {'description': 'Electrochemical measurement of current versus swept potential', 'meaning': 'CHMO:0000025'},
    "KARL_FISCHER_TITRATION": {'description': 'Titrimetric determination of water content', 'meaning': 'CHMO:0002535', 'aliases': ['Karl–Fischer titration']},
    "DISSOLUTION": {'description': 'Measurement of the rate and extent of dissolution of a solid'},
    "DYNAMIC_FOAM_ANALYSIS": {'description': 'Measurement of foam formation and decay'},
    "VISUAL_INSPECTION": {'description': 'Operator or imaging-based visual assessment of a sample'},
    "IMAGE_SAMPLE": {'description': 'Acquisition of a photographic image of a sample'},
    "IMAGE_CELLS": {'description': 'Microscopic imaging of cells'},
    "IMAGE_COLONIES": {'description': 'Imaging of microbial colonies on solid media'},
    "QUANTIFY_COLONIES": {'description': 'Counting and quantification of microbial colonies'},
    "LYSE_CELLS": {'description': 'Disruption of cells to release intracellular contents'},
    "FREEZE_CELLS": {'description': 'Controlled-rate freezing of cells for storage'},
}

__all__ = [
    "RelativeTimeEnum",
    "PresenceEnum",
    "LabUnitOperationEnum",
    "CloudLabExperimentEnum",
]