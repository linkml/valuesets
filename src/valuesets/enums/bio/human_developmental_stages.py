"""
Human Developmental Stages Value Sets

Value sets for human developmental stages from fertilization through aging

Generated from: bio/human_developmental_stages.yaml
"""

from __future__ import annotations

from typing import Dict, Any, Optional
from valuesets.generators.rich_enum import RichEnum

class HumanDevelopmentalStage(RichEnum):
    """
    Human developmental stages from fertilization through aging, based on the HsapDv (Human Developmental Stages) ontology.
    """
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
    "ZYGOTE_STAGE": {'description': 'Single cell formed by fertilization (Carnegie stage 01)', 'meaning': 'HsapDv:0000003'},
    "CLEAVAGE_STAGE": {'description': 'Early cell divisions 2-16 cells (Carnegie stage 02)', 'meaning': 'HsapDv:0000005'},
    "MORULA_STAGE": {'description': 'Solid ball of 16-32 cells', 'meaning': 'HsapDv:0000205'},
    "BLASTOCYST_STAGE": {'description': 'Hollow sphere with inner cell mass (Carnegie stage 03)', 'meaning': 'HsapDv:0000007'},
    "GASTRULA_STAGE": {'description': 'Formation of three germ layers', 'meaning': 'HsapDv:0000010'},
    "NEURULA_STAGE": {'description': 'Formation of neural tube', 'meaning': 'HsapDv:0000012'},
    "ORGANOGENESIS_STAGE": {'description': 'Major organ systems develop (weeks 3-8)', 'meaning': 'HsapDv:0000015'},
    "FETAL_STAGE": {'description': 'Growth and maturation of organs (week 9 to birth)', 'meaning': 'HsapDv:0000037'},
    "NEONATAL_STAGE": {'description': 'First 28 days after birth', 'meaning': 'HsapDv:0000262'},
    "INFANT_STAGE": {'description': 'From 1 month to 1 year', 'meaning': 'HsapDv:0000261'},
    "TODDLER_STAGE": {'description': 'Ages 1-4 years', 'meaning': 'HsapDv:0000265'},
    "CHILD_STAGE": {'description': 'Ages 5-14 years', 'meaning': 'HsapDv:0000271'},
    "ADOLESCENT_STAGE": {'description': 'Ages 15-19 years', 'meaning': 'HsapDv:0000268'},
    "ADULT_STAGE": {'description': 'Ages 20-59 years', 'meaning': 'HsapDv:0000258'},
    "AGED_STAGE": {'description': 'Ages 60+ years', 'meaning': 'HsapDv:0000227'},
    "EMBRYONIC_STAGE": {'description': 'From fertilization to end of week 8', 'meaning': 'HsapDv:0000002'},
    "PRENATAL_STAGE": {'description': 'From fertilization to birth', 'meaning': 'HsapDv:0000045'},
    "POSTNATAL_STAGE": {'description': 'After birth', 'meaning': 'HsapDv:0010000'},
}

__all__ = [
    "HumanDevelopmentalStage",
]