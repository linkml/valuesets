"""
Preservation Event Types

Event types for digital preservation activities, based on PREMIS 3.0.

PREMIS (Preservation Metadata: Implementation Strategies) defines events as
"actions performed within or outside the repository that affect the long term
preservation of digital objects."

See: https://www.loc.gov/standards/premis/


Generated from: preservation/events.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class PreservationEventType(RichEnum):
    """
    Actions performed within or outside a repository that affect the long-term
    preservation of digital objects. Based on PREMIS 3.0 event types.
    
    """
    # Enum members
    ACCESSION = "ACCESSION"
    APPRAISAL = "APPRAISAL"
    CAPTURE = "CAPTURE"
    COMPILING = "COMPILING"
    COMPRESSION = "COMPRESSION"
    CREATION = "CREATION"
    DEACCESSION = "DEACCESSION"
    DECOMPRESSION = "DECOMPRESSION"
    DECRYPTION = "DECRYPTION"
    DELETION = "DELETION"
    DIGITAL_SIGNATURE_GENERATION = "DIGITAL_SIGNATURE_GENERATION"
    DIGITAL_SIGNATURE_VALIDATION = "DIGITAL_SIGNATURE_VALIDATION"
    DISPLAYING = "DISPLAYING"
    DISSEMINATION = "DISSEMINATION"
    ENCRYPTION = "ENCRYPTION"
    EXECUTION = "EXECUTION"
    EXPORTING = "EXPORTING"
    EXTRACTION = "EXTRACTION"
    FILENAME_CHANGE = "FILENAME_CHANGE"
    FIXITY_CHECK = "FIXITY_CHECK"
    FORENSIC_FEATURE_ANALYSIS = "FORENSIC_FEATURE_ANALYSIS"
    FORMAT_IDENTIFICATION = "FORMAT_IDENTIFICATION"
    IMAGING = "IMAGING"
    INFORMATION_PACKAGE_CREATION = "INFORMATION_PACKAGE_CREATION"
    INFORMATION_PACKAGE_MERGING = "INFORMATION_PACKAGE_MERGING"
    INFORMATION_PACKAGE_SPLITTING = "INFORMATION_PACKAGE_SPLITTING"
    INGESTION = "INGESTION"
    INGESTION_END = "INGESTION_END"
    INGESTION_START = "INGESTION_START"
    INTERPRETING = "INTERPRETING"
    MESSAGE_DIGEST_CALCULATION = "MESSAGE_DIGEST_CALCULATION"
    METADATA_EXTRACTION = "METADATA_EXTRACTION"
    METADATA_MODIFICATION = "METADATA_MODIFICATION"
    MIGRATION = "MIGRATION"
    MODIFICATION = "MODIFICATION"
    NORMALIZATION = "NORMALIZATION"
    PACKING = "PACKING"
    POLICY_ASSIGNMENT = "POLICY_ASSIGNMENT"
    PRINTING = "PRINTING"
    QUARANTINE = "QUARANTINE"
    RECOVERY = "RECOVERY"
    REDACTION = "REDACTION"
    REFRESHMENT = "REFRESHMENT"
    RENDERING = "RENDERING"
    REPLICATION = "REPLICATION"
    TRANSFER = "TRANSFER"
    UNPACKING = "UNPACKING"
    UNQUARANTINE = "UNQUARANTINE"
    VALIDATION = "VALIDATION"
    VIRUS_CHECK = "VIRUS_CHECK"

# Set metadata after class creation
PreservationEventType._metadata = {
    "ACCESSION": {'description': "The process of adding objects to a repository's holdings.", 'meaning': 'premis:eventType/acc'},
    "APPRAISAL": {'description': 'The process of evaluating objects for long-term retention.', 'meaning': 'premis:eventType/app'},
    "CAPTURE": {'description': 'The process of recording or acquiring digital content.', 'meaning': 'premis:eventType/cap'},
    "COMPILING": {'description': 'The process of converting source code into executable code.', 'meaning': 'premis:eventType/com'},
    "COMPRESSION": {'description': 'The process of reducing file size through encoding.', 'meaning': 'premis:eventType/cmp'},
    "CREATION": {'description': 'The act of creating a new digital object.', 'meaning': 'premis:eventType/cre'},
    "DEACCESSION": {'description': "The process of removing objects from a repository's holdings.", 'meaning': 'premis:eventType/dea'},
    "DECOMPRESSION": {'description': 'The process of restoring compressed data to its original form.', 'meaning': 'premis:eventType/dec'},
    "DECRYPTION": {'description': 'The process of converting encrypted data back to plaintext.', 'meaning': 'premis:eventType/der'},
    "DELETION": {'description': 'The act of removing a digital object.', 'meaning': 'premis:eventType/del'},
    "DIGITAL_SIGNATURE_GENERATION": {'description': 'The process of creating a digital signature for authentication.', 'meaning': 'premis:eventType/dig'},
    "DIGITAL_SIGNATURE_VALIDATION": {'description': 'The process of verifying the authenticity of a digital signature.', 'meaning': 'premis:eventType/dsv'},
    "DISPLAYING": {'description': 'The process of presenting content for viewing.', 'meaning': 'premis:eventType/dip'},
    "DISSEMINATION": {'description': 'The process of making content available to users.', 'meaning': 'premis:eventType/dis'},
    "ENCRYPTION": {'description': 'The process of converting plaintext to ciphertext.', 'meaning': 'premis:eventType/enc'},
    "EXECUTION": {'description': 'The process of running software or scripts.', 'meaning': 'premis:eventType/exe'},
    "EXPORTING": {'description': 'The process of extracting content from a system.', 'meaning': 'premis:eventType/exp'},
    "EXTRACTION": {'description': 'The process of retrieving content from a container or archive.', 'meaning': 'premis:eventType/ext'},
    "FILENAME_CHANGE": {'description': "The act of modifying a file's name.", 'meaning': 'premis:eventType/fil'},
    "FIXITY_CHECK": {'description': 'The process of verifying data integrity using checksums or hashes.', 'meaning': 'premis:eventType/fix'},
    "FORENSIC_FEATURE_ANALYSIS": {'description': 'Analysis of digital objects for authenticity or provenance evidence.', 'meaning': 'premis:eventType/for'},
    "FORMAT_IDENTIFICATION": {'description': 'The process of determining the file format of a digital object.', 'meaning': 'premis:eventType/fmi'},
    "IMAGING": {'description': 'The process of creating a bit-level copy of storage media.', 'meaning': 'premis:eventType/ima'},
    "INFORMATION_PACKAGE_CREATION": {'description': 'Creating a packaged unit of content and metadata (SIP, AIP, DIP).', 'meaning': 'premis:eventType/ipc'},
    "INFORMATION_PACKAGE_MERGING": {'description': 'Combining multiple information packages into one.', 'meaning': 'premis:eventType/ipm'},
    "INFORMATION_PACKAGE_SPLITTING": {'description': 'Dividing an information package into multiple packages.', 'meaning': 'premis:eventType/ips'},
    "INGESTION": {'description': 'The process of accepting and processing submitted content.', 'meaning': 'premis:eventType/ing'},
    "INGESTION_END": {'description': 'The completion of the ingestion process.', 'meaning': 'premis:eventType/ine'},
    "INGESTION_START": {'description': 'The beginning of the ingestion process.', 'meaning': 'premis:eventType/ins'},
    "INTERPRETING": {'description': 'The process of rendering or executing interpretable content.', 'meaning': 'premis:eventType/int'},
    "MESSAGE_DIGEST_CALCULATION": {'description': 'The process of computing a hash or checksum value.', 'meaning': 'premis:eventType/mes'},
    "METADATA_EXTRACTION": {'description': 'The process of extracting metadata from digital objects.', 'meaning': 'premis:eventType/mee'},
    "METADATA_MODIFICATION": {'description': 'The process of changing metadata associated with an object.', 'meaning': 'premis:eventType/mem'},
    "MIGRATION": {'description': 'The process of converting content from one format to another\nto ensure continued accessibility.\n', 'meaning': 'premis:eventType/mig'},
    "MODIFICATION": {'description': 'The act of changing the content of a digital object.', 'meaning': 'premis:eventType/mod'},
    "NORMALIZATION": {'description': 'The process of converting content to a standard format\nfor preservation or access.\n', 'meaning': 'premis:eventType/nor'},
    "PACKING": {'description': 'The process of combining files into a container format.', 'meaning': 'premis:eventType/pac'},
    "POLICY_ASSIGNMENT": {'description': 'The act of associating preservation policies with objects.', 'meaning': 'premis:eventType/poa'},
    "PRINTING": {'description': 'The process of producing a physical copy of digital content.', 'meaning': 'premis:eventType/pri'},
    "QUARANTINE": {'description': 'Isolating objects suspected of containing malware or corruption.', 'meaning': 'premis:eventType/qua'},
    "RECOVERY": {'description': 'The process of restoring objects from backup or damaged media.', 'meaning': 'premis:eventType/rec'},
    "REDACTION": {'description': 'The process of removing sensitive content from objects.', 'meaning': 'premis:eventType/red'},
    "REFRESHMENT": {'description': 'Copying data to new storage media without format change.', 'meaning': 'premis:eventType/ref'},
    "RENDERING": {'description': 'The process of generating a viewable representation.', 'meaning': 'premis:eventType/ren'},
    "REPLICATION": {'description': 'Creating exact copies for redundancy or distribution.', 'meaning': 'premis:eventType/rep'},
    "TRANSFER": {'description': 'Moving objects between systems or locations.', 'meaning': 'premis:eventType/tra'},
    "UNPACKING": {'description': 'Extracting files from a container format.', 'meaning': 'premis:eventType/unp'},
    "UNQUARANTINE": {'description': 'Releasing objects from quarantine after verification.', 'meaning': 'premis:eventType/unq'},
    "VALIDATION": {'description': 'Verifying that objects conform to expected specifications.', 'meaning': 'premis:eventType/val'},
    "VIRUS_CHECK": {'description': 'Scanning objects for malware or viruses.', 'meaning': 'premis:eventType/vir'},
}

class PreservationEventOutcome(RichEnum):
    """
    The outcome or result of a preservation event.
    """
    # Enum members
    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"
    WARNING = "WARNING"

# Set metadata after class creation
PreservationEventOutcome._metadata = {
    "SUCCESS": {'description': 'The event completed successfully.', 'meaning': 'premis:eventOutcome/suc'},
    "FAILURE": {'description': 'The event failed to complete.', 'meaning': 'premis:eventOutcome/fai'},
    "WARNING": {'description': 'The event completed with warnings or issues.', 'meaning': 'premis:eventOutcome/war'},
}

__all__ = [
    "PreservationEventType",
    "PreservationEventOutcome",
]