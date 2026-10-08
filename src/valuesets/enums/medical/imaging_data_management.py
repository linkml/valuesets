"""
Medical Imaging Data Management Value Sets

Value sets for managing medical imaging data through its research lifecycle, from extraction out of clinical repositories through validation, quality assessment and de-identification to AI-ready datasets. Covers the lifecycle stages, the types of source systems that hold imaging data, the categories of structural and semantic problems found by DICOM validation tools, the image quality metrics computed during pixel data validation, the interoperability standards used to link images to clinical records, and the NIH Bridge2AI data generation projects that produce AI-ready imaging datasets.

Generated from: medical/imaging_data_management.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class ImagingDataLifecycleStageEnum(RichEnum):
    """
    Sequential stages of DICOM data management for preparing FAIR, AI-ready medical imaging datasets. Stages after extraction form the data reliability workflow that checks that imaging data is complete, standardized and biologically plausible before sharing.
    """
    # Enum members
    DATA_EXTRACTION_AND_METADATA_CHARACTERIZATION = "DATA_EXTRACTION_AND_METADATA_CHARACTERIZATION"
    FILE_INTEGRITY_VERIFICATION = "FILE_INTEGRITY_VERIFICATION"
    DATA_COMPLETENESS_AND_CONFORMANCE_CHECKS = "DATA_COMPLETENESS_AND_CONFORMANCE_CHECKS"
    METADATA_TAG_VALIDATION = "METADATA_TAG_VALIDATION"
    IMAGE_QUALITY_AND_PIXEL_DATA_VALIDATION = "IMAGE_QUALITY_AND_PIXEL_DATA_VALIDATION"
    DEIDENTIFICATION = "DEIDENTIFICATION"

# Set metadata after class creation
ImagingDataLifecycleStageEnum._metadata = {
    "DATA_EXTRACTION_AND_METADATA_CHARACTERIZATION": {'description': 'Extraction of imaging data from clinical repositories such as PACS, preceded by a landscape assessment of source locations, database systems, modalities and acquisition devices', 'annotations': {'stage_number': 1}},
    "FILE_INTEGRITY_VERIFICATION": {'description': 'Computation and periodic re-verification of cryptographic checksums such as SHA-256 to detect silent corruption from network errors, media decay or system failure', 'annotations': {'stage_number': 2}},
    "DATA_COMPLETENESS_AND_CONFORMANCE_CHECKS": {'description': 'Detection of structurally invalid DICOM files (truncated, wrong VR encoding, missing required tags) and checks of internal coherence such as identifier uniqueness and demographic consistency across sites', 'annotations': {'stage_number': 3}},
    "METADATA_TAG_VALIDATION": {'description': "Validation of DICOM attributes against the standard's VR, VM and type rules and against biological plausibility, and inventory of private tags", 'annotations': {'stage_number': 4}},
    "IMAGE_QUALITY_AND_PIXEL_DATA_VALIDATION": {'description': 'Verification that pixel data is readable and plausible, that decompression preserves bit depth, and computation of image quality metrics', 'annotations': {'stage_number': 5}},
    "DEIDENTIFICATION": {'description': 'Removal of protected health information from headers and of facial features from pixel data before sharing and reuse', 'meaning': 'NCIT:C45970', 'annotations': {'stage_number': 6}},
}

class ImagingDataSourceTypeEnum(RichEnum):
    """
    Types of systems in a hospital or research network that hold medical imaging data and from which it may be extracted. A landscape assessment records, for each source, the platform vendor, software version, supported query mechanisms, patient identifier handling, retention policy and anonymization capabilities.
    """
    # Enum members
    PACS = "PACS"
    VENDOR_NEUTRAL_ARCHIVE = "VENDOR_NEUTRAL_ARCHIVE"
    DEPARTMENTAL_IMAGING_ARCHIVE = "DEPARTMENTAL_IMAGING_ARCHIVE"
    RESEARCH_IMAGING_PLATFORM = "RESEARCH_IMAGING_PLATFORM"
    MODALITY_WORKSTATION = "MODALITY_WORKSTATION"
    ELECTRONIC_HEALTH_RECORD = "ELECTRONIC_HEALTH_RECORD"
    PUBLIC_IMAGING_REPOSITORY = "PUBLIC_IMAGING_REPOSITORY"
    CLOUD_IMAGING_ARCHIVE = "CLOUD_IMAGING_ARCHIVE"

# Set metadata after class creation
ImagingDataSourceTypeEnum._metadata = {
    "PACS": {'description': 'Clinical system for storing, retrieving and distributing medical images, typically the central radiology archive', 'meaning': 'NCIT:C17624'},
    "VENDOR_NEUTRAL_ARCHIVE": {'description': 'Enterprise archive that stores images from multiple departments and PACS vendors in a standard format', 'aliases': ['VNA']},
    "DEPARTMENTAL_IMAGING_ARCHIVE": {'description': 'Local archive maintained by a clinical department such as cardiology, ophthalmology or endoscopy outside the central PACS'},
    "RESEARCH_IMAGING_PLATFORM": {'description': 'Research-specific imaging informatics database such as XNAT used to manage, store and share imaging data'},
    "MODALITY_WORKSTATION": {'description': 'Acquisition device or attached workstation that exports images through vendor-specific software'},
    "ELECTRONIC_HEALTH_RECORD": {'description': 'Clinical record system that references or embeds imaging studies and provides encounter linkage', 'meaning': 'NCIT:C142529'},
    "PUBLIC_IMAGING_REPOSITORY": {'description': 'Openly accessible imaging data resource such as The Cancer Imaging Archive or OpenNeuro'},
    "CLOUD_IMAGING_ARCHIVE": {'description': 'Cloud-hosted object storage or managed imaging service holding DICOM data'},
}

class DICOMValidationIssueTypeEnum(RichEnum):
    """
    Categories of problems detected when validating DICOM files and collections for completeness, conformance, metadata consistency, pixel data integrity and plausibility. Used to classify findings from tools such as dciodvfy, dcentvfy, DVTk and pydicom during data reliability workflows.
    """
    # Enum members
    TRUNCATED_FILE = "TRUNCATED_FILE"
    INVALID_VR_ENCODING = "INVALID_VR_ENCODING"
    MISSING_REQUIRED_ATTRIBUTE = "MISSING_REQUIRED_ATTRIBUTE"
    VALUE_MULTIPLICITY_VIOLATION = "VALUE_MULTIPLICITY_VIOLATION"
    VALUE_OUT_OF_RANGE = "VALUE_OUT_OF_RANGE"
    INVALID_UID_SYNTAX = "INVALID_UID_SYNTAX"
    DUPLICATE_UID = "DUPLICATE_UID"
    INCONSISTENT_ENTITY_ATTRIBUTES = "INCONSISTENT_ENTITY_ATTRIBUTES"
    DATE_INCONSISTENCY = "DATE_INCONSISTENCY"
    IMPLAUSIBLE_VALUE = "IMPLAUSIBLE_VALUE"
    NONSTANDARD_PRIVATE_ATTRIBUTE = "NONSTANDARD_PRIVATE_ATTRIBUTE"
    IDENTIFIER_LINKAGE_ERROR = "IDENTIFIER_LINKAGE_ERROR"
    UNREADABLE_PIXEL_DATA = "UNREADABLE_PIXEL_DATA"
    DECOMPRESSION_MISMATCH = "DECOMPRESSION_MISMATCH"
    CHECKSUM_MISMATCH = "CHECKSUM_MISMATCH"
    PROTECTED_HEALTH_INFORMATION_PRESENT = "PROTECTED_HEALTH_INFORMATION_PRESENT"

# Set metadata after class creation
DICOMValidationIssueTypeEnum._metadata = {
    "TRUNCATED_FILE": {'description': 'The file is incomplete, for example a truncated transfer syntax or missing pixel data at the end of the file', 'annotations': {'category': 'structural'}},
    "INVALID_VR_ENCODING": {'description': 'An attribute is encoded with a Value Representation that does not match the data dictionary or the transfer syntax', 'annotations': {'category': 'structural'}},
    "MISSING_REQUIRED_ATTRIBUTE": {'description': 'A Type 1 or Type 2 attribute required by the IOD, such as StudyInstanceUID or PixelData, is absent', 'annotations': {'category': 'conformance'}},
    "VALUE_MULTIPLICITY_VIOLATION": {'description': 'An attribute has more or fewer values than permitted by its Value Multiplicity', 'annotations': {'category': 'conformance'}},
    "VALUE_OUT_OF_RANGE": {'description': 'An attribute value is outside the enumerated or defined range allowed by the standard', 'annotations': {'category': 'conformance'}},
    "INVALID_UID_SYNTAX": {'description': 'A UID does not conform to DICOM UID syntax, for example non-numeric components or excess length', 'annotations': {'category': 'conformance'}},
    "DUPLICATE_UID": {'description': 'The same SOP Instance UID or other UID is reused across instances that should be distinct', 'annotations': {'category': 'consistency'}},
    "INCONSISTENT_ENTITY_ATTRIBUTES": {'description': 'Attributes that should be identical across instances of the same entity differ, such as instances in one series carrying different Series Instance UIDs', 'annotations': {'category': 'consistency'}},
    "DATE_INCONSISTENCY": {'description': "Dates are mutually inconsistent, such as a study date after the patient's death date or a series date before the study date", 'annotations': {'category': 'plausibility'}},
    "IMPLAUSIBLE_VALUE": {'description': 'A syntactically valid value that is biologically implausible, such as a patient age of 150 years', 'annotations': {'category': 'plausibility'}},
    "NONSTANDARD_PRIVATE_ATTRIBUTE": {'description': "A private tag is present that is not documented in the site's private tag dictionary", 'annotations': {'category': 'documentation'}},
    "IDENTIFIER_LINKAGE_ERROR": {'description': 'Patient or study identifiers do not link correctly to clinical records, or demographics disagree across linked records', 'annotations': {'category': 'consistency'}},
    "UNREADABLE_PIXEL_DATA": {'description': 'The pixel data cannot be decoded, typically due to acquisition or packaging problems', 'annotations': {'category': 'pixel data'}},
    "DECOMPRESSION_MISMATCH": {'description': 'Decompressed pixel data has an unexpected bit depth or differs from the uncompressed original beyond the expected loss', 'annotations': {'category': 'pixel data'}},
    "CHECKSUM_MISMATCH": {'description': "The file's cryptographic hash no longer matches the value recorded at ingest, indicating corruption or alteration", 'annotations': {'category': 'integrity'}},
    "PROTECTED_HEALTH_INFORMATION_PRESENT": {'description': 'Identifying information remains in the header, private tags or pixel data after de-identification', 'annotations': {'category': 'privacy'}},
}

class ImageQualityMetricEnum(RichEnum):
    """
    Metrics computed during image quality and pixel data validation to document that images are readable and of adequate fidelity for AI applications. Simple metrics can be extended to check conformance with FDA technical performance guidance for quantitative imaging devices where applicable.
    """
    # Enum members
    PIXEL_READABILITY = "PIXEL_READABILITY"
    INTENSITY_HISTOGRAM = "INTENSITY_HISTOGRAM"
    SIGNAL_TO_NOISE_RATIO = "SIGNAL_TO_NOISE_RATIO"
    CONTRAST_TO_NOISE_RATIO = "CONTRAST_TO_NOISE_RATIO"
    SHARPNESS = "SHARPNESS"
    BIT_DEPTH = "BIT_DEPTH"
    PIXEL_SPACING = "PIXEL_SPACING"
    SLICE_THICKNESS = "SLICE_THICKNESS"
    COMPRESSION_FIDELITY = "COMPRESSION_FIDELITY"
    ARTIFACT_PRESENCE = "ARTIFACT_PRESENCE"

# Set metadata after class creation
ImageQualityMetricEnum._metadata = {
    "PIXEL_READABILITY": {'description': 'Whether the pixel array can be decoded without error'},
    "INTENSITY_HISTOGRAM": {'description': 'Distribution of pixel intensities, checked for extreme outliers, clipping or empty images'},
    "SIGNAL_TO_NOISE_RATIO": {'description': 'Ratio of signal in a region of interest to the standard deviation of background noise', 'meaning': 'NCIT:C94983', 'aliases': ['SNR']},
    "CONTRAST_TO_NOISE_RATIO": {'description': 'Difference in signal between two regions relative to background noise', 'aliases': ['CNR']},
    "SHARPNESS": {'description': 'Measure of edge definition or high-frequency content, such as Laplacian variance'},
    "BIT_DEPTH": {'description': 'Number of bits per pixel stored and allocated, checked for consistency after decompression'},
    "PIXEL_SPACING": {'description': 'Physical distance between pixel centres, checked for presence and plausibility'},
    "SLICE_THICKNESS": {'description': 'Nominal thickness of each slice in a volumetric acquisition, checked for presence and plausibility'},
    "COMPRESSION_FIDELITY": {'description': 'Agreement between compressed and original pixel data, for example comparing a JPEG-compressed instance with its uncompressed source'},
    "ARTIFACT_PRESENCE": {'description': 'Detection of motion, metal, aliasing or other acquisition artifacts'},
}

class ImagingInteroperabilityStandardEnum(RichEnum):
    """
    Standards and data models used to represent medical imaging metadata and to link images with clinical records, electronic health records and multimodal research datasets.
    """
    # Enum members
    DICOM = "DICOM"
    DICOMWEB = "DICOMWEB"
    HL7_FHIR_IMAGINGSTUDY = "HL7_FHIR_IMAGINGSTUDY"
    OMOP_CDM_IMAGING_EXTENSION = "OMOP_CDM_IMAGING_EXTENSION"
    IHE_PROFILES = "IHE_PROFILES"
    BIDS = "BIDS"
    NIFTI = "NIFTI"

# Set metadata after class creation
ImagingInteroperabilityStandardEnum._metadata = {
    "DICOM": {'description': 'Digital Imaging and Communications in Medicine (ISO 12052), the standard for storing, transmitting and managing medical imaging data', 'annotations': {'url': 'https://www.dicomstandard.org/'}},
    "DICOMWEB": {'description': 'RESTful web services for DICOM (QIDO-RS, WADO-RS, STOW-RS) defined in DICOM PS3.18', 'annotations': {'url': 'https://www.dicomstandard.org/using/dicomweb'}},
    "HL7_FHIR_IMAGINGSTUDY": {'description': 'FHIR resource representing a DICOM study and its series and instances, used to integrate imaging metadata into FHIR-based systems', 'annotations': {'url': 'https://www.hl7.org/fhir/imagingstudy.html'}},
    "OMOP_CDM_IMAGING_EXTENSION": {'description': 'OHDSI Observational Medical Outcomes Partnership Common Data Model extension for imaging-based observational research, used to link DICOM studies to clinical encounters', 'annotations': {'url': 'https://github.com/OHDSI/OmopImaging'}},
    "IHE_PROFILES": {'description': 'Integrating the Healthcare Enterprise profiles for image sharing and identifier management, such as XDS-I and PIX', 'annotations': {'url': 'https://www.ihe.net/'}},
    "BIDS": {'description': 'Community standard for organizing and describing neuroimaging datasets, commonly used after conversion from DICOM', 'annotations': {'url': 'https://bids.neuroimaging.io/'}},
    "NIFTI": {'description': 'Neuroimaging Informatics Technology Initiative file format for volumetric images, the usual target of DICOM conversion in neuroimaging pipelines', 'annotations': {'url': 'https://nifti.nimh.nih.gov/'}},
}

class Bridge2AIDataGenerationProjectEnum(RichEnum):
    """
    Data generation projects (Grand Challenges) of the NIH Bridge to Artificial Intelligence (Bridge2AI) program, which creates standardized, annotated, ethically sourced AI-ready datasets across a diverse set of modalities.
    """
    # Enum members
    CHORUS = "CHORUS"
    AI_READI = "AI_READI"
    VOICE = "VOICE"
    CM4AI = "CM4AI"

# Set metadata after class creation
Bridge2AIDataGenerationProjectEnum._metadata = {
    "CHORUS": {'description': 'Collaborative Hospital Repository Uniting Standards; the AI/ML for Clinical Care Grand Challenge, linking ICU imaging (MRI, CT, ultrasound, X-ray) with physiologic and clinical data', 'annotations': {'url': 'https://bridge2ai.org/data-chorus/'}, 'aliases': ['Clinical Care']},
    "AI_READI": {'description': 'Artificial Intelligence Ready and Equitable Atlas for Diabetes Insights; the Salutogenesis Grand Challenge, including ophthalmology retinal imaging', 'annotations': {'url': 'https://bridge2ai.org/people-ai-readi/'}, 'aliases': ['Salutogenesis']},
    "VOICE": {'description': 'The Precision Public Health Grand Challenge, connecting voice recordings with laryngoscopy video, brain MRI and CT, and omics data', 'annotations': {'url': 'https://bridge2ai.org/people-voice/'}, 'aliases': ['Precision Public Health']},
    "CM4AI": {'description': 'Cell Maps for Artificial Intelligence; the Functional Genomics Grand Challenge, mapping cellular architecture with imaging and proteomics', 'annotations': {'url': 'https://cm4ai.org/'}, 'aliases': ['Functional Genomics']},
}

__all__ = [
    "ImagingDataLifecycleStageEnum",
    "ImagingDataSourceTypeEnum",
    "DICOMValidationIssueTypeEnum",
    "ImageQualityMetricEnum",
    "ImagingInteroperabilityStandardEnum",
    "Bridge2AIDataGenerationProjectEnum",
]