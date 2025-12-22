"""
Biological Assay Value Sets

Value sets for biological assays including sequencing, imaging, mass spectrometry, cell-based, and clinical/behavioral assays. Derived from NF-OSI metadata dictionary with ontology mappings to OBI, CHMO, BAO, and other relevant ontologies.

Generated from: bio/assays.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class SequencingAssayEnum(RichEnum):
    """
    Sequencing-based assays including RNA-seq, DNA-seq, and related methods
    """
    # Enum members
    RNA_SEQ = "RNA_SEQ"
    SINGLE_CELL_RNA_SEQ = "SINGLE_CELL_RNA_SEQ"
    SINGLE_NUCLEUS_RNA_SEQ = "SINGLE_NUCLEUS_RNA_SEQ"
    SPATIAL_TRANSCRIPTOMICS = "SPATIAL_TRANSCRIPTOMICS"
    LNCRNA_SEQ = "LNCRNA_SEQ"
    MIRNA_SEQ = "MIRNA_SEQ"
    RIBO_SEQ = "RIBO_SEQ"
    WHOLE_GENOME_SEQUENCING = "WHOLE_GENOME_SEQUENCING"
    WHOLE_EXOME_SEQUENCING = "WHOLE_EXOME_SEQUENCING"
    TARGETED_EXOME_SEQUENCING = "TARGETED_EXOME_SEQUENCING"
    NEXT_GENERATION_TARGETED_SEQUENCING = "NEXT_GENERATION_TARGETED_SEQUENCING"
    SANGER_SEQUENCING = "SANGER_SEQUENCING"
    ATAC_SEQ = "ATAC_SEQ"
    SINGLE_CELL_ATAC_SEQ = "SINGLE_CELL_ATAC_SEQ"
    CHIP_SEQ = "CHIP_SEQ"
    CUT_AND_RUN = "CUT_AND_RUN"
    BISULFITE_SEQUENCING = "BISULFITE_SEQUENCING"
    ERR_BISULFITE_SEQUENCING = "ERR_BISULFITE_SEQUENCING"
    OXBS_SEQ = "OXBS_SEQ"
    HI_C = "HI_C"
    ISO_SEQ = "ISO_SEQ"
    NOME_SEQ = "NOME_SEQ"
    CAPP_SEQ = "CAPP_SEQ"
    SAFER_SEQS = "SAFER_SEQS"
    TCR_REPERTOIRE_SEQUENCING = "TCR_REPERTOIRE_SEQUENCING"
    SCCGI_SEQ = "SCCGI_SEQ"
    JUMPING_LIBRARY = "JUMPING_LIBRARY"
    SNP_ARRAY = "SNP_ARRAY"
    RNA_ARRAY = "RNA_ARRAY"
    MIRNA_ARRAY = "MIRNA_ARRAY"
    METHYLATION_ARRAY = "METHYLATION_ARRAY"

# Set metadata after class creation
SequencingAssayEnum._metadata = {
    "RNA_SEQ": {'description': 'RNA sequencing to profile transcriptome', 'meaning': 'OBI:0001271', 'aliases': ['RNA-seq']},
    "SINGLE_CELL_RNA_SEQ": {'description': 'Single-cell RNA sequencing', 'meaning': 'OBI:0002631', 'aliases': ['scRNA-seq']},
    "SINGLE_NUCLEUS_RNA_SEQ": {'description': 'Single-nucleus RNA sequencing', 'aliases': ['snRNA-seq']},
    "SPATIAL_TRANSCRIPTOMICS": {'description': 'Spatially resolved transcriptomics', 'meaning': 'EFO:0008992'},
    "LNCRNA_SEQ": {'description': 'Long non-coding RNA sequencing', 'aliases': ['lncRNA-seq']},
    "MIRNA_SEQ": {'description': 'MicroRNA sequencing', 'meaning': 'OBI:0002112', 'aliases': ['miRNA-seq']},
    "RIBO_SEQ": {'description': 'Ribosome profiling sequencing', 'aliases': ['Ribo-seq']},
    "WHOLE_GENOME_SEQUENCING": {'description': 'Whole genome sequencing', 'meaning': 'OBI:0002117', 'aliases': ['WGS']},
    "WHOLE_EXOME_SEQUENCING": {'description': 'Whole exome sequencing', 'meaning': 'OBI:0002118', 'aliases': ['WES']},
    "TARGETED_EXOME_SEQUENCING": {'description': 'Targeted exome sequencing panel'},
    "NEXT_GENERATION_TARGETED_SEQUENCING": {'description': 'Next generation targeted sequencing panel'},
    "SANGER_SEQUENCING": {'description': 'Sanger chain termination sequencing', 'meaning': 'OBI:0000695'},
    "ATAC_SEQ": {'description': 'Assay for Transposase-Accessible Chromatin sequencing', 'meaning': 'OBI:0002039', 'aliases': ['ATAC-seq']},
    "SINGLE_CELL_ATAC_SEQ": {'description': 'Single-cell ATAC-seq', 'aliases': ['scATAC-seq']},
    "CHIP_SEQ": {'description': 'Chromatin immunoprecipitation sequencing', 'meaning': 'OBI:0000716', 'aliases': ['ChIP-seq']},
    "CUT_AND_RUN": {'description': 'Cleavage Under Targets and Release Using Nuclease', 'aliases': ['CUT&RUN']},
    "BISULFITE_SEQUENCING": {'description': 'Bisulfite sequencing for DNA methylation', 'meaning': 'OBI:0000748', 'aliases': ['BS-seq']},
    "ERR_BISULFITE_SEQUENCING": {'description': 'Enzymatic methyl-seq (EM-seq) or similar error-reduced bisulfite sequencing'},
    "OXBS_SEQ": {'description': 'Oxidative bisulfite sequencing', 'aliases': ['oxBS-seq']},
    "HI_C": {'description': 'High-throughput chromosome conformation capture', 'meaning': 'OBI:0002042', 'aliases': ['Hi-C']},
    "ISO_SEQ": {'description': 'Isoform sequencing (PacBio long-read)', 'aliases': ['Iso-Seq']},
    "NOME_SEQ": {'description': 'Nucleosome Occupancy and Methylome Sequencing', 'aliases': ['NOMe-seq']},
    "CAPP_SEQ": {'description': 'CAncer Personalized Profiling by deep Sequencing', 'aliases': ['CAPP-Seq']},
    "SAFER_SEQS": {'description': 'Safe-Sequencing System'},
    "TCR_REPERTOIRE_SEQUENCING": {'description': 'T cell receptor repertoire sequencing', 'aliases': ['TCR-seq']},
    "SCCGI_SEQ": {'description': 'Single-cell CGI sequencing', 'aliases': ['scCGI-seq']},
    "JUMPING_LIBRARY": {'description': 'Jumping library sequencing for structural variants'},
    "SNP_ARRAY": {'description': 'SNP genotyping array', 'meaning': 'OBI:0001204'},
    "RNA_ARRAY": {'description': 'RNA expression array', 'meaning': 'OBI:0001463'},
    "MIRNA_ARRAY": {'description': 'MicroRNA array'},
    "METHYLATION_ARRAY": {'description': 'DNA methylation array', 'meaning': 'OBI:0001332'},
}

class ImagingAssayEnum(RichEnum):
    """
    Imaging-based assays including microscopy, MRI, and related methods
    """
    # Enum members
    BRIGHTFIELD_MICROSCOPY = "BRIGHTFIELD_MICROSCOPY"
    CONFOCAL_MICROSCOPY = "CONFOCAL_MICROSCOPY"
    THREE_D_CONFOCAL_IMAGING = "THREE_D_CONFOCAL_IMAGING"
    FLUORESCENCE_MICROSCOPY = "FLUORESCENCE_MICROSCOPY"
    PHASE_CONTRAST_MICROSCOPY = "PHASE_CONTRAST_MICROSCOPY"
    ATOMIC_FORCE_MICROSCOPY = "ATOMIC_FORCE_MICROSCOPY"
    THREE_D_ELECTRON_MICROSCOPY = "THREE_D_ELECTRON_MICROSCOPY"
    IMMUNOFLUORESCENCE = "IMMUNOFLUORESCENCE"
    IMMUNOHISTOCHEMISTRY = "IMMUNOHISTOCHEMISTRY"
    IMMUNOCYTOCHEMISTRY = "IMMUNOCYTOCHEMISTRY"
    HISTOLOGY = "HISTOLOGY"
    FISH = "FISH"
    CODEX = "CODEX"
    LIVE_IMAGING = "LIVE_IMAGING"
    AUTORADIOGRAPHY = "AUTORADIOGRAPHY"
    CONVENTIONAL_MRI = "CONVENTIONAL_MRI"
    FUNCTIONAL_MRI = "FUNCTIONAL_MRI"
    DIFFUSION_MRI = "DIFFUSION_MRI"
    MPRAGE_MRI = "MPRAGE_MRI"
    MAGNETIC_RESONANCE_SPECTROSCOPY = "MAGNETIC_RESONANCE_SPECTROSCOPY"
    MAGNETIC_RESONANCE_ANGIOGRAPHY = "MAGNETIC_RESONANCE_ANGIOGRAPHY"
    POSITRON_EMISSION_TOMOGRAPHY = "POSITRON_EMISSION_TOMOGRAPHY"
    OPTICAL_COHERENCE_TOMOGRAPHY = "OPTICAL_COHERENCE_TOMOGRAPHY"
    OPTICAL_TOMOGRAPHY = "OPTICAL_TOMOGRAPHY"
    HIGH_FREQUENCY_ULTRASOUND = "HIGH_FREQUENCY_ULTRASOUND"
    TRANSCRANIAL_DOPPLER = "TRANSCRANIAL_DOPPLER"
    IN_VIVO_BIOLUMINESCENCE = "IN_VIVO_BIOLUMINESCENCE"
    LASER_SPECKLE_IMAGING = "LASER_SPECKLE_IMAGING"
    SPATIAL_FREQUENCY_DOMAIN_IMAGING = "SPATIAL_FREQUENCY_DOMAIN_IMAGING"
    TRACTION_FORCE_MICROSCOPY = "TRACTION_FORCE_MICROSCOPY"
    PHOTOGRAPH = "PHOTOGRAPH"

# Set metadata after class creation
ImagingAssayEnum._metadata = {
    "BRIGHTFIELD_MICROSCOPY": {'description': 'Brightfield microscopy imaging', 'meaning': 'CHMO:0000104'},
    "CONFOCAL_MICROSCOPY": {'description': 'Confocal laser scanning microscopy', 'meaning': 'CHMO:0000545'},
    "THREE_D_CONFOCAL_IMAGING": {'description': 'Three-dimensional confocal imaging', 'aliases': ['3D confocal imaging']},
    "FLUORESCENCE_MICROSCOPY": {'description': 'Fluorescence microscopy assay', 'meaning': 'CHMO:0000087'},
    "PHASE_CONTRAST_MICROSCOPY": {'description': 'Phase-contrast microscopy', 'meaning': 'CHMO:0000056'},
    "ATOMIC_FORCE_MICROSCOPY": {'description': 'Atomic force microscopy', 'meaning': 'CHMO:0000113', 'aliases': ['AFM']},
    "THREE_D_ELECTRON_MICROSCOPY": {'description': 'Three-dimensional electron microscopy', 'aliases': ['3D EM']},
    "IMMUNOFLUORESCENCE": {'description': 'Immunofluorescence staining and imaging', 'meaning': 'OBI:0003357'},
    "IMMUNOHISTOCHEMISTRY": {'description': 'Immunohistochemistry staining', 'meaning': 'OBI:0001986', 'aliases': ['IHC']},
    "IMMUNOCYTOCHEMISTRY": {'description': 'Immunocytochemistry staining', 'aliases': ['ICC']},
    "HISTOLOGY": {'description': 'Histological examination', 'meaning': 'OBI:0600020'},
    "FISH": {'description': 'Fluorescence In Situ Hybridization', 'meaning': 'OBI:0003094', 'aliases': ['Fluorescence In Situ Hybridization']},
    "CODEX": {'description': 'CO-Detection by indEXing imaging'},
    "LIVE_IMAGING": {'description': 'Live cell or tissue imaging'},
    "AUTORADIOGRAPHY": {'description': 'Autoradiography imaging', 'meaning': 'CHMO:0000812'},
    "CONVENTIONAL_MRI": {'description': 'Conventional magnetic resonance imaging', 'meaning': 'OBI:0002985'},
    "FUNCTIONAL_MRI": {'description': 'Functional magnetic resonance imaging', 'meaning': 'OBI:0001501', 'aliases': ['fMRI']},
    "DIFFUSION_MRI": {'description': 'Diffusion-weighted MRI', 'aliases': ['DWI']},
    "MPRAGE_MRI": {'description': 'Magnetization-Prepared Rapid Gradient Echo MRI', 'aliases': ['MPRAGE']},
    "MAGNETIC_RESONANCE_SPECTROSCOPY": {'description': 'Magnetic resonance spectroscopy', 'meaning': 'CHMO:0000566', 'aliases': ['MRS']},
    "MAGNETIC_RESONANCE_ANGIOGRAPHY": {'description': 'Magnetic resonance angiography', 'meaning': 'OBI:0002986', 'aliases': ['MRA']},
    "POSITRON_EMISSION_TOMOGRAPHY": {'description': 'Positron emission tomography', 'meaning': 'OBI:0001912', 'aliases': ['PET']},
    "OPTICAL_COHERENCE_TOMOGRAPHY": {'description': 'Optical coherence tomography', 'meaning': 'CHMO:0000896', 'aliases': ['OCT']},
    "OPTICAL_TOMOGRAPHY": {'description': 'Optical tomography'},
    "HIGH_FREQUENCY_ULTRASOUND": {'description': 'High frequency ultrasound imaging'},
    "TRANSCRANIAL_DOPPLER": {'description': 'Transcranial doppler ultrasonography'},
    "IN_VIVO_BIOLUMINESCENCE": {'description': 'In vivo bioluminescence imaging', 'meaning': 'OBI:0001503'},
    "LASER_SPECKLE_IMAGING": {'description': 'Laser speckle contrast imaging'},
    "SPATIAL_FREQUENCY_DOMAIN_IMAGING": {'description': 'Spatial frequency domain imaging'},
    "TRACTION_FORCE_MICROSCOPY": {'description': 'Traction force microscopy'},
    "PHOTOGRAPH": {'description': 'Photographic documentation'},
}

class MassSpectrometryAssayEnum(RichEnum):
    """
    Mass spectrometry-based assays for proteomics and metabolomics
    """
    # Enum members
    MASS_SPECTROMETRY = "MASS_SPECTROMETRY"
    LC_MS = "LC_MS"
    LC_MS_MS = "LC_MS_MS"
    HPLC_MS_MS = "HPLC_MS_MS"
    UHPLC_MS_MS = "UHPLC_MS_MS"
    FIA_MSMS = "FIA_MSMS"
    LABEL_FREE_MS = "LABEL_FREE_MS"
    TMT_QUANTITATION = "TMT_QUANTITATION"
    MUDPIT = "MUDPIT"
    MIB_MS = "MIB_MS"
    LC_ECD = "LC_ECD"
    FTIR_SPECTROSCOPY = "FTIR_SPECTROSCOPY"
    RPPA = "RPPA"
    PROXIMITY_EXTENSION_ASSAY = "PROXIMITY_EXTENSION_ASSAY"

# Set metadata after class creation
MassSpectrometryAssayEnum._metadata = {
    "MASS_SPECTROMETRY": {'description': 'General mass spectrometry', 'meaning': 'CHMO:0000470', 'aliases': ['MS']},
    "LC_MS": {'description': 'Liquid chromatography-mass spectrometry', 'meaning': 'CHMO:0000524', 'aliases': ['liquid chromatography/mass spectrometry']},
    "LC_MS_MS": {'description': 'Liquid chromatography-tandem mass spectrometry', 'meaning': 'CHMO:0000701', 'aliases': ['LC-MS/MS', 'liquid chromatography/tandem mass spectrometry']},
    "HPLC_MS_MS": {'description': 'High-performance liquid chromatography/tandem mass spectrometry', 'aliases': ['high-performance liquid chromatography/tandem mass spectrometry']},
    "UHPLC_MS_MS": {'description': 'Ultra high-performance liquid chromatography/tandem mass spectrometry', 'aliases': ['ultra high-performance liquid chromatography/tandem mass spectrometry']},
    "FIA_MSMS": {'description': 'Flow injection analysis tandem mass spectrometry', 'aliases': ['FIA-MSMS']},
    "LABEL_FREE_MS": {'description': 'Label-free mass spectrometry quantification', 'aliases': ['label free mass spectrometry']},
    "TMT_QUANTITATION": {'description': 'Tandem mass tag quantitation', 'aliases': ['TMT quantitation']},
    "MUDPIT": {'description': 'Multidimensional Protein Identification Technology', 'aliases': ['MudPIT']},
    "MIB_MS": {'description': 'Multiplexed Inhibitor Beads mass spectrometry', 'aliases': ['MIB/MS']},
    "LC_ECD": {'description': 'Liquid chromatography-electrochemical detection', 'aliases': ['liquid chromatography-electrochemical detection']},
    "FTIR_SPECTROSCOPY": {'description': 'Fourier-transform infrared spectroscopy', 'meaning': 'CHMO:0000817', 'aliases': ['FTIR spectroscopy']},
    "RPPA": {'description': 'Reverse Phase Protein Array', 'meaning': 'OBI:0001975', 'aliases': ['RPPA']},
    "PROXIMITY_EXTENSION_ASSAY": {'description': 'Proximity extension assay', 'aliases': ['PEA']},
}

class CellBasedAssayEnum(RichEnum):
    """
    Cell-based assays including viability, proliferation, and functional assays
    """
    # Enum members
    CELL_VIABILITY_ASSAY = "CELL_VIABILITY_ASSAY"
    CELL_PROLIFERATION_ASSAY = "CELL_PROLIFERATION_ASSAY"
    CELL_COUNT = "CELL_COUNT"
    ALAMAR_BLUE_ABSORBANCE = "ALAMAR_BLUE_ABSORBANCE"
    ALAMAR_BLUE_FLUORESCENCE = "ALAMAR_BLUE_FLUORESCENCE"
    THREE_D_MICROTISSUE_VIABILITY = "THREE_D_MICROTISSUE_VIABILITY"
    BRDU_PROLIFERATION = "BRDU_PROLIFERATION"
    EDU_PROLIFERATION = "EDU_PROLIFERATION"
    ATPASE_ACTIVITY_ASSAY = "ATPASE_ACTIVITY_ASSAY"
    CAMP_GLO_ASSAY = "CAMP_GLO_ASSAY"
    FLOW_CYTOMETRY = "FLOW_CYTOMETRY"
    ELISA = "ELISA"
    SANDWICH_ELISA = "SANDWICH_ELISA"
    WESTERN_BLOT = "WESTERN_BLOT"
    IMMUNOASSAY = "IMMUNOASSAY"
    PCR = "PCR"
    QPCR = "QPCR"
    NANOSTRING_NCOUNTER = "NANOSTRING_NCOUNTER"
    MULTI_ELECTRODE_ARRAY = "MULTI_ELECTRODE_ARRAY"
    CURRENT_CLAMP_ASSAY = "CURRENT_CLAMP_ASSAY"
    WHOLE_CELL_PATCH_CLAMP = "WHOLE_CELL_PATCH_CLAMP"
    LOCAL_FIELD_POTENTIAL = "LOCAL_FIELD_POTENTIAL"
    LONG_TERM_POTENTIATION = "LONG_TERM_POTENTIATION"
    MIGRATION_ASSAY = "MIGRATION_ASSAY"
    IN_VITRO_TUMORIGENESIS = "IN_VITRO_TUMORIGENESIS"
    IN_VIVO_TUMOR_GROWTH = "IN_VIVO_TUMOR_GROWTH"
    IN_VIVO_PDX_VIABILITY = "IN_VIVO_PDX_VIABILITY"
    MATRIGEL_TUMORIGENESIS = "MATRIGEL_TUMORIGENESIS"
    HIGH_CONTENT_SCREEN = "HIGH_CONTENT_SCREEN"
    CELL_PAINTING = "CELL_PAINTING"
    COMPOUND_SCREEN = "COMPOUND_SCREEN"
    COMBINATION_SCREEN = "COMBINATION_SCREEN"
    SMALL_MOLECULE_LIBRARY_SCREEN = "SMALL_MOLECULE_LIBRARY_SCREEN"
    REPORTER_GENE_ASSAY = "REPORTER_GENE_ASSAY"
    MASSIVELY_PARALLEL_REPORTER_ASSAY = "MASSIVELY_PARALLEL_REPORTER_ASSAY"
    SPLIT_GFP_ASSAY = "SPLIT_GFP_ASSAY"
    FOCUS_FORMING_ASSAY = "FOCUS_FORMING_ASSAY"
    OXYGEN_CONSUMPTION_ASSAY = "OXYGEN_CONSUMPTION_ASSAY"
    ROS_ASSAY = "ROS_ASSAY"
    CALCIUM_RETENTION_ASSAY = "CALCIUM_RETENTION_ASSAY"
    TRANS_ENDOTHELIAL_RESISTANCE = "TRANS_ENDOTHELIAL_RESISTANCE"
    CELL_PERMEABILITY_ASSAY = "CELL_PERMEABILITY_ASSAY"
    PHARMACOKINETIC_ADME = "PHARMACOKINETIC_ADME"
    ARRAY = "ARRAY"
    HPLC = "HPLC"
    ELECTROCHEMILUMINESCENCE = "ELECTROCHEMILUMINESCENCE"
    STR_PROFILE = "STR_PROFILE"
    TIDE = "TIDE"
    SURVIVAL_ASSAY = "SURVIVAL_ASSAY"

# Set metadata after class creation
CellBasedAssayEnum._metadata = {
    "CELL_VIABILITY_ASSAY": {'description': 'Cell viability measurement assay', 'meaning': 'BAO:0003009'},
    "CELL_PROLIFERATION_ASSAY": {'description': 'Cell proliferation measurement', 'meaning': 'BAO:0002100'},
    "CELL_COUNT": {'description': 'Cell counting assay', 'meaning': 'BAO:0002097'},
    "ALAMAR_BLUE_ABSORBANCE": {'description': 'AlamarBlue absorbance assay (2D)', 'aliases': ['2D AlamarBlue absorbance']},
    "ALAMAR_BLUE_FLUORESCENCE": {'description': 'AlamarBlue fluorescence assay (2D)', 'aliases': ['2D AlamarBlue fluorescence']},
    "THREE_D_MICROTISSUE_VIABILITY": {'description': '3D microtissue viability assay', 'aliases': ['3D microtissue viability']},
    "BRDU_PROLIFERATION": {'description': 'BrdU incorporation proliferation assay', 'meaning': 'OBI:0001330', 'aliases': ['BrdU proliferation assay']},
    "EDU_PROLIFERATION": {'description': 'EdU incorporation proliferation assay', 'aliases': ['EdU proliferation assay']},
    "ATPASE_ACTIVITY_ASSAY": {'description': 'ATPase activity measurement'},
    "CAMP_GLO_ASSAY": {'description': 'cAMP-Glo Max Assay', 'aliases': ['cAMP-Glo Max Assay']},
    "FLOW_CYTOMETRY": {'description': 'Flow cytometry analysis', 'meaning': 'OBI:0000916'},
    "ELISA": {'description': 'Enzyme-linked immunosorbent assay', 'meaning': 'OBI:0000661'},
    "SANDWICH_ELISA": {'description': 'Sandwich ELISA'},
    "WESTERN_BLOT": {'description': 'Western blot analysis', 'meaning': 'OBI:0000714'},
    "IMMUNOASSAY": {'description': 'General immunoassay', 'meaning': 'OBI:0000717'},
    "PCR": {'description': 'Polymerase chain reaction', 'meaning': 'OBI:0000415', 'aliases': ['polymerase chain reaction']},
    "QPCR": {'description': 'Quantitative PCR', 'meaning': 'OBI:0000893', 'aliases': ['quantitative PCR']},
    "NANOSTRING_NCOUNTER": {'description': 'NanoString nCounter Analysis System'},
    "MULTI_ELECTRODE_ARRAY": {'description': 'Multi-electrode array recording', 'meaning': 'OBI:0002187'},
    "CURRENT_CLAMP_ASSAY": {'description': 'Current clamp electrophysiology'},
    "WHOLE_CELL_PATCH_CLAMP": {'description': 'Whole-cell patch clamp recording', 'meaning': 'OBI:0002179'},
    "LOCAL_FIELD_POTENTIAL": {'description': 'Local field potential recording'},
    "LONG_TERM_POTENTIATION": {'description': 'Long-term potentiation assay'},
    "MIGRATION_ASSAY": {'description': 'Cell migration assay', 'meaning': 'BAO:0002110'},
    "IN_VITRO_TUMORIGENESIS": {'description': 'In vitro tumorigenesis assay'},
    "IN_VIVO_TUMOR_GROWTH": {'description': 'In vivo tumor growth assay'},
    "IN_VIVO_PDX_VIABILITY": {'description': 'In vivo patient-derived xenograft viability'},
    "MATRIGEL_TUMORIGENESIS": {'description': 'Matrigel-based tumorigenesis assay', 'aliases': ['Matrigel-based tumorigenesis assay']},
    "HIGH_CONTENT_SCREEN": {'description': 'High content screening assay', 'meaning': 'BAO:0000514'},
    "CELL_PAINTING": {'description': 'Cell painting morphological profiling', 'meaning': 'BAO:0020000'},
    "COMPOUND_SCREEN": {'description': 'Compound library screening'},
    "COMBINATION_SCREEN": {'description': 'Drug combination screening'},
    "SMALL_MOLECULE_LIBRARY_SCREEN": {'description': 'Small molecule library screen'},
    "REPORTER_GENE_ASSAY": {'description': 'Reporter gene assay', 'meaning': 'BAO:0000098'},
    "MASSIVELY_PARALLEL_REPORTER_ASSAY": {'description': 'Massively parallel reporter assay', 'aliases': ['MPRA']},
    "SPLIT_GFP_ASSAY": {'description': 'Split-GFP protein interaction assay', 'aliases': ['split-GFP assay']},
    "FOCUS_FORMING_ASSAY": {'description': 'Focus forming assay'},
    "OXYGEN_CONSUMPTION_ASSAY": {'description': 'Oxygen consumption rate measurement', 'meaning': 'BAO:0003028'},
    "ROS_ASSAY": {'description': 'Reactive oxygen species assay', 'aliases': ['reactive oxygen species assay']},
    "CALCIUM_RETENTION_ASSAY": {'description': 'Calcium retention capacity assay'},
    "TRANS_ENDOTHELIAL_RESISTANCE": {'description': 'Trans-endothelial electrical resistance measurement', 'aliases': ['trans-endothelial electrical resistance']},
    "CELL_PERMEABILITY_ASSAY": {'description': 'Cell permeability assay'},
    "PHARMACOKINETIC_ADME": {'description': 'Pharmacokinetic ADME assay', 'aliases': ['pharmocokinetic ADME assay']},
    "ARRAY": {'description': 'General array-based assay'},
    "HPLC": {'description': 'High-performance liquid chromatography', 'meaning': 'CHMO:0001009'},
    "ELECTROCHEMILUMINESCENCE": {'description': 'Electrochemiluminescence detection'},
    "STR_PROFILE": {'description': 'Short tandem repeat profiling'},
    "TIDE": {'description': 'Tracking of Indels by Decomposition'},
    "SURVIVAL_ASSAY": {'description': 'Cell or organism survival assay'},
}

class ClinicalBehavioralAssayEnum(RichEnum):
    """
    Clinical assessments and behavioral assays used in research
    """
    # Enum members
    CLINICAL_DATA = "CLINICAL_DATA"
    QUESTIONNAIRE = "QUESTIONNAIRE"
    INTERVIEW = "INTERVIEW"
    FOCUS_GROUP = "FOCUS_GROUP"
    SCALE = "SCALE"
    NEUROPSYCHOLOGICAL_ASSESSMENT = "NEUROPSYCHOLOGICAL_ASSESSMENT"
    COGNITIVE_ASSESSMENT = "COGNITIVE_ASSESSMENT"
    NIH_TOOLBOX = "NIH_TOOLBOX"
    PROMIS_COGNITIVE_FUNCTION = "PROMIS_COGNITIVE_FUNCTION"
    N_BACK_TASK = "N_BACK_TASK"
    CORSI_BLOCKS = "CORSI_BLOCKS"
    CBCL_1_5_5 = "CBCL_1_5_5"
    CBCL_6_18 = "CBCL_6_18"
    SRS = "SRS"
    SRS_2 = "SRS_2"
    BLOOD_CHEMISTRY = "BLOOD_CHEMISTRY"
    METABOLIC_SCREENING = "METABOLIC_SCREENING"
    GENOTYPING = "GENOTYPING"
    BODY_SIZE_MEASUREMENT = "BODY_SIZE_MEASUREMENT"
    GAIT_MEASUREMENT = "GAIT_MEASUREMENT"
    GRIP_STRENGTH = "GRIP_STRENGTH"
    HAND_HELD_DYNAMOMETRY = "HAND_HELD_DYNAMOMETRY"
    SIX_MINUTE_WALK_TEST = "SIX_MINUTE_WALK_TEST"
    ACTIGRAPHY = "ACTIGRAPHY"
    POLYSOMNOGRAPHY = "POLYSOMNOGRAPHY"
    QUANTITATIVE_SENSORY_TESTING = "QUANTITATIVE_SENSORY_TESTING"
    VON_FREY_TEST = "VON_FREY_TEST"
    ALGOMETRX_NOCIOMETER = "ALGOMETRX_NOCIOMETER"
    AUDITORY_BRAINSTEM_RESPONSE = "AUDITORY_BRAINSTEM_RESPONSE"
    PURE_TONE_AVERAGE = "PURE_TONE_AVERAGE"
    WORD_RECOGNITION_SCORE = "WORD_RECOGNITION_SCORE"
    DPOE = "DPOE"
    PATTERN_ERG = "PATTERN_ERG"
    OPTOKINETIC_REFLEX = "OPTOKINETIC_REFLEX"
    RICCARDI_ABLON_SCALES = "RICCARDI_ABLON_SCALES"
    SKINDEX_16 = "SKINDEX_16"
    CNF_SKINDEX = "CNF_SKINDEX"
    CDLQI = "CDLQI"
    FACEQ_DISTRESS = "FACEQ_DISTRESS"
    OPEN_FIELD_TEST = "OPEN_FIELD_TEST"
    ELEVATED_PLUS_MAZE = "ELEVATED_PLUS_MAZE"
    ROTAROD_TEST = "ROTAROD_TEST"
    ACTIVE_AVOIDANCE = "ACTIVE_AVOIDANCE"
    CONTEXTUAL_CONDITIONING = "CONTEXTUAL_CONDITIONING"
    NOVELTY_RESPONSE = "NOVELTY_RESPONSE"
    FEEDING_ASSAY = "FEEDING_ASSAY"

# Set metadata after class creation
ClinicalBehavioralAssayEnum._metadata = {
    "CLINICAL_DATA": {'description': 'Clinical data collection'},
    "QUESTIONNAIRE": {'description': 'Questionnaire-based assessment', 'meaning': 'OBI:0001504'},
    "INTERVIEW": {'description': 'Clinical or research interview'},
    "FOCUS_GROUP": {'description': 'Focus group discussion'},
    "SCALE": {'description': 'Clinical rating scale'},
    "NEUROPSYCHOLOGICAL_ASSESSMENT": {'description': 'Neuropsychological testing', 'meaning': 'OBI:0002508'},
    "COGNITIVE_ASSESSMENT": {'description': 'Cognitive function assessment'},
    "NIH_TOOLBOX": {'description': 'NIH Toolbox assessment battery'},
    "PROMIS_COGNITIVE_FUNCTION": {'description': 'PROMIS Cognitive Function measures'},
    "N_BACK_TASK": {'description': 'N-back working memory task', 'aliases': ['n-back task']},
    "CORSI_BLOCKS": {'description': 'Corsi block-tapping task'},
    "CBCL_1_5_5": {'description': 'Child Behavior Checklist for Ages 1.5-5', 'aliases': ['Child Behavior Checklist for Ages 1.5-5']},
    "CBCL_6_18": {'description': 'Child Behavior Checklist for Ages 6-18', 'aliases': ['Child Behavior Checklist for Ages 6-18']},
    "SRS": {'description': 'Social Responsiveness Scale', 'aliases': ['Social Responsiveness Scale']},
    "SRS_2": {'description': 'Social Responsiveness Scale Second Edition', 'aliases': ['Social Responsiveness Scale Second Edition']},
    "BLOOD_CHEMISTRY": {'description': 'Blood chemistry measurement', 'aliases': ['blood chemistry measurement']},
    "METABOLIC_SCREENING": {'description': 'Metabolic screening panel'},
    "GENOTYPING": {'description': 'Genotyping assay', 'meaning': 'OBI:0000435'},
    "BODY_SIZE_MEASUREMENT": {'description': 'Body size trait measurement', 'meaning': 'MMO:0000013', 'aliases': ['body size trait measurement']},
    "GAIT_MEASUREMENT": {'description': 'Gait analysis measurement', 'aliases': ['gait measurement']},
    "GRIP_STRENGTH": {'description': 'Grip strength measurement'},
    "HAND_HELD_DYNAMOMETRY": {'description': 'Hand-held dynamometry'},
    "SIX_MINUTE_WALK_TEST": {'description': 'Six-minute walk test', 'aliases': ['six-minute walk test']},
    "ACTIGRAPHY": {'description': 'Actigraphy monitoring'},
    "POLYSOMNOGRAPHY": {'description': 'Polysomnography sleep study'},
    "QUANTITATIVE_SENSORY_TESTING": {'description': 'Quantitative sensory testing'},
    "VON_FREY_TEST": {'description': 'Von Frey filament test', 'aliases': ['Von Frey test']},
    "ALGOMETRX_NOCIOMETER": {'description': 'AlgometRx Nociometer assessment'},
    "AUDITORY_BRAINSTEM_RESPONSE": {'description': 'Auditory brainstem response testing', 'aliases': ['ABR']},
    "PURE_TONE_AVERAGE": {'description': 'Pure tone average audiometry'},
    "WORD_RECOGNITION_SCORE": {'description': 'Word recognition score'},
    "DPOE": {'description': 'Distortion product otoacoustic emissions', 'aliases': ['distortion product otoacoustic emissions']},
    "PATTERN_ERG": {'description': 'Pattern electroretinogram', 'aliases': ['pattern electroretinogram']},
    "OPTOKINETIC_REFLEX": {'description': 'Optokinetic reflex assay', 'aliases': ['optokinetic reflex assay']},
    "RICCARDI_ABLON_SCALES": {'description': 'Riccardi and Ablon clinical severity scales'},
    "SKINDEX_16": {'description': 'Skindex-16 dermatology questionnaire'},
    "CNF_SKINDEX": {'description': 'Cutaneous neurofibroma Skindex', 'aliases': ['cNF-Skindex']},
    "CDLQI": {'description': "Children's Dermatology Life Quality Index Questionnaire", 'aliases': ["Children's Dermatology Life Quality Index Questionnaire"]},
    "FACEQ_DISTRESS": {'description': 'FACE-Q Appearance-related Distress', 'aliases': ['FACE-Q Appearance-related Distress']},
    "OPEN_FIELD_TEST": {'description': 'Open field locomotor test', 'meaning': 'MMO:0000093'},
    "ELEVATED_PLUS_MAZE": {'description': 'Elevated plus maze anxiety test', 'meaning': 'MMO:0000292', 'aliases': ['elevated plus maze test']},
    "ROTAROD_TEST": {'description': 'Rotarod motor coordination test', 'meaning': 'MMO:0000091', 'aliases': ['rotarod performance test']},
    "ACTIVE_AVOIDANCE": {'description': 'Active avoidance learning behavior assay', 'aliases': ['active avoidance learning behavior assay']},
    "CONTEXTUAL_CONDITIONING": {'description': 'Contextual conditioning behavior assay', 'aliases': ['contextual conditioning behavior assay']},
    "NOVELTY_RESPONSE": {'description': 'Novelty response behavior assay', 'aliases': ['novelty response behavior assay']},
    "FEEDING_ASSAY": {'description': 'Feeding behavior assay'},
}

__all__ = [
    "SequencingAssayEnum",
    "ImagingAssayEnum",
    "MassSpectrometryAssayEnum",
    "CellBasedAssayEnum",
    "ClinicalBehavioralAssayEnum",
]