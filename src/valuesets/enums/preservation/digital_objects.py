"""
Digital Object Preservation Metadata

Value sets for digital object preservation, based on PREMIS 3.0.

Includes object categories, copyright status, rights basis, and
preservation level classifications.

See: https://www.loc.gov/standards/premis/


Generated from: preservation/digital_objects.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class DigitalObjectCategory(RichEnum):
    """
    The category of object to which preservation metadata applies.
    Based on PREMIS object categories.
    
    """
    # Enum members
    BITSTREAM = "BITSTREAM"
    FILE = "FILE"
    INTELLECTUAL_ENTITY = "INTELLECTUAL_ENTITY"
    REPRESENTATION = "REPRESENTATION"

# Set metadata after class creation
DigitalObjectCategory._metadata = {
    "BITSTREAM": {'description': 'Contiguous or non-contiguous data within a file that has meaningful\nproperties for preservation purposes. A bitstream cannot be transformed\ninto a standalone file without the addition of file structure.\n', 'meaning': 'premis:objectCategory/bit'},
    "FILE": {'description': 'A named and ordered sequence of bytes that is known to an operating\nsystem. A file can be zero or more bytes and has a file format,\naccess permissions, and other file system characteristics.\n', 'meaning': 'premis:objectCategory/fil'},
    "INTELLECTUAL_ENTITY": {'description': 'A coherent set of content that is reasonably described as a unit.\nExamples include a book, a photograph, a database, or a software\napplication. An intellectual entity may contain other intellectual\nentities.\n', 'meaning': 'premis:objectCategory/int'},
    "REPRESENTATION": {'description': 'The set of files, including structural metadata, needed for a\ncomplete and reasonable rendition of an intellectual entity.\nA digital object may have multiple representations.\n', 'meaning': 'premis:objectCategory/rep'},
}

class CopyrightStatus(RichEnum):
    """
    A designation for the copyright status of an object at the time
    the rights statement is recorded. Based on PREMIS.
    
    """
    # Enum members
    COPYRIGHTED = "COPYRIGHTED"
    PUBLIC_DOMAIN = "PUBLIC_DOMAIN"
    UNKNOWN = "UNKNOWN"

# Set metadata after class creation
CopyrightStatus._metadata = {
    "COPYRIGHTED": {'description': 'The object is protected by copyright.', 'meaning': 'premis:copyrightStatus/cpr'},
    "PUBLIC_DOMAIN": {'description': 'The object is not protected by copyright, either because copyright\nhas expired, was never applicable, or has been waived.\n', 'meaning': 'premis:copyrightStatus/pub'},
    "UNKNOWN": {'description': 'The copyright status cannot be determined.', 'meaning': 'premis:copyrightStatus/unk'},
}

class RightsBasis(RichEnum):
    """
    The basis for the right or permission granted for an object.
    Based on PREMIS rights basis vocabulary.
    
    """
    # Enum members
    COPYRIGHT = "COPYRIGHT"
    INSTITUTIONAL_POLICY = "INSTITUTIONAL_POLICY"
    LICENSE = "LICENSE"
    STATUTE = "STATUTE"
    OTHER = "OTHER"

# Set metadata after class creation
RightsBasis._metadata = {
    "COPYRIGHT": {'description': 'Rights based on copyright law.', 'meaning': 'premis:rightsBasis/cop'},
    "INSTITUTIONAL_POLICY": {'description': 'Rights based on the policies of the holding institution.', 'meaning': 'premis:rightsBasis/ins'},
    "LICENSE": {'description': 'Rights based on a license agreement.', 'meaning': 'premis:rightsBasis/lic'},
    "STATUTE": {'description': 'Rights based on statutory law other than copyright.', 'meaning': 'premis:rightsBasis/sta'},
    "OTHER": {'description': 'Rights based on another basis not listed.', 'meaning': 'premis:rightsBasis/oth'},
}

class PreservationLevelRole(RichEnum):
    """
    The context in which a preservation level value is specified.
    Based on PREMIS preservation level role vocabulary.
    
    """
    # Enum members
    CAPABILITY = "CAPABILITY"
    INTENTION = "INTENTION"
    REQUIREMENT = "REQUIREMENT"

# Set metadata after class creation
PreservationLevelRole._metadata = {
    "CAPABILITY": {'description': 'The preservation level that the repository is capable of providing\nbased on its technical infrastructure and resources.\n', 'meaning': 'premis:preservationLevelRole/cap'},
    "INTENTION": {'description': 'The preservation level that the repository intends to provide\nfor the object, based on policy decisions.\n', 'meaning': 'premis:preservationLevelRole/int'},
    "REQUIREMENT": {'description': 'The preservation level required by the depositor or\nother stakeholder for the object.\n', 'meaning': 'premis:preservationLevelRole/req'},
}

class PreservationLevelValue(RichEnum):
    """
    Common preservation level tiers indicating the degree of preservation
    commitment. These are not from PREMIS directly but represent common
    practice in digital preservation.
    
    """
    # Enum members
    BIT_LEVEL = "BIT_LEVEL"
    LOGICAL_PRESERVATION = "LOGICAL_PRESERVATION"
    SEMANTIC_PRESERVATION = "SEMANTIC_PRESERVATION"
    FULL_PRESERVATION = "FULL_PRESERVATION"

# Set metadata after class creation
PreservationLevelValue._metadata = {
    "BIT_LEVEL": {'description': 'Ensures the exact bit sequence is maintained. Includes fixity checks\nand secure storage but no format migration or access provision.\n', 'aliases': ['Level 1']},
    "LOGICAL_PRESERVATION": {'description': 'Maintains the ability to render or use the content. May include\nformat migration to ensure long-term accessibility.\n', 'aliases': ['Level 2', 'Content Preservation']},
    "SEMANTIC_PRESERVATION": {'description': 'Preserves the meaning and context of content, including relationships\nbetween objects and their intellectual context.\n', 'aliases': ['Level 3', 'Full Preservation']},
    "FULL_PRESERVATION": {'description': 'Comprehensive preservation including all aspects: bit-level integrity,\nformat migration, semantic context, and provenance tracking.\n', 'aliases': ['Level 4']},
}

__all__ = [
    "DigitalObjectCategory",
    "CopyrightStatus",
    "RightsBasis",
    "PreservationLevelRole",
    "PreservationLevelValue",
]