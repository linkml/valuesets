"""
Immunology Assay Value Sets

Value sets for immunological assays including ELISA, immunoprecipitation, flow cytometry, western blot, and related methods.

Generated from: bio/assays/immunology.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class ImmunologyAssayEnum(RichEnum):
    """
    Assays for detecting and quantifying immune-related molecules including antibody-based detection, cell sorting, and blotting methods.
    """
    # Enum members
    ELISA = "ELISA"
    SANDWICH_ELISA = "SANDWICH_ELISA"
    IMMUNOPRECIPITATION = "IMMUNOPRECIPITATION"
    FLOW_CYTOMETRY = "FLOW_CYTOMETRY"
    WESTERN_BLOT = "WESTERN_BLOT"
    CYTOKINE_SECRETION_ASSAY = "CYTOKINE_SECRETION_ASSAY"
    IMMUNOBLOT = "IMMUNOBLOT"
    COMPLEMENT_FIXATION = "COMPLEMENT_FIXATION"
    MULTIPLEX_BEAD_ASSAY = "MULTIPLEX_BEAD_ASSAY"

# Set metadata after class creation
ImmunologyAssayEnum._metadata = {
    "ELISA": {'description': 'Enzyme-linked immunosorbent assay for detecting antigens or antibodies', 'meaning': 'BAO:0000134', 'annotations': {'companion_enum_antibody_target': 'Protein', 'companion_enum_detection_method': 'DetectionModeEnum'}},
    "SANDWICH_ELISA": {'description': 'Sandwich ELISA using capture and detection antibodies', 'annotations': {'companion_enum_antibody_target': 'Protein', 'companion_enum_detection_method': 'DetectionModeEnum'}},
    "IMMUNOPRECIPITATION": {'description': 'Precipitation of a protein antigen from solution using a specific antibody', 'meaning': 'BAO:0002508', 'annotations': {'companion_enum_antibody_target': 'Protein', 'companion_enum_detection_method': 'DetectionModeEnum'}},
    "FLOW_CYTOMETRY": {'description': 'Analysis of cell populations using fluorescent antibodies and light scattering', 'meaning': 'BAO:0000005', 'annotations': {'companion_enum_antibody_target': 'Protein', 'companion_enum_detection_method': 'DetectionModeEnum'}},
    "WESTERN_BLOT": {'description': 'Protein detection by gel electrophoresis, membrane transfer, and antibody staining', 'meaning': 'OBI:0000854', 'annotations': {'companion_enum_antibody_target': 'Protein', 'companion_enum_detection_method': 'DetectionModeEnum'}, 'aliases': ['western blot assay']},
    "CYTOKINE_SECRETION_ASSAY": {'description': 'Measurement of cytokine types and amounts released from cells', 'meaning': 'BAO:0003003', 'annotations': {'companion_enum_antibody_target': 'Protein', 'companion_enum_detection_method': 'DetectionModeEnum'}},
    "IMMUNOBLOT": {'description': 'Detection of proteins using antibodies on a membrane', 'meaning': 'BAO:0002422', 'annotations': {'companion_enum_antibody_target': 'Protein', 'companion_enum_detection_method': 'DetectionModeEnum'}},
    "COMPLEMENT_FIXATION": {'description': 'Serological assay detecting antibodies by complement consumption', 'annotations': {'companion_enum_antibody_target': 'Protein'}},
    "MULTIPLEX_BEAD_ASSAY": {'description': 'Simultaneous detection of multiple analytes using antibody-conjugated beads', 'annotations': {'companion_enum_antibody_target': 'Protein', 'companion_enum_detection_method': 'DetectionModeEnum'}},
}

__all__ = [
    "ImmunologyAssayEnum",
]