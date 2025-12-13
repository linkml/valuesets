"""
valuesets-vaccination

Vaccination-related value sets

Generated from: health/vaccination.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class VaccinationStatusEnum(RichEnum):
    """
    The vaccination status of an individual
    """
    # Enum members
    VACCINATED = "VACCINATED"
    NOT_VACCINATED = "NOT_VACCINATED"
    FULLY_VACCINATED = "FULLY_VACCINATED"
    PARTIALLY_VACCINATED = "PARTIALLY_VACCINATED"
    BOOSTER = "BOOSTER"
    UNVACCINATED = "UNVACCINATED"
    UNKNOWN = "UNKNOWN"

# Set metadata after class creation
VaccinationStatusEnum._metadata = {
    "VACCINATED": {'description': 'A status indicating that an individual has received a vaccination', 'meaning': 'NCIT:C28385'},
    "NOT_VACCINATED": {'description': 'A status indicating that an individual has not received any of the required vaccinations', 'meaning': 'NCIT:C183125'},
    "FULLY_VACCINATED": {'description': 'A status indicating that an individual has received all the required vaccinations', 'meaning': 'NCIT:C183123'},
    "PARTIALLY_VACCINATED": {'description': 'A status indicating that an individual has received some of the required vaccinations', 'meaning': 'NCIT:C183124'},
    "BOOSTER": {'description': 'A status indicating that an individual has received a booster vaccination', 'meaning': 'NCIT:C28320'},
    "UNVACCINATED": {'description': 'An organismal quality that indicates an organism is unvaccinated with any vaccine', 'meaning': 'VO:0001377'},
    "UNKNOWN": {'description': 'The vaccination status is not known', 'meaning': 'NCIT:C17998'},
}

class VaccinationPeriodicityEnum(RichEnum):
    """
    The periodicity or frequency of vaccination
    """
    # Enum members
    SINGLE_DOSE = "SINGLE_DOSE"
    ANNUAL = "ANNUAL"
    SEASONAL = "SEASONAL"
    BOOSTER = "BOOSTER"
    PRIMARY_SERIES = "PRIMARY_SERIES"
    PERIODIC = "PERIODIC"
    ONE_TIME = "ONE_TIME"
    AS_NEEDED = "AS_NEEDED"

# Set metadata after class creation
VaccinationPeriodicityEnum._metadata = {
    "SINGLE_DOSE": {'description': 'A vaccination regimen requiring only one dose'},
    "ANNUAL": {'description': 'Vaccination occurring once per year', 'meaning': 'NCIT:C54647'},
    "SEASONAL": {'description': 'Vaccination occurring seasonally (e.g., for influenza)'},
    "BOOSTER": {'description': 'A second or later vaccine dose to maintain immune response', 'meaning': 'NCIT:C28320'},
    "PRIMARY_SERIES": {'description': 'The initial series of vaccine doses'},
    "PERIODIC": {'description': 'Vaccination occurring at regular intervals'},
    "ONE_TIME": {'description': 'A vaccination given only once in a lifetime'},
    "AS_NEEDED": {'description': 'Vaccination given as needed based on exposure risk or other factors'},
}

class VaccineCategoryEnum(RichEnum):
    """
    The broad category or type of vaccine
    """
    # Enum members
    LIVE_ATTENUATED_VACCINE = "LIVE_ATTENUATED_VACCINE"
    INACTIVATED_VACCINE = "INACTIVATED_VACCINE"
    CONJUGATE_VACCINE = "CONJUGATE_VACCINE"
    MRNA_VACCINE = "MRNA_VACCINE"
    DNA_VACCINE = "DNA_VACCINE"
    PEPTIDE_VACCINE = "PEPTIDE_VACCINE"
    VIRAL_VECTOR = "VIRAL_VECTOR"
    SUBUNIT = "SUBUNIT"
    TOXOID = "TOXOID"
    RECOMBINANT = "RECOMBINANT"

# Set metadata after class creation
VaccineCategoryEnum._metadata = {
    "LIVE_ATTENUATED_VACCINE": {'description': 'A vaccine made from microbes that have been weakened in the laboratory', 'meaning': 'VO:0000367'},
    "INACTIVATED_VACCINE": {'description': 'A preparation of killed microorganisms intended to prevent infectious disease', 'meaning': 'NCIT:C29694'},
    "CONJUGATE_VACCINE": {'description': 'A vaccine created by covalently attaching an antigen to a carrier protein', 'meaning': 'NCIT:C1455'},
    "MRNA_VACCINE": {'description': 'A vaccine based on mRNA that encodes the antigen of interest', 'meaning': 'NCIT:C172787'},
    "DNA_VACCINE": {'description': 'A vaccine using DNA to produce protein that promotes immune responses', 'meaning': 'NCIT:C39619'},
    "PEPTIDE_VACCINE": {'description': 'A vaccine based on synthetic peptides', 'meaning': 'NCIT:C1752'},
    "VIRAL_VECTOR": {'description': 'A vaccine using a modified virus as a delivery system'},
    "SUBUNIT": {'description': 'A vaccine containing purified pieces of the pathogen'},
    "TOXOID": {'description': 'A vaccine made from a toxin that has been made harmless'},
    "RECOMBINANT": {'description': 'A vaccine produced using recombinant DNA technology'},
}

__all__ = [
    "VaccinationStatusEnum",
    "VaccinationPeriodicityEnum",
    "VaccineCategoryEnum",
]