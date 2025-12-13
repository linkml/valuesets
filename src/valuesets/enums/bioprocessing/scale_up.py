"""
Bioprocessing Scale-up Value Sets

Value sets for bioprocessing scale-up facilities, fermentation, and biomanufacturing
operations like those at ABPDU (Advanced Biofuels and Bioproducts Process Development Unit)

Generated from: bioprocessing/scale_up.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class ProcessScaleEnum(RichEnum):
    """
    Scale of bioprocessing operations from lab bench to commercial production
    """
    # Enum members
    BENCH_SCALE = "BENCH_SCALE"
    PILOT_SCALE = "PILOT_SCALE"
    DEMONSTRATION_SCALE = "DEMONSTRATION_SCALE"
    PRODUCTION_SCALE = "PRODUCTION_SCALE"
    MICROFLUIDIC_SCALE = "MICROFLUIDIC_SCALE"

# Set metadata after class creation
ProcessScaleEnum._metadata = {
    "BENCH_SCALE": {'description': 'Laboratory bench scale (typically < 10 L)', 'annotations': {'volume_range': '0.1-10 L', 'typical_volume': '1-5 L', 'purpose': 'Initial development and screening'}},
    "PILOT_SCALE": {'description': 'Pilot plant scale (10-1000 L)', 'annotations': {'volume_range': '10-1000 L', 'typical_volume': '50-500 L', 'purpose': 'Process development and optimization'}},
    "DEMONSTRATION_SCALE": {'description': 'Demonstration scale (1000-10000 L)', 'annotations': {'volume_range': '1000-10000 L', 'typical_volume': '2000-5000 L', 'purpose': 'Technology demonstration and validation'}},
    "PRODUCTION_SCALE": {'description': 'Commercial production scale (>10000 L)', 'annotations': {'volume_range': '>10000 L', 'typical_volume': '20000-200000 L', 'purpose': 'Commercial manufacturing'}},
    "MICROFLUIDIC_SCALE": {'description': 'Microfluidic scale (<1 mL)', 'annotations': {'volume_range': '<1 mL', 'typical_volume': '1-1000 μL', 'purpose': 'High-throughput screening'}},
}

class BioreactorTypeEnum(RichEnum):
    """
    Types of bioreactors used in fermentation and cell culture
    """
    # Enum members
    STIRRED_TANK = "STIRRED_TANK"
    AIRLIFT = "AIRLIFT"
    BUBBLE_COLUMN = "BUBBLE_COLUMN"
    PACKED_BED = "PACKED_BED"
    FLUIDIZED_BED = "FLUIDIZED_BED"
    MEMBRANE = "MEMBRANE"
    WAVE_BAG = "WAVE_BAG"
    HOLLOW_FIBER = "HOLLOW_FIBER"
    PHOTOBIOREACTOR = "PHOTOBIOREACTOR"

# Set metadata after class creation
BioreactorTypeEnum._metadata = {
    "STIRRED_TANK": {'description': 'Stirred tank reactor (STR/CSTR)', 'annotations': {'mixing': 'Mechanical agitation', 'common_volumes': '1-200000 L'}},
    "AIRLIFT": {'description': 'Airlift bioreactor', 'annotations': {'mixing': 'Gas sparging', 'advantages': 'Low shear, no mechanical parts'}},
    "BUBBLE_COLUMN": {'description': 'Bubble column bioreactor', 'annotations': {'mixing': 'Gas bubbling', 'advantages': 'Simple design, good mass transfer'}},
    "PACKED_BED": {'description': 'Packed bed bioreactor', 'annotations': {'configuration': 'Fixed bed of immobilized cells/enzymes', 'flow': 'Continuous'}},
    "FLUIDIZED_BED": {'description': 'Fluidized bed bioreactor', 'annotations': {'configuration': 'Suspended solid particles', 'mixing': 'Fluid flow'}},
    "MEMBRANE": {'description': 'Membrane bioreactor', 'meaning': 'ENVO:03600010', 'annotations': {'feature': 'Integrated membrane separation', 'application': 'Cell retention, product separation'}},
    "WAVE_BAG": {'description': 'Wave/rocking bioreactor', 'annotations': {'mixing': 'Rocking motion', 'advantages': 'Single-use, low shear'}},
    "HOLLOW_FIBER": {'description': 'Hollow fiber bioreactor', 'annotations': {'configuration': 'Hollow fiber membranes', 'application': 'High-density cell culture'}},
    "PHOTOBIOREACTOR": {'description': 'Photobioreactor for photosynthetic organisms', 'annotations': {'light_source': 'Required', 'organisms': 'Algae, cyanobacteria'}},
}

class FermentationModeEnum(RichEnum):
    """
    Modes of fermentation operation
    """
    # Enum members
    BATCH = "BATCH"
    FED_BATCH = "FED_BATCH"
    CONTINUOUS = "CONTINUOUS"
    PERFUSION = "PERFUSION"
    REPEATED_BATCH = "REPEATED_BATCH"
    SEMI_CONTINUOUS = "SEMI_CONTINUOUS"

# Set metadata after class creation
FermentationModeEnum._metadata = {
    "BATCH": {'description': 'Batch fermentation', 'meaning': 'MSIO:0000181', 'annotations': {'operation': 'All nutrients added at start', 'duration': 'Fixed time period'}},
    "FED_BATCH": {'description': 'Fed-batch fermentation', 'annotations': {'operation': 'Nutrients added during run', 'advantage': 'Control of growth rate'}},
    "CONTINUOUS": {'description': 'Continuous fermentation (chemostat)', 'meaning': 'MSIO:0000155', 'annotations': {'operation': 'Continuous feed and harvest', 'steady_state': True}},
    "PERFUSION": {'description': 'Perfusion culture', 'annotations': {'operation': 'Continuous media exchange with cell retention', 'application': 'High-density cell culture'}},
    "REPEATED_BATCH": {'description': 'Repeated batch fermentation', 'annotations': {'operation': 'Sequential batches with partial harvest', 'advantage': 'Reduced downtime'}},
    "SEMI_CONTINUOUS": {'description': 'Semi-continuous operation', 'annotations': {'operation': 'Periodic harvest and refill', 'advantage': 'Extended production'}},
}

class OxygenationStrategyEnum(RichEnum):
    """
    Oxygen supply strategies for fermentation
    """
    # Enum members
    AEROBIC = "AEROBIC"
    ANAEROBIC = "ANAEROBIC"
    MICROAEROBIC = "MICROAEROBIC"
    FACULTATIVE = "FACULTATIVE"

# Set metadata after class creation
OxygenationStrategyEnum._metadata = {
    "AEROBIC": {'description': 'Aerobic with active aeration', 'annotations': {'oxygen': 'Required', 'typical_DO': '20-80% saturation'}},
    "ANAEROBIC": {'description': 'Anaerobic (no oxygen)', 'annotations': {'oxygen': 'Excluded', 'atmosphere': 'N2 or CO2'}},
    "MICROAEROBIC": {'description': 'Microaerobic (limited oxygen)', 'annotations': {'oxygen': 'Limited', 'typical_DO': '<5% saturation'}},
    "FACULTATIVE": {'description': 'Facultative (with/without oxygen)', 'annotations': {'oxygen': 'Optional', 'flexibility': 'Organism-dependent'}},
}

class AgitationTypeEnum(RichEnum):
    """
    Types of agitation/mixing in bioreactors
    """
    # Enum members
    RUSHTON_TURBINE = "RUSHTON_TURBINE"
    PITCHED_BLADE = "PITCHED_BLADE"
    MARINE_PROPELLER = "MARINE_PROPELLER"
    ANCHOR = "ANCHOR"
    HELICAL_RIBBON = "HELICAL_RIBBON"
    MAGNETIC_BAR = "MAGNETIC_BAR"
    ORBITAL_SHAKING = "ORBITAL_SHAKING"
    NO_AGITATION = "NO_AGITATION"

# Set metadata after class creation
AgitationTypeEnum._metadata = {
    "RUSHTON_TURBINE": {'description': 'Rushton turbine impeller', 'annotations': {'type': 'Radial flow', 'power_number': '5-6'}},
    "PITCHED_BLADE": {'description': 'Pitched blade turbine', 'annotations': {'type': 'Axial flow', 'angle': '45 degrees'}},
    "MARINE_PROPELLER": {'description': 'Marine propeller', 'annotations': {'type': 'Axial flow', 'low_shear': True}},
    "ANCHOR": {'description': 'Anchor impeller', 'annotations': {'type': 'Close clearance', 'viscous_fluids': True}},
    "HELICAL_RIBBON": {'description': 'Helical ribbon impeller', 'annotations': {'type': 'Close clearance', 'high_viscosity': True}},
    "MAGNETIC_BAR": {'description': 'Magnetic stir bar', 'annotations': {'scale': 'Laboratory', 'volume': '<5 L'}},
    "ORBITAL_SHAKING": {'description': 'Orbital shaking', 'annotations': {'type': 'Platform shaker', 'application': 'Shake flasks'}},
    "NO_AGITATION": {'description': 'No mechanical agitation', 'annotations': {'mixing': 'Gas sparging or static'}},
}

class DownstreamProcessEnum(RichEnum):
    """
    Downstream processing unit operations
    """
    # Enum members
    CENTRIFUGATION = "CENTRIFUGATION"
    FILTRATION = "FILTRATION"
    CHROMATOGRAPHY = "CHROMATOGRAPHY"
    EXTRACTION = "EXTRACTION"
    PRECIPITATION = "PRECIPITATION"
    EVAPORATION = "EVAPORATION"
    DISTILLATION = "DISTILLATION"
    DRYING = "DRYING"
    HOMOGENIZATION = "HOMOGENIZATION"

# Set metadata after class creation
DownstreamProcessEnum._metadata = {
    "CENTRIFUGATION": {'description': 'Centrifugal separation', 'meaning': 'CHMO:0002010', 'annotations': {'principle': 'Density difference', 'types': 'Disk stack, tubular, decanter'}},
    "FILTRATION": {'description': 'Filtration (micro/ultra/nano)', 'meaning': 'CHMO:0001640', 'annotations': {'types': 'Dead-end, crossflow, depth'}},
    "CHROMATOGRAPHY": {'description': 'Chromatographic separation', 'meaning': 'CHMO:0001000', 'annotations': {'types': 'Ion exchange, affinity, size exclusion'}},
    "EXTRACTION": {'description': 'Liquid-liquid extraction', 'meaning': 'CHMO:0001577', 'annotations': {'principle': 'Partitioning between phases'}},
    "PRECIPITATION": {'description': 'Precipitation/crystallization', 'meaning': 'CHMO:0001688', 'annotations': {'agents': 'Salts, solvents, pH'}},
    "EVAPORATION": {'description': 'Evaporation/concentration', 'meaning': 'CHMO:0001574', 'annotations': {'types': 'Falling film, MVR, TVR'}},
    "DISTILLATION": {'description': 'Distillation', 'meaning': 'CHMO:0001534', 'annotations': {'principle': 'Boiling point difference'}},
    "DRYING": {'description': 'Drying operations', 'meaning': 'CHMO:0001551', 'annotations': {'types': 'Spray, freeze, vacuum'}},
    "HOMOGENIZATION": {'description': 'Cell disruption/homogenization', 'annotations': {'methods': 'High pressure, bead mill'}},
}

class FeedstockTypeEnum(RichEnum):
    """
    Types of feedstocks for bioprocessing
    """
    # Enum members
    GLUCOSE = "GLUCOSE"
    SUCROSE = "SUCROSE"
    GLYCEROL = "GLYCEROL"
    MOLASSES = "MOLASSES"
    CORN_STEEP_LIQUOR = "CORN_STEEP_LIQUOR"
    YEAST_EXTRACT = "YEAST_EXTRACT"
    LIGNOCELLULOSIC = "LIGNOCELLULOSIC"
    METHANOL = "METHANOL"
    WASTE_STREAM = "WASTE_STREAM"

# Set metadata after class creation
FeedstockTypeEnum._metadata = {
    "GLUCOSE": {'description': 'Glucose/dextrose', 'meaning': 'CHEBI:17234', 'annotations': {'source': 'Corn, sugarcane', 'carbon_source': True}},
    "SUCROSE": {'description': 'Sucrose', 'meaning': 'CHEBI:17992', 'annotations': {'source': 'Sugarcane, sugar beet', 'carbon_source': True}},
    "GLYCEROL": {'description': 'Glycerol', 'meaning': 'CHEBI:17754', 'annotations': {'source': 'Biodiesel byproduct', 'carbon_source': True}},
    "MOLASSES": {'description': 'Molasses', 'meaning': 'CHEBI:83163', 'annotations': {'source': 'Sugar processing byproduct', 'complex_medium': True}},
    "CORN_STEEP_LIQUOR": {'description': 'Corn steep liquor', 'annotations': {'source': 'Corn wet milling', 'nitrogen_source': True}},
    "YEAST_EXTRACT": {'description': 'Yeast extract', 'meaning': 'FOODON:03315426', 'annotations': {'source': 'Autolyzed yeast', 'complex_nutrient': True}},
    "LIGNOCELLULOSIC": {'description': 'Lignocellulosic biomass', 'annotations': {'source': 'Agricultural residues, wood', 'pretreatment': 'Required'}},
    "METHANOL": {'description': 'Methanol', 'meaning': 'CHEBI:17790', 'annotations': {'carbon_source': True, 'methylotrophic': True}},
    "WASTE_STREAM": {'description': 'Industrial waste stream', 'annotations': {'variable_composition': True, 'sustainability': 'Circular economy'}},
}

class ProductTypeEnum(RichEnum):
    """
    Types of products from bioprocessing
    """
    # Enum members
    BIOFUEL = "BIOFUEL"
    PROTEIN = "PROTEIN"
    ENZYME = "ENZYME"
    ORGANIC_ACID = "ORGANIC_ACID"
    AMINO_ACID = "AMINO_ACID"
    ANTIBIOTIC = "ANTIBIOTIC"
    VITAMIN = "VITAMIN"
    BIOPOLYMER = "BIOPOLYMER"
    BIOMASS = "BIOMASS"
    SECONDARY_METABOLITE = "SECONDARY_METABOLITE"

# Set metadata after class creation
ProductTypeEnum._metadata = {
    "BIOFUEL": {'description': 'Biofuel (ethanol, biodiesel, etc.)', 'meaning': 'CHEBI:33292', 'annotations': {'category': 'Energy'}},
    "PROTEIN": {'description': 'Recombinant protein', 'meaning': 'NCIT:C17021', 'annotations': {'category': 'Biopharmaceutical'}},
    "ENZYME": {'description': 'Industrial enzyme', 'meaning': 'NCIT:C16554', 'annotations': {'category': 'Biocatalyst'}},
    "ORGANIC_ACID": {'description': 'Organic acid (citric, lactic, etc.)', 'meaning': 'CHEBI:64709', 'annotations': {'category': 'Chemical'}},
    "AMINO_ACID": {'description': 'Amino acid', 'meaning': 'CHEBI:33709', 'annotations': {'category': 'Nutritional'}},
    "ANTIBIOTIC": {'description': 'Antibiotic', 'meaning': 'CHEBI:33281', 'annotations': {'category': 'Pharmaceutical'}},
    "VITAMIN": {'description': 'Vitamin', 'meaning': 'CHEBI:33229', 'annotations': {'category': 'Nutritional'}},
    "BIOPOLYMER": {'description': 'Biopolymer (PHA, PLA, etc.)', 'meaning': 'CHEBI:33694', 'annotations': {'category': 'Material'}},
    "BIOMASS": {'description': 'Microbial biomass', 'meaning': 'ENVO:01000155', 'annotations': {'category': 'Feed/food'}},
    "SECONDARY_METABOLITE": {'description': 'Secondary metabolite', 'meaning': 'CHEBI:25212', 'annotations': {'category': 'Specialty chemical'}},
}

class SterilizationMethodEnum(RichEnum):
    """
    Methods for sterilization in bioprocessing
    """
    # Enum members
    STEAM_IN_PLACE = "STEAM_IN_PLACE"
    AUTOCLAVE = "AUTOCLAVE"
    FILTER_STERILIZATION = "FILTER_STERILIZATION"
    GAMMA_IRRADIATION = "GAMMA_IRRADIATION"
    ETHYLENE_OXIDE = "ETHYLENE_OXIDE"
    UV_STERILIZATION = "UV_STERILIZATION"
    CHEMICAL_STERILIZATION = "CHEMICAL_STERILIZATION"

# Set metadata after class creation
SterilizationMethodEnum._metadata = {
    "STEAM_IN_PLACE": {'description': 'Steam in place (SIP)', 'annotations': {'temperature': '121-134°C', 'time': '15-30 min'}},
    "AUTOCLAVE": {'description': 'Autoclave sterilization', 'meaning': 'CHMO:0002846', 'annotations': {'temperature': '121°C', 'pressure': '15 psi'}},
    "FILTER_STERILIZATION": {'description': 'Filter sterilization (0.2 μm)', 'annotations': {'pore_size': '0.2 μm', 'heat_labile': True}},
    "GAMMA_IRRADIATION": {'description': 'Gamma irradiation', 'annotations': {'dose': '25-40 kGy', 'single_use': True}},
    "ETHYLENE_OXIDE": {'description': 'Ethylene oxide sterilization', 'annotations': {'temperature': '30-60°C', 'plastic_compatible': True}},
    "UV_STERILIZATION": {'description': 'UV sterilization', 'annotations': {'wavelength': '254 nm', 'surface_only': True}},
    "CHEMICAL_STERILIZATION": {'description': 'Chemical sterilization', 'annotations': {'agents': 'Bleach, alcohol, peroxide', 'contact_time': 'Variable'}},
}

__all__ = [
    "ProcessScaleEnum",
    "BioreactorTypeEnum",
    "FermentationModeEnum",
    "OxygenationStrategyEnum",
    "AgitationTypeEnum",
    "DownstreamProcessEnum",
    "FeedstockTypeEnum",
    "ProductTypeEnum",
    "SterilizationMethodEnum",
]