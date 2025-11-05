"""
Phenopackets Clinical Value Sets

Value sets derived from GA4GH Phenopackets Schema for clinical genomics and phenotyping

Generated from: clinical/phenopackets.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class KaryotypicSexEnum(RichEnum):
    """
    Karyotypic sex of an individual based on chromosome composition
    """
    # Enum members
    XX = "XX"
    XY = "XY"
    XO = "XO"
    XXY = "XXY"
    XXX = "XXX"
    XXXY = "XXXY"
    XXXX = "XXXX"
    XXYY = "XXYY"
    XYY = "XYY"
    OTHER_KARYOTYPE = "OTHER_KARYOTYPE"
    UNKNOWN_KARYOTYPE = "UNKNOWN_KARYOTYPE"

# Set metadata after class creation
KaryotypicSexEnum._metadata = {
    "XX": {'description': 'Female karyotype (46,XX)', 'meaning': 'NCIT:C45976', 'annotations': {'chromosome_count': 46, 'typical_phenotypic_sex': 'female'}},
    "XY": {'description': 'Male karyotype (46,XY)', 'meaning': 'NCIT:C45977', 'annotations': {'chromosome_count': 46, 'typical_phenotypic_sex': 'male'}},
    "XO": {'description': 'Turner syndrome karyotype (45,X)', 'meaning': 'NCIT:C176780', 'annotations': {'chromosome_count': 45, 'condition': 'Turner syndrome'}},
    "XXY": {'description': 'Klinefelter syndrome karyotype (47,XXY)', 'meaning': 'NCIT:C176784', 'annotations': {'chromosome_count': 47, 'condition': 'Klinefelter syndrome'}},
    "XXX": {'description': 'Triple X syndrome karyotype (47,XXX)', 'meaning': 'NCIT:C176785', 'annotations': {'chromosome_count': 47, 'condition': 'Triple X syndrome'}},
    "XXXY": {'description': 'XXXY syndrome karyotype (48,XXXY)', 'meaning': 'NCIT:C176786', 'annotations': {'chromosome_count': 48, 'condition': 'XXXY syndrome'}},
    "XXXX": {'description': 'Tetrasomy X karyotype (48,XXXX)', 'meaning': 'NCIT:C176787', 'annotations': {'chromosome_count': 48, 'condition': 'Tetrasomy X'}},
    "XXYY": {'description': 'XXYY syndrome karyotype (48,XXYY)', 'meaning': 'NCIT:C89801', 'annotations': {'chromosome_count': 48, 'condition': 'XXYY syndrome'}},
    "XYY": {'description': "Jacob's syndrome karyotype (47,XYY)", 'meaning': 'NCIT:C176782', 'annotations': {'chromosome_count': 47, 'condition': "Jacob's syndrome"}},
    "OTHER_KARYOTYPE": {'description': 'Other karyotypic sex not listed', 'annotations': {'note': 'May include complex chromosomal arrangements'}},
    "UNKNOWN_KARYOTYPE": {'description': 'Karyotype not determined or unknown', 'meaning': 'NCIT:C17998'},
}

class PhenotypicSexEnum(RichEnum):
    """
    Phenotypic sex of an individual based on observable characteristics.
    FHIR mapping: AdministrativeGender
    """
    # Enum members
    MALE = "MALE"
    FEMALE = "FEMALE"
    OTHER_SEX = "OTHER_SEX"
    UNKNOWN_SEX = "UNKNOWN_SEX"

# Set metadata after class creation
PhenotypicSexEnum._metadata = {
    "MALE": {'description': 'Male phenotypic sex', 'meaning': 'PATO:0000384'},
    "FEMALE": {'description': 'Female phenotypic sex', 'meaning': 'PATO:0000383'},
    "OTHER_SEX": {'description': 'Sex characteristics not clearly male or female', 'meaning': 'NCIT:C45908', 'annotations': {'note': 'Includes differences of sex development (DSD)'}},
    "UNKNOWN_SEX": {'description': 'Sex not assessed or not available', 'meaning': 'NCIT:C17998'},
}

class AllelicStateEnum(RichEnum):
    """
    Allelic state/zygosity of a variant or genetic feature
    """
    # Enum members
    HETEROZYGOUS = "HETEROZYGOUS"
    HOMOZYGOUS = "HOMOZYGOUS"
    HEMIZYGOUS = "HEMIZYGOUS"
    COMPOUND_HETEROZYGOUS = "COMPOUND_HETEROZYGOUS"
    HOMOZYGOUS_REFERENCE = "HOMOZYGOUS_REFERENCE"
    HOMOZYGOUS_ALTERNATE = "HOMOZYGOUS_ALTERNATE"

# Set metadata after class creation
AllelicStateEnum._metadata = {
    "HETEROZYGOUS": {'description': 'Different alleles at a locus', 'meaning': 'GENO:0000135', 'annotations': {'symbol': 'het'}},
    "HOMOZYGOUS": {'description': 'Identical alleles at a locus', 'meaning': 'GENO:0000136', 'annotations': {'symbol': 'hom'}},
    "HEMIZYGOUS": {'description': 'Only one allele present (e.g., X-linked in males)', 'meaning': 'GENO:0000134', 'annotations': {'symbol': 'hemi', 'note': 'Common for X-linked genes in males'}},
    "COMPOUND_HETEROZYGOUS": {'description': 'Two different heterozygous variants in same gene', 'meaning': 'GENO:0000402', 'annotations': {'symbol': 'comp het'}},
    "HOMOZYGOUS_REFERENCE": {'description': 'Two reference/wild-type alleles', 'meaning': 'GENO:0000036', 'annotations': {'symbol': 'hom ref'}},
    "HOMOZYGOUS_ALTERNATE": {'description': 'Two alternate/variant alleles', 'meaning': 'GENO:0000002', 'annotations': {'symbol': 'hom alt'}},
}

class LateralityEnum(RichEnum):
    """
    Laterality/sidedness of a finding or anatomical structure
    """
    # Enum members
    RIGHT = "RIGHT"
    LEFT = "LEFT"
    BILATERAL = "BILATERAL"
    UNILATERAL = "UNILATERAL"
    MIDLINE = "MIDLINE"

# Set metadata after class creation
LateralityEnum._metadata = {
    "RIGHT": {'description': 'Right side', 'meaning': 'HP:0012834', 'annotations': {'anatomical_term': 'dexter'}},
    "LEFT": {'description': 'Left side', 'meaning': 'HP:0012835', 'annotations': {'anatomical_term': 'sinister'}},
    "BILATERAL": {'description': 'Both sides', 'meaning': 'HP:0012832', 'annotations': {'note': 'Affecting both left and right'}},
    "UNILATERAL": {'description': 'One side (unspecified which)', 'meaning': 'HP:0012833', 'annotations': {'note': 'Affecting only one side'}},
    "MIDLINE": {'description': 'In the midline/center', 'annotations': {'note': "Along the body's central axis"}},
}

class OnsetTimingEnum(RichEnum):
    """
    Timing of disease or phenotype onset relative to developmental stages
    """
    # Enum members
    ANTENATAL_ONSET = "ANTENATAL_ONSET"
    EMBRYONAL_ONSET = "EMBRYONAL_ONSET"
    FETAL_ONSET = "FETAL_ONSET"
    CONGENITAL_ONSET = "CONGENITAL_ONSET"
    NEONATAL_ONSET = "NEONATAL_ONSET"
    INFANTILE_ONSET = "INFANTILE_ONSET"
    CHILDHOOD_ONSET = "CHILDHOOD_ONSET"
    JUVENILE_ONSET = "JUVENILE_ONSET"
    YOUNG_ADULT_ONSET = "YOUNG_ADULT_ONSET"
    MIDDLE_AGE_ONSET = "MIDDLE_AGE_ONSET"
    LATE_ONSET = "LATE_ONSET"

# Set metadata after class creation
OnsetTimingEnum._metadata = {
    "ANTENATAL_ONSET": {'description': 'Before birth (prenatal)', 'meaning': 'HP:0030674', 'annotations': {'period': 'Before birth'}},
    "EMBRYONAL_ONSET": {'description': 'During embryonic period (0-8 weeks)', 'meaning': 'HP:0011460', 'annotations': {'period': '0-8 weeks gestation'}},
    "FETAL_ONSET": {'description': 'During fetal period (8 weeks to birth)', 'meaning': 'HP:0011461', 'annotations': {'period': '8 weeks to birth'}},
    "CONGENITAL_ONSET": {'description': 'Present at birth', 'meaning': 'HP:0003577', 'annotations': {'period': 'At birth'}},
    "NEONATAL_ONSET": {'description': 'Within first 28 days of life', 'meaning': 'HP:0003623', 'annotations': {'period': '0-28 days'}},
    "INFANTILE_ONSET": {'description': 'Between 28 days and 1 year', 'meaning': 'HP:0003593', 'annotations': {'period': '28 days to 1 year'}},
    "CHILDHOOD_ONSET": {'description': 'Between 1 year and 16 years', 'meaning': 'HP:0011463', 'annotations': {'period': '1-16 years'}},
    "JUVENILE_ONSET": {'description': 'Between 5 years and 16 years', 'meaning': 'HP:0003621', 'annotations': {'period': '5-16 years'}},
    "YOUNG_ADULT_ONSET": {'description': 'Between 16 years and 40 years', 'meaning': 'HP:0011462', 'annotations': {'period': '16-40 years'}},
    "MIDDLE_AGE_ONSET": {'description': 'Between 40 years and 60 years', 'meaning': 'HP:0003596', 'annotations': {'period': '40-60 years'}},
    "LATE_ONSET": {'description': 'After 60 years', 'meaning': 'HP:0003584', 'annotations': {'period': '>60 years'}},
}

class ACMGPathogenicityEnum(RichEnum):
    """
    ACMG/AMP variant pathogenicity classification for clinical genetics
    """
    # Enum members
    PATHOGENIC = "PATHOGENIC"
    LIKELY_PATHOGENIC = "LIKELY_PATHOGENIC"
    UNCERTAIN_SIGNIFICANCE = "UNCERTAIN_SIGNIFICANCE"
    LIKELY_BENIGN = "LIKELY_BENIGN"
    BENIGN = "BENIGN"

# Set metadata after class creation
ACMGPathogenicityEnum._metadata = {
    "PATHOGENIC": {'description': 'Pathogenic variant', 'meaning': 'NCIT:C168799', 'annotations': {'abbreviation': 'P', 'clinical_significance': 'Disease-causing'}},
    "LIKELY_PATHOGENIC": {'description': 'Likely pathogenic variant', 'meaning': 'NCIT:C168800', 'annotations': {'abbreviation': 'LP', 'probability': '>90% certain'}},
    "UNCERTAIN_SIGNIFICANCE": {'description': 'Variant of uncertain significance', 'meaning': 'NCIT:C94187', 'annotations': {'abbreviation': 'VUS', 'note': 'Insufficient evidence'}},
    "LIKELY_BENIGN": {'description': 'Likely benign variant', 'meaning': 'NCIT:C168801', 'annotations': {'abbreviation': 'LB', 'probability': '>90% certain benign'}},
    "BENIGN": {'description': 'Benign variant', 'meaning': 'NCIT:C168802', 'annotations': {'abbreviation': 'B', 'clinical_significance': 'Not disease-causing'}},
}

class TherapeuticActionabilityEnum(RichEnum):
    """
    Clinical actionability of a genetic finding for treatment decisions
    """
    # Enum members
    ACTIONABLE = "ACTIONABLE"
    NOT_ACTIONABLE = "NOT_ACTIONABLE"
    UNKNOWN_ACTIONABILITY = "UNKNOWN_ACTIONABILITY"

# Set metadata after class creation
TherapeuticActionabilityEnum._metadata = {
    "ACTIONABLE": {'description': 'Finding has direct therapeutic implications', 'meaning': 'NCIT:C206303', 'annotations': {'note': 'Can guide treatment selection'}},
    "NOT_ACTIONABLE": {'description': 'No current therapeutic implications', 'meaning': 'NCIT:C206304', 'annotations': {'note': 'No treatment changes indicated'}},
    "UNKNOWN_ACTIONABILITY": {'description': 'Therapeutic implications unclear', 'meaning': 'NCIT:C17998'},
}

class InterpretationProgressEnum(RichEnum):
    """
    Progress status of clinical interpretation or diagnosis
    """
    # Enum members
    SOLVED = "SOLVED"
    UNSOLVED = "UNSOLVED"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    UNKNOWN_PROGRESS = "UNKNOWN_PROGRESS"

# Set metadata after class creation
InterpretationProgressEnum._metadata = {
    "SOLVED": {'description': 'Diagnosis achieved/case solved', 'meaning': 'NCIT:C20826', 'annotations': {'note': 'Molecular cause identified'}},
    "UNSOLVED": {'description': 'No diagnosis achieved', 'meaning': 'NCIT:C125009', 'annotations': {'note': 'Molecular cause not identified'}},
    "IN_PROGRESS": {'description': 'Analysis ongoing', 'meaning': 'NCIT:C25630'},
    "COMPLETED": {'description': 'Analysis completed', 'meaning': 'NCIT:C216251', 'annotations': {'note': 'May be solved or unsolved'}},
    "UNKNOWN_PROGRESS": {'description': 'Progress status unknown', 'meaning': 'NCIT:C17998'},
}

class RegimenStatusEnum(RichEnum):
    """
    Status of a therapeutic regimen or treatment protocol
    """
    # Enum members
    NOT_STARTED = "NOT_STARTED"
    STARTED = "STARTED"
    COMPLETED = "COMPLETED"
    DISCONTINUED_ADVERSE_EVENT = "DISCONTINUED_ADVERSE_EVENT"
    DISCONTINUED_LACK_OF_EFFICACY = "DISCONTINUED_LACK_OF_EFFICACY"
    DISCONTINUED_PHYSICIAN_DECISION = "DISCONTINUED_PHYSICIAN_DECISION"
    DISCONTINUED_PATIENT_DECISION = "DISCONTINUED_PATIENT_DECISION"
    UNKNOWN_STATUS = "UNKNOWN_STATUS"

# Set metadata after class creation
RegimenStatusEnum._metadata = {
    "NOT_STARTED": {'description': 'Treatment not yet begun', 'meaning': 'NCIT:C53601'},
    "STARTED": {'description': 'Treatment initiated', 'meaning': 'NCIT:C165209'},
    "COMPLETED": {'description': 'Treatment finished as planned', 'meaning': 'NCIT:C105740'},
    "DISCONTINUED_ADVERSE_EVENT": {'description': 'Stopped due to adverse event', 'meaning': 'NCIT:C41331', 'annotations': {'reason': 'Toxicity or side effects'}},
    "DISCONTINUED_LACK_OF_EFFICACY": {'description': 'Stopped due to lack of efficacy', 'meaning': 'NCIT:C49502', 'annotations': {'reason': 'Treatment not effective'}},
    "DISCONTINUED_PHYSICIAN_DECISION": {'description': 'Stopped by physician decision', 'meaning': 'NCIT:C49502'},
    "DISCONTINUED_PATIENT_DECISION": {'description': 'Stopped by patient choice', 'meaning': 'NCIT:C48271'},
    "UNKNOWN_STATUS": {'description': 'Treatment status unknown', 'meaning': 'NCIT:C17998'},
}

class DrugResponseEnum(RichEnum):
    """
    Response categories for drug treatment outcomes
    """
    # Enum members
    FAVORABLE = "FAVORABLE"
    UNFAVORABLE = "UNFAVORABLE"
    RESPONSIVE = "RESPONSIVE"
    RESISTANT = "RESISTANT"
    PARTIALLY_RESPONSIVE = "PARTIALLY_RESPONSIVE"
    UNKNOWN_RESPONSE = "UNKNOWN_RESPONSE"

# Set metadata after class creation
DrugResponseEnum._metadata = {
    "FAVORABLE": {'description': 'Favorable response to treatment', 'meaning': 'NCIT:C123584', 'annotations': {'note': 'Better than expected response'}},
    "UNFAVORABLE": {'description': 'Unfavorable response to treatment', 'meaning': 'NCIT:C102561', 'annotations': {'note': 'Worse than expected response'}},
    "RESPONSIVE": {'description': 'Responsive to treatment', 'meaning': 'NCIT:C165206', 'annotations': {'note': 'Shows expected response'}},
    "RESISTANT": {'description': 'Resistant to treatment', 'meaning': 'NCIT:C16523', 'annotations': {'note': 'No response to treatment'}},
    "PARTIALLY_RESPONSIVE": {'description': 'Partial response to treatment', 'meaning': 'NCIT:C18213', 'annotations': {'note': 'Some but not complete response'}},
    "UNKNOWN_RESPONSE": {'description': 'Treatment response unknown', 'meaning': 'NCIT:C17998'},
}

__all__ = [
    "KaryotypicSexEnum",
    "PhenotypicSexEnum",
    "AllelicStateEnum",
    "LateralityEnum",
    "OnsetTimingEnum",
    "ACMGPathogenicityEnum",
    "TherapeuticActionabilityEnum",
    "InterpretationProgressEnum",
    "RegimenStatusEnum",
    "DrugResponseEnum",
]