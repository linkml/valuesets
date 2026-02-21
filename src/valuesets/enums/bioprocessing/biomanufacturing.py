"""
Biomanufacturing Value Sets

Value sets for biomanufacturing scales, processes, and product categories relevant to the DOE Scaling the Biotechnology Revolution challenge

Generated from: bioprocessing/biomanufacturing.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class BiomanufacturingScaleType(RichEnum):
    """
    Scale classifications for biomanufacturing operations, from micro-scale screening through commercial production
    """
    # Enum members
    BENCH_SCALE = "BENCH_SCALE"
    PILOT_SCALE = "PILOT_SCALE"
    DEMONSTRATION_SCALE = "DEMONSTRATION_SCALE"
    COMMERCIAL_SCALE = "COMMERCIAL_SCALE"
    MICRO_SCALE = "MICRO_SCALE"

# Set metadata after class creation
BiomanufacturingScaleType._metadata = {
    "BENCH_SCALE": {'description': 'Laboratory bench scale operations, typically less than 10 liters', 'annotations': {'volume_range': '<10 L', 'purpose': 'Initial development and screening'}},
    "PILOT_SCALE": {'description': 'Pilot plant scale operations for process development, typically 10-1000 liters', 'annotations': {'volume_range': '10-1000 L', 'purpose': 'Process development and optimization'}},
    "DEMONSTRATION_SCALE": {'description': 'Demonstration scale operations for technology validation, typically 1000-10000 liters', 'annotations': {'volume_range': '1000-10000 L', 'purpose': 'Technology demonstration and validation'}},
    "COMMERCIAL_SCALE": {'description': 'Full commercial production scale, typically greater than 10000 liters', 'annotations': {'volume_range': '>10000 L', 'purpose': 'Commercial manufacturing'}},
    "MICRO_SCALE": {'description': 'Micro-scale operations using microfluidic or microtiter plate formats, typically less than 1 mL', 'annotations': {'volume_range': '<1 mL', 'purpose': 'High-throughput screening and optimization'}},
}

class BioproductCategoryType(RichEnum):
    """
    Categories of products derived from biological manufacturing processes
    """
    # Enum members
    BIOFUEL = "BIOFUEL"
    BIOCHEMICAL = "BIOCHEMICAL"
    BIOPLASTIC = "BIOPLASTIC"
    BIOSURFACTANT = "BIOSURFACTANT"
    BIOACTIVE_COMPOUND = "BIOACTIVE_COMPOUND"
    INDUSTRIAL_ENZYME = "INDUSTRIAL_ENZYME"
    BIOFERTILIZER = "BIOFERTILIZER"
    BIOPESTICIDE = "BIOPESTICIDE"
    BIOPHARMACEUTICAL = "BIOPHARMACEUTICAL"
    FOOD_INGREDIENT = "FOOD_INGREDIENT"

# Set metadata after class creation
BioproductCategoryType._metadata = {
    "BIOFUEL": {'description': 'Biologically derived fuel including ethanol, biodiesel, and biogas', 'meaning': 'CHEBI:33292'},
    "BIOCHEMICAL": {'description': 'Chemical compounds produced through biological processes', 'annotations': {'examples': 'organic acids, amino acids, platform chemicals'}},
    "BIOPLASTIC": {'description': 'Biodegradable or bio-based plastic materials such as PHA, PLA, and PBS', 'annotations': {'examples': 'polyhydroxyalkanoates, polylactic acid'}},
    "BIOSURFACTANT": {'description': 'Surface-active compounds produced by microorganisms', 'annotations': {'examples': 'rhamnolipids, sophorolipids, surfactin'}},
    "BIOACTIVE_COMPOUND": {'description': 'Biologically active compounds with therapeutic or functional properties', 'annotations': {'examples': 'alkaloids, terpenoids, flavonoids'}},
    "INDUSTRIAL_ENZYME": {'description': 'Enzymes produced for industrial applications such as detergents, textiles, and food processing', 'meaning': 'NCIT:C16554'},
    "BIOFERTILIZER": {'description': 'Biological preparations containing living microorganisms that enhance plant nutrient availability', 'meaning': 'AGRO:00020001'},
    "BIOPESTICIDE": {'description': 'Biological agents used for pest control in agriculture', 'annotations': {'examples': 'Bacillus thuringiensis, entomopathogenic fungi'}},
    "BIOPHARMACEUTICAL": {'description': 'Pharmaceutical products derived from biological sources or manufactured using biotechnology', 'meaning': 'NCIT:C307', 'annotations': {'examples': 'recombinant proteins, monoclonal antibodies, vaccines'}},
    "FOOD_INGREDIENT": {'description': 'Biologically produced ingredients for food and beverage applications', 'meaning': 'FOODON:00004274'},
}

class BioprocessOptimizationType(RichEnum):
    """
    Strategies and approaches for optimizing biomanufacturing processes to improve yield, productivity, and product quality
    """
    # Enum members
    MEDIA_OPTIMIZATION = "MEDIA_OPTIMIZATION"
    STRAIN_ENGINEERING = "STRAIN_ENGINEERING"
    PROCESS_INTENSIFICATION = "PROCESS_INTENSIFICATION"
    CONTINUOUS_PROCESSING = "CONTINUOUS_PROCESSING"
    FED_BATCH_OPTIMIZATION = "FED_BATCH_OPTIMIZATION"
    DOWNSTREAM_PURIFICATION = "DOWNSTREAM_PURIFICATION"
    IN_LINE_ANALYTICS = "IN_LINE_ANALYTICS"
    DIGITAL_TWIN_MODELING = "DIGITAL_TWIN_MODELING"

# Set metadata after class creation
BioprocessOptimizationType._metadata = {
    "MEDIA_OPTIMIZATION": {'description': 'Optimization of growth media composition including carbon sources, nitrogen sources, and micronutrients'},
    "STRAIN_ENGINEERING": {'description': 'Genetic modification and selection of production strains for improved performance', 'annotations': {'approaches': 'metabolic engineering, directed evolution, adaptive laboratory evolution'}},
    "PROCESS_INTENSIFICATION": {'description': 'Engineering approaches to increase volumetric productivity and reduce process footprint'},
    "CONTINUOUS_PROCESSING": {'description': 'Conversion from batch to continuous operation for improved efficiency and consistency'},
    "FED_BATCH_OPTIMIZATION": {'description': 'Optimization of feeding strategies in fed-batch processes to maximize product yield'},
    "DOWNSTREAM_PURIFICATION": {'description': 'Optimization of product recovery and purification processes', 'annotations': {'approaches': 'chromatography, membrane separation, extraction'}},
    "IN_LINE_ANALYTICS": {'description': 'Implementation of real-time process analytical technology (PAT) for process monitoring and control', 'annotations': {'technologies': 'Raman spectroscopy, NIR, online HPLC'}},
    "DIGITAL_TWIN_MODELING": {'description': 'Use of computational process models for simulation, prediction, and optimization', 'annotations': {'approaches': 'mechanistic models, hybrid models, machine learning'}},
}

__all__ = [
    "BiomanufacturingScaleType",
    "BioproductCategoryType",
    "BioprocessOptimizationType",
]