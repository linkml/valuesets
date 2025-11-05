"""
Croissant ML Value Sets

Value sets for the Croissant ML metadata format for machine learning datasets.

Croissant is a standardized metadata format developed by MLCommons (with Google,
Hugging Face, and others) to make ML datasets more discoverable, accessible, and
interoperable. These value sets represent the controlled vocabularies and
enumerations used in the Croissant format.


Generated from: computing/croissant_ml.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class MLDataType(RichEnum):
    """
    Data types used in Croissant ML for describing field types in datasets.
    Based on XSD (XML Schema Definition) and schema.org vocabulary.
    
    """
    # Enum members
    TEXT = "TEXT"
    INTEGER = "INTEGER"
    FLOAT = "FLOAT"
    BOOLEAN = "BOOLEAN"
    DATE = "DATE"
    TIME = "TIME"
    DATETIME = "DATETIME"
    URL = "URL"

# Set metadata after class creation
MLDataType._metadata = {
    "TEXT": {'description': 'Text or string data', 'meaning': 'xsd:string'},
    "INTEGER": {'description': 'Integer numbers', 'meaning': 'xsd:integer'},
    "FLOAT": {'description': 'Floating point numbers', 'meaning': 'xsd:float'},
    "BOOLEAN": {'description': 'Boolean values (true/false)', 'meaning': 'xsd:boolean'},
    "DATE": {'description': 'Date values', 'meaning': 'xsd:date'},
    "TIME": {'description': 'Time values', 'meaning': 'xsd:time'},
    "DATETIME": {'description': 'Combined date and time values', 'meaning': 'xsd:dateTime'},
    "URL": {'description': 'Uniform Resource Locators', 'meaning': 'xsd:anyURI'},
}

class DatasetEncodingFormat(RichEnum):
    """
    Encoding formats (MIME types) commonly used for ML dataset files in Croissant.
    These specify how data is serialized and stored.
    
    """
    # Enum members
    CSV = "CSV"
    JSON = "JSON"
    JSONL = "JSONL"
    PARQUET = "PARQUET"
    PLAIN_TEXT = "PLAIN_TEXT"
    JPEG = "JPEG"
    PNG = "PNG"
    WAV = "WAV"
    MP4 = "MP4"
    ZIP = "ZIP"
    TAR = "TAR"

# Set metadata after class creation
DatasetEncodingFormat._metadata = {
    "CSV": {'description': 'Comma-separated values format for tabular data', 'meaning': 'EDAM:format_3752', 'annotations': {'mime_type': 'text/csv'}},
    "JSON": {'description': 'JavaScript Object Notation format for structured data', 'meaning': 'EDAM:format_3464', 'annotations': {'mime_type': 'application/json'}},
    "JSONL": {'description': 'JSON Lines format (newline-delimited JSON)', 'annotations': {'mime_type': 'application/jsonl', 'alt_mime_type': 'application/x-ndjson'}},
    "PARQUET": {'description': 'Apache Parquet columnar storage format', 'annotations': {'mime_type': 'application/parquet'}},
    "PLAIN_TEXT": {'description': 'Plain text files', 'annotations': {'mime_type': 'text/plain'}},
    "JPEG": {'description': 'JPEG image format', 'meaning': 'EDAM:format_3579', 'annotations': {'mime_type': 'image/jpeg'}},
    "PNG": {'description': 'Portable Network Graphics image format', 'meaning': 'EDAM:format_3603', 'annotations': {'mime_type': 'image/png'}},
    "WAV": {'description': 'Waveform Audio File Format', 'annotations': {'mime_type': 'audio/wav'}},
    "MP4": {'description': 'MPEG-4 multimedia container format', 'meaning': 'EDAM:format_3997', 'annotations': {'mime_type': 'video/mp4'}},
    "ZIP": {'description': 'ZIP archive format', 'meaning': 'EDAM:format_3987', 'annotations': {'mime_type': 'application/zip'}},
    "TAR": {'description': 'Tape Archive format', 'meaning': 'EDAM:format_3981', 'annotations': {'mime_type': 'application/x-tar'}},
}

class DatasetSplitType(RichEnum):
    """
    Standard dataset split types used in machine learning for training,
    validation, and testing. These splits are fundamental to ML model
    development and evaluation workflows.
    
    """
    # Enum members
    TRAIN = "TRAIN"
    VALIDATION = "VALIDATION"
    TEST = "TEST"
    ALL = "ALL"

# Set metadata after class creation
DatasetSplitType._metadata = {
    "TRAIN": {'description': 'Training split used for model learning', 'annotations': {'typical_size': '60-80% of data', 'purpose': 'model training'}},
    "VALIDATION": {'description': 'Validation split used for hyperparameter tuning and model selection', 'annotations': {'typical_size': '10-20% of data', 'purpose': 'model tuning', 'aliases': 'val, dev'}},
    "TEST": {'description': 'Test split used for final model evaluation', 'annotations': {'typical_size': '10-20% of data', 'purpose': 'model evaluation'}},
    "ALL": {'description': 'Complete dataset without splits'},
}

class MLLicenseType(RichEnum):
    """
    Common open source and Creative Commons licenses used for ML datasets.
    These licenses specify terms of use, redistribution, and modification.
    
    """
    # Enum members
    CC_BY_4_0 = "CC_BY_4_0"
    CC_BY_SA_4_0 = "CC_BY_SA_4_0"
    CC0_1_0 = "CC0_1_0"
    MIT = "MIT"
    APACHE_2_0 = "APACHE_2_0"
    BSD_3_CLAUSE = "BSD_3_CLAUSE"
    GPL_3_0 = "GPL_3_0"

# Set metadata after class creation
MLLicenseType._metadata = {
    "CC_BY_4_0": {'description': 'Creative Commons Attribution 4.0 International', 'meaning': 'spdx:CC-BY-4.0', 'annotations': {'allows_commercial': True, 'requires_attribution': True}},
    "CC_BY_SA_4_0": {'description': 'Creative Commons Attribution-ShareAlike 4.0 International', 'meaning': 'spdx:CC-BY-SA-4.0', 'annotations': {'allows_commercial': True, 'requires_attribution': True, 'share_alike': True}},
    "CC0_1_0": {'description': 'Creative Commons Zero 1.0 Universal (Public Domain Dedication)', 'meaning': 'spdx:CC0-1.0', 'annotations': {'public_domain': True}},
    "MIT": {'description': 'MIT License', 'meaning': 'spdx:MIT', 'annotations': {'osi_approved': True}},
    "APACHE_2_0": {'description': 'Apache License 2.0', 'meaning': 'spdx:Apache-2.0', 'annotations': {'osi_approved': True, 'patent_grant': True}},
    "BSD_3_CLAUSE": {'description': 'BSD 3-Clause "New" or "Revised" License', 'meaning': 'spdx:BSD-3-Clause', 'annotations': {'osi_approved': True}},
    "GPL_3_0": {'description': 'GNU General Public License v3.0', 'meaning': 'spdx:GPL-3.0-only', 'annotations': {'osi_approved': True, 'copyleft': True}},
}

class MLFieldRole(RichEnum):
    """
    Semantic roles that fields play in ML datasets. These roles help understand
    the purpose and usage of different data columns or attributes.
    
    """
    # Enum members
    FEATURE = "FEATURE"
    LABEL = "LABEL"
    METADATA = "METADATA"
    IDENTIFIER = "IDENTIFIER"

# Set metadata after class creation
MLFieldRole._metadata = {
    "FEATURE": {'description': 'Input features used for model prediction', 'annotations': {'also_known_as': 'input, predictor, independent variable'}},
    "LABEL": {'description': 'Target labels or outputs for supervised learning', 'annotations': {'also_known_as': 'target, output, dependent variable, ground truth'}},
    "METADATA": {'description': 'Descriptive information about the dataset or records', 'annotations': {'also_known_as': 'descriptive field, provenance'}},
    "IDENTIFIER": {'description': 'Unique identifiers for records or entities', 'annotations': {'also_known_as': 'ID, key, primary key'}},
}

class CompressionFormat(RichEnum):
    """
    Compression and archive formats commonly used for ML dataset distribution.
    
    """
    # Enum members
    ZIP = "ZIP"
    TAR = "TAR"
    GZIP = "GZIP"
    TAR_GZ = "TAR_GZ"

# Set metadata after class creation
CompressionFormat._metadata = {
    "ZIP": {'description': 'ZIP archive format with lossless data compression', 'meaning': 'EDAM:format_3987', 'annotations': {'mime_type': 'application/zip', 'typical_extension': '.zip'}},
    "TAR": {'description': 'Tape Archive format (typically used with compression)', 'meaning': 'EDAM:format_3981', 'annotations': {'mime_type': 'application/x-tar', 'typical_extension': '.tar'}},
    "GZIP": {'description': 'GNU zip compression format', 'meaning': 'EDAM:format_3989', 'annotations': {'mime_type': 'application/gzip', 'typical_extension': '.gz'}},
    "TAR_GZ": {'description': 'TAR archive compressed with GZIP', 'annotations': {'mime_type': 'application/gzip', 'typical_extension': '.tar.gz'}},
}

class MLMediaType(RichEnum):
    """
    Media types (MIME types) for different modalities of ML data including
    images, audio, video, and text.
    
    """
    # Enum members
    IMAGE_JPEG = "IMAGE_JPEG"
    IMAGE_PNG = "IMAGE_PNG"
    IMAGE_GIF = "IMAGE_GIF"
    IMAGE_TIFF = "IMAGE_TIFF"
    AUDIO_WAV = "AUDIO_WAV"
    AUDIO_MP3 = "AUDIO_MP3"
    AUDIO_FLAC = "AUDIO_FLAC"
    VIDEO_MP4 = "VIDEO_MP4"
    VIDEO_AVI = "VIDEO_AVI"
    VIDEO_WEBM = "VIDEO_WEBM"
    TEXT_PLAIN = "TEXT_PLAIN"
    TEXT_HTML = "TEXT_HTML"

# Set metadata after class creation
MLMediaType._metadata = {
    "IMAGE_JPEG": {'description': 'JPEG image format', 'meaning': 'EDAM:format_3579', 'annotations': {'mime_type': 'image/jpeg', 'modality': 'image'}},
    "IMAGE_PNG": {'description': 'PNG image format', 'meaning': 'EDAM:format_3603', 'annotations': {'mime_type': 'image/png', 'modality': 'image'}},
    "IMAGE_GIF": {'description': 'GIF image format', 'annotations': {'mime_type': 'image/gif', 'modality': 'image'}},
    "IMAGE_TIFF": {'description': 'TIFF image format', 'annotations': {'mime_type': 'image/tiff', 'modality': 'image'}},
    "AUDIO_WAV": {'description': 'Waveform Audio File Format', 'annotations': {'mime_type': 'audio/wav', 'modality': 'audio'}},
    "AUDIO_MP3": {'description': 'MP3 audio format', 'annotations': {'mime_type': 'audio/mpeg', 'modality': 'audio'}},
    "AUDIO_FLAC": {'description': 'FLAC lossless audio format', 'annotations': {'mime_type': 'audio/flac', 'modality': 'audio'}},
    "VIDEO_MP4": {'description': 'MPEG-4 video format', 'meaning': 'EDAM:format_3997', 'annotations': {'mime_type': 'video/mp4', 'modality': 'video'}},
    "VIDEO_AVI": {'description': 'Audio Video Interleaved format', 'meaning': 'EDAM:format_3990', 'annotations': {'mime_type': 'video/x-msvideo', 'modality': 'video'}},
    "VIDEO_WEBM": {'description': 'WebM video format', 'annotations': {'mime_type': 'video/webm', 'modality': 'video'}},
    "TEXT_PLAIN": {'description': 'Plain text format', 'annotations': {'mime_type': 'text/plain', 'modality': 'text'}},
    "TEXT_HTML": {'description': 'HTML format', 'annotations': {'mime_type': 'text/html', 'modality': 'text'}},
}

class MLModalityType(RichEnum):
    """
    High-level data modalities used in machine learning. These represent
    the fundamental types of input data that ML models process.
    
    """
    # Enum members
    TEXT = "TEXT"
    IMAGE = "IMAGE"
    AUDIO = "AUDIO"
    VIDEO = "VIDEO"
    MULTIMODAL = "MULTIMODAL"
    TABULAR = "TABULAR"
    TIME_SERIES = "TIME_SERIES"
    GRAPH = "GRAPH"

# Set metadata after class creation
MLModalityType._metadata = {
    "TEXT": {'description': 'Textual data (natural language, code, etc.)', 'annotations': {'examples': 'documents, sentences, tokens'}},
    "IMAGE": {'description': 'Visual image data', 'meaning': 'EDAM:data_2968', 'annotations': {'examples': 'photographs, diagrams, scans'}},
    "AUDIO": {'description': 'Audio/sound data', 'annotations': {'examples': 'speech, music, sound effects'}},
    "VIDEO": {'description': 'Video data (sequences of images with optional audio)', 'annotations': {'examples': 'movies, recordings, animations'}},
    "MULTIMODAL": {'description': 'Data combining multiple modalities', 'annotations': {'examples': 'image-text pairs, audio-visual data'}},
    "TABULAR": {'description': 'Structured tabular data', 'annotations': {'examples': 'spreadsheets, databases, CSV files'}},
    "TIME_SERIES": {'description': 'Sequential temporal data', 'annotations': {'examples': 'sensor readings, stock prices, logs'}},
    "GRAPH": {'description': 'Graph-structured data with nodes and edges', 'annotations': {'examples': 'social networks, knowledge graphs, molecular structures'}},
}

__all__ = [
    "MLDataType",
    "DatasetEncodingFormat",
    "DatasetSplitType",
    "MLLicenseType",
    "MLFieldRole",
    "CompressionFormat",
    "MLMediaType",
    "MLModalityType",
]