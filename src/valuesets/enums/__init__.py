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
from .academic.organizations import USDOENationalLaboratoryEnum, USFederalFundingAgencyEnum, NIHInstituteCenterEnum, StandardsOrganizationEnum, UNSpecializedAgencyEnum
from .academic.research import PublicationType, PeerReviewStatus, AcademicDegree, LicenseType, ResearchField, FundingType, ManuscriptSection, ResearchRole, OpenAccessType, CitationStyle

# Analytical_Chemistry domain
from .analytical_chemistry.mass_spectrometry import RelativeTimeEnum, PresenceEnum, MassSpectrometerFileFormat, MassSpectrometerVendor, ChromatographyType, DerivatizationMethod, MetabolomicsAssayType, AnalyticalControlType

# Bio domain
from .bio.assays import SequencingAssayEnum, ImagingAssayEnum, MassSpectrometryAssayEnum, CellBasedAssayEnum, ClinicalBehavioralAssayEnum
from .bio.bgc_categories import BgcCategoryEnum
from .bio.biological_colors import EyeColorEnum, HairColorEnum, FlowerColorEnum, AnimalCoatColorEnum, SkinToneEnum, PlantLeafColorEnum
from .bio.biosafety import BiosafetyLevelEnum
from .bio.cell_cycle import CellCyclePhase, MitoticPhase, CellCycleCheckpoint, MeioticPhase, CellCycleRegulator, CellProliferationState, DNADamageResponse
from .bio.currency_chemicals import CurrencyChemical
from .bio.developmental_stages import HumanDevelopmentalStage, MouseDevelopmentalStage, HumanAgeGroupEnum, MousePostnatalAgeGroupEnum
from .bio.expression_units import ExpressionUnitEnum, ConcentrationUnitEnum, TimeUnitEnum
from .bio.gene_perturbation import GenePerturbationMethodEnum, GeneKnockoutMethodEnum, GenotypeEnum, VectorTypeEnum
from .bio.genome_features import GenomeFeatureType
from .bio.genomics import CdsPhaseType, ContigCollectionType, StrandType, SequenceType
from .bio.go_aspect import GOAspect
from .bio.go_causality import CausalPredicateEnum
from .bio.go_evidence import GOEvidenceCode, GOElectronicMethods
from .bio.insdc_geographic_locations import InsdcGeographicLocationEnum
from .bio.insdc_missing_values import InsdcMissingValueEnum
from .bio.lipid_categories import RelativeTimeEnum, PresenceEnum, LipidCategory
from .bio.plant_biology import PlantSexualSystem
from .bio.plant_developmental_stages import PlantDevelopmentalStage
from .bio.plant_experimental_conditions import PlantStudyConditionEnum, SeasonalEnvironmentExposureEnum, EcologicalEnvironmentExposureEnum, PlantGrowthMediumExposureEnum
from .bio.plant_sex import PlantSexEnum
from .bio.protein_evidence import ProteinEvidenceForExistence, RefSeqStatusType
from .bio.proteomics_standards import RelativeTimeEnum, PresenceEnum, PeakAnnotationSeriesLabel, PeptideIonSeries, MassErrorUnit
from .bio.psi_mi import InteractionDetectionMethod, InteractionType, ExperimentalRole, BiologicalRole, ParticipantIdentificationMethod, FeatureType, InteractorType, ConfidenceScore, ExperimentalPreparation
from .bio.relationship_to_oxygen import RelToOxygenEnum
from .bio.sequence_alphabets import DNABaseEnum, DNABaseExtendedEnum, RNABaseEnum, RNABaseExtendedEnum, AminoAcidEnum, AminoAcidExtendedEnum, CodonEnum, NucleotideModificationEnum, SequenceQualityEnum
from .bio.sequence_chemistry import IUPACNucleotideCode, StandardAminoAcid, IUPACAminoAcidCode, SequenceAlphabet, SequenceQualityEncoding, GeneticCodeTable, SequenceStrand, SequenceTopology, SequenceModality
from .bio.sequencing_platforms import SequencingPlatform, SequencingChemistry, LibraryPreparation, SequencingApplication, ReadType, SequenceFileFormat, DataProcessingLevel
from .bio.specimen_processing import SpecimenPreparationMethodEnum, TissuePreservationEnum, SpecimenCollectionMethodEnum, SpecimenTypeEnum, AnalyteTypeEnum, SourceMaterialTypeEnum, SpecimenCreationActivityTypeEnum, SpecimenProcessingActivityTypeEnum, SpecimenQualityObservationTypeEnum, SpecimenQualityObservationMethodEnum, SpecimenQuantityObservationTypeEnum, SectionLocationEnum
from .bio.structural_biology import SampleType, StructuralBiologyTechnique, CryoEMPreparationType, CryoEMGridType, VitrificationMethod, CrystallizationMethod, XRaySource, Detector, WorkflowType, FileFormat, DataType, ProcessingStatus, CoordinationGeometry, MetalLigandType, ProteinModificationType
from .bio.taxonomy import CommonOrganismTaxaEnum, TaxonomicRank, BiologicalKingdom
from .bio.transplantation import TransplantationTypeEnum, XenograftModelEnum, ModelSystemTypeEnum
from .bio.trophic_levels import TrophicLevelEnum
from .bio.uniprot_species import UniProtSpeciesCode
from .bio.viral_genome_types import ViralGenomeTypeEnum

# Bioprocessing domain
from .bioprocessing.scale_up import ProcessScaleEnum, BioreactorTypeEnum, FermentationModeEnum, OxygenationStrategyEnum, AgitationTypeEnum, DownstreamProcessEnum, FeedstockTypeEnum, ProductTypeEnum, SterilizationMethodEnum

# Business domain
from .business.human_resources import EmploymentTypeEnum, JobLevelEnum, HRFunctionEnum, CompensationTypeEnum, PerformanceRatingEnum, RecruitmentSourceEnum, TrainingTypeEnum, EmployeeStatusEnum, WorkArrangementEnum, BenefitsCategoryEnum
from .business.industry_classifications import NAICSSectorEnum, EconomicSectorEnum, BusinessActivityTypeEnum, IndustryMaturityEnum, MarketStructureEnum, IndustryRegulationLevelEnum
from .business.management_operations import ManagementMethodologyEnum, StrategicFrameworkEnum, OperationalModelEnum, PerformanceMeasurementEnum, DecisionMakingStyleEnum, LeadershipStyleEnum, BusinessProcessTypeEnum
from .business.organizational_structures import LegalEntityTypeEnum, OrganizationalStructureEnum, ManagementLevelEnum, CorporateGovernanceRoleEnum, BusinessOwnershipTypeEnum, BusinessSizeClassificationEnum, BusinessLifecycleStageEnum
from .business.quality_management import QualityStandardEnum, QualityMethodologyEnum, QualityControlTechniqueEnum, QualityAssuranceLevelEnum, ProcessImprovementApproachEnum, QualityMaturityLevelEnum
from .business.supply_chain import ProcurementTypeEnum, VendorCategoryEnum, SupplyChainStrategyEnum, LogisticsOperationEnum, SourcingStrategyEnum, SupplierRelationshipTypeEnum, InventoryManagementApproachEnum

# Chemistry domain
from .chemistry.chemical_entities import SubatomicParticleEnum, BondTypeEnum, PeriodicTableBlockEnum, ElementFamilyEnum, ElementMetallicClassificationEnum, HardOrSoftEnum, BronstedAcidBaseRoleEnum, LewisAcidBaseRoleEnum, OxidationStateEnum, ChiralityEnum, NanostructureMorphologyEnum
from .chemistry.reaction_directionality import RelativeTimeEnum, PresenceEnum, ReactionDirectionality
from .chemistry.reactions import ReactionTypeEnum, ReactionMechanismEnum, CatalystTypeEnum, ReactionConditionEnum, ReactionRateOrderEnum, EnzymeClassEnum, SolventClassEnum, ThermodynamicParameterEnum

# Clinical domain
from .clinical.genetics import ModeOfInheritance
from .clinical.nih_demographics import RaceOMB1997Enum, EthnicityOMB1997Enum, BiologicalSexEnum, AgeGroupEnum, ParticipantVitalStatusEnum, RecruitmentStatusEnum, StudyPhaseEnum
from .clinical.phenopackets import KaryotypicSexEnum, PhenotypicSexEnum, AllelicStateEnum, LateralityEnum, OnsetTimingEnum, ACMGPathogenicityEnum, TherapeuticActionabilityEnum, InterpretationProgressEnum, RegimenStatusEnum, DrugResponseEnum
from .clinical.provenance import ConditionProvenanceEnum, VisitProvenanceEnum, DrugExposureProvenanceEnum, StatusEnum, HistoricalStatusEnum, ResearchProjectTypeEnum

# Computing domain
from .computing.croissant_ml import MLDataType, DatasetEncodingFormat, DatasetSplitType, MLLicenseType, MLFieldRole, CompressionFormat, MLMediaType, MLModalityType
from .computing.file_formats import ImageFileFormatEnum, DocumentFormatEnum, DataFormatEnum, ArchiveFormatEnum, VideoFormatEnum, AudioFormatEnum, ProgrammingLanguageFileEnum, NetworkProtocolEnum
from .computing.geospatial_formats import GeospatialRasterFormat, GeospatialVectorFormat
from .computing.maturity_levels import TechnologyReadinessLevel, SoftwareMaturityLevel, CapabilityMaturityLevel, StandardsMaturityLevel, ProjectMaturityLevel, DataMaturityLevel, OpenSourceMaturityLevel
from .computing.mime_types import MimeType, MimeTypeCategory, TextCharset, CompressionType
from .computing.ontologies import OWLProfileEnum

# Core domain
from .confidence_levels import RelativeTimeEnum, PresenceEnum, ConfidenceLevel, CIOConfidenceLevel, OBCSCertaintyLevel, IPCCLikelihoodScale, IPCCConfidenceLevel, NCITFivePointConfidenceScale
from .contributor import ContributorType
from .core import RelativeTimeEnum, PresenceEnum
from .demographics import EducationLevel, MaritalStatus, EmploymentStatus, HousingStatus, GenderIdentity, OmbRaceCategory, OmbEthnicityCategory
from .ecological_interactions import RelativeTimeEnum, PresenceEnum, BioticInteractionType
from .health import VitalStatusEnum
from .healthcare import HealthcareEncounterClassification
from .investigation import CaseOrControlEnum, PlannedProcessCompletionStatus
from .mining_processing import RelativeTimeEnum, PresenceEnum, MineralogyFeedstockClass, BeneficiationPathway, InSituChemistryRegime, ExtractableTargetElement, SensorWhileDrillingFeature, ProcessPerformanceMetric, BioleachOrganism, BioleachMode, AutonomyLevel, RegulatoryConstraint
from .statistics import PredictionOutcomeType
from .stewardship import ValueSetStewardEnum

# Data domain
from .data.data_absent_reason import DataAbsentEnum
from .data.data_use import DataUsePermissionEnum, DataUseModifierEnum

# Data_Catalog domain
from .data_catalog.access import AccessRights, DatasetStatus, UpdateFrequency, DataServiceType
from .data_catalog.contributor_roles import DataCiteContributorType
from .data_catalog.relations import DataCiteRelationType
from .data_catalog.resource_types import DataCiteResourceType

# Data_Science domain
from .data_science.binary_classification import BinaryClassificationEnum, SpamClassificationEnum, AnomalyDetectionEnum, ChurnClassificationEnum, FraudDetectionEnum
from .data_science.emotion_classification import BasicEmotionEnum, ExtendedEmotionEnum
from .data_science.priority_severity import PriorityLevelEnum, SeverityLevelEnum, ConfidenceLevelEnum
from .data_science.quality_control import QualityControlEnum, DefectClassificationEnum
from .data_science.sentiment_analysis import SentimentClassificationEnum, FineSentimentClassificationEnum
from .data_science.text_classification import NewsTopicCategoryEnum, ToxicityClassificationEnum, IntentClassificationEnum

# Earth_Science domain
from .earth_science.collection_methods import SESARCollectionMethod
from .earth_science.fao_soil import FAOSoilType
from .earth_science.material_types import SESARMaterialType
from .earth_science.physiographic_features import SESARPhysiographicFeature
from .earth_science.sample_types import SESARSampleType

# Energy domain
from .energy.energy import EnergySource, EnergyUnit, PowerUnit, EnergyEfficiencyRating, BuildingEnergyStandard, GridType, BatteryType, PVCellType, PVSystemType, EnergyStorageType, EmissionScope, CarbonIntensity, ElectricityMarket, CapabilityStatus
from .energy.fossil_fuels import FossilFuelTypeEnum
from .energy.nuclear.nuclear_facilities import NuclearFacilityTypeEnum, PowerPlantStatusEnum, ResearchReactorTypeEnum, FuelCycleFacilityTypeEnum, WasteFacilityTypeEnum, NuclearShipTypeEnum
from .energy.nuclear.nuclear_fuel_cycle import NuclearFuelCycleStageEnum, NuclearFuelFormEnum, EnrichmentProcessEnum
from .energy.nuclear.nuclear_fuels import NuclearFuelTypeEnum, UraniumEnrichmentLevelEnum, FuelFormEnum, FuelAssemblyTypeEnum, FuelCycleStageEnum, FissileIsotopeEnum
from .energy.nuclear.nuclear_operations import ReactorOperatingStateEnum, MaintenanceTypeEnum, LicensingStageEnum, FuelCycleOperationEnum, ReactorControlModeEnum, OperationalProcedureEnum
from .energy.nuclear.nuclear_regulatory import NuclearRegulatoryBodyEnum, RegulatoryFrameworkEnum, LicensingStageEnum, ComplianceStandardEnum, InspectionTypeEnum
from .energy.nuclear.nuclear_safety import INESLevelEnum, EmergencyClassificationEnum, NuclearSecurityCategoryEnum, SafetySystemClassEnum, ReactorSafetyFunctionEnum, DefenseInDepthLevelEnum, RadiationProtectionZoneEnum
from .energy.nuclear.nuclear_waste import IAEAWasteClassificationEnum, NRCWasteClassEnum, WasteHeatGenerationEnum, WasteHalfLifeCategoryEnum, WasteDisposalMethodEnum, WasteSourceEnum, TransuranicWasteCategoryEnum
from .energy.nuclear.reactor_types import ReactorTypeEnum, ReactorGenerationEnum, ReactorCoolantEnum, ReactorModeratorEnum, ReactorNeutronSpectrumEnum, ReactorSizeCategoryEnum
from .energy.renewable.bioenergy import BiomassFeedstockType, BiofuelType, BiofuelGeneration, BioconversionProcess
from .energy.renewable.geothermal import GeothermalSystemType, GeothermalReservoirType, GeothermalWellType, GeothermalApplication, GeothermalResourceTemperature
from .energy.renewable.hydrogen import HydrogenType, HydrogenProductionMethod, HydrogenStorageMethod, HydrogenApplication

# Environmental_Health domain
from .environmental_health.carcinogenicity import IARCCarcinogenicityGroup, EPAIRISCarcinogenicityGroup, NTPCarcinogenicityGroup
from .environmental_health.exposures import AirPollutantEnum, PesticideTypeEnum, HeavyMetalEnum, ExposureRouteEnum, ExposureSourceEnum, WaterContaminantEnum, EndocrineDisruptorEnum, ExposureDurationEnum, SmokingStatusEnum, ExposureStressorTypeEnum, ExposureTransportPathEnum, ExposureFrequencyEnum, StudyPopulationEnum, HHEARExposureAssessedEnum
from .environmental_health.gb_edoh import ExtremeWeatherEventEnum, ExposureAgentCategoryEnum, TemporalAggregationEnum, SpatialResolutionEnum
from .environmental_health.radionuclides import RadionuclideEnum, NORMEnum

# Geography domain
from .geography.geographic_codes import CountryCodeISO2Enum, CountryCodeISO3Enum, USStateCodeEnum, CanadianProvinceCodeEnum, CompassDirection, RelativeDirection, WindDirection, ContinentEnum, UNRegionEnum, LanguageCodeISO6391enum, TimeZoneEnum, CurrencyCodeISO4217Enum

# Health domain
from .health.vaccination import VaccinationStatusEnum, VaccinationPeriodicityEnum, VaccineCategoryEnum

# Industry domain
from .industry.extractive_industry import ExtractiveIndustryFacilityTypeEnum, ExtractiveIndustryProductTypeEnum, MiningMethodEnum, WellTypeEnum
from .industry.mining import MiningType, MineralCategory, CriticalMineral, CommonMineral, MiningEquipment, OreGrade, MiningPhase, MiningHazard, EnvironmentalImpact
from .industry.safety_colors import SafetyColorEnum, TrafficLightColorEnum, HazmatColorEnum, FireSafetyColorEnum, MaritimeSignalColorEnum, AviationLightColorEnum, ElectricalWireColorEnum

# Lab_Automation domain
from .lab_automation.devices import LaboratoryDeviceTypeEnum, RoboticArmTypeEnum
from .lab_automation.labware import MicroplateFormatEnum, ContainerTypeEnum, PlateMaterialEnum, PlateCoatingEnum
from .lab_automation.operations import LiquidHandlingOperationEnum, SampleProcessingOperationEnum
from .lab_automation.protocols import WorkflowOrchestrationTypeEnum, SchedulerTypeEnum, ProtocolStateEnum, ExecutionModeEnum, WorkflowErrorHandlingEnum, IntegrationSystemEnum
from .lab_automation.standards import AutomationStandardEnum, CommunicationProtocolEnum, LabwareStandardEnum, IntegrationFeatureEnum
from .lab_automation.thermal_cycling import ThermalCyclerTypeEnum, PCROperationTypeEnum, DetectionModeEnum, PCRPlateTypeEnum, ThermalCyclingStepEnum

# Materials_Science domain
from .materials_science.characterization_methods import MicroscopyMethodEnum, SpectroscopyMethodEnum, ThermalAnalysisMethodEnum, MechanicalTestingMethodEnum
from .materials_science.crystal_structures import CrystalSystemEnum, BravaisLatticeEnum
from .materials_science.material_properties import ElectricalConductivityEnum, MagneticPropertyEnum, OpticalPropertyEnum, ThermalConductivityEnum, MechanicalBehaviorEnum
from .materials_science.material_types import MaterialClassEnum, PolymerTypeEnum, MetalTypeEnum, CompositeTypeEnum
from .materials_science.pigments_dyes import TraditionalPigmentEnum, IndustrialDyeEnum, FoodColoringEnum, AutomobilePaintColorEnum
from .materials_science.synthesis_methods import SynthesisMethodEnum, CrystalGrowthMethodEnum, AdditiveManufacturingEnum

# Medical domain
from .medical.clinical import BloodTypeEnum, AnatomicalSystemEnum, MedicalSpecialtyEnum, DrugRouteEnum, VitalSignEnum, DiagnosticTestTypeEnum, SymptomSeverityEnum, AllergyTypeEnum, VaccineTypeEnum, BMIClassificationEnum
from .medical.family_history import FamilyRelationship, FamilyHistoryStatus, GeneticRelationship
from .medical.imaging_platforms import MRIPlatformEnum, MicroscopyPlatformEnum, ImagingSystemPlatformEnum
from .medical.neuroimaging import MRIModalityEnum, MRISequenceTypeEnum, MRIContrastTypeEnum, FMRIParadigmTypeEnum
from .medical.oncology.icdo import TumorTopography, TumorMorphology, TumorBehavior, TumorGrade
from .medical.pediatric_oncology.diagnosis_categories import PediatricOncologyDiagnosisCategory
from .medical.pediatric_oncology.iccc3 import ICCC3MainGroup, ICCC3Subgroup
from .medical.pediatric_oncology.staging.neuroblastoma import INRGSSStage, INSSStage, NeuroblastomaRiskGroup, ImageDefinedRiskFactor

# Physics domain
from .physics.radiation import ElectromagneticRadiationTypeEnum, InfraredRadiationTypeEnum, AcousticRadiationTypeEnum
from .physics.states_of_matter import StateOfMatterEnum

# Preservation domain
from .preservation.digital_objects import DigitalObjectCategory, CopyrightStatus, RightsBasis, PreservationLevelRole, PreservationLevelValue
from .preservation.events import PreservationEventType, PreservationEventOutcome
from .preservation.fixity import CryptographicHashFunction

# Publishing domain
from .publishing.arxiv_categories import ArxivCategory
from .publishing.osti_record import OstiWorkflowStatus, OstiAccessLimitation, OstiCollectionType, OstiSensitivityFlag, OstiOrganizationIdentifierType, OstiProductType, OstiOrganizationType, OstiPersonType, OstiContributorType, OstiRelatedIdentifierType, OstiRelationType, OstiIdentifierType, OstiGeolocationType, OstiMediaLocationType

# Social domain
from .social.person_status import PersonStatusEnum
from .social.sdoh import GravitySdohDomainEnum, EducationalAttainmentEnum

# Spatial domain
from .spatial.spatial_qualifiers import SimpleSpatialDirection, AnatomicalSide, AnatomicalRegion, AnatomicalAxis, AnatomicalPlane, SpatialRelationship, CellPolarity, AnatomicalOrientation

# Statistics domain
from .statistics.prediction_outcomes import OutcomeTypeEnum

# Time domain
from .time.temporal import DayOfWeek, Month, Quarter, Season, TimePeriod, TimeOfDay, BusinessTimeFrame, GeologicalEra, HistoricalPeriod

# Units domain
from .units.measurements import LengthUnitEnum, MassUnitEnum, VolumeUnitEnum, TemperatureUnitEnum, TimeUnitEnum, PressureUnitEnum, ConcentrationUnitEnum, FrequencyUnitEnum, AngleUnitEnum, DataSizeUnitEnum
from .units.quantity_kinds import QuantityKindEnum

# Visual domain
from .visual.colors import BasicColorEnum, WebColorEnum, X11ColorEnum, ColorSpaceEnum

__all__ = [
    "ACMGPathogenicityEnum",
    "AcademicDegree",
    "AccessRights",
    "AcousticRadiationTypeEnum",
    "AdditiveManufacturingEnum",
    "AgeGroupEnum",
    "AgitationTypeEnum",
    "AirPollutantEnum",
    "AllelicStateEnum",
    "AllergyTypeEnum",
    "AminoAcidEnum",
    "AminoAcidExtendedEnum",
    "AnalyteTypeEnum",
    "AnalyticalControlType",
    "AnatomicalAxis",
    "AnatomicalOrientation",
    "AnatomicalPlane",
    "AnatomicalRegion",
    "AnatomicalSide",
    "AnatomicalSystemEnum",
    "AngleUnitEnum",
    "AnimalCoatColorEnum",
    "AnomalyDetectionEnum",
    "ArchiveFormatEnum",
    "ArxivCategory",
    "AudioFormatEnum",
    "AutomationStandardEnum",
    "AutomobilePaintColorEnum",
    "AutonomyLevel",
    "AviationLightColorEnum",
    "BMIClassificationEnum",
    "BasicColorEnum",
    "BasicEmotionEnum",
    "BatteryType",
    "BeneficiationPathway",
    "BenefitsCategoryEnum",
    "BgcCategoryEnum",
    "BinaryClassificationEnum",
    "BioconversionProcess",
    "BiofuelGeneration",
    "BiofuelType",
    "BioleachMode",
    "BioleachOrganism",
    "BiologicalKingdom",
    "BiologicalRole",
    "BiologicalSexEnum",
    "BiomassFeedstockType",
    "BioreactorTypeEnum",
    "BiosafetyLevelEnum",
    "BioticInteractionType",
    "BloodTypeEnum",
    "BondTypeEnum",
    "BravaisLatticeEnum",
    "BronstedAcidBaseRoleEnum",
    "BuildingEnergyStandard",
    "BusinessActivityTypeEnum",
    "BusinessLifecycleStageEnum",
    "BusinessOwnershipTypeEnum",
    "BusinessProcessTypeEnum",
    "BusinessSizeClassificationEnum",
    "BusinessTimeFrame",
    "CIOConfidenceLevel",
    "CanadianProvinceCodeEnum",
    "CapabilityMaturityLevel",
    "CapabilityStatus",
    "CarbonIntensity",
    "CaseOrControlEnum",
    "CatalystTypeEnum",
    "CausalPredicateEnum",
    "CdsPhaseType",
    "CellBasedAssayEnum",
    "CellCycleCheckpoint",
    "CellCyclePhase",
    "CellCycleRegulator",
    "CellPolarity",
    "CellProliferationState",
    "ChiralityEnum",
    "ChromatographyType",
    "ChurnClassificationEnum",
    "CitationStyle",
    "ClinicalBehavioralAssayEnum",
    "CodonEnum",
    "ColorSpaceEnum",
    "CommonMineral",
    "CommonOrganismTaxaEnum",
    "CommunicationProtocolEnum",
    "CompassDirection",
    "CompensationTypeEnum",
    "ComplianceStandardEnum",
    "CompositeTypeEnum",
    "CompressionFormat",
    "CompressionType",
    "ConcentrationUnitEnum",
    "ConditionProvenanceEnum",
    "ConfidenceLevel",
    "ConfidenceLevelEnum",
    "ConfidenceScore",
    "ContainerTypeEnum",
    "ContigCollectionType",
    "ContinentEnum",
    "ContributorType",
    "CoordinationGeometry",
    "CopyrightStatus",
    "CorporateGovernanceRoleEnum",
    "CountryCodeISO2Enum",
    "CountryCodeISO3Enum",
    "CriticalMineral",
    "CryoEMGridType",
    "CryoEMPreparationType",
    "CryptographicHashFunction",
    "CrystalGrowthMethodEnum",
    "CrystalSystemEnum",
    "CrystallizationMethod",
    "CurrencyChemical",
    "CurrencyCodeISO4217Enum",
    "DNABaseEnum",
    "DNABaseExtendedEnum",
    "DNADamageResponse",
    "DataAbsentEnum",
    "DataCiteContributorType",
    "DataCiteRelationType",
    "DataCiteResourceType",
    "DataFormatEnum",
    "DataMaturityLevel",
    "DataProcessingLevel",
    "DataServiceType",
    "DataSizeUnitEnum",
    "DataType",
    "DataUseModifierEnum",
    "DataUsePermissionEnum",
    "DatasetEncodingFormat",
    "DatasetSplitType",
    "DatasetStatus",
    "DayOfWeek",
    "DecisionMakingStyleEnum",
    "DefectClassificationEnum",
    "DefenseInDepthLevelEnum",
    "DerivatizationMethod",
    "DetectionModeEnum",
    "Detector",
    "DiagnosticTestTypeEnum",
    "DigitalObjectCategory",
    "DocumentFormatEnum",
    "DownstreamProcessEnum",
    "DrugExposureProvenanceEnum",
    "DrugResponseEnum",
    "DrugRouteEnum",
    "EPAIRISCarcinogenicityGroup",
    "EcologicalEnvironmentExposureEnum",
    "EconomicSectorEnum",
    "EducationLevel",
    "EducationalAttainmentEnum",
    "ElectricalConductivityEnum",
    "ElectricalWireColorEnum",
    "ElectricityMarket",
    "ElectromagneticRadiationTypeEnum",
    "ElementFamilyEnum",
    "ElementMetallicClassificationEnum",
    "EmergencyClassificationEnum",
    "EmissionScope",
    "EmployeeStatusEnum",
    "EmploymentStatus",
    "EmploymentTypeEnum",
    "EndocrineDisruptorEnum",
    "EnergyEfficiencyRating",
    "EnergySource",
    "EnergyStorageType",
    "EnergyUnit",
    "EnrichmentProcessEnum",
    "EnvironmentalImpact",
    "EnzymeClassEnum",
    "EthnicityOMB1997Enum",
    "ExecutionModeEnum",
    "ExperimentalPreparation",
    "ExperimentalRole",
    "ExposureAgentCategoryEnum",
    "ExposureDurationEnum",
    "ExposureFrequencyEnum",
    "ExposureRouteEnum",
    "ExposureSourceEnum",
    "ExposureStressorTypeEnum",
    "ExposureTransportPathEnum",
    "ExpressionUnitEnum",
    "ExtendedEmotionEnum",
    "ExtractableTargetElement",
    "ExtractiveIndustryFacilityTypeEnum",
    "ExtractiveIndustryProductTypeEnum",
    "ExtremeWeatherEventEnum",
    "EyeColorEnum",
    "FAOSoilType",
    "FMRIParadigmTypeEnum",
    "FamilyHistoryStatus",
    "FamilyRelationship",
    "FeatureType",
    "FeedstockTypeEnum",
    "FermentationModeEnum",
    "FileFormat",
    "FineSentimentClassificationEnum",
    "FireSafetyColorEnum",
    "FissileIsotopeEnum",
    "FlowerColorEnum",
    "FoodColoringEnum",
    "FossilFuelTypeEnum",
    "FraudDetectionEnum",
    "FrequencyUnitEnum",
    "FuelAssemblyTypeEnum",
    "FuelCycleFacilityTypeEnum",
    "FuelCycleOperationEnum",
    "FuelCycleStageEnum",
    "FuelFormEnum",
    "FundingType",
    "GOAspect",
    "GOElectronicMethods",
    "GOEvidenceCode",
    "GenderIdentity",
    "GeneKnockoutMethodEnum",
    "GenePerturbationMethodEnum",
    "GeneticCodeTable",
    "GeneticRelationship",
    "GenomeFeatureType",
    "GenotypeEnum",
    "GeologicalEra",
    "GeospatialRasterFormat",
    "GeospatialVectorFormat",
    "GeothermalApplication",
    "GeothermalReservoirType",
    "GeothermalResourceTemperature",
    "GeothermalSystemType",
    "GeothermalWellType",
    "GravitySdohDomainEnum",
    "GridType",
    "HHEARExposureAssessedEnum",
    "HRFunctionEnum",
    "HairColorEnum",
    "HardOrSoftEnum",
    "HazmatColorEnum",
    "HealthcareEncounterClassification",
    "HeavyMetalEnum",
    "HistoricalPeriod",
    "HistoricalStatusEnum",
    "HousingStatus",
    "HumanAgeGroupEnum",
    "HumanDevelopmentalStage",
    "HydrogenApplication",
    "HydrogenProductionMethod",
    "HydrogenStorageMethod",
    "HydrogenType",
    "IAEAWasteClassificationEnum",
    "IARCCarcinogenicityGroup",
    "ICCC3MainGroup",
    "ICCC3Subgroup",
    "INESLevelEnum",
    "INRGSSStage",
    "INSSStage",
    "IPCCConfidenceLevel",
    "IPCCLikelihoodScale",
    "IUPACAminoAcidCode",
    "IUPACNucleotideCode",
    "ImageDefinedRiskFactor",
    "ImageFileFormatEnum",
    "ImagingAssayEnum",
    "ImagingSystemPlatformEnum",
    "InSituChemistryRegime",
    "IndustrialDyeEnum",
    "IndustryMaturityEnum",
    "IndustryRegulationLevelEnum",
    "InfraredRadiationTypeEnum",
    "InsdcGeographicLocationEnum",
    "InsdcMissingValueEnum",
    "InspectionTypeEnum",
    "IntegrationFeatureEnum",
    "IntegrationSystemEnum",
    "IntentClassificationEnum",
    "InteractionDetectionMethod",
    "InteractionType",
    "InteractorType",
    "InterpretationProgressEnum",
    "InventoryManagementApproachEnum",
    "JobLevelEnum",
    "KaryotypicSexEnum",
    "LaboratoryDeviceTypeEnum",
    "LabwareStandardEnum",
    "LanguageCodeISO6391enum",
    "LateralityEnum",
    "LeadershipStyleEnum",
    "LegalEntityTypeEnum",
    "LengthUnitEnum",
    "LewisAcidBaseRoleEnum",
    "LibraryPreparation",
    "LicenseType",
    "LicensingStageEnum",
    "LipidCategory",
    "LiquidHandlingOperationEnum",
    "LogisticsOperationEnum",
    "MLDataType",
    "MLFieldRole",
    "MLLicenseType",
    "MLMediaType",
    "MLModalityType",
    "MRIContrastTypeEnum",
    "MRIModalityEnum",
    "MRIPlatformEnum",
    "MRISequenceTypeEnum",
    "MagneticPropertyEnum",
    "MaintenanceTypeEnum",
    "ManagementLevelEnum",
    "ManagementMethodologyEnum",
    "ManuscriptSection",
    "MaritalStatus",
    "MaritimeSignalColorEnum",
    "MarketStructureEnum",
    "MassErrorUnit",
    "MassSpectrometerFileFormat",
    "MassSpectrometerVendor",
    "MassSpectrometryAssayEnum",
    "MassUnitEnum",
    "MaterialClassEnum",
    "MechanicalBehaviorEnum",
    "MechanicalTestingMethodEnum",
    "MedicalSpecialtyEnum",
    "MeioticPhase",
    "MetabolomicsAssayType",
    "MetalLigandType",
    "MetalTypeEnum",
    "MicroplateFormatEnum",
    "MicroscopyMethodEnum",
    "MicroscopyPlatformEnum",
    "MimeType",
    "MimeTypeCategory",
    "MineralCategory",
    "MineralogyFeedstockClass",
    "MiningEquipment",
    "MiningHazard",
    "MiningMethodEnum",
    "MiningPhase",
    "MiningType",
    "MitoticPhase",
    "ModeOfInheritance",
    "ModelSystemTypeEnum",
    "Month",
    "MouseDevelopmentalStage",
    "MousePostnatalAgeGroupEnum",
    "NAICSSectorEnum",
    "NCITFivePointConfidenceScale",
    "NIHInstituteCenterEnum",
    "NORMEnum",
    "NRCWasteClassEnum",
    "NTPCarcinogenicityGroup",
    "NanostructureMorphologyEnum",
    "NetworkProtocolEnum",
    "NeuroblastomaRiskGroup",
    "NewsTopicCategoryEnum",
    "NuclearFacilityTypeEnum",
    "NuclearFuelCycleStageEnum",
    "NuclearFuelFormEnum",
    "NuclearFuelTypeEnum",
    "NuclearRegulatoryBodyEnum",
    "NuclearSecurityCategoryEnum",
    "NuclearShipTypeEnum",
    "NucleotideModificationEnum",
    "OBCSCertaintyLevel",
    "OWLProfileEnum",
    "OmbEthnicityCategory",
    "OmbRaceCategory",
    "OnsetTimingEnum",
    "OpenAccessType",
    "OpenSourceMaturityLevel",
    "OperationalModelEnum",
    "OperationalProcedureEnum",
    "OpticalPropertyEnum",
    "OreGrade",
    "OrganizationalStructureEnum",
    "OstiAccessLimitation",
    "OstiCollectionType",
    "OstiContributorType",
    "OstiGeolocationType",
    "OstiIdentifierType",
    "OstiMediaLocationType",
    "OstiOrganizationIdentifierType",
    "OstiOrganizationType",
    "OstiPersonType",
    "OstiProductType",
    "OstiRelatedIdentifierType",
    "OstiRelationType",
    "OstiSensitivityFlag",
    "OstiWorkflowStatus",
    "OutcomeTypeEnum",
    "OxidationStateEnum",
    "OxygenationStrategyEnum",
    "PCROperationTypeEnum",
    "PCRPlateTypeEnum",
    "PVCellType",
    "PVSystemType",
    "ParticipantIdentificationMethod",
    "ParticipantVitalStatusEnum",
    "PeakAnnotationSeriesLabel",
    "PediatricOncologyDiagnosisCategory",
    "PeerReviewStatus",
    "PeptideIonSeries",
    "PerformanceMeasurementEnum",
    "PerformanceRatingEnum",
    "PeriodicTableBlockEnum",
    "PersonStatusEnum",
    "PesticideTypeEnum",
    "PhenotypicSexEnum",
    "PlannedProcessCompletionStatus",
    "PlantDevelopmentalStage",
    "PlantGrowthMediumExposureEnum",
    "PlantLeafColorEnum",
    "PlantSexEnum",
    "PlantSexualSystem",
    "PlantStudyConditionEnum",
    "PlateCoatingEnum",
    "PlateMaterialEnum",
    "PolymerTypeEnum",
    "PowerPlantStatusEnum",
    "PowerUnit",
    "PredictionOutcomeType",
    "PresenceEnum",
    "PreservationEventOutcome",
    "PreservationEventType",
    "PreservationLevelRole",
    "PreservationLevelValue",
    "PressureUnitEnum",
    "PriorityLevelEnum",
    "ProcessImprovementApproachEnum",
    "ProcessPerformanceMetric",
    "ProcessScaleEnum",
    "ProcessingStatus",
    "ProcurementTypeEnum",
    "ProductTypeEnum",
    "ProgrammingLanguageFileEnum",
    "ProjectMaturityLevel",
    "ProteinEvidenceForExistence",
    "ProteinModificationType",
    "ProtocolStateEnum",
    "PublicationType",
    "QualityAssuranceLevelEnum",
    "QualityControlEnum",
    "QualityControlTechniqueEnum",
    "QualityMaturityLevelEnum",
    "QualityMethodologyEnum",
    "QualityStandardEnum",
    "QuantityKindEnum",
    "Quarter",
    "RNABaseEnum",
    "RNABaseExtendedEnum",
    "RaceOMB1997Enum",
    "RadiationProtectionZoneEnum",
    "RadionuclideEnum",
    "ReactionConditionEnum",
    "ReactionDirectionality",
    "ReactionMechanismEnum",
    "ReactionRateOrderEnum",
    "ReactionTypeEnum",
    "ReactorControlModeEnum",
    "ReactorCoolantEnum",
    "ReactorGenerationEnum",
    "ReactorModeratorEnum",
    "ReactorNeutronSpectrumEnum",
    "ReactorOperatingStateEnum",
    "ReactorSafetyFunctionEnum",
    "ReactorSizeCategoryEnum",
    "ReactorTypeEnum",
    "ReadType",
    "RecruitmentSourceEnum",
    "RecruitmentStatusEnum",
    "RefSeqStatusType",
    "RegimenStatusEnum",
    "RegulatoryConstraint",
    "RegulatoryFrameworkEnum",
    "RelToOxygenEnum",
    "RelativeDirection",
    "RelativeTimeEnum",
    "ResearchField",
    "ResearchProjectTypeEnum",
    "ResearchReactorTypeEnum",
    "ResearchRole",
    "RightsBasis",
    "RoboticArmTypeEnum",
    "SESARCollectionMethod",
    "SESARMaterialType",
    "SESARPhysiographicFeature",
    "SESARSampleType",
    "SafetyColorEnum",
    "SafetySystemClassEnum",
    "SampleProcessingOperationEnum",
    "SampleType",
    "SchedulerTypeEnum",
    "Season",
    "SeasonalEnvironmentExposureEnum",
    "SectionLocationEnum",
    "SensorWhileDrillingFeature",
    "SentimentClassificationEnum",
    "SequenceAlphabet",
    "SequenceFileFormat",
    "SequenceModality",
    "SequenceQualityEncoding",
    "SequenceQualityEnum",
    "SequenceStrand",
    "SequenceTopology",
    "SequenceType",
    "SequencingApplication",
    "SequencingAssayEnum",
    "SequencingChemistry",
    "SequencingPlatform",
    "SeverityLevelEnum",
    "SimpleSpatialDirection",
    "SkinToneEnum",
    "SmokingStatusEnum",
    "SoftwareMaturityLevel",
    "SolventClassEnum",
    "SourceMaterialTypeEnum",
    "SourcingStrategyEnum",
    "SpamClassificationEnum",
    "SpatialRelationship",
    "SpatialResolutionEnum",
    "SpecimenCollectionMethodEnum",
    "SpecimenCreationActivityTypeEnum",
    "SpecimenPreparationMethodEnum",
    "SpecimenProcessingActivityTypeEnum",
    "SpecimenQualityObservationMethodEnum",
    "SpecimenQualityObservationTypeEnum",
    "SpecimenQuantityObservationTypeEnum",
    "SpecimenTypeEnum",
    "SpectroscopyMethodEnum",
    "StandardAminoAcid",
    "StandardsMaturityLevel",
    "StandardsOrganizationEnum",
    "StateOfMatterEnum",
    "StatusEnum",
    "SterilizationMethodEnum",
    "StrandType",
    "StrategicFrameworkEnum",
    "StructuralBiologyTechnique",
    "StudyPhaseEnum",
    "StudyPopulationEnum",
    "SubatomicParticleEnum",
    "SupplierRelationshipTypeEnum",
    "SupplyChainStrategyEnum",
    "SymptomSeverityEnum",
    "SynthesisMethodEnum",
    "TaxonomicRank",
    "TechnologyReadinessLevel",
    "TemperatureUnitEnum",
    "TemporalAggregationEnum",
    "TextCharset",
    "TherapeuticActionabilityEnum",
    "ThermalAnalysisMethodEnum",
    "ThermalConductivityEnum",
    "ThermalCyclerTypeEnum",
    "ThermalCyclingStepEnum",
    "ThermodynamicParameterEnum",
    "TimeOfDay",
    "TimePeriod",
    "TimeUnitEnum",
    "TimeZoneEnum",
    "TissuePreservationEnum",
    "ToxicityClassificationEnum",
    "TraditionalPigmentEnum",
    "TrafficLightColorEnum",
    "TrainingTypeEnum",
    "TransplantationTypeEnum",
    "TransuranicWasteCategoryEnum",
    "TrophicLevelEnum",
    "TumorBehavior",
    "TumorGrade",
    "TumorMorphology",
    "TumorTopography",
    "UNRegionEnum",
    "UNSpecializedAgencyEnum",
    "USDOENationalLaboratoryEnum",
    "USFederalFundingAgencyEnum",
    "USStateCodeEnum",
    "UniProtSpeciesCode",
    "UpdateFrequency",
    "UraniumEnrichmentLevelEnum",
    "VaccinationPeriodicityEnum",
    "VaccinationStatusEnum",
    "VaccineCategoryEnum",
    "VaccineTypeEnum",
    "ValueSetStewardEnum",
    "VectorTypeEnum",
    "VendorCategoryEnum",
    "VideoFormatEnum",
    "ViralGenomeTypeEnum",
    "VisitProvenanceEnum",
    "VitalSignEnum",
    "VitalStatusEnum",
    "VitrificationMethod",
    "VolumeUnitEnum",
    "WasteDisposalMethodEnum",
    "WasteFacilityTypeEnum",
    "WasteHalfLifeCategoryEnum",
    "WasteHeatGenerationEnum",
    "WasteSourceEnum",
    "WaterContaminantEnum",
    "WebColorEnum",
    "WellTypeEnum",
    "WindDirection",
    "WorkArrangementEnum",
    "WorkflowErrorHandlingEnum",
    "WorkflowOrchestrationTypeEnum",
    "WorkflowType",
    "X11ColorEnum",
    "XRaySource",
    "XenograftModelEnum",
]