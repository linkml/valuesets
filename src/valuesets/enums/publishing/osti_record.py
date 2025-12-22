"""
OSTI Record Metadata Value Sets

Value sets derived from the OSTI E-Link 2 record schema for
bibliographic and submission metadata.


Generated from: publishing/osti_record.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class OstiWorkflowStatus(RichEnum):
    """
    Workflow status codes for OSTI record revisions.
    """
    # Enum members
    R = "R"
    SA = "SA"
    SR = "SR"
    SO = "SO"
    SF = "SF"
    SX = "SX"
    SV = "SV"

# Set metadata after class creation
OstiWorkflowStatus._metadata = {
}

class OstiAccessLimitation(RichEnum):
    """
    Access and distribution limitation codes from OSTI.
    """
    # Enum members
    UNL = "UNL"
    OPN = "OPN"
    CPY = "CPY"
    OUO = "OUO"
    PROT = "PROT"
    PDOUO = "PDOUO"
    ECI = "ECI"
    PDSH = "PDSH"
    USO = "USO"
    LRD = "LRD"
    NAT = "NAT"
    NNPI = "NNPI"
    INTL = "INTL"
    PROP = "PROP"
    PAT = "PAT"
    OTHR = "OTHR"
    CUI = "CUI"

# Set metadata after class creation
OstiAccessLimitation._metadata = {
}

class OstiCollectionType(RichEnum):
    """
    Collection type codes used by OSTI for record origin.
    """
    # Enum members
    CHORUS = "CHORUS"
    DOE_GRANT = "DOE_GRANT"
    DOE_LAB = "DOE_LAB"

# Set metadata after class creation
OstiCollectionType._metadata = {
}

class OstiSensitivityFlag(RichEnum):
    """
    Sensitivity flags calculated by OSTI for released records.
    """
    # Enum members
    H = "H"
    S = "S"
    U = "U"
    X = "X"

# Set metadata after class creation
OstiSensitivityFlag._metadata = {
}

class OstiOrganizationIdentifierType(RichEnum):
    """
    Identifier types for OSTI organizations.
    """
    # Enum members
    AWARD_DOI = "AWARD_DOI"
    CN_DOE = "CN_DOE"
    CN_NONDOE = "CN_NONDOE"

# Set metadata after class creation
OstiOrganizationIdentifierType._metadata = {
}

class OstiProductType(RichEnum):
    """
    Product type codes from OSTI record metadata.
    """
    # Enum members
    AR = "AR"
    B = "B"
    CO = "CO"
    DA = "DA"
    FS = "FS"
    JA = "JA"
    MI = "MI"
    OT = "OT"
    P = "P"
    PD = "PD"
    SM = "SM"
    TD = "TD"
    TR = "TR"
    PA = "PA"

# Set metadata after class creation
OstiProductType._metadata = {
}

class OstiOrganizationType(RichEnum):
    """
    Organization role types used by OSTI.
    """
    # Enum members
    AUTHOR = "AUTHOR"
    CONTRIBUTING = "CONTRIBUTING"
    RESEARCHING = "RESEARCHING"
    SPONSOR = "SPONSOR"

# Set metadata after class creation
OstiOrganizationType._metadata = {
}

class OstiPersonType(RichEnum):
    """
    Person role types used by OSTI.
    """
    # Enum members
    AUTHOR = "AUTHOR"
    RELEASE = "RELEASE"
    CONTACT = "CONTACT"
    CONTRIBUTING = "CONTRIBUTING"
    PROT_CE = "PROT_CE"
    PROT_RO = "PROT_RO"
    SBIZ_PI = "SBIZ_PI"
    SBIZ_BO = "SBIZ_BO"

# Set metadata after class creation
OstiPersonType._metadata = {
}

class OstiContributorType(RichEnum):
    """
    Contributor role types used by OSTI.
    """
    # Enum members
    CHAIR = "Chair"
    DATACOLLECTOR = "DataCollector"
    DATACURATOR = "DataCurator"
    DATAMANAGER = "DataManager"
    DISTRIBUTOR = "Distributor"
    EDITOR = "Editor"
    HOSTINGINSTITUTION = "HostingInstitution"
    PRODUCER = "Producer"
    PROJECTLEADER = "ProjectLeader"
    PROJECTMANAGER = "ProjectManager"
    PROJECTMEMBER = "ProjectMember"
    REGISTRATIONAGENCY = "RegistrationAgency"
    REGISTRATIONAUTHORITY = "RegistrationAuthority"
    RELATEDPERSON = "RelatedPerson"
    REVIEWER = "Reviewer"
    REVIEWASSISTANT = "ReviewAssistant"
    REVIEWEREXTERNAL = "ReviewerExternal"
    RIGHTSHOLDER = "RightsHolder"
    STATSREVIEWER = "StatsReviewer"
    SUPERVISOR = "Supervisor"
    TRANSLATOR = "Translator"
    WORKPACKAGELEADER = "WorkPackageLeader"
    OTHER = "Other"

# Set metadata after class creation
OstiContributorType._metadata = {
}

class OstiRelatedIdentifierType(RichEnum):
    """
    Identifier types for related resources in OSTI.
    """
    # Enum members
    ARK = "ARK"
    ARXIV = "arXiv"
    BIBCODE = "bibcode"
    DOI = "DOI"
    EAN13 = "EAN13"
    EISSN = "EISSN"
    IGSN = "IGSN"
    ISBN = "ISBN"
    ISSN = "ISSN"
    ISTC = "ISTC"
    HANDLE = "Handle"
    LISSN = "LISSN"
    LSID = "LSID"
    OTHER = "OTHER"
    PMCID = "PMCID"
    PMID = "PMID"
    PURL = "PURL"
    UPC = "UPC"
    URI = "URI"
    URL = "URL"
    URN = "URN"
    UUID = "UUID"
    W3ID = "w3id"

# Set metadata after class creation
OstiRelatedIdentifierType._metadata = {
}

class OstiRelationType(RichEnum):
    """
    Relationship types between records in OSTI.
    """
    # Enum members
    BASEDONDATA = "BasedOnData"
    CITES = "Cites"
    COMPILES = "Compiles"
    CONTINUES = "Continues"
    DESCRIBES = "Describes"
    DOCUMENTS = "Documents"
    FINANCES = "Finances"
    HASCOMMENT = "HasComment"
    HASDERIVATION = "HasDerivation"
    HASMETADATA = "HasMetadata"
    HASPART = "HasPart"
    HASRELATEDMATERIAL = "HasRelatedMaterial"
    HASREPLY = "HasReply"
    HASREVIEW = "HasReview"
    HASVERSION = "HasVersion"
    ISBASEDON = "IsBasedOn"
    ISBASISFOR = "IsBasisFor"
    ISCITEDBY = "IsCitedBy"
    ISCOMMENTON = "IsCommentOn"
    ISCOMPILEDBY = "IsCompiledBy"
    ISCONTINUEDBY = "IsContinuedBy"
    ISDATABASISFOR = "IsDataBasisFor"
    ISDERIVEDFROM = "IsDerivedFrom"
    ISDESCRIBEDBY = "IsDescribedBy"
    ISDOCUMENTEDBY = "IsDocumentedBy"
    ISFINANCEDBY = "IsFinancedBy"
    ISIDENTICALTO = "IsIdenticalTo"
    ISMETADATAFOR = "IsMetadataFor"
    ISNEWVERSIONOF = "IsNewVersionOf"
    ISOBSOLETEDBY = "IsObsoletedBy"
    ISORIGINALFORMOF = "IsOriginalFormOf"
    ISPARTOF = "IsPartOf"
    ISPREVIOUSVERSIONOF = "IsPreviousVersionOf"
    ISREFERENCEDBY = "IsReferencedBy"
    ISRELATEDMATERIAL = "IsRelatedMaterial"
    ISREPLYTO = "IsReplyTo"
    ISREQUIREDBY = "IsRequiredBy"
    ISREVIEWEDBY = "IsReviewedBy"
    ISREVIEWOF = "IsReviewOf"
    ISSOURCEOF = "IsSourceOf"
    ISSUPPLEMENTEDBY = "IsSupplementedBy"
    ISSUPPLEMENTTO = "IsSupplementTo"
    ISVARIANTFORMOF = "IsVariantFormOf"
    ISVERSIONOF = "IsVersionOf"
    OBSOLETES = "Obsoletes"
    REFERENCES = "References"
    REQUIRES = "Requires"
    REVIEWS = "Reviews"

# Set metadata after class creation
OstiRelationType._metadata = {
}

class OstiIdentifierType(RichEnum):
    """
    Identifier type codes from OSTI record metadata.
    """
    # Enum members
    AUTH_REV = "AUTH_REV"
    CN_DOE = "CN_DOE"
    CN_NONDOE = "CN_NONDOE"
    CODEN = "CODEN"
    DOE_DOCKET = "DOE_DOCKET"
    EDB = "EDB"
    ETDE_RN = "ETDE_RN"
    INIS_RN = "INIS_RN"
    ISBN = "ISBN"
    ISSN = "ISSN"
    LEGACY = "LEGACY"
    NSA = "NSA"
    OPN_ACC = "OPN_ACC"
    OTHER_ID = "OTHER_ID"
    PATENT = "PATENT"
    PROJ_ID = "PROJ_ID"
    PROP_REV = "PROP_REV"
    REF = "REF"
    REL_TRN = "REL_TRN"
    RN = "RN"
    TRN = "TRN"
    TVI = "TVI"
    USER_VER = "USER_VER"
    WORK_AUTH = "WORK_AUTH"
    WORK_PROP = "WORK_PROP"

# Set metadata after class creation
OstiIdentifierType._metadata = {
}

class OstiGeolocationType(RichEnum):
    """
    Geolocation shape types in OSTI record metadata.
    """
    # Enum members
    POINT = "POINT"
    BOX = "BOX"
    POLYGON = "POLYGON"

# Set metadata after class creation
OstiGeolocationType._metadata = {
}

class OstiMediaLocationType(RichEnum):
    """
    Location indicators for OSTI media files and sets.
    """
    # Enum members
    L = "L"
    O = "O"

# Set metadata after class creation
OstiMediaLocationType._metadata = {
}

__all__ = [
    "OstiWorkflowStatus",
    "OstiAccessLimitation",
    "OstiCollectionType",
    "OstiSensitivityFlag",
    "OstiOrganizationIdentifierType",
    "OstiProductType",
    "OstiOrganizationType",
    "OstiPersonType",
    "OstiContributorType",
    "OstiRelatedIdentifierType",
    "OstiRelationType",
    "OstiIdentifierType",
    "OstiGeolocationType",
    "OstiMediaLocationType",
]