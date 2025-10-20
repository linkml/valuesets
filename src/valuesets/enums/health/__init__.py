"""Health-related enums."""

# Import from base health module and vaccination module
from ..health_base import VitalStatusEnum
from .vaccination import VaccinationStatusEnum, VaccinationPeriodicityEnum, VaccineCategoryEnum

__all__ = [
    "VitalStatusEnum",
    "VaccinationStatusEnum",
    "VaccinationPeriodicityEnum",
    "VaccineCategoryEnum"
]