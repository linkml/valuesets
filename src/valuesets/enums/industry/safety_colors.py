"""
Safety and Warning Color Value Sets

Color value sets for safety, warning, and signaling purposes based on international standards like ANSI, ISO, and OSHA.


Generated from: industry/safety_colors.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class SafetyColorEnum(RichEnum):
    """
    ANSI/ISO standard safety colors
    """
    # Enum members
    SAFETY_RED = "SAFETY_RED"
    SAFETY_ORANGE = "SAFETY_ORANGE"
    SAFETY_YELLOW = "SAFETY_YELLOW"
    SAFETY_GREEN = "SAFETY_GREEN"
    SAFETY_BLUE = "SAFETY_BLUE"
    SAFETY_PURPLE = "SAFETY_PURPLE"
    SAFETY_BLACK = "SAFETY_BLACK"
    SAFETY_WHITE = "SAFETY_WHITE"
    SAFETY_GRAY = "SAFETY_GRAY"
    SAFETY_BROWN = "SAFETY_BROWN"

# Set metadata after class creation
SafetyColorEnum._metadata = {
    "SAFETY_RED": {'description': 'Safety red - danger, stop, prohibition', 'meaning': 'HEX:C8102E', 'annotations': {'standard': 'ANSI Z535.1', 'pantone': 'PMS 186 C', 'usage': 'fire equipment, stop signs, danger signs'}},
    "SAFETY_ORANGE": {'description': 'Safety orange - warning of dangerous parts', 'meaning': 'HEX:FF6900', 'annotations': {'standard': 'ANSI Z535.1', 'pantone': 'PMS 151 C', 'usage': 'machine parts, exposed edges'}},
    "SAFETY_YELLOW": {'description': 'Safety yellow - caution, physical hazards', 'meaning': 'HEX:F6D04D', 'annotations': {'standard': 'ANSI Z535.1', 'pantone': 'PMS 116 C', 'usage': 'caution signs, physical hazards, stumbling'}},
    "SAFETY_GREEN": {'description': 'Safety green - safety, first aid, emergency egress', 'meaning': 'HEX:00843D', 'annotations': {'standard': 'ANSI Z535.1', 'pantone': 'PMS 355 C', 'usage': 'first aid, safety equipment, emergency exits'}},
    "SAFETY_BLUE": {'description': 'Safety blue - mandatory, information', 'meaning': 'HEX:005EB8', 'annotations': {'standard': 'ANSI Z535.1', 'pantone': 'PMS 285 C', 'usage': 'mandatory signs, information signs'}},
    "SAFETY_PURPLE": {'description': 'Safety purple - radiation hazards', 'meaning': 'HEX:652D90', 'annotations': {'standard': 'ANSI Z535.1', 'pantone': 'PMS 2685 C', 'usage': 'radiation hazards, x-ray equipment'}},
    "SAFETY_BLACK": {'description': 'Safety black - traffic/housekeeping markings', 'meaning': 'HEX:000000', 'annotations': {'standard': 'ANSI Z535.1', 'usage': 'traffic control, housekeeping markers'}},
    "SAFETY_WHITE": {'description': 'Safety white - traffic/housekeeping markings', 'meaning': 'HEX:FFFFFF', 'annotations': {'standard': 'ANSI Z535.1', 'usage': 'traffic lanes, housekeeping boundaries'}},
    "SAFETY_GRAY": {'description': 'Safety gray - inactive/out of service', 'meaning': 'HEX:919191', 'annotations': {'standard': 'ANSI Z535.1', 'usage': 'out of service equipment'}},
    "SAFETY_BROWN": {'description': 'Safety brown - no special hazard (background)', 'meaning': 'HEX:795548', 'annotations': {'usage': 'background color for signs'}},
}

class TrafficLightColorEnum(RichEnum):
    """
    Traffic signal colors (international)
    """
    # Enum members
    RED = "RED"
    AMBER = "AMBER"
    GREEN = "GREEN"
    FLASHING_RED = "FLASHING_RED"
    FLASHING_AMBER = "FLASHING_AMBER"
    WHITE = "WHITE"

# Set metadata after class creation
TrafficLightColorEnum._metadata = {
    "RED": {'description': 'Red - stop', 'meaning': 'HEX:FF0000', 'annotations': {'wavelength': '630-700 nm', 'meaning_universal': 'stop, do not proceed'}},
    "AMBER": {'description': 'Amber/yellow - caution', 'meaning': 'HEX:FFBF00', 'annotations': {'wavelength': '590 nm', 'meaning_universal': 'prepare to stop, caution'}},
    "GREEN": {'description': 'Green - go', 'meaning': 'HEX:00FF00', 'annotations': {'wavelength': '510-570 nm', 'meaning_universal': 'proceed, safe to go'}},
    "FLASHING_RED": {'description': 'Flashing red - stop then proceed', 'meaning': 'HEX:FF0000', 'annotations': {'pattern': 'flashing', 'meaning_universal': 'stop, then proceed when safe'}},
    "FLASHING_AMBER": {'description': 'Flashing amber - proceed with caution', 'meaning': 'HEX:FFBF00', 'annotations': {'pattern': 'flashing', 'meaning_universal': 'proceed with caution'}},
    "WHITE": {'description': 'White - special situations (transit)', 'meaning': 'HEX:FFFFFF', 'annotations': {'usage': 'transit priority signals'}},
}

class HazmatColorEnum(RichEnum):
    """
    Hazardous materials placarding colors (DOT/UN)
    """
    # Enum members
    ORANGE = "ORANGE"
    RED = "RED"
    GREEN = "GREEN"
    YELLOW = "YELLOW"
    WHITE = "WHITE"
    BLACK_WHITE_STRIPES = "BLACK_WHITE_STRIPES"
    BLUE = "BLUE"
    WHITE_RED_STRIPES = "WHITE_RED_STRIPES"

# Set metadata after class creation
HazmatColorEnum._metadata = {
    "ORANGE": {'description': 'Orange - explosives (Class 1)', 'meaning': 'HEX:FF6600', 'annotations': {'class': '1', 'hazard': 'explosives'}},
    "RED": {'description': 'Red - flammable (Classes 2.1, 3)', 'meaning': 'HEX:FF0000', 'annotations': {'class': '2.1, 3', 'hazard': 'flammable gas, flammable liquid'}},
    "GREEN": {'description': 'Green - non-flammable gas (Class 2.2)', 'meaning': 'HEX:00FF00', 'annotations': {'class': '2.2', 'hazard': 'non-flammable gas'}},
    "YELLOW": {'description': 'Yellow - oxidizer, organic peroxide (Classes 5.1, 5.2)', 'meaning': 'HEX:FFFF00', 'annotations': {'class': '5.1, 5.2', 'hazard': 'oxidizing substances, organic peroxides'}},
    "WHITE": {'description': 'White - poison/toxic (Class 6.1)', 'meaning': 'HEX:FFFFFF', 'annotations': {'class': '6.1', 'hazard': 'toxic/poisonous substances'}},
    "BLACK_WHITE_STRIPES": {'description': 'Black and white stripes - corrosive (Class 8)', 'annotations': {'class': '8', 'hazard': 'corrosive substances', 'pattern': 'black and white vertical stripes'}},
    "BLUE": {'description': 'Blue - dangerous when wet (Class 4.3)', 'meaning': 'HEX:0000FF', 'annotations': {'class': '4.3', 'hazard': 'dangerous when wet'}},
    "WHITE_RED_STRIPES": {'description': 'White with red stripes - flammable solid (Class 4.1)', 'annotations': {'class': '4.1', 'hazard': 'flammable solid', 'pattern': 'white with red vertical stripes'}},
}

class FireSafetyColorEnum(RichEnum):
    """
    Fire safety equipment and signage colors
    """
    # Enum members
    FIRE_RED = "FIRE_RED"
    PHOTOLUMINESCENT_GREEN = "PHOTOLUMINESCENT_GREEN"
    YELLOW_BLACK_STRIPES = "YELLOW_BLACK_STRIPES"
    WHITE = "WHITE"
    BLUE = "BLUE"

# Set metadata after class creation
FireSafetyColorEnum._metadata = {
    "FIRE_RED": {'description': 'Fire red - fire equipment', 'meaning': 'HEX:C8102E', 'annotations': {'usage': 'fire extinguishers, alarms, hose reels', 'standard': 'ISO 7010'}},
    "PHOTOLUMINESCENT_GREEN": {'description': 'Photoluminescent green - emergency escape', 'meaning': 'HEX:7FFF00', 'annotations': {'usage': 'emergency exit signs, escape routes', 'property': 'glows in dark'}},
    "YELLOW_BLACK_STRIPES": {'description': 'Yellow with black stripes - fire hazard area', 'annotations': {'pattern': 'diagonal stripes', 'usage': 'fire hazard zones'}},
    "WHITE": {'description': 'White - fire protection water', 'meaning': 'HEX:FFFFFF', 'annotations': {'usage': 'water for fire protection'}},
    "BLUE": {'description': 'Blue - mandatory fire safety', 'meaning': 'HEX:005EB8', 'annotations': {'usage': 'mandatory fire safety equipment'}},
}

class MaritimeSignalColorEnum(RichEnum):
    """
    Maritime signal and navigation colors
    """
    # Enum members
    PORT_RED = "PORT_RED"
    STARBOARD_GREEN = "STARBOARD_GREEN"
    STERN_WHITE = "STERN_WHITE"
    MASTHEAD_WHITE = "MASTHEAD_WHITE"
    ALL_ROUND_WHITE = "ALL_ROUND_WHITE"
    YELLOW_TOWING = "YELLOW_TOWING"
    BLUE_FLASHING = "BLUE_FLASHING"

# Set metadata after class creation
MaritimeSignalColorEnum._metadata = {
    "PORT_RED": {'description': 'Port (left) red light', 'meaning': 'HEX:FF0000', 'annotations': {'side': 'port (left)', 'wavelength': '625-740 nm'}},
    "STARBOARD_GREEN": {'description': 'Starboard (right) green light', 'meaning': 'HEX:00FF00', 'annotations': {'side': 'starboard (right)', 'wavelength': '500-565 nm'}},
    "STERN_WHITE": {'description': 'Stern white light', 'meaning': 'HEX:FFFFFF', 'annotations': {'position': 'stern (rear)'}},
    "MASTHEAD_WHITE": {'description': 'Masthead white light', 'meaning': 'HEX:FFFFFF', 'annotations': {'position': 'masthead (forward)'}},
    "ALL_ROUND_WHITE": {'description': 'All-round white light', 'meaning': 'HEX:FFFFFF', 'annotations': {'visibility': '360 degrees'}},
    "YELLOW_TOWING": {'description': 'Yellow towing light', 'meaning': 'HEX:FFFF00', 'annotations': {'usage': 'vessel towing'}},
    "BLUE_FLASHING": {'description': 'Blue flashing light', 'meaning': 'HEX:0000FF', 'annotations': {'usage': 'law enforcement vessels', 'pattern': 'flashing'}},
}

class AviationLightColorEnum(RichEnum):
    """
    Aviation lighting colors
    """
    # Enum members
    RED_BEACON = "RED_BEACON"
    WHITE_STROBE = "WHITE_STROBE"
    GREEN_NAVIGATION = "GREEN_NAVIGATION"
    RED_NAVIGATION = "RED_NAVIGATION"
    WHITE_NAVIGATION = "WHITE_NAVIGATION"
    BLUE_TAXIWAY = "BLUE_TAXIWAY"
    YELLOW_RUNWAY = "YELLOW_RUNWAY"
    GREEN_THRESHOLD = "GREEN_THRESHOLD"
    RED_RUNWAY_END = "RED_RUNWAY_END"

# Set metadata after class creation
AviationLightColorEnum._metadata = {
    "RED_BEACON": {'description': 'Red obstruction light', 'meaning': 'HEX:FF0000', 'annotations': {'usage': 'obstruction marking', 'intensity': 'high intensity'}},
    "WHITE_STROBE": {'description': 'White anti-collision strobe', 'meaning': 'HEX:FFFFFF', 'annotations': {'usage': 'anti-collision', 'pattern': 'strobe'}},
    "GREEN_NAVIGATION": {'description': 'Green navigation light (right wing)', 'meaning': 'HEX:00FF00', 'annotations': {'position': 'right wing tip'}},
    "RED_NAVIGATION": {'description': 'Red navigation light (left wing)', 'meaning': 'HEX:FF0000', 'annotations': {'position': 'left wing tip'}},
    "WHITE_NAVIGATION": {'description': 'White navigation light (tail)', 'meaning': 'HEX:FFFFFF', 'annotations': {'position': 'tail'}},
    "BLUE_TAXIWAY": {'description': 'Blue taxiway edge lights', 'meaning': 'HEX:0000FF', 'annotations': {'usage': 'taxiway edges'}},
    "YELLOW_RUNWAY": {'description': 'Yellow runway markings', 'meaning': 'HEX:FFFF00', 'annotations': {'usage': 'runway centerline, hold positions'}},
    "GREEN_THRESHOLD": {'description': 'Green runway threshold lights', 'meaning': 'HEX:00FF00', 'annotations': {'usage': 'runway threshold'}},
    "RED_RUNWAY_END": {'description': 'Red runway end lights', 'meaning': 'HEX:FF0000', 'annotations': {'usage': 'runway end'}},
}

class ElectricalWireColorEnum(RichEnum):
    """
    Electrical wire color codes (US/International)
    """
    # Enum members
    BLACK_HOT = "BLACK_HOT"
    RED_HOT = "RED_HOT"
    BLUE_HOT = "BLUE_HOT"
    WHITE_NEUTRAL = "WHITE_NEUTRAL"
    GREEN_GROUND = "GREEN_GROUND"
    GREEN_YELLOW_GROUND = "GREEN_YELLOW_GROUND"
    BROWN_LIVE = "BROWN_LIVE"
    BLUE_NEUTRAL = "BLUE_NEUTRAL"
    GRAY_NEUTRAL = "GRAY_NEUTRAL"

# Set metadata after class creation
ElectricalWireColorEnum._metadata = {
    "BLACK_HOT": {'description': 'Black - hot/live wire (US)', 'meaning': 'HEX:000000', 'annotations': {'voltage': '120/240V', 'region': 'North America'}},
    "RED_HOT": {'description': 'Red - hot/live wire (US secondary)', 'meaning': 'HEX:FF0000', 'annotations': {'voltage': '120/240V', 'region': 'North America'}},
    "BLUE_HOT": {'description': 'Blue - hot/live wire (US tertiary)', 'meaning': 'HEX:0000FF', 'annotations': {'voltage': '120/240V', 'region': 'North America'}},
    "WHITE_NEUTRAL": {'description': 'White - neutral wire (US)', 'meaning': 'HEX:FFFFFF', 'annotations': {'function': 'neutral', 'region': 'North America'}},
    "GREEN_GROUND": {'description': 'Green - ground/earth wire', 'meaning': 'HEX:00FF00', 'annotations': {'function': 'ground/earth', 'region': 'universal'}},
    "GREEN_YELLOW_GROUND": {'description': 'Green with yellow stripe - ground/earth (International)', 'annotations': {'function': 'ground/earth', 'region': 'IEC standard', 'pattern': 'green with yellow stripe'}},
    "BROWN_LIVE": {'description': 'Brown - live wire (EU/IEC)', 'meaning': 'HEX:964B00', 'annotations': {'voltage': '230V', 'region': 'Europe/IEC'}},
    "BLUE_NEUTRAL": {'description': 'Blue - neutral wire (EU/IEC)', 'meaning': 'HEX:0000FF', 'annotations': {'function': 'neutral', 'region': 'Europe/IEC'}},
    "GRAY_NEUTRAL": {'description': 'Gray - neutral wire (alternative)', 'meaning': 'HEX:808080', 'annotations': {'function': 'neutral', 'region': 'some installations'}},
}

__all__ = [
    "SafetyColorEnum",
    "TrafficLightColorEnum",
    "HazmatColorEnum",
    "FireSafetyColorEnum",
    "MaritimeSignalColorEnum",
    "AviationLightColorEnum",
    "ElectricalWireColorEnum",
]