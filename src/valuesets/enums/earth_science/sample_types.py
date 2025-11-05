"""
Earth Science Sample Types

Sample object types for earth samples, based on SESAR (System for Earth Sample Registration) vocabulary

Generated from: earth_science/sample_types.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class SESARSampleType(RichEnum):
    """
    Sample object types as defined by SESAR (System for Earth Sample Registration). These describe the physical form and collection context of samples.
    """
    # Enum members
    CORE = "CORE"
    CORE_CATCHER = "CORE_CATCHER"
    CORE_HALF_ROUND = "CORE_HALF_ROUND"
    CORE_PIECE = "CORE_PIECE"
    CORE_QUARTER_ROUND = "CORE_QUARTER_ROUND"
    CORE_SECTION = "CORE_SECTION"
    CORE_SECTION_HALF = "CORE_SECTION_HALF"
    CORE_SLAB = "CORE_SLAB"
    CORE_SUB_PIECE = "CORE_SUB_PIECE"
    CORE_U_CHANNEL = "CORE_U_CHANNEL"
    CORE_WHOLE_ROUND = "CORE_WHOLE_ROUND"
    CTD = "CTD"
    CUTTINGS = "CUTTINGS"
    DREDGE = "DREDGE"
    EXPERIMENTAL_SPECIMEN = "EXPERIMENTAL_SPECIMEN"
    GRAB = "GRAB"
    HOLE = "HOLE"
    INDIVIDUAL_SAMPLE = "INDIVIDUAL_SAMPLE"
    ORIENTED_CORE = "ORIENTED_CORE"
    OTHER = "OTHER"
    ROCK_POWDER = "ROCK_POWDER"
    SITE = "SITE"
    TERRESTRIAL_SECTION = "TERRESTRIAL_SECTION"

# Set metadata after class creation
SESARSampleType._metadata = {
    "CORE": {'description': 'Long cylindrical cores', 'annotations': {'sesar_definition': 'long cylindrical cores'}},
    "CORE_CATCHER": {'description': 'Material from core catcher treated as separate section'},
    "CORE_HALF_ROUND": {'description': 'Half-cylindrical products of along-axis split of a whole round'},
    "CORE_PIECE": {'description': 'Material occurring between unambiguous breaks in recovery'},
    "CORE_QUARTER_ROUND": {'description': 'Quarter-cylindrical products of along-axis split of a half round'},
    "CORE_SECTION": {'description': 'Arbitrarily cut segments of a core'},
    "CORE_SECTION_HALF": {'description': 'Half-cylindrical products from section splits'},
    "CORE_SLAB": {'description': 'Rectangular prism of material taken from a core with one dimension shorter'},
    "CORE_SUB_PIECE": {'description': 'Mated portion of larger piece for curatorial management'},
    "CORE_U_CHANNEL": {'description': 'Long rectangular prism of material for continuous measurement'},
    "CORE_WHOLE_ROUND": {'description': 'Cylindrical segments of core or core section material'},
    "CTD": {'description': 'A CTD (Conductivity, Temperature, and Depth) cast sample', 'annotations': {'full_name': 'Conductivity Temperature Depth'}},
    "CUTTINGS": {'description': 'Loose, coarse, unconsolidated material suspended in drilling fluid'},
    "DREDGE": {'description': 'A group of rocks collected by dragging a dredge along the seafloor'},
    "EXPERIMENTAL_SPECIMEN": {'description': 'A synthetic material used during an experiment'},
    "GRAB": {'description': 'Mechanically collected sample not necessarily representative'},
    "HOLE": {'description': 'Hole cavity and walls surrounding that cavity'},
    "INDIVIDUAL_SAMPLE": {'description': 'Single unit including rock samples or biological specimens'},
    "ORIENTED_CORE": {'description': 'Core positioned identically to subsurface arrangement'},
    "OTHER": {'description': 'Sample not fitting existing designations'},
    "ROCK_POWDER": {'description': 'A sample created from pulverizing a rock to powder'},
    "SITE": {'description': 'A place where a sample is collected'},
    "TERRESTRIAL_SECTION": {'description': 'A sample of a section of the near-surface Earth, generally in the critical zone'},
}

__all__ = [
    "SESARSampleType",
]