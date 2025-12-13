"""

Generated from: data/data_absent_reason.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class DataAbsentEnum(RichEnum):
    """
    Used to specify why the normally expected content of the data element is missing.
    """
    # Enum members
    UNKNOWN = "unknown"
    ASKED_UNKNOWN = "asked-unknown"
    TEMP_UNKNOWN = "temp-unknown"
    NOT_ASKED = "not-asked"
    ASKED_DECLINED = "asked-declined"
    MASKED = "masked"
    NOT_APPLICABLE = "not-applicable"
    UNSUPPORTED = "unsupported"
    AS_TEXT = "as-text"
    ERROR = "error"
    NOT_A_NUMBER = "not-a-number"
    NEGATIVE_INFINITY = "negative-infinity"
    POSITIVE_INFINITY = "positive-infinity"
    NOT_PERFORMED = "not-performed"
    NOT_PERMITTED = "not-permitted"

# Set metadata after class creation
DataAbsentEnum._metadata = {
    "UNKNOWN": {'description': 'The value is expected to exist but is not known.', 'meaning': 'fhir_data_absent_reason:unknown'},
    "ASKED_UNKNOWN": {'description': 'The source was asked but does not know the value.', 'meaning': 'fhir_data_absent_reason:asked-unknown'},
    "TEMP_UNKNOWN": {'description': 'There is reason to expect (from the workflow) that the value may become known.', 'meaning': 'fhir_data_absent_reason:temp-unknown'},
    "NOT_ASKED": {'description': "The workflow didn't lead to this value being known.", 'meaning': 'fhir_data_absent_reason:not-asked'},
    "ASKED_DECLINED": {'description': 'The source was asked but declined to answer.', 'meaning': 'fhir_data_absent_reason:asked-declined'},
    "MASKED": {'description': 'The information is not available due to security, privacy or related reasons.', 'meaning': 'fhir_data_absent_reason:masked'},
    "NOT_APPLICABLE": {'description': 'There is no proper value for this element (e.g. last menstrual period for a male).', 'meaning': 'fhir_data_absent_reason:not-applicable'},
    "UNSUPPORTED": {'description': "The source system wasn't capable of supporting this element.", 'meaning': 'fhir_data_absent_reason:unsupported'},
    "AS_TEXT": {'description': 'The content of the data is represented in the resource narrative.', 'meaning': 'fhir_data_absent_reason:as-text'},
    "ERROR": {'description': 'Some system or workflow process error means that the information is not available.', 'meaning': 'fhir_data_absent_reason:error'},
    "NOT_A_NUMBER": {'description': 'The numeric value is undefined or unrepresentable due to a floating point processing error.', 'meaning': 'fhir_data_absent_reason:not-a-number'},
    "NEGATIVE_INFINITY": {'description': 'The numeric value is excessively low and unrepresentable due to a floating point processing error.', 'meaning': 'fhir_data_absent_reason:negative-infinity'},
    "POSITIVE_INFINITY": {'description': 'The numeric value is excessively high and unrepresentable due to a floating point processing error.', 'meaning': 'fhir_data_absent_reason:positive-infinity'},
    "NOT_PERFORMED": {'description': 'The value is not available because the observation procedure (test, etc.) was not performed.', 'meaning': 'fhir_data_absent_reason:not-performed'},
    "NOT_PERMITTED": {'description': 'The value is not permitted in this context (e.g. due to profiles, or the base data types).', 'meaning': 'fhir_data_absent_reason:not-permitted'},
}

__all__ = [
    "DataAbsentEnum",
]