"""
Nuclear Facilities and Infrastructure Types

Classifications of nuclear facilities including power plants, research reactors, fuel cycle facilities, waste management facilities, and nuclear infrastructure. Based on IAEA classifications and nuclear industry standards.

Generated from: energy/nuclear/nuclear_facilities.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class NuclearFacilityTypeEnum(RichEnum):
    """
    Types of nuclear facilities and infrastructure
    """
    # Enum members
    COMMERCIAL_POWER_PLANT = "COMMERCIAL_POWER_PLANT"
    RESEARCH_REACTOR = "RESEARCH_REACTOR"
    TEST_REACTOR = "TEST_REACTOR"
    PROTOTYPE_REACTOR = "PROTOTYPE_REACTOR"
    NAVAL_REACTOR = "NAVAL_REACTOR"
    SPACE_REACTOR = "SPACE_REACTOR"
    PRODUCTION_REACTOR = "PRODUCTION_REACTOR"
    URANIUM_MINE = "URANIUM_MINE"
    URANIUM_MILL = "URANIUM_MILL"
    CONVERSION_FACILITY = "CONVERSION_FACILITY"
    ENRICHMENT_FACILITY = "ENRICHMENT_FACILITY"
    FUEL_FABRICATION_FACILITY = "FUEL_FABRICATION_FACILITY"
    REPROCESSING_FACILITY = "REPROCESSING_FACILITY"
    INTERIM_STORAGE_FACILITY = "INTERIM_STORAGE_FACILITY"
    GEOLOGICAL_REPOSITORY = "GEOLOGICAL_REPOSITORY"
    DECOMMISSIONING_SITE = "DECOMMISSIONING_SITE"
    NUCLEAR_LABORATORY = "NUCLEAR_LABORATORY"
    RADIOISOTOPE_PRODUCTION_FACILITY = "RADIOISOTOPE_PRODUCTION_FACILITY"

# Set metadata after class creation
NuclearFacilityTypeEnum._metadata = {
    "COMMERCIAL_POWER_PLANT": {'description': 'Large-scale commercial reactor for electricity generation', 'annotations': {'primary_purpose': 'electricity generation', 'power_output': 'typically 300-1600 MWe', 'operator_type': 'utility company', 'regulatory_oversight': 'extensive'}},
    "RESEARCH_REACTOR": {'description': 'Reactor designed for research, training, and isotope production', 'annotations': {'primary_purpose': 'research, training, isotope production', 'power_output': 'typically <100 MWt', 'neutron_flux': 'optimized for research needs', 'fuel_type': 'various, often HEU or LEU'}},
    "TEST_REACTOR": {'description': 'Reactor for testing materials and components', 'annotations': {'primary_purpose': 'materials and component testing', 'test_capabilities': 'irradiation testing', 'neutron_spectrum': 'variable for testing needs'}},
    "PROTOTYPE_REACTOR": {'description': 'Reactor for demonstrating new technology', 'annotations': {'primary_purpose': 'technology demonstration', 'scale': 'smaller than commercial', 'innovation_focus': 'new reactor concepts'}},
    "NAVAL_REACTOR": {'description': 'Reactor for ship or submarine propulsion', 'annotations': {'primary_purpose': 'vessel propulsion', 'compactness': 'highly compact design', 'fuel_enrichment': 'typically HEU', 'operation_mode': 'mobile platform'}},
    "SPACE_REACTOR": {'description': 'Reactor designed for space applications', 'annotations': {'primary_purpose': 'space power or propulsion', 'mass_constraints': 'extremely lightweight', 'cooling': 'radiative cooling', 'power_output': 'typically <10 MWt'}},
    "PRODUCTION_REACTOR": {'description': 'Reactor for producing nuclear materials', 'annotations': {'primary_purpose': 'isotope or material production', 'products': 'tritium, plutonium, medical isotopes', 'operation_mode': 'specialized for production'}},
    "URANIUM_MINE": {'description': 'Facility for extracting uranium ore', 'annotations': {'extraction_method': 'underground or open pit', 'product': 'uranium ore', 'processing': 'may include milling'}},
    "URANIUM_MILL": {'description': 'Facility for processing uranium ore into yellowcake', 'annotations': {'input_material': 'uranium ore', 'output_product': 'uranium concentrate (U3O8)', 'process': 'chemical extraction and purification'}},
    "CONVERSION_FACILITY": {'description': 'Facility for converting yellowcake to UF6', 'annotations': {'input_material': 'uranium concentrate (U3O8)', 'output_product': 'uranium hexafluoride (UF6)', 'process': 'chemical conversion'}},
    "ENRICHMENT_FACILITY": {'description': 'Facility for increasing U-235 concentration', 'annotations': {'input_material': 'natural UF6', 'output_product': 'enriched UF6', 'process': 'isotope separation (centrifuge, diffusion)', 'sensitive_technology': 'proliferation-sensitive'}},
    "FUEL_FABRICATION_FACILITY": {'description': 'Facility for manufacturing nuclear fuel assemblies', 'annotations': {'input_material': 'enriched UF6', 'output_product': 'fuel assemblies', 'process': 'pellet and rod manufacturing'}},
    "REPROCESSING_FACILITY": {'description': 'Facility for separating spent fuel components', 'annotations': {'input_material': 'spent nuclear fuel', 'output_products': 'uranium, plutonium, waste', 'process': 'chemical separation (PUREX, UREX+)', 'proliferation_sensitivity': 'high'}},
    "INTERIM_STORAGE_FACILITY": {'description': 'Facility for temporary storage of nuclear materials', 'annotations': {'storage_duration': 'intermediate term (5-100 years)', 'storage_medium': 'pools, dry casks', 'typical_materials': 'spent fuel, waste'}},
    "GEOLOGICAL_REPOSITORY": {'description': 'Deep underground facility for permanent waste disposal', 'annotations': {'storage_duration': 'permanent (thousands of years)', 'depth': 'typically >300 meters underground', 'waste_types': 'high-level waste, spent fuel'}},
    "DECOMMISSIONING_SITE": {'description': 'Nuclear facility undergoing dismantlement', 'annotations': {'facility_status': 'being dismantled', 'activities': 'decontamination, demolition', 'duration': 'typically 10-50 years'}},
    "NUCLEAR_LABORATORY": {'description': 'Laboratory facility handling radioactive materials', 'annotations': {'activities': 'research, analysis, small-scale production', 'materials': 'various radioactive substances', 'scale': 'laboratory scale'}},
    "RADIOISOTOPE_PRODUCTION_FACILITY": {'description': 'Facility for producing medical and industrial isotopes', 'annotations': {'products': 'medical isotopes, industrial tracers', 'production_methods': 'reactor irradiation, accelerator', 'market': 'medical and industrial applications'}},
}

class PowerPlantStatusEnum(RichEnum):
    """
    Operational status of nuclear power plants
    """
    # Enum members
    UNDER_CONSTRUCTION = "UNDER_CONSTRUCTION"
    COMMISSIONING = "COMMISSIONING"
    COMMERCIAL_OPERATION = "COMMERCIAL_OPERATION"
    REFUELING_OUTAGE = "REFUELING_OUTAGE"
    EXTENDED_OUTAGE = "EXTENDED_OUTAGE"
    PERMANENTLY_SHUTDOWN = "PERMANENTLY_SHUTDOWN"
    DECOMMISSIONING = "DECOMMISSIONING"
    DECOMMISSIONED = "DECOMMISSIONED"

# Set metadata after class creation
PowerPlantStatusEnum._metadata = {
    "UNDER_CONSTRUCTION": {'description': 'Plant currently being built', 'annotations': {'construction_phase': 'civil and mechanical work ongoing', 'licensing_status': 'construction permit issued', 'commercial_operation': 'not yet started'}},
    "COMMISSIONING": {'description': 'Plant undergoing testing before commercial operation', 'annotations': {'testing_phase': 'systems testing and startup', 'fuel_loading': 'may have occurred', 'commercial_operation': 'not yet achieved'}},
    "COMMERCIAL_OPERATION": {'description': 'Plant operating commercially for electricity generation', 'annotations': {'operational_status': 'fully operational', 'power_generation': 'commercial electricity production', 'licensing_status': 'operating license active'}},
    "REFUELING_OUTAGE": {'description': 'Plant temporarily shut down for fuel replacement and maintenance', 'annotations': {'shutdown_reason': 'scheduled refueling', 'duration': 'typically 30-60 days', 'activities': 'fuel replacement, maintenance, inspection'}},
    "EXTENDED_OUTAGE": {'description': 'Plant shut down for extended period for major work', 'annotations': {'shutdown_duration': 'months to years', 'work_scope': 'major modifications or repairs', 'return_to_service': 'planned'}},
    "PERMANENTLY_SHUTDOWN": {'description': 'Plant permanently ceased operation', 'annotations': {'operational_status': 'permanently ceased', 'fuel_removal': 'may be ongoing or completed', 'decommissioning': 'may be planned or ongoing'}},
    "DECOMMISSIONING": {'description': 'Plant undergoing dismantlement', 'annotations': {'decommissioning_phase': 'active dismantlement', 'radioactive_cleanup': 'ongoing', 'site_restoration': 'planned'}},
    "DECOMMISSIONED": {'description': 'Plant completely dismantled and site restored', 'annotations': {'dismantlement_status': 'completed', 'site_condition': 'restored for unrestricted use', 'radioactive_materials': 'removed'}},
}

class ResearchReactorTypeEnum(RichEnum):
    """
    Types of research reactors
    """
    # Enum members
    POOL_TYPE = "POOL_TYPE"
    TANK_TYPE = "TANK_TYPE"
    HOMOGENEOUS = "HOMOGENEOUS"
    FAST_RESEARCH_REACTOR = "FAST_RESEARCH_REACTOR"
    PULSED_REACTOR = "PULSED_REACTOR"
    CRITICAL_ASSEMBLY = "CRITICAL_ASSEMBLY"
    SUBCRITICAL_ASSEMBLY = "SUBCRITICAL_ASSEMBLY"

# Set metadata after class creation
ResearchReactorTypeEnum._metadata = {
    "POOL_TYPE": {'description': 'Reactor with fuel in open pool of water', 'annotations': {'design': 'open pool with underwater fuel', 'power_level': 'typically 1-20 MW', 'applications': 'neutron beam experiments, training'}},
    "TANK_TYPE": {'description': 'Reactor with fuel in enclosed tank', 'annotations': {'design': 'fuel in pressurized or unpressurized tank', 'power_level': 'variable', 'containment': 'more enclosed than pool type'}},
    "HOMOGENEOUS": {'description': 'Reactor with fuel in liquid form', 'annotations': {'fuel_form': 'aqueous solution', 'design': 'fuel dissolved in moderator', 'power_level': 'typically low'}},
    "FAST_RESEARCH_REACTOR": {'description': 'Research reactor using fast neutrons', 'annotations': {'neutron_spectrum': 'fast neutrons', 'moderator': 'none or minimal', 'applications': 'fast neutron research'}},
    "PULSED_REACTOR": {'description': 'Reactor designed for pulsed operation', 'annotations': {'operation_mode': 'short intense pulses', 'power_level': 'very high peak power', 'applications': 'transient testing, physics research'}},
    "CRITICAL_ASSEMBLY": {'description': 'Minimal reactor for criticality studies', 'annotations': {'power_level': 'essentially zero', 'purpose': 'criticality experiments, training', 'design': 'minimal critical configuration'}},
    "SUBCRITICAL_ASSEMBLY": {'description': 'Neutron source-driven subcritical system', 'annotations': {'criticality': 'subcritical', 'neutron_source': 'external source required', 'applications': 'research, training, transmutation studies'}},
}

class FuelCycleFacilityTypeEnum(RichEnum):
    """
    Types of nuclear fuel cycle facilities
    """
    # Enum members
    IN_SITU_LEACH_MINE = "IN_SITU_LEACH_MINE"
    CONVENTIONAL_MINE = "CONVENTIONAL_MINE"
    HEAP_LEACH_FACILITY = "HEAP_LEACH_FACILITY"
    GASEOUS_DIFFUSION_PLANT = "GASEOUS_DIFFUSION_PLANT"
    GAS_CENTRIFUGE_PLANT = "GAS_CENTRIFUGE_PLANT"
    LASER_ENRICHMENT_FACILITY = "LASER_ENRICHMENT_FACILITY"
    MOX_FUEL_FABRICATION = "MOX_FUEL_FABRICATION"
    AQUEOUS_REPROCESSING = "AQUEOUS_REPROCESSING"
    PYROPROCESSING_FACILITY = "PYROPROCESSING_FACILITY"

# Set metadata after class creation
FuelCycleFacilityTypeEnum._metadata = {
    "IN_SITU_LEACH_MINE": {'description': 'Uranium extraction by solution mining', 'annotations': {'extraction_method': 'chemical leaching in ground', 'environmental_impact': 'lower surface disturbance', 'geology_requirement': 'permeable ore deposits'}},
    "CONVENTIONAL_MINE": {'description': 'Traditional underground or open-pit uranium mining', 'annotations': {'extraction_method': 'physical excavation', 'mine_types': 'underground or open pit', 'ore_grade': 'variable'}},
    "HEAP_LEACH_FACILITY": {'description': 'Uranium extraction from low-grade ores by heap leaching', 'annotations': {'ore_grade': 'low-grade ores', 'process': 'chemical leaching of ore piles', 'economics': 'cost-effective for low grades'}},
    "GASEOUS_DIFFUSION_PLANT": {'description': 'Uranium enrichment using gaseous diffusion', 'annotations': {'enrichment_method': 'gaseous diffusion', 'energy_consumption': 'very high', 'status': 'mostly retired technology'}},
    "GAS_CENTRIFUGE_PLANT": {'description': 'Uranium enrichment using centrifuge technology', 'annotations': {'enrichment_method': 'gas centrifuge', 'energy_consumption': 'lower than diffusion', 'technology_status': 'current standard technology'}},
    "LASER_ENRICHMENT_FACILITY": {'description': 'Uranium enrichment using laser isotope separation', 'annotations': {'enrichment_method': 'laser isotope separation', 'technology_status': 'under development', 'energy_consumption': 'potentially lower'}},
    "MOX_FUEL_FABRICATION": {'description': 'Facility for manufacturing mixed oxide fuel', 'annotations': {'fuel_type': 'mixed oxide (uranium and plutonium)', 'input_materials': 'plutonium dioxide, uranium dioxide', 'special_handling': 'plutonium handling required'}},
    "AQUEOUS_REPROCESSING": {'description': 'Spent fuel reprocessing using aqueous methods', 'annotations': {'process_type': 'PUREX or similar aqueous process', 'separation_products': 'uranium, plutonium, waste', 'technology_maturity': 'commercially proven'}},
    "PYROPROCESSING_FACILITY": {'description': 'Spent fuel reprocessing using electrochemical methods', 'annotations': {'process_type': 'electrochemical separation', 'temperature': 'high temperature operation', 'technology_status': 'under development'}},
}

class WasteFacilityTypeEnum(RichEnum):
    """
    Types of nuclear waste management facilities
    """
    # Enum members
    SPENT_FUEL_POOL = "SPENT_FUEL_POOL"
    DRY_CASK_STORAGE = "DRY_CASK_STORAGE"
    CENTRALIZED_INTERIM_STORAGE = "CENTRALIZED_INTERIM_STORAGE"
    LOW_LEVEL_WASTE_DISPOSAL = "LOW_LEVEL_WASTE_DISPOSAL"
    GREATER_THAN_CLASS_C_STORAGE = "GREATER_THAN_CLASS_C_STORAGE"
    TRANSURANIC_WASTE_REPOSITORY = "TRANSURANIC_WASTE_REPOSITORY"
    HIGH_LEVEL_WASTE_REPOSITORY = "HIGH_LEVEL_WASTE_REPOSITORY"
    WASTE_TREATMENT_FACILITY = "WASTE_TREATMENT_FACILITY"
    DECONTAMINATION_FACILITY = "DECONTAMINATION_FACILITY"

# Set metadata after class creation
WasteFacilityTypeEnum._metadata = {
    "SPENT_FUEL_POOL": {'description': 'Water-filled pool for cooling spent fuel', 'annotations': {'cooling_medium': 'water', 'location': 'typically at reactor site', 'storage_duration': '5-10 years typical'}},
    "DRY_CASK_STORAGE": {'description': 'Air-cooled storage in sealed containers', 'annotations': {'cooling_medium': 'air circulation', 'storage_duration': '20-100 years', 'location': 'on-site or centralized'}},
    "CENTRALIZED_INTERIM_STORAGE": {'description': 'Large-scale interim storage away from reactor sites', 'annotations': {'scale': "multiple reactor's worth of fuel", 'storage_duration': 'decades', 'transportation': 'rail or truck access required'}},
    "LOW_LEVEL_WASTE_DISPOSAL": {'description': 'Near-surface disposal for low-level waste', 'annotations': {'waste_category': 'Class A, B, C low-level waste', 'disposal_depth': 'near-surface (<30 meters)', 'institutional_control': '100 years minimum'}},
    "GREATER_THAN_CLASS_C_STORAGE": {'description': 'Storage for waste exceeding Class C limits', 'annotations': {'waste_category': 'greater than Class C waste', 'storage_type': 'interim storage pending disposal', 'disposal_requirements': 'deep disposal likely required'}},
    "TRANSURANIC_WASTE_REPOSITORY": {'description': 'Deep geological repository for TRU waste', 'annotations': {'waste_category': 'transuranic waste', 'disposal_depth': 'deep underground', 'example': 'Waste Isolation Pilot Plant (WIPP)'}},
    "HIGH_LEVEL_WASTE_REPOSITORY": {'description': 'Deep geological repository for high-level waste', 'annotations': {'waste_category': 'high-level waste, spent fuel', 'disposal_depth': 'typically >300 meters', 'containment_period': 'thousands of years'}},
    "WASTE_TREATMENT_FACILITY": {'description': 'Facility for processing and conditioning waste', 'annotations': {'purpose': 'volume reduction, stabilization', 'processes': 'incineration, compaction, solidification', 'output': 'treated waste for disposal'}},
    "DECONTAMINATION_FACILITY": {'description': 'Facility for cleaning contaminated materials', 'annotations': {'purpose': 'remove radioactive contamination', 'materials': 'equipment, clothing, tools', 'methods': 'chemical, physical decontamination'}},
}

class NuclearShipTypeEnum(RichEnum):
    """
    Types of nuclear-powered vessels
    """
    # Enum members
    AIRCRAFT_CARRIER = "AIRCRAFT_CARRIER"
    SUBMARINE = "SUBMARINE"
    CRUISER = "CRUISER"
    ICEBREAKER = "ICEBREAKER"
    MERCHANT_SHIP = "MERCHANT_SHIP"
    RESEARCH_VESSEL = "RESEARCH_VESSEL"

# Set metadata after class creation
NuclearShipTypeEnum._metadata = {
    "AIRCRAFT_CARRIER": {'description': 'Large naval vessel with nuclear propulsion and aircraft operations', 'annotations': {'propulsion': 'nuclear steam turbine', 'size': 'very large (>80,000 tons)', 'mission': 'power projection, aircraft operations', 'reactor_count': 'typically 2'}},
    "SUBMARINE": {'description': 'Underwater vessel with nuclear propulsion', 'annotations': {'propulsion': 'nuclear steam turbine', 'operational_environment': 'submerged', 'mission': 'various (attack, ballistic missile, cruise missile)', 'reactor_count': 'typically 1'}},
    "CRUISER": {'description': 'Large surface combatant with nuclear propulsion', 'annotations': {'propulsion': 'nuclear steam turbine', 'mission': 'escort, surface warfare', 'size': 'large surface vessel', 'status': 'mostly retired'}},
    "ICEBREAKER": {'description': 'Vessel designed to break ice using nuclear power', 'annotations': {'propulsion': 'nuclear steam turbine or electric', 'mission': 'ice breaking, Arctic operations', 'operational_environment': 'polar regions', 'reactor_count': '1-3'}},
    "MERCHANT_SHIP": {'description': 'Commercial cargo vessel with nuclear propulsion', 'annotations': {'propulsion': 'nuclear steam turbine', 'mission': 'cargo transport', 'commercial_viability': 'limited due to costs', 'examples': 'NS Savannah, few others'}},
    "RESEARCH_VESSEL": {'description': 'Ship designed for oceanographic research with nuclear power', 'annotations': {'propulsion': 'nuclear', 'mission': 'scientific research', 'duration': 'extended operations without refueling', 'examples': 'limited number built'}},
}

__all__ = [
    "NuclearFacilityTypeEnum",
    "PowerPlantStatusEnum",
    "ResearchReactorTypeEnum",
    "FuelCycleFacilityTypeEnum",
    "WasteFacilityTypeEnum",
    "NuclearShipTypeEnum",
]