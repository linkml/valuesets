"""
Nuclear Fuel Types and Classifications

Classifications of nuclear fuel types including uranium enrichment levels, fuel forms, and alternative fuel cycles. Based on IAEA classifications, nuclear fuel cycle standards, and industry specifications.

Generated from: energy/nuclear/nuclear_fuels.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class NuclearFuelTypeEnum(RichEnum):
    """
    Types of nuclear fuel materials and compositions
    """
    # Enum members
    NATURAL_URANIUM = "NATURAL_URANIUM"
    LOW_ENRICHED_URANIUM = "LOW_ENRICHED_URANIUM"
    HIGH_ASSAY_LEU = "HIGH_ASSAY_LEU"
    HIGHLY_ENRICHED_URANIUM = "HIGHLY_ENRICHED_URANIUM"
    WEAPONS_GRADE_URANIUM = "WEAPONS_GRADE_URANIUM"
    REACTOR_GRADE_PLUTONIUM = "REACTOR_GRADE_PLUTONIUM"
    WEAPONS_GRADE_PLUTONIUM = "WEAPONS_GRADE_PLUTONIUM"
    MOX_FUEL = "MOX_FUEL"
    THORIUM_FUEL = "THORIUM_FUEL"
    TRISO_FUEL = "TRISO_FUEL"
    LIQUID_FUEL = "LIQUID_FUEL"
    METALLIC_FUEL = "METALLIC_FUEL"
    CARBIDE_FUEL = "CARBIDE_FUEL"
    NITRIDE_FUEL = "NITRIDE_FUEL"

# Set metadata after class creation
NuclearFuelTypeEnum._metadata = {
    "NATURAL_URANIUM": {'description': 'Uranium as found in nature (0.711% U-235)', 'meaning': 'CHEBI:27214', 'annotations': {'u235_content': '0.711%', 'u238_content': '99.289%', 'enrichment_required': False, 'typical_use': 'PHWR, some research reactors'}, 'aliases': ['Natural U', 'Unat', 'uranium atom']},
    "LOW_ENRICHED_URANIUM": {'description': 'Uranium enriched to 0.7%-20% U-235', 'annotations': {'u235_content': '0.7-20%', 'proliferation_risk': 'low', 'typical_use': 'commercial power reactors', 'iaea_category': 'indirect use material'}, 'aliases': ['LEU']},
    "HIGH_ASSAY_LEU": {'description': 'Uranium enriched to 5%-20% U-235', 'annotations': {'u235_content': '5-20%', 'typical_use': 'advanced reactors, SMRs', 'proliferation_risk': 'moderate'}, 'aliases': ['HALEU', 'LEU+']},
    "HIGHLY_ENRICHED_URANIUM": {'description': 'Uranium enriched to 20% or more U-235', 'annotations': {'u235_content': '≥20%', 'proliferation_risk': 'high', 'typical_use': 'research reactors, naval propulsion', 'iaea_category': 'direct use material'}, 'aliases': ['HEU']},
    "WEAPONS_GRADE_URANIUM": {'description': 'Uranium enriched to 90% or more U-235', 'annotations': {'u235_content': '≥90%', 'proliferation_risk': 'very high', 'typical_use': 'nuclear weapons, some naval reactors'}, 'aliases': ['WGU']},
    "REACTOR_GRADE_PLUTONIUM": {'description': 'Plutonium with high Pu-240 content from spent fuel', 'annotations': {'pu239_content': '<93%', 'pu240_content': '>7%', 'source': 'spent nuclear fuel', 'typical_use': 'MOX fuel'}, 'aliases': ['RGPu']},
    "WEAPONS_GRADE_PLUTONIUM": {'description': 'Plutonium with low Pu-240 content', 'annotations': {'pu239_content': '≥93%', 'pu240_content': '<7%', 'proliferation_risk': 'very high'}, 'aliases': ['WGPu']},
    "MOX_FUEL": {'description': 'Mixture of plutonium and uranium oxides', 'annotations': {'composition': 'UO2 + PuO2', 'plutonium_content': '3-10%', 'typical_use': 'thermal reactors', 'recycling': 'enables plutonium recycling'}, 'aliases': ['MOX', 'Mixed Oxide']},
    "THORIUM_FUEL": {'description': 'Fuel containing thorium-232 as fertile material', 'meaning': 'CHEBI:33385', 'annotations': {'fertile_isotope': 'Th-232', 'fissile_product': 'U-233', 'abundance': 'more abundant than uranium', 'proliferation_resistance': 'high'}, 'aliases': ['Thorium fuel', 'thorium']},
    "TRISO_FUEL": {'description': 'Coated particle fuel with multiple containment layers', 'annotations': {'form': 'coated particles', 'containment_layers': 4, 'meltdown_resistance': 'very high', 'typical_use': 'HTGR, some SMRs'}, 'aliases': ['TRISO']},
    "LIQUID_FUEL": {'description': 'Fuel dissolved in liquid medium', 'annotations': {'phase': 'liquid', 'typical_use': 'molten salt reactors', 'reprocessing': 'online'}},
    "METALLIC_FUEL": {'description': 'Fuel in metallic form', 'annotations': {'form': 'metal alloy', 'typical_use': 'fast reactors', 'thermal_conductivity': 'high'}},
    "CARBIDE_FUEL": {'description': 'Uranium or plutonium carbide fuel', 'annotations': {'chemical_form': 'carbide', 'melting_point': 'very high', 'typical_use': 'advanced reactors'}},
    "NITRIDE_FUEL": {'description': 'Uranium or plutonium nitride fuel', 'annotations': {'chemical_form': 'nitride', 'density': 'high', 'typical_use': 'fast reactors'}},
}

class UraniumEnrichmentLevelEnum(RichEnum):
    """
    Standard uranium-235 enrichment level classifications
    """
    # Enum members
    NATURAL = "NATURAL"
    SLIGHTLY_ENRICHED = "SLIGHTLY_ENRICHED"
    LOW_ENRICHED = "LOW_ENRICHED"
    HIGH_ASSAY_LOW_ENRICHED = "HIGH_ASSAY_LOW_ENRICHED"
    HIGHLY_ENRICHED = "HIGHLY_ENRICHED"
    WEAPONS_GRADE = "WEAPONS_GRADE"

# Set metadata after class creation
UraniumEnrichmentLevelEnum._metadata = {
    "NATURAL": {'description': 'Natural uranium enrichment (0.711% U-235)', 'annotations': {'u235_percentage': 0.711, 'category': 'natural', 'separative_work': 0}},
    "SLIGHTLY_ENRICHED": {'description': 'Minimal enrichment above natural levels', 'annotations': {'u235_percentage': '0.8-2.0', 'category': 'SEU', 'typical_use': 'some heavy water reactors'}},
    "LOW_ENRICHED": {'description': 'Standard commercial reactor enrichment', 'annotations': {'u235_percentage': '2.0-5.0', 'category': 'LEU', 'typical_use': 'PWR, BWR commercial reactors'}},
    "HIGH_ASSAY_LOW_ENRICHED": {'description': 'Higher enrichment for advanced reactors', 'annotations': {'u235_percentage': '5.0-20.0', 'category': 'HALEU', 'typical_use': 'advanced reactors, SMRs'}},
    "HIGHLY_ENRICHED": {'description': 'High enrichment for research and naval reactors', 'annotations': {'u235_percentage': '20.0-90.0', 'category': 'HEU', 'typical_use': 'research reactors, naval propulsion'}},
    "WEAPONS_GRADE": {'description': 'Very high enrichment for weapons', 'annotations': {'u235_percentage': '90.0+', 'category': 'WGU', 'proliferation_concern': 'extreme'}},
}

class FuelFormEnum(RichEnum):
    """
    Physical forms of nuclear fuel
    """
    # Enum members
    OXIDE_PELLETS = "OXIDE_PELLETS"
    METAL_SLUGS = "METAL_SLUGS"
    COATED_PARTICLES = "COATED_PARTICLES"
    LIQUID_SOLUTION = "LIQUID_SOLUTION"
    DISPERSION_FUEL = "DISPERSION_FUEL"
    CERMET_FUEL = "CERMET_FUEL"
    PLATE_FUEL = "PLATE_FUEL"
    ROD_FUEL = "ROD_FUEL"

# Set metadata after class creation
FuelFormEnum._metadata = {
    "OXIDE_PELLETS": {'description': 'Ceramic uranium dioxide pellets', 'annotations': {'chemical_form': 'UO2', 'shape': 'cylindrical pellets', 'typical_use': 'PWR, BWR fuel rods'}},
    "METAL_SLUGS": {'description': 'Metallic uranium fuel elements', 'annotations': {'chemical_form': 'metallic uranium', 'shape': 'cylindrical slugs', 'typical_use': 'production reactors'}},
    "COATED_PARTICLES": {'description': 'Microspheres with protective coatings', 'annotations': {'structure': 'TRISO or BISO coated', 'size': 'microscopic spheres', 'typical_use': 'HTGR'}},
    "LIQUID_SOLUTION": {'description': 'Fuel dissolved in liquid carrier', 'annotations': {'phase': 'liquid', 'typical_use': 'molten salt reactors'}},
    "DISPERSION_FUEL": {'description': 'Fuel particles dispersed in matrix', 'annotations': {'structure': 'particles in matrix', 'typical_use': 'research reactors'}},
    "CERMET_FUEL": {'description': 'Ceramic-metal composite fuel', 'annotations': {'structure': 'ceramic in metal matrix', 'typical_use': 'advanced reactors'}},
    "PLATE_FUEL": {'description': 'Flat plate fuel elements', 'annotations': {'geometry': 'flat plates', 'typical_use': 'research reactors'}},
    "ROD_FUEL": {'description': 'Cylindrical fuel rods', 'annotations': {'geometry': 'long cylinders', 'typical_use': 'commercial power reactors'}},
}

class FuelAssemblyTypeEnum(RichEnum):
    """
    Types of fuel assembly configurations
    """
    # Enum members
    PWR_ASSEMBLY = "PWR_ASSEMBLY"
    BWR_ASSEMBLY = "BWR_ASSEMBLY"
    CANDU_BUNDLE = "CANDU_BUNDLE"
    RBMK_ASSEMBLY = "RBMK_ASSEMBLY"
    AGR_ASSEMBLY = "AGR_ASSEMBLY"
    HTGR_BLOCK = "HTGR_BLOCK"
    FAST_REACTOR_ASSEMBLY = "FAST_REACTOR_ASSEMBLY"

# Set metadata after class creation
FuelAssemblyTypeEnum._metadata = {
    "PWR_ASSEMBLY": {'description': 'Square array fuel assembly for PWR', 'annotations': {'geometry': 'square array', 'rod_count': '264-289 typical', 'control_method': 'control rod clusters'}},
    "BWR_ASSEMBLY": {'description': 'Square array fuel assembly for BWR', 'annotations': {'geometry': 'square array with channel', 'rod_count': '49-100 typical', 'control_method': 'control blades'}},
    "CANDU_BUNDLE": {'description': 'Cylindrical fuel bundle for PHWR', 'annotations': {'geometry': 'cylindrical bundle', 'rod_count': '28-43 typical', 'length': '~50 cm'}},
    "RBMK_ASSEMBLY": {'description': 'Fuel assembly for RBMK reactors', 'annotations': {'geometry': '18-rod bundle', 'length': '~3.5 m', 'control_method': 'control rods'}},
    "AGR_ASSEMBLY": {'description': 'Fuel stringer for AGR', 'annotations': {'geometry': 'stacked pins', 'cladding': 'stainless steel'}},
    "HTGR_BLOCK": {'description': 'Graphite block with TRISO fuel', 'annotations': {'geometry': 'hexagonal or cylindrical blocks', 'fuel_form': 'TRISO particles'}},
    "FAST_REACTOR_ASSEMBLY": {'description': 'Fuel assembly for fast reactors', 'annotations': {'geometry': 'hexagonal wrapper', 'coolant_flow': 'axial'}},
}

class FuelCycleStageEnum(RichEnum):
    """
    Stages in the nuclear fuel cycle
    """
    # Enum members
    MINING = "MINING"
    CONVERSION = "CONVERSION"
    ENRICHMENT = "ENRICHMENT"
    FUEL_FABRICATION = "FUEL_FABRICATION"
    REACTOR_OPERATION = "REACTOR_OPERATION"
    INTERIM_STORAGE = "INTERIM_STORAGE"
    REPROCESSING = "REPROCESSING"
    DISPOSAL = "DISPOSAL"

# Set metadata after class creation
FuelCycleStageEnum._metadata = {
    "MINING": {'description': 'Extraction of uranium ore from deposits', 'annotations': {'process': 'mining and milling', 'product': 'uranium ore concentrate (yellowcake)'}},
    "CONVERSION": {'description': 'Conversion of uranium concentrate to UF6', 'annotations': {'input': 'U3O8 yellowcake', 'output': 'uranium hexafluoride (UF6)'}},
    "ENRICHMENT": {'description': 'Increase of U-235 concentration', 'annotations': {'input': 'natural UF6', 'output': 'enriched UF6', 'waste': 'depleted uranium tails'}},
    "FUEL_FABRICATION": {'description': 'Manufacturing of fuel assemblies', 'annotations': {'input': 'enriched UF6', 'output': 'fuel assemblies', 'process': 'pellet and rod manufacturing'}},
    "REACTOR_OPERATION": {'description': 'Power generation in nuclear reactor', 'annotations': {'input': 'fresh fuel assemblies', 'output': 'electricity and spent fuel', 'duration': '12-24 months per cycle'}},
    "INTERIM_STORAGE": {'description': 'Temporary storage of spent fuel', 'annotations': {'purpose': 'cooling and decay', 'duration': '5-40+ years', 'location': 'reactor pools or dry casks'}},
    "REPROCESSING": {'description': 'Chemical separation of spent fuel components', 'annotations': {'input': 'spent nuclear fuel', 'output': 'uranium, plutonium, waste', 'status': 'practiced in some countries'}},
    "DISPOSAL": {'description': 'Permanent disposal of nuclear waste', 'annotations': {'method': 'geological repository', 'duration': 'permanent', 'status': 'under development globally'}},
}

class FissileIsotopeEnum(RichEnum):
    """
    Fissile isotopes used in nuclear fuel
    """
    # Enum members
    URANIUM_233 = "URANIUM_233"
    URANIUM_235 = "URANIUM_235"
    PLUTONIUM_239 = "PLUTONIUM_239"
    PLUTONIUM_241 = "PLUTONIUM_241"

# Set metadata after class creation
FissileIsotopeEnum._metadata = {
    "URANIUM_233": {'description': 'Fissile isotope produced from thorium', 'annotations': {'mass_number': 233, 'half_life': '159,200 years', 'thermal_fission': True, 'breeding_from': 'Th-232'}, 'aliases': ['U-233']},
    "URANIUM_235": {'description': 'Naturally occurring fissile uranium isotope', 'annotations': {'mass_number': 235, 'half_life': '703,800,000 years', 'natural_abundance': '0.711%', 'thermal_fission': True}, 'aliases': ['U-235']},
    "PLUTONIUM_239": {'description': 'Fissile plutonium isotope from U-238 breeding', 'annotations': {'mass_number': 239, 'half_life': '24,110 years', 'thermal_fission': True, 'breeding_from': 'U-238'}, 'aliases': ['Pu-239']},
    "PLUTONIUM_241": {'description': 'Fissile plutonium isotope with short half-life', 'annotations': {'mass_number': 241, 'half_life': '14.3 years', 'thermal_fission': True, 'decay_product': 'Am-241'}, 'aliases': ['Pu-241']},
}

__all__ = [
    "NuclearFuelTypeEnum",
    "UraniumEnrichmentLevelEnum",
    "FuelFormEnum",
    "FuelAssemblyTypeEnum",
    "FuelCycleStageEnum",
    "FissileIsotopeEnum",
]