"""
valuesets-environmental-health-exposures

Environmental health and exposure-related value sets

Generated from: environmental_health/exposures.yaml
"""

from __future__ import annotations

from typing import Dict, Any, Optional
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
    MULTIPLE_ROUTES = "MULTIPLE_ROUTES"

# Set metadata after class creation
ExposureRouteEnum._metadata = {
    "INHALATION": {'description': 'Exposure through breathing', 'meaning': 'NCIT:C38284'},
    "INGESTION": {'description': 'Exposure through eating or drinking', 'meaning': 'NCIT:C38288'},
    "DERMAL": {'description': 'Exposure through skin contact', 'meaning': 'NCIT:C38675'},
    "INJECTION": {'description': 'Exposure through injection', 'meaning': 'NCIT:C38276'},
    "TRANSPLACENTAL": {'description': 'Exposure through placental transfer', 'meaning': 'NCIT:C38307'},
    "OCULAR": {'description': 'Exposure through the eyes', 'meaning': 'NCIT:C38287'},
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

__all__ = [
    "AirPollutantEnum",
    "PesticideTypeEnum",
    "HeavyMetalEnum",
    "ExposureRouteEnum",
    "ExposureSourceEnum",
    "WaterContaminantEnum",
    "EndocrineDisruptorEnum",
    "ExposureDurationEnum",
]