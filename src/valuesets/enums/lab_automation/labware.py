"""

Generated from: lab_automation/labware.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class MicroplateFormatEnum(RichEnum):
    """
    Standard microplate well configurations following ANSI/SLAS standards
    """
    # Enum members
    WELL_6 = "WELL_6"
    WELL_12 = "WELL_12"
    WELL_24 = "WELL_24"
    WELL_48 = "WELL_48"
    WELL_96 = "WELL_96"
    WELL_384 = "WELL_384"
    WELL_1536 = "WELL_1536"

# Set metadata after class creation
MicroplateFormatEnum._metadata = {
    "WELL_6": {'description': 'Microplate with 6 wells'},
    "WELL_12": {'description': 'Microplate with 12 wells'},
    "WELL_24": {'description': 'Microplate with 24 wells'},
    "WELL_48": {'description': 'Microplate with 48 wells'},
    "WELL_96": {'description': 'Microplate with 96 wells arranged in 8 rows of 12 columns with 9mm well-to-well spacing', 'meaning': 'MSIO:0000162', 'annotations': {'well_spacing': '9mm', 'standard': 'ANSI/SLAS 4-2004'}},
    "WELL_384": {'description': 'Microplate with 384 wells with 4.5mm well-to-well spacing', 'annotations': {'well_spacing': '4.5mm', 'standard': 'ANSI/SLAS 4-2004'}},
    "WELL_1536": {'description': 'Microplate with 1536 wells with 2.25mm well-to-well spacing', 'annotations': {'well_spacing': '2.25mm', 'standard': 'ANSI/SLAS 4-2004'}},
}

class ContainerTypeEnum(RichEnum):
    """
    Types of laboratory containers and labware
    """
    # Enum members
    MICROPLATE = "MICROPLATE"
    DEEP_WELL_PLATE = "DEEP_WELL_PLATE"
    PCR_PLATE = "PCR_PLATE"
    TUBE_RACK = "TUBE_RACK"
    MICROTUBE = "MICROTUBE"
    SCREW_CAP_TUBE = "SCREW_CAP_TUBE"
    SNAP_CAP_TUBE = "SNAP_CAP_TUBE"
    RESERVOIR = "RESERVOIR"
    PIPETTE_TIP_BOX = "PIPETTE_TIP_BOX"
    SPIN_COLUMN = "SPIN_COLUMN"
    MICROPLATE_WELL = "MICROPLATE_WELL"

# Set metadata after class creation
ContainerTypeEnum._metadata = {
    "MICROPLATE": {'description': 'A flat dish with multiple individual wells that are arrayed in a standardized number, size, and arrangement', 'meaning': 'NCIT:C43377'},
    "DEEP_WELL_PLATE": {'description': 'A microplate with deeper wells for increased sample volume capacity'},
    "PCR_PLATE": {'description': 'A microplate specifically designed for PCR thermal cycling applications'},
    "TUBE_RACK": {'description': 'A rack designed to hold multiple laboratory tubes'},
    "MICROTUBE": {'description': 'Small laboratory tube with volume capacity from 0.2 ml to 2.0 ml', 'annotations': {'volume_range': '0.2-2.0 ml'}},
    "SCREW_CAP_TUBE": {'description': 'Laboratory tube with screw cap closure'},
    "SNAP_CAP_TUBE": {'description': 'Laboratory tube with snap cap closure'},
    "RESERVOIR": {'description': 'Container for holding bulk reagents for dispensing'},
    "PIPETTE_TIP_BOX": {'description': 'Container for storing pipette tips in organized racks'},
    "SPIN_COLUMN": {'description': 'A chromatography column which is suitable for putting it into a centrifuge', 'meaning': 'OBI:0000570'},
    "MICROPLATE_WELL": {'description': 'Any of the individual wells on a microwell plate', 'meaning': 'NCIT:C128793'},
}

class PlateMaterialEnum(RichEnum):
    """
    Material composition of laboratory microplates
    """
    # Enum members
    POLYSTYRENE = "POLYSTYRENE"
    POLYPROPYLENE = "POLYPROPYLENE"
    GLASS = "GLASS"

# Set metadata after class creation
PlateMaterialEnum._metadata = {
    "POLYSTYRENE": {'description': 'Plates made from polystyrene, the most common material for standard applications'},
    "POLYPROPYLENE": {'description': 'Plates made from polypropylene for chemical resistance'},
    "GLASS": {'description': 'Plates with glass inserts for samples not suitable for plastic containers'},
}

class PlateCoatingEnum(RichEnum):
    """
    Surface treatment of microplates
    """
    # Enum members
    COATED = "COATED"
    UNCOATED = "UNCOATED"
    TISSUE_CULTURE_TREATED = "TISSUE_CULTURE_TREATED"
    PROTEIN_BINDING = "PROTEIN_BINDING"

# Set metadata after class creation
PlateCoatingEnum._metadata = {
    "COATED": {'description': 'A microplate whose surface has been treated, for instance by covalently attaching proteins to favor cell growth', 'meaning': 'MSIO:0000164'},
    "UNCOATED": {'description': 'A microplate whose surface has not received any treatment and is uniquely made of polymer', 'meaning': 'MSIO:0000170'},
    "TISSUE_CULTURE_TREATED": {'description': 'Surface treatment to enhance cell attachment and growth'},
    "PROTEIN_BINDING": {'description': 'Surface treatment optimized for protein binding assays'},
}

__all__ = [
    "MicroplateFormatEnum",
    "ContainerTypeEnum",
    "PlateMaterialEnum",
    "PlateCoatingEnum",
]