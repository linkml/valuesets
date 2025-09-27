"""
Mouse Developmental Stages Value Sets

Value sets for mouse developmental stages from fertilization through aging

Generated from: bio/mouse_developmental_stages.yaml
"""

from __future__ import annotations

from typing import Dict, Any, Optional
from valuesets.generators.rich_enum import RichEnum

class MouseDevelopmentalStage(RichEnum):
    """
    Mouse developmental stages from fertilization through aging, based on the MmusDv (Mouse Developmental Stages) ontology and Theiler staging system.
    """
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
    "ZYGOTE_STAGE": {'description': 'Single cell after fertilization (Theiler stage 01, E0.5)', 'meaning': 'MmusDv:0000003'},
    "TWO_CELL_STAGE": {'description': 'Two-cell embryo (Theiler stage 02, E1.5)', 'meaning': 'MmusDv:0000005'},
    "FOUR_CELL_STAGE": {'description': 'Four-cell embryo (Theiler stage 02, E2)', 'meaning': 'MmusDv:0000005'},
    "EIGHT_CELL_STAGE": {'description': 'Eight-cell embryo (Theiler stage 03, E2.5)', 'meaning': 'MmusDv:0000006'},
    "MORULA_STAGE": {'description': 'Compact morula (Theiler stage 03, E2.5-3)', 'meaning': 'MmusDv:0000006'},
    "BLASTOCYST_STAGE": {'description': 'Blastocyst with inner cell mass (Theiler stage 05, E3.5-4.5)', 'meaning': 'MmusDv:0000009'},
    "GASTRULA_STAGE": {'description': 'Formation of three germ layers (E6.5-7.5)', 'meaning': 'MmusDv:0000013'},
    "NEURULA_STAGE": {'description': 'Neural tube formation (Theiler stage 11, E8)', 'meaning': 'MmusDv:0000017'},
    "ORGANOGENESIS_STAGE": {'description': 'Major organ development (E8.5-14.5)', 'meaning': 'MmusDv:0000018'},
    "E0_5": {'description': 'Embryonic day 0.5 - fertilization', 'meaning': 'MmusDv:0000003'},
    "E9_5": {'description': 'Embryonic day 9.5 - early organogenesis', 'meaning': 'MmusDv:0000023'},
    "E14_5": {'description': 'Embryonic day 14.5 - late organogenesis', 'meaning': 'MmusDv:0000029'},
    "P0_NEWBORN": {'description': 'Birth/postnatal day 0', 'meaning': 'MmusDv:0000036'},
    "P21_WEANING": {'description': 'Postnatal day 21 - weaning age', 'meaning': 'MmusDv:0000141'},
    "P42_JUVENILE": {'description': 'Postnatal day 42 - juvenile/sexually mature', 'meaning': 'MmusDv:0000151'},
    "P56_ADULT": {'description': 'Postnatal day 56 - young adult', 'meaning': 'MmusDv:0000154'},
    "AGED_12_MONTHS": {'description': '12+ months - aged mouse', 'meaning': 'MmusDv:0000135'},
    "THEILER_STAGE": {'description': 'Reference to Theiler staging system for mouse development'},
}

__all__ = [
    "MouseDevelopmentalStage",
]