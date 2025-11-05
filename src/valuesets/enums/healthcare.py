"""
valuesets-healthcare

Common Data Model Elements

Generated from: healthcare.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class HealthcareEncounterClassification(RichEnum):
    # Enum members
    INPATIENT_VISIT = "Inpatient Visit"
    EMERGENCY_ROOM_VISIT = "Emergency Room Visit"
    EMERGENCY_ROOM_AND_INPATIENT_VISIT = "Emergency Room and Inpatient Visit"
    NON_HOSPITAL_INSTITUTION_VISIT = "Non-hospital institution Visit"
    OUTPATIENT_VISIT = "Outpatient Visit"
    HOME_VISIT = "Home Visit"
    TELEHEALTH_VISIT = "Telehealth Visit"
    PHARMACY_VISIT = "Pharmacy Visit"
    LABORATORY_VISIT = "Laboratory Visit"
    AMBULANCE_VISIT = "Ambulance Visit"
    CASE_MANAGEMENT_VISIT = "Case Management Visit"

# Set metadata after class creation
HealthcareEncounterClassification._metadata = {
    "INPATIENT_VISIT": {'description': 'Person visiting hospital, at a Care Site, in bed, for duration of more than one day, with physicians and other Providers permanently available to deliver service around the clock'},
    "EMERGENCY_ROOM_VISIT": {'description': 'Person visiting dedicated healthcare institution for treating emergencies, at a Care Site, within one day, with physicians and Providers permanently available to deliver service around the clock'},
    "EMERGENCY_ROOM_AND_INPATIENT_VISIT": {'description': 'Person visiting ER followed by a subsequent Inpatient Visit, where Emergency department is part of hospital, and transition from the ER to other hospital departments is undefined'},
    "NON_HOSPITAL_INSTITUTION_VISIT": {'description': 'Person visiting dedicated institution for reasons of poor health, at a Care Site, long-term or permanently, with no physician but possibly other Providers permanently available to deliver service around the clock'},
    "OUTPATIENT_VISIT": {'description': 'Person visiting dedicated ambulatory healthcare institution, at a Care Site, within one day, without bed, with physicians or medical Providers delivering service during Visit'},
    "HOME_VISIT": {'description': 'Provider visiting Person, without a Care Site, within one day, delivering service'},
    "TELEHEALTH_VISIT": {'description': 'Patient engages with Provider through communication media'},
    "PHARMACY_VISIT": {'description': 'Person visiting pharmacy for dispensing of Drug, at a Care Site, within one day'},
    "LABORATORY_VISIT": {'description': 'Patient visiting dedicated institution, at a Care Site, within one day, for the purpose of a Measurement.'},
    "AMBULANCE_VISIT": {'description': 'Person using transportation service for the purpose of initiating one of the other Visits, without a Care Site, within one day, potentially with Providers accompanying the Visit and delivering service'},
    "CASE_MANAGEMENT_VISIT": {'description': 'Person interacting with healthcare system, without a Care Site, within a day, with no Providers involved, for administrative purposes'},
}

__all__ = [
    "HealthcareEncounterClassification",
]