"""
Advanced Manufacturing Value Sets

Value sets for manufacturing processes and technologies relevant to the DOE Reenvisioning Advanced Manufacturing challenge

Generated from: industry/manufacturing.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class ManufacturingProcessType(RichEnum):
    """
    Types of manufacturing processes including additive, subtractive, and formative methods
    """
    # Enum members
    ADDITIVE_MANUFACTURING = "ADDITIVE_MANUFACTURING"
    SUBTRACTIVE_MANUFACTURING = "SUBTRACTIVE_MANUFACTURING"
    FORMATIVE_MANUFACTURING = "FORMATIVE_MANUFACTURING"
    CASTING = "CASTING"
    FORGING = "FORGING"
    WELDING = "WELDING"
    MACHINING = "MACHINING"
    INJECTION_MOLDING = "INJECTION_MOLDING"
    EXTRUSION = "EXTRUSION"
    POWDER_METALLURGY = "POWDER_METALLURGY"
    CHEMICAL_VAPOR_DEPOSITION = "CHEMICAL_VAPOR_DEPOSITION"
    PHYSICAL_VAPOR_DEPOSITION = "PHYSICAL_VAPOR_DEPOSITION"
    ELECTROFORMING = "ELECTROFORMING"

# Set metadata after class creation
ManufacturingProcessType._metadata = {
    "ADDITIVE_MANUFACTURING": {'description': 'Manufacturing by adding material layer by layer to build a three-dimensional object'},
    "SUBTRACTIVE_MANUFACTURING": {'description': 'Manufacturing by removing material from a solid block to create a desired shape'},
    "FORMATIVE_MANUFACTURING": {'description': 'Manufacturing by reshaping material through mechanical forces without significant addition or removal'},
    "CASTING": {'description': 'Pouring molten material into a mold and allowing it to solidify'},
    "FORGING": {'description': 'Shaping metal using compressive forces applied by hammering, pressing, or rolling'},
    "WELDING": {'description': 'Joining materials by applying heat, pressure, or both to fuse them together'},
    "MACHINING": {'description': 'Removing material from a workpiece using cutting tools to achieve a desired geometry'},
    "INJECTION_MOLDING": {'description': 'Forcing molten material into a mold cavity where it cools and hardens', 'meaning': 'CHMO:0001430'},
    "EXTRUSION": {'description': 'Forcing material through a die to create objects with a fixed cross-sectional profile', 'meaning': 'CHMO:0001613'},
    "POWDER_METALLURGY": {'description': 'Forming metal parts from compacted and sintered metal powders'},
    "CHEMICAL_VAPOR_DEPOSITION": {'description': 'Depositing thin films by exposing a substrate to volatile precursors that react on the surface', 'meaning': 'CHMO:0001314'},
    "PHYSICAL_VAPOR_DEPOSITION": {'description': 'Depositing thin films by condensing vaporized material onto a substrate surface', 'meaning': 'CHMO:0001356'},
    "ELECTROFORMING": {'description': 'Producing metal parts by electrodeposition of metal onto a mandrel or pattern'},
}

class SmartManufacturingTechnologyType(RichEnum):
    """
    Types of digital and intelligent technologies used in modern manufacturing environments
    """
    # Enum members
    DIGITAL_TWIN = "DIGITAL_TWIN"
    INDUSTRIAL_IOT = "INDUSTRIAL_IOT"
    PREDICTIVE_MAINTENANCE = "PREDICTIVE_MAINTENANCE"
    COMPUTER_VISION_INSPECTION = "COMPUTER_VISION_INSPECTION"
    ROBOTIC_ASSEMBLY = "ROBOTIC_ASSEMBLY"
    AUTOMATED_QUALITY_CONTROL = "AUTOMATED_QUALITY_CONTROL"
    SUPPLY_CHAIN_OPTIMIZATION = "SUPPLY_CHAIN_OPTIMIZATION"
    PROCESS_SIMULATION = "PROCESS_SIMULATION"

# Set metadata after class creation
SmartManufacturingTechnologyType._metadata = {
    "DIGITAL_TWIN": {'description': 'Virtual replica of a physical asset or process used for simulation and optimization'},
    "INDUSTRIAL_IOT": {'description': 'Network of interconnected sensors and devices in industrial settings for data collection and control'},
    "PREDICTIVE_MAINTENANCE": {'description': 'Using data analytics and machine learning to predict equipment failures before they occur'},
    "COMPUTER_VISION_INSPECTION": {'description': 'Automated visual inspection of manufactured parts using computer vision and image analysis'},
    "ROBOTIC_ASSEMBLY": {'description': 'Automated assembly of components using programmable robotic systems'},
    "AUTOMATED_QUALITY_CONTROL": {'description': 'Automated systems for monitoring and ensuring product quality during manufacturing'},
    "SUPPLY_CHAIN_OPTIMIZATION": {'description': 'Data-driven optimization of supply chain logistics and inventory management'},
    "PROCESS_SIMULATION": {'description': 'Computer-based simulation of manufacturing processes for design and optimization'},
}

__all__ = [
    "ManufacturingProcessType",
    "SmartManufacturingTechnologyType",
]