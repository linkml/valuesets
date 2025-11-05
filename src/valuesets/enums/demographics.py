"""
valuesets-demographics

Demographic and social determinant value sets from NIH CDE and HL7 standards

Generated from: demographics.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class EducationLevel(RichEnum):
    """
    Years of education that a person has completed
    """
    # Enum members
    ELEM = "ELEM"
    SEC = "SEC"
    HS = "HS"
    SCOL = "SCOL"
    ASSOC = "ASSOC"
    BD = "BD"
    PB = "PB"
    GD = "GD"
    POSTG = "POSTG"

# Set metadata after class creation
EducationLevel._metadata = {
    "ELEM": {'description': 'Elementary School', 'meaning': 'HL7:v3-EducationLevel#ELEM'},
    "SEC": {'description': 'Some secondary or high school education', 'meaning': 'HL7:v3-EducationLevel#SEC'},
    "HS": {'description': 'High School or secondary school degree complete', 'meaning': 'HL7:v3-EducationLevel#HS'},
    "SCOL": {'description': 'Some College education', 'meaning': 'HL7:v3-EducationLevel#SCOL'},
    "ASSOC": {'description': "Associate's or technical degree complete", 'meaning': 'HL7:v3-EducationLevel#ASSOC'},
    "BD": {'description': 'College or baccalaureate degree complete', 'meaning': 'HL7:v3-EducationLevel#BD'},
    "PB": {'description': 'Some post-baccalaureate education', 'meaning': 'HL7:v3-EducationLevel#PB'},
    "GD": {'description': 'Graduate or professional Degree complete', 'meaning': 'HL7:v3-EducationLevel#GD'},
    "POSTG": {'description': 'Doctoral or post graduate education', 'meaning': 'HL7:v3-EducationLevel#POSTG'},
}

class MaritalStatus(RichEnum):
    """
    The domestic partnership status of a person
    """
    # Enum members
    ANNULLED = "ANNULLED"
    DIVORCED = "DIVORCED"
    INTERLOCUTORY = "INTERLOCUTORY"
    LEGALLY_SEPARATED = "LEGALLY_SEPARATED"
    MARRIED = "MARRIED"
    COMMON_LAW = "COMMON_LAW"
    POLYGAMOUS = "POLYGAMOUS"
    DOMESTIC_PARTNER = "DOMESTIC_PARTNER"
    UNMARRIED = "UNMARRIED"
    NEVER_MARRIED = "NEVER_MARRIED"
    WIDOWED = "WIDOWED"
    UNKNOWN = "UNKNOWN"

# Set metadata after class creation
MaritalStatus._metadata = {
    "ANNULLED": {'description': 'Marriage contract has been declared null and to not have existed', 'meaning': 'HL7:marital-status#A'},
    "DIVORCED": {'description': 'Marriage contract has been declared dissolved and inactive', 'meaning': 'HL7:marital-status#D'},
    "INTERLOCUTORY": {'description': 'Subject to an Interlocutory Decree', 'meaning': 'HL7:marital-status#I'},
    "LEGALLY_SEPARATED": {'description': 'Legally Separated', 'meaning': 'HL7:marital-status#L'},
    "MARRIED": {'description': 'A current marriage contract is active', 'meaning': 'HL7:marital-status#M'},
    "COMMON_LAW": {'description': "Marriage recognized in some jurisdictions based on parties' agreement", 'meaning': 'HL7:marital-status#C'},
    "POLYGAMOUS": {'description': 'More than 1 current spouse', 'meaning': 'HL7:marital-status#P'},
    "DOMESTIC_PARTNER": {'description': 'Person declares that a domestic partner relationship exists', 'meaning': 'HL7:marital-status#T'},
    "UNMARRIED": {'description': 'Currently not in a marriage contract', 'meaning': 'HL7:marital-status#U'},
    "NEVER_MARRIED": {'description': 'No marriage contract has ever been entered', 'meaning': 'HL7:marital-status#S'},
    "WIDOWED": {'description': 'The spouse has died', 'meaning': 'HL7:marital-status#W'},
    "UNKNOWN": {'description': 'A proper value is applicable, but not known', 'meaning': 'HL7:marital-status#UNK'},
}

class EmploymentStatus(RichEnum):
    """
    Employment status of a person
    """
    # Enum members
    FULL_TIME_EMPLOYED = "FULL_TIME_EMPLOYED"
    PART_TIME_EMPLOYED = "PART_TIME_EMPLOYED"
    UNEMPLOYED = "UNEMPLOYED"
    SELF_EMPLOYED = "SELF_EMPLOYED"
    RETIRED = "RETIRED"
    ACTIVE_MILITARY = "ACTIVE_MILITARY"
    CONTRACT = "CONTRACT"
    PER_DIEM = "PER_DIEM"
    LEAVE_OF_ABSENCE = "LEAVE_OF_ABSENCE"
    OTHER = "OTHER"
    TEMPORARILY_UNEMPLOYED = "TEMPORARILY_UNEMPLOYED"
    UNKNOWN = "UNKNOWN"

# Set metadata after class creation
EmploymentStatus._metadata = {
    "FULL_TIME_EMPLOYED": {'description': 'Full time employed', 'meaning': 'HL7:v2-0066#1'},
    "PART_TIME_EMPLOYED": {'description': 'Part time employed', 'meaning': 'HL7:v2-0066#2'},
    "UNEMPLOYED": {'description': 'Unemployed', 'meaning': 'HL7:v2-0066#3'},
    "SELF_EMPLOYED": {'description': 'Self-employed', 'meaning': 'HL7:v2-0066#4'},
    "RETIRED": {'description': 'Retired', 'meaning': 'HL7:v2-0066#5'},
    "ACTIVE_MILITARY": {'description': 'On active military duty', 'meaning': 'HL7:v2-0066#6'},
    "CONTRACT": {'description': 'Contract, per diem', 'meaning': 'HL7:v2-0066#C'},
    "PER_DIEM": {'description': 'Per Diem', 'meaning': 'HL7:v2-0066#D'},
    "LEAVE_OF_ABSENCE": {'description': 'Leave of absence', 'meaning': 'HL7:v2-0066#L'},
    "OTHER": {'description': 'Other', 'meaning': 'HL7:v2-0066#O'},
    "TEMPORARILY_UNEMPLOYED": {'description': 'Temporarily unemployed', 'meaning': 'HL7:v2-0066#T'},
    "UNKNOWN": {'description': 'Unknown', 'meaning': 'HL7:v2-0066#9'},
}

class HousingStatus(RichEnum):
    """
    Housing status of patients per UDS Plus HRSA standards
    """
    # Enum members
    HOMELESS_SHELTER = "HOMELESS_SHELTER"
    TRANSITIONAL = "TRANSITIONAL"
    DOUBLING_UP = "DOUBLING_UP"
    STREET = "STREET"
    PERMANENT_SUPPORTIVE_HOUSING = "PERMANENT_SUPPORTIVE_HOUSING"
    OTHER = "OTHER"
    UNKNOWN = "UNKNOWN"

# Set metadata after class creation
HousingStatus._metadata = {
    "HOMELESS_SHELTER": {'description': 'Patients who are living in a homeless shelter', 'meaning': 'HL7:udsplus-housing-status-codes#homeless-shelter'},
    "TRANSITIONAL": {'description': 'Patients who do not have a house and are in a transitional state', 'meaning': 'HL7:udsplus-housing-status-codes#transitional'},
    "DOUBLING_UP": {'description': 'Patients who are doubling up with others', 'meaning': 'HL7:udsplus-housing-status-codes#doubling-up'},
    "STREET": {'description': 'Patients who do not have a house and are living on the streets', 'meaning': 'HL7:udsplus-housing-status-codes#street'},
    "PERMANENT_SUPPORTIVE_HOUSING": {'description': 'Patients who are living in a permanent supportive housing', 'meaning': 'HL7:udsplus-housing-status-codes#permanent-supportive-housing'},
    "OTHER": {'description': 'Patients who have other kinds of accommodation', 'meaning': 'HL7:udsplus-housing-status-codes#other'},
    "UNKNOWN": {'description': 'Patients with Unknown accommodation', 'meaning': 'HL7:udsplus-housing-status-codes#unknown'},
}

class GenderIdentity(RichEnum):
    """
    Gender identity codes indicating an individual's personal sense of gender
    """
    # Enum members
    FEMALE = "FEMALE"
    MALE = "MALE"
    NON_BINARY = "NON_BINARY"
    ASKED_DECLINED = "ASKED_DECLINED"
    UNKNOWN = "UNKNOWN"

# Set metadata after class creation
GenderIdentity._metadata = {
    "FEMALE": {'description': 'Identifies as female gender (finding)', 'meaning': 'SNOMED:446141000124107'},
    "MALE": {'description': 'Identifies as male gender (finding)', 'meaning': 'SNOMED:446151000124109'},
    "NON_BINARY": {'description': 'Identifies as gender nonbinary', 'meaning': 'SNOMED:33791000087105'},
    "ASKED_DECLINED": {'description': 'Asked But Declined', 'meaning': 'HL7:asked-declined'},
    "UNKNOWN": {'description': 'A proper value is applicable, but not known', 'meaning': 'HL7:UNK'},
}

class OmbRaceCategory(RichEnum):
    """
    Office of Management and Budget (OMB) race category codes
    """
    # Enum members
    AMERICAN_INDIAN_OR_ALASKA_NATIVE = "AMERICAN_INDIAN_OR_ALASKA_NATIVE"
    ASIAN = "ASIAN"
    BLACK_OR_AFRICAN_AMERICAN = "BLACK_OR_AFRICAN_AMERICAN"
    NATIVE_HAWAIIAN_OR_OTHER_PACIFIC_ISLANDER = "NATIVE_HAWAIIAN_OR_OTHER_PACIFIC_ISLANDER"
    WHITE = "WHITE"
    OTHER_RACE = "OTHER_RACE"
    ASKED_BUT_UNKNOWN = "ASKED_BUT_UNKNOWN"
    UNKNOWN = "UNKNOWN"

# Set metadata after class creation
OmbRaceCategory._metadata = {
    "AMERICAN_INDIAN_OR_ALASKA_NATIVE": {'description': 'American Indian or Alaska Native', 'meaning': 'HL7:CDCREC#1002-5'},
    "ASIAN": {'description': 'Asian', 'meaning': 'HL7:CDCREC#2028-9'},
    "BLACK_OR_AFRICAN_AMERICAN": {'description': 'Black or African American', 'meaning': 'HL7:CDCREC#2054-5'},
    "NATIVE_HAWAIIAN_OR_OTHER_PACIFIC_ISLANDER": {'description': 'Native Hawaiian or Other Pacific Islander', 'meaning': 'HL7:CDCREC#2076-8'},
    "WHITE": {'description': 'White', 'meaning': 'HL7:CDCREC#2106-3'},
    "OTHER_RACE": {'description': 'Other Race (discouraged for statistical analysis)', 'meaning': 'HL7:CDCREC#2131-1'},
    "ASKED_BUT_UNKNOWN": {'description': 'asked but unknown', 'meaning': 'HL7:ASKU'},
    "UNKNOWN": {'description': 'unknown', 'meaning': 'HL7:UNK'},
}

class OmbEthnicityCategory(RichEnum):
    """
    Office of Management and Budget (OMB) ethnicity category codes
    """
    # Enum members
    HISPANIC_OR_LATINO = "HISPANIC_OR_LATINO"
    NOT_HISPANIC_OR_LATINO = "NOT_HISPANIC_OR_LATINO"
    ASKED_BUT_UNKNOWN = "ASKED_BUT_UNKNOWN"
    UNKNOWN = "UNKNOWN"

# Set metadata after class creation
OmbEthnicityCategory._metadata = {
    "HISPANIC_OR_LATINO": {'description': 'Hispanic or Latino', 'meaning': 'HL7:CDCREC#2135-2'},
    "NOT_HISPANIC_OR_LATINO": {'description': 'Not Hispanic or Latino', 'meaning': 'HL7:CDCREC#2186-5'},
    "ASKED_BUT_UNKNOWN": {'description': 'asked but unknown', 'meaning': 'HL7:ASKU'},
    "UNKNOWN": {'description': 'unknown', 'meaning': 'HL7:UNK'},
}

__all__ = [
    "EducationLevel",
    "MaritalStatus",
    "EmploymentStatus",
    "HousingStatus",
    "GenderIdentity",
    "OmbRaceCategory",
    "OmbEthnicityCategory",
]