# Rare Disease Value Sets

Rare disease research requires precise vocabulary for variant interpretation,
phenotyping, family history, and clinical management. This view collects value
sets from across the clinical, medical, and investigation schema domains that
are commonly needed in rare disease genomics and clinical care.

## Coverage Summary

| Domain | Schema Sources | Enums | Ontologies |
|--------|---------------|------:|------------|
| [Genetics and Variants](#genetics-and-variants) | clinical/phenopackets, clinical/genetics, medical/family_history, bio/bio_entities | 6 | GENO, LOINC, HP, OMIM |
| [Phenotyping and Clinical](#phenotyping-and-clinical) | clinical/phenopackets, medical/clinical, bio/bio_entities | 8 | HP, NCIT, UBERON |
| [Family History and Pedigree](#family-history-and-pedigree) | medical/family_history | 3 | NCIT |
| [Treatment and Response](#treatment-and-response) | clinical/phenopackets, medical/clinical | 3 | NCIT, RxNorm |
| [Diagnostics](#diagnostics) | medical/clinical, bio/sequencing_platforms | 3 | NCIT, OBI |
| [Demographics and Study](#demographics-and-study) | clinical/nih_demographics, investigation | 4 | NCIT, OBI |

---

## Genetics and Variants

Variant interpretation in rare disease follows ACMG/AMP guidelines. These enums
capture allelic state, pathogenicity classification, actionability, and the
interpretation workflow.

### Enums

- [AllelicStateEnum](../elements/AllelicStateEnum.md) -- heterozygous, homozygous, hemizygous
- [ACMGPathogenicityEnum](../elements/ACMGPathogenicityEnum.md) -- ACMG/AMP five-tier variant classification
- [TherapeuticActionabilityEnum](../elements/TherapeuticActionabilityEnum.md) -- clinical actionability of variants
- [InterpretationProgressEnum](../elements/InterpretationProgressEnum.md) -- variant interpretation workflow status
- [GeneticRelationship](../elements/GeneticRelationship.md) -- biological relationships (full sibling, half sibling)
- [GeneticDisease](../elements/GeneticDisease.md) -- genetic diseases (dynamic)

---

## Phenotyping and Clinical

Deep phenotyping is central to rare disease diagnosis. These enums support
structured capture of phenotypic features, anatomical systems, onset timing,
laterality, and severity -- aligned with the Human Phenotype Ontology and
Phenopacket standards.

### Enums

- [KaryotypicSexEnum](../elements/KaryotypicSexEnum.md) -- chromosomal sex determination
- [PhenotypicSexEnum](../elements/PhenotypicSexEnum.md) -- phenotypic sex
- [OnsetTimingEnum](../elements/OnsetTimingEnum.md) -- age of disease onset (congenital, infantile, juvenile, adult)
- [LateralityEnum](../elements/LateralityEnum.md) -- sidedness of clinical findings
- [SymptomSeverityEnum](../elements/SymptomSeverityEnum.md) -- mild, moderate, severe, profound
- [Phenotype](../elements/Phenotype.md) -- phenotypic features (dynamic, HP-backed)
- [Disease](../elements/Disease.md) -- diseases (dynamic, MONDO-backed)
- [AnatomicalSystemEnum](../elements/AnatomicalSystemEnum.md) -- affected organ systems

---

## Family History and Pedigree

Rare disease diagnosis depends heavily on family history. These enums support
pedigree construction and recording of family history completeness.

### Enums

- [FamilyRelationship](../elements/FamilyRelationship.md) -- pedigree relationships (parent, child, sibling, cousin)
- [FamilyHistoryStatus](../elements/FamilyHistoryStatus.md) -- completeness of family history collection
- [GeneticRelationship](../elements/GeneticRelationship.md) -- biological relationships

---

## Treatment and Response

Tracking drug response and treatment regimens is important for rare disease
management and clinical trials.

### Enums

- [DrugResponseEnum](../elements/DrugResponseEnum.md) -- patient response to drug therapy
- [DrugRouteEnum](../elements/DrugRouteEnum.md) -- route of drug administration
- [RegimenStatusEnum](../elements/RegimenStatusEnum.md) -- treatment regimen status

---

## Diagnostics

Rare disease workup involves a range of diagnostic modalities, from biochemical
tests to whole-genome sequencing.

### Enums

- [DiagnosticTestTypeEnum](../elements/DiagnosticTestTypeEnum.md) -- laboratory, imaging, and genetic tests
- [BloodTypeEnum](../elements/BloodTypeEnum.md) -- ABO and Rh blood type classification
- [SequencingPlatform](../elements/SequencingPlatform.md) -- WGS/WES platforms for rare disease diagnosis

---

## Demographics and Study

Rare disease studies require careful demographic characterization and study
design documentation, particularly for natural history studies and registries.

### Enums

- [AgeGroupEnum](../elements/AgeGroupEnum.md) -- pediatric, adolescent, adult, geriatric
- [BiologicalSexEnum](../elements/BiologicalSexEnum.md) -- biological sex at birth
- [StudyDesignEnum](../elements/StudyDesignEnum.md) -- observational, experimental, longitudinal
- [StudyPhaseEnum](../elements/StudyPhaseEnum.md) -- clinical trial phases
