"""

Generated from: bio/trophic_levels.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class TrophicLevelEnum(RichEnum):
    """
    Trophic levels are the feeding position in a food chain
    """
    # Enum members
    AUTOTROPH = "AUTOTROPH"
    CARBOXYDOTROPH = "CARBOXYDOTROPH"
    CHEMOAUTOLITHOTROPH = "CHEMOAUTOLITHOTROPH"
    CHEMOAUTOTROPH = "CHEMOAUTOTROPH"
    CHEMOHETEROTROPH = "CHEMOHETEROTROPH"
    CHEMOLITHOAUTOTROPH = "CHEMOLITHOAUTOTROPH"
    CHEMOLITHOTROPH = "CHEMOLITHOTROPH"
    CHEMOORGANOHETEROTROPH = "CHEMOORGANOHETEROTROPH"
    CHEMOORGANOTROPH = "CHEMOORGANOTROPH"
    CHEMOSYNTHETIC = "CHEMOSYNTHETIC"
    CHEMOTROPH = "CHEMOTROPH"
    COPIOTROPH = "COPIOTROPH"
    DIAZOTROPH = "DIAZOTROPH"
    FACULTATIVE = "FACULTATIVE"
    HETEROTROPH = "HETEROTROPH"
    LITHOAUTOTROPH = "LITHOAUTOTROPH"
    LITHOHETEROTROPH = "LITHOHETEROTROPH"
    LITHOTROPH = "LITHOTROPH"
    METHANOTROPH = "METHANOTROPH"
    METHYLOTROPH = "METHYLOTROPH"
    MIXOTROPH = "MIXOTROPH"
    OBLIGATE = "OBLIGATE"
    OLIGOTROPH = "OLIGOTROPH"
    ORGANOHETEROTROPH = "ORGANOHETEROTROPH"
    ORGANOTROPH = "ORGANOTROPH"
    PHOTOAUTOTROPH = "PHOTOAUTOTROPH"
    PHOTOHETEROTROPH = "PHOTOHETEROTROPH"
    PHOTOLITHOAUTOTROPH = "PHOTOLITHOAUTOTROPH"
    PHOTOLITHOTROPH = "PHOTOLITHOTROPH"
    PHOTOSYNTHETIC = "PHOTOSYNTHETIC"
    PHOTOTROPH = "PHOTOTROPH"

# Set metadata after class creation
TrophicLevelEnum._metadata = {
    "AUTOTROPH": {'description': 'Organism capable of synthesizing its own food from inorganic substances', 'meaning': 'ECOCORE:00000023'},
    "CARBOXYDOTROPH": {'description': 'Organism that uses carbon monoxide as a source of carbon and energy'},
    "CHEMOAUTOLITHOTROPH": {'description': 'Autotroph that obtains energy from inorganic compounds'},
    "CHEMOAUTOTROPH": {'description': 'Organism that obtains energy by oxidizing inorganic compounds', 'meaning': 'ECOCORE:00000129'},
    "CHEMOHETEROTROPH": {'description': 'Organism that obtains energy from organic compounds', 'meaning': 'ECOCORE:00000132'},
    "CHEMOLITHOAUTOTROPH": {'description': 'Organism that uses inorganic compounds as electron donors'},
    "CHEMOLITHOTROPH": {'description': 'Organism that obtains energy from oxidation of inorganic compounds'},
    "CHEMOORGANOHETEROTROPH": {'description': 'Organism that uses organic compounds as both carbon and energy source'},
    "CHEMOORGANOTROPH": {'description': 'Organism that obtains energy from organic compounds', 'meaning': 'ECOCORE:00000133'},
    "CHEMOSYNTHETIC": {'description': 'Relating to organisms that produce organic matter through chemosynthesis'},
    "CHEMOTROPH": {'description': 'Organism that obtains energy from chemical compounds'},
    "COPIOTROPH": {'description': 'Organism that thrives in nutrient-rich environments'},
    "DIAZOTROPH": {'description': 'Organism capable of fixing atmospheric nitrogen'},
    "FACULTATIVE": {'description': 'Organism that can switch between different metabolic modes'},
    "HETEROTROPH": {'description': 'Organism that obtains carbon from organic compounds', 'meaning': 'ECOCORE:00000010'},
    "LITHOAUTOTROPH": {'description': 'Autotroph that uses inorganic compounds as electron donors'},
    "LITHOHETEROTROPH": {'description': 'Heterotroph that uses inorganic compounds as electron donors'},
    "LITHOTROPH": {'description': 'Organism that uses inorganic substrates as electron donors'},
    "METHANOTROPH": {'description': 'Organism that uses methane as carbon and energy source'},
    "METHYLOTROPH": {'description': 'Organism that uses single-carbon compounds'},
    "MIXOTROPH": {'description': 'Organism that can use both autotrophic and heterotrophic methods'},
    "OBLIGATE": {'description': 'Organism restricted to a particular metabolic mode'},
    "OLIGOTROPH": {'description': 'Organism that thrives in nutrient-poor environments', 'meaning': 'ECOCORE:00000138'},
    "ORGANOHETEROTROPH": {'description': 'Organism that uses organic compounds as carbon source'},
    "ORGANOTROPH": {'description': 'Organism that uses organic compounds as electron donors'},
    "PHOTOAUTOTROPH": {'description': 'Organism that uses light energy to synthesize organic compounds', 'meaning': 'ECOCORE:00000130'},
    "PHOTOHETEROTROPH": {'description': 'Organism that uses light for energy but organic compounds for carbon', 'meaning': 'ECOCORE:00000131'},
    "PHOTOLITHOAUTOTROPH": {'description': 'Photoautotroph that uses inorganic electron donors'},
    "PHOTOLITHOTROPH": {'description': 'Organism that uses light energy and inorganic electron donors'},
    "PHOTOSYNTHETIC": {'description': 'Relating to organisms that produce organic matter through photosynthesis'},
    "PHOTOTROPH": {'description': 'Organism that obtains energy from light'},
}

__all__ = [
    "TrophicLevelEnum",
]