# Value Set Suggestions for LinkML Common Value Sets

Based on comprehensive research across healthcare standards, genomics consortiums, academic systems, geographic/demographic authorities, and technology frameworks.

## 🏥 **HIGH PRIORITY: Healthcare & Medical Standards**

### Critical Missing FHIR/HL7 Value Sets
- **FHIR Administrative Gender** (`AdministrativeGender`) - Standard: HL7 FHIR
- **FHIR Contact Point System** (`ContactPointSystem`) - Standard: HL7 FHIR
- **FHIR Contact Point Use** (`ContactPointUse`) - Standard: HL7 FHIR
- **FHIR Address Type** (`AddressType`) - Standard: HL7 FHIR
- **FHIR Address Use** (`AddressUse`) - Standard: HL7 FHIR
- **FHIR Observation Status** (`ObservationStatus`) - Standard: HL7 FHIR
- **FHIR Diagnostic Report Status** (`DiagnosticReportStatus`) - Standard: HL7 FHIR
- **FHIR Medication Administration Status** (`MedicationAdministrationStatus`) - Standard: HL7 FHIR

**Rationale**: FHIR is the dominant healthcare interoperability standard globally. These core administrative and clinical status values are used across all healthcare systems.

### SNOMED CT Core Value Sets
- **SNOMED Clinical Finding** - Top-level clinical findings hierarchy
- **SNOMED Procedure** - Medical and surgical procedures
- **SNOMED Substance** - Medications, chemicals, biological substances
- **SNOMED Body Structure** - Anatomical locations and structures
- **SNOMED Qualifier Value** - Clinical qualifiers (severity, laterality, etc.)

**Source**: SNOMED International - 357,000+ healthcare concepts, most comprehensive clinical terminology

### ICD Classification Systems
- **ICD-11 Disease Categories** - Latest WHO disease classification (2022+)
- **ICD-10-CM Chapter Codes** - US clinical modification chapters
- **ICD-10-PCS Section Codes** - Procedure coding system sections

**Source**: WHO ICD-11 (132 countries implementing), CDC ICD-10-CM/PCS

### LOINC Laboratory Value Sets
- **LOINC Top 2000 Results** - Most commonly reported lab tests (98% volume coverage)
- **LOINC Universal Lab Orders** - Top 300 most frequent orders
- **LOINC Document Type** - Clinical document types
- **LOINC Answer List** - Standardized result values

**Source**: Regenstrief Institute LOINC - global standard for lab/clinical observations

## 🧬 **HIGH PRIORITY: Genomics & Biomedical**

### **NEWLY ADDED: Sequence Chemistry & Sequencing Platforms**
- **IUPAC Nucleotide Codes** - Complete DNA/RNA alphabet including ambiguity codes (A,T,G,C,N,R,Y,etc.)
- **IUPAC Amino Acid Codes** - Complete protein alphabet including selenocysteine (U), pyrrolysine (O)
- **Sequence Quality Encodings** - Phred, Solexa, Illumina quality score standards
- **NCBI Genetic Code Tables** - 30+ genetic codes for different organisms/organelles
- **Sequencing Platforms** - Illumina, PacBio, Nanopore, Element, MGI instruments
- **Sequencing Chemistry** - SBS, SMRT, nanopore, pyrosequencing methods
- **Library Preparation Methods** - RNA-seq, ChIP-seq, ATAC-seq, Hi-C, single-cell
- **Sequence File Formats** - FASTA, FASTQ, SAM/BAM, VCF, GFF3 standards

**Source**: IUPAC biochemical nomenclature, NCBI standards, major sequencing vendors

### GA4GH Phenopackets Standards
- **HPO Clinical Modifier** - Human Phenotype Ontology clinical modifiers
- **HPO Onset** - Age/temporal onset descriptors
- **GENO Zygosity** - Genetic zygosity terms
- **NCIT Histopathology** - Cancer histological classifications
- **OMIM Disease** - Mendelian disease identifiers

**Source**: GA4GH Phenopackets v2.0 (ISO 4454:2022 standard)

### OMOP Common Data Model
- **OMOP Domain** - Clinical data domains (Drug, Condition, Procedure, etc.)
- **OMOP Concept Class** - Semantic categories within domains
- **OMOP Vocabulary** - Source vocabulary systems (SNOMED, ICD, LOINC, etc.)
- **OMOP Relationship** - Inter-concept relationship types

**Source**: OHDSI OMOP CDM v5.4 - used by NIH All of Us, 100+ research networks

### FAIR Data Standards
- **Data Use Ontology (DUO)** - Research data use permissions/restrictions
- **EDAM Operations** - Bioinformatics operations and analyses
- **EDAM Data Types** - Biological data format types
- **EDAM Topics** - Biological/computational research domains

**Source**: FAIR Genomes, GA4GH DUO (200,000+ datasets annotated)

## 📚 **HIGH PRIORITY: Academic & Research**

### Research Information Standards
- **CASRAI Research Output Types** - Standardized publication/output categories
- **CRediT Contributor Roles** - Author contribution taxonomy (14 roles)
- **ORCID Work Types** - Research product classifications
- **Grant Agency Types** - Funding organization categories

**Source**: CASRAI, NISO CRediT, ORCID (16+ million researcher profiles)

### Repository Standards
- **COAR Resource Types v3.2** - 105 scholarly resource types in 25 languages
- **COAR Access Rights** - Open access status vocabulary
- **COAR Version Types** - Manuscript version states
- **DataCite Resource Types** - Research data type classifications
- **DataCite Contributor Types** - Data contributor role types

**Source**: COAR (global repository network), DataCite (12+ million DOIs)

### Scientific Publishing
- **OpenAIRE Fields of Science (FOS)** - OECD discipline taxonomy enhanced
- **UN Sustainable Development Goals** - Research alignment with SDGs
- **Journal Article Sections** - Standardized manuscript sections beyond current set
- **Peer Review Types** - Editorial review processes (single-blind, double-blind, open, etc.)

**Source**: OpenAIRE Research Graph, OECD FOS classification

## 🌍 **MEDIUM PRIORITY: Geographic & Demographic**

### International Geographic Standards
- **ISO 3166-1 Country Codes** - Alpha-2, Alpha-3, numeric country codes (249 countries)
- **ISO 3166-2 Subdivision Codes** - States/provinces/regions (5,046 codes)
- **UN M49 Geographic Regions** - Statistical region classifications
- **GeoNames Feature Classes** - 9 main geographic feature types
- **GeoNames Feature Codes** - 645 detailed geographic feature subtypes

**Source**: ISO 3166 Maintenance Agency, UN Statistics, GeoNames (25M+ places)

### US Geographic Standards
- **FIPS State Codes** - US state/territory codes (still widely used despite withdrawal)
- **FIPS County Codes** - US county identifiers
- **Census Geographic Summary Levels** - Administrative/statistical boundary hierarchy

**Source**: US Census Bureau, ANSI geographic codes

### Demographic Classifications
- **UN Population Age Groups** - Standard demographic age cohorts
- **UN Educational Attainment** - International education level classifications
- **UN Labour Force Status** - Employment status categories
- **UN Household Relationship** - Family/household member relationships

**Source**: UN Statistics Division, World Population Prospects 2024

## 💻 **MEDIUM PRIORITY: Technology & Data Science**

### Software Standards
- **SPDX License Identifiers** - 500+ software license types (ISO/IEC 5962:2021)
- **Programming Language Types** - Major language classifications/paradigms
- **Software Development Methodologies** - Agile, Waterfall, DevOps, etc.
- **Version Control Systems** - Git, SVN, Mercurial, etc.
- **Container Technologies** - Docker, Kubernetes, containerd, etc.

**Source**: SPDX License List, IEEE/ACM computing classifications

### Machine Learning & AI
- **ML Algorithm Categories** - Supervised, unsupervised, reinforcement learning
- **ML Model Types** - Decision trees, neural networks, SVM, etc.
- **Deep Learning Architectures** - CNN, RNN, Transformer, GAN, etc.
- **AI Ethics Categories** - Fairness, accountability, transparency, privacy
- **Data Science Lifecycle Stages** - Collection, processing, modeling, deployment

**Source**: ACM Computing Classification 2012, IEEE AI standards

### Data Formats & Standards
- **Internet Media Types (MIME)** - Extended beyond current basic set
- **Character Encodings** - UTF-8, ASCII, Latin-1, etc.
- **Database Types** - Relational, NoSQL, Graph, Time-series
- **API Specification Formats** - OpenAPI, GraphQL, REST, gRPC
- **Serialization Formats** - JSON, XML, YAML, Protocol Buffers, Avro

**Source**: IANA Media Types Registry, W3C standards

## 🏢 **LOW PRIORITY: Organizational & Business**

### Business Classifications
- **NAICS Industry Codes** - North American Industry Classification (1,065 codes)
- **SIC Industry Codes** - Standard Industrial Classification
- **ISIC Industry Codes** - UN International Standard Industrial Classification
- **Company Legal Forms** - Corporation, LLC, Partnership, etc.
- **Business Relationship Types** - Supplier, customer, partner, subsidiary, etc.

**Source**: US Census Bureau, UN Statistics Division

### Professional Standards
- **Professional Certifications** - Industry-recognized credentials
- **Job Function Categories** - HR/recruitment standard classifications
- **Employment Types** - Full-time, part-time, contract, freelance, etc.
- **Remote Work Arrangements** - On-site, hybrid, fully remote, etc.

## 🔬 **SPECIALIZED DOMAINS** (Domain-Specific Priority)

### Environmental Science
- **Climate Variables** - Temperature, precipitation, humidity classifications
- **Environmental Monitoring Parameters** - Air quality, water quality indicators
- **Ecosystem Types** - Biome and habitat classifications
- **Renewable Energy Sources** - Solar, wind, hydro, geothermal, etc.

### Legal & Regulatory
- **Legal Document Types** - Contracts, regulations, statutes, court decisions
- **Regulatory Frameworks** - GDPR, HIPAA, SOX, FDA, etc.
- **Intellectual Property Types** - Patents, trademarks, copyrights
- **Legal Jurisdiction Types** - Federal, state, local, international

### Finance & Economics
- **Currency Codes (ISO 4217)** - 180 active currency codes
- **Financial Instrument Types** - Stocks, bonds, derivatives, commodities
- **Payment Methods** - Credit card, bank transfer, digital wallet, cryptocurrency
- **Economic Indicator Categories** - GDP, inflation, unemployment, trade

---

## 📊 **Implementation Priority Matrix**

| **Priority** | **Rationale** | **Examples** |
|-------------|---------------|--------------|
| **HIGH** | Wide adoption, standards-based, critical for interoperability | FHIR, OMOP, GA4GH, COAR, ISO 3166 |
| **MEDIUM** | Important but more specialized, good standards backing | SPDX, GeoNames, ACM Classification |
| **LOW** | Useful but limited audience, or well-served by existing alternatives | NAICS, Professional certs |

## 🔗 **Key Sources Summary**

- **HL7 FHIR**: Global healthcare interoperability standard
- **SNOMED International**: Comprehensive clinical terminology
- **GA4GH**: Genomics standards (Phenopackets ISO 4454:2022)
- **OHDSI OMOP**: Observational health data standard (NIH All of Us)
- **CASRAI/ORCID**: Research information management
- **COAR**: Repository and scholarly communication standards
- **ISO**: International geographic and technical standards
- **SPDX**: Software licensing standard (ISO/IEC 5962:2021)
- **ACM/IEEE**: Computing and technology classifications

This research-driven prioritization focuses on widely-adopted, standards-based value sets that would maximize interoperability and utility for the LinkML common value sets project.