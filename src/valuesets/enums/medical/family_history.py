"""
Medical Family History Value Sets

Family history and pedigree value sets based on HL7 FHIR, SNOMED CT, and KIN ontology standards

Generated from: medical/family_history.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class FamilyRelationship(RichEnum):
    """
    Family relationships used in pedigree and family history documentation
    """
    # Enum members
    PARENT = "PARENT"
    MOTHER = "MOTHER"
    FATHER = "FATHER"
    NATURAL_MOTHER = "NATURAL_MOTHER"
    NATURAL_FATHER = "NATURAL_FATHER"
    ADOPTIVE_PARENT = "ADOPTIVE_PARENT"
    ADOPTIVE_MOTHER = "ADOPTIVE_MOTHER"
    ADOPTIVE_FATHER = "ADOPTIVE_FATHER"
    STEP_PARENT = "STEP_PARENT"
    STEP_MOTHER = "STEP_MOTHER"
    STEP_FATHER = "STEP_FATHER"
    FOSTER_PARENT = "FOSTER_PARENT"
    GESTATIONAL_MOTHER = "GESTATIONAL_MOTHER"
    SIBLING = "SIBLING"
    BROTHER = "BROTHER"
    SISTER = "SISTER"
    NATURAL_BROTHER = "NATURAL_BROTHER"
    NATURAL_SISTER = "NATURAL_SISTER"
    HALF_BROTHER = "HALF_BROTHER"
    HALF_SISTER = "HALF_SISTER"
    STEP_BROTHER = "STEP_BROTHER"
    STEP_SISTER = "STEP_SISTER"
    TWIN = "TWIN"
    TWIN_BROTHER = "TWIN_BROTHER"
    TWIN_SISTER = "TWIN_SISTER"
    FRATERNAL_TWIN = "FRATERNAL_TWIN"
    IDENTICAL_TWIN = "IDENTICAL_TWIN"
    CHILD = "CHILD"
    SON = "SON"
    DAUGHTER = "DAUGHTER"
    NATURAL_CHILD = "NATURAL_CHILD"
    ADOPTIVE_CHILD = "ADOPTIVE_CHILD"
    FOSTER_CHILD = "FOSTER_CHILD"
    STEP_CHILD = "STEP_CHILD"
    GRANDPARENT = "GRANDPARENT"
    GRANDMOTHER = "GRANDMOTHER"
    GRANDFATHER = "GRANDFATHER"
    MATERNAL_GRANDMOTHER = "MATERNAL_GRANDMOTHER"
    MATERNAL_GRANDFATHER = "MATERNAL_GRANDFATHER"
    PATERNAL_GRANDMOTHER = "PATERNAL_GRANDMOTHER"
    PATERNAL_GRANDFATHER = "PATERNAL_GRANDFATHER"
    GRANDCHILD = "GRANDCHILD"
    GRANDSON = "GRANDSON"
    GRANDDAUGHTER = "GRANDDAUGHTER"
    AUNT = "AUNT"
    UNCLE = "UNCLE"
    MATERNAL_AUNT = "MATERNAL_AUNT"
    MATERNAL_UNCLE = "MATERNAL_UNCLE"
    PATERNAL_AUNT = "PATERNAL_AUNT"
    PATERNAL_UNCLE = "PATERNAL_UNCLE"
    COUSIN = "COUSIN"
    MATERNAL_COUSIN = "MATERNAL_COUSIN"
    PATERNAL_COUSIN = "PATERNAL_COUSIN"
    NIECE = "NIECE"
    NEPHEW = "NEPHEW"
    SPOUSE = "SPOUSE"
    HUSBAND = "HUSBAND"
    WIFE = "WIFE"
    DOMESTIC_PARTNER = "DOMESTIC_PARTNER"
    GREAT_GRANDPARENT = "GREAT_GRANDPARENT"
    GREAT_GRANDMOTHER = "GREAT_GRANDMOTHER"
    GREAT_GRANDFATHER = "GREAT_GRANDFATHER"
    MOTHER_IN_LAW = "MOTHER_IN_LAW"
    FATHER_IN_LAW = "FATHER_IN_LAW"
    DAUGHTER_IN_LAW = "DAUGHTER_IN_LAW"
    SON_IN_LAW = "SON_IN_LAW"
    BROTHER_IN_LAW = "BROTHER_IN_LAW"
    SISTER_IN_LAW = "SISTER_IN_LAW"
    FAMILY_MEMBER = "FAMILY_MEMBER"
    EXTENDED_FAMILY_MEMBER = "EXTENDED_FAMILY_MEMBER"
    SIGNIFICANT_OTHER = "SIGNIFICANT_OTHER"

# Set metadata after class creation
FamilyRelationship._metadata = {
    "PARENT": {'description': 'The player of the role is one who begets, gives birth to, or nurtures and raises the scoping entity (child)', 'meaning': 'HL7:v3-RoleCode#PRN'},
    "MOTHER": {'description': 'The player of the role is a female who conceives, gives birth to, or raises and nurtures the scoping entity (child)', 'meaning': 'HL7:v3-RoleCode#MTH'},
    "FATHER": {'description': 'The player of the role is a male who begets or raises or nurtures the scoping entity (child)', 'meaning': 'HL7:v3-RoleCode#FTH'},
    "NATURAL_MOTHER": {'description': 'The player of the role is a female who conceives or gives birth to the scoping entity (child)', 'meaning': 'HL7:v3-RoleCode#NMTH'},
    "NATURAL_FATHER": {'description': 'The player of the role is a male who begets the scoping entity (child)', 'meaning': 'HL7:v3-RoleCode#NFTH'},
    "ADOPTIVE_PARENT": {'description': 'The player of the role (parent) has taken the scoper (child) into their family through legal means and raises them as his or her own child', 'meaning': 'HL7:v3-RoleCode#ADOPTP'},
    "ADOPTIVE_MOTHER": {'description': 'The player of the role (mother) is a female who has taken the scoper (child) into their family through legal means and raises them as her own child', 'meaning': 'HL7:v3-RoleCode#ADOPTM'},
    "ADOPTIVE_FATHER": {'description': 'The player of the role (father) is a male who has taken the scoper (child) into their family through legal means and raises them as his own child', 'meaning': 'HL7:v3-RoleCode#ADOPTF'},
    "STEP_PARENT": {'description': "The player of the role is the spouse of the scoping person's parent and not the scoping person's natural parent", 'meaning': 'HL7:v3-RoleCode#STPPRN'},
    "STEP_MOTHER": {'description': "The player of the role is the female spouse of the scoping person's parent and not the scoping person's natural mother", 'meaning': 'HL7:v3-RoleCode#STPMTH'},
    "STEP_FATHER": {'description': "The player of the role is the male spouse of the scoping person's parent and not the scoping person's natural father", 'meaning': 'HL7:v3-RoleCode#STPFTH'},
    "FOSTER_PARENT": {'description': 'The player of the role (parent) who is a state-certified caregiver responsible for the scoper (child)', 'meaning': 'HL7:v3-RoleCode#PRNFOST'},
    "GESTATIONAL_MOTHER": {'description': 'The player is a female whose womb carries the fetus of the scoper', 'meaning': 'HL7:v3-RoleCode#GESTM'},
    "SIBLING": {'description': 'The player of the role shares one or both parents in common with the scoping entity', 'meaning': 'HL7:v3-RoleCode#SIB'},
    "BROTHER": {'description': 'The player of the role is a male sharing one or both parents with the scoping entity', 'meaning': 'HL7:v3-RoleCode#BRO'},
    "SISTER": {'description': 'The player of the role is a female sharing one or both parents with the scoping entity', 'meaning': 'HL7:v3-RoleCode#SIS'},
    "NATURAL_BROTHER": {'description': 'The player of the role is a male related to the scoping entity by sharing only the same natural parents', 'meaning': 'HL7:v3-RoleCode#NBRO'},
    "NATURAL_SISTER": {'description': 'The player of the role is a female related to the scoping entity by sharing only the same natural parents', 'meaning': 'HL7:v3-RoleCode#NSIS'},
    "HALF_BROTHER": {'description': 'The player of the role is a male related to the scoping entity by sharing only one biological parent', 'meaning': 'HL7:v3-RoleCode#HBRO'},
    "HALF_SISTER": {'description': 'The player of the role is a female related to the scoping entity by sharing only one biological parent', 'meaning': 'HL7:v3-RoleCode#HSIS'},
    "STEP_BROTHER": {'description': "The player of the role is a male child of the scoping person's stepparent", 'meaning': 'HL7:v3-RoleCode#STPBRO'},
    "STEP_SISTER": {'description': "The player of the role is a female child of the scoping person's stepparent", 'meaning': 'HL7:v3-RoleCode#STPSIS'},
    "TWIN": {'description': 'The scoper and player were carried in the same womb and delivered in the same birth', 'meaning': 'HL7:v3-RoleCode#TWIN'},
    "TWIN_BROTHER": {'description': 'The player of the role is a male born from the same pregnancy as the scoping entity', 'meaning': 'HL7:v3-RoleCode#TWINBRO'},
    "TWIN_SISTER": {'description': 'The player of the role is a female born from the same pregnancy as the scoping entity', 'meaning': 'HL7:v3-RoleCode#TWINSIS'},
    "FRATERNAL_TWIN": {'description': 'The player of the role is born from the same pregnancy as the scoping entity but does not share the same genotype', 'meaning': 'HL7:v3-RoleCode#FTWIN'},
    "IDENTICAL_TWIN": {'description': 'The player of the role is born from the same pregnancy as the scoping entity and shares the same genotype', 'meaning': 'HL7:v3-RoleCode#ITWIN'},
    "CHILD": {'description': 'The player of the role is a child of the scoping entity', 'meaning': 'HL7:v3-RoleCode#CHILD'},
    "SON": {'description': 'The player of the role is a male offspring of the scoping entity (parent)', 'meaning': 'HL7:v3-RoleCode#SON'},
    "DAUGHTER": {'description': 'The player of the role is a female offspring of the scoping entity (parent)', 'meaning': 'HL7:v3-RoleCode#DAU'},
    "NATURAL_CHILD": {'description': 'The player of the role is an offspring of the scoping entity as determined by birth', 'meaning': 'HL7:v3-RoleCode#NCHILD'},
    "ADOPTIVE_CHILD": {'description': 'The player of the role is a child taken into a family through legal means and raised by the scoping person (parent) as his or her own child', 'meaning': 'HL7:v3-RoleCode#CHLDADOPT'},
    "FOSTER_CHILD": {'description': 'The player of the role is a child receiving parental care and nurture from the scoping person (parent) but not related to him or her through legal or blood relationship', 'meaning': 'HL7:v3-RoleCode#CHLDFOST'},
    "STEP_CHILD": {'description': "The player of the role is a child of the scoping person's spouse by a previous union", 'meaning': 'HL7:v3-RoleCode#STPCHLD'},
    "GRANDPARENT": {'description': "The player of the role is a parent of the scoping person's mother or father", 'meaning': 'HL7:v3-RoleCode#GRPRN'},
    "GRANDMOTHER": {'description': "The player of the role is the mother of the scoping person's mother or father", 'meaning': 'HL7:v3-RoleCode#GRMTH'},
    "GRANDFATHER": {'description': "The player of the role is the father of the scoping person's mother or father", 'meaning': 'HL7:v3-RoleCode#GRFTH'},
    "MATERNAL_GRANDMOTHER": {'description': "The player of the role is the mother of the scoping person's mother", 'meaning': 'HL7:v3-RoleCode#MGRMTH'},
    "MATERNAL_GRANDFATHER": {'description': "The player of the role is the father of the scoping person's mother", 'meaning': 'HL7:v3-RoleCode#MGRFTH'},
    "PATERNAL_GRANDMOTHER": {'description': "The player of the role is the mother of the scoping person's father", 'meaning': 'HL7:v3-RoleCode#PGRMTH'},
    "PATERNAL_GRANDFATHER": {'description': "The player of the role is the father of the scoping person's father", 'meaning': 'HL7:v3-RoleCode#PGRFTH'},
    "GRANDCHILD": {'description': "The player of the role is a child of the scoping person's son or daughter", 'meaning': 'HL7:v3-RoleCode#GRNDCHILD'},
    "GRANDSON": {'description': "The player of the role is a son of the scoping person's son or daughter", 'meaning': 'HL7:v3-RoleCode#GRNDSN'},
    "GRANDDAUGHTER": {'description': "The player of the role is a daughter of the scoping person's son or daughter", 'meaning': 'HL7:v3-RoleCode#GRNDDAU'},
    "AUNT": {'description': "The player of the role is a sister of the scoping person's mother or father", 'meaning': 'HL7:v3-RoleCode#AUNT'},
    "UNCLE": {'description': "The player of the role is a brother of the scoping person's mother or father", 'meaning': 'HL7:v3-RoleCode#UNCLE'},
    "MATERNAL_AUNT": {'description': "The player of the role is a sister of the scoping person's mother", 'meaning': 'HL7:v3-RoleCode#MAUNT'},
    "MATERNAL_UNCLE": {'description': "The player of the role is a brother of the scoping person's mother", 'meaning': 'HL7:v3-RoleCode#MUNCLE'},
    "PATERNAL_AUNT": {'description': "The player of the role is a sister of the scoping person's father", 'meaning': 'HL7:v3-RoleCode#PAUNT'},
    "PATERNAL_UNCLE": {'description': "The player of the role is a brother of the scoping person's father", 'meaning': 'HL7:v3-RoleCode#PUNCLE'},
    "COUSIN": {'description': 'The player of the role is a relative descended from a common ancestor, such as a grandparent, by two or more steps in a diverging line', 'meaning': 'HL7:v3-RoleCode#COUSN'},
    "MATERNAL_COUSIN": {'description': 'The player of the role is a child of a maternal aunt or uncle of the scoping person', 'meaning': 'HL7:v3-RoleCode#MCOUSN'},
    "PATERNAL_COUSIN": {'description': 'The player of the role is a child of a paternal aunt or uncle of the scoping person', 'meaning': 'HL7:v3-RoleCode#PCOUSN'},
    "NIECE": {'description': "The player of the role is a daughter of the scoping person's brother or sister or of the brother or sister of the scoping person's spouse", 'meaning': 'HL7:v3-RoleCode#NIECE'},
    "NEPHEW": {'description': "The player of the role is a son of the scoping person's brother or sister or of the brother or sister of the scoping person's spouse", 'meaning': 'HL7:v3-RoleCode#NEPHEW'},
    "SPOUSE": {'description': 'The player of the role is a marriage partner of the scoping person', 'meaning': 'HL7:v3-RoleCode#SPS'},
    "HUSBAND": {'description': 'The player of the role is a man joined to a woman (scoping person) in marriage', 'meaning': 'HL7:v3-RoleCode#HUSB'},
    "WIFE": {'description': 'The player of the role is a woman joined to a man (scoping person) in marriage', 'meaning': 'HL7:v3-RoleCode#WIFE'},
    "DOMESTIC_PARTNER": {'description': "The player of the role cohabits with the scoping person but is not the scoping person's spouse", 'meaning': 'HL7:v3-RoleCode#DOMPART'},
    "GREAT_GRANDPARENT": {'description': "The player of the role is a grandparent of the scoping person's mother or father", 'meaning': 'HL7:v3-RoleCode#GGRPRN'},
    "GREAT_GRANDMOTHER": {'description': "The player of the role is a grandmother of the scoping person's mother or father", 'meaning': 'HL7:v3-RoleCode#GGRMTH'},
    "GREAT_GRANDFATHER": {'description': "The player of the role is a grandfather of the scoping person's mother or father", 'meaning': 'HL7:v3-RoleCode#GGRFTH'},
    "MOTHER_IN_LAW": {'description': "The player of the role is the mother of the scoping person's spouse", 'meaning': 'HL7:v3-RoleCode#MTHINLAW'},
    "FATHER_IN_LAW": {'description': "The player of the role is the father of the scoping person's spouse", 'meaning': 'HL7:v3-RoleCode#FTHINLAW'},
    "DAUGHTER_IN_LAW": {'description': "The player of the role is the wife of scoping person's son", 'meaning': 'HL7:v3-RoleCode#DAUINLAW'},
    "SON_IN_LAW": {'description': "The player of the role is the husband of scoping person's daughter", 'meaning': 'HL7:v3-RoleCode#SONINLAW'},
    "BROTHER_IN_LAW": {'description': "The player of the role is a brother of the scoping person's spouse, or the husband of the scoping person's sister, or the husband of a sister of the scoping person's spouse", 'meaning': 'HL7:v3-RoleCode#BROINLAW'},
    "SISTER_IN_LAW": {'description': "The player of the role is a sister of the scoping person's spouse, or the wife of the scoping person's brother, or the wife of a brother of the scoping person's spouse", 'meaning': 'HL7:v3-RoleCode#SISINLAW'},
    "FAMILY_MEMBER": {'description': 'A relationship between two people characterizing their "familial" relationship', 'meaning': 'HL7:v3-RoleCode#FAMMEMB'},
    "EXTENDED_FAMILY_MEMBER": {'description': 'Description of an extended family member', 'meaning': 'HL7:v3-RoleCode#EXT'},
    "SIGNIFICANT_OTHER": {'description': "A person who is important to one's well being; especially a spouse or one in a similar relationship", 'meaning': 'HL7:v3-RoleCode#SIGOTHR'},
}

class FamilyHistoryStatus(RichEnum):
    """
    Status of family history information availability
    """
    # Enum members
    COMPLETED = "COMPLETED"
    PARTIAL = "PARTIAL"
    UNKNOWN = "UNKNOWN"
    UNABLE_TO_OBTAIN = "UNABLE_TO_OBTAIN"
    NOT_ASKED = "NOT_ASKED"

# Set metadata after class creation
FamilyHistoryStatus._metadata = {
    "COMPLETED": {'description': 'All relevant family history information has been obtained', 'meaning': 'HL7:observation-status#final'},
    "PARTIAL": {'description': 'Some family history information is available but not complete', 'meaning': 'HL7:observation-status#preliminary'},
    "UNKNOWN": {'description': 'Family history status is unknown', 'meaning': 'HL7:data-absent-reason#unknown'},
    "UNABLE_TO_OBTAIN": {'description': 'Information could not be obtained due to patient/family constraints', 'meaning': 'HL7:data-absent-reason#patient-refused'},
    "NOT_ASKED": {'description': 'Family history information was not requested', 'meaning': 'HL7:data-absent-reason#not-asked'},
}

class GeneticRelationship(RichEnum):
    """
    Genetic relationship types for pedigree analysis
    """
    # Enum members
    BIOLOGICAL = "BIOLOGICAL"
    FULL_SIBLING = "FULL_SIBLING"
    HALF_SIBLING = "HALF_SIBLING"
    ADOPTIVE = "ADOPTIVE"
    NO_GENETIC_RELATIONSHIP = "NO_GENETIC_RELATIONSHIP"
    UNKNOWN_GENETIC_RELATIONSHIP = "UNKNOWN_GENETIC_RELATIONSHIP"

# Set metadata after class creation
GeneticRelationship._metadata = {
    "BIOLOGICAL": {'description': 'Genetic relationship through biological inheritance', 'meaning': 'SNOMED:444018008'},
    "FULL_SIBLING": {'description': 'Siblings sharing both biological parents', 'meaning': 'SNOMED:444301002'},
    "HALF_SIBLING": {'description': 'Siblings sharing one biological parent', 'meaning': 'SNOMED:445295006'},
    "ADOPTIVE": {'description': 'Relationship established through adoption', 'meaning': 'SNOMED:160499008'},
    "NO_GENETIC_RELATIONSHIP": {'description': 'No genetic relationship exists', 'meaning': 'SNOMED:373068000'},
    "UNKNOWN_GENETIC_RELATIONSHIP": {'description': 'Genetic relationship status is unknown', 'meaning': 'SNOMED:261665006'},
}

__all__ = [
    "FamilyRelationship",
    "FamilyHistoryStatus",
    "GeneticRelationship",
]