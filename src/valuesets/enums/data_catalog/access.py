"""
Data Access and Status

Value sets for data access rights, dataset status, and update frequencies.

Based on DCAT (Data Catalog Vocabulary) 3.0, EU Vocabularies, and
ADMS (Asset Description Metadata Schema).

See: https://www.w3.org/TR/vocab-dcat-3/


Generated from: data_catalog/access.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class AccessRights(RichEnum):
    """
    Information about who can access the resource or an indication of
    its security status. Based on EU Vocabularies Access Rights authority list
    and DCAT recommendations.
    
    """
    # Enum members
    PUBLIC = "PUBLIC"
    RESTRICTED = "RESTRICTED"
    NON_PUBLIC = "NON_PUBLIC"
    EMBARGOED = "EMBARGOED"
    SENSITIVE = "SENSITIVE"

# Set metadata after class creation
AccessRights._metadata = {
    "PUBLIC": {'description': 'The resource is publicly accessible to everyone without\nrestrictions.\n', 'meaning': 'euvoc:access-right/PUBLIC', 'annotations': {'dcat_mapping': 'http://publications.europa.eu/resource/authority/access-right/PUBLIC'}, 'aliases': ['Open', 'Unrestricted']},
    "RESTRICTED": {'description': 'The resource is available under certain conditions or to\nauthorized users only. Access may require authentication,\npayment, or agreement to terms.\n', 'meaning': 'euvoc:access-right/RESTRICTED', 'annotations': {'dcat_mapping': 'http://publications.europa.eu/resource/authority/access-right/RESTRICTED'}, 'aliases': ['Limited Access']},
    "NON_PUBLIC": {'description': 'The resource is not publicly accessible. May include confidential,\nsensitive, or internal-use-only resources.\n', 'meaning': 'euvoc:access-right/NON_PUBLIC', 'annotations': {'dcat_mapping': 'http://publications.europa.eu/resource/authority/access-right/NON_PUBLIC'}, 'aliases': ['Closed', 'Private']},
    "EMBARGOED": {'description': 'The resource is temporarily restricted and will become publicly\navailable after a specific date or event.\n', 'annotations': {'common_in': 'academic publishing, research data'}},
    "SENSITIVE": {'description': 'The resource contains sensitive information requiring special\nhandling or access controls.\n', 'annotations': {'examples': 'PII, health data, classified information'}},
}

class DatasetStatus(RichEnum):
    """
    The status of a dataset in its lifecycle. Based on ADMS (Asset
    Description Metadata Schema) status vocabulary.
    
    """
    # Enum members
    COMPLETED = "COMPLETED"
    DEPRECATED = "DEPRECATED"
    UNDER_DEVELOPMENT = "UNDER_DEVELOPMENT"
    WITHDRAWN = "WITHDRAWN"

# Set metadata after class creation
DatasetStatus._metadata = {
    "COMPLETED": {'description': 'The dataset is complete and no further updates are planned.\nThe data is in its final form.\n', 'meaning': 'adms:Completed', 'aliases': ['Final', 'Finished']},
    "DEPRECATED": {'description': 'The dataset has been superseded by a newer version or is\nno longer recommended for use.\n', 'meaning': 'adms:Deprecated', 'aliases': ['Superseded', 'Legacy']},
    "UNDER_DEVELOPMENT": {'description': 'The dataset is still being created, collected, or processed.\nNot yet ready for production use.\n', 'meaning': 'adms:UnderDevelopment', 'aliases': ['In Progress', 'Draft', 'Work in Progress']},
    "WITHDRAWN": {'description': 'The dataset has been removed from availability, either\ntemporarily or permanently.\n', 'meaning': 'adms:Withdrawn', 'aliases': ['Retracted', 'Removed']},
}

class UpdateFrequency(RichEnum):
    """
    The frequency at which a dataset is updated with new data.
    Based on Dublin Core Collection Description Frequency Vocabulary.
    
    """
    # Enum members
    CONTINUOUS = "CONTINUOUS"
    DAILY = "DAILY"
    TWICE_WEEKLY = "TWICE_WEEKLY"
    WEEKLY = "WEEKLY"
    BIWEEKLY = "BIWEEKLY"
    MONTHLY = "MONTHLY"
    BIMONTHLY = "BIMONTHLY"
    QUARTERLY = "QUARTERLY"
    SEMIANNUAL = "SEMIANNUAL"
    ANNUAL = "ANNUAL"
    BIENNIAL = "BIENNIAL"
    TRIENNIAL = "TRIENNIAL"
    IRREGULAR = "IRREGULAR"
    NEVER = "NEVER"
    UNKNOWN = "UNKNOWN"

# Set metadata after class creation
UpdateFrequency._metadata = {
    "CONTINUOUS": {'description': 'Data is updated continuously or in real-time.', 'meaning': 'dcterms:Frequency', 'annotations': {'iso_duration': 'PT0S'}},
    "DAILY": {'description': 'Data is updated once per day.', 'annotations': {'iso_duration': 'P1D'}},
    "TWICE_WEEKLY": {'description': 'Data is updated twice per week.', 'annotations': {'iso_duration': 'P3D'}},
    "WEEKLY": {'description': 'Data is updated once per week.', 'annotations': {'iso_duration': 'P1W'}},
    "BIWEEKLY": {'description': 'Data is updated every two weeks.', 'annotations': {'iso_duration': 'P2W'}, 'aliases': ['Fortnightly']},
    "MONTHLY": {'description': 'Data is updated once per month.', 'annotations': {'iso_duration': 'P1M'}},
    "BIMONTHLY": {'description': 'Data is updated every two months.', 'annotations': {'iso_duration': 'P2M'}},
    "QUARTERLY": {'description': 'Data is updated once per quarter (every three months).', 'annotations': {'iso_duration': 'P3M'}},
    "SEMIANNUAL": {'description': 'Data is updated twice per year.', 'annotations': {'iso_duration': 'P6M'}, 'aliases': ['Biannual']},
    "ANNUAL": {'description': 'Data is updated once per year.', 'annotations': {'iso_duration': 'P1Y'}, 'aliases': ['Yearly']},
    "BIENNIAL": {'description': 'Data is updated every two years.', 'annotations': {'iso_duration': 'P2Y'}},
    "TRIENNIAL": {'description': 'Data is updated every three years.', 'annotations': {'iso_duration': 'P3Y'}},
    "IRREGULAR": {'description': 'Data is updated at irregular intervals.', 'aliases': ['As Needed', 'Ad Hoc']},
    "NEVER": {'description': 'Data is not updated after initial publication.\nHistorical or archival datasets.\n', 'aliases': ['Static', 'One-time']},
    "UNKNOWN": {'description': 'The update frequency is not known.'},
}

class DataServiceType(RichEnum):
    """
    The type of data service provided. Based on INSPIRE spatial data
    service types and common data access patterns.
    
    """
    # Enum members
    DISCOVERY = "DISCOVERY"
    VIEW = "VIEW"
    DOWNLOAD = "DOWNLOAD"
    TRANSFORMATION = "TRANSFORMATION"
    INVOKE = "INVOKE"
    SUBSCRIPTION = "SUBSCRIPTION"
    QUERY = "QUERY"

# Set metadata after class creation
DataServiceType._metadata = {
    "DISCOVERY": {'description': 'Service enabling search and discovery of datasets and services.\n', 'annotations': {'inspire_type': 'discovery'}, 'aliases': ['Catalog Service', 'Search Service']},
    "VIEW": {'description': 'Service enabling viewing or visualization of data without\nfull download.\n', 'annotations': {'inspire_type': 'view'}, 'aliases': ['Visualization Service', 'Display Service']},
    "DOWNLOAD": {'description': 'Service enabling bulk download of datasets or portions thereof.\n', 'annotations': {'inspire_type': 'download'}, 'aliases': ['Access Service', 'Retrieval Service']},
    "TRANSFORMATION": {'description': 'Service enabling transformation of data, such as format\nconversion or coordinate transformation.\n', 'annotations': {'inspire_type': 'transformation'}, 'aliases': ['Processing Service', 'Conversion Service']},
    "INVOKE": {'description': 'Service enabling invocation of operations on data, typically\nthrough an API.\n', 'annotations': {'inspire_type': 'invoke'}, 'aliases': ['API Service', 'Web Service']},
    "SUBSCRIPTION": {'description': 'Service enabling subscription to data updates or notifications.\n', 'aliases': ['Notification Service', 'Event Service']},
    "QUERY": {'description': 'Service enabling query-based access to data, returning\nfiltered or aggregated results.\n', 'aliases': ['SPARQL Endpoint', 'Query Service']},
}

__all__ = [
    "AccessRights",
    "DatasetStatus",
    "UpdateFrequency",
    "DataServiceType",
]