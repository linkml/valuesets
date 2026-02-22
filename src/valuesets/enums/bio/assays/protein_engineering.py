"""
Protein Engineering Assay Value Sets

Value sets for protein engineering and characterization assays including binding kinetics, biophysical characterization, and display technologies.

Generated from: bio/assays/protein_engineering.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class ProteinEngineeringAssayEnum(RichEnum):
    """
    Assays for protein engineering including binding kinetics, biophysical characterization, and display-based selection methods.
    """
    # Enum members
    SURFACE_PLASMON_RESONANCE = "SURFACE_PLASMON_RESONANCE"
    BIOLAYER_INTERFEROMETRY = "BIOLAYER_INTERFEROMETRY"
    THERMAL_SHIFT_ASSAY = "THERMAL_SHIFT_ASSAY"
    CIRCULAR_DICHROISM = "CIRCULAR_DICHROISM"
    PHAGE_DISPLAY = "PHAGE_DISPLAY"
    YEAST_DISPLAY = "YEAST_DISPLAY"
    DIRECTED_EVOLUTION_SCREEN = "DIRECTED_EVOLUTION_SCREEN"

# Set metadata after class creation
ProteinEngineeringAssayEnum._metadata = {
    "SURFACE_PLASMON_RESONANCE": {'description': 'Real-time label-free measurement of biomolecular binding kinetics', 'meaning': 'BAO:0000054', 'annotations': {'companion_enum_target_protein': 'Protein', 'companion_enum_readout': 'DetectionModeEnum'}, 'aliases': ['SPR']},
    "BIOLAYER_INTERFEROMETRY": {'description': 'Label-free measurement of biomolecular interactions via interference patterns', 'meaning': 'BAO:0000066', 'annotations': {'companion_enum_target_protein': 'Protein', 'companion_enum_readout': 'DetectionModeEnum'}, 'aliases': ['BLI', 'bio layer interferometry']},
    "THERMAL_SHIFT_ASSAY": {'description': 'Measurement of protein thermal stability via fluorescent dye binding', 'meaning': 'BAO:0010261', 'annotations': {'companion_enum_target_protein': 'Protein', 'companion_enum_readout': 'DetectionModeEnum'}, 'aliases': ['differential scanning fluorimetry', 'DSF']},
    "CIRCULAR_DICHROISM": {'description': 'Assessment of protein secondary and tertiary structure using polarized light', 'meaning': 'BAO:0000161', 'annotations': {'companion_enum_target_protein': 'Protein', 'companion_enum_readout': 'DetectionModeEnum'}, 'aliases': ['CD']},
    "PHAGE_DISPLAY": {'description': 'Selection of peptides or proteins displayed on bacteriophage surface', 'annotations': {'companion_enum_target_protein': 'Protein'}},
    "YEAST_DISPLAY": {'description': 'Selection of proteins displayed on yeast cell surface', 'annotations': {'companion_enum_target_protein': 'Protein'}},
    "DIRECTED_EVOLUTION_SCREEN": {'description': 'High-throughput screening of mutant protein libraries for improved function', 'annotations': {'companion_enum_target_protein': 'Protein', 'companion_enum_readout': 'DetectionModeEnum'}},
}

__all__ = [
    "ProteinEngineeringAssayEnum",
]