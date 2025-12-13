"""
Lipid Categories

Major lipid categories from SwissLipids classification

Generated from: bio/lipid_categories.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class RelativeTimeEnum(RichEnum):
    """
    Temporal relationships between events or time points
    """
    # Enum members
    BEFORE = "BEFORE"
    AFTER = "AFTER"
    AT_SAME_TIME_AS = "AT_SAME_TIME_AS"

# Set metadata after class creation
RelativeTimeEnum._metadata = {
    "BEFORE": {'description': 'Occurs before the reference time point'},
    "AFTER": {'description': 'Occurs after the reference time point'},
    "AT_SAME_TIME_AS": {'description': 'Occurs at the same time as the reference time point'},
}

class PresenceEnum(RichEnum):
    """
    Classification of whether an entity is present, absent, or at detection limits
    """
    # Enum members
    PRESENT = "PRESENT"
    ABSENT = "ABSENT"
    BELOW_DETECTION_LIMIT = "BELOW_DETECTION_LIMIT"
    ABOVE_DETECTION_LIMIT = "ABOVE_DETECTION_LIMIT"

# Set metadata after class creation
PresenceEnum._metadata = {
    "PRESENT": {'description': 'The entity is present'},
    "ABSENT": {'description': 'The entity is absent'},
    "BELOW_DETECTION_LIMIT": {'description': 'The entity is below the detection limit'},
    "ABOVE_DETECTION_LIMIT": {'description': 'The entity is above the detection limit'},
}

class LipidCategory(RichEnum):
    """
    Major categories of lipids based on SwissLipids classification
    """
    # Enum members
    LIPID = "LIPID"
    FATTY_ACYLS_AND_DERIVATIVES = "FATTY_ACYLS_AND_DERIVATIVES"
    GLYCEROLIPIDS = "GLYCEROLIPIDS"
    GLYCEROPHOSPHOLIPIDS = "GLYCEROPHOSPHOLIPIDS"
    SPHINGOLIPIDS = "SPHINGOLIPIDS"
    STEROIDS_AND_DERIVATIVES = "STEROIDS_AND_DERIVATIVES"
    PRENOL_LIPIDS = "PRENOL_LIPIDS"

# Set metadata after class creation
LipidCategory._metadata = {
    "LIPID": {'description': 'Lipid', 'meaning': 'CHEBI:18059'},
    "FATTY_ACYLS_AND_DERIVATIVES": {'description': 'Fatty acyls and derivatives', 'meaning': 'CHEBI:24027', 'aliases': ['fatty-acyl group']},
    "GLYCEROLIPIDS": {'description': 'Glycerolipids', 'meaning': 'CHEBI:35741', 'aliases': ['glycerolipid']},
    "GLYCEROPHOSPHOLIPIDS": {'description': 'Glycerophospholipids', 'meaning': 'CHEBI:37739', 'aliases': ['glycerophospholipid']},
    "SPHINGOLIPIDS": {'description': 'Sphingolipids', 'meaning': 'CHEBI:26739', 'aliases': ['sphingolipid']},
    "STEROIDS_AND_DERIVATIVES": {'description': 'Steroids and derivatives', 'meaning': 'CHEBI:35341', 'aliases': ['steroid']},
    "PRENOL_LIPIDS": {'description': 'Prenol Lipids', 'meaning': 'CHEBI:24913', 'aliases': ['isoprenoid']},
}

__all__ = [
    "RelativeTimeEnum",
    "PresenceEnum",
    "LipidCategory",
]