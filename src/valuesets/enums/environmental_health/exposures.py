"""
valuesets-environmental-health-exposures

Environmental health and exposure-related value sets

Generated from: environmental_health/exposures.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class AirPollutantEnum(RichEnum):
    """
    Common air pollutants and air quality indicators
    """
    # Enum members
    PM2_5 = "PM2_5"
    PM10 = "PM10"
    ULTRAFINE_PARTICLES = "ULTRAFINE_PARTICLES"
    OZONE = "OZONE"
    NITROGEN_DIOXIDE = "NITROGEN_DIOXIDE"
    SULFUR_DIOXIDE = "SULFUR_DIOXIDE"
    CARBON_MONOXIDE = "CARBON_MONOXIDE"
    LEAD = "LEAD"
    BENZENE = "BENZENE"
    FORMALDEHYDE = "FORMALDEHYDE"
    VOLATILE_ORGANIC_COMPOUNDS = "VOLATILE_ORGANIC_COMPOUNDS"
    POLYCYCLIC_AROMATIC_HYDROCARBONS = "POLYCYCLIC_AROMATIC_HYDROCARBONS"

# Set metadata after class creation
AirPollutantEnum._metadata = {
    "PM2_5": {'description': 'Fine particulate matter with diameter less than 2.5 micrometers', 'meaning': 'ENVO:01000415'},
    "PM10": {'description': 'Respirable particulate matter with diameter less than 10 micrometers', 'meaning': 'ENVO:01000405'},
    "ULTRAFINE_PARTICLES": {'description': 'Ultrafine particles with diameter less than 100 nanometers', 'meaning': 'ENVO:01000416'},
    "OZONE": {'description': 'Ground-level ozone (O3)', 'meaning': 'CHEBI:25812'},
    "NITROGEN_DIOXIDE": {'description': 'Nitrogen dioxide (NO2)', 'meaning': 'CHEBI:33101'},
    "SULFUR_DIOXIDE": {'description': 'Sulfur dioxide (SO2)', 'meaning': 'CHEBI:18422'},
    "CARBON_MONOXIDE": {'description': 'Carbon monoxide (CO)', 'meaning': 'CHEBI:17245'},
    "LEAD": {'description': 'Airborne lead particles', 'meaning': 'NCIT:C44396'},
    "BENZENE": {'description': 'Benzene vapor', 'meaning': 'CHEBI:16716'},
    "FORMALDEHYDE": {'description': 'Formaldehyde gas', 'meaning': 'CHEBI:16842'},
    "VOLATILE_ORGANIC_COMPOUNDS": {'description': 'Volatile organic compounds (VOCs)', 'meaning': 'CHEBI:134179'},
    "POLYCYCLIC_AROMATIC_HYDROCARBONS": {'description': 'Polycyclic aromatic hydrocarbons (PAHs)', 'meaning': 'CHEBI:33848'},
}

class PesticideTypeEnum(RichEnum):
    """
    Categories of pesticides by target organism or chemical class
    """
    # Enum members
    HERBICIDE = "HERBICIDE"
    INSECTICIDE = "INSECTICIDE"
    FUNGICIDE = "FUNGICIDE"
    RODENTICIDE = "RODENTICIDE"
    ORGANOPHOSPHATE = "ORGANOPHOSPHATE"
    ORGANOCHLORINE = "ORGANOCHLORINE"
    PYRETHROID = "PYRETHROID"
    CARBAMATE = "CARBAMATE"
    NEONICOTINOID = "NEONICOTINOID"
    GLYPHOSATE = "GLYPHOSATE"

# Set metadata after class creation
PesticideTypeEnum._metadata = {
    "HERBICIDE": {'description': 'Chemical used to kill unwanted plants', 'meaning': 'CHEBI:24527'},
    "INSECTICIDE": {'description': 'Chemical used to kill insects', 'meaning': 'CHEBI:24852'},
    "FUNGICIDE": {'description': 'Chemical used to kill fungi', 'meaning': 'CHEBI:24127'},
    "RODENTICIDE": {'description': 'Chemical used to kill rodents', 'meaning': 'CHEBI:33288'},
    "ORGANOPHOSPHATE": {'description': 'Organophosphate pesticide', 'meaning': 'CHEBI:25708'},
    "ORGANOCHLORINE": {'description': 'Organochlorine pesticide', 'meaning': 'CHEBI:25705'},
    "PYRETHROID": {'description': 'Pyrethroid pesticide', 'meaning': 'CHEBI:26413'},
    "CARBAMATE": {'description': 'Carbamate pesticide', 'meaning': 'CHEBI:38461'},
    "NEONICOTINOID": {'description': 'Neonicotinoid pesticide', 'meaning': 'CHEBI:25540'},
    "GLYPHOSATE": {'description': 'Glyphosate herbicide', 'meaning': 'CHEBI:27744'},
}

class HeavyMetalEnum(RichEnum):
    """
    Heavy metals of environmental health concern
    """
    # Enum members
    LEAD = "LEAD"
    MERCURY = "MERCURY"
    CADMIUM = "CADMIUM"
    ARSENIC = "ARSENIC"
    CHROMIUM = "CHROMIUM"
    NICKEL = "NICKEL"
    COPPER = "COPPER"
    ZINC = "ZINC"
    MANGANESE = "MANGANESE"
    COBALT = "COBALT"

# Set metadata after class creation
HeavyMetalEnum._metadata = {
    "LEAD": {'description': 'Lead (Pb)', 'meaning': 'NCIT:C44396'},
    "MERCURY": {'description': 'Mercury (Hg)', 'meaning': 'NCIT:C66842'},
    "CADMIUM": {'description': 'Cadmium (Cd)', 'meaning': 'NCIT:C44348'},
    "ARSENIC": {'description': 'Arsenic (As)', 'meaning': 'NCIT:C28131'},
    "CHROMIUM": {'description': 'Chromium (Cr)', 'meaning': 'NCIT:C370'},
    "NICKEL": {'description': 'Nickel (Ni)', 'meaning': 'CHEBI:28112'},
    "COPPER": {'description': 'Copper (Cu)', 'meaning': 'CHEBI:28694'},
    "ZINC": {'description': 'Zinc (Zn)', 'meaning': 'CHEBI:27363'},
    "MANGANESE": {'description': 'Manganese (Mn)', 'meaning': 'CHEBI:18291'},
    "COBALT": {'description': 'Cobalt (Co)', 'meaning': 'CHEBI:27638'},
}

class ExposureRouteEnum(RichEnum):
    """
    Routes by which exposure to environmental agents occurs
    """
    # Enum members
    INHALATION = "INHALATION"
    INGESTION = "INGESTION"
    DERMAL = "DERMAL"
    INJECTION = "INJECTION"
    TRANSPLACENTAL = "TRANSPLACENTAL"
    OCULAR = "OCULAR"
    ABSORPTION = "ABSORPTION"
    GASTROINTESTINAL_TRACT = "GASTROINTESTINAL_TRACT"
    GAVAGE = "GAVAGE"
    AMBIENT_ENVIRONMENT = "AMBIENT_ENVIRONMENT"
    AMBIENT_AQUATIC = "AMBIENT_AQUATIC"
    AMBIENT_TERRESTRIAL = "AMBIENT_TERRESTRIAL"
    PASSIVE_INHALATION = "PASSIVE_INHALATION"
    ACTIVE_INHALATION = "ACTIVE_INHALATION"
    SUBCUTANEOUS = "SUBCUTANEOUS"
    INTRAMUSCULAR = "INTRAMUSCULAR"
    INTRAVASCULAR = "INTRAVASCULAR"
    MULTIPLE_ROUTES = "MULTIPLE_ROUTES"

# Set metadata after class creation
ExposureRouteEnum._metadata = {
    "INHALATION": {'description': 'Exposure through breathing', 'meaning': 'NCIT:C38284'},
    "INGESTION": {'description': 'Exposure through eating or drinking', 'meaning': 'NCIT:C38288'},
    "DERMAL": {'description': 'Exposure through skin contact', 'meaning': 'NCIT:C38675'},
    "INJECTION": {'description': 'Exposure through injection', 'meaning': 'NCIT:C38276'},
    "TRANSPLACENTAL": {'description': 'Exposure through placental transfer', 'meaning': 'NCIT:C38307'},
    "OCULAR": {'description': 'Exposure through the eyes', 'meaning': 'NCIT:C38287'},
    "ABSORPTION": {'description': 'Exposure through absorption (dermal or other surface)', 'meaning': 'ExO:0000058'},
    "GASTROINTESTINAL_TRACT": {'description': 'Exposure through the gastrointestinal tract', 'meaning': 'ExO:0000165'},
    "GAVAGE": {'description': 'Direct administration into the stomach', 'meaning': 'ExO:0000166'},
    "AMBIENT_ENVIRONMENT": {'description': 'Exposure through contact with stressors in the ambient surroundings', 'meaning': 'ExO:0000160'},
    "AMBIENT_AQUATIC": {'description': 'Exposure through ambient aquatic environment', 'meaning': 'ExO:0000161'},
    "AMBIENT_TERRESTRIAL": {'description': 'Exposure through ambient terrestrial environment', 'meaning': 'ExO:0000162'},
    "PASSIVE_INHALATION": {'description': 'Passive inhalation of ambient environment stressors', 'meaning': 'ExO:0000163'},
    "ACTIVE_INHALATION": {'description': 'Purposeful breathing or inhaling of stressor', 'meaning': 'ExO:0000164'},
    "SUBCUTANEOUS": {'description': 'Exposure through subcutaneous tissue'},
    "INTRAMUSCULAR": {'description': 'Exposure through muscle tissue'},
    "INTRAVASCULAR": {'description': 'Exposure through blood vessels'},
    "MULTIPLE_ROUTES": {'description': 'Exposure through multiple pathways'},
}

class ExposureSourceEnum(RichEnum):
    """
    Common sources of environmental exposures
    """
    # Enum members
    AMBIENT_AIR = "AMBIENT_AIR"
    INDOOR_AIR = "INDOOR_AIR"
    DRINKING_WATER = "DRINKING_WATER"
    SOIL = "SOIL"
    FOOD = "FOOD"
    OCCUPATIONAL = "OCCUPATIONAL"
    CONSUMER_PRODUCTS = "CONSUMER_PRODUCTS"
    INDUSTRIAL_EMISSIONS = "INDUSTRIAL_EMISSIONS"
    AGRICULTURAL = "AGRICULTURAL"
    TRAFFIC = "TRAFFIC"
    TOBACCO_SMOKE = "TOBACCO_SMOKE"
    CONSTRUCTION = "CONSTRUCTION"
    MINING = "MINING"

# Set metadata after class creation
ExposureSourceEnum._metadata = {
    "AMBIENT_AIR": {'description': 'Outdoor air pollution'},
    "INDOOR_AIR": {'description': 'Indoor air pollution'},
    "DRINKING_WATER": {'description': 'Contaminated drinking water'},
    "SOIL": {'description': 'Contaminated soil', 'meaning': 'ENVO:00002116'},
    "FOOD": {'description': 'Contaminated food'},
    "OCCUPATIONAL": {'description': 'Workplace exposure', 'meaning': 'ENVO:03501332'},
    "CONSUMER_PRODUCTS": {'description': 'Household and consumer products'},
    "INDUSTRIAL_EMISSIONS": {'description': 'Industrial facility emissions'},
    "AGRICULTURAL": {'description': 'Agricultural activities'},
    "TRAFFIC": {'description': 'Traffic-related pollution'},
    "TOBACCO_SMOKE": {'description': 'Active or passive tobacco smoke exposure', 'meaning': 'NCIT:C17140'},
    "CONSTRUCTION": {'description': 'Construction-related exposure'},
    "MINING": {'description': 'Mining-related exposure'},
}

class WaterContaminantEnum(RichEnum):
    """
    Common water contaminants
    """
    # Enum members
    LEAD = "LEAD"
    ARSENIC = "ARSENIC"
    NITRATES = "NITRATES"
    FLUORIDE = "FLUORIDE"
    CHLORINE = "CHLORINE"
    BACTERIA = "BACTERIA"
    VIRUSES = "VIRUSES"
    PARASITES = "PARASITES"
    PFAS = "PFAS"
    MICROPLASTICS = "MICROPLASTICS"
    PHARMACEUTICALS = "PHARMACEUTICALS"
    PESTICIDES = "PESTICIDES"

# Set metadata after class creation
WaterContaminantEnum._metadata = {
    "LEAD": {'description': 'Lead contamination', 'meaning': 'NCIT:C44396'},
    "ARSENIC": {'description': 'Arsenic contamination', 'meaning': 'NCIT:C28131'},
    "NITRATES": {'description': 'Nitrate contamination', 'meaning': 'CHEBI:17632'},
    "FLUORIDE": {'description': 'Fluoride levels', 'meaning': 'CHEBI:17051'},
    "CHLORINE": {'description': 'Chlorine and chlorination byproducts', 'meaning': 'NCIT:C28140'},
    "BACTERIA": {'description': 'Bacterial contamination', 'meaning': 'NCIT:C14187'},
    "VIRUSES": {'description': 'Viral contamination', 'meaning': 'NCIT:C14283'},
    "PARASITES": {'description': 'Parasitic contamination', 'meaning': 'NCIT:C28176'},
    "PFAS": {'description': 'Per- and polyfluoroalkyl substances', 'meaning': 'CHEBI:172397'},
    "MICROPLASTICS": {'description': 'Microplastic particles', 'meaning': 'ENVO:01000944'},
    "PHARMACEUTICALS": {'description': 'Pharmaceutical residues', 'meaning': 'CHEBI:52217'},
    "PESTICIDES": {'description': 'Pesticide residues', 'meaning': 'CHEBI:25944'},
}

class EndocrineDisruptorEnum(RichEnum):
    """
    Common endocrine disrupting chemicals
    """
    # Enum members
    BPA = "BPA"
    PHTHALATES = "PHTHALATES"
    PFAS = "PFAS"
    PCB = "PCB"
    DIOXINS = "DIOXINS"
    DDT = "DDT"
    PARABENS = "PARABENS"
    TRICLOSAN = "TRICLOSAN"
    FLAME_RETARDANTS = "FLAME_RETARDANTS"

# Set metadata after class creation
EndocrineDisruptorEnum._metadata = {
    "BPA": {'description': 'Bisphenol A', 'meaning': 'CHEBI:33216'},
    "PHTHALATES": {'description': 'Phthalates', 'meaning': 'CHEBI:26092'},
    "PFAS": {'description': 'Per- and polyfluoroalkyl substances', 'meaning': 'CHEBI:172397'},
    "PCB": {'description': 'Polychlorinated biphenyls', 'meaning': 'CHEBI:53156'},
    "DIOXINS": {'description': 'Dioxins', 'meaning': 'NCIT:C442'},
    "DDT": {'description': 'Dichlorodiphenyltrichloroethane and metabolites', 'meaning': 'CHEBI:16130'},
    "PARABENS": {'description': 'Parabens', 'meaning': 'CHEBI:85122'},
    "TRICLOSAN": {'description': 'Triclosan', 'meaning': 'CHEBI:164200'},
    "FLAME_RETARDANTS": {'description': 'Brominated flame retardants', 'meaning': 'CHEBI:172368'},
}

class ExposureDurationEnum(RichEnum):
    """
    Duration categories for environmental exposures
    """
    # Enum members
    ACUTE = "ACUTE"
    SUBACUTE = "SUBACUTE"
    SUBCHRONIC = "SUBCHRONIC"
    CHRONIC = "CHRONIC"
    LIFETIME = "LIFETIME"
    PRENATAL = "PRENATAL"
    POSTNATAL = "POSTNATAL"
    DEVELOPMENTAL = "DEVELOPMENTAL"

# Set metadata after class creation
ExposureDurationEnum._metadata = {
    "ACUTE": {'description': 'Single or short-term exposure (hours to days)'},
    "SUBACUTE": {'description': 'Repeated exposure over weeks'},
    "SUBCHRONIC": {'description': 'Repeated exposure over months'},
    "CHRONIC": {'description': 'Long-term exposure over years'},
    "LIFETIME": {'description': 'Exposure over entire lifetime'},
    "PRENATAL": {'description': 'Exposure during pregnancy'},
    "POSTNATAL": {'description': 'Exposure after birth'},
    "DEVELOPMENTAL": {'description': 'Exposure during critical developmental periods'},
}

class SmokingStatusEnum(RichEnum):
    """
    Tobacco and nicotine consumption status
    """
    # Enum members
    CURRENT_SMOKER = "CURRENT_SMOKER"
    FORMER_SMOKER = "FORMER_SMOKER"
    NEVER_SMOKER = "NEVER_SMOKER"
    NON_SMOKER = "NON_SMOKER"

# Set metadata after class creation
SmokingStatusEnum._metadata = {
    "CURRENT_SMOKER": {'description': 'Person who is currently smoking tobacco', 'meaning': 'ExO:0000115'},
    "FORMER_SMOKER": {'description': 'Person who has smoked at least 100 cigarettes in their life but is not currently smoking', 'meaning': 'ExO:0000116'},
    "NEVER_SMOKER": {'description': 'Person who has smoked less than 100 cigarettes in their life', 'meaning': 'ExO:0000117'},
    "NON_SMOKER": {'description': 'Person who is not currently smoking', 'meaning': 'ExO:0000118'},
}

class ExposureStressorTypeEnum(RichEnum):
    """
    Types of exposure stressors by their origin or nature
    """
    # Enum members
    BIOLOGICAL_AGENT = "BIOLOGICAL_AGENT"
    CHEMICAL_AGENT = "CHEMICAL_AGENT"
    PHYSICAL_AGENT = "PHYSICAL_AGENT"
    PSYCHOSOCIAL_AGENT = "PSYCHOSOCIAL_AGENT"
    BIOMECHANICAL_AGENT = "BIOMECHANICAL_AGENT"
    ECOLOGICAL_PERTURBATION = "ECOLOGICAL_PERTURBATION"

# Set metadata after class creation
ExposureStressorTypeEnum._metadata = {
    "BIOLOGICAL_AGENT": {'description': 'Agent of biological origin (e.g., bacteria, viruses, allergens)', 'meaning': 'ExO:0000005'},
    "CHEMICAL_AGENT": {'description': 'Agent of chemical origin (e.g., toxins, pollutants)', 'meaning': 'ExO:0000006'},
    "PHYSICAL_AGENT": {'description': 'Physical source of energy that may cause injury (e.g., radiation, noise, temperature extremes)', 'meaning': 'ExO:0000008'},
    "PSYCHOSOCIAL_AGENT": {'description': 'Agent that interferes with psychological development or social interaction', 'meaning': 'ExO:0000009'},
    "BIOMECHANICAL_AGENT": {'description': 'Mechanical agent applied to biological systems (e.g., repetitive motion, physical strain)', 'meaning': 'ExO:0000011'},
    "ECOLOGICAL_PERTURBATION": {'description': 'Disruption to ecological systems (e.g., habitat degradation, climate change)', 'meaning': 'ExO:0000007'},
}

class ExposureTransportPathEnum(RichEnum):
    """
    Transport medium through which exposure stressor reaches the recipient
    """
    # Enum members
    AIR_TRANSPORT_PATH = "AIR_TRANSPORT_PATH"
    WATER_TRANSPORT_PATH = "WATER_TRANSPORT_PATH"
    SOIL_TRANSPORT_PATH = "SOIL_TRANSPORT_PATH"

# Set metadata after class creation
ExposureTransportPathEnum._metadata = {
    "AIR_TRANSPORT_PATH": {'description': 'Transport path allowing stressor to interact with recipient via air', 'meaning': 'ExO:0000010'},
    "WATER_TRANSPORT_PATH": {'description': 'Transport path involving interaction with stressor via water', 'meaning': 'ExO:0000028'},
    "SOIL_TRANSPORT_PATH": {'description': 'Transport path involving interaction with stressor via soil', 'meaning': 'ExO:0000029'},
}

class ExposureFrequencyEnum(RichEnum):
    """
    Temporal pattern of exposure occurrence
    """
    # Enum members
    INTERMITTENT = "INTERMITTENT"
    CONTINUOUS = "CONTINUOUS"

# Set metadata after class creation
ExposureFrequencyEnum._metadata = {
    "INTERMITTENT": {'description': 'Exposure occurring at irregular intervals or periodically', 'meaning': 'ExO:0000052'},
    "CONTINUOUS": {'description': 'Exposure occurring without interruption', 'meaning': 'ExO:0000053'},
}

class StudyPopulationEnum(RichEnum):
    """
    Specific population groups commonly studied in exposure research
    """
    # Enum members
    CHILDREN = "CHILDREN"
    FETUSES = "FETUSES"
    INFANTS_OR_NEWBORNS = "INFANTS_OR_NEWBORNS"
    PREGNANT_FEMALES = "PREGNANT_FEMALES"
    MOTHERS = "MOTHERS"
    MILITARY_PERSONNEL = "MILITARY_PERSONNEL"
    VETERANS = "VETERANS"
    WORKERS = "WORKERS"
    CONTROLS = "CONTROLS"

# Set metadata after class creation
StudyPopulationEnum._metadata = {
    "CHILDREN": {'description': 'Human children (pediatric population)', 'meaning': 'ExO:0000119'},
    "FETUSES": {'description': 'Human fetuses (prenatal population)', 'meaning': 'ExO:0000122'},
    "INFANTS_OR_NEWBORNS": {'description': 'Human infants and newborns', 'meaning': 'ExO:0000123'},
    "PREGNANT_FEMALES": {'description': 'Human females who are pregnant', 'meaning': 'ExO:0000126'},
    "MOTHERS": {'description': 'Human mothers', 'meaning': 'ExO:0000125'},
    "MILITARY_PERSONNEL": {'description': 'Active military personnel', 'meaning': 'ExO:0000124'},
    "VETERANS": {'description': 'Military veterans', 'meaning': 'ExO:0000130'},
    "WORKERS": {'description': 'Occupational workers', 'meaning': 'ExO:0000131'},
    "CONTROLS": {'description': 'Control group participants without the disease or phenotype of interest', 'meaning': 'ExO:0000121'},
}

class HHEARExposureAssessedEnum(RichEnum):
    """
    Categories of environmental exposures assessed in Human Health Exposure Analysis Resource (HHEAR) studies. Based on the HHEAR value set HHEARVS:00008 (Study Environmental Exposures Assessed).
    """
    # Enum members
    AIR_POLLUTANT = "AIR_POLLUTANT"
    ALKYL_PHOSPHATE_PESTICIDE_METABOLITE = "ALKYL_PHOSPHATE_PESTICIDE_METABOLITE"
    ALLERGEN = "ALLERGEN"
    ARSENIC_SPECIES = "ARSENIC_SPECIES"
    BROMINATED_FLAME_RETARDANT = "BROMINATED_FLAME_RETARDANT"
    BUILT_ENVIRONMENT = "BUILT_ENVIRONMENT"
    ENVIRONMENTAL_PHENOL = "ENVIRONMENTAL_PHENOL"
    FOOD_PACKAGING = "FOOD_PACKAGING"
    MERCURY_SPECIES = "MERCURY_SPECIES"
    METAL = "METAL"
    ORGANOCHLORINE_COMPOUND = "ORGANOCHLORINE_COMPOUND"
    ORGANOPHOSPHORUS_FLAME_RETARDANT = "ORGANOPHOSPHORUS_FLAME_RETARDANT"
    PARABEN = "PARABEN"
    PERFLUOROALKYL_AND_POLYFLUOROALKYL_SUBSTANCE = "PERFLUOROALKYL_AND_POLYFLUOROALKYL_SUBSTANCE"
    PESTICIDE = "PESTICIDE"
    PHTHALATE = "PHTHALATE"
    POLYBROMINATED_DIPHENYL_ETHER = "POLYBROMINATED_DIPHENYL_ETHER"
    TOBACCO_METABOLITE = "TOBACCO_METABOLITE"
    TOBACCO_SMOKE_EXPOSURE = "TOBACCO_SMOKE_EXPOSURE"
    VOLATILE_ORGANIC_COMPOUND = "VOLATILE_ORGANIC_COMPOUND"
    WEATHER = "WEATHER"

# Set metadata after class creation
HHEARExposureAssessedEnum._metadata = {
    "AIR_POLLUTANT": {'description': 'Airborne pollutants including particulate matter and gaseous contaminants', 'meaning': 'ECTO:8000036'},
    "ALKYL_PHOSPHATE_PESTICIDE_METABOLITE": {'description': 'Metabolites of organophosphate pesticides', 'meaning': 'ECTO:0000530'},
    "ALLERGEN": {'description': 'Substances that can cause allergic reactions', 'meaning': 'ECTO:0000726'},
    "ARSENIC_SPECIES": {'description': 'Various forms of arsenic compounds', 'meaning': 'ECTO:9000032'},
    "BROMINATED_FLAME_RETARDANT": {'description': 'Organobromine compounds used as flame retardants', 'meaning': 'ECTO:9002162'},
    "BUILT_ENVIRONMENT": {'description': 'Human-made surroundings including buildings and infrastructure', 'meaning': 'ExO:0000048'},
    "ENVIRONMENTAL_PHENOL": {'description': 'Phenolic compounds in the environment', 'meaning': 'ECTO:9000071'},
    "FOOD_PACKAGING": {'description': 'Materials used to package food products', 'meaning': 'FOODON:03490100'},
    "MERCURY_SPECIES": {'description': 'Various forms of mercury compounds', 'meaning': 'ECTO:0001571'},
    "METAL": {'description': 'Metallic elements and compounds', 'meaning': 'ECTO:9002163'},
    "ORGANOCHLORINE_COMPOUND": {'description': 'Organic compounds containing chlorine', 'meaning': 'ECTO:0001152'},
    "ORGANOPHOSPHORUS_FLAME_RETARDANT": {'description': 'Organophosphorus compounds used as flame retardants', 'meaning': 'ECTO:9000284'},
    "PARABEN": {'description': '4-hydroxybenzoate esters used as preservatives', 'meaning': 'ECTO:9000930'},
    "PERFLUOROALKYL_AND_POLYFLUOROALKYL_SUBSTANCE": {'description': 'PFAS compounds including PFOA and PFOS', 'meaning': 'ECTO:9002160', 'aliases': ['PFAS']},
    "PESTICIDE": {'description': 'Substances used to control pests', 'meaning': 'ECTO:0000530'},
    "PHTHALATE": {'description': 'Phthalic acid esters used as plasticizers', 'meaning': 'ECTO:9000522'},
    "POLYBROMINATED_DIPHENYL_ETHER": {'description': 'Brominated aromatic ethers used as flame retardants', 'meaning': 'ECTO:9001619', 'aliases': ['PBDE']},
    "TOBACCO_METABOLITE": {'description': 'Metabolites of tobacco and nicotine', 'meaning': 'ECTO:0100013'},
    "TOBACCO_SMOKE_EXPOSURE": {'description': 'Exposure to primary or secondhand tobacco smoke', 'meaning': 'ECTO:6000029'},
    "VOLATILE_ORGANIC_COMPOUND": {'description': 'Organic compounds with high vapor pressure', 'meaning': 'ECTO:9001621', 'aliases': ['VOC']},
    "WEATHER": {'description': 'Atmospheric conditions and weather-related exposures', 'meaning': 'ECTO:1000020'},
}

__all__ = [
    "AirPollutantEnum",
    "PesticideTypeEnum",
    "HeavyMetalEnum",
    "ExposureRouteEnum",
    "ExposureSourceEnum",
    "WaterContaminantEnum",
    "EndocrineDisruptorEnum",
    "ExposureDurationEnum",
    "SmokingStatusEnum",
    "ExposureStressorTypeEnum",
    "ExposureTransportPathEnum",
    "ExposureFrequencyEnum",
    "StudyPopulationEnum",
    "HHEARExposureAssessedEnum",
]