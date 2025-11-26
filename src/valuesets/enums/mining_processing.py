"""
Mining and Mineral Processing Value Sets

Value sets for mining operations, mineral processing, beneficiation, and in-situ extraction, including bioleaching and autonomous mining systems.

Generated from: mining_processing.yaml
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

class MineralogyFeedstockClass(RichEnum):
    """
    Types of mineral feedstock sources for extraction and processing operations, including primary and secondary sources.
    
    """
    # Enum members
    HARDROCK_PRIMARY = "HARDROCK_PRIMARY"
    TAILINGS_LEGACY = "TAILINGS_LEGACY"
    WASTE_PILES = "WASTE_PILES"
    COAL_BYPRODUCT = "COAL_BYPRODUCT"
    E_WASTE = "E_WASTE"
    BRINES = "BRINES"

# Set metadata after class creation
MineralogyFeedstockClass._metadata = {
    "HARDROCK_PRIMARY": {'description': 'Primary ore from hardrock mining operations'},
    "TAILINGS_LEGACY": {'description': 'Historical mine tailings available for reprocessing'},
    "WASTE_PILES": {'description': 'Accumulated mining waste materials'},
    "COAL_BYPRODUCT": {'description': 'Byproducts from coal mining and processing'},
    "E_WASTE": {'description': 'Electronic waste containing recoverable metals'},
    "BRINES": {'description': 'Saline water sources containing dissolved minerals'},
}

class BeneficiationPathway(RichEnum):
    """
    Methods for mineral separation and concentration aligned with advanced ore processing initiatives (AOI-2).
    
    """
    # Enum members
    ORE_SORTING = "ORE_SORTING"
    DENSE_MEDIUM_SEPARATION = "DENSE_MEDIUM_SEPARATION"
    MICROWAVE_PREWEAKENING = "MICROWAVE_PREWEAKENING"
    ELECTRIC_PULSE_PREWEAKENING = "ELECTRIC_PULSE_PREWEAKENING"
    GRINDING_DYNAMIC = "GRINDING_DYNAMIC"
    ELECTROSTATIC_SEP = "ELECTROSTATIC_SEP"
    MAGNETIC_SEP = "MAGNETIC_SEP"
    FLOTATION_LOW_H2O = "FLOTATION_LOW_H2O"
    BIO_BENEFICIATION = "BIO_BENEFICIATION"

# Set metadata after class creation
BeneficiationPathway._metadata = {
    "ORE_SORTING": {'description': 'Sensor-based sorting of ore particles'},
    "DENSE_MEDIUM_SEPARATION": {'description': 'Gravity separation using dense media'},
    "MICROWAVE_PREWEAKENING": {'description': 'Microwave treatment to weaken ore structure'},
    "ELECTRIC_PULSE_PREWEAKENING": {'description': 'High-voltage electric pulse fragmentation'},
    "GRINDING_DYNAMIC": {'description': 'Dynamic grinding optimization systems'},
    "ELECTROSTATIC_SEP": {'description': 'Electrostatic separation of minerals'},
    "MAGNETIC_SEP": {'description': 'Magnetic separation of ferromagnetic minerals'},
    "FLOTATION_LOW_H2O": {'description': 'Low-water flotation processes'},
    "BIO_BENEFICIATION": {'description': 'Biological methods for mineral beneficiation'},
}

class InSituChemistryRegime(RichEnum):
    """
    Chemical leaching systems for in-situ extraction with associated parameters including pH, Eh, temperature, and ionic strength.
    
    """
    # Enum members
    ACIDIC_SULFATE = "ACIDIC_SULFATE"
    ACIDIC_CHLORIDE = "ACIDIC_CHLORIDE"
    AMMONIA_BASED = "AMMONIA_BASED"
    ORGANIC_ACID = "ORGANIC_ACID"
    BIOLEACH_SULFUR_OXIDIZING = "BIOLEACH_SULFUR_OXIDIZING"
    BIOLEACH_IRON_OXIDIZING = "BIOLEACH_IRON_OXIDIZING"

# Set metadata after class creation
InSituChemistryRegime._metadata = {
    "ACIDIC_SULFATE": {'description': 'Sulfuric acid-based leaching system'},
    "ACIDIC_CHLORIDE": {'description': 'Hydrochloric acid or chloride-based leaching'},
    "AMMONIA_BASED": {'description': 'Ammonia or ammonium-based leaching system'},
    "ORGANIC_ACID": {'description': 'Organic acid leaching (citric, oxalic, etc.)'},
    "BIOLEACH_SULFUR_OXIDIZING": {'description': 'Bioleaching using sulfur-oxidizing bacteria'},
    "BIOLEACH_IRON_OXIDIZING": {'description': 'Bioleaching using iron-oxidizing bacteria'},
}

class ExtractableTargetElement(RichEnum):
    """
    Target elements for extraction, particularly rare earth elements (REE) and critical minerals.
    
    """
    # Enum members
    REE_LA = "REE_LA"
    REE_CE = "REE_CE"
    REE_PR = "REE_PR"
    REE_ND = "REE_ND"
    REE_PM = "REE_PM"
    REE_SM = "REE_SM"
    REE_EU = "REE_EU"
    REE_GD = "REE_GD"
    REE_TB = "REE_TB"
    REE_DY = "REE_DY"
    REE_HO = "REE_HO"
    REE_ER = "REE_ER"
    REE_TM = "REE_TM"
    REE_YB = "REE_YB"
    REE_LU = "REE_LU"
    SC = "SC"
    CO = "CO"
    NI = "NI"
    LI = "LI"

# Set metadata after class creation
ExtractableTargetElement._metadata = {
    "REE_LA": {'description': 'Lanthanum'},
    "REE_CE": {'description': 'Cerium'},
    "REE_PR": {'description': 'Praseodymium'},
    "REE_ND": {'description': 'Neodymium'},
    "REE_PM": {'description': 'Promethium'},
    "REE_SM": {'description': 'Samarium'},
    "REE_EU": {'description': 'Europium'},
    "REE_GD": {'description': 'Gadolinium'},
    "REE_TB": {'description': 'Terbium'},
    "REE_DY": {'description': 'Dysprosium'},
    "REE_HO": {'description': 'Holmium'},
    "REE_ER": {'description': 'Erbium'},
    "REE_TM": {'description': 'Thulium'},
    "REE_YB": {'description': 'Ytterbium'},
    "REE_LU": {'description': 'Lutetium'},
    "SC": {'description': 'Scandium'},
    "CO": {'description': 'Cobalt'},
    "NI": {'description': 'Nickel'},
    "LI": {'description': 'Lithium'},
}

class SensorWhileDrillingFeature(RichEnum):
    """
    Measurement while drilling (MWD) and logging while drilling (LWD) features for orebody ML and geosteering applications.
    
    """
    # Enum members
    WOB = "WOB"
    ROP = "ROP"
    TORQUE = "TORQUE"
    MWD_GAMMA = "MWD_GAMMA"
    MWD_RESISTIVITY = "MWD_RESISTIVITY"
    MUD_LOSS = "MUD_LOSS"
    VIBRATION = "VIBRATION"
    RSS_ANGLE = "RSS_ANGLE"

# Set metadata after class creation
SensorWhileDrillingFeature._metadata = {
    "WOB": {'description': 'Weight on bit measurement'},
    "ROP": {'description': 'Rate of penetration'},
    "TORQUE": {'description': 'Rotational torque measurement'},
    "MWD_GAMMA": {'description': 'Gamma ray logging while drilling'},
    "MWD_RESISTIVITY": {'description': 'Resistivity logging while drilling'},
    "MUD_LOSS": {'description': 'Drilling mud loss measurement'},
    "VIBRATION": {'description': 'Drill string vibration monitoring'},
    "RSS_ANGLE": {'description': 'Rotary steerable system angle'},
}

class ProcessPerformanceMetric(RichEnum):
    """
    Key performance indicators for mining and processing operations tied to SMART milestones and sustainability goals.
    
    """
    # Enum members
    RECOVERY_PCT = "RECOVERY_PCT"
    SELECTIVITY_INDEX = "SELECTIVITY_INDEX"
    SPECIFIC_ENERGY_KWH_T = "SPECIFIC_ENERGY_KWH_T"
    WATER_INTENSITY_L_T = "WATER_INTENSITY_L_T"
    REAGENT_INTENSITY_KG_T = "REAGENT_INTENSITY_KG_T"
    CO2E_KG_T = "CO2E_KG_T"
    TAILINGS_MASS_REDUCTION_PCT = "TAILINGS_MASS_REDUCTION_PCT"

# Set metadata after class creation
ProcessPerformanceMetric._metadata = {
    "RECOVERY_PCT": {'description': 'Percentage recovery of target material'},
    "SELECTIVITY_INDEX": {'description': 'Selectivity index for separation processes'},
    "SPECIFIC_ENERGY_KWH_T": {'description': 'Specific energy consumption in kWh per tonne'},
    "WATER_INTENSITY_L_T": {'description': 'Water usage intensity in liters per tonne'},
    "REAGENT_INTENSITY_KG_T": {'description': 'Reagent consumption in kg per tonne'},
    "CO2E_KG_T": {'description': 'CO2 equivalent emissions in kg per tonne'},
    "TAILINGS_MASS_REDUCTION_PCT": {'description': 'Percentage reduction in tailings mass'},
}

class BioleachOrganism(RichEnum):
    """
    Microorganisms used in bioleaching and biomining operations, including engineered strains.
    
    """
    # Enum members
    ACIDITHIOBACILLUS_FERROOXIDANS = "ACIDITHIOBACILLUS_FERROOXIDANS"
    LEPTOSPIRILLUM_FERROOXIDANS = "LEPTOSPIRILLUM_FERROOXIDANS"
    ASPERGILLUS_NIGER = "ASPERGILLUS_NIGER"
    ENGINEERED_STRAIN = "ENGINEERED_STRAIN"

# Set metadata after class creation
BioleachOrganism._metadata = {
    "ACIDITHIOBACILLUS_FERROOXIDANS": {'description': 'Iron and sulfur oxidizing bacterium', 'meaning': 'NCBITaxon:920'},
    "LEPTOSPIRILLUM_FERROOXIDANS": {'description': 'Iron oxidizing bacterium', 'meaning': 'NCBITaxon:180'},
    "ASPERGILLUS_NIGER": {'description': 'Organic acid producing fungus', 'meaning': 'NCBITaxon:5061'},
    "ENGINEERED_STRAIN": {'description': 'Genetically modified organism for enhanced bioleaching'},
}

class BioleachMode(RichEnum):
    """
    Mechanisms of bioleaching including indirect and direct bacterial action.
    
    """
    # Enum members
    INDIRECT_BIOLEACH_ORGANIC_ACIDS = "INDIRECT_BIOLEACH_ORGANIC_ACIDS"
    SULFUR_OXIDATION = "SULFUR_OXIDATION"
    IRON_OXIDATION = "IRON_OXIDATION"

# Set metadata after class creation
BioleachMode._metadata = {
    "INDIRECT_BIOLEACH_ORGANIC_ACIDS": {'description': 'Indirect bioleaching through organic acid production'},
    "SULFUR_OXIDATION": {'description': 'Direct bacterial oxidation of sulfur compounds'},
    "IRON_OXIDATION": {'description': 'Direct bacterial oxidation of iron compounds'},
}

class AutonomyLevel(RichEnum):
    """
    Levels of autonomy for mining systems including drilling, hauling, and sorting robots (relevant for Topic 1 initiatives).
    
    """
    # Enum members
    ASSISTIVE = "ASSISTIVE"
    SUPERVISED_AUTONOMY = "SUPERVISED_AUTONOMY"
    SEMI_AUTONOMOUS = "SEMI_AUTONOMOUS"
    FULLY_AUTONOMOUS = "FULLY_AUTONOMOUS"

# Set metadata after class creation
AutonomyLevel._metadata = {
    "ASSISTIVE": {'description': 'Human operator with assistive technologies'},
    "SUPERVISED_AUTONOMY": {'description': 'Autonomous operation with human supervision'},
    "SEMI_AUTONOMOUS": {'description': 'Partial autonomy with human intervention capability'},
    "FULLY_AUTONOMOUS": {'description': 'Complete autonomous operation without human intervention'},
}

class RegulatoryConstraint(RichEnum):
    """
    Regulatory and community constraints affecting mining operations, particularly for in-situ extraction and community engagement.
    
    """
    # Enum members
    AQUIFER_PROTECTION = "AQUIFER_PROTECTION"
    EMISSIONS_CAP = "EMISSIONS_CAP"
    CULTURAL_HERITAGE_ZONE = "CULTURAL_HERITAGE_ZONE"
    WATER_RIGHTS_LIMIT = "WATER_RIGHTS_LIMIT"

# Set metadata after class creation
RegulatoryConstraint._metadata = {
    "AQUIFER_PROTECTION": {'description': 'Requirements for groundwater and aquifer protection'},
    "EMISSIONS_CAP": {'description': 'Limits on atmospheric emissions'},
    "CULTURAL_HERITAGE_ZONE": {'description': 'Protection of cultural heritage sites'},
    "WATER_RIGHTS_LIMIT": {'description': 'Restrictions based on water usage rights'},
}

__all__ = [
    "RelativeTimeEnum",
    "PresenceEnum",
    "MineralogyFeedstockClass",
    "BeneficiationPathway",
    "InSituChemistryRegime",
    "ExtractableTargetElement",
    "SensorWhileDrillingFeature",
    "ProcessPerformanceMetric",
    "BioleachOrganism",
    "BioleachMode",
    "AutonomyLevel",
    "RegulatoryConstraint",
]