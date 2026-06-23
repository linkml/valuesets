"""
PATO Phenotypic Quality Value Sets

Value sets derived from the Phenotype And Trait Ontology (PATO). Each enum corresponds to a leaf attribute in the PATO hierarchy, with child quality values as permissible values.

Generated from: bio/pato.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class ColorEnum(RichEnum):
    """
    A composite chromatic quality composed of hue, saturation and intensity parts. Derived from PATO color (PATO:0000014) child values.
    """
    # Enum members
    BLACK = "BLACK"
    WHITE = "WHITE"
    GREY = "GREY"
    RED = "RED"
    ORANGE = "ORANGE"
    YELLOW = "YELLOW"
    GREEN = "GREEN"
    CYAN = "CYAN"
    BLUE = "BLUE"
    VIOLET = "VIOLET"
    PURPLE = "PURPLE"
    MAGENTA = "MAGENTA"
    BROWN = "BROWN"
    MAROON = "MAROON"
    ROSY = "ROSY"
    VERMILION = "VERMILION"
    COLORED = "COLORED"

# Set metadata after class creation
ColorEnum._metadata = {
    "BLACK": {'description': 'A color that lacks any hues as parts', 'meaning': 'PATO:0000317'},
    "WHITE": {'description': 'An achromatic color of maximum brightness', 'meaning': 'PATO:0000323'},
    "GREY": {'description': 'A color between white and black colors', 'meaning': 'PATO:0000950', 'aliases': ['gray']},
    "RED": {'description': 'A color hue with high wavelength of the long-wave end of the visible spectrum (630-750 nm)', 'meaning': 'PATO:0000322'},
    "ORANGE": {'description': 'A color hue with high-medium wavelength lying between red and yellow (585-620 nm)', 'meaning': 'PATO:0000953'},
    "YELLOW": {'description': 'A color hue with medium wavelength lying between orange and green (570-590 nm)', 'meaning': 'PATO:0000324'},
    "GREEN": {'description': 'A color hue with medium-low wavelength lying between yellow and blue (490-570 nm)', 'meaning': 'PATO:0000320'},
    "CYAN": {'description': 'A color consisting of green and blue hue', 'meaning': 'PATO:0000319'},
    "BLUE": {'description': 'A color hue with low wavelength lying between green and indigo (420-490 nm)', 'meaning': 'PATO:0000318'},
    "VIOLET": {'description': 'A color hue with very low wavelength lying between reddish blue and bluish purple (380-420 nm)', 'meaning': 'PATO:0001424'},
    "PURPLE": {'description': 'A color that falls about midway between red and blue in hue', 'meaning': 'PATO:0000951'},
    "MAGENTA": {'description': 'A color consisting of red and blue hues', 'meaning': 'PATO:0000321'},
    "BROWN": {'description': 'A color consisting of dark orange, red, of very low intensity', 'meaning': 'PATO:0000952'},
    "MAROON": {'description': 'A color consisting of purple and brown hue', 'meaning': 'PATO:0001426'},
    "ROSY": {'description': 'A color hue consisting of red and yellow hue with high brightness', 'meaning': 'PATO:0001425', 'aliases': ['pink']},
    "VERMILION": {'description': 'A color consisting of red and orange hue with a slight amount of gray', 'meaning': 'PATO:0001302'},
    "COLORED": {'description': 'A color quality inhering in a bearer by virtue of having color', 'meaning': 'PATO:0000336'},
}

class ShapeEnum(RichEnum):
    """
    A morphological quality inhering in a bearer by virtue of the bearer's ratios of distances between its features. Derived from PATO shape (PATO:0000052) child values.
    """
    # Enum members
    CIRCULAR = "CIRCULAR"
    ELLIPTIC = "ELLIPTIC"
    SPHEROID = "SPHEROID"
    CONICAL = "CONICAL"
    COLUMNAR = "COLUMNAR"
    TUBULAR = "TUBULAR"
    FLAT = "FLAT"
    ELONGATED = "ELONGATED"
    LINEAR = "LINEAR"
    FILAMENTOUS = "FILAMENTOUS"
    SLENDER = "SLENDER"
    BROAD = "BROAD"
    ROBUST = "ROBUST"
    STRAIGHT = "STRAIGHT"
    BENT = "BENT"
    ANGULAR = "ANGULAR"
    LOBED = "LOBED"
    TRUNCATED = "TRUNCATED"
    PYRAMIDAL = "PYRAMIDAL"
    STAR_SHAPED = "STAR_SHAPED"
    SIGMOID = "SIGMOID"
    UNDULATE = "UNDULATE"
    PINNATE = "PINNATE"
    PLEOMORPHIC = "PLEOMORPHIC"
    COILING = "COILING"

# Set metadata after class creation
ShapeEnum._metadata = {
    "CIRCULAR": {'description': 'A shape where every part of the surface or circumference is equidistant from the center', 'meaning': 'PATO:0000411'},
    "ELLIPTIC": {'description': 'Oval with two axes of symmetry, as produced by a conical section', 'meaning': 'PATO:0000947', 'aliases': ['oval']},
    "SPHEROID": {'description': 'A convex 3-D shape obtained by rotating an ellipse about one of its principal axes', 'meaning': 'PATO:0001865'},
    "CONICAL": {'description': 'A convex 3-D shape resembling a cone with a round cross section that tapers', 'meaning': 'PATO:0002021'},
    "COLUMNAR": {'description': 'Elongated and cylindrical in shape', 'meaning': 'PATO:0002063', 'aliases': ['cylindrical']},
    "TUBULAR": {'description': 'A cylindrical shape that is hollow', 'meaning': 'PATO:0002299'},
    "FLAT": {'description': 'Having a horizontal surface without a slope, tilt, or curvature', 'meaning': 'PATO:0000407'},
    "ELONGATED": {'description': 'Length being notably higher relative to width', 'meaning': 'PATO:0001154'},
    "LINEAR": {'description': 'Narrow, with approximately parallel sides', 'meaning': 'PATO:0001199'},
    "FILAMENTOUS": {'description': 'Having thin filaments or thread-like structures', 'meaning': 'PATO:0001360'},
    "SLENDER": {'description': 'Being small or narrow in circumference or width in proportion to length or height', 'meaning': 'PATO:0002212'},
    "BROAD": {'description': 'Width being notably higher relative to comparable entities', 'meaning': 'PATO:0002359'},
    "ROBUST": {'description': 'Being strong, thick, or stout in form', 'meaning': 'PATO:0002310'},
    "STRAIGHT": {'description': 'Free of curves, bends, or angles', 'meaning': 'PATO:0002180'},
    "BENT": {'description': 'Having one or more fixed curves, folds, or angles', 'meaning': 'PATO:0000617'},
    "ANGULAR": {'description': 'Having at least one angle formed by two planes', 'meaning': 'PATO:0001977'},
    "LOBED": {'description': 'Being partly divided into a determinate number of segments', 'meaning': 'PATO:0001979'},
    "TRUNCATED": {'description': 'Terminating abruptly by a transverse line or plane', 'meaning': 'PATO:0000936'},
    "PYRAMIDAL": {'description': 'Having triangular faces meeting at a common point', 'meaning': 'PATO:0002336'},
    "STAR_SHAPED": {'description': 'Being arranged like a star with radiating points', 'meaning': 'PATO:0002065', 'aliases': ['stellate']},
    "SIGMOID": {'description': 'Consisting of two curves in opposite directions like the letter S', 'meaning': 'PATO:0001878'},
    "UNDULATE": {'description': 'Having a sinuate margin that moves smoothly and regularly up and down', 'meaning': 'PATO:0000967', 'aliases': ['wavy']},
    "PINNATE": {'description': 'Having leaflets or branches on each side of a common axis', 'meaning': 'PATO:0000410'},
    "PLEOMORPHIC": {'description': 'Having the ability to take on multiple forms', 'meaning': 'PATO:0001356'},
    "COILING": {'description': 'Being wound in a spiral or helix', 'meaning': 'PATO:0001794', 'aliases': ['coiled', 'helical']},
}

class RelativeChangeEnum(RichEnum):
    """
    Direction of change of any quality relative to normal or baseline. This is PATO's general-purpose deviation-from-normal axis (PATO:0000069) that crosscuts all specific quality attributes (size, rate, amount, etc.).
    """
    # Enum members
    NORMAL = "NORMAL"
    ABNORMAL = "ABNORMAL"
    INCREASED = "INCREASED"
    DECREASED = "DECREASED"
    INCREASED_MAGNITUDE = "INCREASED_MAGNITUDE"
    DECREASED_MAGNITUDE = "DECREASED_MAGNITUDE"

# Set metadata after class creation
RelativeChangeEnum._metadata = {
    "NORMAL": {'description': 'Exhibiting no deviation from normal or average', 'meaning': 'PATO:0000461'},
    "ABNORMAL": {'description': 'Deviating from normal or average', 'meaning': 'PATO:0000460'},
    "INCREASED": {'description': 'A value that is increased compared to normal or average', 'meaning': 'PATO:0002300', 'aliases': ['elevated', 'high']},
    "DECREASED": {'description': 'A value that is decreased compared to normal or average', 'meaning': 'PATO:0002301', 'aliases': ['reduced', 'low']},
    "INCREASED_MAGNITUDE": {'description': 'An increased magnitude of a quality', 'meaning': 'PATO:0002017'},
    "DECREASED_MAGNITUDE": {'description': 'A decreased magnitude of a quality', 'meaning': 'PATO:0002018'},
}

class IntensityEnum(RichEnum):
    """
    A quality inhering in a bearer by virtue of the bearer's possessing or displaying a distinctive feature in type or degree or effect or force. Derived from PATO intensity (PATO:0000049) child values.
    """
    # Enum members
    BORDERLINE = "BORDERLINE"
    MILD = "MILD"
    MODERATE = "MODERATE"
    SEVERE = "SEVERE"
    PROFOUND = "PROFOUND"
    INCREASED_INTENSITY = "INCREASED_INTENSITY"
    DECREASED_INTENSITY = "DECREASED_INTENSITY"
    REMITTENT = "REMITTENT"

# Set metadata after class creation
IntensityEnum._metadata = {
    "BORDERLINE": {'description': 'Borderline in effect or force compared to baseline or normal', 'meaning': 'PATO:0002628'},
    "MILD": {'description': 'Less than moderate in type or degree or effect or force', 'meaning': 'PATO:0000394'},
    "MODERATE": {'description': 'Less than extreme in type or degree or effect or force', 'meaning': 'PATO:0000395'},
    "SEVERE": {'description': 'Extremely bad or unpleasant in type or degree or effect or force', 'meaning': 'PATO:0000396'},
    "PROFOUND": {'description': 'Very severe in intensity', 'meaning': 'PATO:0002629'},
    "INCREASED_INTENSITY": {'description': 'Intensity which is relatively high', 'meaning': 'PATO:0001782'},
    "DECREASED_INTENSITY": {'description': 'Intensity which is relatively low', 'meaning': 'PATO:0001783'},
    "REMITTENT": {'description': 'Characterised by temporary abatement in severity', 'meaning': 'PATO:0001841'},
}

class TextureEnum(RichEnum):
    """
    A morphological quality inhering in a bearer by virtue of the bearer's surface characteristics. Derived from PATO texture (PATO:0000150) child values.
    """
    # Enum members
    SMOOTH = "SMOOTH"
    ROUGH = "ROUGH"
    SCALY = "SCALY"
    FLAKY = "FLAKY"
    GROOVED = "GROOVED"
    BLISTERED = "BLISTERED"
    HAIRY = "HAIRY"
    ABRASED = "ABRASED"
    RUSTY = "RUSTY"
    FOVEATE = "FOVEATE"

# Set metadata after class creation
TextureEnum._metadata = {
    "SMOOTH": {'description': 'Having a surface free of roughness or irregularities', 'meaning': 'PATO:0000701'},
    "ROUGH": {'description': 'Having an irregular surface', 'meaning': 'PATO:0000700'},
    "SCALY": {'description': 'Being covered or partially covered with scales', 'meaning': 'PATO:0001804'},
    "FLAKY": {'description': 'Formed or tending to form flakes or thin, crisp fragments', 'meaning': 'PATO:0001805'},
    "GROOVED": {'description': 'Being marked with one or more channels', 'meaning': 'PATO:0002255'},
    "BLISTERED": {'description': 'Having a local accumulation of fluid underneath the surface', 'meaning': 'PATO:0001928'},
    "HAIRY": {'description': 'Having hair or bristles', 'meaning': 'PATO:0000066', 'aliases': ['pilose', 'hairy']},
    "ABRASED": {'description': 'Having a portion of the surface scraped away', 'meaning': 'PATO:0001849'},
    "RUSTY": {'description': 'Being covered by iron oxide as a result of oxidation', 'meaning': 'PATO:0070059'},
    "FOVEATE": {'description': 'Being marked by the presence of small, shallow, regular depressions', 'meaning': 'PATO:0002296'},
}

class PATOBiologicalSexEnum(RichEnum):
    """
    An organismal quality inhering in a bearer by virtue of the bearer's ability to undergo sexual reproduction. Derived from PATO biological sex (PATO:0000047) and phenotypic sex (PATO:0001894) child values.
    """
    # Enum members
    FEMALE = "FEMALE"
    MALE = "MALE"
    HERMAPHRODITE = "HERMAPHRODITE"
    MALE_WITH_DSD = "MALE_WITH_DSD"
    FEMALE_WITH_DSD = "FEMALE_WITH_DSD"
    PSEUDOHERMAPHRODITE = "PSEUDOHERMAPHRODITE"

# Set metadata after class creation
PATOBiologicalSexEnum._metadata = {
    "FEMALE": {'description': 'A biological sex quality inhering in an individual or population that only produces gametes that can be fertilised by male gametes', 'meaning': 'PATO:0000383'},
    "MALE": {'description': 'A biological sex quality inhering in an individual or population whose sex organs contain only male gametes', 'meaning': 'PATO:0000384'},
    "HERMAPHRODITE": {'description': 'A biological sex quality inhering in an organism or population with both male and female sexual organs in one individual', 'meaning': 'PATO:0001340'},
    "MALE_WITH_DSD": {'description': 'A male of a non-hermaphroditic species with ambiguous or atypical congenital development of the reproductive system', 'meaning': 'PATO:0040049'},
    "FEMALE_WITH_DSD": {'description': 'A female of a non-hermaphroditic species with ambiguous or atypical congenital development of the reproductive system', 'meaning': 'PATO:0040056'},
    "PSEUDOHERMAPHRODITE": {'description': 'Having internal reproductive organs of one sex and external sexual characteristics of the other sex', 'meaning': 'PATO:0001827'},
}

class MaturityEnum(RichEnum):
    """
    A quality of a single physical entity held by a bearer when it exhibits a state of growth, differentiation, or development. Derived from PATO maturity (PATO:0000261) child values.
    """
    # Enum members
    NEONATAL = "NEONATAL"
    LARVAL = "LARVAL"
    PREPUBESCENT = "PREPUBESCENT"
    PUPAL = "PUPAL"
    PREPUPAL = "PREPUPAL"
    PUBESCENT = "PUBESCENT"
    ADOLESCENT = "ADOLESCENT"
    JUVENILE = "JUVENILE"
    IMMATURE = "IMMATURE"
    MATURE = "MATURE"

# Set metadata after class creation
MaturityEnum._metadata = {
    "NEONATAL": {'description': 'Being at the point or shortly after birth', 'meaning': 'PATO:0002206'},
    "LARVAL": {'description': 'Undergoing indirect development and metamorphosis', 'meaning': 'PATO:0001185'},
    "PREPUBESCENT": {'description': 'Being at the age immediately before puberty', 'meaning': 'PATO:0001186'},
    "PUPAL": {'description': 'Being in the chrysalis (cocoon) or post-larval stage', 'meaning': 'PATO:0001187'},
    "PREPUPAL": {'description': 'Being in an inactive stage between the larval and the pupal stages', 'meaning': 'PATO:0001188'},
    "PUBESCENT": {'description': 'Having arrived at the onset of puberty but not yet fully mature', 'meaning': 'PATO:0000455'},
    "ADOLESCENT": {'description': 'Being between the onset of puberty and maturity', 'meaning': 'PATO:0001189'},
    "JUVENILE": {'description': 'Not fully grown or developed', 'meaning': 'PATO:0001190'},
    "IMMATURE": {'description': 'Lacking complete growth, differentiation, or development', 'meaning': 'PATO:0001501'},
    "MATURE": {'description': 'Exhibiting complete growth, differentiation, or development', 'meaning': 'PATO:0001701', 'aliases': ['adult']},
}

class ViabilityEnum(RichEnum):
    """
    An organismal quality inhering in a bearer by virtue of the bearer's disposition to survive and develop normally. Derived from PATO viability (PATO:0000169) child values.
    """
    # Enum members
    ALIVE = "ALIVE"
    DEAD = "DEAD"
    VIABLE = "VIABLE"
    LETHAL = "LETHAL"
    SEMI_VIABLE = "SEMI_VIABLE"
    SEMI_LETHAL = "SEMI_LETHAL"
    IMMORTAL = "IMMORTAL"
    DECAYED = "DECAYED"

# Set metadata after class creation
ViabilityEnum._metadata = {
    "ALIVE": {'description': "The bearer's condition before death", 'meaning': 'PATO:0001421'},
    "DEAD": {'description': "The cessation of the bearer's life", 'meaning': 'PATO:0001422'},
    "VIABLE": {'description': "The bearer's ability to survive or the long term survival ability of a given population", 'meaning': 'PATO:0000719'},
    "LETHAL": {'description': "The bearer's long term survival inability", 'meaning': 'PATO:0000718'},
    "SEMI_VIABLE": {'description': "Some of the population members' ability to survive", 'meaning': 'PATO:0001770'},
    "SEMI_LETHAL": {'description': "Some of the population members' inability to survive to reproduce", 'meaning': 'PATO:0001768'},
    "IMMORTAL": {'description': 'Being capable of indefinite growth or division', 'meaning': 'PATO:0001991'},
    "DECAYED": {'description': 'Decomposition into component parts', 'meaning': 'PATO:0001432'},
}

class CellularityEnum(RichEnum):
    """
    An organismal quality inhering in a bearer by virtue of the bearer's consisting of cells. Derived from PATO cellularity (PATO:0001992) child values.
    """
    # Enum members
    UNICELLULAR = "UNICELLULAR"
    MULTICELLULAR = "MULTICELLULAR"

# Set metadata after class creation
CellularityEnum._metadata = {
    "UNICELLULAR": {'description': 'Consisting of exactly one cell', 'meaning': 'PATO:0001994'},
    "MULTICELLULAR": {'description': 'Consisting of more than one cell', 'meaning': 'PATO:0001993'},
}

class SpatialPatternEnum(RichEnum):
    """
    A spatial quality inhering in a bearer by virtue of the bearer's exhibiting repetition of placement of its parts. Derived from PATO spatial pattern (PATO:0000060) child values.
    """
    # Enum members
    LOCALIZED = "LOCALIZED"
    UNLOCALISED = "UNLOCALISED"
    MULTI_LOCALISED = "MULTI_LOCALISED"
    DISTRIBUTED = "DISTRIBUTED"
    UNDISTRIBUTED = "UNDISTRIBUTED"
    SPARSE = "SPARSE"
    UNILATERAL = "UNILATERAL"
    VERTICAL = "VERTICAL"
    REGULAR_SPATIAL_PATTERN = "REGULAR_SPATIAL_PATTERN"
    IRREGULAR_SPATIAL_PATTERN = "IRREGULAR_SPATIAL_PATTERN"
    GENERALIZED = "GENERALIZED"
    SEGMENTAL = "SEGMENTAL"
    RANDOM_PATTERN = "RANDOM_PATTERN"
    SYMMETRICAL = "SYMMETRICAL"

# Set metadata after class creation
SpatialPatternEnum._metadata = {
    "LOCALIZED": {'description': 'Being confined or restricted to a particular location', 'meaning': 'PATO:0000627'},
    "UNLOCALISED": {'description': 'Not being confined or restricted to a particular location', 'meaning': 'PATO:0000635', 'aliases': ['diffuse']},
    "MULTI_LOCALISED": {'description': 'Being confined or restricted to multiple locations', 'meaning': 'PATO:0001791'},
    "DISTRIBUTED": {'description': 'Being spread out or scattered about or divided up', 'meaning': 'PATO:0001566'},
    "UNDISTRIBUTED": {'description': 'Not being spread out or scattered about or divided up', 'meaning': 'PATO:0001567'},
    "SPARSE": {'description': 'Being scattered and spread irregularly at a distance from each other', 'meaning': 'PATO:0001609'},
    "UNILATERAL": {'description': 'Involving only one part or side', 'meaning': 'PATO:0000634'},
    "VERTICAL": {'description': 'Being situated at right angles to the horizon', 'meaning': 'PATO:0001854'},
    "REGULAR_SPATIAL_PATTERN": {'description': 'Having a repeatable or predictable placement', 'meaning': 'PATO:0000440'},
    "IRREGULAR_SPATIAL_PATTERN": {'description': 'Magnitude or relationships between repeated parts lack consistency', 'meaning': 'PATO:0000330'},
    "GENERALIZED": {'description': 'Affecting all regions without specificity of distribution', 'meaning': 'PATO:0002403'},
    "SEGMENTAL": {'description': 'Affecting a segment or segments', 'meaning': 'PATO:0002404'},
    "RANDOM_PATTERN": {'description': 'Characterised by an unidentifiable pattern', 'meaning': 'PATO:0002401'},
    "SYMMETRICAL": {'description': 'Correspondence in size, shape, and relative position of parts on opposite sides of a dividing line or about a center or axis', 'meaning': 'PATO:0000965'},
}

__all__ = [
    "ColorEnum",
    "ShapeEnum",
    "RelativeChangeEnum",
    "IntensityEnum",
    "TextureEnum",
    "PATOBiologicalSexEnum",
    "MaturityEnum",
    "ViabilityEnum",
    "CellularityEnum",
    "SpatialPatternEnum",
]