"""
Units and Measurements Value Sets

Value sets for units of measurement including length, mass, volume, temperature, and other physical quantities following SI and common standards.


Generated from: units/measurements.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class LengthUnitEnum(RichEnum):
    """
    Units of length/distance measurement
    """
    # Enum members
    METER = "METER"
    KILOMETER = "KILOMETER"
    CENTIMETER = "CENTIMETER"
    MILLIMETER = "MILLIMETER"
    MICROMETER = "MICROMETER"
    NANOMETER = "NANOMETER"
    ANGSTROM = "ANGSTROM"
    INCH = "INCH"
    FOOT = "FOOT"
    YARD = "YARD"
    MILE = "MILE"
    NAUTICAL_MILE = "NAUTICAL_MILE"

# Set metadata after class creation
LengthUnitEnum._metadata = {
    "METER": {'description': 'Meter (SI base unit)', 'meaning': 'UO:0000008', 'annotations': {'symbol': 'm', 'system': 'SI'}},
    "KILOMETER": {'description': 'Kilometer (1000 meters)', 'meaning': 'UO:0010066', 'annotations': {'symbol': 'km', 'conversion_to_meter': '1000'}},
    "CENTIMETER": {'description': 'Centimeter (0.01 meter)', 'meaning': 'UO:0000015', 'annotations': {'symbol': 'cm', 'conversion_to_meter': '0.01'}},
    "MILLIMETER": {'description': 'Millimeter (0.001 meter)', 'meaning': 'UO:0000016', 'annotations': {'symbol': 'mm', 'conversion_to_meter': '0.001'}},
    "MICROMETER": {'description': 'Micrometer/micron (10^-6 meter)', 'meaning': 'UO:0000017', 'annotations': {'symbol': 'μm', 'conversion_to_meter': '1e-6'}},
    "NANOMETER": {'description': 'Nanometer (10^-9 meter)', 'meaning': 'UO:0000018', 'annotations': {'symbol': 'nm', 'conversion_to_meter': '1e-9'}},
    "ANGSTROM": {'description': 'Angstrom (10^-10 meter)', 'meaning': 'UO:0000019', 'annotations': {'symbol': 'Å', 'conversion_to_meter': '1e-10'}},
    "INCH": {'description': 'Inch (imperial)', 'meaning': 'UO:0010011', 'annotations': {'symbol': 'in', 'conversion_to_meter': '0.0254', 'system': 'imperial'}},
    "FOOT": {'description': 'Foot (imperial)', 'meaning': 'UO:0010013', 'annotations': {'symbol': 'ft', 'conversion_to_meter': '0.3048', 'system': 'imperial'}},
    "YARD": {'description': 'Yard (imperial)', 'meaning': 'UO:0010014', 'annotations': {'symbol': 'yd', 'conversion_to_meter': '0.9144', 'system': 'imperial'}},
    "MILE": {'description': 'Mile (imperial)', 'meaning': 'UO:0010017', 'annotations': {'symbol': 'mi', 'conversion_to_meter': '1609.344', 'system': 'imperial'}},
    "NAUTICAL_MILE": {'description': 'Nautical mile', 'meaning': 'UO:0010022', 'annotations': {'symbol': 'nmi', 'conversion_to_meter': '1852'}},
}

class MassUnitEnum(RichEnum):
    """
    Units of mass measurement
    """
    # Enum members
    KILOGRAM = "KILOGRAM"
    GRAM = "GRAM"
    MILLIGRAM = "MILLIGRAM"
    MICROGRAM = "MICROGRAM"
    NANOGRAM = "NANOGRAM"
    METRIC_TON = "METRIC_TON"
    POUND = "POUND"
    OUNCE = "OUNCE"
    STONE = "STONE"
    DALTON = "DALTON"

# Set metadata after class creation
MassUnitEnum._metadata = {
    "KILOGRAM": {'description': 'Kilogram (SI base unit)', 'meaning': 'UO:0000009', 'annotations': {'symbol': 'kg', 'system': 'SI'}},
    "GRAM": {'description': 'Gram (0.001 kilogram)', 'meaning': 'UO:0000021', 'annotations': {'symbol': 'g', 'conversion_to_kg': '0.001'}},
    "MILLIGRAM": {'description': 'Milligram (10^-6 kilogram)', 'meaning': 'UO:0000022', 'annotations': {'symbol': 'mg', 'conversion_to_kg': '1e-6'}},
    "MICROGRAM": {'description': 'Microgram (10^-9 kilogram)', 'meaning': 'UO:0000023', 'annotations': {'symbol': 'μg', 'conversion_to_kg': '1e-9'}},
    "NANOGRAM": {'description': 'Nanogram (10^-12 kilogram)', 'meaning': 'UO:0000024', 'annotations': {'symbol': 'ng', 'conversion_to_kg': '1e-12'}},
    "METRIC_TON": {'description': 'Metric ton/tonne (1000 kilograms)', 'meaning': 'UO:0010038', 'annotations': {'symbol': 't', 'conversion_to_kg': '1000'}, 'aliases': ['ton']},
    "POUND": {'description': 'Pound (imperial)', 'meaning': 'UO:0010034', 'annotations': {'symbol': 'lb', 'conversion_to_kg': '0.453592', 'system': 'imperial'}},
    "OUNCE": {'description': 'Ounce (imperial)', 'meaning': 'UO:0010033', 'annotations': {'symbol': 'oz', 'conversion_to_kg': '0.0283495', 'system': 'imperial'}},
    "STONE": {'description': 'Stone (imperial)', 'meaning': 'UO:0010035', 'annotations': {'symbol': 'st', 'conversion_to_kg': '6.35029', 'system': 'imperial'}},
    "DALTON": {'description': 'Dalton/atomic mass unit', 'meaning': 'UO:0000221', 'annotations': {'symbol': 'Da', 'conversion_to_kg': '1.66054e-27', 'use': 'molecular mass'}},
}

class VolumeUnitEnum(RichEnum):
    """
    Units of volume measurement
    """
    # Enum members
    LITER = "LITER"
    MILLILITER = "MILLILITER"
    MICROLITER = "MICROLITER"
    CUBIC_METER = "CUBIC_METER"
    CUBIC_CENTIMETER = "CUBIC_CENTIMETER"
    GALLON_US = "GALLON_US"
    GALLON_UK = "GALLON_UK"
    FLUID_OUNCE_US = "FLUID_OUNCE_US"
    PINT_US = "PINT_US"
    QUART_US = "QUART_US"
    CUP_US = "CUP_US"
    TABLESPOON = "TABLESPOON"
    TEASPOON = "TEASPOON"

# Set metadata after class creation
VolumeUnitEnum._metadata = {
    "LITER": {'description': 'Liter (SI derived)', 'meaning': 'UO:0000099', 'annotations': {'symbol': 'L', 'conversion_to_m3': '0.001'}},
    "MILLILITER": {'description': 'Milliliter (0.001 liter)', 'meaning': 'UO:0000098', 'annotations': {'symbol': 'mL', 'conversion_to_m3': '1e-6'}},
    "MICROLITER": {'description': 'Microliter (10^-6 liter)', 'meaning': 'UO:0000101', 'annotations': {'symbol': 'μL', 'conversion_to_m3': '1e-9'}},
    "CUBIC_METER": {'description': 'Cubic meter (SI derived)', 'meaning': 'UO:0000096', 'annotations': {'symbol': 'm³', 'system': 'SI'}},
    "CUBIC_CENTIMETER": {'description': 'Cubic centimeter', 'meaning': 'UO:0000097', 'annotations': {'symbol': 'cm³', 'conversion_to_m3': '1e-6'}},
    "GALLON_US": {'description': 'US gallon', 'annotations': {'symbol': 'gal', 'conversion_to_m3': '0.00378541', 'system': 'US'}},
    "GALLON_UK": {'description': 'UK/Imperial gallon', 'meaning': 'UO:0010030', 'annotations': {'symbol': 'gal', 'conversion_to_m3': '0.00454609', 'system': 'imperial'}, 'aliases': ['imperial gallon']},
    "FLUID_OUNCE_US": {'description': 'US fluid ounce', 'meaning': 'UO:0010026', 'annotations': {'symbol': 'fl oz', 'conversion_to_m3': '2.95735e-5', 'system': 'US'}, 'aliases': ['imperial fluid ounce']},
    "PINT_US": {'description': 'US pint', 'meaning': 'UO:0010028', 'annotations': {'symbol': 'pt', 'conversion_to_m3': '0.000473176', 'system': 'US'}, 'aliases': ['imperial pint']},
    "QUART_US": {'description': 'US quart', 'meaning': 'UO:0010029', 'annotations': {'symbol': 'qt', 'conversion_to_m3': '0.000946353', 'system': 'US'}, 'aliases': ['imperial quart']},
    "CUP_US": {'description': 'US cup', 'meaning': 'UO:0010046', 'annotations': {'symbol': 'cup', 'conversion_to_m3': '0.000236588', 'system': 'US'}},
    "TABLESPOON": {'description': 'Tablespoon', 'meaning': 'UO:0010044', 'annotations': {'symbol': 'tbsp', 'conversion_to_m3': '1.47868e-5'}},
    "TEASPOON": {'description': 'Teaspoon', 'meaning': 'UO:0010041', 'annotations': {'symbol': 'tsp', 'conversion_to_m3': '4.92892e-6'}},
}

class TemperatureUnitEnum(RichEnum):
    """
    Units of temperature measurement
    """
    # Enum members
    KELVIN = "KELVIN"
    CELSIUS = "CELSIUS"
    FAHRENHEIT = "FAHRENHEIT"
    RANKINE = "RANKINE"

# Set metadata after class creation
TemperatureUnitEnum._metadata = {
    "KELVIN": {'description': 'Kelvin (SI base unit)', 'meaning': 'UO:0000012', 'annotations': {'symbol': 'K', 'system': 'SI', 'absolute': 'true'}},
    "CELSIUS": {'description': 'Celsius/Centigrade', 'meaning': 'UO:0000027', 'annotations': {'symbol': '°C', 'conversion': 'K - 273.15'}},
    "FAHRENHEIT": {'description': 'Fahrenheit', 'meaning': 'UO:0000195', 'annotations': {'symbol': '°F', 'conversion': '(K - 273.15) * 9/5 + 32', 'system': 'imperial'}},
    "RANKINE": {'description': 'Rankine', 'annotations': {'symbol': '°R', 'conversion': 'K * 9/5', 'absolute': 'true'}},
}

class TimeUnitEnum(RichEnum):
    """
    Units of time measurement
    """
    # Enum members
    SECOND = "SECOND"
    MILLISECOND = "MILLISECOND"
    MICROSECOND = "MICROSECOND"
    NANOSECOND = "NANOSECOND"
    MINUTE = "MINUTE"
    HOUR = "HOUR"
    DAY = "DAY"
    WEEK = "WEEK"
    MONTH = "MONTH"
    YEAR = "YEAR"

# Set metadata after class creation
TimeUnitEnum._metadata = {
    "SECOND": {'description': 'Second (SI base unit)', 'meaning': 'UO:0000010', 'annotations': {'symbol': 's', 'system': 'SI'}},
    "MILLISECOND": {'description': 'Millisecond (0.001 second)', 'meaning': 'UO:0000028', 'annotations': {'symbol': 'ms', 'conversion_to_second': '0.001'}},
    "MICROSECOND": {'description': 'Microsecond (10^-6 second)', 'meaning': 'UO:0000029', 'annotations': {'symbol': 'μs', 'conversion_to_second': '1e-6'}},
    "NANOSECOND": {'description': 'Nanosecond (10^-9 second)', 'meaning': 'UO:0000150', 'annotations': {'symbol': 'ns', 'conversion_to_second': '1e-9'}},
    "MINUTE": {'description': 'Minute (60 seconds)', 'meaning': 'UO:0000031', 'annotations': {'symbol': 'min', 'conversion_to_second': '60'}},
    "HOUR": {'description': 'Hour (3600 seconds)', 'meaning': 'UO:0000032', 'annotations': {'symbol': 'h', 'conversion_to_second': '3600'}},
    "DAY": {'description': 'Day (86400 seconds)', 'meaning': 'UO:0000033', 'annotations': {'symbol': 'd', 'conversion_to_second': '86400'}},
    "WEEK": {'description': 'Week (7 days)', 'meaning': 'UO:0000034', 'annotations': {'symbol': 'wk', 'conversion_to_second': '604800'}},
    "MONTH": {'description': 'Month (approximately 30 days)', 'meaning': 'UO:0000035', 'annotations': {'symbol': 'mo', 'conversion_to_second': '2592000', 'note': 'approximate, varies by month'}},
    "YEAR": {'description': 'Year (365.25 days)', 'meaning': 'UO:0000036', 'annotations': {'symbol': 'yr', 'conversion_to_second': '31557600', 'note': 'accounts for leap years'}},
}

class PressureUnitEnum(RichEnum):
    """
    Units of pressure measurement
    """
    # Enum members
    PASCAL = "PASCAL"
    KILOPASCAL = "KILOPASCAL"
    MEGAPASCAL = "MEGAPASCAL"
    BAR = "BAR"
    MILLIBAR = "MILLIBAR"
    ATMOSPHERE = "ATMOSPHERE"
    TORR = "TORR"
    PSI = "PSI"
    MM_HG = "MM_HG"

# Set metadata after class creation
PressureUnitEnum._metadata = {
    "PASCAL": {'description': 'Pascal (SI derived unit)', 'meaning': 'UO:0000110', 'annotations': {'symbol': 'Pa', 'system': 'SI', 'definition': 'N/m²'}},
    "KILOPASCAL": {'description': 'Kilopascal (1000 pascals)', 'annotations': {'symbol': 'kPa', 'conversion_to_pascal': '1000'}},
    "MEGAPASCAL": {'description': 'Megapascal (10^6 pascals)', 'annotations': {'symbol': 'MPa', 'conversion_to_pascal': '1e6'}},
    "BAR": {'description': 'Bar', 'annotations': {'symbol': 'bar', 'conversion_to_pascal': '100000'}},
    "MILLIBAR": {'description': 'Millibar', 'annotations': {'symbol': 'mbar', 'conversion_to_pascal': '100'}},
    "ATMOSPHERE": {'description': 'Standard atmosphere', 'annotations': {'symbol': 'atm', 'conversion_to_pascal': '101325'}},
    "TORR": {'description': 'Torr (millimeter of mercury)', 'annotations': {'symbol': 'Torr', 'conversion_to_pascal': '133.322'}},
    "PSI": {'description': 'Pounds per square inch', 'meaning': 'UO:0010052', 'annotations': {'symbol': 'psi', 'conversion_to_pascal': '6894.76', 'system': 'imperial'}, 'aliases': ['pound-force per square inch']},
    "MM_HG": {'description': 'Millimeters of mercury', 'meaning': 'UO:0000272', 'annotations': {'symbol': 'mmHg', 'conversion_to_pascal': '133.322', 'use': 'medical blood pressure'}},
}

class ConcentrationUnitEnum(RichEnum):
    """
    Units of concentration measurement
    """
    # Enum members
    MOLAR = "MOLAR"
    MILLIMOLAR = "MILLIMOLAR"
    MICROMOLAR = "MICROMOLAR"
    NANOMOLAR = "NANOMOLAR"
    PICOMOLAR = "PICOMOLAR"
    MG_PER_ML = "MG_PER_ML"
    UG_PER_ML = "UG_PER_ML"
    NG_PER_ML = "NG_PER_ML"
    PERCENT = "PERCENT"
    PPM = "PPM"
    PPB = "PPB"

# Set metadata after class creation
ConcentrationUnitEnum._metadata = {
    "MOLAR": {'description': 'Molar (moles per liter)', 'meaning': 'UO:0000062', 'annotations': {'symbol': 'M', 'definition': 'mol/L'}},
    "MILLIMOLAR": {'description': 'Millimolar (10^-3 molar)', 'meaning': 'UO:0000063', 'annotations': {'symbol': 'mM', 'conversion_to_molar': '0.001'}},
    "MICROMOLAR": {'description': 'Micromolar (10^-6 molar)', 'meaning': 'UO:0000064', 'annotations': {'symbol': 'μM', 'conversion_to_molar': '1e-6'}},
    "NANOMOLAR": {'description': 'Nanomolar (10^-9 molar)', 'meaning': 'UO:0000065', 'annotations': {'symbol': 'nM', 'conversion_to_molar': '1e-9'}},
    "PICOMOLAR": {'description': 'Picomolar (10^-12 molar)', 'meaning': 'UO:0000066', 'annotations': {'symbol': 'pM', 'conversion_to_molar': '1e-12'}},
    "MG_PER_ML": {'description': 'Milligrams per milliliter', 'meaning': 'UO:0000176', 'annotations': {'symbol': 'mg/mL'}},
    "UG_PER_ML": {'description': 'Micrograms per milliliter', 'meaning': 'UO:0000274', 'annotations': {'symbol': 'μg/mL'}},
    "NG_PER_ML": {'description': 'Nanograms per milliliter', 'meaning': 'UO:0000275', 'annotations': {'symbol': 'ng/mL'}},
    "PERCENT": {'description': 'Percent (parts per hundred)', 'meaning': 'UO:0000187', 'annotations': {'symbol': '%', 'conversion_to_fraction': '0.01'}},
    "PPM": {'description': 'Parts per million', 'meaning': 'UO:0000169', 'annotations': {'symbol': 'ppm', 'conversion_to_fraction': '1e-6'}},
    "PPB": {'description': 'Parts per billion', 'meaning': 'UO:0000170', 'annotations': {'symbol': 'ppb', 'conversion_to_fraction': '1e-9'}},
}

class FrequencyUnitEnum(RichEnum):
    """
    Units of frequency measurement
    """
    # Enum members
    HERTZ = "HERTZ"
    KILOHERTZ = "KILOHERTZ"
    MEGAHERTZ = "MEGAHERTZ"
    GIGAHERTZ = "GIGAHERTZ"
    RPM = "RPM"
    BPM = "BPM"

# Set metadata after class creation
FrequencyUnitEnum._metadata = {
    "HERTZ": {'description': 'Hertz (cycles per second)', 'meaning': 'UO:0000106', 'annotations': {'symbol': 'Hz', 'system': 'SI'}},
    "KILOHERTZ": {'description': 'Kilohertz (1000 Hz)', 'annotations': {'symbol': 'kHz', 'conversion_to_hz': '1000'}},
    "MEGAHERTZ": {'description': 'Megahertz (10^6 Hz)', 'meaning': 'UO:0000325', 'annotations': {'symbol': 'MHz', 'conversion_to_hz': '1e6'}},
    "GIGAHERTZ": {'description': 'Gigahertz (10^9 Hz)', 'annotations': {'symbol': 'GHz', 'conversion_to_hz': '1e9'}},
    "RPM": {'description': 'Revolutions per minute', 'annotations': {'symbol': 'rpm', 'conversion_to_hz': '0.0166667'}},
    "BPM": {'description': 'Beats per minute', 'annotations': {'symbol': 'bpm', 'conversion_to_hz': '0.0166667', 'use': 'heart rate'}},
}

class AngleUnitEnum(RichEnum):
    """
    Units of angle measurement
    """
    # Enum members
    RADIAN = "RADIAN"
    DEGREE = "DEGREE"
    MINUTE_OF_ARC = "MINUTE_OF_ARC"
    SECOND_OF_ARC = "SECOND_OF_ARC"
    GRADIAN = "GRADIAN"
    TURN = "TURN"

# Set metadata after class creation
AngleUnitEnum._metadata = {
    "RADIAN": {'description': 'Radian (SI derived unit)', 'meaning': 'UO:0000123', 'annotations': {'symbol': 'rad', 'system': 'SI'}},
    "DEGREE": {'description': 'Degree', 'meaning': 'UO:0000185', 'annotations': {'symbol': '°', 'conversion_to_radian': '0.0174533'}},
    "MINUTE_OF_ARC": {'description': 'Minute of arc/arcminute', 'annotations': {'symbol': "'", 'conversion_to_degree': '0.0166667'}},
    "SECOND_OF_ARC": {'description': 'Second of arc/arcsecond', 'annotations': {'symbol': '"', 'conversion_to_degree': '0.000277778'}},
    "GRADIAN": {'description': 'Gradian/gon', 'annotations': {'symbol': 'gon', 'conversion_to_degree': '0.9'}},
    "TURN": {'description': 'Turn/revolution', 'annotations': {'symbol': 'turn', 'conversion_to_radian': '6.28319'}},
}

class DataSizeUnitEnum(RichEnum):
    """
    Units of digital data size
    """
    # Enum members
    BIT = "BIT"
    BYTE = "BYTE"
    KILOBYTE = "KILOBYTE"
    MEGABYTE = "MEGABYTE"
    GIGABYTE = "GIGABYTE"
    TERABYTE = "TERABYTE"
    PETABYTE = "PETABYTE"
    KIBIBYTE = "KIBIBYTE"
    MEBIBYTE = "MEBIBYTE"
    GIBIBYTE = "GIBIBYTE"
    TEBIBYTE = "TEBIBYTE"

# Set metadata after class creation
DataSizeUnitEnum._metadata = {
    "BIT": {'description': 'Bit (binary digit)', 'annotations': {'symbol': 'bit', 'base': 'binary'}},
    "BYTE": {'description': 'Byte (8 bits)', 'meaning': 'UO:0000233', 'annotations': {'symbol': 'B', 'conversion_to_bit': '8'}},
    "KILOBYTE": {'description': 'Kilobyte (1000 bytes)', 'meaning': 'UO:0000234', 'annotations': {'symbol': 'KB', 'conversion_to_byte': '1000', 'standard': 'decimal'}},
    "MEGABYTE": {'description': 'Megabyte (10^6 bytes)', 'meaning': 'UO:0000235', 'annotations': {'symbol': 'MB', 'conversion_to_byte': '1e6', 'standard': 'decimal'}},
    "GIGABYTE": {'description': 'Gigabyte (10^9 bytes)', 'annotations': {'symbol': 'GB', 'conversion_to_byte': '1e9', 'standard': 'decimal'}},
    "TERABYTE": {'description': 'Terabyte (10^12 bytes)', 'annotations': {'symbol': 'TB', 'conversion_to_byte': '1e12', 'standard': 'decimal'}},
    "PETABYTE": {'description': 'Petabyte (10^15 bytes)', 'annotations': {'symbol': 'PB', 'conversion_to_byte': '1e15', 'standard': 'decimal'}},
    "KIBIBYTE": {'description': 'Kibibyte (1024 bytes)', 'annotations': {'symbol': 'KiB', 'conversion_to_byte': '1024', 'standard': 'binary'}},
    "MEBIBYTE": {'description': 'Mebibyte (2^20 bytes)', 'annotations': {'symbol': 'MiB', 'conversion_to_byte': '1048576', 'standard': 'binary'}},
    "GIBIBYTE": {'description': 'Gibibyte (2^30 bytes)', 'annotations': {'symbol': 'GiB', 'conversion_to_byte': '1073741824', 'standard': 'binary'}},
    "TEBIBYTE": {'description': 'Tebibyte (2^40 bytes)', 'annotations': {'symbol': 'TiB', 'conversion_to_byte': '1099511627776', 'standard': 'binary'}},
}

__all__ = [
    "LengthUnitEnum",
    "MassUnitEnum",
    "VolumeUnitEnum",
    "TemperatureUnitEnum",
    "TimeUnitEnum",
    "PressureUnitEnum",
    "ConcentrationUnitEnum",
    "FrequencyUnitEnum",
    "AngleUnitEnum",
    "DataSizeUnitEnum",
]