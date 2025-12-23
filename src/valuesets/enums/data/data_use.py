"""
Data Use Conditions Value Sets

Value sets for data use permissions and conditions based on the GA4GH Data Use Ontology (DUO).

Generated from: data/data_use.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class DataUsePermissionEnum(RichEnum):
    """
    Primary data use permissions from the GA4GH Data Use Ontology (DUO) indicating what research purposes data can be used for.
    """
    # Enum members
    GRU = "GRU"
    HMB = "HMB"
    DS = "DS"
    NO_RESTRICTION = "NO_RESTRICTION"

# Set metadata after class creation
DataUsePermissionEnum._metadata = {
    "GRU": {'description': 'General research use - allowed for any research purpose including health/medical/biomedical, fundamental biology, population origins, statistical methods development, and social-sciences research.', 'meaning': 'DUO:0000042', 'aliases': ['general research use']},
    "HMB": {'description': 'Health/medical/biomedical research only - does not include study of population origins or ancestry.', 'meaning': 'DUO:0000006', 'aliases': ['health or medical or biomedical research']},
    "DS": {'description': 'Disease-specific research - use allowed only for research related to specified disease(s). Should be coupled with disease ontology term.', 'meaning': 'DUO:0000007', 'aliases': ['disease specific research']},
    "NO_RESTRICTION": {'description': 'No restriction on use of the data.', 'meaning': 'DUO:0000004', 'aliases': ['no restriction']},
}

class DataUseModifierEnum(RichEnum):
    """
    Additional conditions and modifiers for data use from the GA4GH Data Use Ontology (DUO).
    """
    # Enum members
    NPUNCU = "NPUNCU"
    NPO = "NPO"
    NCU = "NCU"
    IRB = "IRB"
    NRES = "NRES"
    NMDS = "NMDS"
    RS = "RS"

# Set metadata after class creation
DataUseModifierEnum._metadata = {
    "NPUNCU": {'description': 'Not-for-profit use only - use limited to not-for-profit organizations and non-commercial use.', 'meaning': 'DUO:0000018', 'aliases': ['not for profit, non commercial use only']},
    "NPO": {'description': 'Use limited to not-for-profit organizations only.', 'meaning': 'DUO:0000045', 'aliases': ['not for profit organisation use only']},
    "NCU": {'description': 'Non-commercial use only - data can be used by commercial organizations for research but not commercial purposes.', 'meaning': 'DUO:0000046', 'aliases': ['non-commercial use only']},
    "IRB": {'description': 'Ethics approval required - requestor must provide documentation of local IRB/ERB approval.', 'meaning': 'DUO:0000021', 'aliases': ['ethics approval required']},
    "NRES": {'description': 'No restriction on data use.', 'meaning': 'DUO:0000004', 'aliases': ['no restriction']},
    "NMDS": {'description': 'No general methods research - does not allow methods development.', 'meaning': 'DUO:0000015', 'aliases': ['no general methods research']},
    "RS": {'description': 'Research-specific restrictions apply.', 'meaning': 'DUO:0000012', 'aliases': ['research specific restrictions']},
}

__all__ = [
    "DataUsePermissionEnum",
    "DataUseModifierEnum",
]