"""
Color Value Sets

Comprehensive color value sets including basic colors, web colors, X11/Unix colors, and CSS color specifications with hex codes as meanings.


Generated from: visual/colors.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class BasicColorEnum(RichEnum):
    """
    Basic color names commonly used in everyday language
    """
    # Enum members
    RED = "RED"
    GREEN = "GREEN"
    BLUE = "BLUE"
    YELLOW = "YELLOW"
    ORANGE = "ORANGE"
    PURPLE = "PURPLE"
    BLACK = "BLACK"
    WHITE = "WHITE"
    GRAY = "GRAY"
    BROWN = "BROWN"
    PINK = "PINK"
    CYAN = "CYAN"
    MAGENTA = "MAGENTA"

# Set metadata after class creation
BasicColorEnum._metadata = {
    "RED": {'description': 'Primary red color', 'meaning': 'HEX:FF0000', 'annotations': {'wavelength': '700 nm', 'rgb': '255,0,0'}},
    "GREEN": {'description': 'Primary green color', 'meaning': 'HEX:008000', 'annotations': {'wavelength': '550 nm', 'rgb': '0,128,0'}},
    "BLUE": {'description': 'Primary blue color', 'meaning': 'HEX:0000FF', 'annotations': {'wavelength': '450 nm', 'rgb': '0,0,255'}},
    "YELLOW": {'description': 'Secondary yellow color', 'meaning': 'HEX:FFFF00', 'annotations': {'wavelength': '580 nm', 'rgb': '255,255,0'}},
    "ORANGE": {'description': 'Secondary orange color', 'meaning': 'HEX:FFA500', 'annotations': {'wavelength': '600 nm', 'rgb': '255,165,0'}},
    "PURPLE": {'description': 'Secondary purple color', 'meaning': 'HEX:800080', 'annotations': {'wavelength': '420 nm', 'rgb': '128,0,128'}},
    "BLACK": {'description': 'Absence of color', 'meaning': 'HEX:000000', 'annotations': {'rgb': '0,0,0'}},
    "WHITE": {'description': 'All colors combined', 'meaning': 'HEX:FFFFFF', 'annotations': {'rgb': '255,255,255'}},
    "GRAY": {'description': 'Neutral gray', 'meaning': 'HEX:808080', 'annotations': {'rgb': '128,128,128', 'aliases': 'grey'}},
    "BROWN": {'description': 'Brown color', 'meaning': 'HEX:A52A2A', 'annotations': {'rgb': '165,42,42'}},
    "PINK": {'description': 'Light red/pink color', 'meaning': 'HEX:FFC0CB', 'annotations': {'rgb': '255,192,203'}},
    "CYAN": {'description': 'Cyan/aqua color', 'meaning': 'HEX:00FFFF', 'annotations': {'wavelength': '490 nm', 'rgb': '0,255,255'}},
    "MAGENTA": {'description': 'Magenta color', 'meaning': 'HEX:FF00FF', 'annotations': {'rgb': '255,0,255'}},
}

class WebColorEnum(RichEnum):
    """
    Standard HTML/CSS named colors (147 colors)
    """
    # Enum members
    INDIAN_RED = "INDIAN_RED"
    LIGHT_CORAL = "LIGHT_CORAL"
    SALMON = "SALMON"
    DARK_SALMON = "DARK_SALMON"
    CRIMSON = "CRIMSON"
    FIREBRICK = "FIREBRICK"
    DARK_RED = "DARK_RED"
    HOT_PINK = "HOT_PINK"
    DEEP_PINK = "DEEP_PINK"
    LIGHT_PINK = "LIGHT_PINK"
    PALE_VIOLET_RED = "PALE_VIOLET_RED"
    CORAL = "CORAL"
    TOMATO = "TOMATO"
    ORANGE_RED = "ORANGE_RED"
    DARK_ORANGE = "DARK_ORANGE"
    GOLD = "GOLD"
    LIGHT_YELLOW = "LIGHT_YELLOW"
    LEMON_CHIFFON = "LEMON_CHIFFON"
    PAPAYA_WHIP = "PAPAYA_WHIP"
    MOCCASIN = "MOCCASIN"
    PEACH_PUFF = "PEACH_PUFF"
    KHAKI = "KHAKI"
    LAVENDER = "LAVENDER"
    THISTLE = "THISTLE"
    PLUM = "PLUM"
    VIOLET = "VIOLET"
    ORCHID = "ORCHID"
    FUCHSIA = "FUCHSIA"
    MEDIUM_ORCHID = "MEDIUM_ORCHID"
    MEDIUM_PURPLE = "MEDIUM_PURPLE"
    BLUE_VIOLET = "BLUE_VIOLET"
    DARK_VIOLET = "DARK_VIOLET"
    DARK_ORCHID = "DARK_ORCHID"
    DARK_MAGENTA = "DARK_MAGENTA"
    INDIGO = "INDIGO"
    GREEN_YELLOW = "GREEN_YELLOW"
    CHARTREUSE = "CHARTREUSE"
    LAWN_GREEN = "LAWN_GREEN"
    LIME = "LIME"
    LIME_GREEN = "LIME_GREEN"
    PALE_GREEN = "PALE_GREEN"
    LIGHT_GREEN = "LIGHT_GREEN"
    MEDIUM_SPRING_GREEN = "MEDIUM_SPRING_GREEN"
    SPRING_GREEN = "SPRING_GREEN"
    MEDIUM_SEA_GREEN = "MEDIUM_SEA_GREEN"
    SEA_GREEN = "SEA_GREEN"
    FOREST_GREEN = "FOREST_GREEN"
    DARK_GREEN = "DARK_GREEN"
    YELLOW_GREEN = "YELLOW_GREEN"
    OLIVE_DRAB = "OLIVE_DRAB"
    OLIVE = "OLIVE"
    DARK_OLIVE_GREEN = "DARK_OLIVE_GREEN"
    AQUA = "AQUA"
    CYAN = "CYAN"
    LIGHT_CYAN = "LIGHT_CYAN"
    PALE_TURQUOISE = "PALE_TURQUOISE"
    AQUAMARINE = "AQUAMARINE"
    TURQUOISE = "TURQUOISE"
    MEDIUM_TURQUOISE = "MEDIUM_TURQUOISE"
    DARK_TURQUOISE = "DARK_TURQUOISE"
    LIGHT_SEA_GREEN = "LIGHT_SEA_GREEN"
    CADET_BLUE = "CADET_BLUE"
    DARK_CYAN = "DARK_CYAN"
    TEAL = "TEAL"
    LIGHT_STEEL_BLUE = "LIGHT_STEEL_BLUE"
    POWDER_BLUE = "POWDER_BLUE"
    LIGHT_BLUE = "LIGHT_BLUE"
    SKY_BLUE = "SKY_BLUE"
    LIGHT_SKY_BLUE = "LIGHT_SKY_BLUE"
    DEEP_SKY_BLUE = "DEEP_SKY_BLUE"
    DODGER_BLUE = "DODGER_BLUE"
    CORNFLOWER_BLUE = "CORNFLOWER_BLUE"
    STEEL_BLUE = "STEEL_BLUE"
    ROYAL_BLUE = "ROYAL_BLUE"
    MEDIUM_BLUE = "MEDIUM_BLUE"
    DARK_BLUE = "DARK_BLUE"
    NAVY = "NAVY"
    MIDNIGHT_BLUE = "MIDNIGHT_BLUE"
    CORNSILK = "CORNSILK"
    BLANCHED_ALMOND = "BLANCHED_ALMOND"
    BISQUE = "BISQUE"
    NAVAJO_WHITE = "NAVAJO_WHITE"
    WHEAT = "WHEAT"
    BURLYWOOD = "BURLYWOOD"
    TAN = "TAN"
    ROSY_BROWN = "ROSY_BROWN"
    SANDY_BROWN = "SANDY_BROWN"
    GOLDENROD = "GOLDENROD"
    DARK_GOLDENROD = "DARK_GOLDENROD"
    PERU = "PERU"
    CHOCOLATE = "CHOCOLATE"
    SADDLE_BROWN = "SADDLE_BROWN"
    SIENNA = "SIENNA"
    MAROON = "MAROON"
    SNOW = "SNOW"
    HONEYDEW = "HONEYDEW"
    MINT_CREAM = "MINT_CREAM"
    AZURE = "AZURE"
    ALICE_BLUE = "ALICE_BLUE"
    GHOST_WHITE = "GHOST_WHITE"
    WHITE_SMOKE = "WHITE_SMOKE"
    SEASHELL = "SEASHELL"
    BEIGE = "BEIGE"
    OLD_LACE = "OLD_LACE"
    FLORAL_WHITE = "FLORAL_WHITE"
    IVORY = "IVORY"
    ANTIQUE_WHITE = "ANTIQUE_WHITE"
    LINEN = "LINEN"
    LAVENDER_BLUSH = "LAVENDER_BLUSH"
    MISTY_ROSE = "MISTY_ROSE"
    GAINSBORO = "GAINSBORO"
    LIGHT_GRAY = "LIGHT_GRAY"
    SILVER = "SILVER"
    DARK_GRAY = "DARK_GRAY"
    DIM_GRAY = "DIM_GRAY"
    LIGHT_SLATE_GRAY = "LIGHT_SLATE_GRAY"
    SLATE_GRAY = "SLATE_GRAY"
    DARK_SLATE_GRAY = "DARK_SLATE_GRAY"

# Set metadata after class creation
WebColorEnum._metadata = {
    "INDIAN_RED": {'description': 'Indian red', 'meaning': 'HEX:CD5C5C', 'annotations': {'rgb': '205,92,92'}},
    "LIGHT_CORAL": {'description': 'Light coral', 'meaning': 'HEX:F08080', 'annotations': {'rgb': '240,128,128'}},
    "SALMON": {'description': 'Salmon', 'meaning': 'HEX:FA8072', 'annotations': {'rgb': '250,128,114'}},
    "DARK_SALMON": {'description': 'Dark salmon', 'meaning': 'HEX:E9967A', 'annotations': {'rgb': '233,150,122'}},
    "CRIMSON": {'description': 'Crimson', 'meaning': 'HEX:DC143C', 'annotations': {'rgb': '220,20,60'}},
    "FIREBRICK": {'description': 'Firebrick', 'meaning': 'HEX:B22222', 'annotations': {'rgb': '178,34,34'}},
    "DARK_RED": {'description': 'Dark red', 'meaning': 'HEX:8B0000', 'annotations': {'rgb': '139,0,0'}},
    "HOT_PINK": {'description': 'Hot pink', 'meaning': 'HEX:FF69B4', 'annotations': {'rgb': '255,105,180'}},
    "DEEP_PINK": {'description': 'Deep pink', 'meaning': 'HEX:FF1493', 'annotations': {'rgb': '255,20,147'}},
    "LIGHT_PINK": {'description': 'Light pink', 'meaning': 'HEX:FFB6C1', 'annotations': {'rgb': '255,182,193'}},
    "PALE_VIOLET_RED": {'description': 'Pale violet red', 'meaning': 'HEX:DB7093', 'annotations': {'rgb': '219,112,147'}},
    "CORAL": {'description': 'Coral', 'meaning': 'HEX:FF7F50', 'annotations': {'rgb': '255,127,80'}},
    "TOMATO": {'description': 'Tomato', 'meaning': 'HEX:FF6347', 'annotations': {'rgb': '255,99,71'}},
    "ORANGE_RED": {'description': 'Orange red', 'meaning': 'HEX:FF4500', 'annotations': {'rgb': '255,69,0'}},
    "DARK_ORANGE": {'description': 'Dark orange', 'meaning': 'HEX:FF8C00', 'annotations': {'rgb': '255,140,0'}},
    "GOLD": {'description': 'Gold', 'meaning': 'HEX:FFD700', 'annotations': {'rgb': '255,215,0'}},
    "LIGHT_YELLOW": {'description': 'Light yellow', 'meaning': 'HEX:FFFFE0', 'annotations': {'rgb': '255,255,224'}},
    "LEMON_CHIFFON": {'description': 'Lemon chiffon', 'meaning': 'HEX:FFFACD', 'annotations': {'rgb': '255,250,205'}},
    "PAPAYA_WHIP": {'description': 'Papaya whip', 'meaning': 'HEX:FFEFD5', 'annotations': {'rgb': '255,239,213'}},
    "MOCCASIN": {'description': 'Moccasin', 'meaning': 'HEX:FFE4B5', 'annotations': {'rgb': '255,228,181'}},
    "PEACH_PUFF": {'description': 'Peach puff', 'meaning': 'HEX:FFDAB9', 'annotations': {'rgb': '255,218,185'}},
    "KHAKI": {'description': 'Khaki', 'meaning': 'HEX:F0E68C', 'annotations': {'rgb': '240,230,140'}},
    "LAVENDER": {'description': 'Lavender', 'meaning': 'HEX:E6E6FA', 'annotations': {'rgb': '230,230,250'}},
    "THISTLE": {'description': 'Thistle', 'meaning': 'HEX:D8BFD8', 'annotations': {'rgb': '216,191,216'}},
    "PLUM": {'description': 'Plum', 'meaning': 'HEX:DDA0DD', 'annotations': {'rgb': '221,160,221'}},
    "VIOLET": {'description': 'Violet', 'meaning': 'HEX:EE82EE', 'annotations': {'rgb': '238,130,238'}},
    "ORCHID": {'description': 'Orchid', 'meaning': 'HEX:DA70D6', 'annotations': {'rgb': '218,112,214'}},
    "FUCHSIA": {'description': 'Fuchsia', 'meaning': 'HEX:FF00FF', 'annotations': {'rgb': '255,0,255'}},
    "MEDIUM_ORCHID": {'description': 'Medium orchid', 'meaning': 'HEX:BA55D3', 'annotations': {'rgb': '186,85,211'}},
    "MEDIUM_PURPLE": {'description': 'Medium purple', 'meaning': 'HEX:9370DB', 'annotations': {'rgb': '147,112,219'}},
    "BLUE_VIOLET": {'description': 'Blue violet', 'meaning': 'HEX:8A2BE2', 'annotations': {'rgb': '138,43,226'}},
    "DARK_VIOLET": {'description': 'Dark violet', 'meaning': 'HEX:9400D3', 'annotations': {'rgb': '148,0,211'}},
    "DARK_ORCHID": {'description': 'Dark orchid', 'meaning': 'HEX:9932CC', 'annotations': {'rgb': '153,50,204'}},
    "DARK_MAGENTA": {'description': 'Dark magenta', 'meaning': 'HEX:8B008B', 'annotations': {'rgb': '139,0,139'}},
    "INDIGO": {'description': 'Indigo', 'meaning': 'HEX:4B0082', 'annotations': {'rgb': '75,0,130'}},
    "GREEN_YELLOW": {'description': 'Green yellow', 'meaning': 'HEX:ADFF2F', 'annotations': {'rgb': '173,255,47'}},
    "CHARTREUSE": {'description': 'Chartreuse', 'meaning': 'HEX:7FFF00', 'annotations': {'rgb': '127,255,0'}},
    "LAWN_GREEN": {'description': 'Lawn green', 'meaning': 'HEX:7CFC00', 'annotations': {'rgb': '124,252,0'}},
    "LIME": {'description': 'Lime', 'meaning': 'HEX:00FF00', 'annotations': {'rgb': '0,255,0'}},
    "LIME_GREEN": {'description': 'Lime green', 'meaning': 'HEX:32CD32', 'annotations': {'rgb': '50,205,50'}},
    "PALE_GREEN": {'description': 'Pale green', 'meaning': 'HEX:98FB98', 'annotations': {'rgb': '152,251,152'}},
    "LIGHT_GREEN": {'description': 'Light green', 'meaning': 'HEX:90EE90', 'annotations': {'rgb': '144,238,144'}},
    "MEDIUM_SPRING_GREEN": {'description': 'Medium spring green', 'meaning': 'HEX:00FA9A', 'annotations': {'rgb': '0,250,154'}},
    "SPRING_GREEN": {'description': 'Spring green', 'meaning': 'HEX:00FF7F', 'annotations': {'rgb': '0,255,127'}},
    "MEDIUM_SEA_GREEN": {'description': 'Medium sea green', 'meaning': 'HEX:3CB371', 'annotations': {'rgb': '60,179,113'}},
    "SEA_GREEN": {'description': 'Sea green', 'meaning': 'HEX:2E8B57', 'annotations': {'rgb': '46,139,87'}},
    "FOREST_GREEN": {'description': 'Forest green', 'meaning': 'HEX:228B22', 'annotations': {'rgb': '34,139,34'}},
    "DARK_GREEN": {'description': 'Dark green', 'meaning': 'HEX:006400', 'annotations': {'rgb': '0,100,0'}},
    "YELLOW_GREEN": {'description': 'Yellow green', 'meaning': 'HEX:9ACD32', 'annotations': {'rgb': '154,205,50'}},
    "OLIVE_DRAB": {'description': 'Olive drab', 'meaning': 'HEX:6B8E23', 'annotations': {'rgb': '107,142,35'}},
    "OLIVE": {'description': 'Olive', 'meaning': 'HEX:808000', 'annotations': {'rgb': '128,128,0'}},
    "DARK_OLIVE_GREEN": {'description': 'Dark olive green', 'meaning': 'HEX:556B2F', 'annotations': {'rgb': '85,107,47'}},
    "AQUA": {'description': 'Aqua', 'meaning': 'HEX:00FFFF', 'annotations': {'rgb': '0,255,255'}},
    "CYAN": {'description': 'Cyan', 'meaning': 'HEX:00FFFF', 'annotations': {'rgb': '0,255,255'}},
    "LIGHT_CYAN": {'description': 'Light cyan', 'meaning': 'HEX:E0FFFF', 'annotations': {'rgb': '224,255,255'}},
    "PALE_TURQUOISE": {'description': 'Pale turquoise', 'meaning': 'HEX:AFEEEE', 'annotations': {'rgb': '175,238,238'}},
    "AQUAMARINE": {'description': 'Aquamarine', 'meaning': 'HEX:7FFFD4', 'annotations': {'rgb': '127,255,212'}},
    "TURQUOISE": {'description': 'Turquoise', 'meaning': 'HEX:40E0D0', 'annotations': {'rgb': '64,224,208'}},
    "MEDIUM_TURQUOISE": {'description': 'Medium turquoise', 'meaning': 'HEX:48D1CC', 'annotations': {'rgb': '72,209,204'}},
    "DARK_TURQUOISE": {'description': 'Dark turquoise', 'meaning': 'HEX:00CED1', 'annotations': {'rgb': '0,206,209'}},
    "LIGHT_SEA_GREEN": {'description': 'Light sea green', 'meaning': 'HEX:20B2AA', 'annotations': {'rgb': '32,178,170'}},
    "CADET_BLUE": {'description': 'Cadet blue', 'meaning': 'HEX:5F9EA0', 'annotations': {'rgb': '95,158,160'}},
    "DARK_CYAN": {'description': 'Dark cyan', 'meaning': 'HEX:008B8B', 'annotations': {'rgb': '0,139,139'}},
    "TEAL": {'description': 'Teal', 'meaning': 'HEX:008080', 'annotations': {'rgb': '0,128,128'}},
    "LIGHT_STEEL_BLUE": {'description': 'Light steel blue', 'meaning': 'HEX:B0C4DE', 'annotations': {'rgb': '176,196,222'}},
    "POWDER_BLUE": {'description': 'Powder blue', 'meaning': 'HEX:B0E0E6', 'annotations': {'rgb': '176,224,230'}},
    "LIGHT_BLUE": {'description': 'Light blue', 'meaning': 'HEX:ADD8E6', 'annotations': {'rgb': '173,216,230'}},
    "SKY_BLUE": {'description': 'Sky blue', 'meaning': 'HEX:87CEEB', 'annotations': {'rgb': '135,206,235'}},
    "LIGHT_SKY_BLUE": {'description': 'Light sky blue', 'meaning': 'HEX:87CEFA', 'annotations': {'rgb': '135,206,250'}},
    "DEEP_SKY_BLUE": {'description': 'Deep sky blue', 'meaning': 'HEX:00BFFF', 'annotations': {'rgb': '0,191,255'}},
    "DODGER_BLUE": {'description': 'Dodger blue', 'meaning': 'HEX:1E90FF', 'annotations': {'rgb': '30,144,255'}},
    "CORNFLOWER_BLUE": {'description': 'Cornflower blue', 'meaning': 'HEX:6495ED', 'annotations': {'rgb': '100,149,237'}},
    "STEEL_BLUE": {'description': 'Steel blue', 'meaning': 'HEX:4682B4', 'annotations': {'rgb': '70,130,180'}},
    "ROYAL_BLUE": {'description': 'Royal blue', 'meaning': 'HEX:4169E1', 'annotations': {'rgb': '65,105,225'}},
    "MEDIUM_BLUE": {'description': 'Medium blue', 'meaning': 'HEX:0000CD', 'annotations': {'rgb': '0,0,205'}},
    "DARK_BLUE": {'description': 'Dark blue', 'meaning': 'HEX:00008B', 'annotations': {'rgb': '0,0,139'}},
    "NAVY": {'description': 'Navy', 'meaning': 'HEX:000080', 'annotations': {'rgb': '0,0,128'}},
    "MIDNIGHT_BLUE": {'description': 'Midnight blue', 'meaning': 'HEX:191970', 'annotations': {'rgb': '25,25,112'}},
    "CORNSILK": {'description': 'Cornsilk', 'meaning': 'HEX:FFF8DC', 'annotations': {'rgb': '255,248,220'}},
    "BLANCHED_ALMOND": {'description': 'Blanched almond', 'meaning': 'HEX:FFEBCD', 'annotations': {'rgb': '255,235,205'}},
    "BISQUE": {'description': 'Bisque', 'meaning': 'HEX:FFE4C4', 'annotations': {'rgb': '255,228,196'}},
    "NAVAJO_WHITE": {'description': 'Navajo white', 'meaning': 'HEX:FFDEAD', 'annotations': {'rgb': '255,222,173'}},
    "WHEAT": {'description': 'Wheat', 'meaning': 'HEX:F5DEB3', 'annotations': {'rgb': '245,222,179'}},
    "BURLYWOOD": {'description': 'Burlywood', 'meaning': 'HEX:DEB887', 'annotations': {'rgb': '222,184,135'}},
    "TAN": {'description': 'Tan', 'meaning': 'HEX:D2B48C', 'annotations': {'rgb': '210,180,140'}},
    "ROSY_BROWN": {'description': 'Rosy brown', 'meaning': 'HEX:BC8F8F', 'annotations': {'rgb': '188,143,143'}},
    "SANDY_BROWN": {'description': 'Sandy brown', 'meaning': 'HEX:F4A460', 'annotations': {'rgb': '244,164,96'}},
    "GOLDENROD": {'description': 'Goldenrod', 'meaning': 'HEX:DAA520', 'annotations': {'rgb': '218,165,32'}},
    "DARK_GOLDENROD": {'description': 'Dark goldenrod', 'meaning': 'HEX:B8860B', 'annotations': {'rgb': '184,134,11'}},
    "PERU": {'description': 'Peru', 'meaning': 'HEX:CD853F', 'annotations': {'rgb': '205,133,63'}},
    "CHOCOLATE": {'description': 'Chocolate', 'meaning': 'HEX:D2691E', 'annotations': {'rgb': '210,105,30'}},
    "SADDLE_BROWN": {'description': 'Saddle brown', 'meaning': 'HEX:8B4513', 'annotations': {'rgb': '139,69,19'}},
    "SIENNA": {'description': 'Sienna', 'meaning': 'HEX:A0522D', 'annotations': {'rgb': '160,82,45'}},
    "MAROON": {'description': 'Maroon', 'meaning': 'HEX:800000', 'annotations': {'rgb': '128,0,0'}},
    "SNOW": {'description': 'Snow', 'meaning': 'HEX:FFFAFA', 'annotations': {'rgb': '255,250,250'}},
    "HONEYDEW": {'description': 'Honeydew', 'meaning': 'HEX:F0FFF0', 'annotations': {'rgb': '240,255,240'}},
    "MINT_CREAM": {'description': 'Mint cream', 'meaning': 'HEX:F5FFFA', 'annotations': {'rgb': '245,255,250'}},
    "AZURE": {'description': 'Azure', 'meaning': 'HEX:F0FFFF', 'annotations': {'rgb': '240,255,255'}},
    "ALICE_BLUE": {'description': 'Alice blue', 'meaning': 'HEX:F0F8FF', 'annotations': {'rgb': '240,248,255'}},
    "GHOST_WHITE": {'description': 'Ghost white', 'meaning': 'HEX:F8F8FF', 'annotations': {'rgb': '248,248,255'}},
    "WHITE_SMOKE": {'description': 'White smoke', 'meaning': 'HEX:F5F5F5', 'annotations': {'rgb': '245,245,245'}},
    "SEASHELL": {'description': 'Seashell', 'meaning': 'HEX:FFF5EE', 'annotations': {'rgb': '255,245,238'}},
    "BEIGE": {'description': 'Beige', 'meaning': 'HEX:F5F5DC', 'annotations': {'rgb': '245,245,220'}},
    "OLD_LACE": {'description': 'Old lace', 'meaning': 'HEX:FDF5E6', 'annotations': {'rgb': '253,245,230'}},
    "FLORAL_WHITE": {'description': 'Floral white', 'meaning': 'HEX:FFFAF0', 'annotations': {'rgb': '255,250,240'}},
    "IVORY": {'description': 'Ivory', 'meaning': 'HEX:FFFFF0', 'annotations': {'rgb': '255,255,240'}},
    "ANTIQUE_WHITE": {'description': 'Antique white', 'meaning': 'HEX:FAEBD7', 'annotations': {'rgb': '250,235,215'}},
    "LINEN": {'description': 'Linen', 'meaning': 'HEX:FAF0E6', 'annotations': {'rgb': '250,240,230'}},
    "LAVENDER_BLUSH": {'description': 'Lavender blush', 'meaning': 'HEX:FFF0F5', 'annotations': {'rgb': '255,240,245'}},
    "MISTY_ROSE": {'description': 'Misty rose', 'meaning': 'HEX:FFE4E1', 'annotations': {'rgb': '255,228,225'}},
    "GAINSBORO": {'description': 'Gainsboro', 'meaning': 'HEX:DCDCDC', 'annotations': {'rgb': '220,220,220'}},
    "LIGHT_GRAY": {'description': 'Light gray', 'meaning': 'HEX:D3D3D3', 'annotations': {'rgb': '211,211,211'}},
    "SILVER": {'description': 'Silver', 'meaning': 'HEX:C0C0C0', 'annotations': {'rgb': '192,192,192'}},
    "DARK_GRAY": {'description': 'Dark gray', 'meaning': 'HEX:A9A9A9', 'annotations': {'rgb': '169,169,169'}},
    "DIM_GRAY": {'description': 'Dim gray', 'meaning': 'HEX:696969', 'annotations': {'rgb': '105,105,105'}},
    "LIGHT_SLATE_GRAY": {'description': 'Light slate gray', 'meaning': 'HEX:778899', 'annotations': {'rgb': '119,136,153'}},
    "SLATE_GRAY": {'description': 'Slate gray', 'meaning': 'HEX:708090', 'annotations': {'rgb': '112,128,144'}},
    "DARK_SLATE_GRAY": {'description': 'Dark slate gray', 'meaning': 'HEX:2F4F4F', 'annotations': {'rgb': '47,79,79'}},
}

class X11ColorEnum(RichEnum):
    """
    X11/Unix system colors (extended set)
    """
    # Enum members
    X11_AQUA = "X11_AQUA"
    X11_GRAY0 = "X11_GRAY0"
    X11_GRAY25 = "X11_GRAY25"
    X11_GRAY50 = "X11_GRAY50"
    X11_GRAY75 = "X11_GRAY75"
    X11_GRAY100 = "X11_GRAY100"
    X11_GREEN1 = "X11_GREEN1"
    X11_GREEN2 = "X11_GREEN2"
    X11_GREEN3 = "X11_GREEN3"
    X11_GREEN4 = "X11_GREEN4"
    X11_BLUE1 = "X11_BLUE1"
    X11_BLUE2 = "X11_BLUE2"
    X11_BLUE3 = "X11_BLUE3"
    X11_BLUE4 = "X11_BLUE4"
    X11_RED1 = "X11_RED1"
    X11_RED2 = "X11_RED2"
    X11_RED3 = "X11_RED3"
    X11_RED4 = "X11_RED4"

# Set metadata after class creation
X11ColorEnum._metadata = {
    "X11_AQUA": {'description': 'X11 Aqua', 'meaning': 'HEX:00FFFF'},
    "X11_GRAY0": {'description': 'X11 Gray 0 (black)', 'meaning': 'HEX:000000'},
    "X11_GRAY25": {'description': 'X11 Gray 25%', 'meaning': 'HEX:404040'},
    "X11_GRAY50": {'description': 'X11 Gray 50%', 'meaning': 'HEX:808080'},
    "X11_GRAY75": {'description': 'X11 Gray 75%', 'meaning': 'HEX:BFBFBF'},
    "X11_GRAY100": {'description': 'X11 Gray 100 (white)', 'meaning': 'HEX:FFFFFF'},
    "X11_GREEN1": {'description': 'X11 Green 1', 'meaning': 'HEX:00FF00'},
    "X11_GREEN2": {'description': 'X11 Green 2', 'meaning': 'HEX:00EE00'},
    "X11_GREEN3": {'description': 'X11 Green 3', 'meaning': 'HEX:00CD00'},
    "X11_GREEN4": {'description': 'X11 Green 4', 'meaning': 'HEX:008B00'},
    "X11_BLUE1": {'description': 'X11 Blue 1', 'meaning': 'HEX:0000FF'},
    "X11_BLUE2": {'description': 'X11 Blue 2', 'meaning': 'HEX:0000EE'},
    "X11_BLUE3": {'description': 'X11 Blue 3', 'meaning': 'HEX:0000CD'},
    "X11_BLUE4": {'description': 'X11 Blue 4', 'meaning': 'HEX:00008B'},
    "X11_RED1": {'description': 'X11 Red 1', 'meaning': 'HEX:FF0000'},
    "X11_RED2": {'description': 'X11 Red 2', 'meaning': 'HEX:EE0000'},
    "X11_RED3": {'description': 'X11 Red 3', 'meaning': 'HEX:CD0000'},
    "X11_RED4": {'description': 'X11 Red 4', 'meaning': 'HEX:8B0000'},
}

class ColorSpaceEnum(RichEnum):
    """
    Color space and model types
    """
    # Enum members
    RGB = "RGB"
    CMYK = "CMYK"
    HSL = "HSL"
    HSV = "HSV"
    LAB = "LAB"
    PANTONE = "PANTONE"
    RAL = "RAL"
    NCS = "NCS"
    MUNSELL = "MUNSELL"

# Set metadata after class creation
ColorSpaceEnum._metadata = {
    "RGB": {'description': 'Red Green Blue color model'},
    "CMYK": {'description': 'Cyan Magenta Yellow Key (black) color model'},
    "HSL": {'description': 'Hue Saturation Lightness color model'},
    "HSV": {'description': 'Hue Saturation Value color model'},
    "LAB": {'description': 'CIELAB color space'},
    "PANTONE": {'description': 'Pantone Matching System'},
    "RAL": {'description': 'RAL color standard'},
    "NCS": {'description': 'Natural Color System'},
    "MUNSELL": {'description': 'Munsell color system'},
}

__all__ = [
    "BasicColorEnum",
    "WebColorEnum",
    "X11ColorEnum",
    "ColorSpaceEnum",
]