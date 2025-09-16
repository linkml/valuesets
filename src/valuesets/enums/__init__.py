"""
Common Value Sets - Rich Enum Collection

This module provides convenient access to all enum definitions.
Each enum includes rich metadata (descriptions, ontology mappings, annotations)
while maintaining full Python enum compatibility.

Usage:
    from valuesets.enums import Presenceenum, AnatomicalSide
    
    # Or import everything
    from valuesets.enums import *
"""

# flake8: noqa

# Academic domain
from .academic.research import PublicationType, PeerReviewStatus, AcademicDegree, LicenseType, ResearchField, FundingType, ManuscriptSection, ResearchRole, OpenAccessType, CitationStyle

# Bio domain
from .bio.biological_colors import EyeColorEnum, HairColorEnum, FlowerColorEnum, AnimalCoatColorEnum, SkinToneEnum, PlantLeafColorEnum
from .bio.cell_cycle import CellCyclePhase, MitoticPhase, CellCycleCheckpoint, MeioticPhase, CellCycleRegulator, CellProliferationState, DNADamageResponse
from .bio.genome_features import GenomeFeatureType
from .bio.go_evidence import GOEvidenceCode, GOElectronicMethods
from .bio.insdc_missing_values import InsdcMissingValueEnum
from .bio.plant_biology import PlantSexualSystem
from .bio.plant_sex import PlantSexEnum
from .bio.relationship_to_oxygen import RelToOxygenEnum
from .bio.sequence_alphabets import DNABaseEnum, DNABaseExtendedEnum, RNABaseEnum, RNABaseExtendedEnum, AminoAcidEnum, AminoAcidExtendedEnum, CodonEnum, NucleotideModificationEnum, SequenceQualityEnum
from .bio.structural_biology import SampleType, StructuralBiologyTechnique, CryoEMPreparationType, CryoEMGridType, VitrificationMethod, CrystallizationMethod, XRaySource, Detector, WorkflowType, FileFormat, DataType, ProcessingStatus
from .bio.taxonomy import CommonOrganismTaxaEnum, TaxonomicRank, BiologicalKingdom
from .bio.trophic_levels import TrophicLevelEnum
from .bio.viral_genome_types import ViralGenomeTypeEnum

# Bioprocessing domain
from .bioprocessing.scale_up import ProcessScaleEnum, BioreactorTypeEnum, FermentationModeEnum, OxygenationStrategyEnum, AgitationTypeEnum, DownstreamProcessEnum, FeedstockTypeEnum, ProductTypeEnum, SterilizationMethodEnum

# Chemistry domain
from .chemistry.chemical_entities import SubatomicParticleEnum, BondTypeEnum, PeriodicTableBlockEnum, ElementFamilyEnum, ElementMetallicClassificationEnum, HardOrSoftEnum, BronstedAcidBaseRoleEnum, LewisAcidBaseRoleEnum, OxidationStateEnum, ChiralityEnum, NanostructureMorphologyEnum
from .chemistry.reactions import ReactionTypeEnum, ReactionMechanismEnum, CatalystTypeEnum, ReactionConditionEnum, ReactionRateOrderEnum, EnzymeClassEnum, SolventClassEnum, ThermodynamicParameterEnum

# Clinical domain
from .clinical.nih_demographics import RaceOMB1997Enum, EthnicityOMB1997Enum, BiologicalSexEnum, GenderIdentityEnum, AgeGroupEnum, ParticipantVitalStatusEnum, RecruitmentStatusEnum, StudyPhaseEnum, EducationLevelEnum
from .clinical.phenopackets import KaryotypicSexEnum, PhenotypicSexEnum, AllelicStateEnum, LateralityEnum, OnsetTimingEnum, ACMGPathogenicityEnum, TherapeuticActionabilityEnum, InterpretationProgressEnum, RegimenStatusEnum, DrugResponseEnum

# Computing domain
from .computing.file_formats import ImageFileFormatEnum, DocumentFormatEnum, DataFormatEnum, ArchiveFormatEnum, VideoFormatEnum, AudioFormatEnum, ProgrammingLanguageFileEnum, NetworkProtocolEnum
from .computing.mime_types import MimeType, MimeTypeCategory, TextCharset, CompressionType

# Core domain
from .core import RelativeTimeEnum, PresenceEnum
from .health import VitalStatusEnum
from .healthcare import HealthcareEncounterClassification
from .investigation import CaseOrControlEnum
from .statistics import PredictionOutcomeType

# Data domain
from .data.data_absent_reason import DataAbsentEnum

# Data_Science domain
from .data_science.binary_classification import BinaryClassificationEnum, SpamClassificationEnum, AnomalyDetectionEnum, ChurnClassificationEnum, FraudDetectionEnum
from .data_science.emotion_classification import BasicEmotionEnum, ExtendedEmotionEnum
from .data_science.priority_severity import PriorityLevelEnum, SeverityLevelEnum, ConfidenceLevelEnum
from .data_science.quality_control import QualityControlEnum, DefectClassificationEnum
from .data_science.sentiment_analysis import SentimentClassificationEnum, FineSentimentClassificationEnum
from .data_science.text_classification import NewsTopicCategoryEnum, ToxicityClassificationEnum, IntentClassificationEnum

# Energy domain
from .energy.energy import EnergySource, EnergyUnit, PowerUnit, EnergyEfficiencyRating, BuildingEnergyStandard, GridType, EnergyStorageType, EmissionScope, CarbonIntensity, ElectricityMarket
from .energy.fossil_fuels import FossilFuelTypeEnum

# Environmental_Health domain
from .environmental_health.exposures import AirPollutantEnum, PesticideTypeEnum, HeavyMetalEnum, ExposureRouteEnum, ExposureSourceEnum, WaterContaminantEnum, EndocrineDisruptorEnum, ExposureDurationEnum

# Geography domain
from .geography.geographic_codes import CountryCodeISO2Enum, CountryCodeISO3Enum, USStateCodeEnum, CanadianProvinceCodeEnum, CompassDirection, RelativeDirection, WindDirection, ContinentEnum, UNRegionEnum, LanguageCodeISO6391enum, TimeZoneEnum, CurrencyCodeISO4217Enum

# Industry domain
from .industry.extractive_industry import ExtractiveIndustryFacilityTypeEnum, ExtractiveIndustryProductTypeEnum, MiningMethodEnum, WellTypeEnum
from .industry.mining import MiningType, MineralCategory, CriticalMineral, CommonMineral, MiningEquipment, OreGrade, MiningPhase, MiningHazard, EnvironmentalImpact
from .industry.safety_colors import SafetyColorEnum, TrafficLightColorEnum, HazmatColorEnum, FireSafetyColorEnum, MaritimeSignalColorEnum, AviationLightColorEnum, ElectricalWireColorEnum

# Materials_Science domain
from .materials_science.characterization_methods import MicroscopyMethodEnum, SpectroscopyMethodEnum, ThermalAnalysisMethodEnum, MechanicalTestingMethodEnum
from .materials_science.crystal_structures import CrystalSystemEnum, BravaisLatticeEnum
from .materials_science.material_properties import ElectricalConductivityEnum, MagneticPropertyEnum, OpticalPropertyEnum, ThermalConductivityEnum, MechanicalBehaviorEnum
from .materials_science.material_types import MaterialClassEnum, PolymerTypeEnum, MetalTypeEnum, CompositeTypeEnum
from .materials_science.pigments_dyes import TraditionalPigmentEnum, IndustrialDyeEnum, FoodColoringEnum, AutomobilePaintColorEnum
from .materials_science.synthesis_methods import SynthesisMethodEnum, CrystalGrowthMethodEnum, AdditiveManufacturingEnum

# Medical domain
from .medical.clinical import BloodTypeEnum, AnatomicalSystemEnum, MedicalSpecialtyEnum, DrugRouteEnum, VitalSignEnum, DiagnosticTestTypeEnum, SymptomSeverityEnum, AllergyTypeEnum, VaccineTypeEnum, BMIClassificationEnum

# Physics domain
from .physics.states_of_matter import StateOfMatterEnum

# Social domain
from .social.person_status import PersonStatusEnum, MaritalStatusEnum, EmploymentStatusEnum

# Spatial domain
from .spatial.spatial_qualifiers import SimpleSpatialDirection, AnatomicalSide, AnatomicalRegion, AnatomicalAxis, AnatomicalPlane, SpatialRelationship, CellPolarity

# Statistics domain
from .statistics.prediction_outcomes import OutcomeTypeEnum

# Time domain
from .time.temporal import DayOfWeek, Month, Quarter, Season, TimePeriod, TimeUnit, TimeOfDay, BusinessTimeFrame, GeologicalEra, HistoricalPeriod

# Units domain
from .units.measurements import LengthUnitEnum, MassUnitEnum, VolumeUnitEnum, TemperatureUnitEnum, TimeUnitEnum, PressureUnitEnum, ConcentrationUnitEnum, FrequencyUnitEnum, AngleUnitEnum, DataSizeUnitEnum

# Visual domain
from .visual.colors import BasicColorEnum, WebColorEnum, X11ColorEnum, ColorSpaceEnum

__all__ = [
    "ACMGPathogenicityEnum",
    "AcademicDegree",
    "AdditiveManufacturingEnum",
    "AgeGroupEnum",
    "AgitationTypeEnum",
    "AirPollutantEnum",
    "AllelicStateEnum",
    "AllergyTypeEnum",
    "AminoAcidEnum",
    "AminoAcidExtendedEnum",
    "AnatomicalAxis",
    "AnatomicalPlane",
    "AnatomicalRegion",
    "AnatomicalSide",
    "AnatomicalSystemEnum",
    "AngleUnitEnum",
    "AnimalCoatColorEnum",
    "AnomalyDetectionEnum",
    "ArchiveFormatEnum",
    "AudioFormatEnum",
    "AutomobilePaintColorEnum",
    "AviationLightColorEnum",
    "BMIClassificationEnum",
    "BasicColorEnum",
    "BasicEmotionEnum",
    "BinaryClassificationEnum",
    "BiologicalKingdom",
    "BiologicalSexEnum",
    "BioreactorTypeEnum",
    "BloodTypeEnum",
    "BondTypeEnum",
    "BravaisLatticeEnum",
    "BronstedAcidBaseRoleEnum",
    "BuildingEnergyStandard",
    "BusinessTimeFrame",
    "CanadianProvinceCodeEnum",
    "CarbonIntensity",
    "CaseOrControlEnum",
    "CatalystTypeEnum",
    "CellCycleCheckpoint",
    "CellCyclePhase",
    "CellCycleRegulator",
    "CellPolarity",
    "CellProliferationState",
    "ChiralityEnum",
    "ChurnClassificationEnum",
    "CitationStyle",
    "CodonEnum",
    "ColorSpaceEnum",
    "CommonMineral",
    "CommonOrganismTaxaEnum",
    "CompassDirection",
    "CompositeTypeEnum",
    "CompressionType",
    "ConcentrationUnitEnum",
    "ConfidenceLevelEnum",
    "ContinentEnum",
    "CountryCodeISO2Enum",
    "CountryCodeISO3Enum",
    "CriticalMineral",
    "CryoEMGridType",
    "CryoEMPreparationType",
    "CrystalGrowthMethodEnum",
    "CrystalSystemEnum",
    "CrystallizationMethod",
    "CurrencyCodeISO4217Enum",
    "DNABaseEnum",
    "DNABaseExtendedEnum",
    "DNADamageResponse",
    "DataAbsentEnum",
    "DataFormatEnum",
    "DataSizeUnitEnum",
    "DataType",
    "DayOfWeek",
    "DefectClassificationEnum",
    "Detector",
    "DiagnosticTestTypeEnum",
    "DocumentFormatEnum",
    "DownstreamProcessEnum",
    "DrugResponseEnum",
    "DrugRouteEnum",
    "EducationLevelEnum",
    "ElectricalConductivityEnum",
    "ElectricalWireColorEnum",
    "ElectricityMarket",
    "ElementFamilyEnum",
    "ElementMetallicClassificationEnum",
    "EmissionScope",
    "EmploymentStatusEnum",
    "EndocrineDisruptorEnum",
    "EnergyEfficiencyRating",
    "EnergySource",
    "EnergyStorageType",
    "EnergyUnit",
    "EnvironmentalImpact",
    "EnzymeClassEnum",
    "EthnicityOMB1997Enum",
    "ExposureDurationEnum",
    "ExposureRouteEnum",
    "ExposureSourceEnum",
    "ExtendedEmotionEnum",
    "ExtractiveIndustryFacilityTypeEnum",
    "ExtractiveIndustryProductTypeEnum",
    "EyeColorEnum",
    "FeedstockTypeEnum",
    "FermentationModeEnum",
    "FileFormat",
    "FineSentimentClassificationEnum",
    "FireSafetyColorEnum",
    "FlowerColorEnum",
    "FoodColoringEnum",
    "FossilFuelTypeEnum",
    "FraudDetectionEnum",
    "FrequencyUnitEnum",
    "FundingType",
    "GOElectronicMethods",
    "GOEvidenceCode",
    "GenderIdentityEnum",
    "GenomeFeatureType",
    "GeologicalEra",
    "GridType",
    "HairColorEnum",
    "HardOrSoftEnum",
    "HazmatColorEnum",
    "HealthcareEncounterClassification",
    "HeavyMetalEnum",
    "HistoricalPeriod",
    "ImageFileFormatEnum",
    "IndustrialDyeEnum",
    "InsdcMissingValueEnum",
    "IntentClassificationEnum",
    "InterpretationProgressEnum",
    "KaryotypicSexEnum",
    "LanguageCodeISO6391enum",
    "LateralityEnum",
    "LengthUnitEnum",
    "LewisAcidBaseRoleEnum",
    "LicenseType",
    "MagneticPropertyEnum",
    "ManuscriptSection",
    "MaritalStatusEnum",
    "MaritimeSignalColorEnum",
    "MassUnitEnum",
    "MaterialClassEnum",
    "MechanicalBehaviorEnum",
    "MechanicalTestingMethodEnum",
    "MedicalSpecialtyEnum",
    "MeioticPhase",
    "MetalTypeEnum",
    "MicroscopyMethodEnum",
    "MimeType",
    "MimeTypeCategory",
    "MineralCategory",
    "MiningEquipment",
    "MiningHazard",
    "MiningMethodEnum",
    "MiningPhase",
    "MiningType",
    "MitoticPhase",
    "Month",
    "NanostructureMorphologyEnum",
    "NetworkProtocolEnum",
    "NewsTopicCategoryEnum",
    "NucleotideModificationEnum",
    "OnsetTimingEnum",
    "OpenAccessType",
    "OpticalPropertyEnum",
    "OreGrade",
    "OutcomeTypeEnum",
    "OxidationStateEnum",
    "OxygenationStrategyEnum",
    "ParticipantVitalStatusEnum",
    "PeerReviewStatus",
    "PeriodicTableBlockEnum",
    "PersonStatusEnum",
    "PesticideTypeEnum",
    "PhenotypicSexEnum",
    "PlantLeafColorEnum",
    "PlantSexEnum",
    "PlantSexualSystem",
    "PolymerTypeEnum",
    "PowerUnit",
    "PredictionOutcomeType",
    "PresenceEnum",
    "PressureUnitEnum",
    "PriorityLevelEnum",
    "ProcessScaleEnum",
    "ProcessingStatus",
    "ProductTypeEnum",
    "ProgrammingLanguageFileEnum",
    "PublicationType",
    "QualityControlEnum",
    "Quarter",
    "RNABaseEnum",
    "RNABaseExtendedEnum",
    "RaceOMB1997Enum",
    "ReactionConditionEnum",
    "ReactionMechanismEnum",
    "ReactionRateOrderEnum",
    "ReactionTypeEnum",
    "RecruitmentStatusEnum",
    "RegimenStatusEnum",
    "RelToOxygenEnum",
    "RelativeDirection",
    "RelativeTimeEnum",
    "ResearchField",
    "ResearchRole",
    "SafetyColorEnum",
    "SampleType",
    "Season",
    "SentimentClassificationEnum",
    "SequenceQualityEnum",
    "SeverityLevelEnum",
    "SimpleSpatialDirection",
    "SkinToneEnum",
    "SolventClassEnum",
    "SpamClassificationEnum",
    "SpatialRelationship",
    "SpectroscopyMethodEnum",
    "StateOfMatterEnum",
    "SterilizationMethodEnum",
    "StructuralBiologyTechnique",
    "StudyPhaseEnum",
    "SubatomicParticleEnum",
    "SymptomSeverityEnum",
    "SynthesisMethodEnum",
    "TaxonomicRank",
    "TemperatureUnitEnum",
    "TextCharset",
    "TherapeuticActionabilityEnum",
    "ThermalAnalysisMethodEnum",
    "ThermalConductivityEnum",
    "ThermodynamicParameterEnum",
    "TimeOfDay",
    "TimePeriod",
    "TimeUnit",
    "TimeUnitEnum",
    "TimeZoneEnum",
    "ToxicityClassificationEnum",
    "TraditionalPigmentEnum",
    "TrafficLightColorEnum",
    "TrophicLevelEnum",
    "UNRegionEnum",
    "USStateCodeEnum",
    "VaccineTypeEnum",
    "VideoFormatEnum",
    "ViralGenomeTypeEnum",
    "VitalSignEnum",
    "VitalStatusEnum",
    "VitrificationMethod",
    "VolumeUnitEnum",
    "WaterContaminantEnum",
    "WebColorEnum",
    "WellTypeEnum",
    "WindDirection",
    "WorkflowType",
    "X11ColorEnum",
    "XRaySource",
]