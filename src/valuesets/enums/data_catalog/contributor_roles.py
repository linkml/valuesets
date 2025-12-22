"""
DataCite Contributor Types

Contributor type classifications from DataCite 4.6.

This enum is separate from CRediT (Contributor Roles Taxonomy) which
focuses on research contribution activities. DataCite contributor types
describe organizational and functional roles in resource creation and
management.

For research contribution activities, see ResearchRole in academic/research.yaml
which uses CRediT terms.

See: https://datacite-metadata-schema.readthedocs.io/


Generated from: data_catalog/contributor_roles.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class DataCiteContributorType(RichEnum):
    """
    Types of contributors to research resources from DataCite 4.6.
    These describe organizational and functional roles rather than
    specific contribution activities (see CRediT/ResearchRole for those).
    
    """
    # Enum members
    CONTACT_PERSON = "CONTACT_PERSON"
    DATA_COLLECTOR = "DATA_COLLECTOR"
    DATA_CURATOR = "DATA_CURATOR"
    DATA_MANAGER = "DATA_MANAGER"
    DISTRIBUTOR = "DISTRIBUTOR"
    EDITOR = "EDITOR"
    HOSTING_INSTITUTION = "HOSTING_INSTITUTION"
    PRODUCER = "PRODUCER"
    PROJECT_LEADER = "PROJECT_LEADER"
    PROJECT_MANAGER = "PROJECT_MANAGER"
    PROJECT_MEMBER = "PROJECT_MEMBER"
    REGISTRATION_AGENCY = "REGISTRATION_AGENCY"
    REGISTRATION_AUTHORITY = "REGISTRATION_AUTHORITY"
    RELATED_PERSON = "RELATED_PERSON"
    RESEARCHER = "RESEARCHER"
    RESEARCH_GROUP = "RESEARCH_GROUP"
    RIGHTS_HOLDER = "RIGHTS_HOLDER"
    SPONSOR = "SPONSOR"
    SUPERVISOR = "SUPERVISOR"
    TRANSLATOR = "TRANSLATOR"
    WORK_PACKAGE_LEADER = "WORK_PACKAGE_LEADER"
    OTHER = "OTHER"

# Set metadata after class creation
DataCiteContributorType._metadata = {
    "CONTACT_PERSON": {'description': 'Person with knowledge of how to access, troubleshoot, or\notherwise field issues related to the resource.\n', 'meaning': 'DataCite:ContactPerson', 'annotations': {'category': 'support'}},
    "DATA_COLLECTOR": {'description': 'Person or institution responsible for finding, gathering, or\ncollecting data under the guidelines of the author(s) or\nPrincipal Investigator (PI).\n', 'meaning': 'DataCite:DataCollector', 'annotations': {'category': 'data_work'}},
    "DATA_CURATOR": {'description': 'Person tasked with reviewing, enhancing, cleaning, or standardizing\nmetadata and the associated data submitted for storage, use, and\nmaintenance within a repository.\n', 'meaning': 'DataCite:DataCurator', 'annotations': {'category': 'data_work'}},
    "DATA_MANAGER": {'description': 'Person or organization responsible for maintaining the finished\nresource, including data quality, access permissions, and\nlong-term availability.\n', 'meaning': 'DataCite:DataManager', 'annotations': {'category': 'data_work'}},
    "DISTRIBUTOR": {'description': 'Institution tasked with responsibility to generate or disseminate\ncopies of the resource in either electronic or print form.\n', 'meaning': 'DataCite:Distributor', 'annotations': {'category': 'dissemination'}},
    "EDITOR": {'description': 'A person who oversees the details related to the publication\nformat of the resource.\n', 'meaning': 'DataCite:Editor', 'annotations': {'category': 'editorial'}},
    "HOSTING_INSTITUTION": {'description': 'Typically, the organization allowing the resource to be available\non the internet through the provision of its hardware, software,\nor operating support.\n', 'meaning': 'DataCite:HostingInstitution', 'annotations': {'category': 'infrastructure'}},
    "PRODUCER": {'description': 'Person or organization responsible for the artistic and technical\naspects of a resource, typically in audiovisual or media contexts.\n', 'meaning': 'DataCite:Producer', 'annotations': {'category': 'production'}},
    "PROJECT_LEADER": {'description': 'Person officially designated as head of a project team or\nsub-project team instrumental in the work necessary to the\ndevelopment of the resource.\n', 'meaning': 'DataCite:ProjectLeader', 'annotations': {'category': 'leadership'}, 'aliases': ['Principal Investigator', 'PI']},
    "PROJECT_MANAGER": {'description': 'Person officially designated as manager of a project, responsible\nfor day-to-day management activities.\n', 'meaning': 'DataCite:ProjectManager', 'annotations': {'category': 'leadership'}},
    "PROJECT_MEMBER": {'description': 'Person on the membership list of a designated project or\nproject team.\n', 'meaning': 'DataCite:ProjectMember', 'annotations': {'category': 'team'}},
    "REGISTRATION_AGENCY": {'description': 'Institution or organization officially appointed by a Registration\nAuthority to handle specific tasks within a defined area of\nresponsibility.\n', 'meaning': 'DataCite:RegistrationAgency', 'annotations': {'category': 'governance', 'examples': 'DataCite member organizations'}},
    "REGISTRATION_AUTHORITY": {'description': 'A standards-setting body from which Registration Agencies obtain\ntheir official recognition and guidance.\n', 'meaning': 'DataCite:RegistrationAuthority', 'annotations': {'category': 'governance', 'examples': 'International DOI Foundation'}},
    "RELATED_PERSON": {'description': 'A person without a specifically defined role in the development\nof the resource, but who is someone the author wishes to recognize.\n', 'meaning': 'DataCite:RelatedPerson', 'annotations': {'category': 'acknowledgment'}},
    "RESEARCHER": {'description': 'A person involved in analyzing data or the results of an\nexperiment or formal study.\n', 'meaning': 'DataCite:Researcher', 'annotations': {'category': 'research'}},
    "RESEARCH_GROUP": {'description': 'A group of individuals with a common research focus, typically\nwithin a lab, department, or division.\n', 'meaning': 'DataCite:ResearchGroup', 'annotations': {'category': 'team'}},
    "RIGHTS_HOLDER": {'description': 'Person or institution owning or managing property rights,\nincluding intellectual property rights, over the resource.\n', 'meaning': 'DataCite:RightsHolder', 'annotations': {'category': 'legal'}},
    "SPONSOR": {'description': 'Person or organization that issued a contract or under the\nauspices of which a work has been written, printed, published,\ndeveloped, etc.\n', 'meaning': 'DataCite:Sponsor', 'annotations': {'category': 'funding'}},
    "SUPERVISOR": {'description': 'Designated administrator overseeing one or more groups or teams\nworking to produce the resource.\n', 'meaning': 'DataCite:Supervisor', 'annotations': {'category': 'leadership'}},
    "TRANSLATOR": {'description': 'Person, organization, or automated system responsible for\nrendering the content of a resource from one language into\nanother.\n', 'meaning': 'DataCite:Translator', 'annotations': {'category': 'translation', 'added_version': '4.6'}},
    "WORK_PACKAGE_LEADER": {'description': 'A Work Package is a recognized data product, and the Work Package\nLeader ensures the comprehensive contents, availability, and\nquality of the work package.\n', 'meaning': 'DataCite:WorkPackageLeader', 'annotations': {'category': 'leadership'}},
    "OTHER": {'description': 'Any person or institution making a significant contribution not\ncovered by other contributor type values.\n', 'meaning': 'DataCite:Other', 'annotations': {'note': 'Should be accompanied by free-text description'}},
}

__all__ = [
    "DataCiteContributorType",
]