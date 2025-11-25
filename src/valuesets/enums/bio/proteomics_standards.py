"""
Proteomics Standards

Controlled vocabularies for mass spectrometry and proteomics data annotation from HUPO-PSI standards

Generated from: bio/proteomics_standards.yaml
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

class PeakAnnotationSeriesLabel(RichEnum):
    """
    Types of peak annotations in mass spectrometry data
    """
    # Enum members
    PEPTIDE = "PEPTIDE"
    INTERNAL = "INTERNAL"
    PRECURSOR = "PRECURSOR"
    IMMONIUM = "IMMONIUM"
    REFERENCE = "REFERENCE"
    NAMED_COMPOUND = "NAMED_COMPOUND"
    FORMULA = "FORMULA"
    SMILES = "SMILES"
    UNANNOTATED = "UNANNOTATED"

# Set metadata after class creation
PeakAnnotationSeriesLabel._metadata = {
    "PEPTIDE": {'description': 'Peptide fragment ion'},
    "INTERNAL": {'description': 'Internal fragment ion'},
    "PRECURSOR": {'description': 'Precursor ion'},
    "IMMONIUM": {'description': 'Immonium ion'},
    "REFERENCE": {'description': 'Reference peak or calibrant'},
    "NAMED_COMPOUND": {'description': 'Named chemical compound'},
    "FORMULA": {'description': 'Chemical formula'},
    "SMILES": {'description': 'SMILES structure notation'},
    "UNANNOTATED": {'description': 'Unannotated peak'},
}

class PeptideIonSeries(RichEnum):
    """
    Types of peptide fragment ion series in mass spectrometry
    """
    # Enum members
    B = "B"
    Y = "Y"
    A = "A"
    X = "X"
    C = "C"
    Z = "Z"
    D = "D"
    V = "V"
    W = "W"
    DA = "DA"
    DB = "DB"
    WA = "WA"
    WB = "WB"

# Set metadata after class creation
PeptideIonSeries._metadata = {
    "B": {'description': 'B ion series - N-terminal fragment with CO'},
    "Y": {'description': 'Y ion series - C-terminal fragment with H'},
    "A": {'description': 'A ion series - N-terminal fragment minus CO'},
    "X": {'description': 'X ion series - C-terminal fragment plus CO'},
    "C": {'description': 'C ion series - N-terminal fragment with NH3'},
    "Z": {'description': 'Z ion series - C-terminal fragment minus NH'},
    "D": {'description': 'D ion series - partial side chain cleavage'},
    "V": {'description': 'V ion series - side chain loss from y ion'},
    "W": {'description': 'W ion series - side chain loss from z ion'},
    "DA": {'description': 'DA ion series - a ion with side chain loss'},
    "DB": {'description': 'DB ion series - b ion with side chain loss'},
    "WA": {'description': 'WA ion series - a ion with tryptophan side chain loss'},
    "WB": {'description': 'WB ion series - b ion with tryptophan side chain loss'},
}

class MassErrorUnit(RichEnum):
    """
    Units for expressing mass error in mass spectrometry
    """
    # Enum members
    PPM = "PPM"
    DA = "DA"

# Set metadata after class creation
MassErrorUnit._metadata = {
    "PPM": {'description': 'Parts per million - relative mass error'},
    "DA": {'description': 'Dalton - absolute mass error', 'aliases': ['Dalton', 'u', 'amu']},
}

__all__ = [
    "RelativeTimeEnum",
    "PresenceEnum",
    "PeakAnnotationSeriesLabel",
    "PeptideIonSeries",
    "MassErrorUnit",
]