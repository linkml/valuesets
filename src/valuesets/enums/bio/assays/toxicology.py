"""
Toxicology Assay Value Sets

Value sets for toxicological assays including cytotoxicity, genotoxicity, mutagenicity, and dose-response measurements.

Generated from: bio/assays/toxicology.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class ToxicologyAssayEnum(RichEnum):
    """
    Assays for evaluating toxicity, genotoxicity, and safety of compounds including cytotoxicity, mutagenicity, and ADME measurements.
    """
    # Enum members
    TOXICITY_ASSAY = "TOXICITY_ASSAY"
    MTT_ASSAY = "MTT_ASSAY"
    LDH_RELEASE_ASSAY = "LDH_RELEASE_ASSAY"
    AMES_TEST = "AMES_TEST"
    COMET_ASSAY = "COMET_ASSAY"
    MICRONUCLEUS_ASSAY = "MICRONUCLEUS_ASSAY"
    DOSE_RESPONSE = "DOSE_RESPONSE"
    ADME_ASSAY = "ADME_ASSAY"

# Set metadata after class creation
ToxicologyAssayEnum._metadata = {
    "TOXICITY_ASSAY": {'description': 'General assay measuring degree of substance toxicity to living cells', 'meaning': 'BAO:0002189', 'annotations': {'companion_enum_compound': 'ChemicalEntity', 'companion_enum_cell_line': 'CellType'}},
    "MTT_ASSAY": {'description': 'Colorimetric assay measuring cell metabolic activity via MTT reduction', 'meaning': 'BAO:0002457', 'annotations': {'companion_enum_compound': 'ChemicalEntity', 'companion_enum_cell_line': 'CellType'}, 'aliases': ['MTT reduction assay']},
    "LDH_RELEASE_ASSAY": {'description': 'Cytotoxicity assay measuring lactate dehydrogenase release from damaged cells', 'meaning': 'BAO:0013056', 'annotations': {'companion_enum_compound': 'ChemicalEntity', 'companion_enum_cell_line': 'CellType'}},
    "AMES_TEST": {'description': 'Mutagenicity assay using bacterial reverse mutation in Salmonella strains', 'meaning': 'BAO:0013054', 'annotations': {'companion_enum_compound': 'ChemicalEntity'}},
    "COMET_ASSAY": {'description': 'Single cell gel electrophoresis assay measuring DNA strand breaks', 'meaning': 'OBI:0302736', 'annotations': {'companion_enum_compound': 'ChemicalEntity', 'companion_enum_cell_line': 'CellType'}},
    "MICRONUCLEUS_ASSAY": {'description': 'Genotoxicity assay detecting chromosomal damage via micronucleus formation', 'meaning': 'BAO:0013055', 'annotations': {'companion_enum_compound': 'ChemicalEntity', 'companion_enum_cell_line': 'CellType'}},
    "DOSE_RESPONSE": {'description': 'Measurement of biological response as a function of compound concentration', 'annotations': {'companion_enum_compound': 'ChemicalEntity', 'companion_enum_cell_line': 'CellType'}},
    "ADME_ASSAY": {'description': 'Absorption, distribution, metabolism, and excretion profiling', 'annotations': {'companion_enum_compound': 'ChemicalEntity'}},
}

__all__ = [
    "ToxicologyAssayEnum",
]