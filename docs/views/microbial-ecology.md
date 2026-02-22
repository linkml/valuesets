# Microbial Ecology Value Sets

Microbial ecology research spans taxonomy, physiology, environmental genomics, and
ecosystem interactions. This view collects value sets from across multiple schema
domains -- biology, earth science, and investigation -- that are commonly needed
when describing microbial communities and their environments.

## Coverage Summary

| Domain | Schema Sources | Enums | Ontologies |
|--------|---------------|------:|------------|
| [Taxonomy and Organisms](#taxonomy-and-organisms) | bio/taxonomy | 4 | NCBITaxon, ENVO |
| [Physiology and Metabolism](#physiology-and-metabolism) | bio/relationship_to_oxygen, bio/bio_entities | 3 | ENVO, GO |
| [Ecological Interactions](#ecological-interactions) | ecological_interactions, bio/bio_entities, industry/mining | 3 | RO, ENVO |
| [Sequencing and Genomics](#sequencing-and-genomics) | bio/sequencing_platforms, bio/genome_features | 5 | OBI, GENEPIO |
| [Aquatic and Subsurface Environments](#aquatic-and-subsurface-environments) | earth_science/water_resources, earth_science/hydrogeology, earth_science/subsurface | 5 | ENVO, CHEBI |
| [Study Design](#study-design) | investigation | 2 | OBI |

---

## Taxonomy and Organisms

Microbial community studies require precise taxonomic classification from domain
level through strain. These enums support both fixed lists of common taxa and
dynamic lookups against the NCBI Taxonomy.

### Enums

- [CommonOrganismTaxaEnum](../elements/CommonOrganismTaxaEnum.md) -- frequently studied bacteria, archaea, and proteobacteria
- [OrganismTaxonEnum](../elements/OrganismTaxonEnum.md) -- dynamic taxonomy lookup
- [TaxonomicRank](../elements/TaxonomicRank.md) -- domain through strain
- [BiologicalKingdom](../elements/BiologicalKingdom.md) -- high-level kingdoms of life

---

## Physiology and Metabolism

Oxygen tolerance and metabolic capabilities are fundamental to characterizing
microbial isolates and interpreting metagenome-assembled genomes.

### Enums

- [RelToOxygenEnum](../elements/RelToOxygenEnum.md) -- aerobe, anaerobe, facultative, microaerophilic
- [BiologicalProcess](../elements/BiologicalProcess.md) -- biological processes (dynamic, GO-backed)
- [BiologicalRole](../elements/BiologicalRole.md) -- functional roles of chemical entities

---

## Ecological Interactions

Microbes exist in complex webs of competition, mutualism, and parasitism. These
enums describe biotic interactions and the environmental materials and impacts
relevant to microbial ecology fieldwork.

### Enums

- [BioticInteractionType](../elements/BioticInteractionType.md) -- predation, parasitism, mutualism, symbiosis, commensalism
- [EnvironmentalMaterial](../elements/EnvironmentalMaterial.md) -- soil, sediment, water, biofilm, and other environmental materials
- [EnvironmentalImpact](../elements/EnvironmentalImpact.md) -- environmental impacts from industrial and natural processes

---

## Sequencing and Genomics

Amplicon sequencing (16S/18S/ITS), metagenomics, and metatranscriptomics are
core methods in microbial ecology. These enums standardize platform, chemistry,
library preparation, and genomic feature descriptions.

### Enums

- [SequencingPlatform](../elements/SequencingPlatform.md) -- Illumina, PacBio, Oxford Nanopore, Ion Torrent
- [SequencingChemistry](../elements/SequencingChemistry.md) -- platform-specific chemistries
- [LibraryPreparation](../elements/LibraryPreparation.md) -- amplicon, shotgun, Hi-C, and other library types
- [GeneFeature](../elements/GeneFeature.md) -- gene-level features (dynamic)
- [GenomeFeatureType](../elements/GenomeFeatureType.md) -- CDS, rRNA, tRNA, CRISPR, and other genome features

---

## Aquatic and Subsurface Environments

Many microbial ecology studies focus on aquatic systems, groundwater, or
subsurface formations. These enums from the earth science domain describe
water resources, aquifer types, and subsurface geological contexts.

### Enums

- [WaterResourceType](../elements/WaterResourceType.md) -- surface water, groundwater, produced water
- [WaterQualityParameterType](../elements/WaterQualityParameterType.md) -- pH, dissolved oxygen, turbidity, nitrate
- [AquiferType](../elements/AquiferType.md) -- unconfined, confined, artesian, karst
- [GroundwaterProcessType](../elements/GroundwaterProcessType.md) -- recharge, discharge, saltwater intrusion
- [SubsurfaceFormationType](../elements/SubsurfaceFormationType.md) -- permafrost, karst, shale, fault zones

---

## Study Design

Microbial ecology experiments range from controlled mesocosms to large-scale
field surveys. These investigation enums capture study-level metadata.

### Enums

- [StudyDesignEnum](../elements/StudyDesignEnum.md) -- observational, experimental, longitudinal, cross-sectional
- [StudyTypeEnum](../elements/StudyTypeEnum.md) -- field study, laboratory study, computational study
