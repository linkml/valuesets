# Lab Automation Value Sets

Modern laboratories increasingly rely on robotic systems, automated workflows,
and self-driving experimentation. This view collects value sets from across
the lab automation, bioprocessing, assay, specimen processing, and computing
domains that are needed to describe automated laboratory operations end-to-end.

## Coverage Summary

| Domain | Schema Sources | Enums | Ontologies |
|--------|---------------|------:|------------|
| [Robotic Systems and Devices](#robotic-systems-and-devices) | lab_automation/autonomous_labs, lab_automation/devices | 5 | OBI |
| [Labware and Consumables](#labware-and-consumables) | lab_automation/labware | 4 | |
| [Liquid Handling and Operations](#liquid-handling-and-operations) | lab_automation/operations | 2 | |
| [Protocols and Orchestration](#protocols-and-orchestration) | lab_automation/protocols | 6 | |
| [Standards and Integration](#standards-and-integration) | lab_automation/standards | 4 | |
| [Thermal Cycling and PCR](#thermal-cycling-and-pcr) | lab_automation/thermal_cycling | 5 | |
| [Sequencing Platforms](#sequencing-platforms) | bio/sequencing_platforms | 4 | OBI, GENEPIO |
| [Specimen Processing](#specimen-processing) | bio/specimen_processing | 5 | OBI, NCIT |
| [Bioprocessing and Scale-Up](#bioprocessing-and-scale-up) | bioprocessing/biomanufacturing, bioprocessing/scale_up | 6 | OBI, CHEBI |
| [Assays](#assays) | bio/assays/* | 12+ | OBI, BAO |

---

## Assays

Laboratory assays are the core measurements that automated systems perform.
This section covers both broad ontology-backed dynamic enums and curated
domain-specific static enums with companion annotations for microschema coupling.

### Dynamic Enums (Ontology-backed)

- [OBIAssayEnum](../elements/OBIAssayEnum.md) -- all OBI assay subclasses (OBI:0000070)
- [BAOBioassayEnum](../elements/BAOBioassayEnum.md) -- all BAO bioassay subclasses (BAO:0000015)

### Domain-Specific Static Enums

- [EnzymologyAssayEnum](../elements/EnzymologyAssayEnum.md) -- enzyme activity, kinetics, inhibition, substrate specificity
- [ImmunologyAssayEnum](../elements/ImmunologyAssayEnum.md) -- ELISA, flow cytometry, western blot, immunoprecipitation
- [ProteinEngineeringAssayEnum](../elements/ProteinEngineeringAssayEnum.md) -- SPR, BLI, thermal shift, display technologies
- [ToxicologyAssayEnum](../elements/ToxicologyAssayEnum.md) -- cytotoxicity, genotoxicity, ADME, dose-response

### NF-OSI Assay Enums

- [SequencingAssayEnum](../elements/SequencingAssayEnum.md) -- RNA-seq, ATAC-seq, ChIP-seq, whole genome sequencing
- [ImagingAssayEnum](../elements/ImagingAssayEnum.md) -- confocal, electron microscopy, MRI, live-cell imaging
- [MassSpectrometryAssayEnum](../elements/MassSpectrometryAssayEnum.md) -- LC-MS, MALDI, proteomics, metabolomics
- [CellBasedAssayEnum](../elements/CellBasedAssayEnum.md) -- viability, proliferation, migration, reporter assays
- [ClinicalBehavioralAssayEnum](../elements/ClinicalBehavioralAssayEnum.md) -- behavioral testing, clinical assessments

---

## Robotic Systems and Devices

Autonomous labs combine robotic hardware, AI experiment planners, and
high-throughput screening platforms. These enums describe the components
of an automated laboratory and the experimental design methods that drive them.

### Enums

- [AutonomousLabComponentType](../elements/AutonomousLabComponentType.md) -- robotic handlers, automated synthesizers, HTS platforms, AI planners
- [LabAutomationWorkflowType](../elements/LabAutomationWorkflowType.md) -- closed-loop optimization, self-driving experimentation
- [ExperimentalDesignMethodType](../elements/ExperimentalDesignMethodType.md) -- Bayesian optimization, active learning, DOE
- [LaboratoryDeviceTypeEnum](../elements/LaboratoryDeviceTypeEnum.md) -- liquid handlers, centrifuges, plate readers, thermal cyclers
- [RoboticArmTypeEnum](../elements/RoboticArmTypeEnum.md) -- flexible channel, multi-channel, gripper arms

---

## Labware and Consumables

Standardized labware is essential for robotic interoperability. These enums
cover microplate formats, container types, and surface treatments.

### Enums

- [MicroplateFormatEnum](../elements/MicroplateFormatEnum.md) -- 6 through 1536-well plate formats
- [ContainerTypeEnum](../elements/ContainerTypeEnum.md) -- microplates, deep well plates, tube racks, reservoirs
- [PlateMaterialEnum](../elements/PlateMaterialEnum.md) -- polystyrene, polypropylene, glass
- [PlateCoatingEnum](../elements/PlateCoatingEnum.md) -- tissue culture treated, protein binding surfaces

---

## Liquid Handling and Operations

Liquid handling is the backbone of lab automation. These enums describe
pipetting operations and sample processing steps performed by robotic systems.

### Enums

- [LiquidHandlingOperationEnum](../elements/LiquidHandlingOperationEnum.md) -- aspirate, dispense, transfer, serial dilution, plate stamping
- [SampleProcessingOperationEnum](../elements/SampleProcessingOperationEnum.md) -- centrifugation, incubation, thermal cycling, washing, detection

---

## Protocols and Orchestration

Automated workflows require protocol management, scheduling, and error handling.
These enums describe how protocols are executed and orchestrated across instruments.

### Enums

- [WorkflowOrchestrationTypeEnum](../elements/WorkflowOrchestrationTypeEnum.md) -- static, dynamic, event-driven, parallel processing
- [SchedulerTypeEnum](../elements/SchedulerTypeEnum.md) -- priority-based, FIFO, resource-aware, deadline-driven
- [ProtocolStateEnum](../elements/ProtocolStateEnum.md) -- pending, running, paused, completed, failed
- [ExecutionModeEnum](../elements/ExecutionModeEnum.md) -- automated, manual, semi-automated, simulation, dry run
- [WorkflowErrorHandlingEnum](../elements/WorkflowErrorHandlingEnum.md) -- retry, abort, skip and continue, rollback
- [IntegrationSystemEnum](../elements/IntegrationSystemEnum.md) -- LIMS, ELN, MES, SCADA

---

## Standards and Integration

Lab automation standards ensure interoperability between instruments from
different vendors. These enums cover communication protocols, labware standards,
and integration features.

### Enums

- [AutomationStandardEnum](../elements/AutomationStandardEnum.md) -- SiLA 2, LabOP, Autoprotocol, CLSI standards
- [CommunicationProtocolEnum](../elements/CommunicationProtocolEnum.md) -- gRPC, REST API, OPC UA, Modbus
- [LabwareStandardEnum](../elements/LabwareStandardEnum.md) -- ANSI/SLAS microplate standards, SBS footprint
- [IntegrationFeatureEnum](../elements/IntegrationFeatureEnum.md) -- barcode tracking, audit trail, electronic signatures

---

## Thermal Cycling and PCR

PCR and qPCR are among the most automated laboratory procedures. These enums
describe cycler types, reaction configurations, and detection methods.

### Enums

- [ThermalCyclerTypeEnum](../elements/ThermalCyclerTypeEnum.md) -- standard, real-time qPCR, digital PCR, gradient
- [PCROperationTypeEnum](../elements/PCROperationTypeEnum.md) -- standard PCR, RT-qPCR, multiplex, touchdown, digital PCR
- [DetectionModeEnum](../elements/DetectionModeEnum.md) -- SYBR Green, TaqMan, molecular beacon, FRET
- [PCRPlateTypeEnum](../elements/PCRPlateTypeEnum.md) -- 96-well, 384-well, tube strips
- [ThermalCyclingStepEnum](../elements/ThermalCyclingStepEnum.md) -- denaturation, annealing, extension, melt curve

---

## Sequencing Platforms

Next-generation sequencing is a core automated workflow. These enums describe
instrument platforms, chemistries, library preparations, and data formats.

### Enums

- [SequencingPlatform](../elements/SequencingPlatform.md) -- Illumina, PacBio, Oxford Nanopore, Element, MGI
- [SequencingChemistry](../elements/SequencingChemistry.md) -- sequencing by synthesis, SMRT, nanopore
- [LibraryPreparation](../elements/LibraryPreparation.md) -- genomic DNA, RNA-seq, single-cell, metagenomics
- [SequenceFileFormat](../elements/SequenceFileFormat.md) -- FASTQ, BAM, CRAM, VCF, GFF3

---

## Specimen Processing

Sample preparation is the critical first step in any automated pipeline. These
enums describe how specimens are collected, preserved, and processed.

### Enums

- [SpecimenCollectionMethodEnum](../elements/SpecimenCollectionMethodEnum.md) -- biopsy, venipuncture, swab, lavage
- [SpecimenPreparationMethodEnum](../elements/SpecimenPreparationMethodEnum.md) -- FFPE, cryopreservation, flash freezing, RNAlater
- [SpecimenTypeEnum](../elements/SpecimenTypeEnum.md) -- tissue, blood, plasma, serum, urine, CSF
- [AnalyteTypeEnum](../elements/AnalyteTypeEnum.md) -- DNA, RNA, protein, cfDNA
- [SourceMaterialTypeEnum](../elements/SourceMaterialTypeEnum.md) -- primary tumor, blood-derived, cell lines, xenografts

---

## Bioprocessing and Scale-Up

Automated biomanufacturing scales from microfluidic devices to commercial
fermenters. These enums cover reactor types, operating modes, and purification.

### Enums

- [BiomanufacturingScaleType](../elements/BiomanufacturingScaleType.md) -- micro through commercial scale
- [BioreactorTypeEnum](../elements/BioreactorTypeEnum.md) -- stirred tank, airlift, wave bag, photobioreactor
- [FermentationModeEnum](../elements/FermentationModeEnum.md) -- batch, fed-batch, continuous, perfusion
- [DownstreamProcessEnum](../elements/DownstreamProcessEnum.md) -- centrifugation, filtration, chromatography, extraction
- [SterilizationMethodEnum](../elements/SterilizationMethodEnum.md) -- steam in place, autoclave, filter sterilization
- [BioprocessOptimizationType](../elements/BioprocessOptimizationType.md) -- media optimization, PAT, digital twin modeling
