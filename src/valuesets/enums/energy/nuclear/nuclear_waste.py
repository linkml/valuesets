"""
Nuclear Waste Classifications

Classifications of radioactive waste based on IAEA standards, NRC 10 CFR 61 classifications, and international waste management standards. Includes activity levels, disposal requirements, and time scales.

Generated from: energy/nuclear/nuclear_waste.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class IAEAWasteClassificationEnum(RichEnum):
    """
    IAEA General Safety Requirements radioactive waste classification scheme
    """
    # Enum members
    EXEMPT_WASTE = "EXEMPT_WASTE"
    VERY_SHORT_LIVED_WASTE = "VERY_SHORT_LIVED_WASTE"
    VERY_LOW_LEVEL_WASTE = "VERY_LOW_LEVEL_WASTE"
    LOW_LEVEL_WASTE = "LOW_LEVEL_WASTE"
    INTERMEDIATE_LEVEL_WASTE = "INTERMEDIATE_LEVEL_WASTE"
    HIGH_LEVEL_WASTE = "HIGH_LEVEL_WASTE"

# Set metadata after class creation
IAEAWasteClassificationEnum._metadata = {
    "EXEMPT_WASTE": {'description': 'Waste with negligible radioactivity requiring no regulatory control', 'annotations': {'regulatory_control': 'none required', 'clearance': 'can be cleared from regulatory control', 'disposal': 'as ordinary waste', 'activity_level': 'negligible'}, 'aliases': ['EW']},
    "VERY_SHORT_LIVED_WASTE": {'description': 'Waste stored for decay to exempt levels within few years', 'annotations': {'storage_period': 'up to few years', 'decay_strategy': 'storage for decay', 'clearance': 'after decay period', 'typical_sources': 'medical, research isotopes'}, 'aliases': ['VSLW']},
    "VERY_LOW_LEVEL_WASTE": {'description': 'Waste requiring limited containment and isolation', 'annotations': {'containment_requirement': 'limited', 'disposal': 'near-surface landfill-type', 'activity_level': 'very low but above exempt', 'isolation_period': 'limited'}, 'aliases': ['VLLW']},
    "LOW_LEVEL_WASTE": {'description': 'Waste requiring containment for up to hundreds of years', 'annotations': {'containment_period': 'up to few hundred years', 'disposal': 'near-surface disposal', 'activity_level': 'low', 'heat_generation': 'negligible'}, 'aliases': ['LLW']},
    "INTERMEDIATE_LEVEL_WASTE": {'description': 'Waste requiring containment for thousands of years', 'annotations': {'containment_period': 'up to thousands of years', 'disposal': 'geological disposal', 'activity_level': 'intermediate', 'heat_generation': 'low (<2 kW/m³)', 'shielding': 'required'}, 'aliases': ['ILW']},
    "HIGH_LEVEL_WASTE": {'description': 'Waste requiring containment for thousands to hundreds of thousands of years', 'annotations': {'containment_period': 'thousands to hundreds of thousands of years', 'disposal': 'geological disposal', 'activity_level': 'high', 'heat_generation': 'significant (>2 kW/m³)', 'cooling': 'required', 'shielding': 'heavy shielding required'}, 'aliases': ['HLW']},
}

class NRCWasteClassEnum(RichEnum):
    """
    US NRC 10 CFR 61 low-level radioactive waste classification
    """
    # Enum members
    CLASS_A = "CLASS_A"
    CLASS_B = "CLASS_B"
    CLASS_C = "CLASS_C"
    GREATER_THAN_CLASS_C = "GREATER_THAN_CLASS_C"

# Set metadata after class creation
NRCWasteClassEnum._metadata = {
    "CLASS_A": {'description': 'Lowest radioactivity waste suitable for shallow land burial', 'annotations': {'disposal_method': 'shallow land burial', 'segregation_requirements': 'minimal', 'waste_form_requirements': 'none', 'typical_sources': 'medical, industrial, power plants', 'concentration_limits': 'lowest of three classes'}},
    "CLASS_B": {'description': 'Intermediate radioactivity requiring waste form stability', 'annotations': {'disposal_method': 'shallow land burial', 'segregation_requirements': 'from Class A', 'waste_form_requirements': 'structural stability', 'institutional_control': '100 years minimum', 'concentration_limits': 'intermediate'}},
    "CLASS_C": {'description': 'Highest concentration suitable for shallow land burial', 'annotations': {'disposal_method': 'shallow land burial', 'segregation_requirements': 'enhanced', 'waste_form_requirements': 'structural stability', 'institutional_control': '100 years minimum', 'intruder_barriers': 'required', 'concentration_limits': 'highest for shallow burial'}},
    "GREATER_THAN_CLASS_C": {'description': 'Waste exceeding Class C limits, generally unsuitable for shallow burial', 'annotations': {'disposal_method': 'case-by-case evaluation', 'shallow_burial': 'generally not acceptable', 'deep_disposal': 'may be required', 'nrc_evaluation': 'required', 'concentration_limits': 'exceeds Class C'}, 'aliases': ['GTCC']},
}

class WasteHeatGenerationEnum(RichEnum):
    """
    Heat generation categories for radioactive waste
    """
    # Enum members
    NEGLIGIBLE_HEAT = "NEGLIGIBLE_HEAT"
    LOW_HEAT = "LOW_HEAT"
    HIGH_HEAT = "HIGH_HEAT"

# Set metadata after class creation
WasteHeatGenerationEnum._metadata = {
    "NEGLIGIBLE_HEAT": {'description': 'Waste generating negligible heat', 'annotations': {'heat_output': '<0.1 kW/m³', 'cooling_required': False, 'thermal_consideration': 'minimal'}},
    "LOW_HEAT": {'description': 'Waste generating low but measurable heat', 'annotations': {'heat_output': '0.1-2 kW/m³', 'cooling_required': 'minimal', 'thermal_consideration': 'some design consideration'}},
    "HIGH_HEAT": {'description': 'Waste generating significant heat requiring thermal management', 'annotations': {'heat_output': '>2 kW/m³', 'cooling_required': True, 'thermal_consideration': 'major design factor', 'typical_waste': 'spent nuclear fuel, HLW glass'}},
}

class WasteHalfLifeCategoryEnum(RichEnum):
    """
    Half-life categories for radioactive waste classification
    """
    # Enum members
    VERY_SHORT_LIVED = "VERY_SHORT_LIVED"
    SHORT_LIVED = "SHORT_LIVED"
    LONG_LIVED = "LONG_LIVED"

# Set metadata after class creation
WasteHalfLifeCategoryEnum._metadata = {
    "VERY_SHORT_LIVED": {'description': 'Radionuclides with very short half-lives', 'annotations': {'half_life_range': 'seconds to days', 'decay_strategy': 'storage for decay', 'typical_examples': 'medical isotopes, some activation products'}},
    "SHORT_LIVED": {'description': 'Radionuclides with short half-lives', 'annotations': {'half_life_range': '<30 years', 'containment_period': 'hundreds of years', 'decay_significance': 'significant over containment period'}},
    "LONG_LIVED": {'description': 'Radionuclides with long half-lives', 'annotations': {'half_life_range': '>30 years', 'containment_period': 'thousands to millions of years', 'decay_significance': 'minimal over human timescales', 'examples': 'actinides, some fission products'}},
}

class WasteDisposalMethodEnum(RichEnum):
    """
    Methods for radioactive waste disposal
    """
    # Enum members
    CLEARANCE = "CLEARANCE"
    DECAY_STORAGE = "DECAY_STORAGE"
    NEAR_SURFACE_DISPOSAL = "NEAR_SURFACE_DISPOSAL"
    GEOLOGICAL_DISPOSAL = "GEOLOGICAL_DISPOSAL"
    BOREHOLE_DISPOSAL = "BOREHOLE_DISPOSAL"
    TRANSMUTATION = "TRANSMUTATION"

# Set metadata after class creation
WasteDisposalMethodEnum._metadata = {
    "CLEARANCE": {'description': 'Release from regulatory control as ordinary waste', 'annotations': {'regulatory_oversight': 'none after clearance', 'waste_category': 'exempt waste', 'disposal_location': 'conventional facilities'}},
    "DECAY_STORAGE": {'description': 'Storage for radioactive decay to exempt levels', 'annotations': {'storage_duration': 'typically <10 years', 'waste_category': 'very short-lived waste', 'final_disposal': 'as ordinary waste after decay'}},
    "NEAR_SURFACE_DISPOSAL": {'description': 'Disposal in engineered near-surface facilities', 'annotations': {'depth': 'typically <30 meters', 'waste_categories': 'VLLW, LLW, some ILW', 'institutional_control': '100-300 years', 'barriers': 'engineered barriers'}},
    "GEOLOGICAL_DISPOSAL": {'description': 'Deep underground disposal in stable geological formations', 'annotations': {'depth': 'typically >300 meters', 'waste_categories': 'HLW, long-lived ILW, spent fuel', 'containment_period': 'thousands to millions of years', 'barriers': 'multiple barriers including geology'}},
    "BOREHOLE_DISPOSAL": {'description': 'Disposal in deep boreholes', 'annotations': {'depth': '1-5 kilometers', 'waste_categories': 'disused sealed sources, some HLW', 'isolation': 'extreme depth isolation'}},
    "TRANSMUTATION": {'description': 'Nuclear transformation to shorter-lived or stable isotopes', 'annotations': {'method': 'accelerator-driven systems or fast reactors', 'waste_categories': 'long-lived actinides', 'status': 'research and development'}},
}

class WasteSourceEnum(RichEnum):
    """
    Sources of radioactive waste generation
    """
    # Enum members
    NUCLEAR_POWER_PLANTS = "NUCLEAR_POWER_PLANTS"
    MEDICAL_APPLICATIONS = "MEDICAL_APPLICATIONS"
    INDUSTRIAL_APPLICATIONS = "INDUSTRIAL_APPLICATIONS"
    RESEARCH_FACILITIES = "RESEARCH_FACILITIES"
    NUCLEAR_WEAPONS_PROGRAM = "NUCLEAR_WEAPONS_PROGRAM"
    DECOMMISSIONING = "DECOMMISSIONING"
    URANIUM_MINING = "URANIUM_MINING"
    FUEL_CYCLE_FACILITIES = "FUEL_CYCLE_FACILITIES"

# Set metadata after class creation
WasteSourceEnum._metadata = {
    "NUCLEAR_POWER_PLANTS": {'description': 'Waste from commercial nuclear power generation', 'annotations': {'waste_types': 'spent fuel, operational waste, decommissioning waste', 'volume_fraction': 'largest single source', 'waste_classes': 'all classes including HLW'}},
    "MEDICAL_APPLICATIONS": {'description': 'Waste from nuclear medicine and radiotherapy', 'annotations': {'waste_types': 'short-lived medical isotopes, sealed sources', 'typical_classification': 'Class A, VSLW', 'decay_strategy': 'often storage for decay'}},
    "INDUSTRIAL_APPLICATIONS": {'description': 'Waste from industrial use of radioactive materials', 'annotations': {'applications': 'gauging, radiography, sterilization', 'waste_types': 'sealed sources, contaminated equipment', 'typical_classification': 'Class A and B'}},
    "RESEARCH_FACILITIES": {'description': 'Waste from research reactors and laboratories', 'annotations': {'waste_types': 'activation products, contaminated materials', 'typical_classification': 'Class A, B, and C', 'fuel_type': 'often HEU spent fuel'}},
    "NUCLEAR_WEAPONS_PROGRAM": {'description': 'Waste from defense nuclear activities', 'annotations': {'waste_types': 'TRU waste, HLW, contaminated equipment', 'legacy_waste': 'significant volumes from past activities', 'classification': 'all classes including TRU'}},
    "DECOMMISSIONING": {'description': 'Waste from dismantling nuclear facilities', 'annotations': {'waste_types': 'activated concrete, contaminated metal', 'volume': 'large volumes of VLLW and LLW', 'activity_level': 'generally low level'}},
    "URANIUM_MINING": {'description': 'Waste from uranium extraction and processing', 'annotations': {'waste_types': 'tailings, contaminated equipment', 'volume': 'very large volumes', 'activity_level': 'naturally occurring radioactivity'}},
    "FUEL_CYCLE_FACILITIES": {'description': 'Waste from fuel fabrication, enrichment, and reprocessing', 'annotations': {'waste_types': 'contaminated equipment, process waste', 'classification': 'variable depending on process', 'uranium_content': 'often contains enriched uranium'}},
}

class TransuranicWasteCategoryEnum(RichEnum):
    """
    Transuranic waste classifications (US system)
    """
    # Enum members
    CONTACT_HANDLED_TRU = "CONTACT_HANDLED_TRU"
    REMOTE_HANDLED_TRU = "REMOTE_HANDLED_TRU"
    TRU_MIXED_WASTE = "TRU_MIXED_WASTE"

# Set metadata after class creation
TransuranicWasteCategoryEnum._metadata = {
    "CONTACT_HANDLED_TRU": {'description': 'TRU waste with surface dose rate ≤200 mrem/hr', 'annotations': {'dose_rate': '≤200 mrem/hr at surface', 'handling': 'direct contact possible with protection', 'disposal': 'geological repository (WIPP)', 'plutonium_content': '>100 nCi/g'}, 'aliases': ['CH-TRU']},
    "REMOTE_HANDLED_TRU": {'description': 'TRU waste with surface dose rate >200 mrem/hr', 'annotations': {'dose_rate': '>200 mrem/hr at surface', 'handling': 'remote handling required', 'disposal': 'geological repository with additional shielding', 'plutonium_content': '>100 nCi/g'}, 'aliases': ['RH-TRU']},
    "TRU_MIXED_WASTE": {'description': 'TRU waste also containing hazardous chemical components', 'annotations': {'regulation': 'both radiological and chemical hazard regulations', 'treatment': 'may require chemical treatment before disposal', 'disposal': 'geological repository after treatment', 'complexity': 'dual regulatory framework'}},
}

__all__ = [
    "IAEAWasteClassificationEnum",
    "NRCWasteClassEnum",
    "WasteHeatGenerationEnum",
    "WasteHalfLifeCategoryEnum",
    "WasteDisposalMethodEnum",
    "WasteSourceEnum",
    "TransuranicWasteCategoryEnum",
]