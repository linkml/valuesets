"""

Generated from: bio/plant_sex.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class PlantSexEnum(RichEnum):
    """
    Plant reproductive and sexual system types
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
PlantSexEnum._metadata = {
    "ANDRODIOECIOUS": {'description': 'Having male and hermaphrodite flowers on separate plants'},
    "ANDROECIOUS": {'description': 'Having only male flowers'},
    "ANDROGYNOMONOECIOUS": {'description': 'Having male, female, and hermaphrodite flowers on the same plant'},
    "ANDROGYNOUS": {'description': 'Having both male and female reproductive organs in the same flower'},
    "ANDROMONOECIOUS": {'description': 'Having male and hermaphrodite flowers on the same plant'},
    "BISEXUAL": {'description': 'Having both male and female reproductive organs'},
    "DICHOGAMOUS": {'description': 'Male and female organs mature at different times'},
    "DICLINOUS": {'description': 'Having male and female reproductive organs in separate flowers'},
    "DIOECIOUS": {'description': 'Having male and female flowers on separate plants'},
    "GYNODIOECIOUS": {'description': 'Having female and hermaphrodite flowers on separate plants'},
    "GYNOECIOUS": {'description': 'Having only female flowers'},
    "GYNOMONOECIOUS": {'description': 'Having female and hermaphrodite flowers on the same plant'},
    "HERMAPHRODITIC": {'description': 'Having both male and female reproductive organs', 'meaning': 'PATO:0001340'},
    "IMPERFECT": {'description': 'Flower lacking either male or female reproductive organs'},
    "MONOCLINOUS": {'description': 'Having both male and female reproductive organs in the same flower'},
    "MONOECIOUS": {'description': 'Having male and female flowers on the same plant'},
    "PERFECT": {'description': 'Flower having both male and female reproductive organs'},
    "POLYGAMODIOECIOUS": {'description': 'Having male, female, and hermaphrodite flowers on separate plants'},
    "POLYGAMOMONOECIOUS": {'description': 'Having male, female, and hermaphrodite flowers on the same plant'},
    "POLYGAMOUS": {'description': 'Having male, female, and hermaphrodite flowers'},
    "PROTANDROUS": {'description': 'Male organs mature before female organs'},
    "PROTOGYNOUS": {'description': 'Female organs mature before male organs'},
    "SUBANDROECIOUS": {'description': 'Mostly male flowers with occasional hermaphrodite flowers'},
    "SUBDIOECIOUS": {'description': 'Mostly dioecious with occasional hermaphrodite flowers'},
    "SUBGYNOECIOUS": {'description': 'Mostly female flowers with occasional hermaphrodite flowers'},
    "SYNOECIOUS": {'description': 'Having male and female organs fused together'},
    "TRIMONOECIOUS": {'description': 'Having male, female, and hermaphrodite flowers on the same plant'},
    "TRIOECIOUS": {'description': 'Having male, female, and hermaphrodite flowers on separate plants'},
    "UNISEXUAL": {'description': 'Having only one sex of reproductive organs'},
}

__all__ = [
    "PlantSexEnum",
]