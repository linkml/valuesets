"""
Radionuclide Value Sets

Radioactive elements and isotopes of environmental and health concern, commonly measured in environmental monitoring and exposure assessment.

Generated from: environmental_health/radionuclides.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class RadionuclideEnum(RichEnum):
    """
    Radioactive elements and isotopes commonly measured in environmental health studies, including naturally occurring radioactive materials (NORM) and anthropogenic radionuclides.
    """
    # Enum members
    RADON_222 = "RADON_222"
    URANIUM_238 = "URANIUM_238"
    URANIUM_235 = "URANIUM_235"
    THORIUM_232 = "THORIUM_232"
    RADIUM_226 = "RADIUM_226"
    RADIUM_228 = "RADIUM_228"
    POTASSIUM_40 = "POTASSIUM_40"
    CESIUM_137 = "CESIUM_137"
    STRONTIUM_90 = "STRONTIUM_90"
    IODINE_131 = "IODINE_131"
    PLUTONIUM_239 = "PLUTONIUM_239"
    AMERICIUM_241 = "AMERICIUM_241"
    TRITIUM = "TRITIUM"
    CARBON_14 = "CARBON_14"
    LEAD_210 = "LEAD_210"
    POLONIUM_210 = "POLONIUM_210"

# Set metadata after class creation
RadionuclideEnum._metadata = {
    "RADON_222": {'description': 'Radioactive noble gas produced by decay of radium-226. Major contributor to natural background radiation and indoor air quality concern.', 'meaning': 'CHEBI:33492', 'annotations': {'symbol': 'Rn-222', 'half_life': '3.82 days', 'decay_mode': 'alpha', 'parent': 'Ra-226', 'health_concern': 'lung cancer risk from inhalation'}},
    "URANIUM_238": {'description': 'Most abundant uranium isotope, primordial radionuclide. Parent of the uranium decay series.', 'annotations': {'symbol': 'U-238', 'half_life': '4.47 billion years', 'decay_mode': 'alpha', 'abundance': '99.3%'}},
    "URANIUM_235": {'description': 'Fissile uranium isotope used in nuclear reactors and weapons.', 'annotations': {'symbol': 'U-235', 'half_life': '704 million years', 'decay_mode': 'alpha', 'abundance': '0.7%'}},
    "THORIUM_232": {'description': 'Primordial radionuclide, parent of the thorium decay series. Found in soil, rocks, and building materials.', 'annotations': {'symbol': 'Th-232', 'half_life': '14 billion years', 'decay_mode': 'alpha'}},
    "RADIUM_226": {'description': 'Radioactive alkaline earth metal in the uranium decay series. Historically significant in medicine and industry.', 'meaning': 'CHEBI:80504', 'annotations': {'symbol': 'Ra-226', 'half_life': '1600 years', 'decay_mode': 'alpha', 'daughter': 'Rn-222'}},
    "RADIUM_228": {'description': 'Radioactive isotope in the thorium decay series.', 'meaning': 'CHEBI:80505', 'annotations': {'symbol': 'Ra-228', 'half_life': '5.75 years', 'decay_mode': 'beta'}},
    "POTASSIUM_40": {'description': 'Primordial radionuclide, naturally occurring in all potassium. Major contributor to internal dose from dietary intake.', 'annotations': {'symbol': 'K-40', 'half_life': '1.25 billion years', 'decay_mode': 'beta, electron capture', 'abundance': '0.012% of natural potassium'}},
    "CESIUM_137": {'description': 'Anthropogenic radionuclide from nuclear fission. Environmental contaminant from nuclear weapons testing and accidents.', 'meaning': 'CHEBI:196959', 'annotations': {'symbol': 'Cs-137', 'half_life': '30.17 years', 'decay_mode': 'beta', 'source': 'nuclear fission'}},
    "STRONTIUM_90": {'description': 'Anthropogenic radionuclide from nuclear fission. Bone-seeking due to chemical similarity to calcium.', 'meaning': 'NCIT:C29776', 'annotations': {'symbol': 'Sr-90', 'half_life': '28.8 years', 'decay_mode': 'beta', 'health_concern': 'bone cancer, leukemia'}},
    "IODINE_131": {'description': 'Radioactive iodine isotope from nuclear fission. Concentrates in thyroid gland. Used medically and released in nuclear accidents.', 'meaning': 'NCIT:C1639', 'annotations': {'symbol': 'I-131', 'half_life': '8.02 days', 'decay_mode': 'beta', 'health_concern': 'thyroid cancer'}},
    "PLUTONIUM_239": {'description': 'Transuranic element produced in nuclear reactors. Highly toxic alpha emitter with very long half-life.', 'meaning': 'NCIT:C29774', 'annotations': {'symbol': 'Pu-239', 'half_life': '24100 years', 'decay_mode': 'alpha', 'source': 'nuclear reactors'}},
    "AMERICIUM_241": {'description': 'Transuranic element, alpha emitter. Used in smoke detectors.', 'annotations': {'symbol': 'Am-241', 'half_life': '432 years', 'decay_mode': 'alpha', 'use': 'smoke detectors'}},
    "TRITIUM": {'description': 'Radioactive hydrogen isotope. Produced naturally and in nuclear reactors. Weak beta emitter.', 'meaning': 'CHEBI:29238', 'annotations': {'symbol': 'H-3', 'half_life': '12.3 years', 'decay_mode': 'beta (weak)'}},
    "CARBON_14": {'description': 'Cosmogenic radionuclide used in radiocarbon dating. Produced by cosmic ray interactions in atmosphere.', 'meaning': 'CHEBI:36927', 'annotations': {'symbol': 'C-14', 'half_life': '5730 years', 'decay_mode': 'beta', 'use': 'radiocarbon dating'}},
    "LEAD_210": {'description': 'Radioactive lead isotope in uranium decay series. Used as environmental tracer for sedimentation dating.', 'annotations': {'symbol': 'Pb-210', 'half_life': '22.3 years', 'decay_mode': 'beta', 'use': 'sediment dating'}},
    "POLONIUM_210": {'description': 'Highly radioactive alpha emitter in uranium decay series. Found in tobacco smoke.', 'meaning': 'CHEBI:37340', 'annotations': {'symbol': 'Po-210', 'half_life': '138 days', 'decay_mode': 'alpha', 'health_concern': 'lung cancer from tobacco'}},
}

class NORMEnum(RichEnum):
    """
    Naturally occurring radioactive materials (NORM) found in the environment. These are primordial radionuclides and their decay products.
    """
    # Enum members
    URANIUM_SERIES = "URANIUM_SERIES"
    THORIUM_SERIES = "THORIUM_SERIES"
    ACTINIUM_SERIES = "ACTINIUM_SERIES"
    POTASSIUM_40_PRIMORDIAL = "POTASSIUM_40_PRIMORDIAL"

# Set metadata after class creation
NORMEnum._metadata = {
    "URANIUM_SERIES": {'description': 'The uranium decay series starting from U-238 and ending with stable Pb-206. Includes Ra-226, Rn-222, Po-210, and other isotopes.', 'annotations': {'parent': 'U-238', 'end_product': 'Pb-206', 'key_members': 'Ra-226, Rn-222, Po-210, Pb-210'}},
    "THORIUM_SERIES": {'description': 'The thorium decay series starting from Th-232 and ending with stable Pb-208. Includes Ra-228, Rn-220 (thoron), and other isotopes.', 'annotations': {'parent': 'Th-232', 'end_product': 'Pb-208', 'key_members': 'Ra-228, Rn-220, Pb-212'}},
    "ACTINIUM_SERIES": {'description': 'The actinium decay series starting from U-235 and ending with stable Pb-207.', 'annotations': {'parent': 'U-235', 'end_product': 'Pb-207'}},
    "POTASSIUM_40_PRIMORDIAL": {'description': 'Primordial radionuclide present in all potassium-bearing minerals and biological tissues.', 'annotations': {'type': 'primordial', 'ubiquity': 'present in all potassium'}},
}

__all__ = [
    "RadionuclideEnum",
    "NORMEnum",
]