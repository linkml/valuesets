"""
Enzymology Assay Value Sets

Value sets for enzymology assays including enzyme activity, kinetics, inhibition, and substrate specificity measurements.

Generated from: bio/assays/enzymology.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class EnzymologyAssayEnum(RichEnum):
    """
    Assays for characterizing enzyme function including activity, kinetics, inhibition, and substrate specificity.
    """
    # Enum members
    ENZYME_ACTIVITY_ASSAY = "ENZYME_ACTIVITY_ASSAY"
    MICHAELIS_MENTEN_KINETICS = "MICHAELIS_MENTEN_KINETICS"
    INHIBITION_ASSAY = "INHIBITION_ASSAY"
    SUBSTRATE_SPECIFICITY = "SUBSTRATE_SPECIFICITY"
    FLUOROMETRIC_ENZYME_ASSAY = "FLUOROMETRIC_ENZYME_ASSAY"
    COLORIMETRIC_ENZYME_ASSAY = "COLORIMETRIC_ENZYME_ASSAY"
    COUPLED_ENZYME_ASSAY = "COUPLED_ENZYME_ASSAY"
    CONTINUOUS_ENZYME_ASSAY = "CONTINUOUS_ENZYME_ASSAY"
    ENDPOINT_ENZYME_ASSAY = "ENDPOINT_ENZYME_ASSAY"

# Set metadata after class creation
EnzymologyAssayEnum._metadata = {
    "ENZYME_ACTIVITY_ASSAY": {'description': 'Measures the effect of a perturbagen on enzyme activity', 'meaning': 'BAO:0002994', 'annotations': {'companion_enum_substrate': 'ChemicalEntity', 'companion_enum_enzyme': 'Protein', 'companion_enum_readout': 'DetectionModeEnum'}},
    "MICHAELIS_MENTEN_KINETICS": {'description': 'Enzyme kinetics assay measuring Km and Vmax parameters', 'annotations': {'companion_enum_substrate': 'ChemicalEntity', 'companion_enum_enzyme': 'Protein'}},
    "INHIBITION_ASSAY": {'description': 'Assay to measure enzyme inhibition (IC50, Ki)', 'annotations': {'companion_enum_substrate': 'ChemicalEntity', 'companion_enum_enzyme': 'Protein'}},
    "SUBSTRATE_SPECIFICITY": {'description': 'Assay to determine enzyme substrate preference and specificity', 'annotations': {'companion_enum_substrate': 'ChemicalEntity', 'companion_enum_enzyme': 'Protein'}},
    "FLUOROMETRIC_ENZYME_ASSAY": {'description': 'Enzyme assay using fluorescent substrates or products for detection', 'annotations': {'companion_enum_substrate': 'ChemicalEntity', 'companion_enum_enzyme': 'Protein', 'companion_enum_readout': 'DetectionModeEnum'}},
    "COLORIMETRIC_ENZYME_ASSAY": {'description': 'Enzyme assay using chromogenic substrates for absorbance-based detection', 'annotations': {'companion_enum_substrate': 'ChemicalEntity', 'companion_enum_enzyme': 'Protein', 'companion_enum_readout': 'DetectionModeEnum'}},
    "COUPLED_ENZYME_ASSAY": {'description': 'Enzyme assay using a secondary enzyme reaction for signal generation', 'annotations': {'companion_enum_substrate': 'ChemicalEntity', 'companion_enum_enzyme': 'Protein'}},
    "CONTINUOUS_ENZYME_ASSAY": {'description': 'Real-time monitoring of enzyme reaction progress', 'annotations': {'companion_enum_substrate': 'ChemicalEntity', 'companion_enum_enzyme': 'Protein'}},
    "ENDPOINT_ENZYME_ASSAY": {'description': 'Single time-point measurement of enzyme reaction product', 'annotations': {'companion_enum_substrate': 'ChemicalEntity', 'companion_enum_enzyme': 'Protein'}},
}

__all__ = [
    "EnzymologyAssayEnum",
]