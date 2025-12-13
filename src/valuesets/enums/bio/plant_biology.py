"""
Plant Biology Value Sets

Value sets related to plant biology, including reproductive systems,
breeding systems, and other plant-specific characteristics.

Generated from: bio/plant_biology.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class PlantSexualSystem(RichEnum):
    """
    Sexual systems in plants, describing the distribution and types of
    reproductive organs (flowers) within and among individual plants.
    """
    # Enum members
    ANDRODIOECIOUS = "ANDRODIOECIOUS"
    ANDROECIOUS = "ANDROECIOUS"
    ANDROGYNOMONOECIOUS = "ANDROGYNOMONOECIOUS"
    ANDROGYNOUS = "ANDROGYNOUS"
    ANDROMONOECIOUS = "ANDROMONOECIOUS"
    BISEXUAL = "BISEXUAL"
    DICHOGAMOUS = "DICHOGAMOUS"
    DICLINOUS = "DICLINOUS"
    DIOECIOUS = "DIOECIOUS"
    GYNODIOECIOUS = "GYNODIOECIOUS"
    GYNOECIOUS = "GYNOECIOUS"
    GYNOMONOECIOUS = "GYNOMONOECIOUS"
    HERMAPHRODITIC = "HERMAPHRODITIC"
    IMPERFECT = "IMPERFECT"
    MONOCLINOUS = "MONOCLINOUS"
    MONOECIOUS = "MONOECIOUS"
    PERFECT = "PERFECT"
    POLYGAMODIOECIOUS = "POLYGAMODIOECIOUS"
    POLYGAMOMONOECIOUS = "POLYGAMOMONOECIOUS"
    POLYGAMOUS = "POLYGAMOUS"
    PROTANDROUS = "PROTANDROUS"
    PROTOGYNOUS = "PROTOGYNOUS"
    SUBANDROECIOUS = "SUBANDROECIOUS"
    SUBDIOECIOUS = "SUBDIOECIOUS"
    SUBGYNOECIOUS = "SUBGYNOECIOUS"
    SYNOECIOUS = "SYNOECIOUS"
    TRIMONOECIOUS = "TRIMONOECIOUS"
    TRIOECIOUS = "TRIOECIOUS"
    UNISEXUAL = "UNISEXUAL"

# Set metadata after class creation
PlantSexualSystem._metadata = {
    "ANDRODIOECIOUS": {'description': 'A sexual system in which males and hermaphrodites coexist in a population', 'meaning': 'GSSO:011874'},
    "ANDROECIOUS": {'description': 'Having only male flowers (staminate flowers)'},
    "ANDROGYNOMONOECIOUS": {'description': 'Having male, female, and bisexual flowers on the same plant'},
    "ANDROGYNOUS": {'description': 'Having both male and female reproductive organs; hermaphroditic'},
    "ANDROMONOECIOUS": {'description': 'Having both male and hermaphroditic flowers on the same plant', 'meaning': 'GSSO:011870'},
    "BISEXUAL": {'description': 'Having both male and female reproductive organs in the same flower'},
    "DICHOGAMOUS": {'description': 'Having male and female organs that mature at different times'},
    "DICLINOUS": {'description': 'Having unisexual flowers (either male or female, not both)'},
    "DIOECIOUS": {'description': 'Having male and female flowers on separate plants', 'meaning': 'GSSO:011872'},
    "GYNODIOECIOUS": {'description': 'Having female and hermaphroditic plants in the same population', 'meaning': 'GSSO:011873'},
    "GYNOECIOUS": {'description': 'Having only female flowers (pistillate flowers)'},
    "GYNOMONOECIOUS": {'description': 'Having both female and hermaphroditic flowers on the same plant', 'meaning': 'GSSO:011869'},
    "HERMAPHRODITIC": {'description': 'Having both male and female reproductive organs', 'meaning': 'PATO:0001340'},
    "IMPERFECT": {'description': 'Flowers lacking either stamens or pistils (unisexual)'},
    "MONOCLINOUS": {'description': 'Having bisexual flowers (both male and female organs)'},
    "MONOECIOUS": {'description': 'Having separate male and female flowers on the same plant', 'meaning': 'GSSO:011868'},
    "PERFECT": {'description': 'Flowers having both stamens and pistils (bisexual)'},
    "POLYGAMODIOECIOUS": {'description': 'Having male, female, and bisexual flowers on separate plants'},
    "POLYGAMOMONOECIOUS": {'description': 'Having male, female, and bisexual flowers on the same plant'},
    "POLYGAMOUS": {'description': 'Having male, female, and bisexual flowers'},
    "PROTANDROUS": {'description': 'Starting as male and changing to female at a later stage', 'meaning': 'PATO:0040053'},
    "PROTOGYNOUS": {'description': 'Starting as female and changing to male at a later stage', 'meaning': 'PATO:0040052'},
    "SUBANDROECIOUS": {'description': 'Predominantly male plants with occasional hermaphroditic flowers'},
    "SUBDIOECIOUS": {'description': 'Predominantly dioecious with occasional hermaphroditic individuals'},
    "SUBGYNOECIOUS": {'description': 'Predominantly female plants with occasional hermaphroditic flowers'},
    "SYNOECIOUS": {'description': 'Having male and female organs in the same structure'},
    "TRIMONOECIOUS": {'description': 'Having male, female, and bisexual flowers on the same plant'},
    "TRIOECIOUS": {'description': 'Having males, females, and hermaphrodites in the same population', 'meaning': 'GSSO:011875'},
    "UNISEXUAL": {'description': 'Having only one sex (either male or female reproductive organs)'},
}

__all__ = [
    "PlantSexualSystem",
]