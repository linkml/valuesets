"""
Mining and Extractive Industry Value Sets

Value sets for mining operations, minerals, extraction methods, and related concepts

Generated from: industry/mining.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class MiningType(RichEnum):
    """
    Types of mining operations
    """
    # Enum members
    OPEN_PIT = "OPEN_PIT"
    STRIP_MINING = "STRIP_MINING"
    MOUNTAINTOP_REMOVAL = "MOUNTAINTOP_REMOVAL"
    QUARRYING = "QUARRYING"
    PLACER = "PLACER"
    DREDGING = "DREDGING"
    SHAFT_MINING = "SHAFT_MINING"
    DRIFT_MINING = "DRIFT_MINING"
    SLOPE_MINING = "SLOPE_MINING"
    ROOM_AND_PILLAR = "ROOM_AND_PILLAR"
    LONGWALL = "LONGWALL"
    BLOCK_CAVING = "BLOCK_CAVING"
    SOLUTION_MINING = "SOLUTION_MINING"
    HYDRAULIC_MINING = "HYDRAULIC_MINING"
    ARTISANAL = "ARTISANAL"
    DEEP_SEA = "DEEP_SEA"

# Set metadata after class creation
MiningType._metadata = {
    "OPEN_PIT": {'description': 'Open-pit mining', 'meaning': 'ENVO:00000284', 'annotations': {'category': 'surface', 'depth': 'shallow to deep'}},
    "STRIP_MINING": {'description': 'Strip mining', 'meaning': 'ENVO:01001441', 'annotations': {'category': 'surface', 'aliases': 'surface mining, opencast mining'}},
    "MOUNTAINTOP_REMOVAL": {'description': 'Mountaintop removal mining', 'annotations': {'category': 'surface', 'region': 'primarily Appalachian'}},
    "QUARRYING": {'description': 'Quarrying', 'meaning': 'ENVO:00000284', 'annotations': {'category': 'surface', 'materials': 'stone, sand, gravel'}},
    "PLACER": {'description': 'Placer mining', 'meaning': 'ENVO:01001204', 'annotations': {'category': 'surface', 'target': 'alluvial deposits'}},
    "DREDGING": {'description': 'Dredging', 'annotations': {'category': 'surface/underwater', 'environment': 'rivers, harbors, seas'}},
    "SHAFT_MINING": {'description': 'Shaft mining', 'annotations': {'category': 'underground', 'access': 'vertical shaft'}},
    "DRIFT_MINING": {'description': 'Drift mining', 'annotations': {'category': 'underground', 'access': 'horizontal tunnel'}},
    "SLOPE_MINING": {'description': 'Slope mining', 'annotations': {'category': 'underground', 'access': 'inclined shaft'}},
    "ROOM_AND_PILLAR": {'description': 'Room and pillar mining', 'annotations': {'category': 'underground', 'method': 'leaves pillars for support'}},
    "LONGWALL": {'description': 'Longwall mining', 'annotations': {'category': 'underground', 'method': 'progressive slice extraction'}},
    "BLOCK_CAVING": {'description': 'Block caving', 'annotations': {'category': 'underground', 'method': 'gravity-assisted'}},
    "SOLUTION_MINING": {'description': 'Solution mining (in-situ leaching)', 'annotations': {'category': 'specialized', 'method': 'chemical dissolution'}},
    "HYDRAULIC_MINING": {'description': 'Hydraulic mining', 'annotations': {'category': 'specialized', 'method': 'high-pressure water'}},
    "ARTISANAL": {'description': 'Artisanal and small-scale mining', 'annotations': {'category': 'small-scale', 'equipment': 'minimal mechanization'}},
    "DEEP_SEA": {'description': 'Deep sea mining', 'annotations': {'category': 'marine', 'depth': 'ocean floor'}},
}

class MineralCategory(RichEnum):
    """
    Categories of minerals and materials
    """
    # Enum members
    PRECIOUS_METALS = "PRECIOUS_METALS"
    BASE_METALS = "BASE_METALS"
    FERROUS_METALS = "FERROUS_METALS"
    RARE_EARTH_ELEMENTS = "RARE_EARTH_ELEMENTS"
    RADIOACTIVE = "RADIOACTIVE"
    INDUSTRIAL_MINERALS = "INDUSTRIAL_MINERALS"
    GEMSTONES = "GEMSTONES"
    ENERGY_MINERALS = "ENERGY_MINERALS"
    CONSTRUCTION_MATERIALS = "CONSTRUCTION_MATERIALS"
    CHEMICAL_MINERALS = "CHEMICAL_MINERALS"

# Set metadata after class creation
MineralCategory._metadata = {
    "PRECIOUS_METALS": {'description': 'Precious metals', 'annotations': {'examples': 'gold, silver, platinum'}},
    "BASE_METALS": {'description': 'Base metals', 'annotations': {'examples': 'copper, lead, zinc, tin'}},
    "FERROUS_METALS": {'description': 'Ferrous metals', 'annotations': {'examples': 'iron, steel, manganese'}},
    "RARE_EARTH_ELEMENTS": {'description': 'Rare earth elements', 'annotations': {'examples': 'neodymium, dysprosium, cerium', 'count': '17 elements'}},
    "RADIOACTIVE": {'description': 'Radioactive minerals', 'annotations': {'examples': 'uranium, thorium, radium'}},
    "INDUSTRIAL_MINERALS": {'description': 'Industrial minerals', 'annotations': {'examples': 'limestone, gypsum, salt'}},
    "GEMSTONES": {'description': 'Gemstones', 'annotations': {'examples': 'diamond, ruby, emerald'}},
    "ENERGY_MINERALS": {'description': 'Energy minerals', 'annotations': {'examples': 'coal, oil shale, tar sands'}},
    "CONSTRUCTION_MATERIALS": {'description': 'Construction materials', 'annotations': {'examples': 'sand, gravel, crushed stone'}},
    "CHEMICAL_MINERALS": {'description': 'Chemical and fertilizer minerals', 'annotations': {'examples': 'phosphate, potash, sulfur'}},
}

class CriticalMineral(RichEnum):
    """
    Critical minerals essential for economic and national security,
    particularly for clean energy, defense, and technology applications.
    Based on US Geological Survey and EU critical raw materials lists.
    """
    # Enum members
    LITHIUM = "LITHIUM"
    COBALT = "COBALT"
    NICKEL = "NICKEL"
    GRAPHITE = "GRAPHITE"
    MANGANESE = "MANGANESE"
    NEODYMIUM = "NEODYMIUM"
    DYSPROSIUM = "DYSPROSIUM"
    PRASEODYMIUM = "PRASEODYMIUM"
    TERBIUM = "TERBIUM"
    EUROPIUM = "EUROPIUM"
    YTTRIUM = "YTTRIUM"
    CERIUM = "CERIUM"
    LANTHANUM = "LANTHANUM"
    GALLIUM = "GALLIUM"
    GERMANIUM = "GERMANIUM"
    INDIUM = "INDIUM"
    TELLURIUM = "TELLURIUM"
    ARSENIC = "ARSENIC"
    TITANIUM = "TITANIUM"
    VANADIUM = "VANADIUM"
    CHROMIUM = "CHROMIUM"
    TUNGSTEN = "TUNGSTEN"
    TANTALUM = "TANTALUM"
    NIOBIUM = "NIOBIUM"
    ZIRCONIUM = "ZIRCONIUM"
    HAFNIUM = "HAFNIUM"
    PLATINUM = "PLATINUM"
    PALLADIUM = "PALLADIUM"
    RHODIUM = "RHODIUM"
    IRIDIUM = "IRIDIUM"
    RUTHENIUM = "RUTHENIUM"
    ANTIMONY = "ANTIMONY"
    BISMUTH = "BISMUTH"
    BERYLLIUM = "BERYLLIUM"
    MAGNESIUM = "MAGNESIUM"
    ALUMINUM = "ALUMINUM"
    TIN = "TIN"
    FLUORSPAR = "FLUORSPAR"
    BARITE = "BARITE"
    HELIUM = "HELIUM"
    POTASH = "POTASH"
    PHOSPHATE_ROCK = "PHOSPHATE_ROCK"
    SCANDIUM = "SCANDIUM"
    STRONTIUM = "STRONTIUM"

# Set metadata after class creation
CriticalMineral._metadata = {
    "LITHIUM": {'description': 'Lithium (Li) - essential for batteries', 'meaning': 'CHEBI:30145', 'annotations': {'symbol': 'Li', 'atomic_number': 3, 'applications': 'batteries, ceramics, glass'}},
    "COBALT": {'description': 'Cobalt (Co) - battery cathodes and superalloys', 'meaning': 'CHEBI:27638', 'annotations': {'symbol': 'Co', 'atomic_number': 27, 'applications': 'batteries, superalloys, magnets'}},
    "NICKEL": {'description': 'Nickel (Ni) - stainless steel and batteries', 'meaning': 'CHEBI:28112', 'annotations': {'symbol': 'Ni', 'atomic_number': 28, 'applications': 'stainless steel, batteries, alloys'}},
    "GRAPHITE": {'description': 'Graphite - battery anodes and refractories', 'meaning': 'CHEBI:33418', 'annotations': {'formula': 'C', 'applications': 'batteries, lubricants, refractories'}},
    "MANGANESE": {'description': 'Manganese (Mn) - steel and battery production', 'meaning': 'CHEBI:18291', 'annotations': {'symbol': 'Mn', 'atomic_number': 25, 'applications': 'steel, batteries, aluminum alloys'}},
    "NEODYMIUM": {'description': 'Neodymium (Nd) - permanent magnets', 'meaning': 'CHEBI:33372', 'annotations': {'symbol': 'Nd', 'atomic_number': 60, 'category': 'light rare earth', 'applications': 'magnets, lasers, glass'}},
    "DYSPROSIUM": {'description': 'Dysprosium (Dy) - high-performance magnets', 'meaning': 'CHEBI:33377', 'annotations': {'symbol': 'Dy', 'atomic_number': 66, 'category': 'heavy rare earth', 'applications': 'magnets, nuclear control rods'}},
    "PRASEODYMIUM": {'description': 'Praseodymium (Pr) - magnets and alloys', 'meaning': 'CHEBI:49828', 'annotations': {'symbol': 'Pr', 'atomic_number': 59, 'category': 'light rare earth', 'applications': 'magnets, aircraft engines, glass'}},
    "TERBIUM": {'description': 'Terbium (Tb) - phosphors and magnets', 'meaning': 'CHEBI:33376', 'annotations': {'symbol': 'Tb', 'atomic_number': 65, 'category': 'heavy rare earth', 'applications': 'solid-state devices, fuel cells'}},
    "EUROPIUM": {'description': 'Europium (Eu) - phosphors and nuclear control', 'meaning': 'CHEBI:32999', 'annotations': {'symbol': 'Eu', 'atomic_number': 63, 'category': 'heavy rare earth', 'applications': 'LED phosphors, lasers'}},
    "YTTRIUM": {'description': 'Yttrium (Y) - phosphors and ceramics', 'meaning': 'CHEBI:33331', 'annotations': {'symbol': 'Y', 'atomic_number': 39, 'applications': 'LEDs, superconductors, ceramics'}},
    "CERIUM": {'description': 'Cerium (Ce) - catalysts and glass polishing', 'meaning': 'CHEBI:33369', 'annotations': {'symbol': 'Ce', 'atomic_number': 58, 'category': 'light rare earth', 'applications': 'catalysts, glass polishing, alloys'}},
    "LANTHANUM": {'description': 'Lanthanum (La) - catalysts and optics', 'meaning': 'CHEBI:33336', 'annotations': {'symbol': 'La', 'atomic_number': 57, 'category': 'light rare earth', 'applications': 'catalysts, optical glass, batteries'}},
    "GALLIUM": {'description': 'Gallium (Ga) - semiconductors and LEDs', 'meaning': 'CHEBI:49631', 'annotations': {'symbol': 'Ga', 'atomic_number': 31, 'applications': 'semiconductors, LEDs, solar cells'}},
    "GERMANIUM": {'description': 'Germanium (Ge) - fiber optics and infrared', 'meaning': 'CHEBI:30441', 'annotations': {'symbol': 'Ge', 'atomic_number': 32, 'applications': 'fiber optics, infrared optics, solar cells'}},
    "INDIUM": {'description': 'Indium (In) - displays and semiconductors', 'meaning': 'CHEBI:30430', 'annotations': {'symbol': 'In', 'atomic_number': 49, 'applications': 'LCD displays, semiconductors, solar panels'}},
    "TELLURIUM": {'description': 'Tellurium (Te) - solar panels and thermoelectrics', 'meaning': 'CHEBI:30452', 'annotations': {'symbol': 'Te', 'atomic_number': 52, 'applications': 'solar panels, thermoelectrics, alloys'}},
    "ARSENIC": {'description': 'Arsenic (As) - semiconductors and alloys', 'meaning': 'CHEBI:27563', 'annotations': {'symbol': 'As', 'atomic_number': 33, 'applications': 'semiconductors, wood preservatives'}},
    "TITANIUM": {'description': 'Titanium (Ti) - aerospace and defense', 'meaning': 'CHEBI:33341', 'annotations': {'symbol': 'Ti', 'atomic_number': 22, 'applications': 'aerospace, medical implants, pigments'}},
    "VANADIUM": {'description': 'Vanadium (V) - steel alloys and batteries', 'meaning': 'CHEBI:27698', 'annotations': {'symbol': 'V', 'atomic_number': 23, 'applications': 'steel alloys, flow batteries, catalysts'}},
    "CHROMIUM": {'description': 'Chromium (Cr) - stainless steel and alloys', 'meaning': 'CHEBI:28073', 'annotations': {'symbol': 'Cr', 'atomic_number': 24, 'applications': 'stainless steel, superalloys, plating'}},
    "TUNGSTEN": {'description': 'Tungsten (W) - hard metals and electronics', 'meaning': 'CHEBI:27998', 'annotations': {'symbol': 'W', 'atomic_number': 74, 'applications': 'cutting tools, electronics, alloys'}},
    "TANTALUM": {'description': 'Tantalum (Ta) - capacitors and superalloys', 'meaning': 'CHEBI:33348', 'annotations': {'symbol': 'Ta', 'atomic_number': 73, 'applications': 'capacitors, medical implants, superalloys'}},
    "NIOBIUM": {'description': 'Niobium (Nb) - steel alloys and superconductors', 'meaning': 'CHEBI:33344', 'annotations': {'symbol': 'Nb', 'atomic_number': 41, 'applications': 'steel alloys, superconductors, capacitors'}},
    "ZIRCONIUM": {'description': 'Zirconium (Zr) - nuclear and ceramics', 'meaning': 'CHEBI:33342', 'annotations': {'symbol': 'Zr', 'atomic_number': 40, 'applications': 'nuclear reactors, ceramics, alloys'}},
    "HAFNIUM": {'description': 'Hafnium (Hf) - nuclear and semiconductors', 'meaning': 'CHEBI:33343', 'annotations': {'symbol': 'Hf', 'atomic_number': 72, 'applications': 'nuclear control rods, superalloys'}},
    "PLATINUM": {'description': 'Platinum (Pt) - catalysts and electronics', 'meaning': 'CHEBI:33400', 'annotations': {'symbol': 'Pt', 'atomic_number': 78, 'category': 'PGM', 'applications': 'catalysts, jewelry, electronics'}},
    "PALLADIUM": {'description': 'Palladium (Pd) - catalysts and electronics', 'meaning': 'CHEBI:33363', 'annotations': {'symbol': 'Pd', 'atomic_number': 46, 'category': 'PGM', 'applications': 'catalysts, electronics, dentistry'}},
    "RHODIUM": {'description': 'Rhodium (Rh) - catalysts and electronics', 'meaning': 'CHEBI:33359', 'annotations': {'symbol': 'Rh', 'atomic_number': 45, 'category': 'PGM', 'applications': 'catalysts, electronics, glass'}},
    "IRIDIUM": {'description': 'Iridium (Ir) - electronics and catalysts', 'meaning': 'CHEBI:49666', 'annotations': {'symbol': 'Ir', 'atomic_number': 77, 'category': 'PGM', 'applications': 'spark plugs, electronics, catalysts'}},
    "RUTHENIUM": {'description': 'Ruthenium (Ru) - electronics and catalysts', 'meaning': 'CHEBI:30682', 'annotations': {'symbol': 'Ru', 'atomic_number': 44, 'category': 'PGM', 'applications': 'electronics, catalysts, solar cells'}},
    "ANTIMONY": {'description': 'Antimony (Sb) - flame retardants and batteries', 'meaning': 'CHEBI:30513', 'annotations': {'symbol': 'Sb', 'atomic_number': 51, 'applications': 'flame retardants, batteries, alloys'}},
    "BISMUTH": {'description': 'Bismuth (Bi) - pharmaceuticals and alloys', 'meaning': 'CHEBI:33301', 'annotations': {'symbol': 'Bi', 'atomic_number': 83, 'applications': 'pharmaceuticals, cosmetics, alloys'}},
    "BERYLLIUM": {'description': 'Beryllium (Be) - aerospace and defense', 'meaning': 'CHEBI:30501', 'annotations': {'symbol': 'Be', 'atomic_number': 4, 'applications': 'aerospace, defense, nuclear'}},
    "MAGNESIUM": {'description': 'Magnesium (Mg) - lightweight alloys', 'meaning': 'CHEBI:25107', 'annotations': {'symbol': 'Mg', 'atomic_number': 12, 'applications': 'alloys, automotive, aerospace'}},
    "ALUMINUM": {'description': 'Aluminum (Al) - construction and transportation', 'meaning': 'CHEBI:28984', 'annotations': {'symbol': 'Al', 'atomic_number': 13, 'applications': 'construction, transportation, packaging'}},
    "TIN": {'description': 'Tin (Sn) - solders and coatings', 'meaning': 'CHEBI:27007', 'annotations': {'symbol': 'Sn', 'atomic_number': 50, 'applications': 'solders, coatings, alloys'}},
    "FLUORSPAR": {'description': 'Fluorspar (CaF2) - steel and aluminum production', 'meaning': 'CHEBI:35437', 'annotations': {'formula': 'CaF2', 'mineral_name': 'fluorite', 'applications': 'steel, aluminum, refrigerants'}},
    "BARITE": {'description': 'Barite (BaSO4) - drilling and chemicals', 'meaning': 'CHEBI:133326', 'annotations': {'formula': 'BaSO4', 'applications': 'oil drilling, chemicals, radiation shielding'}},
    "HELIUM": {'description': 'Helium (He) - cryogenics and electronics', 'meaning': 'CHEBI:33681', 'annotations': {'symbol': 'He', 'atomic_number': 2, 'applications': 'MRI, semiconductors, aerospace'}},
    "POTASH": {'description': 'Potash (K2O) - fertilizers and chemicals', 'meaning': 'CHEBI:88321', 'annotations': {'formula': 'K2O', 'applications': 'fertilizers, chemicals, glass'}},
    "PHOSPHATE_ROCK": {'description': 'Phosphate rock - fertilizers and chemicals', 'meaning': 'CHEBI:26020', 'annotations': {'applications': 'fertilizers, food additives, chemicals'}},
    "SCANDIUM": {'description': 'Scandium (Sc) - aerospace alloys', 'meaning': 'CHEBI:33330', 'annotations': {'symbol': 'Sc', 'atomic_number': 21, 'applications': 'aerospace alloys, solid oxide fuel cells'}},
    "STRONTIUM": {'description': 'Strontium (Sr) - magnets and pyrotechnics', 'meaning': 'CHEBI:33324', 'annotations': {'symbol': 'Sr', 'atomic_number': 38, 'applications': 'magnets, pyrotechnics, medical'}},
}

class CommonMineral(RichEnum):
    """
    Common minerals extracted through mining
    """
    # Enum members
    GOLD = "GOLD"
    SILVER = "SILVER"
    PLATINUM = "PLATINUM"
    COPPER = "COPPER"
    IRON = "IRON"
    ALUMINUM = "ALUMINUM"
    ZINC = "ZINC"
    LEAD = "LEAD"
    NICKEL = "NICKEL"
    TIN = "TIN"
    COAL = "COAL"
    URANIUM = "URANIUM"
    LIMESTONE = "LIMESTONE"
    SALT = "SALT"
    PHOSPHATE = "PHOSPHATE"
    POTASH = "POTASH"
    LITHIUM = "LITHIUM"
    COBALT = "COBALT"
    DIAMOND = "DIAMOND"

# Set metadata after class creation
CommonMineral._metadata = {
    "GOLD": {'description': 'Gold (Au)', 'meaning': 'CHEBI:29287', 'annotations': {'symbol': 'Au', 'atomic_number': 79}},
    "SILVER": {'description': 'Silver (Ag)', 'meaning': 'CHEBI:30512', 'annotations': {'symbol': 'Ag', 'atomic_number': 47}},
    "PLATINUM": {'description': 'Platinum (Pt)', 'meaning': 'CHEBI:49202', 'annotations': {'symbol': 'Pt', 'atomic_number': 78}},
    "COPPER": {'description': 'Copper (Cu)', 'meaning': 'CHEBI:28694', 'annotations': {'symbol': 'Cu', 'atomic_number': 29}},
    "IRON": {'description': 'Iron (Fe)', 'meaning': 'CHEBI:18248', 'annotations': {'symbol': 'Fe', 'atomic_number': 26}},
    "ALUMINUM": {'description': 'Aluminum (Al)', 'meaning': 'CHEBI:28984', 'annotations': {'symbol': 'Al', 'atomic_number': 13, 'ore': 'bauxite'}},
    "ZINC": {'description': 'Zinc (Zn)', 'meaning': 'CHEBI:27363', 'annotations': {'symbol': 'Zn', 'atomic_number': 30}},
    "LEAD": {'description': 'Lead (Pb)', 'meaning': 'CHEBI:25016', 'annotations': {'symbol': 'Pb', 'atomic_number': 82}},
    "NICKEL": {'description': 'Nickel (Ni)', 'meaning': 'CHEBI:28112', 'annotations': {'symbol': 'Ni', 'atomic_number': 28}},
    "TIN": {'description': 'Tin (Sn)', 'meaning': 'CHEBI:27007', 'annotations': {'symbol': 'Sn', 'atomic_number': 50}},
    "COAL": {'description': 'Coal', 'meaning': 'ENVO:02000091', 'annotations': {'types': 'anthracite, bituminous, lignite'}},
    "URANIUM": {'description': 'Uranium (U)', 'meaning': 'CHEBI:27214', 'annotations': {'symbol': 'U', 'atomic_number': 92}},
    "LIMESTONE": {'description': 'Limestone (CaCO3)', 'meaning': 'ENVO:00002053', 'annotations': {'formula': 'CaCO3', 'use': 'cement, steel production'}},
    "SALT": {'description': 'Salt (NaCl)', 'meaning': 'CHEBI:24866', 'annotations': {'formula': 'NaCl', 'aliases': 'halite, rock salt'}},
    "PHOSPHATE": {'description': 'Phosphate rock', 'meaning': 'CHEBI:26020', 'annotations': {'use': 'fertilizer production'}},
    "POTASH": {'description': 'Potash (K2O)', 'meaning': 'CHEBI:88321', 'annotations': {'formula': 'K2O', 'use': 'fertilizer'}},
    "LITHIUM": {'description': 'Lithium (Li)', 'meaning': 'CHEBI:30145', 'annotations': {'symbol': 'Li', 'atomic_number': 3, 'use': 'batteries'}},
    "COBALT": {'description': 'Cobalt (Co)', 'meaning': 'CHEBI:27638', 'annotations': {'symbol': 'Co', 'atomic_number': 27, 'use': 'batteries, alloys'}},
    "DIAMOND": {'description': 'Diamond (C)', 'meaning': 'CHEBI:33417', 'annotations': {'formula': 'C', 'use': 'gemstone, industrial'}},
}

class MiningEquipment(RichEnum):
    """
    Types of mining equipment
    """
    # Enum members
    DRILL_RIG = "DRILL_RIG"
    JUMBO_DRILL = "JUMBO_DRILL"
    EXCAVATOR = "EXCAVATOR"
    DRAGLINE = "DRAGLINE"
    BUCKET_WHEEL_EXCAVATOR = "BUCKET_WHEEL_EXCAVATOR"
    HAUL_TRUCK = "HAUL_TRUCK"
    LOADER = "LOADER"
    CONVEYOR = "CONVEYOR"
    CRUSHER = "CRUSHER"
    BALL_MILL = "BALL_MILL"
    FLOTATION_CELL = "FLOTATION_CELL"
    CONTINUOUS_MINER = "CONTINUOUS_MINER"
    ROOF_BOLTER = "ROOF_BOLTER"
    SHUTTLE_CAR = "SHUTTLE_CAR"

# Set metadata after class creation
MiningEquipment._metadata = {
    "DRILL_RIG": {'description': 'Drilling rig', 'annotations': {'category': 'drilling'}},
    "JUMBO_DRILL": {'description': 'Jumbo drill', 'annotations': {'category': 'drilling', 'use': 'underground'}},
    "EXCAVATOR": {'description': 'Excavator', 'annotations': {'category': 'excavation'}},
    "DRAGLINE": {'description': 'Dragline excavator', 'annotations': {'category': 'excavation', 'size': 'large-scale'}},
    "BUCKET_WHEEL_EXCAVATOR": {'description': 'Bucket-wheel excavator', 'annotations': {'category': 'excavation', 'use': 'continuous mining'}},
    "HAUL_TRUCK": {'description': 'Haul truck', 'annotations': {'category': 'hauling', 'capacity': 'up to 400 tons'}},
    "LOADER": {'description': 'Loader', 'annotations': {'category': 'loading'}},
    "CONVEYOR": {'description': 'Conveyor system', 'annotations': {'category': 'transport'}},
    "CRUSHER": {'description': 'Crusher', 'annotations': {'category': 'processing', 'types': 'jaw, cone, impact'}},
    "BALL_MILL": {'description': 'Ball mill', 'annotations': {'category': 'processing', 'use': 'grinding'}},
    "FLOTATION_CELL": {'description': 'Flotation cell', 'annotations': {'category': 'processing', 'use': 'mineral separation'}},
    "CONTINUOUS_MINER": {'description': 'Continuous miner', 'annotations': {'category': 'underground'}},
    "ROOF_BOLTER": {'description': 'Roof bolter', 'annotations': {'category': 'underground', 'use': 'support installation'}},
    "SHUTTLE_CAR": {'description': 'Shuttle car', 'annotations': {'category': 'underground transport'}},
}

class OreGrade(RichEnum):
    """
    Classification of ore grades
    """
    # Enum members
    HIGH_GRADE = "HIGH_GRADE"
    MEDIUM_GRADE = "MEDIUM_GRADE"
    LOW_GRADE = "LOW_GRADE"
    MARGINAL = "MARGINAL"
    SUB_ECONOMIC = "SUB_ECONOMIC"
    WASTE = "WASTE"

# Set metadata after class creation
OreGrade._metadata = {
    "HIGH_GRADE": {'description': 'High-grade ore', 'annotations': {'concentration': 'high', 'processing': 'minimal required'}},
    "MEDIUM_GRADE": {'description': 'Medium-grade ore', 'annotations': {'concentration': 'moderate'}},
    "LOW_GRADE": {'description': 'Low-grade ore', 'annotations': {'concentration': 'low', 'processing': 'extensive required'}},
    "MARGINAL": {'description': 'Marginal ore', 'annotations': {'economics': 'borderline profitable'}},
    "SUB_ECONOMIC": {'description': 'Sub-economic ore', 'annotations': {'economics': 'not currently profitable'}},
    "WASTE": {'description': 'Waste rock', 'annotations': {'concentration': 'below cutoff'}},
}

class MiningPhase(RichEnum):
    """
    Phases of mining operations
    """
    # Enum members
    EXPLORATION = "EXPLORATION"
    DEVELOPMENT = "DEVELOPMENT"
    PRODUCTION = "PRODUCTION"
    PROCESSING = "PROCESSING"
    CLOSURE = "CLOSURE"
    RECLAMATION = "RECLAMATION"
    POST_CLOSURE = "POST_CLOSURE"

# Set metadata after class creation
MiningPhase._metadata = {
    "EXPLORATION": {'description': 'Exploration phase', 'annotations': {'activities': 'prospecting, sampling, drilling'}},
    "DEVELOPMENT": {'description': 'Development phase', 'annotations': {'activities': 'infrastructure, access roads'}},
    "PRODUCTION": {'description': 'Production/extraction phase', 'annotations': {'activities': 'active mining'}},
    "PROCESSING": {'description': 'Processing/beneficiation phase', 'annotations': {'activities': 'crushing, milling, concentration'}},
    "CLOSURE": {'description': 'Closure phase', 'annotations': {'activities': 'decommissioning, capping'}},
    "RECLAMATION": {'description': 'Reclamation phase', 'annotations': {'activities': 'restoration, revegetation'}},
    "POST_CLOSURE": {'description': 'Post-closure monitoring', 'annotations': {'activities': 'long-term monitoring'}},
}

class MiningHazard(RichEnum):
    """
    Mining-related hazards and risks
    """
    # Enum members
    CAVE_IN = "CAVE_IN"
    GAS_EXPLOSION = "GAS_EXPLOSION"
    FLOODING = "FLOODING"
    DUST_EXPOSURE = "DUST_EXPOSURE"
    CHEMICAL_EXPOSURE = "CHEMICAL_EXPOSURE"
    RADIATION = "RADIATION"
    NOISE = "NOISE"
    VIBRATION = "VIBRATION"
    HEAT_STRESS = "HEAT_STRESS"
    EQUIPMENT_ACCIDENT = "EQUIPMENT_ACCIDENT"

# Set metadata after class creation
MiningHazard._metadata = {
    "CAVE_IN": {'description': 'Cave-in/roof collapse', 'annotations': {'type': 'structural'}},
    "GAS_EXPLOSION": {'description': 'Gas explosion', 'annotations': {'type': 'chemical', 'gases': 'methane, coal dust'}},
    "FLOODING": {'description': 'Mine flooding', 'annotations': {'type': 'water'}},
    "DUST_EXPOSURE": {'description': 'Dust exposure', 'annotations': {'type': 'respiratory', 'diseases': 'silicosis, pneumoconiosis'}},
    "CHEMICAL_EXPOSURE": {'description': 'Chemical exposure', 'annotations': {'type': 'toxic', 'chemicals': 'mercury, cyanide, acids'}},
    "RADIATION": {'description': 'Radiation exposure', 'annotations': {'type': 'radioactive', 'source': 'uranium, radon'}},
    "NOISE": {'description': 'Noise exposure', 'annotations': {'type': 'physical'}},
    "VIBRATION": {'description': 'Vibration exposure', 'annotations': {'type': 'physical'}},
    "HEAT_STRESS": {'description': 'Heat stress', 'annotations': {'type': 'thermal'}},
    "EQUIPMENT_ACCIDENT": {'description': 'Equipment-related accident', 'annotations': {'type': 'mechanical'}},
}

class EnvironmentalImpact(RichEnum):
    """
    Environmental impacts of mining
    """
    # Enum members
    HABITAT_DESTRUCTION = "HABITAT_DESTRUCTION"
    WATER_POLLUTION = "WATER_POLLUTION"
    AIR_POLLUTION = "AIR_POLLUTION"
    SOIL_CONTAMINATION = "SOIL_CONTAMINATION"
    DEFORESTATION = "DEFORESTATION"
    EROSION = "EROSION"
    ACID_MINE_DRAINAGE = "ACID_MINE_DRAINAGE"
    TAILINGS = "TAILINGS"
    SUBSIDENCE = "SUBSIDENCE"
    BIODIVERSITY_LOSS = "BIODIVERSITY_LOSS"

# Set metadata after class creation
EnvironmentalImpact._metadata = {
    "HABITAT_DESTRUCTION": {'description': 'Habitat destruction', 'meaning': 'ExO:0000012'},
    "WATER_POLLUTION": {'description': 'Water pollution', 'meaning': 'ENVO:02500039', 'annotations': {'types': 'acid mine drainage, heavy metals'}},
    "AIR_POLLUTION": {'description': 'Air pollution', 'meaning': 'ENVO:02500037', 'annotations': {'sources': 'dust, emissions'}},
    "SOIL_CONTAMINATION": {'description': 'Soil contamination', 'meaning': 'ENVO:00002116'},
    "DEFORESTATION": {'description': 'Deforestation', 'meaning': 'ENVO:02500012'},
    "EROSION": {'description': 'Erosion and sedimentation', 'meaning': 'ENVO:01001346'},
    "ACID_MINE_DRAINAGE": {'description': 'Acid mine drainage', 'meaning': 'ENVO:00001997'},
    "TAILINGS": {'description': 'Tailings contamination', 'annotations': {'storage': 'tailings ponds, dams'}},
    "SUBSIDENCE": {'description': 'Ground subsidence', 'annotations': {'cause': 'underground voids'}},
    "BIODIVERSITY_LOSS": {'description': 'Biodiversity loss', 'annotations': {'impact': 'species extinction, ecosystem disruption'}},
}

__all__ = [
    "MiningType",
    "MineralCategory",
    "CriticalMineral",
    "CommonMineral",
    "MiningEquipment",
    "OreGrade",
    "MiningPhase",
    "MiningHazard",
    "EnvironmentalImpact",
]