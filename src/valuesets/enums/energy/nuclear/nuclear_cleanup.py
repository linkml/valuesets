"""
Nuclear Cleanup and Restoration Value Sets

Value sets for nuclear site cleanup, remediation, and environmental restoration relevant to the DOE Transforming Nuclear Cleanup challenge

Generated from: energy/nuclear/nuclear_cleanup.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class NuclearRemediationType(RichEnum):
    """
    Methods for remediating radioactive contamination at nuclear sites
    """
    # Enum members
    SOIL_EXCAVATION = "SOIL_EXCAVATION"
    GROUNDWATER_PUMP_AND_TREAT = "GROUNDWATER_PUMP_AND_TREAT"
    IN_SITU_BIOREMEDIATION = "IN_SITU_BIOREMEDIATION"
    VITRIFICATION = "VITRIFICATION"
    STABILIZATION = "STABILIZATION"
    CAPPING = "CAPPING"
    PHYTOREMEDIATION = "PHYTOREMEDIATION"
    ELECTROKINETIC_REMEDIATION = "ELECTROKINETIC_REMEDIATION"
    CHEMICAL_OXIDATION = "CHEMICAL_OXIDATION"
    MONITORED_NATURAL_ATTENUATION = "MONITORED_NATURAL_ATTENUATION"

# Set metadata after class creation
NuclearRemediationType._metadata = {
    "SOIL_EXCAVATION": {'description': 'Physical removal and disposal of contaminated soil'},
    "GROUNDWATER_PUMP_AND_TREAT": {'description': 'Pumping contaminated groundwater to the surface for treatment and reinjection'},
    "IN_SITU_BIOREMEDIATION": {'description': 'Using microorganisms in place to degrade or immobilize radioactive contaminants'},
    "VITRIFICATION": {'description': 'Immobilizing radioactive waste by incorporating it into a glass matrix'},
    "STABILIZATION": {'description': 'Chemical or physical treatment to reduce the mobility of contaminants in soil or waste'},
    "CAPPING": {'description': 'Placing an engineered barrier over contaminated material to prevent migration and exposure'},
    "PHYTOREMEDIATION": {'description': 'Using plants to extract, contain, or degrade radioactive contaminants from soil and water'},
    "ELECTROKINETIC_REMEDIATION": {'description': 'Applying electric fields to move and concentrate contaminants in soil for removal'},
    "CHEMICAL_OXIDATION": {'description': 'Using chemical oxidants to destroy or transform organic contaminants at nuclear sites'},
    "MONITORED_NATURAL_ATTENUATION": {'description': 'Monitoring natural processes that reduce contaminant concentrations without active intervention'},
}

class DecommissioningPhaseType(RichEnum):
    """
    Phases in the decommissioning lifecycle of nuclear facilities
    """
    # Enum members
    CHARACTERIZATION = "CHARACTERIZATION"
    DECONTAMINATION = "DECONTAMINATION"
    DISMANTLEMENT = "DISMANTLEMENT"
    WASTE_MANAGEMENT = "WASTE_MANAGEMENT"
    SITE_RESTORATION = "SITE_RESTORATION"
    LONG_TERM_MONITORING = "LONG_TERM_MONITORING"
    LICENSE_TERMINATION = "LICENSE_TERMINATION"

# Set metadata after class creation
DecommissioningPhaseType._metadata = {
    "CHARACTERIZATION": {'description': 'Surveying and characterizing radiological and hazardous conditions at the facility'},
    "DECONTAMINATION": {'description': 'Removing radioactive contamination from surfaces, equipment, and structures', 'meaning': 'NCIT:C68769'},
    "DISMANTLEMENT": {'description': 'Physical demolition and removal of contaminated structures and equipment'},
    "WASTE_MANAGEMENT": {'description': 'Processing, packaging, transporting, and disposing of radioactive waste'},
    "SITE_RESTORATION": {'description': 'Restoring the site to a condition suitable for future use'},
    "LONG_TERM_MONITORING": {'description': 'Ongoing environmental monitoring after initial cleanup is complete'},
    "LICENSE_TERMINATION": {'description': 'Final regulatory review and release of the site from nuclear licensing requirements'},
}

class RadioactiveContaminantType(RichEnum):
    """
    Common radioactive contaminants found at nuclear cleanup sites
    """
    # Enum members
    CESIUM_137 = "CESIUM_137"
    STRONTIUM_90 = "STRONTIUM_90"
    TECHNETIUM_99 = "TECHNETIUM_99"
    TRITIUM = "TRITIUM"
    URANIUM = "URANIUM"
    PLUTONIUM = "PLUTONIUM"
    AMERICIUM_241 = "AMERICIUM_241"
    IODINE_129 = "IODINE_129"
    COBALT_60 = "COBALT_60"
    RADIUM_226 = "RADIUM_226"

# Set metadata after class creation
RadioactiveContaminantType._metadata = {
    "CESIUM_137": {'description': 'Cesium-137, a beta and gamma emitter with a half-life of approximately 30 years', 'meaning': 'CHEBI:196959', 'annotations': {'half_life': '30.17 years', 'decay_mode': 'beta, gamma'}},
    "STRONTIUM_90": {'description': 'Strontium-90, a beta emitter with a half-life of approximately 29 years', 'meaning': 'NCIT:C29776', 'annotations': {'half_life': '28.8 years', 'decay_mode': 'beta'}},
    "TECHNETIUM_99": {'description': 'Technetium-99, a long-lived beta emitter produced in fission reactors', 'meaning': 'CHEBI:33371', 'annotations': {'half_life': '211100 years', 'decay_mode': 'beta'}},
    "TRITIUM": {'description': 'Tritium (hydrogen-3), a low-energy beta emitter with a half-life of approximately 12 years', 'meaning': 'CHEBI:29238', 'annotations': {'half_life': '12.33 years', 'decay_mode': 'beta'}},
    "URANIUM": {'description': 'Uranium isotopes, alpha emitters with very long half-lives', 'meaning': 'CHEBI:27214', 'annotations': {'decay_mode': 'alpha'}},
    "PLUTONIUM": {'description': 'Plutonium isotopes, alpha emitters with long half-lives and high radiotoxicity', 'meaning': 'CHEBI:33388', 'annotations': {'decay_mode': 'alpha'}},
    "AMERICIUM_241": {'description': 'Americium-241, an alpha emitter with a half-life of approximately 432 years', 'meaning': 'CHEBI:33389', 'annotations': {'half_life': '432.2 years', 'decay_mode': 'alpha'}},
    "IODINE_129": {'description': 'Iodine-129, a long-lived beta and gamma emitter produced in nuclear fission', 'meaning': 'CHEBI:52636', 'annotations': {'half_life': '15.7 million years', 'decay_mode': 'beta, gamma'}},
    "COBALT_60": {'description': 'Cobalt-60, a gamma emitter with a half-life of approximately 5 years', 'meaning': 'NCIT:C28239', 'annotations': {'half_life': '5.27 years', 'decay_mode': 'beta, gamma'}},
    "RADIUM_226": {'description': 'Radium-226, an alpha emitter with a half-life of approximately 1600 years', 'meaning': 'CHEBI:80504', 'annotations': {'half_life': '1600 years', 'decay_mode': 'alpha'}},
}

__all__ = [
    "NuclearRemediationType",
    "DecommissioningPhaseType",
    "RadioactiveContaminantType",
]