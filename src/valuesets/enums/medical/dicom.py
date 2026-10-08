"""
DICOM Standard Value Sets

Value sets drawn from the Digital Imaging and Communications in Medicine (DICOM) standard (ISO 12052), the internationally recognized format for storing, transmitting and managing medical imaging data. Covers the acquisition modality codes used in the Modality (0008,0060) attribute, the Value Representations (VRs) that govern attribute encoding, the attribute requirement types (1, 1C, 2, 2C, 3) used in Information Object Definitions, the registered transfer syntaxes that define byte ordering and pixel data compression, the DIMSE and DICOMweb network services used to query and retrieve images from PACS, and the open-source toolkits commonly used to read, validate and serve DICOM files.
These value sets support DICOM data extraction, conformance checking and metadata tag validation, where VR, VM and attribute type rules are checked with tools such as dciodvfy, dcentvfy, DVTk and pydicom.
Codes that come from the DICOM standard itself (modality codes, VRs, action codes) are kept in their standard form rather than being upper-cased or expanded.

Generated from: medical/dicom.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class DICOMModalityEnum(RichEnum):
    """
    Acquisition modality codes from DICOM PS3.16 Context ID 29 (Acquisition Modality), the defined terms for the Modality (0008,0060) attribute. The permissible value is the DICOM code itself; the title is the NCI Thesaurus label where a mapping exists and the DICOM code meaning is carried as an alias when it differs. Where an NCI Thesaurus term exists it is the meaning and the DCM code is an exact mapping; otherwise the DCM code is the meaning, so every value carries its DCM code in one of the two fields. Waveform modalities (ECG, EEG, etc.) are defined in CID 34 and are not included here, nor are the non-acquisition values that also appear in Modality (0008,0060) such as SR, PR, SEG, KO, DOC, OT and the RT objects.
    """
    # Enum members
    AR = "AR"
    BI = "BI"
    BMD = "BMD"
    CR = "CR"
    CT = "CT"
    CFM = "CFM"
    DMS = "DMS"
    DG = "DG"
    DX = "DX"
    ES = "ES"
    XC = "XC"
    GM = "GM"
    IO = "IO"
    IVOCT = "IVOCT"
    IVUS = "IVUS"
    KER = "KER"
    LS = "LS"
    LEN = "LEN"
    MR = "MR"
    MG = "MG"
    NM = "NM"
    OAM = "OAM"
    OPM = "OPM"
    OP = "OP"
    OPT = "OPT"
    OPTBSV = "OPTBSV"
    OPTENF = "OPTENF"
    OPV = "OPV"
    OCT = "OCT"
    OSS = "OSS"
    PX = "PX"
    PA = "PA"
    PT = "PT"
    RF = "RF"
    RG = "RG"
    RTIMAGE = "RTIMAGE"
    SM = "SM"
    SRF = "SRF"
    TG = "TG"
    US = "US"
    BDUS = "BDUS"
    VA = "VA"
    XA = "XA"

# Set metadata after class creation
DICOMModalityEnum._metadata = {
    "AR": {'description': 'Automated measurement of refractive error of the eye', 'meaning': 'NCIT:C176330'},
    "BI": {'description': 'Imaging based on magnetic fields produced by the body, such as magnetoencephalography', 'meaning': 'DCM:BI'},
    "BMD": {'description': 'Measurement of bone mineral content and density, such as DXA', 'meaning': 'NCIT:C190514'},
    "CR": {'description': 'X-ray imaging using a phosphor imaging plate read out to a digital image', 'meaning': 'NCIT:C190521'},
    "CT": {'description': 'Cross-sectional X-ray imaging reconstructed by computer', 'meaning': 'NCIT:C17204'},
    "CFM": {'description': 'Laser-scanning microscopy that rejects out-of-focus light', 'meaning': 'NCIT:C17753'},
    "DMS": {'description': 'Non-invasive microscopic examination of the skin surface', 'meaning': 'NCIT:C116478'},
    "DG": {'description': 'Transillumination imaging of tissue, historically used for the breast', 'meaning': 'DCM:DG'},
    "DX": {'description': 'Projection X-ray imaging acquired directly with a digital detector', 'meaning': 'NCIT:C18001'},
    "ES": {'description': 'Imaging from an endoscope inserted into a body cavity or organ, including laryngoscopy and video endoscopy', 'meaning': 'NCIT:C16546', 'aliases': ['Endoscopy']},
    "XC": {'description': 'Visible-light photography of the patient with an external camera', 'meaning': 'DCM:XC'},
    "GM": {'description': 'General microscopy not otherwise classified', 'meaning': 'NCIT:C16853', 'aliases': ['General Microscopy']},
    "IO": {'description': 'Dental X-ray imaging with the detector inside the mouth', 'meaning': 'NCIT:C190548', 'aliases': ['Intra-oral Radiography']},
    "IVOCT": {'description': 'Catheter-based optical coherence tomography of blood vessels', 'meaning': 'NCIT:C190550'},
    "IVUS": {'description': 'Catheter-based ultrasound imaging of blood vessels', 'meaning': 'NCIT:C99535'},
    "KER": {'description': 'Measurement of the curvature of the anterior corneal surface', 'meaning': 'NCIT:C190551'},
    "LS": {'description': 'Surface geometry acquired with a laser scanner', 'meaning': 'DCM:LS'},
    "LEN": {'description': 'Measurement of the optical properties of spectacle lenses', 'meaning': 'DCM:LEN'},
    "MR": {'description': 'Imaging using radiofrequency pulses in a strong magnetic field', 'meaning': 'NCIT:C16809', 'aliases': ['Magnetic Resonance']},
    "MG": {'description': 'Low-dose X-ray imaging of the breast', 'meaning': 'NCIT:C16818'},
    "NM": {'description': 'Gamma camera imaging of an administered radiotracer, including planar and SPECT', 'meaning': 'NCIT:C62667', 'aliases': ['Nuclear Medicine']},
    "OAM": {'description': 'Measurement of axial dimensions of the eye, such as axial length', 'meaning': 'DCM:OAM'},
    "OPM": {'description': 'Topographic or thickness maps of ocular structures', 'meaning': 'DCM:OPM'},
    "OP": {'description': 'Photography of the eye, including fundus and slit lamp photography', 'meaning': 'NCIT:C190559'},
    "OPT": {'description': 'Optical coherence tomography of the eye, including retinal OCT B-scans', 'meaning': 'NCIT:C190561'},
    "OPTBSV": {'description': 'Volume analysis derived from ophthalmic OCT B-scans', 'meaning': 'DCM:OPTBSV'},
    "OPTENF": {'description': 'Transverse (en face) images derived from ophthalmic OCT volumes', 'meaning': 'NCIT:C190563', 'aliases': ['Ophthalmic Tomography En Face']},
    "OPV": {'description': 'Perimetry results describing the visual field', 'meaning': 'DCM:OPV'},
    "OCT": {'description': 'Interferometric imaging using near-infrared light, used outside ophthalmology', 'meaning': 'NCIT:C20828'},
    "OSS": {'description': 'Surface geometry acquired with an optical (non-laser) scanner', 'meaning': 'DCM:OSS'},
    "PX": {'description': 'Dental panoramic radiography of the jaws', 'meaning': 'DCM:PX'},
    "PA": {'description': 'Imaging of ultrasonic waves generated by optical absorption of pulsed light', 'meaning': 'NCIT:C116749', 'aliases': ['Photoacoustic']},
    "PT": {'description': 'Tomographic imaging of a positron-emitting radiotracer', 'meaning': 'NCIT:C17007'},
    "RF": {'description': 'Real-time X-ray imaging, including radiofluoroscopy', 'meaning': 'NCIT:C16588', 'aliases': ['Radiofluoroscopy']},
    "RG": {'description': 'Conventional film or screen radiographic imaging', 'meaning': 'NCIT:C38101', 'aliases': ['Radiographic imaging']},
    "RTIMAGE": {'description': 'Radiotherapy portal or setup image', 'meaning': 'DCM:RTIMAGE'},
    "SM": {'description': 'Whole slide imaging of microscope slides', 'meaning': 'DCM:SM'},
    "SRF": {'description': 'Refraction measured with patient feedback', 'meaning': 'DCM:SRF'},
    "TG": {'description': 'Imaging of body surface temperature', 'meaning': 'NCIT:C17194'},
    "US": {'description': 'Imaging using high-frequency sound waves, including static images and cine loops', 'meaning': 'NCIT:C17230', 'aliases': ['Ultrasound']},
    "BDUS": {'description': 'Quantitative ultrasound estimation of bone mineral density', 'meaning': 'NCIT:C190516'},
    "VA": {'description': 'Measurement of the sharpness of vision', 'meaning': 'NCIT:C87149'},
    "XA": {'description': 'X-ray imaging of blood vessels with contrast, including digital subtraction angiography', 'meaning': 'NCIT:C20080'},
}

class DICOMValueRepresentationEnum(RichEnum):
    """
    The Value Representations (VRs) defined in DICOM PS3.5 Section 6.2, which specify the data type and format of the value of a data element. Tag validation tools check that each attribute is encoded with the VR required by the data dictionary. Permissible values are the two-letter DICOM VR codes.
    """
    # Enum members
    AE = "AE"
    AS = "AS"
    AT = "AT"
    CS = "CS"
    DA = "DA"
    DS = "DS"
    DT = "DT"
    FL = "FL"
    FD = "FD"
    IS = "IS"
    LO = "LO"
    LT = "LT"
    OB = "OB"
    OD = "OD"
    OF = "OF"
    OL = "OL"
    OV = "OV"
    OW = "OW"
    PN = "PN"
    SH = "SH"
    SL = "SL"
    SQ = "SQ"
    SS = "SS"
    ST = "ST"
    SV = "SV"
    TM = "TM"
    UC = "UC"
    UI = "UI"
    UL = "UL"
    UN = "UN"
    UR = "UR"
    US = "US"
    UT = "UT"
    UV = "UV"

# Set metadata after class creation
DICOMValueRepresentationEnum._metadata = {
    "AE": {'description': 'A string identifying an Application Entity; 16 bytes maximum', 'annotations': {'category': 'string'}},
    "AS": {'description': 'Age in the format nnnD, nnnW, nnnM or nnnY (days, weeks, months, years)', 'annotations': {'category': 'string'}},
    "AT": {'description': 'An ordered pair of 16-bit unsigned integers that is the value of a data element tag', 'annotations': {'category': 'binary'}},
    "CS": {'description': 'A string identifying a controlled concept; uppercase letters, digits, space and underscore, 16 bytes maximum', 'annotations': {'category': 'string'}},
    "DA": {'description': 'A date in the format YYYYMMDD', 'annotations': {'category': 'date_time'}},
    "DS": {'description': 'A string representing a fixed point or floating point number', 'annotations': {'category': 'string'}},
    "DT": {'description': 'A concatenated date-time string of the form YYYYMMDDHHMMSS.FFFFFF&ZZXX', 'annotations': {'category': 'date_time'}},
    "FL": {'description': 'Single precision IEEE 754 binary32 floating point value', 'annotations': {'category': 'binary'}},
    "FD": {'description': 'Double precision IEEE 754 binary64 floating point value', 'annotations': {'category': 'binary'}},
    "IS": {'description': 'A string representing a base-10 integer', 'annotations': {'category': 'string'}},
    "LO": {'description': 'A character string of up to 64 characters', 'annotations': {'category': 'string'}},
    "LT": {'description': 'A character string that may contain one or more paragraphs, up to 10240 characters', 'annotations': {'category': 'text'}},
    "OB": {'description': 'An octet stream whose encoding is specified by the negotiated transfer syntax', 'annotations': {'category': 'binary'}},
    "OD": {'description': 'A stream of IEEE 754 binary64 values', 'annotations': {'category': 'binary'}},
    "OF": {'description': 'A stream of IEEE 754 binary32 values', 'annotations': {'category': 'binary'}},
    "OL": {'description': 'A stream of 32-bit words', 'annotations': {'category': 'binary'}},
    "OV": {'description': 'A stream of 64-bit words', 'annotations': {'category': 'binary'}},
    "OW": {'description': 'A stream of 16-bit words; commonly used for Pixel Data', 'annotations': {'category': 'binary'}},
    "PN": {'description': 'A character string encoded using a five-component convention (family, given, middle, prefix, suffix)', 'annotations': {'category': 'string'}},
    "SH": {'description': 'A character string of up to 16 characters', 'annotations': {'category': 'string'}},
    "SL": {'description': "Signed 32-bit two's complement integer", 'annotations': {'category': 'binary'}},
    "SQ": {'description': 'A sequence of zero or more items, each of which is a nested data set', 'annotations': {'category': 'sequence'}},
    "SS": {'description': "Signed 16-bit two's complement integer", 'annotations': {'category': 'binary'}},
    "ST": {'description': 'A character string that may contain one or more paragraphs, up to 1024 characters', 'annotations': {'category': 'text'}},
    "SV": {'description': 'Signed 64-bit integer', 'annotations': {'category': 'binary'}},
    "TM": {'description': 'A time in the format HHMMSS.FFFFFF', 'annotations': {'category': 'date_time'}},
    "UC": {'description': 'A character string of unlimited length', 'annotations': {'category': 'string'}},
    "UI": {'description': 'A string of numeric components separated by periods, up to 64 characters, used for UIDs such as SOP Instance UIDs and transfer syntax UIDs', 'annotations': {'category': 'string'}},
    "UL": {'description': 'Unsigned 32-bit integer', 'annotations': {'category': 'binary'}},
    "UN": {'description': 'An octet stream whose encoding of the contents is unknown', 'annotations': {'category': 'binary'}},
    "UR": {'description': 'A string identifying a URI or URL as defined in RFC 3986', 'annotations': {'category': 'string'}},
    "US": {'description': 'Unsigned 16-bit integer', 'annotations': {'category': 'binary'}},
    "UT": {'description': 'A character string that may contain one or more paragraphs, of unlimited length', 'annotations': {'category': 'text'}},
    "UV": {'description': 'Unsigned 64-bit integer', 'annotations': {'category': 'binary'}},
}

class DICOMAttributeTypeEnum(RichEnum):
    """
    Attribute requirement types defined in DICOM PS3.5 Section 7.4, which state whether an attribute must be present in a data set and whether it may have a zero-length value. Conformance checkers report missing Type 1 and Type 2 attributes as errors. These types also determine which de-identification action (D, Z or X) may be applied to an attribute.
    """
    # Enum members
    TYPE_1 = "TYPE_1"
    TYPE_1C = "TYPE_1C"
    TYPE_2 = "TYPE_2"
    TYPE_2C = "TYPE_2C"
    TYPE_3 = "TYPE_3"

# Set metadata after class creation
DICOMAttributeTypeEnum._metadata = {
    "TYPE_1": {'description': 'The attribute shall be present with a valid non-zero-length value', 'aliases': ['1']},
    "TYPE_1C": {'description': 'The attribute shall be present with a valid value when a specified condition is met, and shall not be present otherwise', 'aliases': ['1C']},
    "TYPE_2": {'description': 'The attribute shall be present but may have a zero-length value if the value is unknown', 'aliases': ['2']},
    "TYPE_2C": {'description': 'The attribute shall be present, possibly with zero length, when a specified condition is met', 'aliases': ['2C']},
    "TYPE_3": {'description': 'The attribute is optional and may be absent or present with or without a value', 'aliases': ['3']},
}

class DICOMTransferSyntaxEnum(RichEnum):
    """
    Transfer syntaxes registered in DICOM PS3.6 Annex A that define the byte ordering, VR encoding and pixel data compression of a DICOM data set. Pixel data validation includes confirming that decompression from a lossy or lossless transfer syntax yields the expected bit depth and that no unintended data loss occurred. Video transfer syntaxes (MPEG-2, H.264, HEVC) are used for endoscopy and ultrasound cine acquisitions. Fragmentable variants of the MPEG transfer syntaxes and retired JPEG processes are omitted; the full registry is at the see_also link.
    """
    # Enum members
    IMPLICIT_VR_LITTLE_ENDIAN = "IMPLICIT_VR_LITTLE_ENDIAN"
    EXPLICIT_VR_LITTLE_ENDIAN = "EXPLICIT_VR_LITTLE_ENDIAN"
    ENCAPSULATED_UNCOMPRESSED_EXPLICIT_VR_LITTLE_ENDIAN = "ENCAPSULATED_UNCOMPRESSED_EXPLICIT_VR_LITTLE_ENDIAN"
    DEFLATED_EXPLICIT_VR_LITTLE_ENDIAN = "DEFLATED_EXPLICIT_VR_LITTLE_ENDIAN"
    EXPLICIT_VR_BIG_ENDIAN = "EXPLICIT_VR_BIG_ENDIAN"
    JPEG_BASELINE_PROCESS_1 = "JPEG_BASELINE_PROCESS_1"
    JPEG_EXTENDED_PROCESS_2_4 = "JPEG_EXTENDED_PROCESS_2_4"
    JPEG_LOSSLESS_PROCESS_14 = "JPEG_LOSSLESS_PROCESS_14"
    JPEG_LOSSLESS_PROCESS_14_SV1 = "JPEG_LOSSLESS_PROCESS_14_SV1"
    JPEG_LS_LOSSLESS = "JPEG_LS_LOSSLESS"
    JPEG_LS_NEAR_LOSSLESS = "JPEG_LS_NEAR_LOSSLESS"
    JPEG_2000_LOSSLESS_ONLY = "JPEG_2000_LOSSLESS_ONLY"
    JPEG_2000 = "JPEG_2000"
    JPEG_2000_MULTICOMPONENT_LOSSLESS_ONLY = "JPEG_2000_MULTICOMPONENT_LOSSLESS_ONLY"
    JPEG_2000_MULTICOMPONENT = "JPEG_2000_MULTICOMPONENT"
    JPIP_REFERENCED = "JPIP_REFERENCED"
    JPIP_REFERENCED_DEFLATE = "JPIP_REFERENCED_DEFLATE"
    MPEG2_MAIN_PROFILE_MAIN_LEVEL = "MPEG2_MAIN_PROFILE_MAIN_LEVEL"
    MPEG2_MAIN_PROFILE_HIGH_LEVEL = "MPEG2_MAIN_PROFILE_HIGH_LEVEL"
    MPEG4_AVC_H264_HIGH_PROFILE_LEVEL_4_1 = "MPEG4_AVC_H264_HIGH_PROFILE_LEVEL_4_1"
    MPEG4_AVC_H264_BD_COMPATIBLE_HIGH_PROFILE_LEVEL_4_1 = "MPEG4_AVC_H264_BD_COMPATIBLE_HIGH_PROFILE_LEVEL_4_1"
    MPEG4_AVC_H264_HIGH_PROFILE_LEVEL_4_2_2D = "MPEG4_AVC_H264_HIGH_PROFILE_LEVEL_4_2_2D"
    MPEG4_AVC_H264_HIGH_PROFILE_LEVEL_4_2_3D = "MPEG4_AVC_H264_HIGH_PROFILE_LEVEL_4_2_3D"
    MPEG4_AVC_H264_STEREO_HIGH_PROFILE_LEVEL_4_2 = "MPEG4_AVC_H264_STEREO_HIGH_PROFILE_LEVEL_4_2"
    HEVC_H265_MAIN_PROFILE_LEVEL_5_1 = "HEVC_H265_MAIN_PROFILE_LEVEL_5_1"
    HEVC_H265_MAIN_10_PROFILE_LEVEL_5_1 = "HEVC_H265_MAIN_10_PROFILE_LEVEL_5_1"
    JPEG_XL_LOSSLESS = "JPEG_XL_LOSSLESS"
    JPEG_XL_JPEG_RECOMPRESSION = "JPEG_XL_JPEG_RECOMPRESSION"
    JPEG_XL = "JPEG_XL"
    HTJ2K_LOSSLESS_ONLY = "HTJ2K_LOSSLESS_ONLY"
    HTJ2K_RPCL_LOSSLESS_ONLY = "HTJ2K_RPCL_LOSSLESS_ONLY"
    HTJ2K = "HTJ2K"
    RLE_LOSSLESS = "RLE_LOSSLESS"
    SMPTE_ST_2110_20_UNCOMPRESSED_PROGRESSIVE_VIDEO = "SMPTE_ST_2110_20_UNCOMPRESSED_PROGRESSIVE_VIDEO"
    SMPTE_ST_2110_20_UNCOMPRESSED_INTERLACED_VIDEO = "SMPTE_ST_2110_20_UNCOMPRESSED_INTERLACED_VIDEO"

# Set metadata after class creation
DICOMTransferSyntaxEnum._metadata = {
    "IMPLICIT_VR_LITTLE_ENDIAN": {'description': 'Default transfer syntax for DICOM; VRs are looked up from the data dictionary rather than encoded', 'annotations': {'uid': '1.2.840.10008.1.2', 'compression': 'none'}},
    "EXPLICIT_VR_LITTLE_ENDIAN": {'description': 'Uncompressed encoding with VRs explicitly encoded in each data element', 'annotations': {'uid': '1.2.840.10008.1.2.1', 'compression': 'none'}},
    "ENCAPSULATED_UNCOMPRESSED_EXPLICIT_VR_LITTLE_ENDIAN": {'description': 'Uncompressed pixel data encapsulated in fragments, one per frame', 'annotations': {'uid': '1.2.840.10008.1.2.1.98', 'compression': 'none'}},
    "DEFLATED_EXPLICIT_VR_LITTLE_ENDIAN": {'description': 'Explicit VR Little Endian data set compressed as a whole with the deflate algorithm', 'annotations': {'uid': '1.2.840.10008.1.2.1.99', 'compression': 'lossless'}},
    "EXPLICIT_VR_BIG_ENDIAN": {'description': 'Big endian byte ordering with explicit VRs; retired but still encountered in legacy archives', 'annotations': {'uid': '1.2.840.10008.1.2.2', 'compression': 'none', 'retired': 'true'}},
    "JPEG_BASELINE_PROCESS_1": {'description': 'Default transfer syntax for lossy JPEG 8-bit image compression', 'annotations': {'uid': '1.2.840.10008.1.2.4.50', 'compression': 'lossy'}},
    "JPEG_EXTENDED_PROCESS_2_4": {'description': 'Default transfer syntax for lossy JPEG 12-bit image compression (Process 4 only)', 'annotations': {'uid': '1.2.840.10008.1.2.4.51', 'compression': 'lossy'}},
    "JPEG_LOSSLESS_PROCESS_14": {'description': 'Lossless JPEG compression using any predictor', 'annotations': {'uid': '1.2.840.10008.1.2.4.57', 'compression': 'lossless'}},
    "JPEG_LOSSLESS_PROCESS_14_SV1": {'description': 'Default transfer syntax for lossless JPEG image compression', 'annotations': {'uid': '1.2.840.10008.1.2.4.70', 'compression': 'lossless'}},
    "JPEG_LS_LOSSLESS": {'description': 'Lossless compression using the JPEG-LS (ISO 14495) algorithm', 'annotations': {'uid': '1.2.840.10008.1.2.4.80', 'compression': 'lossless'}},
    "JPEG_LS_NEAR_LOSSLESS": {'description': 'Near-lossless JPEG-LS compression with a bounded per-pixel error', 'annotations': {'uid': '1.2.840.10008.1.2.4.81', 'compression': 'lossy'}},
    "JPEG_2000_LOSSLESS_ONLY": {'description': 'JPEG 2000 wavelet compression restricted to reversible (lossless) mode', 'annotations': {'uid': '1.2.840.10008.1.2.4.90', 'compression': 'lossless'}},
    "JPEG_2000": {'description': 'JPEG 2000 wavelet compression, lossy or lossless', 'annotations': {'uid': '1.2.840.10008.1.2.4.91', 'compression': 'lossy or lossless'}},
    "JPEG_2000_MULTICOMPONENT_LOSSLESS_ONLY": {'description': 'JPEG 2000 Part 2 multi-component transform, reversible mode only', 'annotations': {'uid': '1.2.840.10008.1.2.4.92', 'compression': 'lossless'}},
    "JPEG_2000_MULTICOMPONENT": {'description': 'JPEG 2000 Part 2 multi-component transform, lossy or lossless', 'annotations': {'uid': '1.2.840.10008.1.2.4.93', 'compression': 'lossy or lossless'}},
    "JPIP_REFERENCED": {'description': 'Pixel data referenced via a JPEG 2000 Interactive Protocol URL rather than encoded in the data set', 'annotations': {'uid': '1.2.840.10008.1.2.4.94', 'compression': 'referenced'}},
    "JPIP_REFERENCED_DEFLATE": {'description': 'JPIP referenced pixel data with the remaining data set deflated', 'annotations': {'uid': '1.2.840.10008.1.2.4.95', 'compression': 'referenced'}},
    "MPEG2_MAIN_PROFILE_MAIN_LEVEL": {'description': 'MPEG-2 video compression for standard definition video', 'annotations': {'uid': '1.2.840.10008.1.2.4.100', 'compression': 'lossy', 'media': 'video'}},
    "MPEG2_MAIN_PROFILE_HIGH_LEVEL": {'description': 'MPEG-2 video compression for high definition video', 'annotations': {'uid': '1.2.840.10008.1.2.4.101', 'compression': 'lossy', 'media': 'video'}},
    "MPEG4_AVC_H264_HIGH_PROFILE_LEVEL_4_1": {'description': 'H.264 video compression for high definition video', 'annotations': {'uid': '1.2.840.10008.1.2.4.102', 'compression': 'lossy', 'media': 'video'}},
    "MPEG4_AVC_H264_BD_COMPATIBLE_HIGH_PROFILE_LEVEL_4_1": {'description': 'H.264 video compression constrained for Blu-ray Disc compatibility', 'annotations': {'uid': '1.2.840.10008.1.2.4.103', 'compression': 'lossy', 'media': 'video'}},
    "MPEG4_AVC_H264_HIGH_PROFILE_LEVEL_4_2_2D": {'description': 'H.264 video compression for 2D video at higher frame rates and resolutions', 'annotations': {'uid': '1.2.840.10008.1.2.4.104', 'compression': 'lossy', 'media': 'video'}},
    "MPEG4_AVC_H264_HIGH_PROFILE_LEVEL_4_2_3D": {'description': 'H.264 video compression for 3D (stereoscopic) video', 'annotations': {'uid': '1.2.840.10008.1.2.4.105', 'compression': 'lossy', 'media': 'video'}},
    "MPEG4_AVC_H264_STEREO_HIGH_PROFILE_LEVEL_4_2": {'description': 'H.264 stereo high profile for stereoscopic video', 'annotations': {'uid': '1.2.840.10008.1.2.4.106', 'compression': 'lossy', 'media': 'video'}},
    "HEVC_H265_MAIN_PROFILE_LEVEL_5_1": {'description': 'HEVC video compression with 8-bit samples', 'annotations': {'uid': '1.2.840.10008.1.2.4.107', 'compression': 'lossy', 'media': 'video'}},
    "HEVC_H265_MAIN_10_PROFILE_LEVEL_5_1": {'description': 'HEVC video compression with 10-bit samples', 'annotations': {'uid': '1.2.840.10008.1.2.4.108', 'compression': 'lossy', 'media': 'video'}},
    "JPEG_XL_LOSSLESS": {'description': 'JPEG XL compression restricted to lossless mode', 'annotations': {'uid': '1.2.840.10008.1.2.4.110', 'compression': 'lossless'}},
    "JPEG_XL_JPEG_RECOMPRESSION": {'description': 'Lossless recompression of existing JPEG codestreams using JPEG XL', 'annotations': {'uid': '1.2.840.10008.1.2.4.111', 'compression': 'lossless'}},
    "JPEG_XL": {'description': 'JPEG XL compression, lossy or lossless', 'annotations': {'uid': '1.2.840.10008.1.2.4.112', 'compression': 'lossy or lossless'}},
    "HTJ2K_LOSSLESS_ONLY": {'description': 'High-throughput JPEG 2000 (Part 15) restricted to lossless mode', 'annotations': {'uid': '1.2.840.10008.1.2.4.201', 'compression': 'lossless'}},
    "HTJ2K_RPCL_LOSSLESS_ONLY": {'description': 'Lossless high-throughput JPEG 2000 with resolution-position-component-layer progression for progressive decoding', 'annotations': {'uid': '1.2.840.10008.1.2.4.202', 'compression': 'lossless'}},
    "HTJ2K": {'description': 'High-throughput JPEG 2000, lossy or lossless', 'annotations': {'uid': '1.2.840.10008.1.2.4.203', 'compression': 'lossy or lossless'}},
    "RLE_LOSSLESS": {'description': 'Run-length encoded lossless compression, widely used for ultrasound', 'annotations': {'uid': '1.2.840.10008.1.2.5', 'compression': 'lossless'}},
    "SMPTE_ST_2110_20_UNCOMPRESSED_PROGRESSIVE_VIDEO": {'description': 'Uncompressed progressive video streamed per SMPTE ST 2110-20, used in real-time video communication', 'annotations': {'uid': '1.2.840.10008.1.2.7.1', 'compression': 'none', 'media': 'video'}},
    "SMPTE_ST_2110_20_UNCOMPRESSED_INTERLACED_VIDEO": {'description': 'Uncompressed interlaced video streamed per SMPTE ST 2110-20', 'annotations': {'uid': '1.2.840.10008.1.2.7.2', 'compression': 'none', 'media': 'video'}},
}

class DICOMNetworkServiceEnum(RichEnum):
    """
    Network services used to query, retrieve and store DICOM instances between imaging systems such as PACS, modalities and research archives. Includes the classic DIMSE (DICOM Message Service Element) services of PS3.7 and the RESTful DICOMweb services of PS3.18. Cataloguing which services a source repository supports is part of the data landscape assessment that precedes extraction.
    """
    # Enum members
    C_ECHO = "C_ECHO"
    C_STORE = "C_STORE"
    C_FIND = "C_FIND"
    C_MOVE = "C_MOVE"
    C_GET = "C_GET"
    N_EVENT_REPORT = "N_EVENT_REPORT"
    N_GET = "N_GET"
    N_SET = "N_SET"
    N_ACTION = "N_ACTION"
    N_CREATE = "N_CREATE"
    N_DELETE = "N_DELETE"
    QIDO_RS = "QIDO_RS"
    WADO_RS = "WADO_RS"
    STOW_RS = "STOW_RS"
    WADO_URI = "WADO_URI"
    UPS_RS = "UPS_RS"
    CUSTOM_API = "CUSTOM_API"

# Set metadata after class creation
DICOMNetworkServiceEnum._metadata = {
    "C_ECHO": {'description': 'DIMSE verification service used to test connectivity between two application entities', 'annotations': {'protocol': 'DIMSE'}},
    "C_STORE": {'description': 'DIMSE storage service that pushes a composite instance to a peer', 'annotations': {'protocol': 'DIMSE'}},
    "C_FIND": {'description': "DIMSE query service that matches attributes against a peer's database at patient, study, series or instance level", 'annotations': {'protocol': 'DIMSE'}},
    "C_MOVE": {'description': 'DIMSE retrieve service that instructs a peer to send matching instances to a named destination via C-STORE', 'annotations': {'protocol': 'DIMSE'}},
    "C_GET": {'description': 'DIMSE retrieve service that returns matching instances on the same association', 'annotations': {'protocol': 'DIMSE'}},
    "N_EVENT_REPORT": {'description': 'DIMSE-N notification service used to report events on a normalized SOP instance', 'annotations': {'protocol': 'DIMSE'}},
    "N_GET": {'description': 'DIMSE-N service that retrieves attribute values of a normalized SOP instance', 'annotations': {'protocol': 'DIMSE'}},
    "N_SET": {'description': 'DIMSE-N service that modifies attribute values of a normalized SOP instance', 'annotations': {'protocol': 'DIMSE'}},
    "N_ACTION": {'description': 'DIMSE-N service that requests an action on a normalized SOP instance, such as storage commitment', 'annotations': {'protocol': 'DIMSE'}},
    "N_CREATE": {'description': 'DIMSE-N service that creates a normalized SOP instance', 'annotations': {'protocol': 'DIMSE'}},
    "N_DELETE": {'description': 'DIMSE-N service that deletes a normalized SOP instance', 'annotations': {'protocol': 'DIMSE'}},
    "QIDO_RS": {'description': 'DICOMweb RESTful query service (Query based on ID for DICOM Objects) for searching studies, series and instances', 'annotations': {'protocol': 'DICOMweb'}},
    "WADO_RS": {'description': 'DICOMweb RESTful retrieve service (Web Access to DICOM Objects) for retrieving studies, series, instances, frames, metadata and rendered images', 'annotations': {'protocol': 'DICOMweb'}},
    "STOW_RS": {'description': 'DICOMweb RESTful store service (Store Over the Web) for uploading instances', 'annotations': {'protocol': 'DICOMweb'}},
    "WADO_URI": {'description': 'Legacy DICOMweb URI-based retrieve service for single instances', 'annotations': {'protocol': 'DICOMweb'}},
    "UPS_RS": {'description': 'DICOMweb RESTful worklist service for Unified Procedure Step management', 'annotations': {'protocol': 'DICOMweb'}},
    "CUSTOM_API": {'description': 'A vendor- or institution-specific interface that is not a standard DICOM network service'},
}

class DICOMSoftwareToolEnum(RichEnum):
    """
    Software toolkits, libraries, validators, servers and platforms commonly used to read, write, validate, anonymize and serve DICOM data in research data management pipelines. The category annotation distinguishes general-purpose toolkits from conformance validators, archive servers and metadata anonymizers.
    """
    # Enum members
    DCMTK = "DCMTK"
    PYDICOM = "PYDICOM"
    GDCM = "GDCM"
    DCM4CHE = "DCM4CHE"
    ITK = "ITK"
    DVTK = "DVTK"
    DICOM3TOOLS = "DICOM3TOOLS"
    DCIODVFY = "DCIODVFY"
    DCENTVFY = "DCENTVFY"
    PIXELMED = "PIXELMED"
    RSNA_CTP = "RSNA_CTP"
    ORTHANC = "ORTHANC"
    DCM4CHEE = "DCM4CHEE"
    XNAT = "XNAT"
    TCIA_UTILS = "TCIA_UTILS"
    DICOM_CLEANER = "DICOM_CLEANER"
    HOROS = "HOROS"
    OSIRIX = "OSIRIX"
    SLICER_3D = "SLICER_3D"
    ITK_SNAP = "ITK_SNAP"

# Set metadata after class creation
DICOMSoftwareToolEnum._metadata = {
    "DCMTK": {'description': 'OFFIS DICOM Toolkit; C/C++ libraries and command-line utilities implementing DICOM network services and file handling', 'annotations': {'category': 'toolkit', 'language': 'C++', 'license': 'BSD', 'url': 'https://dicom.offis.de/en/dcmtk/'}},
    "PYDICOM": {'description': 'Pure Python library for reading, modifying and writing DICOM files, including pixel data access', 'annotations': {'category': 'toolkit', 'language': 'Python', 'license': 'MIT', 'url': 'https://github.com/pydicom/pydicom'}},
    "GDCM": {'description': 'Grassroots DICOM; C++ library with Python and other bindings for DICOM file and image codec handling', 'annotations': {'category': 'toolkit', 'language': 'C++', 'license': 'BSD', 'url': 'https://sourceforge.net/projects/gdcm/'}},
    "DCM4CHE": {'description': 'Java DICOM toolkit and the basis of the dcm4chee archive', 'annotations': {'category': 'toolkit', 'language': 'Java', 'license': 'MPL/GPL/LGPL', 'url': 'https://www.dcm4che.org/'}},
    "ITK": {'description': 'Insight Toolkit; C++ image processing library with DICOM readers built on GDCM', 'annotations': {'category': 'toolkit', 'language': 'C++', 'license': 'Apache-2.0', 'url': 'https://itk.org/'}},
    "DVTK": {'description': 'DICOM Validation Toolkit; validates object conformance and network behaviour against the standard', 'annotations': {'category': 'validator', 'language': 'C#', 'license': 'LGPL', 'url': 'https://www.dvtk.org/'}},
    "DICOM3TOOLS": {'description': "David Clunie's command-line utilities for creating, modifying, dumping and validating DICOM files", 'annotations': {'category': 'validator', 'language': 'C++', 'license': 'BSD', 'url': 'http://www.dclunie.com/dicom3tools.html'}},
    "DCIODVFY": {'description': 'dicom3tools utility that verifies a file against the Information Object Definition for its modality, reporting missing required attributes, incorrect VRs and values outside allowed ranges', 'annotations': {'category': 'validator', 'part_of': 'dicom3tools'}},
    "DCENTVFY": {'description': 'dicom3tools utility that checks consistency of entity-level attributes across multiple files, such as all instances in a series sharing the same Series Instance UID', 'annotations': {'category': 'validator', 'part_of': 'dicom3tools'}},
    "PIXELMED": {'description': 'PixelMed Java DICOM toolkit, including the DicomCleaner metadata anonymizer', 'annotations': {'category': 'toolkit', 'language': 'Java', 'license': 'BSD', 'url': 'https://www.pixelmed.com/'}},
    "RSNA_CTP": {'description': 'RSNA Clinical Trial Processor; pipeline application with a configurable DICOM anonymizer', 'annotations': {'category': 'anonymizer', 'language': 'Java', 'url': 'https://mircwiki.rsna.org/index.php?title=CTP-The_RSNA_Clinical_Trial_Processor'}},
    "ORTHANC": {'description': 'Lightweight open-source DICOM server with a REST API and DICOMweb plugin', 'annotations': {'category': 'server', 'language': 'C++', 'license': 'GPL-3.0', 'url': 'https://www.orthanc-server.com/'}},
    "DCM4CHEE": {'description': 'Open-source DICOM archive and image manager built on dcm4che', 'annotations': {'category': 'server', 'language': 'Java', 'url': 'https://www.dcm4che.org/'}},
    "XNAT": {'description': 'Extensible Neuroimaging Archive Toolkit; open-source imaging informatics platform for managing, storing and sharing imaging data', 'annotations': {'category': 'platform', 'language': 'Java', 'license': 'BSD', 'url': 'https://www.xnat.org/'}},
    "TCIA_UTILS": {'description': 'Python utilities from The Cancer Imaging Archive for querying, downloading and inventorying DICOM metadata', 'annotations': {'category': 'toolkit', 'language': 'Python', 'url': 'https://github.com/kirbyju/tcia_utils'}},
    "DICOM_CLEANER": {'description': 'PixelMed graphical tool for metadata de-identification and blackout of burned-in text', 'annotations': {'category': 'anonymizer', 'language': 'Java', 'part_of': 'PixelMed'}},
    "HOROS": {'description': 'Open-source macOS DICOM viewer forked from OsiriX with built-in anonymization', 'annotations': {'category': 'viewer', 'license': 'LGPL-3.0', 'url': 'https://horosproject.org/'}},
    "OSIRIX": {'description': 'Commercial macOS DICOM viewer and workstation', 'annotations': {'category': 'viewer', 'license': 'commercial', 'url': 'https://www.osirix-viewer.com/'}},
    "SLICER_3D": {'description': 'Open-source platform for medical image visualization, segmentation and analysis with DICOM import', 'annotations': {'category': 'viewer', 'license': 'BSD-style', 'url': 'https://www.slicer.org/'}},
    "ITK_SNAP": {'description': 'Open-source tool for manual and semi-automatic segmentation of 3D medical images', 'annotations': {'category': 'viewer', 'license': 'GPL', 'url': 'http://www.itksnap.org/'}},
}

__all__ = [
    "DICOMModalityEnum",
    "DICOMValueRepresentationEnum",
    "DICOMAttributeTypeEnum",
    "DICOMTransferSyntaxEnum",
    "DICOMNetworkServiceEnum",
    "DICOMSoftwareToolEnum",
]