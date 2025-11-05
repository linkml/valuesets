"""
Plant Developmental Stages Value Sets

Value sets for plant developmental stages from germination through senescence

Generated from: bio/plant_developmental_stages.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class PlantDevelopmentalStage(RichEnum):
    """
    Major developmental stages in the plant life cycle, from seed germination through senescence. Based on the Plant Ontology (PO) standardized stages.
    """
    # Enum members
    SEED_GERMINATION_STAGE = "SEED_GERMINATION_STAGE"
    SEEDLING_STAGE = "SEEDLING_STAGE"
    VEGETATIVE_GROWTH_STAGE = "VEGETATIVE_GROWTH_STAGE"
    FLOWERING_STAGE = "FLOWERING_STAGE"
    FRUIT_DEVELOPMENT_STAGE = "FRUIT_DEVELOPMENT_STAGE"
    SEED_DEVELOPMENT_STAGE = "SEED_DEVELOPMENT_STAGE"
    SENESCENCE_STAGE = "SENESCENCE_STAGE"
    DORMANCY_STAGE = "DORMANCY_STAGE"
    EMBRYO_DEVELOPMENT_STAGE = "EMBRYO_DEVELOPMENT_STAGE"
    ROOT_DEVELOPMENT_STAGE = "ROOT_DEVELOPMENT_STAGE"
    LEAF_DEVELOPMENT_STAGE = "LEAF_DEVELOPMENT_STAGE"
    REPRODUCTIVE_STAGE = "REPRODUCTIVE_STAGE"
    MATURITY_STAGE = "MATURITY_STAGE"
    POST_HARVEST_STAGE = "POST_HARVEST_STAGE"

# Set metadata after class creation
PlantDevelopmentalStage._metadata = {
    "SEED_GERMINATION_STAGE": {'description': 'Stage beginning with seed imbibition and ending with radicle emergence', 'meaning': 'PO:0007057'},
    "SEEDLING_STAGE": {'description': 'Stage from germination until development of first adult vascular leaf', 'meaning': 'PO:0007131', 'aliases': ['seedling development stage']},
    "VEGETATIVE_GROWTH_STAGE": {'description': 'Stage of growth before reproductive structure formation', 'meaning': 'PO:0007134', 'aliases': ['sporophyte vegetative stage']},
    "FLOWERING_STAGE": {'description': 'Stage when flowers open with pollen release and/or receptive stigma', 'meaning': 'PO:0007616'},
    "FRUIT_DEVELOPMENT_STAGE": {'description': 'Stage of fruit formation through ripening', 'meaning': 'PO:0001002'},
    "SEED_DEVELOPMENT_STAGE": {'description': 'Stage from fertilization to mature seed', 'meaning': 'PO:0001170'},
    "SENESCENCE_STAGE": {'description': 'Stage of aging with loss of function and organ deterioration', 'meaning': 'PO:0007017', 'aliases': ['sporophyte senescent stage']},
    "DORMANCY_STAGE": {'description': 'Stage of suspended physiological activity and growth', 'meaning': 'PO:0007132', 'aliases': ['sporophyte dormant stage']},
    "EMBRYO_DEVELOPMENT_STAGE": {'description': 'Stage from zygote first division to seed germination initiation', 'meaning': 'PO:0007631', 'aliases': ['plant embryo development stage']},
    "ROOT_DEVELOPMENT_STAGE": {'description': 'Stages in root growth and development', 'meaning': 'PO:0007520'},
    "LEAF_DEVELOPMENT_STAGE": {'description': 'Stages in leaf formation and expansion', 'meaning': 'PO:0001050'},
    "REPRODUCTIVE_STAGE": {'description': 'Stage from reproductive structure initiation to senescence onset', 'meaning': 'PO:0007130', 'aliases': ['sporophyte reproductive stage']},
    "MATURITY_STAGE": {'description': 'Stage when plant or plant embryo reaches full development', 'meaning': 'PO:0001081', 'aliases': ['mature plant embryo stage']},
    "POST_HARVEST_STAGE": {'description': 'Stage after harvest when plant parts are detached from parent plant'},
}

__all__ = [
    "PlantDevelopmentalStage",
]