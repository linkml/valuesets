"""
Neuroimaging Value Sets

Value sets for neuroimaging including MRI modalities, fMRI paradigms, acquisition parameters, and image analysis methods.

Generated from: medical/neuroimaging.yaml
"""

from __future__ import annotations

from typing import Dict, Any, Optional
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
    "STRUCTURAL_T1": {'description': 'High-resolution anatomical imaging with T1 contrast', 'meaning': 'NCIT:C116455', 'annotations': {'contrast_mechanism': 'T1 relaxation', 'typical_use': 'anatomical reference, volumetric analysis', 'tissue_contrast': 'good gray/white matter contrast'}},
    "STRUCTURAL_T2": {'description': 'Structural imaging with T2 contrast', 'meaning': 'NCIT:C116456', 'annotations': {'contrast_mechanism': 'T2 relaxation', 'typical_use': 'pathology detection, CSF visualization', 'tissue_contrast': 'good fluid contrast'}},
    "FLAIR": {'description': 'T2-weighted sequence with CSF signal suppressed', 'meaning': 'NCIT:C82392', 'annotations': {'contrast_mechanism': 'T2 with fluid suppression', 'typical_use': 'lesion detection, periventricular pathology', 'advantage': 'suppresses CSF signal'}},
    "BOLD_FMRI": {'description': 'Functional MRI based on blood oxygenation changes', 'meaning': 'NCIT:C17958', 'annotations': {'contrast_mechanism': 'BOLD signal', 'typical_use': 'brain activation mapping', 'temporal_resolution': 'seconds'}},
    "ASL": {'description': 'Perfusion imaging using magnetically labeled blood', 'meaning': 'NCIT:C116450', 'annotations': {'contrast_mechanism': 'arterial blood labeling', 'typical_use': 'cerebral blood flow measurement', 'advantage': 'no contrast agent required'}},
    "DWI": {'description': 'Imaging sensitive to water molecule diffusion', 'meaning': 'mesh:D038524', 'annotations': {'contrast_mechanism': 'water diffusion', 'typical_use': 'stroke detection, fiber tracking', 'parameter': 'apparent diffusion coefficient'}},
    "DTI": {'description': 'Advanced diffusion imaging with directional information', 'meaning': 'NCIT:C64862', 'annotations': {'contrast_mechanism': 'directional diffusion', 'typical_use': 'white matter tractography', 'parameters': 'fractional anisotropy, mean diffusivity'}},
    "PERFUSION_DSC": {'description': 'Perfusion imaging using contrast agent bolus', 'meaning': 'NCIT:C116459', 'annotations': {'contrast_mechanism': 'contrast agent dynamics', 'typical_use': 'cerebral blood flow, blood volume', 'requires': 'gadolinium contrast'}},
    "PERFUSION_DCE": {'description': 'Perfusion imaging with pharmacokinetic modeling', 'meaning': 'NCIT:C116458', 'annotations': {'contrast_mechanism': 'contrast enhancement kinetics', 'typical_use': 'blood-brain barrier permeability', 'analysis': 'pharmacokinetic modeling'}},
    "SWI": {'description': 'High-resolution venography and iron detection', 'meaning': 'NCIT:C121377', 'annotations': {'contrast_mechanism': 'magnetic susceptibility', 'typical_use': 'venography, microbleeds, iron deposits', 'strength': 'high field preferred'}},
    "TASK_FMRI": {'description': 'fMRI during specific cognitive or motor tasks', 'meaning': 'NCIT:C178023', 'annotations': {'paradigm': 'stimulus-response', 'typical_use': 'localization of brain functions', 'analysis': 'statistical parametric mapping'}},
    "RESTING_STATE_FMRI": {'description': 'fMRI acquired at rest without explicit tasks', 'meaning': 'NCIT:C178024', 'annotations': {'paradigm': 'no task', 'typical_use': 'functional connectivity analysis', 'networks': 'default mode, attention, executive'}},
    "FUNCTIONAL_CONNECTIVITY": {'description': 'Analysis of temporal correlations between brain regions', 'meaning': 'NCIT:C116454', 'annotations': {'analysis_type': 'connectivity mapping', 'typical_use': 'network analysis', 'metric': 'correlation coefficients'}},
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
    "GRADIENT_ECHO": {'description': 'Fast imaging sequence using gradient reversal', 'annotations': {'speed': 'fast', 'typical_use': 'T2*, functional imaging', 'artifact_sensitivity': 'susceptible to magnetic field inhomogeneity'}},
    "SPIN_ECHO": {'description': 'Sequence using 180-degree refocusing pulse', 'annotations': {'speed': 'slower', 'typical_use': 'T2 imaging, reduced artifacts', 'artifact_resistance': 'good'}},
    "EPI": {'description': 'Ultrafast imaging sequence', 'annotations': {'speed': 'very fast', 'typical_use': 'functional MRI, diffusion imaging', 'temporal_resolution': 'subsecond'}},
    "MPRAGE": {'description': 'T1-weighted 3D sequence with preparation pulse', 'annotations': {'image_type': 'T1-weighted', 'typical_use': 'high-resolution anatomical imaging', 'dimension': '3D'}},
    "SPACE": {'description': '3D turbo spin echo sequence', 'annotations': {'image_type': 'T2-weighted', 'typical_use': 'high-resolution T2 imaging', 'dimension': '3D'}},
    "TRUFI": {'description': 'Balanced steady-state free precession sequence', 'annotations': {'contrast': 'mixed T1/T2', 'typical_use': 'cardiac imaging, fast scanning', 'signal': 'high'}},
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
    "T1_WEIGHTED": {'description': 'Image contrast based on T1 relaxation times', 'annotations': {'tissue_contrast': 'gray matter darker than white matter', 'typical_use': 'anatomical structure'}},
    "T2_WEIGHTED": {'description': 'Image contrast based on T2 relaxation times', 'annotations': {'tissue_contrast': 'CSF bright, gray matter brighter than white', 'typical_use': 'pathology detection'}},
    "T2_STAR": {'description': 'Image contrast sensitive to magnetic susceptibility', 'annotations': {'sensitivity': 'blood, iron, air-tissue interfaces', 'typical_use': 'functional imaging, venography'}},
    "PROTON_DENSITY": {'description': 'Image contrast based on hydrogen density', 'annotations': {'tissue_contrast': 'proportional to water content', 'typical_use': 'joint imaging, some brain pathology'}},
    "DIFFUSION_WEIGHTED": {'description': 'Image contrast based on water diffusion', 'annotations': {'sensitivity': 'molecular motion', 'typical_use': 'stroke, tumor cellularity'}},
    "PERFUSION_WEIGHTED": {'description': 'Image contrast based on blood flow dynamics', 'annotations': {'measurement': 'cerebral blood flow/volume', 'typical_use': 'stroke, tumor vascularity'}},
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
    "BLOCK_DESIGN": {'description': 'Alternating blocks of task and rest conditions', 'annotations': {'duration': 'typically 15-30 seconds per block', 'advantage': 'high statistical power', 'typical_use': 'robust activation detection'}},
    "EVENT_RELATED": {'description': 'Brief stimuli presented at varying intervals', 'annotations': {'duration': 'single events (seconds)', 'advantage': 'flexible timing, event separation', 'typical_use': 'studying cognitive processes'}},
    "MIXED_DESIGN": {'description': 'Combination of block and event-related elements', 'annotations': {'flexibility': 'high', 'advantage': 'sustained and transient responses', 'complexity': 'high'}},
    "RESTING_STATE": {'description': 'No explicit task, spontaneous brain activity', 'annotations': {'instruction': 'rest, eyes open/closed', 'duration': 'typically 5-10 minutes', 'analysis': 'functional connectivity'}},
    "NATURALISTIC": {'description': 'Ecologically valid stimuli (movies, stories)', 'annotations': {'stimulus_type': 'complex, realistic', 'advantage': 'ecological validity', 'analysis': 'inter-subject correlation'}},
}

__all__ = [
    "MRIModalityEnum",
    "MRISequenceTypeEnum",
    "MRIContrastTypeEnum",
    "FMRIParadigmTypeEnum",
]