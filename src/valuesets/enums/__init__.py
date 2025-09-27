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
from .bio.currency_chemicals import CurrencyChemical
from .bio.developmental_stages import HumanDevelopmentalStage, MouseDevelopmentalStage
from .bio.genome_features import GenomeFeatureType
from .bio.genomics import CdsPhaseType, ContigCollectionType, StrandType, SequenceType
from .bio.go_evidence import GOEvidenceCode, GOElectronicMethods
from .bio.insdc_geographic_locations import InsdcGeographicLocationEnum
from .bio.insdc_missing_values import InsdcMissingValueEnum
from .bio.lipid_categories import RelativeTimeEnum, PresenceEnum, LipidCategory
from .bio.plant_biology import PlantSexualSystem
from .bio.plant_developmental_stages import PlantDevelopmentalStage
from .bio.plant_sex import PlantSexEnum
from .bio.protein_evidence import ProteinEvidenceForExistence, RefSeqStatusType
from .bio.proteomics_standards import RelativeTimeEnum, PresenceEnum, PeakAnnotationSeriesLabel, PeptideIonSeries, MassErrorUnit
from .bio.psi_mi import InteractionDetectionMethod, InteractionType, ExperimentalRole, BiologicalRole, ParticipantIdentificationMethod, FeatureType, InteractorType, ConfidenceScore, ExperimentalPreparation
from .bio.relationship_to_oxygen import RelToOxygenEnum
from .bio.sequence_alphabets import DNABaseEnum, DNABaseExtendedEnum, RNABaseEnum, RNABaseExtendedEnum, AminoAcidEnum, AminoAcidExtendedEnum, CodonEnum, NucleotideModificationEnum, SequenceQualityEnum
from .bio.sequence_chemistry import DNABase, RNABase, IUPACNucleotideCode, StandardAminoAcid, IUPACAminoAcidCode, SequenceAlphabet, SequenceQualityEncoding, GeneticCodeTable, SequenceStrand, SequenceTopology, SequenceModality
from .bio.sequencing_platforms import SequencingPlatform, SequencingChemistry, LibraryPreparation, SequencingApplication, ReadType, SequenceFileFormat, DataProcessingLevel
from .bio.structural_biology import SampleType, StructuralBiologyTechnique, CryoEMPreparationType, CryoEMGridType, VitrificationMethod, CrystallizationMethod, XRaySource, Detector, WorkflowType, FileFormat, DataType, ProcessingStatus
from .bio.taxonomy import CommonOrganismTaxaEnum, TaxonomicRank, BiologicalKingdom
from .bio.trophic_levels import TrophicLevelEnum
from .bio.uniprot_species import UniProtSpeciesCode
from .bio.viral_genome_types import ViralGenomeTypeEnum

# Bioprocessing domain
from .bioprocessing.scale_up import ProcessScaleEnum, BioreactorTypeEnum, FermentationModeEnum, OxygenationStrategyEnum, AgitationTypeEnum, DownstreamProcessEnum, FeedstockTypeEnum, ProductTypeEnum, SterilizationMethodEnum

# Chemistry domain
from .chemistry.chemical_entities import SubatomicParticleEnum, BondTypeEnum, PeriodicTableBlockEnum, ElementFamilyEnum, ElementMetallicClassificationEnum, HardOrSoftEnum, BronstedAcidBaseRoleEnum, LewisAcidBaseRoleEnum, OxidationStateEnum, ChiralityEnum, NanostructureMorphologyEnum
from .chemistry.reaction_directionality import RelativeTimeEnum, PresenceEnum, ReactionDirectionality
from .chemistry.reactions import ReactionTypeEnum, ReactionMechanismEnum, CatalystTypeEnum, ReactionConditionEnum, ReactionRateOrderEnum, EnzymeClassEnum, SolventClassEnum, ThermodynamicParameterEnum

# Clinical domain
from .clinical.nih_demographics import RaceOMB1997Enum, EthnicityOMB1997Enum, BiologicalSexEnum, GenderIdentityEnum, AgeGroupEnum, ParticipantVitalStatusEnum, RecruitmentStatusEnum, StudyPhaseEnum, EducationLevelEnum
from .clinical.phenopackets import KaryotypicSexEnum, PhenotypicSexEnum, AllelicStateEnum, LateralityEnum, OnsetTimingEnum, ACMGPathogenicityEnum, TherapeuticActionabilityEnum, InterpretationProgressEnum, RegimenStatusEnum, DrugResponseEnum

# Computing domain
from .computing.file_formats import ImageFileFormatEnum, DocumentFormatEnum, DataFormatEnum, ArchiveFormatEnum, VideoFormatEnum, AudioFormatEnum, ProgrammingLanguageFileEnum, NetworkProtocolEnum
from .computing.maturity_levels import TechnologyReadinessLevel, SoftwareMaturityLevel, CapabilityMaturityLevel, StandardsMaturityLevel, ProjectMaturityLevel, DataMaturityLevel, OpenSourceMaturityLevel
from .computing.mime_types import MimeType, MimeTypeCategory, TextCharset, CompressionType

# Core domain
from .confidence_levels import RelativeTimeEnum, PresenceEnum, ConfidenceLevel, CIOConfidenceLevel, OBCSCertaintyLevel, IPCCLikelihoodScale, IPCCConfidenceLevel, NCITFivePointConfidenceScale
from .contributor import ContributorType
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
    "AcademicDomainEnum",
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
    "BinaryClassificationSchemaEnum",
    "BioDomainEnum",
    "BioEntitiesSchemaEnum",
    "BiologicalColorsSchemaEnum",
    "BiologicalKingdom",
    "BiologicalRole",
    "BiologicalSexEnum",
    "BioprocessingDomainEnum",
    "BioreactorTypeEnum",
    "BloodTypeEnum",
    "BondTypeEnum",
    "BravaisLatticeEnum",
    "BronstedAcidBaseRoleEnum",
    "BuildingEnergyStandard",
    "BusinessTimeFrame",
    "CIOConfidenceLevel",
    "CanadianProvinceCodeEnum",
    "CapabilityMaturityLevel",
    "CarbonIntensity",
    "CaseOrControlEnum",
    "CatalystTypeEnum",
    "CdsPhaseType",
    "CellCycleCheckpoint",
    "CellCyclePhase",
    "CellCycleRegulator",
    "CellCycleSchemaEnum",
    "CellPolarity",
    "CellProliferationState",
    "CharacterizationMethodsSchemaEnum",
    "ChemicalEntitiesSchemaEnum",
    "ChemistryDomainEnum",
    "ChiralityEnum",
    "ChurnClassificationEnum",
    "CitationStyle",
    "ClinicalDomainEnum",
    "ClinicalSchemaEnum",
    "CodonEnum",
    "ColorSpaceEnum",
    "ColorsSchemaEnum",
    "CommonMineral",
    "CommonOrganismTaxaEnum",
    "CompassDirection",
    "CompositeTypeEnum",
    "CompressionType",
    "ComputingDomainEnum",
    "ConcentrationUnitEnum",
    "ConfidenceLevel",
    "ConfidenceLevelEnum",
    "ConfidenceLevelsSchemaEnum",
    "ConfidenceScore",
    "ContigCollectionType",
    "ContinentEnum",
    "ContributorSchemaEnum",
    "ContributorType",
    "CoreSchemaEnum",
    "CountryCodeISO2Enum",
    "CountryCodeISO3Enum",
    "CriticalMineral",
    "CryoEMGridType",
    "CryoEMPreparationType",
    "CrystalGrowthMethodEnum",
    "CrystalStructuresSchemaEnum",
    "CrystalSystemEnum",
    "CrystallizationMethod",
    "CurrencyChemical",
    "CurrencyChemicalsSchemaEnum",
    "CurrencyCodeISO4217Enum",
    "DNABase",
    "DNABaseEnum",
    "DNABaseExtendedEnum",
    "DNADamageResponse",
    "DataAbsentEnum",
    "DataAbsentReasonSchemaEnum",
    "DataDomainEnum",
    "DataFormatEnum",
    "DataMaturityLevel",
    "DataProcessingLevel",
    "DataScienceDomainEnum",
    "DataSizeUnitEnum",
    "DataType",
    "DayOfWeek",
    "DefectClassificationEnum",
    "Detector",
    "DevelopmentalStagesSchemaEnum",
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
    "EmotionClassificationSchemaEnum",
    "EmploymentStatusEnum",
    "EndocrineDisruptorEnum",
    "EnergyDomainEnum",
    "EnergyEfficiencyRating",
    "EnergySchemaEnum",
    "EnergySource",
    "EnergyStorageType",
    "EnergyUnit",
    "EnvironmentalHealthDomainEnum",
    "EnvironmentalImpact",
    "EnzymeClassEnum",
    "EthnicityOMB1997Enum",
    "ExperimentalPreparation",
    "ExperimentalRole",
    "ExposureDurationEnum",
    "ExposureRouteEnum",
    "ExposureSourceEnum",
    "ExposuresSchemaEnum",
    "ExtendedEmotionEnum",
    "ExtractiveIndustryFacilityTypeEnum",
    "ExtractiveIndustryProductTypeEnum",
    "ExtractiveIndustrySchemaEnum",
    "EyeColorEnum",
    "FeatureType",
    "FeedstockTypeEnum",
    "FermentationModeEnum",
    "FileFormat",
    "FileFormatsSchemaEnum",
    "FineSentimentClassificationEnum",
    "FireSafetyColorEnum",
    "FlowerColorEnum",
    "FoodColoringEnum",
    "FossilFuelTypeEnum",
    "FossilFuelsSchemaEnum",
    "FraudDetectionEnum",
    "FrequencyUnitEnum",
    "FundingType",
    "GOElectronicMethods",
    "GOEvidenceCode",
    "GenderIdentityEnum",
    "GeneticCodeTable",
    "GenomeFeatureType",
    "GenomeFeaturesSchemaEnum",
    "GenomicsSchemaEnum",
    "GeographicCodesSchemaEnum",
    "GeographyDomainEnum",
    "GeologicalEra",
    "GoEvidenceSchemaEnum",
    "GridType",
    "HairColorEnum",
    "HardOrSoftEnum",
    "HazmatColorEnum",
    "HealthSchemaEnum",
    "HealthcareEncounterClassification",
    "HealthcareSchemaEnum",
    "HeavyMetalEnum",
    "HistoricalPeriod",
    "HumanDevelopmentalStage",
    "IPCCConfidenceLevel",
    "IPCCLikelihoodScale",
    "IUPACAminoAcidCode",
    "IUPACNucleotideCode",
    "ImageFileFormatEnum",
    "IndustrialDyeEnum",
    "IndustryDomainEnum",
    "InsdcGeographicLocationEnum",
    "InsdcGeographicLocationsSchemaEnum",
    "InsdcMissingValueEnum",
    "InsdcMissingValuesSchemaEnum",
    "IntentClassificationEnum",
    "InteractionDetectionMethod",
    "InteractionType",
    "InteractorType",
    "InterpretationProgressEnum",
    "InvestigationSchemaEnum",
    "KaryotypicSexEnum",
    "LanguageCodeISO6391enum",
    "LateralityEnum",
    "LengthUnitEnum",
    "LewisAcidBaseRoleEnum",
    "LibraryPreparation",
    "LicenseType",
    "LipidCategoriesSchemaEnum",
    "LipidCategory",
    "MagneticPropertyEnum",
    "ManuscriptSection",
    "MaritalStatusEnum",
    "MaritimeSignalColorEnum",
    "MassErrorUnit",
    "MassUnitEnum",
    "MaterialClassEnum",
    "MaterialPropertiesSchemaEnum",
    "MaterialTypesSchemaEnum",
    "MaterialsScienceDomainEnum",
    "MaturityLevelsSchemaEnum",
    "MeasurementsSchemaEnum",
    "MechanicalBehaviorEnum",
    "MechanicalTestingMethodEnum",
    "MedicalDomainEnum",
    "MedicalSpecialtyEnum",
    "MeioticPhase",
    "MetalTypeEnum",
    "MicroscopyMethodEnum",
    "MimeType",
    "MimeTypeCategory",
    "MimeTypesSchemaEnum",
    "MineralCategory",
    "MiningEquipment",
    "MiningHazard",
    "MiningMethodEnum",
    "MiningPhase",
    "MiningSchemaEnum",
    "MiningType",
    "MitoticPhase",
    "Month",
    "MouseDevelopmentalStage",
    "NCITFivePointConfidenceScale",
    "NanostructureMorphologyEnum",
    "NetworkProtocolEnum",
    "NewsTopicCategoryEnum",
    "NihDemographicsSchemaEnum",
    "NucleotideModificationEnum",
    "OBCSCertaintyLevel",
    "OnsetTimingEnum",
    "OpenAccessType",
    "OpenSourceMaturityLevel",
    "OpticalPropertyEnum",
    "OreGrade",
    "OutcomeTypeEnum",
    "OxidationStateEnum",
    "OxygenationStrategyEnum",
    "ParticipantIdentificationMethod",
    "ParticipantVitalStatusEnum",
    "PeakAnnotationSeriesLabel",
    "PeerReviewStatus",
    "PeptideIonSeries",
    "PeriodicTableBlockEnum",
    "PersonStatusEnum",
    "PersonStatusSchemaEnum",
    "PesticideTypeEnum",
    "PhenopacketsSchemaEnum",
    "PhenotypicSexEnum",
    "PhysicsDomainEnum",
    "PigmentsDyesSchemaEnum",
    "PlantBiologySchemaEnum",
    "PlantDevelopmentalStage",
    "PlantDevelopmentalStagesSchemaEnum",
    "PlantLeafColorEnum",
    "PlantSexEnum",
    "PlantSexSchemaEnum",
    "PlantSexualSystem",
    "PolymerTypeEnum",
    "PowerUnit",
    "PredictionOutcomeType",
    "PredictionOutcomesSchemaEnum",
    "PresenceEnum",
    "PressureUnitEnum",
    "PriorityLevelEnum",
    "PrioritySeveritySchemaEnum",
    "ProcessScaleEnum",
    "ProcessingStatus",
    "ProductTypeEnum",
    "ProgrammingLanguageFileEnum",
    "ProjectMaturityLevel",
    "ProteinEvidenceForExistence",
    "ProteinEvidenceSchemaEnum",
    "ProteomicsStandardsSchemaEnum",
    "PsiMiSchemaEnum",
    "PublicationType",
    "QualityControlEnum",
    "QualityControlSchemaEnum",
    "Quarter",
    "RNABase",
    "RNABaseEnum",
    "RNABaseExtendedEnum",
    "RaceOMB1997Enum",
    "ReactionConditionEnum",
    "ReactionDirectionality",
    "ReactionDirectionalitySchemaEnum",
    "ReactionMechanismEnum",
    "ReactionRateOrderEnum",
    "ReactionTypeEnum",
    "ReactionsSchemaEnum",
    "ReadType",
    "RecruitmentStatusEnum",
    "RefSeqStatusType",
    "RegimenStatusEnum",
    "RelToOxygenEnum",
    "RelationshipToOxygenSchemaEnum",
    "RelativeDirection",
    "RelativeTimeEnum",
    "ResearchField",
    "ResearchRole",
    "ResearchSchemaEnum",
    "RootDomainEnum",
    "SafetyColorEnum",
    "SafetyColorsSchemaEnum",
    "SampleType",
    "ScaleUpSchemaEnum",
    "Season",
    "SentimentAnalysisSchemaEnum",
    "SentimentClassificationEnum",
    "SequenceAlphabet",
    "SequenceAlphabetsSchemaEnum",
    "SequenceChemistrySchemaEnum",
    "SequenceFileFormat",
    "SequenceModality",
    "SequenceQualityEncoding",
    "SequenceQualityEnum",
    "SequenceStrand",
    "SequenceTopology",
    "SequenceType",
    "SequencingApplication",
    "SequencingChemistry",
    "SequencingPlatform",
    "SequencingPlatformsSchemaEnum",
    "SeverityLevelEnum",
    "SimpleSpatialDirection",
    "SkinToneEnum",
    "SocialDomainEnum",
    "SoftwareMaturityLevel",
    "SolventClassEnum",
    "SpamClassificationEnum",
    "SpatialDomainEnum",
    "SpatialQualifiersSchemaEnum",
    "SpatialRelationship",
    "SpectroscopyMethodEnum",
    "StandardAminoAcid",
    "StandardsMaturityLevel",
    "StateOfMatterEnum",
    "StatesOfMatterSchemaEnum",
    "StatisticsDomainEnum",
    "StatisticsSchemaEnum",
    "SterilizationMethodEnum",
    "StrandType",
    "StructuralBiologySchemaEnum",
    "StructuralBiologyTechnique",
    "StudyPhaseEnum",
    "SubatomicParticleEnum",
    "SymptomSeverityEnum",
    "SynthesisMethodEnum",
    "SynthesisMethodsSchemaEnum",
    "TaxonomicRank",
    "TaxonomySchemaEnum",
    "TechnologyReadinessLevel",
    "TemperatureUnitEnum",
    "TemporalSchemaEnum",
    "TextCharset",
    "TextClassificationSchemaEnum",
    "TherapeuticActionabilityEnum",
    "ThermalAnalysisMethodEnum",
    "ThermalConductivityEnum",
    "ThermodynamicParameterEnum",
    "TimeDomainEnum",
    "TimeOfDay",
    "TimePeriod",
    "TimeUnit",
    "TimeUnitEnum",
    "TimeZoneEnum",
    "ToxicityClassificationEnum",
    "TraditionalPigmentEnum",
    "TrafficLightColorEnum",
    "TrophicLevelEnum",
    "TrophicLevelsSchemaEnum",
    "UNRegionEnum",
    "USStateCodeEnum",
    "UniProtSpeciesCode",
    "UniprotSpeciesSchemaEnum",
    "UnitsDomainEnum",
    "VaccineTypeEnum",
    "ValueSetEnum",
    "VideoFormatEnum",
    "ViralGenomeTypeEnum",
    "ViralGenomeTypesSchemaEnum",
    "VisualDomainEnum",
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