"""
valuesets-geography-geographic-codes

Geographic codes and regional value sets

Generated from: geography/geographic_codes.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class CountryCodeISO2Enum(RichEnum):
    """
    ISO 3166-1 alpha-2 country codes (2-letter codes)
    """
    # Enum members
    US = "US"
    CA = "CA"
    MX = "MX"
    GB = "GB"
    FR = "FR"
    DE = "DE"
    IT = "IT"
    ES = "ES"
    PT = "PT"
    NL = "NL"
    BE = "BE"
    CH = "CH"
    AT = "AT"
    SE = "SE"
    FALSE = "False"
    DK = "DK"
    FI = "FI"
    PL = "PL"
    RU = "RU"
    UA = "UA"
    CN = "CN"
    JP = "JP"
    KR = "KR"
    IN = "IN"
    AU = "AU"
    NZ = "NZ"
    BR = "BR"
    AR = "AR"
    CL = "CL"
    CO = "CO"
    PE = "PE"
    VE = "VE"
    ZA = "ZA"
    EG = "EG"
    NG = "NG"
    KE = "KE"
    IL = "IL"
    SA = "SA"
    AE = "AE"
    TR = "TR"
    GR = "GR"
    IE = "IE"
    SG = "SG"
    MY = "MY"
    TH = "TH"
    ID = "ID"
    PH = "PH"
    VN = "VN"
    PK = "PK"
    BD = "BD"

# Set metadata after class creation
CountryCodeISO2Enum._metadata = {
    "US": {'description': 'United States of America', 'meaning': 'iso3166loc:us'},
    "CA": {'description': 'Canada', 'meaning': 'iso3166loc:ca'},
    "MX": {'description': 'Mexico', 'meaning': 'iso3166loc:mx'},
    "GB": {'description': 'United Kingdom', 'meaning': 'iso3166loc:gb'},
    "FR": {'description': 'France', 'meaning': 'iso3166loc:fr'},
    "DE": {'description': 'Germany', 'meaning': 'iso3166loc:de'},
    "IT": {'description': 'Italy', 'meaning': 'iso3166loc:it'},
    "ES": {'description': 'Spain', 'meaning': 'iso3166loc:es'},
    "PT": {'description': 'Portugal', 'meaning': 'iso3166loc:pt'},
    "NL": {'description': 'Netherlands', 'meaning': 'iso3166loc:nl'},
    "BE": {'description': 'Belgium', 'meaning': 'iso3166loc:be'},
    "CH": {'description': 'Switzerland', 'meaning': 'iso3166loc:ch'},
    "AT": {'description': 'Austria', 'meaning': 'iso3166loc:at'},
    "SE": {'description': 'Sweden', 'meaning': 'iso3166loc:se'},
    "FALSE": {'description': 'Norway', 'meaning': 'iso3166loc:no'},
    "DK": {'description': 'Denmark', 'meaning': 'iso3166loc:dk'},
    "FI": {'description': 'Finland', 'meaning': 'iso3166loc:fi'},
    "PL": {'description': 'Poland', 'meaning': 'iso3166loc:pl'},
    "RU": {'description': 'Russian Federation', 'meaning': 'iso3166loc:ru'},
    "UA": {'description': 'Ukraine', 'meaning': 'iso3166loc:ua'},
    "CN": {'description': 'China', 'meaning': 'iso3166loc:cn'},
    "JP": {'description': 'Japan', 'meaning': 'iso3166loc:jp'},
    "KR": {'description': 'South Korea', 'meaning': 'iso3166loc:kr'},
    "IN": {'description': 'India', 'meaning': 'iso3166loc:in'},
    "AU": {'description': 'Australia', 'meaning': 'iso3166loc:au'},
    "NZ": {'description': 'New Zealand', 'meaning': 'iso3166loc:nz'},
    "BR": {'description': 'Brazil', 'meaning': 'iso3166loc:br'},
    "AR": {'description': 'Argentina', 'meaning': 'iso3166loc:ar'},
    "CL": {'description': 'Chile', 'meaning': 'iso3166loc:cl'},
    "CO": {'description': 'Colombia', 'meaning': 'iso3166loc:co'},
    "PE": {'description': 'Peru', 'meaning': 'iso3166loc:pe'},
    "VE": {'description': 'Venezuela', 'meaning': 'iso3166loc:ve'},
    "ZA": {'description': 'South Africa', 'meaning': 'iso3166loc:za'},
    "EG": {'description': 'Egypt', 'meaning': 'iso3166loc:eg'},
    "NG": {'description': 'Nigeria', 'meaning': 'iso3166loc:ng'},
    "KE": {'description': 'Kenya', 'meaning': 'iso3166loc:ke'},
    "IL": {'description': 'Israel', 'meaning': 'iso3166loc:il'},
    "SA": {'description': 'Saudi Arabia', 'meaning': 'iso3166loc:sa'},
    "AE": {'description': 'United Arab Emirates', 'meaning': 'iso3166loc:ae'},
    "TR": {'description': 'Turkey', 'meaning': 'iso3166loc:tr'},
    "GR": {'description': 'Greece', 'meaning': 'iso3166loc:gr'},
    "IE": {'description': 'Ireland', 'meaning': 'iso3166loc:ie'},
    "SG": {'description': 'Singapore', 'meaning': 'iso3166loc:sg'},
    "MY": {'description': 'Malaysia', 'meaning': 'iso3166loc:my'},
    "TH": {'description': 'Thailand', 'meaning': 'iso3166loc:th'},
    "ID": {'description': 'Indonesia', 'meaning': 'iso3166loc:id'},
    "PH": {'description': 'Philippines', 'meaning': 'iso3166loc:ph'},
    "VN": {'description': 'Vietnam', 'meaning': 'iso3166loc:vn'},
    "PK": {'description': 'Pakistan', 'meaning': 'iso3166loc:pk'},
    "BD": {'description': 'Bangladesh', 'meaning': 'iso3166loc:bd'},
}

class CountryCodeISO3Enum(RichEnum):
    """
    ISO 3166-1 alpha-3 country codes (3-letter codes)
    """
    # Enum members
    USA = "USA"
    CAN = "CAN"
    MEX = "MEX"
    GBR = "GBR"
    FRA = "FRA"
    DEU = "DEU"
    ITA = "ITA"
    ESP = "ESP"
    PRT = "PRT"
    NLD = "NLD"
    BEL = "BEL"
    CHE = "CHE"
    AUT = "AUT"
    SWE = "SWE"
    NOR = "NOR"
    DNK = "DNK"
    FIN = "FIN"
    POL = "POL"
    RUS = "RUS"
    UKR = "UKR"
    CHN = "CHN"
    JPN = "JPN"
    KOR = "KOR"
    IND = "IND"
    AUS = "AUS"
    NZL = "NZL"
    BRA = "BRA"
    ARG = "ARG"
    CHL = "CHL"
    COL = "COL"

# Set metadata after class creation
CountryCodeISO3Enum._metadata = {
    "USA": {'description': 'United States of America', 'meaning': 'iso3166loc:us'},
    "CAN": {'description': 'Canada', 'meaning': 'iso3166loc:ca'},
    "MEX": {'description': 'Mexico', 'meaning': 'iso3166loc:mx'},
    "GBR": {'description': 'United Kingdom', 'meaning': 'iso3166loc:gb'},
    "FRA": {'description': 'France', 'meaning': 'iso3166loc:fr'},
    "DEU": {'description': 'Germany', 'meaning': 'iso3166loc:de'},
    "ITA": {'description': 'Italy', 'meaning': 'iso3166loc:it'},
    "ESP": {'description': 'Spain', 'meaning': 'iso3166loc:es'},
    "PRT": {'description': 'Portugal', 'meaning': 'iso3166loc:pt'},
    "NLD": {'description': 'Netherlands', 'meaning': 'iso3166loc:nl'},
    "BEL": {'description': 'Belgium', 'meaning': 'iso3166loc:be'},
    "CHE": {'description': 'Switzerland', 'meaning': 'iso3166loc:ch'},
    "AUT": {'description': 'Austria', 'meaning': 'iso3166loc:at'},
    "SWE": {'description': 'Sweden', 'meaning': 'iso3166loc:se'},
    "NOR": {'description': 'Norway', 'meaning': 'iso3166loc:no'},
    "DNK": {'description': 'Denmark', 'meaning': 'iso3166loc:dk'},
    "FIN": {'description': 'Finland', 'meaning': 'iso3166loc:fi'},
    "POL": {'description': 'Poland', 'meaning': 'iso3166loc:pl'},
    "RUS": {'description': 'Russian Federation', 'meaning': 'iso3166loc:ru'},
    "UKR": {'description': 'Ukraine', 'meaning': 'iso3166loc:ua'},
    "CHN": {'description': 'China', 'meaning': 'iso3166loc:cn'},
    "JPN": {'description': 'Japan', 'meaning': 'iso3166loc:jp'},
    "KOR": {'description': 'South Korea', 'meaning': 'iso3166loc:kr'},
    "IND": {'description': 'India', 'meaning': 'iso3166loc:in'},
    "AUS": {'description': 'Australia', 'meaning': 'iso3166loc:au'},
    "NZL": {'description': 'New Zealand', 'meaning': 'iso3166loc:nz'},
    "BRA": {'description': 'Brazil', 'meaning': 'iso3166loc:br'},
    "ARG": {'description': 'Argentina', 'meaning': 'iso3166loc:ar'},
    "CHL": {'description': 'Chile', 'meaning': 'iso3166loc:cl'},
    "COL": {'description': 'Colombia', 'meaning': 'iso3166loc:co'},
}

class USStateCodeEnum(RichEnum):
    """
    United States state and territory codes
    """
    # Enum members
    AL = "AL"
    AK = "AK"
    AZ = "AZ"
    AR = "AR"
    CA = "CA"
    CO = "CO"
    CT = "CT"
    DE = "DE"
    FL = "FL"
    GA = "GA"
    HI = "HI"
    ID = "ID"
    IL = "IL"
    IN = "IN"
    IA = "IA"
    KS = "KS"
    KY = "KY"
    LA = "LA"
    ME = "ME"
    MD = "MD"
    MA = "MA"
    MI = "MI"
    MN = "MN"
    MS = "MS"
    MO = "MO"
    MT = "MT"
    NE = "NE"
    NV = "NV"
    NH = "NH"
    NJ = "NJ"
    NM = "NM"
    NY = "NY"
    NC = "NC"
    ND = "ND"
    OH = "OH"
    OK = "OK"
    OR = "OR"
    PA = "PA"
    RI = "RI"
    SC = "SC"
    SD = "SD"
    TN = "TN"
    TX = "TX"
    UT = "UT"
    VT = "VT"
    VA = "VA"
    WA = "WA"
    WV = "WV"
    WI = "WI"
    WY = "WY"
    DC = "DC"
    PR = "PR"
    VI = "VI"
    GU = "GU"
    AS = "AS"
    MP = "MP"

# Set metadata after class creation
USStateCodeEnum._metadata = {
    "AL": {'description': 'Alabama'},
    "AK": {'description': 'Alaska'},
    "AZ": {'description': 'Arizona'},
    "AR": {'description': 'Arkansas'},
    "CA": {'description': 'California'},
    "CO": {'description': 'Colorado'},
    "CT": {'description': 'Connecticut'},
    "DE": {'description': 'Delaware'},
    "FL": {'description': 'Florida'},
    "GA": {'description': 'Georgia'},
    "HI": {'description': 'Hawaii'},
    "ID": {'description': 'Idaho'},
    "IL": {'description': 'Illinois'},
    "IN": {'description': 'Indiana'},
    "IA": {'description': 'Iowa'},
    "KS": {'description': 'Kansas'},
    "KY": {'description': 'Kentucky'},
    "LA": {'description': 'Louisiana'},
    "ME": {'description': 'Maine'},
    "MD": {'description': 'Maryland'},
    "MA": {'description': 'Massachusetts'},
    "MI": {'description': 'Michigan'},
    "MN": {'description': 'Minnesota'},
    "MS": {'description': 'Mississippi'},
    "MO": {'description': 'Missouri'},
    "MT": {'description': 'Montana'},
    "NE": {'description': 'Nebraska'},
    "NV": {'description': 'Nevada'},
    "NH": {'description': 'New Hampshire'},
    "NJ": {'description': 'New Jersey'},
    "NM": {'description': 'New Mexico'},
    "NY": {'description': 'New York'},
    "NC": {'description': 'North Carolina'},
    "ND": {'description': 'North Dakota'},
    "OH": {'description': 'Ohio'},
    "OK": {'description': 'Oklahoma'},
    "OR": {'description': 'Oregon'},
    "PA": {'description': 'Pennsylvania'},
    "RI": {'description': 'Rhode Island'},
    "SC": {'description': 'South Carolina'},
    "SD": {'description': 'South Dakota'},
    "TN": {'description': 'Tennessee'},
    "TX": {'description': 'Texas'},
    "UT": {'description': 'Utah'},
    "VT": {'description': 'Vermont'},
    "VA": {'description': 'Virginia'},
    "WA": {'description': 'Washington'},
    "WV": {'description': 'West Virginia'},
    "WI": {'description': 'Wisconsin'},
    "WY": {'description': 'Wyoming'},
    "DC": {'description': 'District of Columbia'},
    "PR": {'description': 'Puerto Rico'},
    "VI": {'description': 'U.S. Virgin Islands'},
    "GU": {'description': 'Guam'},
    "AS": {'description': 'American Samoa'},
    "MP": {'description': 'Northern Mariana Islands'},
}

class CanadianProvinceCodeEnum(RichEnum):
    """
    Canadian province and territory codes
    """
    # Enum members
    AB = "AB"
    BC = "BC"
    MB = "MB"
    NB = "NB"
    NL = "NL"
    NS = "NS"
    NT = "NT"
    NU = "NU"
    TRUE = "True"
    PE = "PE"
    QC = "QC"
    SK = "SK"
    YT = "YT"

# Set metadata after class creation
CanadianProvinceCodeEnum._metadata = {
    "AB": {'description': 'Alberta'},
    "BC": {'description': 'British Columbia'},
    "MB": {'description': 'Manitoba'},
    "NB": {'description': 'New Brunswick'},
    "NL": {'description': 'Newfoundland and Labrador'},
    "NS": {'description': 'Nova Scotia'},
    "NT": {'description': 'Northwest Territories'},
    "NU": {'description': 'Nunavut'},
    "TRUE": {'description': 'Ontario'},
    "PE": {'description': 'Prince Edward Island'},
    "QC": {'description': 'Quebec'},
    "SK": {'description': 'Saskatchewan'},
    "YT": {'description': 'Yukon'},
}

class CompassDirection(RichEnum):
    """
    Cardinal and intercardinal compass directions
    """
    # Enum members
    NORTH = "NORTH"
    EAST = "EAST"
    SOUTH = "SOUTH"
    WEST = "WEST"
    NORTHEAST = "NORTHEAST"
    SOUTHEAST = "SOUTHEAST"
    SOUTHWEST = "SOUTHWEST"
    NORTHWEST = "NORTHWEST"
    NORTH_NORTHEAST = "NORTH_NORTHEAST"
    EAST_NORTHEAST = "EAST_NORTHEAST"
    EAST_SOUTHEAST = "EAST_SOUTHEAST"
    SOUTH_SOUTHEAST = "SOUTH_SOUTHEAST"
    SOUTH_SOUTHWEST = "SOUTH_SOUTHWEST"
    WEST_SOUTHWEST = "WEST_SOUTHWEST"
    WEST_NORTHWEST = "WEST_NORTHWEST"
    NORTH_NORTHWEST = "NORTH_NORTHWEST"

# Set metadata after class creation
CompassDirection._metadata = {
    "NORTH": {'description': 'North (0°/360°)', 'annotations': {'abbreviation': 'N', 'degrees': 0}},
    "EAST": {'description': 'East (90°)', 'annotations': {'abbreviation': 'E', 'degrees': 90}},
    "SOUTH": {'description': 'South (180°)', 'annotations': {'abbreviation': 'S', 'degrees': 180}},
    "WEST": {'description': 'West (270°)', 'annotations': {'abbreviation': 'W', 'degrees': 270}},
    "NORTHEAST": {'description': 'Northeast (45°)', 'annotations': {'abbreviation': 'NE', 'degrees': 45}},
    "SOUTHEAST": {'description': 'Southeast (135°)', 'annotations': {'abbreviation': 'SE', 'degrees': 135}},
    "SOUTHWEST": {'description': 'Southwest (225°)', 'annotations': {'abbreviation': 'SW', 'degrees': 225}},
    "NORTHWEST": {'description': 'Northwest (315°)', 'annotations': {'abbreviation': 'NW', 'degrees': 315}},
    "NORTH_NORTHEAST": {'description': 'North-northeast (22.5°)', 'annotations': {'abbreviation': 'NNE', 'degrees': 22.5}},
    "EAST_NORTHEAST": {'description': 'East-northeast (67.5°)', 'annotations': {'abbreviation': 'ENE', 'degrees': 67.5}},
    "EAST_SOUTHEAST": {'description': 'East-southeast (112.5°)', 'annotations': {'abbreviation': 'ESE', 'degrees': 112.5}},
    "SOUTH_SOUTHEAST": {'description': 'South-southeast (157.5°)', 'annotations': {'abbreviation': 'SSE', 'degrees': 157.5}},
    "SOUTH_SOUTHWEST": {'description': 'South-southwest (202.5°)', 'annotations': {'abbreviation': 'SSW', 'degrees': 202.5}},
    "WEST_SOUTHWEST": {'description': 'West-southwest (247.5°)', 'annotations': {'abbreviation': 'WSW', 'degrees': 247.5}},
    "WEST_NORTHWEST": {'description': 'West-northwest (292.5°)', 'annotations': {'abbreviation': 'WNW', 'degrees': 292.5}},
    "NORTH_NORTHWEST": {'description': 'North-northwest (337.5°)', 'annotations': {'abbreviation': 'NNW', 'degrees': 337.5}},
}

class RelativeDirection(RichEnum):
    """
    Relative directional terms
    """
    # Enum members
    FORWARD = "FORWARD"
    BACKWARD = "BACKWARD"
    LEFT = "LEFT"
    RIGHT = "RIGHT"
    UP = "UP"
    DOWN = "DOWN"
    INWARD = "INWARD"
    OUTWARD = "OUTWARD"
    CLOCKWISE = "CLOCKWISE"
    COUNTERCLOCKWISE = "COUNTERCLOCKWISE"

# Set metadata after class creation
RelativeDirection._metadata = {
    "FORWARD": {'description': 'Forward/Ahead', 'annotations': {'aliases': 'ahead, front'}},
    "BACKWARD": {'description': 'Backward/Behind', 'annotations': {'aliases': 'behind, back, rear'}},
    "LEFT": {'description': 'Left', 'annotations': {'aliases': 'port (nautical)'}},
    "RIGHT": {'description': 'Right', 'annotations': {'aliases': 'starboard (nautical)'}},
    "UP": {'description': 'Up/Above', 'annotations': {'aliases': 'above, upward'}},
    "DOWN": {'description': 'Down/Below', 'annotations': {'aliases': 'below, downward'}},
    "INWARD": {'description': 'Inward/Toward center', 'annotations': {'aliases': 'toward center, centripetal'}},
    "OUTWARD": {'description': 'Outward/Away from center', 'annotations': {'aliases': 'away from center, centrifugal'}},
    "CLOCKWISE": {'description': 'Clockwise rotation', 'annotations': {'abbreviation': 'CW'}},
    "COUNTERCLOCKWISE": {'description': 'Counterclockwise rotation', 'annotations': {'abbreviation': 'CCW', 'aliases': 'anticlockwise'}},
}

class WindDirection(RichEnum):
    """
    Wind direction nomenclature (named for where wind comes FROM)
    """
    # Enum members
    NORTHERLY = "NORTHERLY"
    NORTHEASTERLY = "NORTHEASTERLY"
    EASTERLY = "EASTERLY"
    SOUTHEASTERLY = "SOUTHEASTERLY"
    SOUTHERLY = "SOUTHERLY"
    SOUTHWESTERLY = "SOUTHWESTERLY"
    WESTERLY = "WESTERLY"
    NORTHWESTERLY = "NORTHWESTERLY"
    VARIABLE = "VARIABLE"

# Set metadata after class creation
WindDirection._metadata = {
    "NORTHERLY": {'description': 'Wind from the north', 'annotations': {'from_direction': 'north', 'toward_direction': 'south'}},
    "NORTHEASTERLY": {'description': 'Wind from the northeast', 'annotations': {'from_direction': 'northeast', 'toward_direction': 'southwest'}},
    "EASTERLY": {'description': 'Wind from the east', 'annotations': {'from_direction': 'east', 'toward_direction': 'west'}},
    "SOUTHEASTERLY": {'description': 'Wind from the southeast', 'annotations': {'from_direction': 'southeast', 'toward_direction': 'northwest'}},
    "SOUTHERLY": {'description': 'Wind from the south', 'annotations': {'from_direction': 'south', 'toward_direction': 'north'}},
    "SOUTHWESTERLY": {'description': 'Wind from the southwest', 'annotations': {'from_direction': 'southwest', 'toward_direction': 'northeast'}},
    "WESTERLY": {'description': 'Wind from the west', 'annotations': {'from_direction': 'west', 'toward_direction': 'east'}},
    "NORTHWESTERLY": {'description': 'Wind from the northwest', 'annotations': {'from_direction': 'northwest', 'toward_direction': 'southeast'}},
    "VARIABLE": {'description': 'Variable wind direction', 'annotations': {'note': 'changing or inconsistent direction'}},
}

class ContinentEnum(RichEnum):
    """
    Continental regions
    """
    # Enum members
    AFRICA = "AFRICA"
    ANTARCTICA = "ANTARCTICA"
    ASIA = "ASIA"
    EUROPE = "EUROPE"
    NORTH_AMERICA = "NORTH_AMERICA"
    OCEANIA = "OCEANIA"
    SOUTH_AMERICA = "SOUTH_AMERICA"

# Set metadata after class creation
ContinentEnum._metadata = {
    "AFRICA": {'description': 'Africa'},
    "ANTARCTICA": {'description': 'Antarctica'},
    "ASIA": {'description': 'Asia'},
    "EUROPE": {'description': 'Europe'},
    "NORTH_AMERICA": {'description': 'North America'},
    "OCEANIA": {'description': 'Oceania (including Australia)'},
    "SOUTH_AMERICA": {'description': 'South America'},
}

class UNRegionEnum(RichEnum):
    """
    United Nations regional classifications
    """
    # Enum members
    EASTERN_AFRICA = "EASTERN_AFRICA"
    MIDDLE_AFRICA = "MIDDLE_AFRICA"
    NORTHERN_AFRICA = "NORTHERN_AFRICA"
    SOUTHERN_AFRICA = "SOUTHERN_AFRICA"
    WESTERN_AFRICA = "WESTERN_AFRICA"
    CARIBBEAN = "CARIBBEAN"
    CENTRAL_AMERICA = "CENTRAL_AMERICA"
    NORTHERN_AMERICA = "NORTHERN_AMERICA"
    SOUTH_AMERICA = "SOUTH_AMERICA"
    CENTRAL_ASIA = "CENTRAL_ASIA"
    EASTERN_ASIA = "EASTERN_ASIA"
    SOUTHERN_ASIA = "SOUTHERN_ASIA"
    SOUTH_EASTERN_ASIA = "SOUTH_EASTERN_ASIA"
    WESTERN_ASIA = "WESTERN_ASIA"
    EASTERN_EUROPE = "EASTERN_EUROPE"
    NORTHERN_EUROPE = "NORTHERN_EUROPE"
    SOUTHERN_EUROPE = "SOUTHERN_EUROPE"
    WESTERN_EUROPE = "WESTERN_EUROPE"
    AUSTRALIA_NEW_ZEALAND = "AUSTRALIA_NEW_ZEALAND"
    MELANESIA = "MELANESIA"
    MICRONESIA = "MICRONESIA"
    POLYNESIA = "POLYNESIA"

# Set metadata after class creation
UNRegionEnum._metadata = {
    "EASTERN_AFRICA": {'description': 'Eastern Africa'},
    "MIDDLE_AFRICA": {'description': 'Middle Africa'},
    "NORTHERN_AFRICA": {'description': 'Northern Africa'},
    "SOUTHERN_AFRICA": {'description': 'Southern Africa'},
    "WESTERN_AFRICA": {'description': 'Western Africa'},
    "CARIBBEAN": {'description': 'Caribbean'},
    "CENTRAL_AMERICA": {'description': 'Central America'},
    "NORTHERN_AMERICA": {'description': 'Northern America'},
    "SOUTH_AMERICA": {'description': 'South America'},
    "CENTRAL_ASIA": {'description': 'Central Asia'},
    "EASTERN_ASIA": {'description': 'Eastern Asia'},
    "SOUTHERN_ASIA": {'description': 'Southern Asia'},
    "SOUTH_EASTERN_ASIA": {'description': 'South-Eastern Asia'},
    "WESTERN_ASIA": {'description': 'Western Asia'},
    "EASTERN_EUROPE": {'description': 'Eastern Europe'},
    "NORTHERN_EUROPE": {'description': 'Northern Europe'},
    "SOUTHERN_EUROPE": {'description': 'Southern Europe'},
    "WESTERN_EUROPE": {'description': 'Western Europe'},
    "AUSTRALIA_NEW_ZEALAND": {'description': 'Australia and New Zealand'},
    "MELANESIA": {'description': 'Melanesia'},
    "MICRONESIA": {'description': 'Micronesia'},
    "POLYNESIA": {'description': 'Polynesia'},
}

class LanguageCodeISO6391enum(RichEnum):
    """
    ISO 639-1 two-letter language codes
    """
    # Enum members
    EN = "EN"
    ES = "ES"
    FR = "FR"
    DE = "DE"
    IT = "IT"
    PT = "PT"
    RU = "RU"
    ZH = "ZH"
    JA = "JA"
    KO = "KO"
    AR = "AR"
    HI = "HI"
    BN = "BN"
    PA = "PA"
    UR = "UR"
    NL = "NL"
    PL = "PL"
    TR = "TR"
    VI = "VI"
    TH = "TH"
    SV = "SV"
    DA = "DA"
    FALSE = "False"
    FI = "FI"
    EL = "EL"
    HE = "HE"
    CS = "CS"
    HU = "HU"
    RO = "RO"
    UK = "UK"

# Set metadata after class creation
LanguageCodeISO6391enum._metadata = {
    "EN": {'description': 'English'},
    "ES": {'description': 'Spanish'},
    "FR": {'description': 'French'},
    "DE": {'description': 'German'},
    "IT": {'description': 'Italian'},
    "PT": {'description': 'Portuguese'},
    "RU": {'description': 'Russian'},
    "ZH": {'description': 'Chinese'},
    "JA": {'description': 'Japanese'},
    "KO": {'description': 'Korean'},
    "AR": {'description': 'Arabic'},
    "HI": {'description': 'Hindi'},
    "BN": {'description': 'Bengali'},
    "PA": {'description': 'Punjabi'},
    "UR": {'description': 'Urdu'},
    "NL": {'description': 'Dutch'},
    "PL": {'description': 'Polish'},
    "TR": {'description': 'Turkish'},
    "VI": {'description': 'Vietnamese'},
    "TH": {'description': 'Thai'},
    "SV": {'description': 'Swedish'},
    "DA": {'description': 'Danish'},
    "FALSE": {'description': 'Norwegian'},
    "FI": {'description': 'Finnish'},
    "EL": {'description': 'Greek'},
    "HE": {'description': 'Hebrew'},
    "CS": {'description': 'Czech'},
    "HU": {'description': 'Hungarian'},
    "RO": {'description': 'Romanian'},
    "UK": {'description': 'Ukrainian'},
}

class TimeZoneEnum(RichEnum):
    """
    Common time zones
    """
    # Enum members
    UTC = "UTC"
    EST = "EST"
    EDT = "EDT"
    CST = "CST"
    CDT = "CDT"
    MST = "MST"
    MDT = "MDT"
    PST = "PST"
    PDT = "PDT"
    GMT = "GMT"
    BST = "BST"
    CET = "CET"
    CEST = "CEST"
    EET = "EET"
    EEST = "EEST"
    JST = "JST"
    CST_CHINA = "CST_CHINA"
    IST = "IST"
    AEST = "AEST"
    AEDT = "AEDT"
    NZST = "NZST"
    NZDT = "NZDT"

# Set metadata after class creation
TimeZoneEnum._metadata = {
    "UTC": {'description': 'Coordinated Universal Time'},
    "EST": {'description': 'Eastern Standard Time (UTC-5)'},
    "EDT": {'description': 'Eastern Daylight Time (UTC-4)'},
    "CST": {'description': 'Central Standard Time (UTC-6)'},
    "CDT": {'description': 'Central Daylight Time (UTC-5)'},
    "MST": {'description': 'Mountain Standard Time (UTC-7)'},
    "MDT": {'description': 'Mountain Daylight Time (UTC-6)'},
    "PST": {'description': 'Pacific Standard Time (UTC-8)'},
    "PDT": {'description': 'Pacific Daylight Time (UTC-7)'},
    "GMT": {'description': 'Greenwich Mean Time (UTC+0)'},
    "BST": {'description': 'British Summer Time (UTC+1)'},
    "CET": {'description': 'Central European Time (UTC+1)'},
    "CEST": {'description': 'Central European Summer Time (UTC+2)'},
    "EET": {'description': 'Eastern European Time (UTC+2)'},
    "EEST": {'description': 'Eastern European Summer Time (UTC+3)'},
    "JST": {'description': 'Japan Standard Time (UTC+9)'},
    "CST_CHINA": {'description': 'China Standard Time (UTC+8)'},
    "IST": {'description': 'India Standard Time (UTC+5:30)'},
    "AEST": {'description': 'Australian Eastern Standard Time (UTC+10)'},
    "AEDT": {'description': 'Australian Eastern Daylight Time (UTC+11)'},
    "NZST": {'description': 'New Zealand Standard Time (UTC+12)'},
    "NZDT": {'description': 'New Zealand Daylight Time (UTC+13)'},
}

class CurrencyCodeISO4217Enum(RichEnum):
    """
    ISO 4217 currency codes
    """
    # Enum members
    USD = "USD"
    EUR = "EUR"
    GBP = "GBP"
    JPY = "JPY"
    CNY = "CNY"
    CHF = "CHF"
    CAD = "CAD"
    AUD = "AUD"
    NZD = "NZD"
    SEK = "SEK"
    NOK = "NOK"
    DKK = "DKK"
    PLN = "PLN"
    RUB = "RUB"
    INR = "INR"
    BRL = "BRL"
    MXN = "MXN"
    ZAR = "ZAR"
    KRW = "KRW"
    SGD = "SGD"
    HKD = "HKD"
    TWD = "TWD"
    THB = "THB"
    MYR = "MYR"
    IDR = "IDR"
    PHP = "PHP"
    VND = "VND"
    TRY = "TRY"
    AED = "AED"
    SAR = "SAR"
    ILS = "ILS"
    EGP = "EGP"

# Set metadata after class creation
CurrencyCodeISO4217Enum._metadata = {
    "USD": {'description': 'United States Dollar'},
    "EUR": {'description': 'Euro'},
    "GBP": {'description': 'British Pound Sterling'},
    "JPY": {'description': 'Japanese Yen'},
    "CNY": {'description': 'Chinese Yuan Renminbi'},
    "CHF": {'description': 'Swiss Franc'},
    "CAD": {'description': 'Canadian Dollar'},
    "AUD": {'description': 'Australian Dollar'},
    "NZD": {'description': 'New Zealand Dollar'},
    "SEK": {'description': 'Swedish Krona'},
    "NOK": {'description': 'Norwegian Krone'},
    "DKK": {'description': 'Danish Krone'},
    "PLN": {'description': 'Polish Zloty'},
    "RUB": {'description': 'Russian Ruble'},
    "INR": {'description': 'Indian Rupee'},
    "BRL": {'description': 'Brazilian Real'},
    "MXN": {'description': 'Mexican Peso'},
    "ZAR": {'description': 'South African Rand'},
    "KRW": {'description': 'South Korean Won'},
    "SGD": {'description': 'Singapore Dollar'},
    "HKD": {'description': 'Hong Kong Dollar'},
    "TWD": {'description': 'Taiwan Dollar'},
    "THB": {'description': 'Thai Baht'},
    "MYR": {'description': 'Malaysian Ringgit'},
    "IDR": {'description': 'Indonesian Rupiah'},
    "PHP": {'description': 'Philippine Peso'},
    "VND": {'description': 'Vietnamese Dong'},
    "TRY": {'description': 'Turkish Lira'},
    "AED": {'description': 'UAE Dirham'},
    "SAR": {'description': 'Saudi Riyal'},
    "ILS": {'description': 'Israeli Shekel'},
    "EGP": {'description': 'Egyptian Pound'},
}

__all__ = [
    "CountryCodeISO2Enum",
    "CountryCodeISO3Enum",
    "USStateCodeEnum",
    "CanadianProvinceCodeEnum",
    "CompassDirection",
    "RelativeDirection",
    "WindDirection",
    "ContinentEnum",
    "UNRegionEnum",
    "LanguageCodeISO6391enum",
    "TimeZoneEnum",
    "CurrencyCodeISO4217Enum",
]