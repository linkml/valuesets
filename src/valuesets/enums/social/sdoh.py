"""
Social Determinants of Health Value Sets

Value sets for Social Determinants of Health (SDOH) domains and related observations, based on the Gravity Project standards.

Generated from: social/sdoh.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class GravitySdohDomainEnum(RichEnum):
    """
    Social Determinants of Health domains as defined by the Gravity Project. These domains represent key areas of social need that impact health outcomes.
    """
    # Enum members
    FOOD_INSECURITY = "FOOD_INSECURITY"
    HOUSING_INSTABILITY = "HOUSING_INSTABILITY"
    HOMELESSNESS = "HOMELESSNESS"
    INADEQUATE_HOUSING = "INADEQUATE_HOUSING"
    TRANSPORTATION_INSECURITY = "TRANSPORTATION_INSECURITY"
    FINANCIAL_INSECURITY = "FINANCIAL_INSECURITY"
    MATERIAL_HARDSHIP = "MATERIAL_HARDSHIP"
    EMPLOYMENT_STATUS = "EMPLOYMENT_STATUS"
    EDUCATIONAL_ATTAINMENT = "EDUCATIONAL_ATTAINMENT"
    VETERAN_STATUS = "VETERAN_STATUS"
    STRESS = "STRESS"
    SOCIAL_CONNECTION = "SOCIAL_CONNECTION"
    INTIMATE_PARTNER_VIOLENCE = "INTIMATE_PARTNER_VIOLENCE"
    ELDER_ABUSE = "ELDER_ABUSE"
    HEALTH_LITERACY = "HEALTH_LITERACY"
    MEDICAL_COST_BURDEN = "MEDICAL_COST_BURDEN"
    HEALTH_INSURANCE_COVERAGE_STATUS = "HEALTH_INSURANCE_COVERAGE_STATUS"
    DIGITAL_LITERACY = "DIGITAL_LITERACY"
    DIGITAL_ACCESS = "DIGITAL_ACCESS"
    UTILITY_INSECURITY = "UTILITY_INSECURITY"

# Set metadata after class creation
GravitySdohDomainEnum._metadata = {
    "FOOD_INSECURITY": {'description': 'Limited or uncertain availability of nutritionally adequate and safe foods', 'meaning': 'NCIT:C171542', 'aliases': ['Food Insecurity']},
    "HOUSING_INSTABILITY": {'description': 'Challenges with housing including trouble paying rent or frequent moves', 'meaning': 'SNOMED:1156191002', 'aliases': ['Housing instability']},
    "HOMELESSNESS": {'description': 'The condition of lacking stable, safe, and adequate housing', 'meaning': 'SNOMED:32911000', 'aliases': ['Homeless']},
    "INADEQUATE_HOUSING": {'description': 'Housing that does not meet basic standards for safety and habitability', 'meaning': 'SNOMED:105531004', 'aliases': ['Unsatisfactory housing conditions']},
    "TRANSPORTATION_INSECURITY": {'description': 'Lack of reliable, safe, and affordable transportation'},
    "FINANCIAL_INSECURITY": {'description': 'Inability to meet basic financial needs and obligations'},
    "MATERIAL_HARDSHIP": {'description': 'Difficulty affording basic necessities such as food, housing, and utilities'},
    "EMPLOYMENT_STATUS": {'description': 'Current employment situation and stability', 'meaning': 'NCIT:C179143', 'aliases': ['Employment Status']},
    "EDUCATIONAL_ATTAINMENT": {'description': 'Highest level of education completed', 'meaning': 'EFO:0011015', 'aliases': ['educational attainment']},
    "VETERAN_STATUS": {'description': 'Military veteran status and related needs'},
    "STRESS": {'description': 'Psychological stress affecting health and wellbeing', 'meaning': 'NCIT:C35041', 'aliases': ['Stress']},
    "SOCIAL_CONNECTION": {'description': 'Quality and quantity of social relationships and support networks'},
    "INTIMATE_PARTNER_VIOLENCE": {'description': 'Abuse occurring between people in a close relationship', 'meaning': 'MESH:D000066511', 'aliases': ['IPV', 'domestic violence', 'Intimate Partner Violence']},
    "ELDER_ABUSE": {'description': 'Abuse, neglect, or exploitation of older adults', 'meaning': 'MESH:D004552', 'aliases': ['Elder Abuse']},
    "HEALTH_LITERACY": {'description': 'Ability to obtain, process, and understand health information', 'meaning': 'MESH:D057220', 'aliases': ['Health Literacy']},
    "MEDICAL_COST_BURDEN": {'description': 'Financial strain from healthcare costs'},
    "HEALTH_INSURANCE_COVERAGE_STATUS": {'description': 'Status of health insurance coverage', 'meaning': 'NCIT:C157356', 'aliases': ['Health Insurance']},
    "DIGITAL_LITERACY": {'description': 'Ability to use digital technology and access digital resources'},
    "DIGITAL_ACCESS": {'description': 'Access to internet and digital devices'},
    "UTILITY_INSECURITY": {'description': 'Difficulty paying for utilities such as electricity, gas, or water'},
}

class EducationalAttainmentEnum(RichEnum):
    """
    Levels of educational attainment for survey and demographic purposes. Based on standard US educational categories.
    """
    # Enum members
    EIGHTH_GRADE_OR_LESS = "EIGHTH_GRADE_OR_LESS"
    HIGH_SCHOOL_NO_DIPLOMA = "HIGH_SCHOOL_NO_DIPLOMA"
    HIGH_SCHOOL_GRADUATE_GED = "HIGH_SCHOOL_GRADUATE_GED"
    SOME_COLLEGE_NO_DEGREE = "SOME_COLLEGE_NO_DEGREE"
    ASSOCIATE_DEGREE = "ASSOCIATE_DEGREE"
    BACHELORS_DEGREE = "BACHELORS_DEGREE"
    MASTERS_DEGREE = "MASTERS_DEGREE"
    DOCTORAL_DEGREE = "DOCTORAL_DEGREE"

# Set metadata after class creation
EducationalAttainmentEnum._metadata = {
    "EIGHTH_GRADE_OR_LESS": {'description': 'Completed 8th grade or less', 'aliases': ['8TH_GRADE_OR_LESS', 'elementary']},
    "HIGH_SCHOOL_NO_DIPLOMA": {'description': 'Some high school but no diploma', 'meaning': 'NCIT:C76123', 'aliases': ['some high school', 'Not High School Graduate']},
    "HIGH_SCHOOL_GRADUATE_GED": {'description': 'High school graduate or GED equivalent', 'meaning': 'NCIT:C67136', 'aliases': ['high school diploma', 'GED', 'High School Completion']},
    "SOME_COLLEGE_NO_DEGREE": {'description': 'Some college or technical school but no degree', 'aliases': ['SOME_COLLEGE_OR_TECH_NO_DEGREE']},
    "ASSOCIATE_DEGREE": {'description': 'Associate degree (2-year college)', 'meaning': 'NCIT:C71344', 'aliases': ['Associate of Science']},
    "BACHELORS_DEGREE": {'description': "Bachelor's degree (4-year college)", 'meaning': 'NCIT:C71345', 'aliases': ['COLLEGE_OR_TECH_WITH_DEGREE', 'Bachelor of Arts']},
    "MASTERS_DEGREE": {'description': "Master's degree", 'meaning': 'NCIT:C39452', 'aliases': ['Master of Science']},
    "DOCTORAL_DEGREE": {'description': 'Doctoral or professional degree (PhD, MD, JD, etc.)', 'meaning': 'NCIT:C39387', 'aliases': ['MASTERS_OR_DOCTORAL_DEGREE', 'Doctor of Philosophy']},
}

__all__ = [
    "GravitySdohDomainEnum",
    "EducationalAttainmentEnum",
]