"""

Generated from: lab_automation/operations.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class LiquidHandlingOperationEnum(RichEnum):
    """
    Operations for automated liquid handling in laboratory automation
    """
    # Enum members
    PICK_UP_TIPS = "PICK_UP_TIPS"
    ASPIRATE = "ASPIRATE"
    DISPENSE = "DISPENSE"
    RETURN_TIPS = "RETURN_TIPS"
    DROP_TIPS = "DROP_TIPS"
    TRANSFER = "TRANSFER"
    PIPETTING = "PIPETTING"
    MIXING = "MIXING"
    ALIQUOTING = "ALIQUOTING"
    SERIAL_DILUTION = "SERIAL_DILUTION"
    PLATE_STAMPING = "PLATE_STAMPING"
    ACOUSTIC_TRANSFER = "ACOUSTIC_TRANSFER"
    MOUTH_PIPETTING = "MOUTH_PIPETTING"

# Set metadata after class creation
LiquidHandlingOperationEnum._metadata = {
    "PICK_UP_TIPS": {'description': 'Operation to pick up pipette tips from a tip rack'},
    "ASPIRATE": {'description': 'Operation to draw liquid into pipette tips'},
    "DISPENSE": {'description': 'Operation to dispense liquid from pipette tips'},
    "RETURN_TIPS": {'description': 'Operation to return pipette tips to a tip rack'},
    "DROP_TIPS": {'description': 'Operation to drop or discard pipette tips'},
    "TRANSFER": {'description': 'Combined operation to aspirate from source and dispense to destination'},
    "PIPETTING": {'description': 'A procedure or technique by which the size of the three dimensional space occupied by a liquid substance is ascertained using a pipette', 'meaning': 'MMO:0000392'},
    "MIXING": {'description': 'Operation to mix liquids by repeated aspiration and dispensing'},
    "ALIQUOTING": {'description': 'Operation to distribute a sample into multiple equal portions'},
    "SERIAL_DILUTION": {'description': 'Operation to create a series of dilutions of a substance in solution'},
    "PLATE_STAMPING": {'description': 'Operation to transfer samples from one plate to another in the same well pattern'},
    "ACOUSTIC_TRANSFER": {'description': 'Acoustic liquid handling that uses acoustics to fly individual droplets from a source container to a destination'},
    "MOUTH_PIPETTING": {'description': "A method of using the researcher's mouth to apply small negative pressure to aspirate a volume into a pipette", 'meaning': 'EFO:0010182'},
}

class SampleProcessingOperationEnum(RichEnum):
    """
    General sample processing operations in automated laboratories
    """
    # Enum members
    CENTRIFUGATION = "CENTRIFUGATION"
    INCUBATION = "INCUBATION"
    THERMAL_CYCLING = "THERMAL_CYCLING"
    WASHING = "WASHING"
    DETECTION = "DETECTION"
    MEASUREMENT = "MEASUREMENT"
    SEPARATION = "SEPARATION"
    EXTRACTION = "EXTRACTION"
    HEATING = "HEATING"
    COOLING = "COOLING"
    SHAKING = "SHAKING"
    PLATE_MOVEMENT = "PLATE_MOVEMENT"
    BARCODE_READING = "BARCODE_READING"

# Set metadata after class creation
SampleProcessingOperationEnum._metadata = {
    "CENTRIFUGATION": {'description': 'Operation to separate components of a sample using centrifugal force'},
    "INCUBATION": {'description': 'Operation to maintain samples at controlled environmental conditions over time'},
    "THERMAL_CYCLING": {'description': 'Operation to cycle samples through different temperatures for PCR or similar processes'},
    "WASHING": {'description': 'Operation to wash samples or plates to remove unwanted material'},
    "DETECTION": {'description': 'Operation to detect signals from samples (absorbance, fluorescence, luminescence)'},
    "MEASUREMENT": {'description': 'Operation to measure a property or characteristic of a sample'},
    "SEPARATION": {'description': 'Operation to separate components of a sample mixture'},
    "EXTRACTION": {'description': 'Operation to extract specific components from a sample'},
    "HEATING": {'description': 'Operation to heat samples to a specified temperature'},
    "COOLING": {'description': 'Operation to cool samples to a specified temperature'},
    "SHAKING": {'description': 'Operation to shake samples for mixing or agitation'},
    "PLATE_MOVEMENT": {'description': 'Operation to move plates between different locations or devices'},
    "BARCODE_READING": {'description': 'Operation to read barcode labels on samples or containers'},
}

__all__ = [
    "LiquidHandlingOperationEnum",
    "SampleProcessingOperationEnum",
]