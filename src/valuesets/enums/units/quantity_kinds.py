"""
QUDT Quantity Kinds Value Set

Value set for physical quantity kinds based on QUDT (Quantities, Units, Dimensions and Types). Quantity kinds represent the abstract type of a physical quantity, independent of its units. For example, "length" is a quantity kind that can be measured in meters, feet, etc.

Generated from: units/quantity_kinds.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class QuantityKindEnum(RichEnum):
    """
    Physical quantity kinds based on QUDT. These represent abstract types of physical quantities independent of the units used to measure them.
    """
    # Enum members
    LENGTH = "LENGTH"
    MASS = "MASS"
    TIME = "TIME"
    THERMODYNAMIC_TEMPERATURE = "THERMODYNAMIC_TEMPERATURE"
    AMOUNT_OF_SUBSTANCE = "AMOUNT_OF_SUBSTANCE"
    ELECTRIC_CURRENT = "ELECTRIC_CURRENT"
    LUMINOUS_INTENSITY = "LUMINOUS_INTENSITY"
    AREA = "AREA"
    VOLUME = "VOLUME"
    ANGLE = "ANGLE"
    SOLID_ANGLE = "SOLID_ANGLE"
    VELOCITY = "VELOCITY"
    SPEED = "SPEED"
    ACCELERATION = "ACCELERATION"
    FORCE = "FORCE"
    PRESSURE = "PRESSURE"
    ENERGY = "ENERGY"
    WORK = "WORK"
    POWER = "POWER"
    MOMENTUM = "MOMENTUM"
    TORQUE = "TORQUE"
    ANGULAR_VELOCITY = "ANGULAR_VELOCITY"
    ANGULAR_ACCELERATION = "ANGULAR_ACCELERATION"
    DENSITY = "DENSITY"
    VISCOSITY = "VISCOSITY"
    KINEMATIC_VISCOSITY = "KINEMATIC_VISCOSITY"
    FREQUENCY = "FREQUENCY"
    MASS_CONCENTRATION = "MASS_CONCENTRATION"
    AMOUNT_CONCENTRATION = "AMOUNT_CONCENTRATION"
    ELECTRIC_CHARGE = "ELECTRIC_CHARGE"
    ELECTRIC_POTENTIAL = "ELECTRIC_POTENTIAL"
    ELECTRIC_RESISTANCE = "ELECTRIC_RESISTANCE"
    ELECTRICAL_CONDUCTIVITY = "ELECTRICAL_CONDUCTIVITY"
    CAPACITANCE = "CAPACITANCE"
    INDUCTANCE = "INDUCTANCE"
    MAGNETIC_FLUX = "MAGNETIC_FLUX"
    MAGNETIC_FLUX_DENSITY = "MAGNETIC_FLUX_DENSITY"
    HEAT_CAPACITY = "HEAT_CAPACITY"
    SPECIFIC_HEAT_CAPACITY = "SPECIFIC_HEAT_CAPACITY"
    THERMAL_CONDUCTIVITY = "THERMAL_CONDUCTIVITY"
    LUMINOUS_FLUX = "LUMINOUS_FLUX"
    ILLUMINANCE = "ILLUMINANCE"
    RADIANT_INTENSITY = "RADIANT_INTENSITY"
    ACTIVITY = "ACTIVITY"
    ABSORBED_DOSE = "ABSORBED_DOSE"
    DOSE_EQUIVALENT = "DOSE_EQUIVALENT"
    INFORMATION_ENTROPY = "INFORMATION_ENTROPY"
    DATA_RATE = "DATA_RATE"

# Set metadata after class creation
QuantityKindEnum._metadata = {
    "LENGTH": {'description': 'A 1-D extent quality representing distance between two points', 'meaning': 'quantitykind:Length', 'annotations': {'si_base': 'true', 'dimension': 'L'}},
    "MASS": {'description': 'The amount of matter in an object', 'meaning': 'quantitykind:Mass', 'annotations': {'si_base': 'true', 'dimension': 'M'}},
    "TIME": {'description': 'Duration or temporal extent', 'meaning': 'quantitykind:Time', 'annotations': {'si_base': 'true', 'dimension': 'T', 'pato_label': 'duration'}},
    "THERMODYNAMIC_TEMPERATURE": {'description': 'The thermal energy of a system', 'meaning': 'quantitykind:ThermodynamicTemperature', 'annotations': {'si_base': 'true', 'dimension': 'Θ', 'pato_label': 'temperature'}},
    "AMOUNT_OF_SUBSTANCE": {'description': 'The number of elementary entities (atoms, molecules, etc.)', 'meaning': 'quantitykind:AmountOfSubstance', 'annotations': {'si_base': 'true', 'dimension': 'N', 'pato_label': 'amount'}},
    "ELECTRIC_CURRENT": {'description': 'Flow of electric charge per unit time', 'meaning': 'quantitykind:ElectricCurrent', 'annotations': {'si_base': 'true', 'dimension': 'I'}},
    "LUMINOUS_INTENSITY": {'description': 'Luminous power per unit solid angle emitted by a point light source', 'meaning': 'quantitykind:LuminousIntensity', 'annotations': {'si_base': 'true', 'dimension': 'J', 'pato_label': 'luminance'}},
    "AREA": {'description': 'A 2-D extent representing the size of a surface', 'meaning': 'quantitykind:Area', 'annotations': {'dimension': 'L²'}},
    "VOLUME": {'description': 'A 3-D extent representing the amount of space occupied', 'meaning': 'quantitykind:Volume', 'annotations': {'dimension': 'L³'}},
    "ANGLE": {'description': 'The figure formed by two rays sharing a common endpoint', 'meaning': 'quantitykind:Angle', 'annotations': {'dimension': 'dimensionless'}},
    "SOLID_ANGLE": {'description': 'A 3-D angular measure', 'meaning': 'quantitykind:SolidAngle', 'annotations': {'dimension': 'dimensionless'}},
    "VELOCITY": {'description': 'Rate of change of position with direction', 'meaning': 'quantitykind:Velocity', 'annotations': {'dimension': 'L·T⁻¹'}},
    "SPEED": {'description': 'Scalar rate of change of position', 'meaning': 'quantitykind:Speed', 'annotations': {'dimension': 'L·T⁻¹'}},
    "ACCELERATION": {'description': 'Rate of change of velocity', 'meaning': 'quantitykind:Acceleration', 'annotations': {'dimension': 'L·T⁻²'}},
    "FORCE": {'description': 'Rate of change of momentum', 'meaning': 'quantitykind:Force', 'annotations': {'dimension': 'M·L·T⁻²'}},
    "PRESSURE": {'description': 'Force per unit area', 'meaning': 'quantitykind:Pressure', 'annotations': {'dimension': 'M·L⁻¹·T⁻²'}},
    "ENERGY": {'description': 'Capacity to do work', 'meaning': 'quantitykind:Energy', 'annotations': {'dimension': 'M·L²·T⁻²'}},
    "WORK": {'description': 'Energy transferred by a force', 'meaning': 'quantitykind:Work', 'annotations': {'dimension': 'M·L²·T⁻²'}},
    "POWER": {'description': 'Rate of doing work or transferring energy', 'meaning': 'quantitykind:Power', 'annotations': {'dimension': 'M·L²·T⁻³'}},
    "MOMENTUM": {'description': 'Product of mass and velocity', 'meaning': 'quantitykind:Momentum', 'annotations': {'dimension': 'M·L·T⁻¹'}},
    "TORQUE": {'description': 'Rotational force or moment of force', 'meaning': 'quantitykind:Torque', 'annotations': {'dimension': 'M·L²·T⁻²'}},
    "ANGULAR_VELOCITY": {'description': 'Rate of change of angular position', 'meaning': 'quantitykind:AngularVelocity', 'annotations': {'dimension': 'T⁻¹'}},
    "ANGULAR_ACCELERATION": {'description': 'Rate of change of angular velocity', 'meaning': 'quantitykind:AngularAcceleration', 'annotations': {'dimension': 'T⁻²'}},
    "DENSITY": {'description': 'Mass per unit volume', 'meaning': 'quantitykind:Density', 'annotations': {'dimension': 'M·L⁻³', 'pato_label': 'mass density'}},
    "VISCOSITY": {'description': 'Internal resistance to flow', 'meaning': 'quantitykind:DynamicViscosity', 'annotations': {'dimension': 'M·L⁻¹·T⁻¹'}},
    "KINEMATIC_VISCOSITY": {'description': 'Dynamic viscosity divided by density', 'meaning': 'quantitykind:KinematicViscosity', 'annotations': {'dimension': 'L²·T⁻¹'}},
    "FREQUENCY": {'description': 'Number of repetitive events per unit time', 'meaning': 'quantitykind:Frequency', 'annotations': {'dimension': 'T⁻¹'}},
    "MASS_CONCENTRATION": {'description': 'Mass of a substance per unit volume', 'meaning': 'quantitykind:MassConcentration', 'annotations': {'dimension': 'M·L⁻³', 'pato_label': 'concentration of'}},
    "AMOUNT_CONCENTRATION": {'description': 'Amount of substance per unit volume (molarity)', 'meaning': 'quantitykind:AmountConcentration', 'annotations': {'dimension': 'N·L⁻³'}},
    "ELECTRIC_CHARGE": {'description': 'Fundamental property of matter causing electromagnetic interaction', 'meaning': 'quantitykind:ElectricCharge', 'annotations': {'dimension': 'I·T'}},
    "ELECTRIC_POTENTIAL": {'description': 'Potential energy per unit charge (voltage)', 'meaning': 'quantitykind:ElectricPotential', 'annotations': {'dimension': 'M·L²·T⁻³·I⁻¹'}, 'aliases': ['voltage']},
    "ELECTRIC_RESISTANCE": {'description': 'Opposition to electric current flow', 'meaning': 'quantitykind:Resistance', 'annotations': {'dimension': 'M·L²·T⁻³·I⁻²'}},
    "ELECTRICAL_CONDUCTIVITY": {'description': 'Ability to conduct electric current', 'meaning': 'quantitykind:Conductivity', 'annotations': {'dimension': 'I²·T³·M⁻¹·L⁻³'}},
    "CAPACITANCE": {'description': 'Ability to store electric charge', 'meaning': 'quantitykind:Capacitance', 'annotations': {'dimension': 'I²·T⁴·M⁻¹·L⁻²'}},
    "INDUCTANCE": {'description': 'Property relating magnetic flux to electric current', 'meaning': 'quantitykind:Inductance', 'annotations': {'dimension': 'M·L²·T⁻²·I⁻²'}},
    "MAGNETIC_FLUX": {'description': 'Measure of total magnetic field passing through a surface', 'meaning': 'quantitykind:MagneticFlux', 'annotations': {'dimension': 'M·L²·T⁻²·I⁻¹'}},
    "MAGNETIC_FLUX_DENSITY": {'description': 'Magnetic flux per unit area', 'meaning': 'quantitykind:MagneticFluxDensity', 'annotations': {'dimension': 'M·T⁻²·I⁻¹'}},
    "HEAT_CAPACITY": {'description': 'Heat required to raise temperature by one unit', 'meaning': 'quantitykind:HeatCapacity', 'annotations': {'dimension': 'M·L²·T⁻²·Θ⁻¹'}},
    "SPECIFIC_HEAT_CAPACITY": {'description': 'Heat capacity per unit mass', 'meaning': 'quantitykind:SpecificHeatCapacity', 'annotations': {'dimension': 'L²·T⁻²·Θ⁻¹'}},
    "THERMAL_CONDUCTIVITY": {'description': 'Ability to conduct heat', 'meaning': 'quantitykind:ThermalConductivity', 'annotations': {'dimension': 'M·L·T⁻³·Θ⁻¹', 'pato_label': 'heat conductivity'}},
    "LUMINOUS_FLUX": {'description': 'Total perceived light power emitted', 'meaning': 'quantitykind:LuminousFlux', 'annotations': {'dimension': 'J'}},
    "ILLUMINANCE": {'description': 'Luminous flux per unit area', 'meaning': 'quantitykind:Illuminance', 'annotations': {'dimension': 'J·L⁻²'}},
    "RADIANT_INTENSITY": {'description': 'Radiant power per unit solid angle', 'meaning': 'quantitykind:RadiantIntensity', 'annotations': {'dimension': 'M·L²·T⁻³'}},
    "ACTIVITY": {'description': 'Number of nuclear disintegrations per unit time', 'meaning': 'quantitykind:Activity', 'annotations': {'dimension': 'T⁻¹'}},
    "ABSORBED_DOSE": {'description': 'Energy deposited per unit mass by ionizing radiation', 'meaning': 'quantitykind:AbsorbedDose', 'annotations': {'dimension': 'L²·T⁻²'}},
    "DOSE_EQUIVALENT": {'description': 'Absorbed dose weighted by radiation type', 'meaning': 'quantitykind:DoseEquivalent', 'annotations': {'dimension': 'L²·T⁻²'}},
    "INFORMATION_ENTROPY": {'description': 'Measure of information content or uncertainty', 'meaning': 'quantitykind:InformationEntropy', 'annotations': {'dimension': 'dimensionless'}},
    "DATA_RATE": {'description': 'Amount of data transferred per unit time', 'meaning': 'quantitykind:DataRate', 'annotations': {'dimension': 'T⁻¹'}},
}

__all__ = [
    "QuantityKindEnum",
]