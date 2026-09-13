"""
Medical Image De-identification Value Sets

Value sets for de-identifying medical imaging data before sharing and reuse. Covers the DICOM PS3.15 Annex E de-identification profile and options (with their DCM codes from Context ID 7050), the action codes that specify how each attribute is treated, the parts of an image object that can carry identifying information, the regulatory frameworks that define what must be removed, and the pixel-level "de-facing" methods and tools used to remove reconstructable facial features from head CT and MRI volumes.
Defacing only addresses pixel data. A complete de-identification pipeline also strips or pseudonymizes protected health information in the DICOM header, and anticipates adversarial re-identification such as face-recognition matching of surface renderings of head scans.

Generated from: medical/imaging_deidentification.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class DICOMDeidentificationMethodEnum(RichEnum):
    """
    The Basic Application Level Confidentiality Profile and its options defined in DICOM PS3.15 Annex E, as coded in PS3.16 Context ID 7050 (De-identification Method). These codes are recorded in the De-identification Method Code Sequence (0012,0064) to document what was done to an instance. The "Clean" options remove additional identifying content; the "Retain" options preserve information that the basic profile would otherwise remove.
    """
    # Enum members
    BASIC_APPLICATION_CONFIDENTIALITY_PROFILE = "BASIC_APPLICATION_CONFIDENTIALITY_PROFILE"
    CLEAN_PIXEL_DATA_OPTION = "CLEAN_PIXEL_DATA_OPTION"
    CLEAN_RECOGNIZABLE_VISUAL_FEATURES_OPTION = "CLEAN_RECOGNIZABLE_VISUAL_FEATURES_OPTION"
    CLEAN_GRAPHICS_OPTION = "CLEAN_GRAPHICS_OPTION"
    CLEAN_STRUCTURED_CONTENT_OPTION = "CLEAN_STRUCTURED_CONTENT_OPTION"
    CLEAN_DESCRIPTORS_OPTION = "CLEAN_DESCRIPTORS_OPTION"
    RETAIN_LONGITUDINAL_TEMPORAL_INFORMATION_FULL_DATES_OPTION = "RETAIN_LONGITUDINAL_TEMPORAL_INFORMATION_FULL_DATES_OPTION"
    RETAIN_LONGITUDINAL_TEMPORAL_INFORMATION_MODIFIED_DATES_OPTION = "RETAIN_LONGITUDINAL_TEMPORAL_INFORMATION_MODIFIED_DATES_OPTION"
    RETAIN_PATIENT_CHARACTERISTICS_OPTION = "RETAIN_PATIENT_CHARACTERISTICS_OPTION"
    RETAIN_DEVICE_IDENTITY_OPTION = "RETAIN_DEVICE_IDENTITY_OPTION"
    RETAIN_UIDS_OPTION = "RETAIN_UIDS_OPTION"
    RETAIN_SAFE_PRIVATE_OPTION = "RETAIN_SAFE_PRIVATE_OPTION"
    RETAIN_INSTITUTION_IDENTITY_OPTION = "RETAIN_INSTITUTION_IDENTITY_OPTION"

# Set metadata after class creation
DICOMDeidentificationMethodEnum._metadata = {
    "BASIC_APPLICATION_CONFIDENTIALITY_PROFILE": {'description': 'The baseline profile that removes or replaces all attributes known to carry identifying information, including UIDs, dates and descriptive text', 'meaning': 'DCM:113100', 'annotations': {'kind': 'profile'}},
    "CLEAN_PIXEL_DATA_OPTION": {'description': 'Burned-in identifying text and annotations in the pixel data are removed', 'meaning': 'DCM:113101', 'annotations': {'kind': 'clean option'}},
    "CLEAN_RECOGNIZABLE_VISUAL_FEATURES_OPTION": {'description': 'Recognizable visual features such as the face are removed from pixel data; this is the option under which de-facing is recorded', 'meaning': 'DCM:113102', 'annotations': {'kind': 'clean option'}},
    "CLEAN_GRAPHICS_OPTION": {'description': 'Identifying information in graphic annotations, overlays and presentation states is removed', 'meaning': 'DCM:113103', 'annotations': {'kind': 'clean option'}},
    "CLEAN_STRUCTURED_CONTENT_OPTION": {'description': 'Identifying information in structured report content items is removed', 'meaning': 'DCM:113104', 'annotations': {'kind': 'clean option'}},
    "CLEAN_DESCRIPTORS_OPTION": {'description': 'Free-text descriptors such as Study Description are cleaned of identifying content rather than removed', 'meaning': 'DCM:113105', 'annotations': {'kind': 'clean option'}},
    "RETAIN_LONGITUDINAL_TEMPORAL_INFORMATION_FULL_DATES_OPTION": {'description': 'Dates and times are retained unmodified to preserve the temporal relationship between studies', 'meaning': 'DCM:113106', 'annotations': {'kind': 'retain option'}},
    "RETAIN_LONGITUDINAL_TEMPORAL_INFORMATION_MODIFIED_DATES_OPTION": {'description': 'Dates and times are shifted consistently so that intervals between studies are preserved', 'meaning': 'DCM:113107', 'annotations': {'kind': 'retain option'}},
    "RETAIN_PATIENT_CHARACTERISTICS_OPTION": {'description': 'Physical characteristics such as age, sex, height and weight are retained', 'meaning': 'DCM:113108', 'annotations': {'kind': 'retain option'}},
    "RETAIN_DEVICE_IDENTITY_OPTION": {'description': 'Device identifying attributes such as manufacturer, model and serial number are retained', 'meaning': 'DCM:113109', 'annotations': {'kind': 'retain option'}},
    "RETAIN_UIDS_OPTION": {'description': 'Original UIDs are retained rather than replaced', 'meaning': 'DCM:113110', 'annotations': {'kind': 'retain option'}},
    "RETAIN_SAFE_PRIVATE_OPTION": {'description': 'Private attributes known not to contain identifying information are retained', 'meaning': 'DCM:113111', 'annotations': {'kind': 'retain option'}},
    "RETAIN_INSTITUTION_IDENTITY_OPTION": {'description': 'Institution identifying attributes such as institution name and address are retained', 'meaning': 'DCM:113112', 'annotations': {'kind': 'retain option'}},
}

class DICOMDeidentificationActionEnum(RichEnum):
    """
    Action codes from DICOM PS3.15 Table E.1-1a that specify how a de-identifier treats each attribute under the Basic Application Level Confidentiality Profile. Compound codes (for example Z/D) indicate that the first action applies unless the attribute's type requires the second to maintain IOD conformance. Permissible values use the DICOM code letters, with slashes replaced by underscores in compound codes.
    """
    # Enum members
    D = "D"
    Z = "Z"
    X = "X"
    K = "K"
    C = "C"
    U = "U"
    Z_D = "Z_D"
    X_Z = "X_Z"
    X_D = "X_D"
    X_Z_D = "X_Z_D"
    X_Z_U = "X_Z_U"

# Set metadata after class creation
DICOMDeidentificationActionEnum._metadata = {
    "D": {'description': 'Replace with a non-zero length value that may be a dummy value and consistent with the VR'},
    "Z": {'description': 'Replace with a zero length value, or a non-zero length value that may be a dummy value and consistent with the VR'},
    "X": {'description': 'Remove the attribute, and if the attribute is a sequence, remove all sequence items and their contained attributes'},
    "K": {'description': 'Keep unchanged for non-sequence attributes; cleaned for sequences'},
    "C": {'description': 'Replace with values of similar meaning known not to contain identifying information and consistent with the VR'},
    "U": {'description': 'Replace with a non-zero length UID that is internally consistent within a set of instances'},
    "Z_D": {'description': 'Z unless D is required to maintain IOD conformance (Type 2 versus Type 1)', 'aliases': ['Z/D']},
    "X_Z": {'description': 'X unless Z is required to maintain IOD conformance (Type 3 versus Type 2)', 'aliases': ['X/Z']},
    "X_D": {'description': 'X unless D is required to maintain IOD conformance (Type 3 versus Type 1)', 'aliases': ['X/D']},
    "X_Z_D": {'description': 'X unless Z or D is required to maintain IOD conformance (Type 3 versus Type 2 versus Type 1)', 'aliases': ['X/Z/D']},
    "X_Z_U": {'description': 'X unless Z or replacement of contained instance UIDs (U) is required to maintain IOD conformance (Type 3 versus Type 2 versus Type 1 sequences containing UID references)', 'aliases': ['X/Z/U*']},
}

class ImageDeidentificationTargetEnum(RichEnum):
    """
    The components of a medical imaging object that can carry identifying information and therefore need to be addressed by a de-identification workflow. A workflow first assesses whether an image requires pixel-level (face or head) de-identification or only metadata de-identification.
    """
    # Enum members
    HEADER_METADATA = "HEADER_METADATA"
    PRIVATE_ATTRIBUTES = "PRIVATE_ATTRIBUTES"
    BURNED_IN_ANNOTATION = "BURNED_IN_ANNOTATION"
    FACIAL_FEATURES = "FACIAL_FEATURES"
    UNIQUE_IDENTIFIERS = "UNIQUE_IDENTIFIERS"
    STRUCTURED_CONTENT = "STRUCTURED_CONTENT"

# Set metadata after class creation
ImageDeidentificationTargetEnum._metadata = {
    "HEADER_METADATA": {'description': 'Standard DICOM attributes such as patient name, identifiers, birth date and study dates'},
    "PRIVATE_ATTRIBUTES": {'description': 'Vendor-specific private tags that may contain identifying information and are not covered by the standard attribute list'},
    "BURNED_IN_ANNOTATION": {'description': 'Text or graphics rendered into the pixel data, common in ultrasound, secondary capture and screenshots'},
    "FACIAL_FEATURES": {'description': 'Facial surface anatomy reconstructable from volumetric head CT or MRI pixel data, or visible in photographs and video'},
    "UNIQUE_IDENTIFIERS": {'description': 'Study, series and instance UIDs and accession numbers that can link an instance back to the source system'},
    "STRUCTURED_CONTENT": {'description': 'Identifying content in structured reports, overlays, presentation states and embedded documents'},
}

class DeidentificationRegulatoryFrameworkEnum(RichEnum):
    """
    Regulations and standards that define when medical imaging data is considered de-identified. Under HIPAA, full-face photographs and comparable images are direct identifiers; under the GDPR, facial images are biometric personal data requiring special handling.
    """
    # Enum members
    HIPAA_SAFE_HARBOR = "HIPAA_SAFE_HARBOR"
    HIPAA_EXPERT_DETERMINATION = "HIPAA_EXPERT_DETERMINATION"
    GDPR_ANONYMISATION = "GDPR_ANONYMISATION"
    GDPR_PSEUDONYMISATION = "GDPR_PSEUDONYMISATION"
    DICOM_PS3_15_CONFIDENTIALITY_PROFILE = "DICOM_PS3_15_CONFIDENTIALITY_PROFILE"
    MIDI_TASK_GROUP_RECOMMENDATIONS = "MIDI_TASK_GROUP_RECOMMENDATIONS"

# Set metadata after class creation
DeidentificationRegulatoryFrameworkEnum._metadata = {
    "HIPAA_SAFE_HARBOR": {'description': 'US HIPAA Privacy Rule method requiring removal of 18 specified identifier types, including full-face photographs and comparable images', 'annotations': {'jurisdiction': 'United States', 'citation': '45 CFR 164.514(b)(2)'}},
    "HIPAA_EXPERT_DETERMINATION": {'description': 'US HIPAA Privacy Rule method in which a qualified expert determines that the risk of re-identification is very small', 'annotations': {'jurisdiction': 'United States', 'citation': '45 CFR 164.514(b)(1)'}},
    "GDPR_ANONYMISATION": {'description': 'Irreversible processing such that the data subject is no longer identifiable, taking the data outside the scope of the EU General Data Protection Regulation', 'meaning': 'NCIT:C142392', 'annotations': {'jurisdiction': 'European Union'}, 'aliases': ['GDPR anonymisation']},
    "GDPR_PSEUDONYMISATION": {'description': 'Processing so that data can no longer be attributed to a subject without additional information kept separately, as defined in GDPR Article 4(5)', 'meaning': 'NCIT:C142654', 'annotations': {'jurisdiction': 'European Union'}, 'aliases': ['GDPR pseudonymisation']},
    "DICOM_PS3_15_CONFIDENTIALITY_PROFILE": {'description': "The DICOM standard's own de-identification profile and options, designed to satisfy known regulations", 'annotations': {'jurisdiction': 'international'}},
    "MIDI_TASK_GROUP_RECOMMENDATIONS": {'description': 'Best practices and recommendations of the Medical Image De-Identification (MIDI) Task Group (Clunie et al.)', 'annotations': {'jurisdiction': 'international'}},
}

class DefacingMethodEnum(RichEnum):
    """
    Approaches to pixel-level de-identification that remove or obscure facial features in head imaging. Skull-stripping removes all non-brain tissue and may discard useful anatomy; face-specific methods aim to remove only facial features while preserving as much of the head volume as possible.
    """
    # Enum members
    SKULL_STRIPPING = "SKULL_STRIPPING"
    TEMPLATE_BASED_MASKING = "TEMPLATE_BASED_MASKING"
    SURFACE_BLURRING = "SURFACE_BLURRING"
    SHEARING_PLANE = "SHEARING_PLANE"
    DEEP_LEARNING_SEGMENTATION = "DEEP_LEARNING_SEGMENTATION"
    REFACING = "REFACING"
    MANUAL_MASKING = "MANUAL_MASKING"
    FACE_DETECTION_AND_BLURRING = "FACE_DETECTION_AND_BLURRING"
    MANUAL_CROP_OR_BLUR = "MANUAL_CROP_OR_BLUR"

# Set metadata after class creation
DefacingMethodEnum._metadata = {
    "SKULL_STRIPPING": {'description': 'Removal of all non-brain tissue including scalp, skull and face, for example with FSL BET or AFNI 3dSkullStrip', 'annotations': {'preserves_skull': 'false'}, 'aliases': ['brain extraction']},
    "TEMPLATE_BASED_MASKING": {'description': 'Registration of the image to a standard brain template such as MNI152 followed by application of a predefined binary face mask that zeros out facial voxels', 'annotations': {'preserves_skull': 'true', 'example_tools': 'PyDeface, FreeSurfer mri_deface, mydeface'}},
    "SURFACE_BLURRING": {'description': 'Diffusion or blurring of face surface voxels to obscure identity while preserving head shape, as in Milchenko and Marcus (2013)', 'annotations': {'preserves_skull': 'true'}},
    "SHEARING_PLANE": {'description': 'Removal of the front of the head by computing a plane through the head and discarding voxels in front of it, as in QuickShear', 'annotations': {'preserves_skull': 'partial'}, 'aliases': ['cropping plane']},
    "DEEP_LEARNING_SEGMENTATION": {'description': 'Use of a trained neural network such as a 3D U-Net to segment facial features (eyes, ears, nose) and mask or blur them', 'annotations': {'preserves_skull': 'true', 'example_tools': 'DeepDefacer, Asan Defacer'}},
    "REFACING": {'description': "Replacement of the subject's face with an average or synthetic face so that images retain a realistic head surface", 'annotations': {'preserves_skull': 'true', 'example_tools': 'AFNI refacer'}},
    "MANUAL_MASKING": {'description': 'Interactive painting or erosion of a face mask in an image editor such as 3D Slicer or ITK-SNAP, followed by zeroing or blurring of masked voxels', 'annotations': {'preserves_skull': 'true'}},
    "FACE_DETECTION_AND_BLURRING": {'description': 'Frame-by-frame detection of faces in 2D images or video followed by blurring, pixelation or masking, for example with OpenCV Haar cascades', 'annotations': {'applicable_to': 'photographs, video'}},
    "MANUAL_CROP_OR_BLUR": {'description': 'Manual cropping or blurring of the face region in photographs or video with an image or video editor', 'annotations': {'applicable_to': 'photographs, video'}},
}

class DefacingToolEnum(RichEnum):
    """
    Software tools and pipelines used for pixel-level de-identification of head imaging and photographs, with their supported modalities, method and licensing. Metadata-only anonymizers are included for completeness because they are commonly paired with defacing tools, but they do not remove facial features.
    """
    # Enum members
    PYDEFACE = "PYDEFACE"
    FREESURFER_MRI_DEFACE = "FREESURFER_MRI_DEFACE"
    AFNI_REFACER = "AFNI_REFACER"
    QUICKSHEAR = "QUICKSHEAR"
    DEEPDEFACER = "DEEPDEFACER"
    ASAN_DEFACER = "ASAN_DEFACER"
    MYDEFACE = "MYDEFACE"
    MASK_FACE = "MASK_FACE"
    FSL_BET = "FSL_BET"
    AFNI_3DSKULLSTRIP = "AFNI_3DSKULLSTRIP"
    ITK_SNAP = "ITK_SNAP"
    SLICER_3D = "SLICER_3D"
    IMAGEJ_FIJI = "IMAGEJ_FIJI"
    OPENCV = "OPENCV"
    OSIRIX_HOROS_PLUGIN = "OSIRIX_HOROS_PLUGIN"
    PIXELMED_DICOM_ANONYMIZER = "PIXELMED_DICOM_ANONYMIZER"
    MANUAL_PHOTO_VIDEO_EDITING = "MANUAL_PHOTO_VIDEO_EDITING"

# Set metadata after class creation
DefacingToolEnum._metadata = {
    "PYDEFACE": {'description': 'Aligns a T1-weighted MRI to a template with FSL FLIRT and zeros out voxels in a predefined facial mask', 'annotations': {'modality': 'MRI (T1w)', 'method': 'template-based masking', 'license': 'BSD', 'url': 'https://github.com/poldracklab/pydeface'}},
    "FREESURFER_MRI_DEFACE": {'description': 'Template mask defacing using affine registration to fit a generic face mask, distributed with FreeSurfer', 'annotations': {'modality': 'MRI (T1w)', 'method': 'template-based masking', 'license': 'FreeSurfer'}},
    "AFNI_REFACER": {'description': 'AFNI template-based defacing and refacing tool, often combined with skull stripping', 'annotations': {'modality': 'MRI (T1w)', 'method': 'refacing', 'license': 'AFNI (open source)'}},
    "QUICKSHEAR": {'description': 'Computes a shearing plane through the head and removes the front of the head', 'annotations': {'modality': 'MRI (T1w)', 'method': 'shearing plane', 'license': 'open source'}},
    "DEEPDEFACER": {'description': '3D U-Net trained to generate a facial mask from T1 MRI scans', 'annotations': {'modality': 'MRI (T1w, T2w)', 'method': 'deep learning segmentation', 'license': 'open source'}},
    "ASAN_DEFACER": {'description': '3D U-Net that segments eyes, ears and nose and masks them, applicable to MRI and CT', 'annotations': {'modality': 'MRI, CT', 'method': 'deep learning segmentation', 'license': 'open source'}},
    "MYDEFACE": {'description': 'Defacing utility similar to PyDeface using an FSL FLIRT-registered mask', 'annotations': {'modality': 'MRI (T1w, FLAIR)', 'method': 'template-based masking', 'license': 'BSD', 'url': 'https://github.com/neurolabusc/mydeface'}},
    "MASK_FACE": {'description': 'Surface blurring tool from Milchenko and Marcus that obscures surface anatomy in volumetric data', 'annotations': {'modality': 'MRI, CT', 'method': 'surface blurring', 'license': 'open source'}},
    "FSL_BET": {'description': 'FMRIB Software Library Brain Extraction Tool; removes all non-brain tissue', 'annotations': {'modality': 'MRI, CT, PET', 'method': 'skull stripping', 'license': 'FSL (open source)'}},
    "AFNI_3DSKULLSTRIP": {'description': 'AFNI brain extraction program; removes all non-brain tissue', 'annotations': {'modality': 'MRI, CT, PET', 'method': 'skull stripping', 'license': 'AFNI (open source)'}},
    "ITK_SNAP": {'description': 'Interactive segmentation tool used to manually paint or erode a face mask in any 3D volume', 'annotations': {'modality': 'any 3D volume', 'method': 'manual masking', 'license': 'GPL'}},
    "SLICER_3D": {'description': 'Image computing platform used to manually paint a face mask over a region of interest', 'annotations': {'modality': 'any 3D volume', 'method': 'manual masking', 'license': 'BSD-style'}},
    "IMAGEJ_FIJI": {'description': 'General image analysis tools used to manually blur or crop the face region in 2D or 3D images', 'annotations': {'modality': '2D and 3D images', 'method': 'manual crop or blur', 'license': 'open source'}},
    "OPENCV": {'description': 'Computer vision library used for face detection (for example Haar cascades) followed by blurring or pixelation in video and 2D images', 'annotations': {'modality': 'video, 2D images', 'method': 'face detection and blurring', 'license': 'Apache-2.0'}},
    "OSIRIX_HOROS_PLUGIN": {'description': 'Viewer plugins offering built-in anonymization with face removal options for multi-modality DICOM', 'annotations': {'modality': 'DICOM (multi-modality)', 'method': 'template-based masking', 'license': 'commercial / free'}},
    "PIXELMED_DICOM_ANONYMIZER": {'description': 'Metadata anonymization only; does not mask faces', 'annotations': {'modality': 'DICOM files', 'method': 'metadata anonymization', 'license': 'BSD'}},
    "MANUAL_PHOTO_VIDEO_EDITING": {'description': 'Cropping or blurring faces in photographs and videos with general-purpose editors', 'annotations': {'modality': 'photographs, video', 'method': 'manual crop or blur'}},
}

__all__ = [
    "DICOMDeidentificationMethodEnum",
    "DICOMDeidentificationActionEnum",
    "ImageDeidentificationTargetEnum",
    "DeidentificationRegulatoryFrameworkEnum",
    "DefacingMethodEnum",
    "DefacingToolEnum",
]