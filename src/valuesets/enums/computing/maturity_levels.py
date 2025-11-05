"""
Software and Technology Maturity Levels

Value sets for assessing maturity levels of software, technology, and standards across different frameworks and domains.

Generated from: computing/maturity_levels.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class TechnologyReadinessLevel(RichEnum):
    """
    NASA's Technology Readiness Level scale for assessing the maturity of technologies from basic research through operational deployment
    """
    # Enum members
    TRL_1 = "TRL_1"
    TRL_2 = "TRL_2"
    TRL_3 = "TRL_3"
    TRL_4 = "TRL_4"
    TRL_5 = "TRL_5"
    TRL_6 = "TRL_6"
    TRL_7 = "TRL_7"
    TRL_8 = "TRL_8"
    TRL_9 = "TRL_9"

# Set metadata after class creation
TechnologyReadinessLevel._metadata = {
    "TRL_1": {'description': 'Basic principles observed and reported'},
    "TRL_2": {'description': 'Technology concept and/or application formulated'},
    "TRL_3": {'description': 'Analytical and experimental critical function and/or characteristic proof of concept'},
    "TRL_4": {'description': 'Component and/or breadboard validation in laboratory environment'},
    "TRL_5": {'description': 'Component and/or breadboard validation in relevant environment'},
    "TRL_6": {'description': 'System/subsystem model or prototype demonstration in a relevant environment'},
    "TRL_7": {'description': 'System prototype demonstration in an operational environment'},
    "TRL_8": {'description': 'Actual system completed and qualified through test and demonstration'},
    "TRL_9": {'description': 'Actual system proven through successful mission operations'},
}

class SoftwareMaturityLevel(RichEnum):
    """
    General software maturity assessment levels
    """
    # Enum members
    ALPHA = "ALPHA"
    BETA = "BETA"
    RELEASE_CANDIDATE = "RELEASE_CANDIDATE"
    STABLE = "STABLE"
    MATURE = "MATURE"
    LEGACY = "LEGACY"
    DEPRECATED = "DEPRECATED"
    OBSOLETE = "OBSOLETE"

# Set metadata after class creation
SoftwareMaturityLevel._metadata = {
    "ALPHA": {'description': 'Early development stage with basic functionality, may be unstable'},
    "BETA": {'description': 'Feature-complete but may contain bugs, ready for testing'},
    "RELEASE_CANDIDATE": {'description': 'Stable version ready for final testing before release'},
    "STABLE": {'description': 'Production-ready with proven stability and reliability'},
    "MATURE": {'description': 'Well-established with extensive usage and proven track record'},
    "LEGACY": {'description': 'Older version still in use but no longer actively developed'},
    "DEPRECATED": {'description': 'No longer recommended for use, superseded by newer versions'},
    "OBSOLETE": {'description': 'No longer supported or maintained'},
}

class CapabilityMaturityLevel(RichEnum):
    """
    CMMI levels for assessing organizational process maturity in software development
    """
    # Enum members
    LEVEL_1 = "LEVEL_1"
    LEVEL_2 = "LEVEL_2"
    LEVEL_3 = "LEVEL_3"
    LEVEL_4 = "LEVEL_4"
    LEVEL_5 = "LEVEL_5"

# Set metadata after class creation
CapabilityMaturityLevel._metadata = {
    "LEVEL_1": {'description': 'Initial - Processes are unpredictable, poorly controlled, and reactive'},
    "LEVEL_2": {'description': 'Managed - Processes are characterized for projects and reactive'},
    "LEVEL_3": {'description': 'Defined - Processes are characterized for the organization and proactive'},
    "LEVEL_4": {'description': 'Quantitatively Managed - Processes are measured and controlled'},
    "LEVEL_5": {'description': 'Optimizing - Focus on continuous process improvement'},
}

class StandardsMaturityLevel(RichEnum):
    """
    Maturity levels for standards and specifications
    """
    # Enum members
    DRAFT = "DRAFT"
    WORKING_DRAFT = "WORKING_DRAFT"
    COMMITTEE_DRAFT = "COMMITTEE_DRAFT"
    CANDIDATE_RECOMMENDATION = "CANDIDATE_RECOMMENDATION"
    PROPOSED_STANDARD = "PROPOSED_STANDARD"
    STANDARD = "STANDARD"
    MATURE_STANDARD = "MATURE_STANDARD"
    SUPERSEDED = "SUPERSEDED"
    WITHDRAWN = "WITHDRAWN"

# Set metadata after class creation
StandardsMaturityLevel._metadata = {
    "DRAFT": {'description': 'Initial draft under development'},
    "WORKING_DRAFT": {'description': 'Work in progress by working group'},
    "COMMITTEE_DRAFT": {'description': 'Draft reviewed by committee'},
    "CANDIDATE_RECOMMENDATION": {'description': 'Mature draft ready for implementation testing'},
    "PROPOSED_STANDARD": {'description': 'Stable specification ready for adoption'},
    "STANDARD": {'description': 'Approved and published standard'},
    "MATURE_STANDARD": {'description': 'Well-established standard with wide adoption'},
    "SUPERSEDED": {'description': 'Replaced by a newer version'},
    "WITHDRAWN": {'description': 'No longer valid or recommended'},
}

class ProjectMaturityLevel(RichEnum):
    """
    General project development maturity assessment
    """
    # Enum members
    CONCEPT = "CONCEPT"
    PLANNING = "PLANNING"
    DEVELOPMENT = "DEVELOPMENT"
    TESTING = "TESTING"
    PILOT = "PILOT"
    PRODUCTION = "PRODUCTION"
    MAINTENANCE = "MAINTENANCE"
    END_OF_LIFE = "END_OF_LIFE"

# Set metadata after class creation
ProjectMaturityLevel._metadata = {
    "CONCEPT": {'description': 'Initial idea or concept stage'},
    "PLANNING": {'description': 'Project planning and design phase'},
    "DEVELOPMENT": {'description': 'Active development in progress'},
    "TESTING": {'description': 'Testing and quality assurance phase'},
    "PILOT": {'description': 'Limited deployment or pilot testing'},
    "PRODUCTION": {'description': 'Full production deployment'},
    "MAINTENANCE": {'description': 'Maintenance and support mode'},
    "END_OF_LIFE": {'description': 'Project reaching end of lifecycle'},
}

class DataMaturityLevel(RichEnum):
    """
    Levels of data quality, governance, and organizational maturity
    """
    # Enum members
    RAW = "RAW"
    CLEANED = "CLEANED"
    STANDARDIZED = "STANDARDIZED"
    INTEGRATED = "INTEGRATED"
    CURATED = "CURATED"
    PUBLISHED = "PUBLISHED"
    ARCHIVED = "ARCHIVED"

# Set metadata after class creation
DataMaturityLevel._metadata = {
    "RAW": {'description': 'Unprocessed, uncleaned data'},
    "CLEANED": {'description': 'Basic cleaning and validation applied'},
    "STANDARDIZED": {'description': 'Conforms to defined standards and formats'},
    "INTEGRATED": {'description': 'Combined with other data sources'},
    "CURATED": {'description': 'Expert-reviewed and validated'},
    "PUBLISHED": {'description': 'Publicly available with proper metadata'},
    "ARCHIVED": {'description': 'Long-term preservation with access controls'},
}

class OpenSourceMaturityLevel(RichEnum):
    """
    Maturity assessment for open source projects
    """
    # Enum members
    EXPERIMENTAL = "EXPERIMENTAL"
    EMERGING = "EMERGING"
    ESTABLISHED = "ESTABLISHED"
    MATURE = "MATURE"
    DECLINING = "DECLINING"
    ARCHIVED = "ARCHIVED"

# Set metadata after class creation
OpenSourceMaturityLevel._metadata = {
    "EXPERIMENTAL": {'description': 'Early experimental project'},
    "EMERGING": {'description': 'Gaining traction and contributors'},
    "ESTABLISHED": {'description': 'Stable with active community'},
    "MATURE": {'description': 'Well-established with proven governance'},
    "DECLINING": {'description': 'Decreasing activity and maintenance'},
    "ARCHIVED": {'description': 'No longer actively maintained'},
}

__all__ = [
    "TechnologyReadinessLevel",
    "SoftwareMaturityLevel",
    "CapabilityMaturityLevel",
    "StandardsMaturityLevel",
    "ProjectMaturityLevel",
    "DataMaturityLevel",
    "OpenSourceMaturityLevel",
]