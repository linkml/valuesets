"""

Generated from: lab_automation/devices.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class LaboratoryDeviceTypeEnum(RichEnum):
    """
    Types of automated laboratory devices and equipment
    """
    # Enum members
    LIQUID_HANDLER = "LIQUID_HANDLER"
    LIQUID_EXTRACTION_ROBOT = "LIQUID_EXTRACTION_ROBOT"
    CENTRIFUGE = "CENTRIFUGE"
    MICROCENTRIFUGE = "MICROCENTRIFUGE"
    INCUBATOR = "INCUBATOR"
    INCUBATOR_SHAKER = "INCUBATOR_SHAKER"
    MICROPLATE_READER = "MICROPLATE_READER"
    ELISA_MICROPLATE_READER = "ELISA_MICROPLATE_READER"
    MULTIMODE_MICROPLATE_READER = "MULTIMODE_MICROPLATE_READER"
    MICROPLATE_WASHER = "MICROPLATE_WASHER"
    ELISA_MICROPLATE_WASHER = "ELISA_MICROPLATE_WASHER"
    MULTICHANNEL_PIPETTE = "MULTICHANNEL_PIPETTE"
    ROBOTIC_ARM = "ROBOTIC_ARM"
    THERMAL_CYCLER = "THERMAL_CYCLER"
    COLONY_PICKER = "COLONY_PICKER"
    BARCODE_READER = "BARCODE_READER"
    PLATE_HANDLER = "PLATE_HANDLER"
    DISPENSER = "DISPENSER"

# Set metadata after class creation
LaboratoryDeviceTypeEnum._metadata = {
    "LIQUID_HANDLER": {'description': 'A device that is used for automated liquid transfer and handling', 'meaning': 'OBI:0400112'},
    "LIQUID_EXTRACTION_ROBOT": {'description': 'A liquid handling device that provides automatic liquid extraction', 'meaning': 'OBI:0001097'},
    "CENTRIFUGE": {'description': 'A device with a rapidly rotating container that applies centrifugal force to its contents', 'meaning': 'OBI:0400106'},
    "MICROCENTRIFUGE": {'description': 'A type of centrifuge that is designed for small tubes (0.2 ml to 2.0 ml), has a compact design, and has a small footprint', 'meaning': 'OBI:0001100'},
    "INCUBATOR": {'description': 'A device in which environmental conditions (light, photoperiod, temperature, humidity, etc.) can be controlled', 'meaning': 'OBI:0000136'},
    "INCUBATOR_SHAKER": {'description': 'An incubating device that provides shaking motion for biomedical applications (e.g., cell cultures)', 'meaning': 'OBI:0001076'},
    "MICROPLATE_READER": {'description': 'A measurement device that detects biological, chemical or physical events of samples in microtiter plates', 'meaning': 'OBI:0001058'},
    "ELISA_MICROPLATE_READER": {'description': 'A microplate reader that is used for enzyme-linked immunosorbent assays (ELISA)', 'meaning': 'OBI:0001059'},
    "MULTIMODE_MICROPLATE_READER": {'description': 'A microplate reader that can detect multiple types of absorbance, luminescence or fluorescence', 'meaning': 'OBI:0001090'},
    "MICROPLATE_WASHER": {'description': 'A device that is used to wash immunoassays in microwell strips and plates with professional accuracy', 'meaning': 'OBI:0001113'},
    "ELISA_MICROPLATE_WASHER": {'description': 'A microplate washer that is used for enzyme-linked immunosorbent assays (ELISA)', 'meaning': 'OBI:0001115'},
    "MULTICHANNEL_PIPETTE": {'description': 'A pipetting system that has a plurality of tip fittings and is used for multi-well plate applications', 'meaning': 'OBI:0001118'},
    "ROBOTIC_ARM": {'description': 'A programmable mechanical arm used in laboratory automation', 'meaning': 'SNOMED:82830000'},
    "THERMAL_CYCLER": {'description': 'A laboratory apparatus used to amplify DNA segments via the polymerase chain reaction'},
    "COLONY_PICKER": {'description': 'An automated device for selecting and transferring individual bacterial or yeast colonies'},
    "BARCODE_READER": {'description': 'A device that reads barcode labels on laboratory samples and containers'},
    "PLATE_HANDLER": {'description': 'An automated device designed to transfer microplates between workstations and lab instruments'},
    "DISPENSER": {'description': 'A device for automated dispensing of reagents or samples'},
}

class RoboticArmTypeEnum(RichEnum):
    """
    Types of robotic arms used in laboratory automation systems
    """
    # Enum members
    FLEXIBLE_CHANNEL_ARM = "FLEXIBLE_CHANNEL_ARM"
    MULTI_CHANNEL_ARM = "MULTI_CHANNEL_ARM"
    ROBOTIC_GRIPPER_ARM = "ROBOTIC_GRIPPER_ARM"
    SINGLE_PROBE_ARM = "SINGLE_PROBE_ARM"

# Set metadata after class creation
RoboticArmTypeEnum._metadata = {
    "FLEXIBLE_CHANNEL_ARM": {'description': 'Robotic arm with flexible channels for disposable tip handling and liquid handling', 'annotations': {'abbreviation': 'FCA'}},
    "MULTI_CHANNEL_ARM": {'description': 'Robotic arm used for high-throughput pipetting with 96 or 384 channels', 'annotations': {'abbreviation': 'MCA'}},
    "ROBOTIC_GRIPPER_ARM": {'description': 'Robotic arm used to pick and transfer objects within the working area, equipped with dedicated gripper fingers', 'annotations': {'abbreviation': 'RGA'}},
    "SINGLE_PROBE_ARM": {'description': 'Robotic arm with a single probe for individual sample handling'},
}

__all__ = [
    "LaboratoryDeviceTypeEnum",
    "RoboticArmTypeEnum",
]