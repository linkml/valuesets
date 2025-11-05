"""
Neuroimaging Value Sets

Value sets for neuroimaging including MRI modalities, fMRI paradigms, acquisition parameters, and image analysis methods.

Generated from: medical/neuroimaging.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class MRIModalityEnum(RichEnum):
    """
    MRI imaging modalities and techniques
    """
    # Enum members
    STRUCTURAL_T1 = "STRUCTURAL_T1"
    STRUCTURAL_T2 = "STRUCTURAL_T2"
    FLAIR = "FLAIR"
    BOLD_FMRI = "BOLD_FMRI"
    ASL = "ASL"
    DWI = "DWI"
    DTI = "DTI"
    PERFUSION_DSC = "PERFUSION_DSC"
    PERFUSION_DCE = "PERFUSION_DCE"
    SWI = "SWI"
    TASK_FMRI = "TASK_FMRI"
    RESTING_STATE_FMRI = "RESTING_STATE_FMRI"
    FUNCTIONAL_CONNECTIVITY = "FUNCTIONAL_CONNECTIVITY"

# Set metadata after class creation
MRIModalityEnum._metadata = {
    "STRUCTURAL_T1": {'description': 'High-resolution anatomical imaging with T1 contrast', 'meaning': 'NCIT:C116455', 'annotations': {'contrast_mechanism': 'T1 relaxation', 'typical_use': 'anatomical reference, volumetric analysis', 'tissue_contrast': 'good gray/white matter contrast'}, 'aliases': ['High Field Strength Magnetic Resonance Imaging']},
    "STRUCTURAL_T2": {'description': 'Structural imaging with T2 contrast', 'meaning': 'NCIT:C116456', 'annotations': {'contrast_mechanism': 'T2 relaxation', 'typical_use': 'pathology detection, CSF visualization', 'tissue_contrast': 'good fluid contrast'}, 'aliases': ['Low Field Strength Magnetic Resonance Imaging']},
    "FLAIR": {'description': 'T2-weighted sequence with CSF signal suppressed', 'meaning': 'NCIT:C82392', 'annotations': {'contrast_mechanism': 'T2 with fluid suppression', 'typical_use': 'lesion detection, periventricular pathology', 'advantage': 'suppresses CSF signal'}},
    "BOLD_FMRI": {'description': 'Functional MRI based on blood oxygenation changes', 'meaning': 'NCIT:C17958', 'annotations': {'contrast_mechanism': 'BOLD signal', 'typical_use': 'brain activation mapping', 'temporal_resolution': 'seconds'}, 'aliases': ['Functional Magnetic Resonance Imaging']},
    "ASL": {'description': 'Perfusion imaging using magnetically labeled blood', 'meaning': 'NCIT:C116450', 'annotations': {'contrast_mechanism': 'arterial blood labeling', 'typical_use': 'cerebral blood flow measurement', 'advantage': 'no contrast agent required'}, 'aliases': ['Arterial Spin Labeling Magnetic Resonance Imaging']},
    "DWI": {'description': 'Imaging sensitive to water molecule diffusion', 'meaning': 'mesh:D038524', 'annotations': {'contrast_mechanism': 'water diffusion', 'typical_use': 'stroke detection, fiber tracking', 'parameter': 'apparent diffusion coefficient'}},
    "DTI": {'description': 'Advanced diffusion imaging with directional information', 'meaning': 'NCIT:C64862', 'annotations': {'contrast_mechanism': 'directional diffusion', 'typical_use': 'white matter tractography', 'parameters': 'fractional anisotropy, mean diffusivity'}},
    "PERFUSION_DSC": {'description': 'Perfusion imaging using contrast agent bolus', 'meaning': 'NCIT:C116459', 'annotations': {'contrast_mechanism': 'contrast agent dynamics', 'typical_use': 'cerebral blood flow, blood volume', 'requires': 'gadolinium contrast'}, 'aliases': ['Secretin-Enhanced Magnetic Resonance Imaging']},
    "PERFUSION_DCE": {'description': 'Perfusion imaging with pharmacokinetic modeling', 'meaning': 'NCIT:C116458', 'annotations': {'contrast_mechanism': 'contrast enhancement kinetics', 'typical_use': 'blood-brain barrier permeability', 'analysis': 'pharmacokinetic modeling'}, 'aliases': ['Multiparametric Magnetic Resonance Imaging']},
    "SWI": {'description': 'High-resolution venography and iron detection', 'meaning': 'NCIT:C121377', 'annotations': {'contrast_mechanism': 'magnetic susceptibility', 'typical_use': 'venography, microbleeds, iron deposits', 'strength': 'high field preferred'}},
    "TASK_FMRI": {'description': 'fMRI during specific cognitive or motor tasks', 'meaning': 'NCIT:C178023', 'annotations': {'paradigm': 'stimulus-response', 'typical_use': 'localization of brain functions', 'analysis': 'statistical parametric mapping'}, 'aliases': ['Task Functional Magnetic Resonance Imaging']},
    "RESTING_STATE_FMRI": {'description': 'fMRI acquired at rest without explicit tasks', 'meaning': 'NCIT:C178024', 'annotations': {'paradigm': 'no task', 'typical_use': 'functional connectivity analysis', 'networks': 'default mode, attention, executive'}, 'aliases': ['Resting Functional Magnetic Resonance Imaging']},
    "FUNCTIONAL_CONNECTIVITY": {'description': 'Analysis of temporal correlations between brain regions', 'meaning': 'NCIT:C116454', 'annotations': {'analysis_type': 'connectivity mapping', 'typical_use': 'network analysis', 'metric': 'correlation coefficients'}, 'aliases': ['Functional Connectivity Magnetic Resonance Imaging']},
}

class MRISequenceTypeEnum(RichEnum):
    """
    MRI pulse sequence types
    """
    # Enum members
    GRADIENT_ECHO = "GRADIENT_ECHO"
    SPIN_ECHO = "SPIN_ECHO"
    EPI = "EPI"
    MPRAGE = "MPRAGE"
    SPACE = "SPACE"
    TRUFI = "TRUFI"

# Set metadata after class creation
MRISequenceTypeEnum._metadata = {
    "GRADIENT_ECHO": {'description': 'Fast imaging sequence using gradient reversal', 'meaning': 'NCIT:C154542', 'annotations': {'speed': 'fast', 'typical_use': 'T2*, functional imaging', 'artifact_sensitivity': 'susceptible to magnetic field inhomogeneity'}, 'aliases': ['Gradient Echo MRI']},
    "SPIN_ECHO": {'description': 'Sequence using 180-degree refocusing pulse', 'meaning': 'CHMO:0001868', 'annotations': {'speed': 'slower', 'typical_use': 'T2 imaging, reduced artifacts', 'artifact_resistance': 'good'}, 'aliases': ['spin echo pulse sequence']},
    "EPI": {'description': 'Ultrafast imaging sequence', 'meaning': 'NCIT:C17558', 'annotations': {'speed': 'very fast', 'typical_use': 'functional MRI, diffusion imaging', 'temporal_resolution': 'subsecond'}},
    "MPRAGE": {'description': 'T1-weighted 3D sequence with preparation pulse', 'meaning': 'NCIT:C118462', 'annotations': {'image_type': 'T1-weighted', 'typical_use': 'high-resolution anatomical imaging', 'dimension': '3D'}, 'aliases': ['Magnetization-Prepared Rapid Gradient Echo MRI']},
    "SPACE": {'description': '3D turbo spin echo sequence', 'annotations': {'image_type': 'T2-weighted', 'typical_use': 'high-resolution T2 imaging', 'dimension': '3D'}},
    "TRUFI": {'description': 'Balanced steady-state free precession sequence', 'meaning': 'NCIT:C200534', 'annotations': {'contrast': 'mixed T1/T2', 'typical_use': 'cardiac imaging, fast scanning', 'signal': 'high'}, 'aliases': ['Constructive Interference In Steady State']},
}

class MRIContrastTypeEnum(RichEnum):
    """
    MRI image contrast mechanisms
    """
    # Enum members
    T1_WEIGHTED = "T1_WEIGHTED"
    T2_WEIGHTED = "T2_WEIGHTED"
    T2_STAR = "T2_STAR"
    PROTON_DENSITY = "PROTON_DENSITY"
    DIFFUSION_WEIGHTED = "DIFFUSION_WEIGHTED"
    PERFUSION_WEIGHTED = "PERFUSION_WEIGHTED"

# Set metadata after class creation
MRIContrastTypeEnum._metadata = {
    "T1_WEIGHTED": {'description': 'Image contrast based on T1 relaxation times', 'meaning': 'NCIT:C180727', 'annotations': {'tissue_contrast': 'gray matter darker than white matter', 'typical_use': 'anatomical structure'}, 'aliases': ['T1-Weighted Magnetic Resonance Imaging']},
    "T2_WEIGHTED": {'description': 'Image contrast based on T2 relaxation times', 'meaning': 'NCIT:C180729', 'annotations': {'tissue_contrast': 'CSF bright, gray matter brighter than white', 'typical_use': 'pathology detection'}, 'aliases': ['T2-Weighted Magnetic Resonance Imaging']},
    "T2_STAR": {'description': 'Image contrast sensitive to magnetic susceptibility', 'meaning': 'NCIT:C156447', 'annotations': {'sensitivity': 'blood, iron, air-tissue interfaces', 'typical_use': 'functional imaging, venography'}, 'aliases': ['T2 (Observed)-Weighted Imaging']},
    "PROTON_DENSITY": {'description': 'Image contrast based on hydrogen density', 'meaning': 'NCIT:C170797', 'annotations': {'tissue_contrast': 'proportional to water content', 'typical_use': 'joint imaging, some brain pathology'}, 'aliases': ['Proton Density MRI']},
    "DIFFUSION_WEIGHTED": {'description': 'Image contrast based on water diffusion', 'meaning': 'NCIT:C111116', 'annotations': {'sensitivity': 'molecular motion', 'typical_use': 'stroke, tumor cellularity'}, 'aliases': ['Diffusion Weighted Imaging']},
    "PERFUSION_WEIGHTED": {'description': 'Image contrast based on blood flow dynamics', 'meaning': 'mesh:D000098642', 'annotations': {'measurement': 'cerebral blood flow/volume', 'typical_use': 'stroke, tumor vascularity'}},
}

class FMRIParadigmTypeEnum(RichEnum):
    """
    fMRI experimental paradigm types
    """
    # Enum members
    BLOCK_DESIGN = "BLOCK_DESIGN"
    EVENT_RELATED = "EVENT_RELATED"
    MIXED_DESIGN = "MIXED_DESIGN"
    RESTING_STATE = "RESTING_STATE"
    NATURALISTIC = "NATURALISTIC"

# Set metadata after class creation
FMRIParadigmTypeEnum._metadata = {
    "BLOCK_DESIGN": {'description': 'Alternating blocks of task and rest conditions', 'meaning': 'STATO:0000046', 'annotations': {'duration': 'typically 15-30 seconds per block', 'advantage': 'high statistical power', 'typical_use': 'robust activation detection'}},
    "EVENT_RELATED": {'description': 'Brief stimuli presented at varying intervals', 'meaning': 'EDAM:topic_3678', 'annotations': {'duration': 'single events (seconds)', 'advantage': 'flexible timing, event separation', 'typical_use': 'studying cognitive processes'}, 'aliases': ['Experimental design and studies']},
    "MIXED_DESIGN": {'description': 'Combination of block and event-related elements', 'meaning': 'EDAM:topic_3678', 'annotations': {'flexibility': 'high', 'advantage': 'sustained and transient responses', 'complexity': 'high'}, 'aliases': ['Experimental design and studies']},
    "RESTING_STATE": {'description': 'No explicit task, spontaneous brain activity', 'meaning': 'NCIT:C178024', 'annotations': {'instruction': 'rest, eyes open/closed', 'duration': 'typically 5-10 minutes', 'analysis': 'functional connectivity'}, 'aliases': ['Resting Functional Magnetic Resonance Imaging']},
    "NATURALISTIC": {'description': 'Ecologically valid stimuli (movies, stories)', 'meaning': 'EDAM:topic_3678', 'annotations': {'stimulus_type': 'complex, realistic', 'advantage': 'ecological validity', 'analysis': 'inter-subject correlation'}, 'aliases': ['Experimental design and studies']},
}

__all__ = [
    "MRIModalityEnum",
    "MRISequenceTypeEnum",
    "MRIContrastTypeEnum",
    "FMRIParadigmTypeEnum",
]