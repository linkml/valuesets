"""
Clinical Data Provenance Value Sets

Value sets for tracking the provenance and source of clinical data, including condition, visit, drug, and device exposure provenance types.

Generated from: clinical/provenance.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class ConditionProvenanceEnum(RichEnum):
    """
    Sources of condition/diagnosis records indicating how the condition was documented or determined.
    """
    # Enum members
    EHR_BILLING_DIAGNOSIS = "EHR_BILLING_DIAGNOSIS"
    EHR_CHIEF_COMPLAINT = "EHR_CHIEF_COMPLAINT"
    EHR_ENCOUNTER_DIAGNOSIS = "EHR_ENCOUNTER_DIAGNOSIS"
    EHR_EPISODE_ENTRY = "EHR_EPISODE_ENTRY"
    EHR_PROBLEM_LIST_ENTRY = "EHR_PROBLEM_LIST_ENTRY"
    FIRST_POSITION_CONDITION = "FIRST_POSITION_CONDITION"
    NLP_DERIVED = "NLP_DERIVED"
    OBSERVATION_RECORDED_FROM_EHR = "OBSERVATION_RECORDED_FROM_EHR"
    PATIENT_SELF_REPORTED_CONDITION = "PATIENT_SELF_REPORTED_CONDITION"
    PRIMARY_CONDITION = "PRIMARY_CONDITION"
    REFERRAL_RECORD = "REFERRAL_RECORD"
    SECONDARY_CONDITION = "SECONDARY_CONDITION"
    TUMOR_REGISTRY = "TUMOR_REGISTRY"
    WORKING_DIAGNOSIS = "WORKING_DIAGNOSIS"
    CLINICAL_DIAGNOSIS = "CLINICAL_DIAGNOSIS"

# Set metadata after class creation
ConditionProvenanceEnum._metadata = {
    "EHR_BILLING_DIAGNOSIS": {'description': 'Diagnosis recorded for billing purposes in EHR'},
    "EHR_CHIEF_COMPLAINT": {'description': 'Condition documented as chief complaint in EHR'},
    "EHR_ENCOUNTER_DIAGNOSIS": {'description': 'Diagnosis recorded during healthcare encounter'},
    "EHR_EPISODE_ENTRY": {'description': 'Condition recorded as part of care episode'},
    "EHR_PROBLEM_LIST_ENTRY": {'description': 'Condition on patient problem list in EHR'},
    "FIRST_POSITION_CONDITION": {'description': 'Primary diagnosis in first position on claim'},
    "NLP_DERIVED": {'description': 'Condition derived through natural language processing'},
    "OBSERVATION_RECORDED_FROM_EHR": {'description': 'Condition recorded as observation in EHR'},
    "PATIENT_SELF_REPORTED_CONDITION": {'description': 'Condition reported by the patient', 'aliases': ['PATIENT_SELF-REPORTED_CONDITION']},
    "PRIMARY_CONDITION": {'description': 'Primary condition for an encounter or episode'},
    "REFERRAL_RECORD": {'description': 'Condition documented in referral record'},
    "SECONDARY_CONDITION": {'description': 'Secondary or comorbid condition'},
    "TUMOR_REGISTRY": {'description': 'Condition from tumor registry'},
    "WORKING_DIAGNOSIS": {'description': 'Preliminary or working diagnosis'},
    "CLINICAL_DIAGNOSIS": {'description': 'Clinically confirmed diagnosis'},
}

class VisitProvenanceEnum(RichEnum):
    """
    Sources of healthcare visit/encounter records indicating the origin of the visit documentation.
    """
    # Enum members
    CASE_REPORT_FORM = "CASE_REPORT_FORM"
    CLAIM = "CLAIM"
    EHR = "EHR"
    EHR_ENCOUNTER_RECORD = "EHR_ENCOUNTER_RECORD"
    EHR_ADMISSION_NOTE = "EHR_ADMISSION_NOTE"
    EHR_DISCHARGE_RECORD = "EHR_DISCHARGE_RECORD"
    EHR_EMERGENCY_ROOM_NOTE = "EHR_EMERGENCY_ROOM_NOTE"
    EHR_INPATIENT_NOTE = "EHR_INPATIENT_NOTE"
    EHR_OUTPATIENT_NOTE = "EHR_OUTPATIENT_NOTE"
    INPATIENT_CLAIM = "INPATIENT_CLAIM"
    OUTPATIENT_CLAIM = "OUTPATIENT_CLAIM"
    FACILITY_CLAIM = "FACILITY_CLAIM"
    PROFESSIONAL_CLAIM = "PROFESSIONAL_CLAIM"
    PHARMACY_CLAIM = "PHARMACY_CLAIM"
    LAB = "LAB"
    REGISTRY = "REGISTRY"
    SURVEY = "SURVEY"
    PATIENT_SELF_REPORT = "PATIENT_SELF_REPORT"
    NLP = "NLP"
    HEALTH_INFORMATION_EXCHANGE_RECORD = "HEALTH_INFORMATION_EXCHANGE_RECORD"

# Set metadata after class creation
VisitProvenanceEnum._metadata = {
    "CASE_REPORT_FORM": {'description': 'Visit from clinical trial case report form'},
    "CLAIM": {'description': 'Visit derived from insurance claim'},
    "EHR": {'description': 'Visit from electronic health record'},
    "EHR_ENCOUNTER_RECORD": {'description': 'Visit from EHR encounter documentation'},
    "EHR_ADMISSION_NOTE": {'description': 'Visit from EHR admission note'},
    "EHR_DISCHARGE_RECORD": {'description': 'Visit from EHR discharge documentation'},
    "EHR_EMERGENCY_ROOM_NOTE": {'description': 'Visit from EHR emergency room note'},
    "EHR_INPATIENT_NOTE": {'description': 'Visit from EHR inpatient note'},
    "EHR_OUTPATIENT_NOTE": {'description': 'Visit from EHR outpatient note'},
    "INPATIENT_CLAIM": {'description': 'Visit from inpatient insurance claim'},
    "OUTPATIENT_CLAIM": {'description': 'Visit from outpatient insurance claim'},
    "FACILITY_CLAIM": {'description': 'Visit from facility insurance claim'},
    "PROFESSIONAL_CLAIM": {'description': 'Visit from professional services claim'},
    "PHARMACY_CLAIM": {'description': 'Visit from pharmacy claim'},
    "LAB": {'description': 'Visit from laboratory record'},
    "REGISTRY": {'description': 'Visit from disease or patient registry'},
    "SURVEY": {'description': 'Visit from patient survey'},
    "PATIENT_SELF_REPORT": {'description': 'Visit reported by patient', 'aliases': ['PATIENT_SELF-REPORT']},
    "NLP": {'description': 'Visit derived through natural language processing'},
    "HEALTH_INFORMATION_EXCHANGE_RECORD": {'description': 'Visit from health information exchange'},
}

class DrugExposureProvenanceEnum(RichEnum):
    """
    Sources of drug exposure records indicating how the medication information was documented.
    """
    # Enum members
    RANDOMIZED_DRUG = "RANDOMIZED_DRUG"
    PATIENT_SELF_REPORTED_MEDICATION = "PATIENT_SELF_REPORTED_MEDICATION"
    NLP_DERIVED = "NLP_DERIVED"
    PRESCRIPTION_DISPENSED_IN_PHARMACY = "PRESCRIPTION_DISPENSED_IN_PHARMACY"
    PHYSICIAN_ADMINISTERED_DRUG_FROM_EHR_ORDER = "PHYSICIAN_ADMINISTERED_DRUG_FROM_EHR_ORDER"
    DISPENSED_IN_OUTPATIENT_OFFICE = "DISPENSED_IN_OUTPATIENT_OFFICE"
    PRESCRIPTION_DISPENSED_THROUGH_MAIL_ORDER = "PRESCRIPTION_DISPENSED_THROUGH_MAIL_ORDER"
    PRESCRIPTION_WRITTEN = "PRESCRIPTION_WRITTEN"
    MEDICATION_LIST_ENTRY = "MEDICATION_LIST_ENTRY"
    PHYSICIAN_ADMINISTERED_DRUG_AS_PROCEDURE = "PHYSICIAN_ADMINISTERED_DRUG_AS_PROCEDURE"
    INPATIENT_ADMINISTRATION = "INPATIENT_ADMINISTRATION"

# Set metadata after class creation
DrugExposureProvenanceEnum._metadata = {
    "RANDOMIZED_DRUG": {'description': 'Drug from clinical trial randomization', 'aliases': ['RANDOMIZED DRUG']},
    "PATIENT_SELF_REPORTED_MEDICATION": {'description': 'Medication reported by patient', 'aliases': ['PATIENT SELF-REPORTED MEDICATION']},
    "NLP_DERIVED": {'description': 'Drug exposure derived through NLP', 'aliases': ['NLP DERIVED']},
    "PRESCRIPTION_DISPENSED_IN_PHARMACY": {'description': 'Prescription dispensed at pharmacy', 'aliases': ['PRESCRIPTION DISPENSED IN PHARMACY']},
    "PHYSICIAN_ADMINISTERED_DRUG_FROM_EHR_ORDER": {'description': 'Drug administered by physician from EHR order', 'aliases': ['PHYSICIAN ADMINISTERED DRUG (IDENTIFIED FROM EHR ORDER)']},
    "DISPENSED_IN_OUTPATIENT_OFFICE": {'description': 'Drug dispensed in outpatient office', 'aliases': ['DISPENSED IN OUTPATIENT OFFICE']},
    "PRESCRIPTION_DISPENSED_THROUGH_MAIL_ORDER": {'description': 'Prescription dispensed via mail order', 'aliases': ['PRESCRIPTION DISPENSED THROUGH MAIL ORDER']},
    "PRESCRIPTION_WRITTEN": {'description': 'Prescription written by provider', 'aliases': ['PRESCRIPTION WRITTEN']},
    "MEDICATION_LIST_ENTRY": {'description': 'Drug from medication list', 'aliases': ['MEDICATION LIST ENTRY']},
    "PHYSICIAN_ADMINISTERED_DRUG_AS_PROCEDURE": {'description': 'Drug administered as procedure', 'aliases': ['PHYSICIAN ADMINISTERED DRUG (IDENTIFIED AS PROCEDURE)']},
    "INPATIENT_ADMINISTRATION": {'description': 'Drug administered during inpatient stay', 'aliases': ['INPATIENT ADMINISTRATION']},
}

class StatusEnum(RichEnum):
    """
    Values indicating whether a condition or observation is present, absent, or of unknown status.
    """
    # Enum members
    PRESENT = "PRESENT"
    ABSENT = "ABSENT"
    UNKNOWN = "UNKNOWN"

# Set metadata after class creation
StatusEnum._metadata = {
    "PRESENT": {'description': 'Was present in the patient at observation time'},
    "ABSENT": {'description': 'Was absent in the patient at observation time'},
    "UNKNOWN": {'description': 'Status was unknown at observation time'},
}

class HistoricalStatusEnum(RichEnum):
    """
    Extended status values including historical presence of conditions or observations.
    """
    # Enum members
    PRESENT = "PRESENT"
    ABSENT = "ABSENT"
    UNKNOWN = "UNKNOWN"
    HISTORICAL = "HISTORICAL"

# Set metadata after class creation
HistoricalStatusEnum._metadata = {
    "PRESENT": {'description': 'Currently present in the patient'},
    "ABSENT": {'description': 'Currently absent in the patient'},
    "UNKNOWN": {'description': 'Current status is unknown'},
    "HISTORICAL": {'description': 'Was present in the patient historically but not currently'},
}

class ResearchProjectTypeEnum(RichEnum):
    """
    Types of research projects and studies
    """
    # Enum members
    CONSORTIUM = "CONSORTIUM"
    STUDY = "STUDY"

# Set metadata after class creation
ResearchProjectTypeEnum._metadata = {
    "CONSORTIUM": {'description': 'Multi-institutional research consortium'},
    "STUDY": {'description': 'Individual research study'},
}

__all__ = [
    "ConditionProvenanceEnum",
    "VisitProvenanceEnum",
    "DrugExposureProvenanceEnum",
    "StatusEnum",
    "HistoricalStatusEnum",
    "ResearchProjectTypeEnum",
]