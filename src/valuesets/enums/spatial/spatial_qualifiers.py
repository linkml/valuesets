"""
Spatial Qualifier Value Sets

Value sets for spatial qualifiers, directions, and anatomical positions,
including both simple directional terms and biological spatial terminology

Generated from: spatial/spatial_qualifiers.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class SimpleSpatialDirection(RichEnum):
    """
    Basic spatial directional terms for general use
    """
    # Enum members
    LEFT = "LEFT"
    RIGHT = "RIGHT"
    FORWARD = "FORWARD"
    BACKWARD = "BACKWARD"
    UP = "UP"
    DOWN = "DOWN"
    INWARD = "INWARD"
    OUTWARD = "OUTWARD"
    TOP = "TOP"
    BOTTOM = "BOTTOM"
    MIDDLE = "MIDDLE"

# Set metadata after class creation
SimpleSpatialDirection._metadata = {
    "LEFT": {'description': 'To the left side'},
    "RIGHT": {'description': 'To the right side'},
    "FORWARD": {'description': 'In the forward direction', 'annotations': {'aliases': 'ahead, front'}},
    "BACKWARD": {'description': 'In the backward direction', 'annotations': {'aliases': 'back, behind, rear'}},
    "UP": {'description': 'In the upward direction', 'annotations': {'aliases': 'above, upward'}},
    "DOWN": {'description': 'In the downward direction', 'annotations': {'aliases': 'below, downward'}},
    "INWARD": {'description': 'Toward the center or interior', 'annotations': {'aliases': 'medial, toward center'}},
    "OUTWARD": {'description': 'Away from the center or exterior', 'annotations': {'aliases': 'peripheral, away from center'}},
    "TOP": {'description': 'At or toward the top', 'annotations': {'aliases': 'upper, uppermost'}},
    "BOTTOM": {'description': 'At or toward the bottom', 'annotations': {'aliases': 'lower, lowermost'}},
    "MIDDLE": {'description': 'At or toward the middle', 'annotations': {'aliases': 'center, central'}},
}

class AnatomicalSide(RichEnum):
    """
    Anatomical sides as defined in the Biological Spatial Ontology (BSPO).
    An anatomical region bounded by a plane perpendicular to an axis through the middle.
    """
    # Enum members
    LEFT = "LEFT"
    RIGHT = "RIGHT"
    ANTERIOR = "ANTERIOR"
    POSTERIOR = "POSTERIOR"
    DORSAL = "DORSAL"
    VENTRAL = "VENTRAL"
    LATERAL = "LATERAL"
    MEDIAL = "MEDIAL"
    PROXIMAL = "PROXIMAL"
    DISTAL = "DISTAL"
    APICAL = "APICAL"
    BASAL = "BASAL"
    SUPERFICIAL = "SUPERFICIAL"
    DEEP = "DEEP"
    SUPERIOR = "SUPERIOR"
    INFERIOR = "INFERIOR"
    IPSILATERAL = "IPSILATERAL"
    CONTRALATERAL = "CONTRALATERAL"
    CENTRAL = "CENTRAL"

# Set metadata after class creation
AnatomicalSide._metadata = {
    "LEFT": {'meaning': 'BSPO:0000000', 'aliases': ['left side']},
    "RIGHT": {'meaning': 'BSPO:0000007', 'aliases': ['right side']},
    "ANTERIOR": {'meaning': 'BSPO:0000055', 'annotations': {'aliases': 'front, rostral, cranial (in head region)'}, 'aliases': ['anterior side']},
    "POSTERIOR": {'meaning': 'BSPO:0000056', 'annotations': {'aliases': 'back, caudal'}, 'aliases': ['posterior side']},
    "DORSAL": {'meaning': 'BSPO:0000063', 'annotations': {'aliases': 'back (in vertebrates), upper (in humans)'}, 'aliases': ['dorsal side']},
    "VENTRAL": {'meaning': 'BSPO:0000068', 'annotations': {'aliases': 'belly, front (in vertebrates), lower (in humans)'}, 'aliases': ['ventral side']},
    "LATERAL": {'meaning': 'BSPO:0000066', 'annotations': {'aliases': 'side, outer'}, 'aliases': ['lateral side']},
    "MEDIAL": {'meaning': 'BSPO:0000067', 'annotations': {'aliases': 'inner, middle'}, 'aliases': ['medial side']},
    "PROXIMAL": {'meaning': 'BSPO:0000061', 'annotations': {'context': 'commonly used for limbs'}, 'aliases': ['proximal side']},
    "DISTAL": {'meaning': 'BSPO:0000062', 'annotations': {'context': 'commonly used for limbs'}, 'aliases': ['distal side']},
    "APICAL": {'meaning': 'BSPO:0000057', 'annotations': {'context': 'cells, organs, organisms'}, 'aliases': ['apical side']},
    "BASAL": {'meaning': 'BSPO:0000058', 'annotations': {'context': 'cells, organs, organisms'}, 'aliases': ['basal side']},
    "SUPERFICIAL": {'meaning': 'BSPO:0000004', 'annotations': {'aliases': 'external, outer'}, 'aliases': ['superficial side']},
    "DEEP": {'meaning': 'BSPO:0000003', 'annotations': {'aliases': 'internal, inner'}, 'aliases': ['deep side']},
    "SUPERIOR": {'meaning': 'BSPO:0000022', 'annotations': {'aliases': 'cranial (toward head), upper'}, 'aliases': ['superior side']},
    "INFERIOR": {'meaning': 'BSPO:0000025', 'annotations': {'aliases': 'caudal (toward tail), lower'}, 'aliases': ['inferior side']},
    "IPSILATERAL": {'meaning': 'BSPO:0000065', 'annotations': {'context': 'relative to a reference point'}, 'aliases': ['ipsilateral side']},
    "CONTRALATERAL": {'meaning': 'BSPO:0000060', 'annotations': {'context': 'relative to a reference point'}, 'aliases': ['contralateral side']},
    "CENTRAL": {'meaning': 'BSPO:0000059', 'annotations': {'aliases': 'middle'}, 'aliases': ['central side']},
}

class AnatomicalRegion(RichEnum):
    """
    Anatomical regions based on spatial position
    """
    # Enum members
    ANTERIOR_REGION = "ANTERIOR_REGION"
    POSTERIOR_REGION = "POSTERIOR_REGION"
    DORSAL_REGION = "DORSAL_REGION"
    VENTRAL_REGION = "VENTRAL_REGION"
    LATERAL_REGION = "LATERAL_REGION"
    MEDIAL_REGION = "MEDIAL_REGION"
    PROXIMAL_REGION = "PROXIMAL_REGION"
    DISTAL_REGION = "DISTAL_REGION"
    APICAL_REGION = "APICAL_REGION"
    BASAL_REGION = "BASAL_REGION"
    CENTRAL_REGION = "CENTRAL_REGION"
    PERIPHERAL_REGION = "PERIPHERAL_REGION"

# Set metadata after class creation
AnatomicalRegion._metadata = {
    "ANTERIOR_REGION": {'meaning': 'BSPO:0000071', 'aliases': ['anterior region']},
    "POSTERIOR_REGION": {'meaning': 'BSPO:0000072', 'aliases': ['posterior region']},
    "DORSAL_REGION": {'meaning': 'BSPO:0000079', 'aliases': ['dorsal region']},
    "VENTRAL_REGION": {'meaning': 'BSPO:0000084', 'aliases': ['ventral region']},
    "LATERAL_REGION": {'meaning': 'BSPO:0000082', 'aliases': ['lateral region']},
    "MEDIAL_REGION": {'meaning': 'BSPO:0000083', 'aliases': ['medial region']},
    "PROXIMAL_REGION": {'meaning': 'BSPO:0000077', 'aliases': ['proximal region']},
    "DISTAL_REGION": {'meaning': 'BSPO:0000078', 'aliases': ['distal region']},
    "APICAL_REGION": {'meaning': 'BSPO:0000073', 'aliases': ['apical region']},
    "BASAL_REGION": {'meaning': 'BSPO:0000074', 'aliases': ['basal region']},
    "CENTRAL_REGION": {'meaning': 'BSPO:0000075', 'aliases': ['central region']},
    "PERIPHERAL_REGION": {'meaning': 'BSPO:0000127', 'aliases': ['peripheral region']},
}

class AnatomicalAxis(RichEnum):
    """
    Anatomical axes defining spatial organization
    """
    # Enum members
    ANTERIOR_POSTERIOR = "ANTERIOR_POSTERIOR"
    DORSAL_VENTRAL = "DORSAL_VENTRAL"
    LEFT_RIGHT = "LEFT_RIGHT"
    PROXIMAL_DISTAL = "PROXIMAL_DISTAL"
    APICAL_BASAL = "APICAL_BASAL"

# Set metadata after class creation
AnatomicalAxis._metadata = {
    "ANTERIOR_POSTERIOR": {'meaning': 'BSPO:0000013', 'annotations': {'aliases': 'AP axis, rostrocaudal axis'}, 'aliases': ['anterior-posterior axis']},
    "DORSAL_VENTRAL": {'meaning': 'BSPO:0000016', 'annotations': {'aliases': 'DV axis'}, 'aliases': ['dorsal-ventral axis']},
    "LEFT_RIGHT": {'meaning': 'BSPO:0000017', 'annotations': {'aliases': 'LR axis, mediolateral axis'}, 'aliases': ['left-right axis']},
    "PROXIMAL_DISTAL": {'meaning': 'BSPO:0000018', 'annotations': {'context': 'commonly used for appendages'}, 'aliases': ['transverse plane']},
    "APICAL_BASAL": {'meaning': 'BSPO:0000023', 'annotations': {'context': 'epithelial cells, plant structures'}, 'aliases': ['apical-basal gradient']},
}

class AnatomicalPlane(RichEnum):
    """
    Standard anatomical planes for sectioning
    """
    # Enum members
    SAGITTAL = "SAGITTAL"
    MIDSAGITTAL = "MIDSAGITTAL"
    PARASAGITTAL = "PARASAGITTAL"
    CORONAL = "CORONAL"
    TRANSVERSE = "TRANSVERSE"
    OBLIQUE = "OBLIQUE"

# Set metadata after class creation
AnatomicalPlane._metadata = {
    "SAGITTAL": {'meaning': 'BSPO:0000417', 'annotations': {'orientation': 'parallel to the median plane'}, 'aliases': ['sagittal plane']},
    "MIDSAGITTAL": {'meaning': 'BSPO:0000009', 'annotations': {'aliases': 'median plane', 'note': 'divides body into equal left and right halves'}, 'aliases': ['midsagittal plane']},
    "PARASAGITTAL": {'meaning': 'BSPO:0000008', 'annotations': {'note': 'any sagittal plane not at midline'}, 'aliases': ['parasagittal plane']},
    "CORONAL": {'meaning': 'BSPO:0000019', 'annotations': {'aliases': 'frontal plane', 'orientation': 'perpendicular to sagittal plane'}, 'aliases': ['horizontal plane']},
    "TRANSVERSE": {'meaning': 'BSPO:0000018', 'annotations': {'aliases': 'horizontal plane, axial plane', 'orientation': 'perpendicular to longitudinal axis'}, 'aliases': ['transverse plane']},
    "OBLIQUE": {'description': 'Any plane not parallel to sagittal, coronal, or transverse planes', 'annotations': {'note': 'angled section'}},
}

class SpatialRelationship(RichEnum):
    """
    Spatial relationships between anatomical structures
    """
    # Enum members
    ADJACENT_TO = "ADJACENT_TO"
    ANTERIOR_TO = "ANTERIOR_TO"
    POSTERIOR_TO = "POSTERIOR_TO"
    DORSAL_TO = "DORSAL_TO"
    VENTRAL_TO = "VENTRAL_TO"
    LATERAL_TO = "LATERAL_TO"
    MEDIAL_TO = "MEDIAL_TO"
    PROXIMAL_TO = "PROXIMAL_TO"
    DISTAL_TO = "DISTAL_TO"
    SUPERFICIAL_TO = "SUPERFICIAL_TO"
    DEEP_TO = "DEEP_TO"
    SURROUNDS = "SURROUNDS"
    WITHIN = "WITHIN"
    BETWEEN = "BETWEEN"

# Set metadata after class creation
SpatialRelationship._metadata = {
    "ADJACENT_TO": {'meaning': 'RO:0002220', 'aliases': ['adjacent to']},
    "ANTERIOR_TO": {'meaning': 'BSPO:0000096', 'aliases': ['anterior to']},
    "POSTERIOR_TO": {'meaning': 'BSPO:0000099', 'aliases': ['posterior to']},
    "DORSAL_TO": {'meaning': 'BSPO:0000098', 'aliases': ['dorsal to']},
    "VENTRAL_TO": {'meaning': 'BSPO:0000102', 'aliases': ['ventral to']},
    "LATERAL_TO": {'meaning': 'BSPO:0000114', 'aliases': ['lateral to']},
    "MEDIAL_TO": {'meaning': 'BSPO:0000115', 'aliases': ['X medial to y if x is closer to the midsagittal plane than y.']},
    "PROXIMAL_TO": {'meaning': 'BSPO:0000100', 'aliases': ['proximal to']},
    "DISTAL_TO": {'meaning': 'BSPO:0000097', 'aliases': ['distal to']},
    "SUPERFICIAL_TO": {'meaning': 'BSPO:0000108', 'aliases': ['superficial to']},
    "DEEP_TO": {'meaning': 'BSPO:0000107', 'aliases': ['deep to']},
    "SURROUNDS": {'meaning': 'RO:0002221', 'aliases': ['surrounds']},
    "WITHIN": {'description': 'Inside or contained by', 'annotations': {'inverse_of': 'contains'}},
    "BETWEEN": {'description': 'In the space separating two structures', 'annotations': {'note': 'requires two reference points'}},
}

class CellPolarity(RichEnum):
    """
    Spatial polarity in cells and tissues
    """
    # Enum members
    APICAL = "APICAL"
    BASAL = "BASAL"
    LATERAL = "LATERAL"
    APICAL_LATERAL = "APICAL_LATERAL"
    BASAL_LATERAL = "BASAL_LATERAL"
    LEADING_EDGE = "LEADING_EDGE"
    TRAILING_EDGE = "TRAILING_EDGE"
    PROXIMAL_POLE = "PROXIMAL_POLE"
    DISTAL_POLE = "DISTAL_POLE"

# Set metadata after class creation
CellPolarity._metadata = {
    "APICAL": {'description': 'The free surface of an epithelial cell', 'annotations': {'location': 'typically faces lumen or external environment'}},
    "BASAL": {'description': 'The attached surface of an epithelial cell', 'annotations': {'location': 'typically attached to basement membrane'}},
    "LATERAL": {'description': 'The sides of an epithelial cell', 'annotations': {'location': 'faces neighboring cells'}},
    "APICAL_LATERAL": {'description': 'Junction between apical and lateral surfaces'},
    "BASAL_LATERAL": {'description': 'Junction between basal and lateral surfaces'},
    "LEADING_EDGE": {'description': 'Front of a migrating cell', 'annotations': {'context': 'cell migration'}},
    "TRAILING_EDGE": {'description': 'Rear of a migrating cell', 'annotations': {'context': 'cell migration'}},
    "PROXIMAL_POLE": {'description': 'Pole closer to the cell body', 'annotations': {'context': 'neurons, polarized cells'}},
    "DISTAL_POLE": {'description': 'Pole further from the cell body', 'annotations': {'context': 'neurons, polarized cells'}},
}

__all__ = [
    "SimpleSpatialDirection",
    "AnatomicalSide",
    "AnatomicalRegion",
    "AnatomicalAxis",
    "AnatomicalPlane",
    "SpatialRelationship",
    "CellPolarity",
]