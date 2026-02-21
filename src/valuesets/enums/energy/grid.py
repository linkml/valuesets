"""
Electrical Grid Value Sets

Value sets for electrical grid components, energy storage, and grid management relevant to the DOE Scaling the Grid challenge

Generated from: energy/grid.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class GridComponentType(RichEnum):
    """
    Types of physical components in electrical transmission and distribution grids
    """
    # Enum members
    TRANSMISSION_LINE = "TRANSMISSION_LINE"
    DISTRIBUTION_LINE = "DISTRIBUTION_LINE"
    TRANSFORMER = "TRANSFORMER"
    SUBSTATION = "SUBSTATION"
    CIRCUIT_BREAKER = "CIRCUIT_BREAKER"
    CAPACITOR_BANK = "CAPACITOR_BANK"
    FACTS_DEVICE = "FACTS_DEVICE"
    SMART_METER = "SMART_METER"
    INVERTER = "INVERTER"
    RELAY = "RELAY"

# Set metadata after class creation
GridComponentType._metadata = {
    "TRANSMISSION_LINE": {'description': 'High-voltage conductors that carry electricity over long distances from generation to substations'},
    "DISTRIBUTION_LINE": {'description': 'Medium- and low-voltage conductors that deliver electricity from substations to end users'},
    "TRANSFORMER": {'description': 'Device that changes voltage levels between transmission and distribution systems', 'meaning': 'NCIT:C50227'},
    "SUBSTATION": {'description': 'Facility that switches, transforms, and regulates electrical power in the grid'},
    "CIRCUIT_BREAKER": {'description': 'Protective device that automatically interrupts current flow during fault conditions'},
    "CAPACITOR_BANK": {'description': 'Array of capacitors used for reactive power compensation and voltage regulation'},
    "FACTS_DEVICE": {'description': 'Flexible AC Transmission System device for controlling power flow and improving grid stability'},
    "SMART_METER": {'description': 'Advanced metering device that records energy consumption and communicates with the utility'},
    "INVERTER": {'description': 'Device that converts direct current (DC) to alternating current (AC) for grid connection'},
    "RELAY": {'description': 'Protective device that detects abnormal conditions and triggers circuit breakers'},
}

class GridEnergyStorageType(RichEnum):
    """
    Types of energy storage technologies used for grid-scale and distributed applications
    """
    # Enum members
    LITHIUM_ION_BATTERY = "LITHIUM_ION_BATTERY"
    FLOW_BATTERY = "FLOW_BATTERY"
    PUMPED_HYDROELECTRIC = "PUMPED_HYDROELECTRIC"
    COMPRESSED_AIR = "COMPRESSED_AIR"
    FLYWHEEL = "FLYWHEEL"
    SUPERCAPACITOR = "SUPERCAPACITOR"
    THERMAL_STORAGE = "THERMAL_STORAGE"
    HYDROGEN_STORAGE = "HYDROGEN_STORAGE"
    GRAVITY_STORAGE = "GRAVITY_STORAGE"
    SODIUM_ION_BATTERY = "SODIUM_ION_BATTERY"

# Set metadata after class creation
GridEnergyStorageType._metadata = {
    "LITHIUM_ION_BATTERY": {'description': 'Rechargeable battery using lithium ion intercalation in electrode materials', 'meaning': 'OEO:00000248'},
    "FLOW_BATTERY": {'description': 'Rechargeable battery using liquid electrolytes stored in external tanks for scalable capacity', 'meaning': 'OEO:00000169'},
    "PUMPED_HYDROELECTRIC": {'description': 'Energy storage by pumping water to an elevated reservoir and releasing it through turbines'},
    "COMPRESSED_AIR": {'description': 'Energy storage by compressing air into underground caverns or tanks for later expansion through turbines'},
    "FLYWHEEL": {'description': 'Energy storage as rotational kinetic energy in a spinning mass'},
    "SUPERCAPACITOR": {'description': 'Electrochemical capacitor providing high power density with rapid charge and discharge cycles'},
    "THERMAL_STORAGE": {'description': 'Energy storage as heat in materials such as molten salt, concrete, or phase-change materials'},
    "HYDROGEN_STORAGE": {'description': 'Energy storage by producing hydrogen via electrolysis for later use in fuel cells or turbines'},
    "GRAVITY_STORAGE": {'description': 'Energy storage by raising heavy masses to height and lowering them to generate electricity'},
    "SODIUM_ION_BATTERY": {'description': 'Rechargeable battery using sodium ion intercalation as a lower-cost alternative to lithium-ion', 'meaning': 'OEO:00000376'},
}

class GridManagementStrategyType(RichEnum):
    """
    Strategies for managing and optimizing the operation of electrical grids
    """
    # Enum members
    DEMAND_RESPONSE = "DEMAND_RESPONSE"
    LOAD_BALANCING = "LOAD_BALANCING"
    FREQUENCY_REGULATION = "FREQUENCY_REGULATION"
    VOLTAGE_CONTROL = "VOLTAGE_CONTROL"
    PEAK_SHAVING = "PEAK_SHAVING"
    DISTRIBUTED_GENERATION = "DISTRIBUTED_GENERATION"
    MICROGRID_OPERATION = "MICROGRID_OPERATION"
    VIRTUAL_POWER_PLANT = "VIRTUAL_POWER_PLANT"
    GRID_SCALE_STORAGE_DISPATCH = "GRID_SCALE_STORAGE_DISPATCH"

# Set metadata after class creation
GridManagementStrategyType._metadata = {
    "DEMAND_RESPONSE": {'description': 'Adjusting consumer electricity demand in response to supply conditions or price signals'},
    "LOAD_BALANCING": {'description': 'Distributing electrical load across generation sources to maintain grid stability'},
    "FREQUENCY_REGULATION": {'description': 'Maintaining grid frequency at nominal levels by balancing generation and load in real time'},
    "VOLTAGE_CONTROL": {'description': 'Maintaining voltage levels within acceptable ranges across the grid'},
    "PEAK_SHAVING": {'description': 'Reducing peak electricity demand through storage dispatch or demand reduction programs'},
    "DISTRIBUTED_GENERATION": {'description': 'Generating electricity from many small sources close to the point of consumption'},
    "MICROGRID_OPERATION": {'description': 'Operating a localized energy grid that can function independently or connected to the main grid'},
    "VIRTUAL_POWER_PLANT": {'description': 'Aggregating distributed energy resources to operate as a single coordinated power source'},
    "GRID_SCALE_STORAGE_DISPATCH": {'description': 'Coordinating charge and discharge of large-scale energy storage assets for grid optimization'},
}

__all__ = [
    "GridComponentType",
    "GridEnergyStorageType",
    "GridManagementStrategyType",
]