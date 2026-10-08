"""
Process Engineering Unit Operations Value Sets

Value sets for chemical and process engineering unit operations and process equipment. Unit operations are the fundamental processing steps (separation, reaction, heat/mass transfer, solids handling) that compose a process flowsheet, while process equipment types are the physical assets that implement them. These value sets are intended to support flowsheet data models such as the PISCES Standard Flowsheet Format (SFF), where unit operations / equipment are the nodes of a process graph.

Generated from: process_engineering/unit_operations.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class UnitOperationType(RichEnum):
    """
    Fundamental chemical and process engineering unit operations - the discrete processing steps that transform, separate, combine, or move process material. Grouped (via the unit_operation_class annotation) into momentum transfer, heat transfer, mass-transfer separations, mechanical separations, solids processing, reaction, and storage.
    """
    # Enum members
    PUMPING = "PUMPING"
    COMPRESSION = "COMPRESSION"
    GAS_MOVING = "GAS_MOVING"
    FLOW_SPLITTING = "FLOW_SPLITTING"
    STREAM_MIXING = "STREAM_MIXING"
    HEAT_EXCHANGE = "HEAT_EXCHANGE"
    HEATING = "HEATING"
    COOLING = "COOLING"
    CONDENSATION = "CONDENSATION"
    EVAPORATION = "EVAPORATION"
    DISTILLATION = "DISTILLATION"
    ABSORPTION = "ABSORPTION"
    STRIPPING = "STRIPPING"
    LIQUID_LIQUID_EXTRACTION = "LIQUID_LIQUID_EXTRACTION"
    LEACHING = "LEACHING"
    ADSORPTION = "ADSORPTION"
    ION_EXCHANGE = "ION_EXCHANGE"
    CHROMATOGRAPHY = "CHROMATOGRAPHY"
    CRYSTALLIZATION = "CRYSTALLIZATION"
    PRECIPITATION = "PRECIPITATION"
    DRYING = "DRYING"
    FREEZE_DRYING = "FREEZE_DRYING"
    HUMIDIFICATION = "HUMIDIFICATION"
    MEMBRANE_SEPARATION = "MEMBRANE_SEPARATION"
    MICROFILTRATION = "MICROFILTRATION"
    ULTRAFILTRATION = "ULTRAFILTRATION"
    NANOFILTRATION = "NANOFILTRATION"
    REVERSE_OSMOSIS = "REVERSE_OSMOSIS"
    DIALYSIS = "DIALYSIS"
    ELECTRODIALYSIS = "ELECTRODIALYSIS"
    PERVAPORATION = "PERVAPORATION"
    FILTRATION = "FILTRATION"
    CENTRIFUGATION = "CENTRIFUGATION"
    SEDIMENTATION = "SEDIMENTATION"
    CLARIFICATION = "CLARIFICATION"
    FLOTATION = "FLOTATION"
    FLOCCULATION = "FLOCCULATION"
    CYCLONE_SEPARATION = "CYCLONE_SEPARATION"
    SCREENING = "SCREENING"
    GAS_LIQUID_SEPARATION = "GAS_LIQUID_SEPARATION"
    SIZE_REDUCTION = "SIZE_REDUCTION"
    SIZE_ENLARGEMENT = "SIZE_ENLARGEMENT"
    MIXING = "MIXING"
    SOLIDS_CONVEYING = "SOLIDS_CONVEYING"
    CHEMICAL_REACTION = "CHEMICAL_REACTION"
    FERMENTATION = "FERMENTATION"
    COMBUSTION = "COMBUSTION"
    GASIFICATION = "GASIFICATION"
    PYROLYSIS = "PYROLYSIS"
    ELECTROLYSIS = "ELECTROLYSIS"
    NEUTRALIZATION = "NEUTRALIZATION"
    PURIFICATION = "PURIFICATION"
    STORAGE = "STORAGE"

# Set metadata after class creation
UnitOperationType._metadata = {
    "PUMPING": {'description': 'Raising the pressure or moving of a liquid stream using a pump', 'annotations': {'unit_operation_class': 'MOMENTUM_TRANSFER'}},
    "COMPRESSION": {'description': 'Raising the pressure of a gas or vapor stream using a compressor', 'annotations': {'unit_operation_class': 'MOMENTUM_TRANSFER'}},
    "GAS_MOVING": {'description': 'Moving a gas stream at low pressure rise using a fan or blower', 'annotations': {'unit_operation_class': 'MOMENTUM_TRANSFER'}},
    "FLOW_SPLITTING": {'description': 'Dividing a single stream into two or more streams of identical composition', 'annotations': {'unit_operation_class': 'MOMENTUM_TRANSFER'}},
    "STREAM_MIXING": {'description': 'Combining two or more streams into a single stream', 'annotations': {'unit_operation_class': 'MOMENTUM_TRANSFER'}},
    "HEAT_EXCHANGE": {'description': 'Transfer of thermal energy between two streams without phase-change intent', 'annotations': {'unit_operation_class': 'HEAT_TRANSFER'}},
    "HEATING": {'description': 'Raising the temperature of a process stream', 'annotations': {'unit_operation_class': 'HEAT_TRANSFER'}},
    "COOLING": {'description': 'Lowering the temperature of a process stream', 'annotations': {'unit_operation_class': 'HEAT_TRANSFER'}},
    "CONDENSATION": {'description': 'Converting a vapor to a liquid by removing heat', 'annotations': {'unit_operation_class': 'HEAT_TRANSFER'}},
    "EVAPORATION": {'description': 'Concentrating a solution by vaporizing solvent, typically water', 'meaning': 'CHMO:0001574', 'annotations': {'unit_operation_class': 'HEAT_TRANSFER'}},
    "DISTILLATION": {'description': 'Separation of components by differences in volatility (boiling point)', 'meaning': 'CHMO:0001532', 'annotations': {'unit_operation_class': 'MASS_TRANSFER_SEPARATION'}},
    "ABSORPTION": {'description': 'Selective transfer of one or more gas-phase components into a liquid solvent', 'annotations': {'unit_operation_class': 'MASS_TRANSFER_SEPARATION'}},
    "STRIPPING": {'description': 'Selective transfer of dissolved components from a liquid into a gas stream', 'annotations': {'unit_operation_class': 'MASS_TRANSFER_SEPARATION'}},
    "LIQUID_LIQUID_EXTRACTION": {'description': 'Separation by partitioning of solutes between two immiscible liquid phases', 'meaning': 'CHMO:0001577', 'annotations': {'unit_operation_class': 'MASS_TRANSFER_SEPARATION'}},
    "LEACHING": {'description': 'Solid-liquid extraction of soluble components from a solid using a solvent', 'meaning': 'CHMO:0001681', 'annotations': {'unit_operation_class': 'MASS_TRANSFER_SEPARATION'}},
    "ADSORPTION": {'description': 'Selective uptake of components onto the surface of a solid sorbent', 'annotations': {'unit_operation_class': 'MASS_TRANSFER_SEPARATION'}},
    "ION_EXCHANGE": {'description': 'Reversible exchange of ions between a solution and a solid ion-exchange resin', 'annotations': {'unit_operation_class': 'MASS_TRANSFER_SEPARATION'}},
    "CHROMATOGRAPHY": {'description': 'Separation by differential partitioning of solutes between a mobile and stationary phase', 'meaning': 'CHMO:0001000', 'annotations': {'unit_operation_class': 'MASS_TRANSFER_SEPARATION'}},
    "CRYSTALLIZATION": {'description': 'Formation of a solid crystalline phase from a solution or melt', 'meaning': 'PROCO:0000052', 'annotations': {'unit_operation_class': 'MASS_TRANSFER_SEPARATION'}},
    "PRECIPITATION": {'description': 'Formation of an insoluble solid from solution by chemical or physical means', 'meaning': 'CHMO:0001688', 'annotations': {'unit_operation_class': 'MASS_TRANSFER_SEPARATION'}},
    "DRYING": {'description': 'Removal of a liquid (usually water) from a solid or surface by vaporization', 'annotations': {'unit_operation_class': 'MASS_TRANSFER_SEPARATION'}},
    "FREEZE_DRYING": {'description': 'Removal of solvent by sublimation from the frozen state (lyophilization)', 'meaning': 'CHMO:0001553', 'annotations': {'unit_operation_class': 'MASS_TRANSFER_SEPARATION', 'aliases': 'lyophilization'}},
    "HUMIDIFICATION": {'description': 'Addition of water vapor to a gas stream', 'annotations': {'unit_operation_class': 'MASS_TRANSFER_SEPARATION'}},
    "MEMBRANE_SEPARATION": {'description': 'Separation of stream components using a semipermeable membrane', 'annotations': {'unit_operation_class': 'MEMBRANE_SEPARATION'}},
    "MICROFILTRATION": {'description': 'Membrane separation retaining particles roughly 0.1-10 micrometers', 'meaning': 'CHMO:0001641', 'annotations': {'unit_operation_class': 'MEMBRANE_SEPARATION'}},
    "ULTRAFILTRATION": {'description': 'Membrane separation retaining macromolecules and colloids', 'meaning': 'CHMO:0001645', 'annotations': {'unit_operation_class': 'MEMBRANE_SEPARATION'}},
    "NANOFILTRATION": {'description': 'Membrane separation retaining small molecules and multivalent ions', 'meaning': 'CHMO:0001642', 'annotations': {'unit_operation_class': 'MEMBRANE_SEPARATION'}},
    "REVERSE_OSMOSIS": {'description': 'Pressure-driven membrane separation rejecting dissolved salts and small solutes', 'meaning': 'CHMO:0001643', 'annotations': {'unit_operation_class': 'MEMBRANE_SEPARATION'}},
    "DIALYSIS": {'description': 'Diffusive membrane separation of solutes across a concentration gradient', 'meaning': 'CHMO:0001522', 'annotations': {'unit_operation_class': 'MEMBRANE_SEPARATION'}},
    "ELECTRODIALYSIS": {'description': 'Membrane separation of ions driven by an applied electric field', 'annotations': {'unit_operation_class': 'MEMBRANE_SEPARATION'}},
    "PERVAPORATION": {'description': 'Membrane separation combining permeation and partial vaporization of the permeate', 'annotations': {'unit_operation_class': 'MEMBRANE_SEPARATION'}},
    "FILTRATION": {'description': 'Separation of solids from a fluid by passage through a porous medium', 'meaning': 'CHMO:0001640', 'annotations': {'unit_operation_class': 'MECHANICAL_SEPARATION'}},
    "CENTRIFUGATION": {'description': 'Separation of phases by density difference under centrifugal force', 'meaning': 'OBI:0302886', 'annotations': {'unit_operation_class': 'MECHANICAL_SEPARATION'}},
    "SEDIMENTATION": {'description': 'Gravity separation of suspended solids or immiscible liquids by settling', 'annotations': {'unit_operation_class': 'MECHANICAL_SEPARATION'}},
    "CLARIFICATION": {'description': 'Removal of suspended solids from a liquid to produce a clarified stream', 'annotations': {'unit_operation_class': 'MECHANICAL_SEPARATION'}},
    "FLOTATION": {'description': 'Separation of solids or droplets by attachment to rising gas bubbles', 'annotations': {'unit_operation_class': 'MECHANICAL_SEPARATION'}},
    "FLOCCULATION": {'description': 'Aggregation of fine suspended particles into larger flocs to aid separation', 'annotations': {'unit_operation_class': 'MECHANICAL_SEPARATION'}},
    "CYCLONE_SEPARATION": {'description': 'Separation of particles from a fluid using centrifugal force in a cyclone', 'annotations': {'unit_operation_class': 'MECHANICAL_SEPARATION'}},
    "SCREENING": {'description': 'Separation of particulate solids by size using a screen or sieve', 'annotations': {'unit_operation_class': 'MECHANICAL_SEPARATION'}},
    "GAS_LIQUID_SEPARATION": {'description': 'Disengagement of vapor and liquid phases, e.g. in a flash or knockout drum', 'annotations': {'unit_operation_class': 'MECHANICAL_SEPARATION'}},
    "SIZE_REDUCTION": {'description': 'Reduction of particle size by crushing, grinding, or milling (comminution)', 'annotations': {'unit_operation_class': 'SOLIDS_PROCESSING'}},
    "SIZE_ENLARGEMENT": {'description': 'Increase of particle size by granulation, agglomeration, or pelletizing', 'annotations': {'unit_operation_class': 'SOLIDS_PROCESSING'}},
    "MIXING": {'description': 'Blending of materials to achieve compositional or thermal uniformity', 'meaning': 'CHMO:0001685', 'annotations': {'unit_operation_class': 'SOLIDS_PROCESSING'}},
    "SOLIDS_CONVEYING": {'description': 'Transport of bulk particulate solids between process steps', 'annotations': {'unit_operation_class': 'SOLIDS_PROCESSING'}},
    "CHEMICAL_REACTION": {'description': 'Chemical conversion of reactants to products in a reactor', 'annotations': {'unit_operation_class': 'REACTION'}},
    "FERMENTATION": {'description': 'Microbial or enzymatic conversion of substrate to product in a bioreactor', 'meaning': 'CHMO:0001624', 'annotations': {'unit_operation_class': 'REACTION'}},
    "COMBUSTION": {'description': 'Exothermic oxidation of a fuel, typically to generate heat or power', 'meaning': 'CHMO:0001473', 'annotations': {'unit_operation_class': 'REACTION'}},
    "GASIFICATION": {'description': 'Conversion of carbonaceous feedstock to synthesis gas under limited oxygen', 'meaning': 'CHMO:0001501', 'annotations': {'unit_operation_class': 'REACTION'}},
    "PYROLYSIS": {'description': 'Thermal decomposition of material in the absence of oxygen', 'meaning': 'CHMO:0001502', 'annotations': {'unit_operation_class': 'REACTION'}},
    "ELECTROLYSIS": {'description': 'Driving a non-spontaneous chemical reaction using electrical energy', 'annotations': {'unit_operation_class': 'REACTION'}},
    "NEUTRALIZATION": {'description': 'Adjustment of pH by reaction of acid and base', 'annotations': {'unit_operation_class': 'REACTION'}},
    "PURIFICATION": {'description': 'Removal of impurities to increase the purity of a product stream', 'meaning': 'CHMO:0002231', 'annotations': {'unit_operation_class': 'SEPARATION'}},
    "STORAGE": {'description': 'Holding of material in a vessel or tank between process steps', 'annotations': {'unit_operation_class': 'STORAGE'}},
}

class ProcessEquipmentType(RichEnum):
    """
    Physical equipment / asset types used in process plants. These correspond to the nodes of a process flowsheet and complement UnitOperationType (which describes the function performed). Grouped via the equipment_class annotation.
    """
    # Enum members
    STORAGE_TANK = "STORAGE_TANK"
    PRESSURE_VESSEL = "PRESSURE_VESSEL"
    HOPPER = "HOPPER"
    FLASH_DRUM = "FLASH_DRUM"
    KNOCKOUT_DRUM = "KNOCKOUT_DRUM"
    REACTOR = "REACTOR"
    BIOREACTOR = "BIOREACTOR"
    FERMENTER = "FERMENTER"
    DISTILLATION_COLUMN = "DISTILLATION_COLUMN"
    ABSORPTION_COLUMN = "ABSORPTION_COLUMN"
    STRIPPING_COLUMN = "STRIPPING_COLUMN"
    EXTRACTION_COLUMN = "EXTRACTION_COLUMN"
    CHROMATOGRAPHY_COLUMN = "CHROMATOGRAPHY_COLUMN"
    SCRUBBER = "SCRUBBER"
    HEAT_EXCHANGER = "HEAT_EXCHANGER"
    CONDENSER = "CONDENSER"
    REBOILER = "REBOILER"
    EVAPORATOR = "EVAPORATOR"
    FURNACE = "FURNACE"
    BOILER = "BOILER"
    COOLING_TOWER = "COOLING_TOWER"
    DRYER = "DRYER"
    CRYSTALLIZER = "CRYSTALLIZER"
    PUMP = "PUMP"
    COMPRESSOR = "COMPRESSOR"
    BLOWER = "BLOWER"
    FAN = "FAN"
    VALVE = "VALVE"
    CENTRIFUGE = "CENTRIFUGE"
    FILTER = "FILTER"
    DECANTER = "DECANTER"
    CLARIFIER = "CLARIFIER"
    CYCLONE = "CYCLONE"
    HYDROCYCLONE = "HYDROCYCLONE"
    MEMBRANE_MODULE = "MEMBRANE_MODULE"
    SETTLER = "SETTLER"
    MIXER = "MIXER"
    AGITATOR = "AGITATOR"
    MILL = "MILL"
    CRUSHER = "CRUSHER"
    SCREEN = "SCREEN"
    CONVEYOR = "CONVEYOR"

# Set metadata after class creation
ProcessEquipmentType._metadata = {
    "STORAGE_TANK": {'description': 'Atmospheric or low-pressure vessel for holding liquids or solids', 'annotations': {'equipment_class': 'VESSEL'}},
    "PRESSURE_VESSEL": {'description': 'Vessel designed to hold contents at elevated pressure', 'annotations': {'equipment_class': 'VESSEL'}},
    "HOPPER": {'description': 'Funnel-shaped vessel for storing and discharging bulk solids', 'annotations': {'equipment_class': 'VESSEL'}},
    "FLASH_DRUM": {'description': 'Vessel for separating vapor and liquid produced by a pressure let-down', 'annotations': {'equipment_class': 'VESSEL'}},
    "KNOCKOUT_DRUM": {'description': 'Vessel that removes entrained liquid from a gas stream', 'annotations': {'equipment_class': 'VESSEL'}},
    "REACTOR": {'description': 'Vessel in which chemical reactions are carried out', 'annotations': {'equipment_class': 'REACTOR', 'subtypes': 'CSTR, plug-flow, batch, fixed-bed, fluidized-bed'}},
    "BIOREACTOR": {'description': 'Vessel for culturing cells or carrying out enzymatic reactions', 'meaning': 'OBI:0001046', 'annotations': {'equipment_class': 'REACTOR'}},
    "FERMENTER": {'description': 'Bioreactor configured for microbial fermentation', 'annotations': {'equipment_class': 'REACTOR'}},
    "DISTILLATION_COLUMN": {'description': 'Column with trays or packing for vapor-liquid separation by distillation', 'annotations': {'equipment_class': 'COLUMN'}},
    "ABSORPTION_COLUMN": {'description': 'Column for gas absorption into a liquid solvent', 'annotations': {'equipment_class': 'COLUMN'}},
    "STRIPPING_COLUMN": {'description': 'Column for stripping volatile components from a liquid', 'annotations': {'equipment_class': 'COLUMN'}},
    "EXTRACTION_COLUMN": {'description': 'Column for liquid-liquid extraction', 'annotations': {'equipment_class': 'COLUMN'}},
    "CHROMATOGRAPHY_COLUMN": {'description': 'Column packed with a stationary phase for chromatographic separation', 'meaning': 'OBI:0000038', 'annotations': {'equipment_class': 'COLUMN'}},
    "SCRUBBER": {'description': 'Contactor for removing pollutants or particulates from a gas using a liquid', 'annotations': {'equipment_class': 'COLUMN'}},
    "HEAT_EXCHANGER": {'description': 'Equipment that transfers heat between two fluid streams', 'annotations': {'equipment_class': 'HEAT_TRANSFER', 'subtypes': 'shell-and-tube, plate, air-cooled'}},
    "CONDENSER": {'description': 'Heat exchanger that condenses a vapor to liquid', 'annotations': {'equipment_class': 'HEAT_TRANSFER'}},
    "REBOILER": {'description': 'Heat exchanger that supplies boilup at the base of a distillation column', 'annotations': {'equipment_class': 'HEAT_TRANSFER'}},
    "EVAPORATOR": {'description': 'Equipment that concentrates a solution by vaporizing solvent', 'annotations': {'equipment_class': 'HEAT_TRANSFER'}},
    "FURNACE": {'description': 'Fired heater that raises stream temperature by combustion', 'annotations': {'equipment_class': 'HEAT_TRANSFER'}},
    "BOILER": {'description': 'Equipment that generates steam by transferring combustion heat to water', 'annotations': {'equipment_class': 'HEAT_TRANSFER'}},
    "COOLING_TOWER": {'description': 'Equipment that rejects process heat to the atmosphere by evaporative cooling', 'annotations': {'equipment_class': 'HEAT_TRANSFER'}},
    "DRYER": {'description': 'Equipment for removing liquid from solids by vaporization', 'annotations': {'equipment_class': 'HEAT_TRANSFER'}},
    "CRYSTALLIZER": {'description': 'Equipment for producing crystalline solids from solution or melt', 'annotations': {'equipment_class': 'HEAT_TRANSFER'}},
    "PUMP": {'description': 'Machine that moves or pressurizes a liquid', 'annotations': {'equipment_class': 'FLUID_MOVER'}},
    "COMPRESSOR": {'description': 'Machine that raises the pressure of a gas', 'annotations': {'equipment_class': 'FLUID_MOVER'}},
    "BLOWER": {'description': 'Machine that moves gas at a low pressure rise', 'annotations': {'equipment_class': 'FLUID_MOVER'}},
    "FAN": {'description': 'Machine that moves large gas volumes at very low pressure rise', 'annotations': {'equipment_class': 'FLUID_MOVER'}},
    "VALVE": {'description': 'Device that regulates, directs, or controls stream flow', 'annotations': {'equipment_class': 'FLUID_MOVER'}},
    "CENTRIFUGE": {'description': 'Equipment that separates phases by density under centrifugal force', 'meaning': 'OBI:0400106', 'annotations': {'equipment_class': 'SEPARATION'}},
    "FILTER": {'description': 'Equipment that separates solids from a fluid using a porous medium', 'annotations': {'equipment_class': 'SEPARATION'}},
    "DECANTER": {'description': 'Equipment that separates immiscible liquids or settled solids by gravity', 'annotations': {'equipment_class': 'SEPARATION'}},
    "CLARIFIER": {'description': 'Settling tank that removes suspended solids from a liquid', 'annotations': {'equipment_class': 'SEPARATION'}},
    "CYCLONE": {'description': 'Device that separates particles from a fluid by centrifugal action', 'annotations': {'equipment_class': 'SEPARATION'}},
    "HYDROCYCLONE": {'description': 'Cyclone that separates solids or immiscible liquids from a liquid stream', 'annotations': {'equipment_class': 'SEPARATION'}},
    "MEMBRANE_MODULE": {'description': 'Housing containing membrane elements for a membrane separation', 'annotations': {'equipment_class': 'SEPARATION'}},
    "SETTLER": {'description': 'Vessel allowing phases to separate by gravity settling', 'annotations': {'equipment_class': 'SEPARATION'}},
    "MIXER": {'description': 'Equipment for blending streams or materials', 'annotations': {'equipment_class': 'SOLIDS_HANDLING'}},
    "AGITATOR": {'description': 'Impeller-driven device that mixes vessel contents', 'annotations': {'equipment_class': 'SOLIDS_HANDLING'}},
    "MILL": {'description': 'Equipment that reduces particle size by grinding or crushing', 'annotations': {'equipment_class': 'SOLIDS_HANDLING'}},
    "CRUSHER": {'description': 'Equipment that reduces large solids by mechanical force', 'annotations': {'equipment_class': 'SOLIDS_HANDLING'}},
    "SCREEN": {'description': 'Equipment that classifies particulate solids by size', 'annotations': {'equipment_class': 'SOLIDS_HANDLING'}},
    "CONVEYOR": {'description': 'Equipment that transports bulk solids between locations', 'annotations': {'equipment_class': 'SOLIDS_HANDLING'}},
}

__all__ = [
    "UnitOperationType",
    "ProcessEquipmentType",
]