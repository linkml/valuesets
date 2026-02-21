"""
Unconventional Mineral Resources Value Sets

Value sets for unconventional mineral resource types and recovery methods relevant to the DOE AI-Driven Living Mine lighthouse

Generated from: industry/unconventional_resources.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class UnconventionalMineralResourceType(RichEnum):
    """
    Types of unconventional mineral resources including industrial waste streams, mining residues, and brines that contain recoverable critical minerals and metals
    """
    # Enum members
    MINE_TAILINGS = "MINE_TAILINGS"
    WASTE_ROCK = "WASTE_ROCK"
    ACID_MINE_DRAINAGE = "ACID_MINE_DRAINAGE"
    COAL_COMBUSTION_RESIDUALS = "COAL_COMBUSTION_RESIDUALS"
    RED_MUD = "RED_MUD"
    PHOSPHOGYPSUM = "PHOSPHOGYPSUM"
    SLAG = "SLAG"
    FLY_ASH = "FLY_ASH"
    ELECTRONIC_WASTE = "ELECTRONIC_WASTE"
    SPENT_CATALYSTS = "SPENT_CATALYSTS"
    GEOTHERMAL_BRINE = "GEOTHERMAL_BRINE"
    OIL_FIELD_BRINE = "OIL_FIELD_BRINE"

# Set metadata after class creation
UnconventionalMineralResourceType._metadata = {
    "MINE_TAILINGS": {'description': 'Materials remaining after separating the valuable fraction from the uneconomic fraction of an ore', 'meaning': 'ENVO:00000003'},
    "WASTE_ROCK": {'description': 'Rock removed during mining that does not contain sufficient mineral of interest for processing', 'annotations': {'source': 'surface and underground mining'}},
    "ACID_MINE_DRAINAGE": {'description': 'Acidic water outflow from mines containing dissolved metals and sulfuric acid', 'meaning': 'ENVO:00001997'},
    "COAL_COMBUSTION_RESIDUALS": {'description': 'Residual materials from combustion of coal in power plants, including fly ash, bottom ash, and boiler slag', 'meaning': 'ENVO:02000127'},
    "RED_MUD": {'description': 'Alkaline residue generated during alumina extraction from bauxite ore via the Bayer process', 'annotations': {'composition': 'iron oxides, alumina, silica, rare earth elements', 'source': 'alumina refining'}},
    "PHOSPHOGYPSUM": {'description': 'Gypsum byproduct from phosphoric acid production containing trace radioactive elements and rare earth elements', 'annotations': {'composition': 'calcium sulfate dihydrate with trace REE', 'source': 'phosphate fertilizer production'}},
    "SLAG": {'description': 'Glassy material formed as a byproduct of smelting and refining metal ores', 'meaning': 'ENVO:02000130'},
    "FLY_ASH": {'description': 'Fine powdery material composed mostly of silica collected from flue gases during coal combustion', 'meaning': 'ENVO:02000128'},
    "ELECTRONIC_WASTE": {'description': 'Discarded electronic devices and components containing recoverable precious and critical metals', 'annotations': {'metals': 'gold, silver, platinum, copper, rare earth elements'}},
    "SPENT_CATALYSTS": {'description': 'Used industrial catalysts containing recoverable platinum group metals and other valuable elements', 'annotations': {'metals': 'platinum, palladium, rhodium, rhenium', 'source': 'petroleum refining, chemical manufacturing'}},
    "GEOTHERMAL_BRINE": {'description': 'Hot saline water from geothermal systems containing dissolved lithium, rare earth elements, and other minerals', 'meaning': 'ENVO:00003044'},
    "OIL_FIELD_BRINE": {'description': 'Saline water produced during oil and gas extraction containing dissolved minerals including lithium and boron', 'annotations': {'minerals': 'lithium, bromine, boron, iodine', 'source': 'oil and gas production'}},
}

class BioextractionMethodType(RichEnum):
    """
    Biological methods for extracting metals and minerals from unconventional resources using microorganisms or plants
    """
    # Enum members
    HEAP_BIOLEACHING = "HEAP_BIOLEACHING"
    STIRRED_TANK_BIOLEACHING = "STIRRED_TANK_BIOLEACHING"
    IN_SITU_BIOLEACHING = "IN_SITU_BIOLEACHING"
    PHYTOMINING = "PHYTOMINING"
    BIOSORPTION = "BIOSORPTION"
    BIOACCUMULATION = "BIOACCUMULATION"
    BIOPRECIPITATION = "BIOPRECIPITATION"
    BIOFLOTATION = "BIOFLOTATION"

# Set metadata after class creation
BioextractionMethodType._metadata = {
    "HEAP_BIOLEACHING": {'description': 'Biological leaching of metals from crushed ore stacked in heaps irrigated with acidic microbial solutions', 'annotations': {'organisms': 'Acidithiobacillus ferrooxidans, Acidithiobacillus thiooxidans', 'scale': 'industrial'}},
    "STIRRED_TANK_BIOLEACHING": {'description': 'Biological leaching of metals in agitated tank reactors with controlled conditions', 'annotations': {'organisms': 'Acidithiobacillus, Leptospirillum', 'scale': 'industrial, pilot'}},
    "IN_SITU_BIOLEACHING": {'description': 'Biological leaching of metals directly in the ore body without excavation', 'annotations': {'advantage': 'minimal surface disturbance', 'application': 'low-grade deposits'}},
    "PHYTOMINING": {'description': 'Use of hyperaccumulator plants to extract metals from soil or mining waste for recovery', 'annotations': {'organisms': 'Alyssum, Thlaspi, Pteris', 'metals': 'nickel, zinc, thallium'}},
    "BIOSORPTION": {'description': 'Passive binding of metal ions to the surface of biological materials such as microbial biomass', 'annotations': {'mechanism': 'surface complexation, ion exchange', 'materials': 'dead biomass, algae, fungi'}},
    "BIOACCUMULATION": {'description': 'Active uptake and intracellular concentration of metals by living organisms', 'annotations': {'mechanism': 'metabolically driven intracellular uptake', 'organisms': 'bacteria, fungi, algae'}},
    "BIOPRECIPITATION": {'description': 'Microbially mediated precipitation of metals as insoluble compounds such as sulfides or phosphates', 'annotations': {'mechanism': 'sulfate reduction, phosphate release', 'products': 'metal sulfides, metal phosphates'}},
    "BIOFLOTATION": {'description': 'Use of microorganisms or biosurfactants to selectively separate mineral particles by flotation', 'annotations': {'mechanism': 'selective surface modification', 'organisms': 'Mycobacterium, Bacillus'}},
}

class TailingCharacterizationType(RichEnum):
    """
    Types of measurements and analyses used to characterize mine tailings and other mineral processing residues for resource recovery potential
    """
    # Enum members
    PARTICLE_SIZE_DISTRIBUTION = "PARTICLE_SIZE_DISTRIBUTION"
    MINERALOGICAL_COMPOSITION = "MINERALOGICAL_COMPOSITION"
    ACID_GENERATING_POTENTIAL = "ACID_GENERATING_POTENTIAL"
    METAL_CONTENT = "METAL_CONTENT"
    MOISTURE_CONTENT = "MOISTURE_CONTENT"
    GEOTECHNICAL_STABILITY = "GEOTECHNICAL_STABILITY"
    ENVIRONMENTAL_RISK_CLASSIFICATION = "ENVIRONMENTAL_RISK_CLASSIFICATION"

# Set metadata after class creation
TailingCharacterizationType._metadata = {
    "PARTICLE_SIZE_DISTRIBUTION": {'description': 'Measurement of the distribution of particle sizes in tailing material', 'meaning': 'CHMO:0002119', 'annotations': {'methods': 'sieve analysis, laser diffraction, sedimentation'}},
    "MINERALOGICAL_COMPOSITION": {'description': 'Determination of mineral phases present in tailing material using diffraction and spectroscopic methods', 'annotations': {'methods': 'XRD, SEM-EDS, QEMSCAN, MLA'}},
    "ACID_GENERATING_POTENTIAL": {'description': 'Assessment of the potential for tailings to generate acid drainage through sulfide oxidation', 'annotations': {'tests': 'acid-base accounting, NAG test, kinetic testing'}},
    "METAL_CONTENT": {'description': 'Quantitative analysis of metal and element concentrations in tailing material', 'annotations': {'methods': 'ICP-MS, ICP-OES, XRF'}},
    "MOISTURE_CONTENT": {'description': 'Measurement of water content in tailing material affecting stability and handling', 'annotations': {'methods': 'gravimetric, nuclear moisture gauge'}},
    "GEOTECHNICAL_STABILITY": {'description': 'Assessment of the mechanical and physical stability of tailing storage facilities', 'annotations': {'parameters': 'shear strength, consolidation, liquefaction potential'}},
    "ENVIRONMENTAL_RISK_CLASSIFICATION": {'description': 'Classification of environmental risk based on contaminant mobility, toxicity, and exposure pathways', 'annotations': {'frameworks': 'TCLP, WET, environmental impact assessment'}},
}

__all__ = [
    "UnconventionalMineralResourceType",
    "BioextractionMethodType",
    "TailingCharacterizationType",
]