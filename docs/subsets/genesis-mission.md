# DOE Genesis Mission Value Sets

The U.S. Department of Energy's [Genesis Mission](https://www.energy.gov/genesis) defines
26 national science and technology challenges spanning clean energy, advanced computing,
manufacturing, earth systems, and national security. This project provides standardized
value sets (enums with ontology mappings) that support data interoperability across
these challenge areas.

The 19 schema modules below cover topics from grid modernization and fusion energy to
quantum computing and autonomous laboratories. Each enum is mapped to established
ontologies wherever possible, enabling integration with broader scientific data ecosystems.

## Coverage Summary

| Domain | Schema | Enums | Ontologies |
|--------|--------|------:|------------|
| [Energy and Grid](#energy-and-grid) | grid, subsurface_energy | 6 | OEO, ENVO, CHEBI |
| [Nuclear](#nuclear) | fusion, nuclear_cleanup, nuclear_forensics | 8 | CHEBI, NCIT, CHMO, ENVO |
| [Earth Science](#earth-science) | subsurface, hydrogeology, remote_sensing, water_resources | 12 | ENVO, PATO, CHEBI, OBI |
| [Computing](#computing) | data_centers, microelectronics, quantum | 6 | Brick, CHEBI, NCIT |
| [Industry](#industry) | manufacturing, construction, unconventional_resources | 7 | OBI, CHMO, ENVO, Brick |
| [Materials and Physics](#materials-and-physics) | computational_materials, particle_physics | 5 | NCIT, CHEBI, PATO, SWO |
| [Bioprocessing and Labs](#bioprocessing-and-labs) | biomanufacturing, autonomous_labs | 6 | OBI, CHEBI, NCIT, BAO |

---

## Energy and Grid

Grid modernization and subsurface energy are central to the Genesis challenges on
decarbonization and energy security. These value sets standardize terminology for
grid components, storage technologies, and subsurface resources.

### Enums

- GridComponentType -- transmission lines, transformers, substations, inverters
- GridEnergyStorageType -- battery chemistries, pumped hydro, hydrogen storage
- GridManagementStrategyType -- demand response, load balancing, virtual power plants
- SubsurfaceEnergyResourceType -- geothermal, oil, gas hydrate reservoirs
- SubsurfaceStorageType -- CCS, underground hydrogen, compressed air
- ReservoirCharacterizationMethodType -- well tests, seismic, core analysis

### Example Mappings

| Permissible Value | Enum | Ontology Mapping |
|-------------------|------|------------------|
| LITHIUM_ION_BATTERY | GridEnergyStorageType | OEO:00000248 |
| GEOTHERMAL_RESERVOIR | SubsurfaceEnergyResourceType | ENVO:2000034 |
| CARBON_CAPTURE_AND_STORAGE | SubsurfaceStorageType | OEO:00010141 |
| TRANSFORMER | GridComponentType | OEO:00000420 |

---

## Nuclear

Fusion energy, environmental cleanup of legacy nuclear sites, and nuclear forensics
each present distinct vocabulary needs. These enums cover confinement approaches,
plasma parameters, remediation techniques, and analytical methods.

### Enums

- FusionConfinementType -- tokamak, stellarator, inertial confinement
- FusionFuelType -- D-T, D-D, D-He3, p-B11 fuel cycles
- FusionPlasmaParameterType -- temperature, density, beta value
- NuclearRemediationType -- soil excavation, vitrification, phytoremediation
- DecommissioningPhaseType -- characterization through long-term monitoring
- RadioactiveContaminantType -- Cs-137, Sr-90, Tc-99, Pu, U
- NuclearForensicsMethodType -- isotope ratios, mass spec, gamma spectroscopy
- NuclearThreatCategoryType -- IND, RDD, material theft scenarios

### Example Mappings

| Permissible Value | Enum | Ontology Mapping |
|-------------------|------|------------------|
| CESIUM_137 | RadioactiveContaminantType | CHEBI:196959 |
| ISOTOPE_RATIO_ANALYSIS | NuclearForensicsMethodType | CHMO:0000506 |
| DECONTAMINATION | DecommissioningPhaseType | NCIT:C68769 |
| PLASMA_TEMPERATURE | FusionPlasmaParameterType | PATO:0000146 |

---

## Earth Science

Subsurface characterization, hydrogeology, remote sensing, and water resources span
multiple Genesis challenges related to environmental stewardship, critical minerals,
and climate resilience.

### Enums

- SubsurfaceFormationType -- aquifers, fault zones, permafrost, shale
- GeophysicalMethodType -- seismic, GPR, resistivity tomography
- SubsurfacePropertyType -- porosity, permeability, geothermal gradient
- AquiferType -- unconfined, confined, artesian, karst
- GroundwaterProcessType -- recharge, discharge, saltwater intrusion
- HydrogeologyWellType -- monitoring, production, injection wells
- RemoteSensingPlatformType -- satellite, airborne, UAV, ground-based
- RemoteSensingDataType -- multispectral, hyperspectral, SAR, LiDAR
- WaterResourceType -- surface water, groundwater, produced water
- WaterUseCategoryType -- irrigation, industrial cooling, environmental flow
- WaterQualityParameterType -- pH, dissolved oxygen, turbidity, nitrate
- WaterContaminantEnum -- water contaminant classification

### Example Mappings

| Permissible Value | Enum | Ontology Mapping |
|-------------------|------|------------------|
| AQUIFER | SubsurfaceFormationType | ENVO:00012408 |
| POROSITY | SubsurfacePropertyType | PATO:0000973 |
| SURFACE_WATER | WaterResourceType | ENVO:00002042 |
| DISSOLVED_OXYGEN | WaterQualityParameterType | CHEBI:15379 |

---

## Computing

Data center infrastructure, semiconductor fabrication, and quantum computing are
addressed by Genesis challenges on advanced computing and microelectronics supply chains.

### Enums

- DataCenterCoolingType -- air, liquid, immersion, geothermal cooling
- DataCenterTierLevel -- Tier I through Tier IV reliability
- SemiconductorMaterialType -- silicon, GaN, SiC, diamond
- ChipFabricationNodeType -- 3 nm through mature node processes
- QubitType -- superconducting, trapped ion, photonic, topological
- QuantumAlgorithmCategoryType -- optimization, simulation, ML, cryptography

### Example Mappings

| Permissible Value | Enum | Ontology Mapping |
|-------------------|------|------------------|
| SILICON | SemiconductorMaterialType | CHEBI:27573 |
| SILICON_CARBIDE | SemiconductorMaterialType | CHEBI:29390 |
| PHOTONIC | QubitType | CHEBI:30212 |
| SYNCHROTRON | ParticleAcceleratorType | NCIT:C48205 |

---

## Industry

Advanced manufacturing, building energy performance, and unconventional mineral
resources reflect Genesis challenges on industrial competitiveness, infrastructure
resilience, and critical material supply chains.

### Enums

- ManufacturingProcessType -- additive, subtractive, casting, CVD, PVD
- SmartManufacturingTechnologyType -- digital twins, IIoT, predictive maintenance
- BuildingSystemType -- HVAC, electrical, structural, fire protection
- BuildingEnergyPerformanceLevel -- net zero, passive house, LEED tiers
- UnconventionalMineralResourceType -- mine tailings, red mud, fly ash, geothermal brine
- BioextractionMethodType -- bioleaching, phytomining, biosorption
- TailingCharacterizationType -- particle size, mineralogy, metal content

### Example Mappings

| Permissible Value | Enum | Ontology Mapping |
|-------------------|------|------------------|
| INJECTION_MOLDING | ManufacturingProcessType | CHMO:0001430 |
| HVAC | BuildingSystemType | brick:HVAC_System |
| MINE_TAILINGS | UnconventionalMineralResourceType | ENVO:00000003 |
| HEAP_BIOLEACHING | BioextractionMethodType | CHMO:0001681 |

---

## Materials and Physics

Computational materials discovery and particle physics instrumentation underpin
Genesis challenges on scientific discovery and next-generation materials.

### Enums

- MaterialsSimulationType -- DFT, molecular dynamics, Monte Carlo, phase field
- MaterialPropertyPredictionType -- band gap, elastic modulus, thermal conductivity
- ParticleAcceleratorType -- linac, synchrotron, cyclotron, FEL
- FundamentalParticleType -- Standard Model particles (quarks, leptons, bosons)
- DetectorType -- calorimeters, tracking, Cherenkov, muon spectrometers

### Example Mappings

| Permissible Value | Enum | Ontology Mapping |
|-------------------|------|------------------|
| MOLECULAR_DYNAMICS | MaterialsSimulationType | NCIT:C18097 |
| ELASTIC_MODULUS | MaterialPropertyPredictionType | PATO:0001031 |
| ELECTRON | FundamentalParticleType | CHEBI:10545 |
| HIGGS_BOSON | FundamentalParticleType | CHEBI:146278 |

---

## Bioprocessing and Labs

Biomanufacturing scale-up and autonomous/self-driving laboratories address Genesis
challenges on the bioeconomy and accelerated scientific discovery.

### Enums

- BiomanufacturingScaleType -- micro through commercial scale
- BioproductCategoryType -- biofuels, biochemicals, enzymes, biopharmaceuticals
- BioprocessOptimizationType -- media optimization, strain engineering, PAT
- AutonomousLabComponentType -- robotic handlers, synthesizers, HTS platforms
- ExperimentalDesignMethodType -- Bayesian optimization, active learning, DOE
- LabAutomationWorkflowType -- closed-loop optimization, self-driving experimentation

### Example Mappings

| Permissible Value | Enum | Ontology Mapping |
|-------------------|------|------------------|
| BIOFUEL | BioproductCategoryType | CHEBI:33292 |
| ROBOTIC_SAMPLE_HANDLER | AutonomousLabComponentType | OBI:0400112 |
| HIGH_THROUGHPUT_SCREENING | LabAutomationWorkflowType | BAO:0010074 |
| DOWNSTREAM_PURIFICATION | BioprocessOptimizationType | OBI:0001505 |

---

## Ontology Coverage

The Genesis value sets draw on 15 ontologies:

| Ontology | Full Name | Used In |
|----------|-----------|---------|
| CHEBI | Chemical Entities of Biological Interest | 9 modules |
| ENVO | Environment Ontology | 8 modules |
| NCIT | NCI Thesaurus | 8 modules |
| PATO | Phenotype and Trait Ontology | 6 modules |
| OBI | Ontology for Biomedical Investigations | 4 modules |
| CHMO | Chemical Methods Ontology | 4 modules |
| OEO | Open Energy Ontology | 3 modules |
| Brick | Brick Schema for Buildings | 2 modules |
| MS | Mass Spectrometry Ontology | 1 module |
| SWO | Software Ontology | 1 module |
| AGRO | Agronomy Ontology | 1 module |
| FOODON | Food Ontology | 1 module |
| PROCO | Process Chemistry Ontology | 1 module |
| BAO | BioAssay Ontology | 1 module |
| STATO | Statistics Ontology | 1 module |
