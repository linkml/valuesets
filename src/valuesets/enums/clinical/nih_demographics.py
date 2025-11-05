"""
NIH Demographics and Common Data Elements

Standard value sets for NIH Common Data Elements (CDEs) including demographics,
race, ethnicity, sex, and other clinical variables following NIH and OMB standards

Generated from: clinical/nih_demographics.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class RaceOMB1997Enum(RichEnum):
    """
    Race categories following OMB 1997 standards used by NIH and federal agencies.
    Respondents may select multiple races.
    """
    # Enum members
    AMERICAN_INDIAN_OR_ALASKA_NATIVE = "AMERICAN_INDIAN_OR_ALASKA_NATIVE"
    ASIAN = "ASIAN"
    BLACK_OR_AFRICAN_AMERICAN = "BLACK_OR_AFRICAN_AMERICAN"
    NATIVE_HAWAIIAN_OR_OTHER_PACIFIC_ISLANDER = "NATIVE_HAWAIIAN_OR_OTHER_PACIFIC_ISLANDER"
    WHITE = "WHITE"
    MORE_THAN_ONE_RACE = "MORE_THAN_ONE_RACE"
    UNKNOWN_OR_NOT_REPORTED = "UNKNOWN_OR_NOT_REPORTED"

# Set metadata after class creation
RaceOMB1997Enum._metadata = {
    "AMERICAN_INDIAN_OR_ALASKA_NATIVE": {'description': 'A person having origins in any of the original peoples of North and South America (including Central America), and who maintains tribal affiliation or community attachment', 'meaning': 'NCIT:C41259', 'annotations': {'omb_code': '1002-5'}},
    "ASIAN": {'description': 'A person having origins in any of the original peoples of the Far East, Southeast Asia, or the Indian subcontinent', 'meaning': 'NCIT:C41260', 'annotations': {'omb_code': '2028-9', 'includes': 'Cambodia, China, India, Japan, Korea, Malaysia, Pakistan, Philippine Islands, Thailand, Vietnam'}},
    "BLACK_OR_AFRICAN_AMERICAN": {'description': 'A person having origins in any of the black racial groups of Africa', 'meaning': 'NCIT:C16352', 'annotations': {'omb_code': '2054-5'}},
    "NATIVE_HAWAIIAN_OR_OTHER_PACIFIC_ISLANDER": {'description': 'A person having origins in any of the original peoples of Hawaii, Guam, Samoa, or other Pacific Islands', 'meaning': 'NCIT:C41219', 'annotations': {'omb_code': '2076-8'}},
    "WHITE": {'description': 'A person having origins in any of the original peoples of Europe, the Middle East, or North Africa', 'meaning': 'NCIT:C41261', 'annotations': {'omb_code': '2106-3'}},
    "MORE_THAN_ONE_RACE": {'description': 'Person identifies with more than one race category', 'meaning': 'NCIT:C67109', 'annotations': {'note': 'Added after 1997 revision to allow multiple race reporting'}},
    "UNKNOWN_OR_NOT_REPORTED": {'description': 'Race not known, not reported, or declined to answer', 'meaning': 'NCIT:C17998', 'annotations': {'aliases': 'Unknown, Not Reported, Prefer not to answer'}},
}

class EthnicityOMB1997Enum(RichEnum):
    """
    Ethnicity categories following OMB 1997 standards used by NIH and federal agencies
    """
    # Enum members
    HISPANIC_OR_LATINO = "HISPANIC_OR_LATINO"
    NOT_HISPANIC_OR_LATINO = "NOT_HISPANIC_OR_LATINO"
    UNKNOWN_OR_NOT_REPORTED = "UNKNOWN_OR_NOT_REPORTED"

# Set metadata after class creation
EthnicityOMB1997Enum._metadata = {
    "HISPANIC_OR_LATINO": {'description': 'A person of Cuban, Mexican, Puerto Rican, South or Central American, or other Spanish culture or origin, regardless of race', 'meaning': 'NCIT:C17459', 'annotations': {'omb_code': '2135-2'}},
    "NOT_HISPANIC_OR_LATINO": {'description': 'A person not of Hispanic or Latino origin', 'meaning': 'NCIT:C41222', 'annotations': {'omb_code': '2186-5'}},
    "UNKNOWN_OR_NOT_REPORTED": {'description': 'Ethnicity not known, not reported, or declined to answer', 'meaning': 'NCIT:C17998', 'annotations': {'aliases': 'Unknown, Not Reported, Prefer not to answer'}},
}

class BiologicalSexEnum(RichEnum):
    """
    Biological sex assigned at birth based on anatomical and physiological traits.
    Required by NIH as a biological variable in research.
    """
    # Enum members
    MALE = "MALE"
    FEMALE = "FEMALE"
    INTERSEX = "INTERSEX"
    UNKNOWN_OR_NOT_REPORTED = "UNKNOWN_OR_NOT_REPORTED"

# Set metadata after class creation
BiologicalSexEnum._metadata = {
    "MALE": {'description': 'Male sex assigned at birth', 'meaning': 'PATO:0000384'},
    "FEMALE": {'description': 'Female sex assigned at birth', 'meaning': 'PATO:0000383'},
    "INTERSEX": {'description': "Born with reproductive or sexual anatomy that doesn't fit typical definitions of male or female", 'meaning': 'NCIT:C45908', 'annotations': {'prevalence': '0.018% to 1.7%', 'note': 'May be assigned male or female at birth'}},
    "UNKNOWN_OR_NOT_REPORTED": {'description': 'Sex not known, not reported, or declined to answer', 'meaning': 'NCIT:C17998'},
}

class AgeGroupEnum(RichEnum):
    """
    Standard age groups used in NIH clinical research, particularly NINDS CDEs
    """
    # Enum members
    NEONATE = "NEONATE"
    INFANT = "INFANT"
    YOUNG_PEDIATRIC = "YOUNG_PEDIATRIC"
    PEDIATRIC = "PEDIATRIC"
    ADOLESCENT = "ADOLESCENT"
    YOUNG_ADULT = "YOUNG_ADULT"
    ADULT = "ADULT"
    OLDER_ADULT = "OLDER_ADULT"

# Set metadata after class creation
AgeGroupEnum._metadata = {
    "NEONATE": {'description': 'Birth to 28 days', 'meaning': 'NCIT:C16731', 'annotations': {'max_age_days': 28}},
    "INFANT": {'description': '29 days to less than 1 year', 'meaning': 'NCIT:C27956', 'annotations': {'min_age_days': 29, 'max_age_years': 1}},
    "YOUNG_PEDIATRIC": {'description': '0 to 5 years (NINDS CDE definition)', 'meaning': 'NCIT:C39299', 'annotations': {'min_age_years': 0, 'max_age_years': 5, 'ninds_category': True}},
    "PEDIATRIC": {'description': '6 to 12 years (NINDS CDE definition)', 'meaning': 'NCIT:C16423', 'annotations': {'min_age_years': 6, 'max_age_years': 12, 'ninds_category': True}},
    "ADOLESCENT": {'description': '13 to 17 years', 'meaning': 'NCIT:C27954', 'annotations': {'min_age_years': 13, 'max_age_years': 17}},
    "YOUNG_ADULT": {'description': '18 to 24 years', 'meaning': 'NCIT:C91107', 'annotations': {'min_age_years': 18, 'max_age_years': 24}},
    "ADULT": {'description': '25 to 64 years', 'meaning': 'NCIT:C17600', 'annotations': {'min_age_years': 25, 'max_age_years': 64}},
    "OLDER_ADULT": {'description': '65 years and older', 'meaning': 'NCIT:C16268', 'annotations': {'min_age_years': 65, 'aliases': 'Geriatric, Elderly, Senior'}},
}

class ParticipantVitalStatusEnum(RichEnum):
    """
    Vital status of a research participant in clinical studies
    """
    # Enum members
    ALIVE = "ALIVE"
    DECEASED = "DECEASED"
    UNKNOWN = "UNKNOWN"

# Set metadata after class creation
ParticipantVitalStatusEnum._metadata = {
    "ALIVE": {'description': 'Participant is living', 'meaning': 'NCIT:C37987'},
    "DECEASED": {'description': 'Participant is deceased', 'meaning': 'NCIT:C28554'},
    "UNKNOWN": {'description': 'Vital status unknown or lost to follow-up', 'meaning': 'NCIT:C17998'},
}

class RecruitmentStatusEnum(RichEnum):
    """
    Clinical trial or study recruitment status per NIH/ClinicalTrials.gov
    """
    # Enum members
    NOT_YET_RECRUITING = "NOT_YET_RECRUITING"
    RECRUITING = "RECRUITING"
    ENROLLING_BY_INVITATION = "ENROLLING_BY_INVITATION"
    ACTIVE_NOT_RECRUITING = "ACTIVE_NOT_RECRUITING"
    SUSPENDED = "SUSPENDED"
    TERMINATED = "TERMINATED"
    COMPLETED = "COMPLETED"
    WITHDRAWN = "WITHDRAWN"

# Set metadata after class creation
RecruitmentStatusEnum._metadata = {
    "NOT_YET_RECRUITING": {'description': 'Study has not started recruiting participants', 'meaning': 'NCIT:C211610'},
    "RECRUITING": {'description': 'Currently recruiting participants', 'meaning': 'NCIT:C142621'},
    "ENROLLING_BY_INVITATION": {'description': 'Enrolling participants by invitation only', 'meaning': 'NCIT:C211611'},
    "ACTIVE_NOT_RECRUITING": {'description': 'Study ongoing but not recruiting new participants', 'meaning': 'NCIT:C211612'},
    "SUSPENDED": {'description': 'Study temporarily stopped', 'meaning': 'NCIT:C211613'},
    "TERMINATED": {'description': 'Study stopped early and will not resume', 'meaning': 'NCIT:C70757'},
    "COMPLETED": {'description': 'Study has ended normally', 'meaning': 'NCIT:C70756'},
    "WITHDRAWN": {'description': 'Study withdrawn before enrollment', 'meaning': 'NCIT:C70758'},
}

class StudyPhaseEnum(RichEnum):
    """
    Clinical trial phases per FDA and NIH definitions
    """
    # Enum members
    EARLY_PHASE_1 = "EARLY_PHASE_1"
    PHASE_1 = "PHASE_1"
    PHASE_1_2 = "PHASE_1_2"
    PHASE_2 = "PHASE_2"
    PHASE_2_3 = "PHASE_2_3"
    PHASE_3 = "PHASE_3"
    PHASE_4 = "PHASE_4"
    NOT_APPLICABLE = "NOT_APPLICABLE"

# Set metadata after class creation
StudyPhaseEnum._metadata = {
    "EARLY_PHASE_1": {'description': 'Exploratory trials before traditional Phase 1', 'meaning': 'NCIT:C54721', 'annotations': {'aliases': 'Phase 0'}},
    "PHASE_1": {'description': 'Initial safety and dosage studies', 'meaning': 'NCIT:C15600', 'annotations': {'participants': '20-100'}},
    "PHASE_1_2": {'description': 'Combined Phase 1 and Phase 2 trial', 'meaning': 'NCIT:C15694'},
    "PHASE_2": {'description': 'Efficacy and side effects studies', 'meaning': 'NCIT:C15601', 'annotations': {'participants': '100-300'}},
    "PHASE_2_3": {'description': 'Combined Phase 2 and Phase 3 trial', 'meaning': 'NCIT:C49686'},
    "PHASE_3": {'description': 'Efficacy comparison with standard treatment', 'meaning': 'NCIT:C15602', 'annotations': {'participants': '300-3000'}},
    "PHASE_4": {'description': 'Post-marketing surveillance', 'meaning': 'NCIT:C15603', 'annotations': {'note': 'After FDA approval'}},
    "NOT_APPLICABLE": {'description': 'Not a phased clinical trial', 'meaning': 'NCIT:C48660', 'annotations': {'note': 'For observational studies, device trials, etc.'}},
}

__all__ = [
    "RaceOMB1997Enum",
    "EthnicityOMB1997Enum",
    "BiologicalSexEnum",
    "AgeGroupEnum",
    "ParticipantVitalStatusEnum",
    "RecruitmentStatusEnum",
    "StudyPhaseEnum",
]