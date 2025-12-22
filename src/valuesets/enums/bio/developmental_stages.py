"""
Developmental Stages Value Sets

Ontology-mapped developmental stages for human and mouse organisms. Human stages use HsapDv (Human Developmental Stages) ontology. Mouse stages use MmusDv (Mouse Developmental Stages) ontology.

Generated from: bio/developmental_stages.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class HumanDevelopmentalStage(RichEnum):
    # Enum members
    ZYGOTE_STAGE = "ZYGOTE_STAGE"
    CLEAVAGE_STAGE = "CLEAVAGE_STAGE"
    MORULA_STAGE = "MORULA_STAGE"
    BLASTOCYST_STAGE = "BLASTOCYST_STAGE"
    GASTRULA_STAGE = "GASTRULA_STAGE"
    NEURULA_STAGE = "NEURULA_STAGE"
    ORGANOGENESIS_STAGE = "ORGANOGENESIS_STAGE"
    FETAL_STAGE = "FETAL_STAGE"
    NEONATAL_STAGE = "NEONATAL_STAGE"
    INFANT_STAGE = "INFANT_STAGE"
    TODDLER_STAGE = "TODDLER_STAGE"
    CHILD_STAGE = "CHILD_STAGE"
    ADOLESCENT_STAGE = "ADOLESCENT_STAGE"
    ADULT_STAGE = "ADULT_STAGE"
    AGED_STAGE = "AGED_STAGE"
    EMBRYONIC_STAGE = "EMBRYONIC_STAGE"
    PRENATAL_STAGE = "PRENATAL_STAGE"
    POSTNATAL_STAGE = "POSTNATAL_STAGE"

# Set metadata after class creation
HumanDevelopmentalStage._metadata = {
    "ZYGOTE_STAGE": {'description': 'Embryonic stage defined by a fertilized oocyte and presence of pronuclei. Starts at day 1 post-fertilization.', 'meaning': 'HsapDv:0000003'},
    "CLEAVAGE_STAGE": {'description': 'Embryonic stage during which cell division occurs with reduction in cytoplasmic volume, and formation of inner and outer cell mass. 2-8 cells. Usually starts between day 2-3 post-fertilization.', 'meaning': 'HsapDv:0000005'},
    "MORULA_STAGE": {'description': 'The later part of Carnegie stage 02 when the cells have coalesced into a mass but the blastocystic cavity has not formed.', 'meaning': 'HsapDv:0000205'},
    "BLASTOCYST_STAGE": {'description': 'Blastula stage with the loss of the zona pellucida and the definition of a free blastocyst. Usually starts between day 4-5 post-fertilization.', 'meaning': 'HsapDv:0000007'},
    "GASTRULA_STAGE": {'description': 'Embryonic stage defined by a complex and coordinated series of cellular movements that occurs at the end of cleavage.', 'meaning': 'HsapDv:0000010'},
    "NEURULA_STAGE": {'description': 'Embryonic stage defined by the formation of a tube from the flat layer of ectodermal cells known as the neural plate. This stage starts the emergence of the central nervous system.', 'meaning': 'HsapDv:0000012'},
    "ORGANOGENESIS_STAGE": {'description': 'Embryonic stage at which the ectoderm, endoderm, and mesoderm develop into the internal organs of the organism.', 'meaning': 'HsapDv:0000015'},
    "FETAL_STAGE": {'description': 'Prenatal stage that starts with the fully formed embryo and ends at birth. Generally from 8 weeks post-fertilization until birth.', 'meaning': 'HsapDv:0000037'},
    "NEONATAL_STAGE": {'description': 'Immature stage that refers to a human newborn within the first 28 days of life.', 'meaning': 'HsapDv:0000262'},
    "INFANT_STAGE": {'description': 'Immature stage that refers to an infant who is over 28 days and is under 12 months old.', 'meaning': 'HsapDv:0000261'},
    "TODDLER_STAGE": {'description': 'Human stage that refers to a child who is over 12 months and under 5 years old. Often divided into early toddler (1-2 years) and late toddler (2-3 years).', 'meaning': 'HsapDv:0000265'},
    "CHILD_STAGE": {'description': 'Pediatric stage that refers to a human who is over 5 and under 15 years old. Covers elementary and middle school ages.', 'meaning': 'HsapDv:0000271'},
    "ADOLESCENT_STAGE": {'description': 'A young adult stage that refers to an individual who is over 15 and under 20 years old. Period of transition from childhood to adulthood.', 'meaning': 'HsapDv:0000268'},
    "ADULT_STAGE": {'description': 'Human developmental stage that refers to a sexually mature human. Starts at approximately 15 years according to HPO definitions.', 'meaning': 'HsapDv:0000258'},
    "AGED_STAGE": {'description': 'Late adult stage that refers to an individual who is over 60 and starts to have some age-related impairments. Often subdivided into young-old (60-79) and old-old (80+).', 'meaning': 'HsapDv:0000227'},
    "EMBRYONIC_STAGE": {'description': 'Prenatal stage that starts with fertilization and ends with a fully formed embryo, before undergoing last development during the fetal stage. Up to 8 weeks post-fertilization.', 'meaning': 'HsapDv:0000002'},
    "PRENATAL_STAGE": {'description': 'Prenatal stage that starts with fertilization and ends at birth. Encompasses both embryonic and fetal stages.', 'meaning': 'HsapDv:0000045'},
    "POSTNATAL_STAGE": {'description': 'Human developmental stage that covers the whole of human life post birth.', 'meaning': 'HsapDv:0010000'},
}

class MouseDevelopmentalStage(RichEnum):
    # Enum members
    ZYGOTE_STAGE = "ZYGOTE_STAGE"
    TWO_CELL_STAGE = "TWO_CELL_STAGE"
    FOUR_CELL_STAGE = "FOUR_CELL_STAGE"
    EIGHT_CELL_STAGE = "EIGHT_CELL_STAGE"
    MORULA_STAGE = "MORULA_STAGE"
    BLASTOCYST_STAGE = "BLASTOCYST_STAGE"
    GASTRULA_STAGE = "GASTRULA_STAGE"
    NEURULA_STAGE = "NEURULA_STAGE"
    ORGANOGENESIS_STAGE = "ORGANOGENESIS_STAGE"
    E0_5 = "E0_5"
    E9_5 = "E9_5"
    E14_5 = "E14_5"
    P0_NEWBORN = "P0_NEWBORN"
    P21_WEANING = "P21_WEANING"
    P42_JUVENILE = "P42_JUVENILE"
    P56_ADULT = "P56_ADULT"
    AGED_12_MONTHS = "AGED_12_MONTHS"
    THEILER_STAGE = "THEILER_STAGE"

# Set metadata after class creation
MouseDevelopmentalStage._metadata = {
    "ZYGOTE_STAGE": {'description': 'Embryonic stage defined by a one-cell embryo (fertilised egg) with zona pellucida present. Embryonic age 0-0.9 dpc (days post coitum).', 'meaning': 'MmusDv:0000003'},
    "TWO_CELL_STAGE": {'description': 'Embryonic cleavage stage defined by a dividing 2-4 cells egg. Embryonic age 1 dpc.', 'meaning': 'MmusDv:0000005'},
    "FOUR_CELL_STAGE": {'description': 'Part of Theiler stage 02 - dividing egg with 4 cells. Embryonic age approximately 1 dpc.', 'meaning': 'MmusDv:0000005'},
    "EIGHT_CELL_STAGE": {'description': 'Part of early morula stage - dividing egg with 8 cells. Embryonic age approximately 2 dpc.', 'meaning': 'MmusDv:0000006'},
    "MORULA_STAGE": {'description': 'Embryonic cleavage stage defined by a dividing 4-16 cells egg, early to fully compacted morula. Embryonic age 2 dpc.', 'meaning': 'MmusDv:0000006'},
    "BLASTOCYST_STAGE": {'description': 'Embryonic blastula stage defined by a zona free blastocyst (zona pellucida absent). Embryonic age 4 dpc.', 'meaning': 'MmusDv:0000009'},
    "GASTRULA_STAGE": {'description': 'Embryonic stage defined by complex and coordinated series of cellular movements that occurs at the end of cleavage.', 'meaning': 'MmusDv:0000013'},
    "NEURULA_STAGE": {'description': 'Embryonic stage called presomite stage and defined by the formation of the neural plate. This stage starts the emergence of the central nervous system at embryonic age 7.5 dpc.', 'meaning': 'MmusDv:0000017'},
    "ORGANOGENESIS_STAGE": {'description': 'Embryonic stage at which the ectoderm, endoderm, and mesoderm develop into the internal organs of the organism.', 'meaning': 'MmusDv:0000018'},
    "E0_5": {'description': 'Embryonic day 0.5 - one-cell embryo stage. Corresponds to Theiler stage 01.', 'meaning': 'MmusDv:0000003'},
    "E9_5": {'description': 'Embryonic day 9.5 - organogenesis stage with visible hind limb buds. Between Theiler stages 15 and 16.', 'meaning': 'MmusDv:0000023'},
    "E14_5": {'description': 'Embryonic day 14.5 - late organogenesis with clearly visible fingers and long bones of the limbs present.', 'meaning': 'MmusDv:0000029'},
    "P0_NEWBORN": {'description': 'Stage that refers to the newborn mouse, aged E19-20, P0. Used for postnatal days 0 through 3.', 'meaning': 'MmusDv:0000036'},
    "P21_WEANING": {'description': 'Weaning stage at approximately 21-22 days old. Transition from nursing to independent feeding.', 'meaning': 'MmusDv:0000141'},
    "P42_JUVENILE": {'description': 'Prime adult stage at 6 weeks (42 days) old. Commonly considered the milestone for sexual maturity.', 'meaning': 'MmusDv:0000151'},
    "P56_ADULT": {'description': 'Adult stage at 8 weeks (56 days) old. Fully mature adult mouse.', 'meaning': 'MmusDv:0000154'},
    "AGED_12_MONTHS": {'description': 'Middle aged stage for mice over 10 and under 18 months old. Shows progressive age-related changes.', 'meaning': 'MmusDv:0000135'},
    "THEILER_STAGE": {'description': 'Reference to any Theiler stage (TS1-TS28) which provides standardized morphological staging for mouse development.'},
}

class HumanAgeGroupEnum(RichEnum):
    """
    Simplified human age group categories based on MeSH classifications. Useful for cohort stratification and demographic reporting.
    """
    # Enum members
    INFANT = "INFANT"
    CHILD = "CHILD"
    ADOLESCENT = "ADOLESCENT"
    ADULT = "ADULT"

# Set metadata after class creation
HumanAgeGroupEnum._metadata = {
    "INFANT": {'description': 'A child between 1 and 23 months of age', 'meaning': 'MESH:D007223', 'annotations': {'age_range': '1-23 months'}, 'aliases': ['Infant']},
    "CHILD": {'description': 'A person 2 to 12 years of age', 'meaning': 'MESH:D002648', 'annotations': {'age_range': '2-12 years'}, 'aliases': ['Child']},
    "ADOLESCENT": {'description': 'A person 13 to 18 years of age', 'meaning': 'MESH:D000293', 'annotations': {'age_range': '13-18 years'}, 'aliases': ['Adolescent', 'Teenager']},
    "ADULT": {'description': 'A person having attained full growth or maturity. Adults are of 19 to 120 years of age', 'meaning': 'MESH:D000328', 'annotations': {'age_range': '19-120 years'}, 'aliases': ['Adult']},
}

class MousePostnatalAgeGroupEnum(RichEnum):
    """
    Postnatal mouse age groups using postnatal day (P) notation. Common categories used in laboratory research for developmental studies.
    """
    # Enum members
    P0_P3_NEONATAL = "P0_P3_NEONATAL"
    P4_P21_PREWEANING = "P4_P21_PREWEANING"
    P21_P60_YOUNG_ADULT = "P21_P60_YOUNG_ADULT"
    P60_P180_ADULT = "P60_P180_ADULT"
    P180_P365_MIDDLE_AGED = "P180_P365_MIDDLE_AGED"
    P365_PLUS_AGED = "P365_PLUS_AGED"

# Set metadata after class creation
MousePostnatalAgeGroupEnum._metadata = {
    "P0_P3_NEONATAL": {'description': 'Neonatal stage from birth through postnatal day 3', 'annotations': {'postnatal_days': 'P0-P3', 'approximate_age': 'birth to day 3'}, 'aliases': ['P0-P3 Neonatal']},
    "P4_P21_PREWEANING": {'description': 'Pre-weaning stage from postnatal days 4-21 (typical weaning age)', 'annotations': {'postnatal_days': 'P4-P21', 'approximate_age': 'days 4-21'}, 'aliases': ['P4-P21 Pre-weaning']},
    "P21_P60_YOUNG_ADULT": {'description': 'Young adult stage from postnatal days 21-60 (3 weeks to 2 months)', 'annotations': {'postnatal_days': 'P21-P60', 'approximate_age': '3 weeks to 2 months'}, 'aliases': ['P21-P60 Young Adult']},
    "P60_P180_ADULT": {'description': 'Adult stage from postnatal days 60-180 (2 to 6 months)', 'annotations': {'postnatal_days': 'P60-P180', 'approximate_age': '2 to 6 months'}, 'aliases': ['P60-P180 Adult']},
    "P180_P365_MIDDLE_AGED": {'description': 'Middle-aged stage from postnatal days 180-365 (6 to 12 months)', 'annotations': {'postnatal_days': 'P180-P365', 'approximate_age': '6 to 12 months'}, 'aliases': ['P180-P365 Middle-Aged']},
    "P365_PLUS_AGED": {'description': 'Aged stage from postnatal day 365 onwards (12+ months)', 'annotations': {'postnatal_days': 'P365+', 'approximate_age': '12+ months'}, 'aliases': ['P365+ Aged']},
}

__all__ = [
    "HumanDevelopmentalStage",
    "MouseDevelopmentalStage",
    "HumanAgeGroupEnum",
    "MousePostnatalAgeGroupEnum",
]