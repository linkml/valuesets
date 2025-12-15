"""
Value Set Stewardship Organizations

Organizations and consortia that steward value sets and terminologies.

This enum is used with the `stewards`, `publishers`, and `endorsers` slots
defined in the valuesets_meta metamodel to track organizational responsibility
for value set content.

## Identifier Guidelines

- **ROR IDs** (https://ror.org/) are preferred for formal organizations
- For consortia without ROR IDs, use canonical website URLs
- All identifiers should be stable, persistent URIs


Generated from: stewardship.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class ValueSetStewardEnum(RichEnum):
    """
    Organizations and consortia that may serve as stewards, publishers, or
    endorsers for value sets. Includes standards bodies, bioinformatics
    consortia, and data coordination centers.
    
    Use ROR IDs where available; otherwise use canonical organization URLs.
    
    """
    # Enum members
    GA4GH = "GA4GH"
    GENE_ONTOLOGY_CONSORTIUM = "GENE_ONTOLOGY_CONSORTIUM"
    GENOMIC_STANDARDS_CONSORTIUM = "GENOMIC_STANDARDS_CONSORTIUM"
    MONARCH_INITIATIVE = "MONARCH_INITIATIVE"
    OBO_FOUNDRY = "OBO_FOUNDRY"
    OHDSI = "OHDSI"
    PHENOPACKETS = "PHENOPACKETS"
    EMBL_EBI = "EMBL_EBI"
    NCBI = "NCBI"
    CDISC = "CDISC"
    HL7 = "HL7"
    ISO = "ISO"
    W3C = "W3C"
    VALUESETS_PROJECT = "VALUESETS_PROJECT"

# Set metadata after class creation
ValueSetStewardEnum._metadata = {
    "GA4GH": {'description': 'International consortium developing standards for responsible sharing\nof genomic and health-related data. Develops standards including\nPhenopackets, VRS, DRS, and Beacon.\n', 'meaning': 'https://ga4gh.org', 'annotations': {'established': '2013', 'headquarters': 'Multiple host institutions', 'website': 'https://ga4gh.org'}, 'aliases': ['Global Alliance for Genomics and Health']},
    "GENE_ONTOLOGY_CONSORTIUM": {'description': "International consortium developing and maintaining the Gene Ontology,\nthe world's largest source of information on gene function. Provides\nGO annotations and the GO ontology itself.\n", 'meaning': 'https://geneontology.org', 'annotations': {'established': '1998', 'website': 'https://geneontology.org'}, 'aliases': ['GO Consortium', 'GOC']},
    "GENOMIC_STANDARDS_CONSORTIUM": {'description': 'Open-membership community developing standards for describing genomes,\nmetagenomes, and related data. Develops MIxS checklists and related\nmetadata standards.\n', 'meaning': 'https://gensc.org', 'annotations': {'established': '2005', 'website': 'https://gensc.org'}, 'aliases': ['GSC']},
    "MONARCH_INITIATIVE": {'description': 'International consortium integrating genotype-phenotype data across\nspecies. Develops and maintains ontologies including HPO, Mondo,\nand Upheno, and provides data integration services.\n', 'meaning': 'https://monarchinitiative.org', 'annotations': {'website': 'https://monarchinitiative.org'}, 'aliases': ['Monarch']},
    "OBO_FOUNDRY": {'description': 'Collaborative effort to develop interoperable ontologies for the\nlife sciences. Coordinates ontology development and establishes\nprinciples for ontology best practices.\n', 'meaning': 'https://obofoundry.org', 'annotations': {'established': '2007', 'website': 'https://obofoundry.org'}, 'aliases': ['Open Biological and Biomedical Ontologies Foundry']},
    "OHDSI": {'description': 'Observational Health Data Sciences and Informatics program.\nInternational collaborative developing open-source analytics solutions\nfor observational health data. Maintains the OMOP Common Data Model.\n', 'meaning': 'https://ohdsi.org', 'annotations': {'established': '2014', 'website': 'https://ohdsi.org', 'coordinating_center': 'Columbia University'}, 'aliases': ['Observational Health Data Sciences and Informatics']},
    "PHENOPACKETS": {'description': 'GA4GH work stream developing standards for sharing disease and\nphenotype information. Develops the Phenopacket Schema for\nrepresenting clinical and phenotypic data.\n', 'meaning': 'https://phenopackets.org', 'annotations': {'parent_organization': 'GA4GH', 'website': 'https://phenopackets.org'}, 'aliases': ['GA4GH Phenopackets']},
    "EMBL_EBI": {'description': "EMBL's European Bioinformatics Institute, a global leader in\nbioinformatics services, databases, and tools. Hosts major resources\nincluding UniProt, Ensembl, and the Ontology Lookup Service.\n", 'meaning': 'ROR:02catss52', 'annotations': {'parent_organization': 'European Molecular Biology Laboratory', 'website': 'https://www.ebi.ac.uk/', 'location': 'Hinxton, UK'}, 'aliases': ['EMBL-EBI', 'EBI']},
    "NCBI": {'description': 'Part of the United States National Library of Medicine. Develops\ndatabases and tools for molecular biology including GenBank,\nPubMed, and the NCBI Taxonomy.\n', 'meaning': 'ROR:02meqm098', 'annotations': {'parent_organization': 'National Library of Medicine', 'website': 'https://www.ncbi.nlm.nih.gov/', 'location': 'Bethesda, MD, USA'}, 'aliases': ['National Center for Biotechnology Information']},
    "CDISC": {'description': 'Clinical Data Interchange Standards Consortium. Develops global\ndata standards for clinical research including CDASH, SDTM,\nand ADaM.\n', 'meaning': 'https://cdisc.org', 'annotations': {'established': '1997', 'website': 'https://cdisc.org'}, 'aliases': ['Clinical Data Interchange Standards Consortium']},
    "HL7": {'description': 'Standards development organization for healthcare information\nexchange. Develops FHIR, CDA, and HL7 v2 messaging standards.\n', 'meaning': 'ROR:029ga8k16', 'annotations': {'established': '1987', 'website': 'https://www.hl7.org/', 'headquarters': 'Ann Arbor, Michigan'}, 'aliases': ['Health Level Seven', 'HL7 International']},
    "ISO": {'description': 'International standard-setting body for industrial and commercial\nstandards. Develops standards across many domains including\nterminology (ISO 704) and healthcare.\n', 'meaning': 'ROR:004s85t07', 'annotations': {'established': '1947', 'website': 'https://www.iso.org/', 'headquarters': 'Geneva, Switzerland'}},
    "W3C": {'description': 'International standards organization for the World Wide Web.\nDevelops standards including RDF, OWL, SPARQL, and accessibility\nguidelines.\n', 'meaning': 'ROR:0059y1582', 'annotations': {'established': '1994', 'website': 'https://www.w3.org/'}},
    "VALUESETS_PROJECT": {'description': 'The valuesets repository itself, for value sets that are community\ncontributions without a specific external steward. Use sparingly;\nprefer identifying an appropriate domain consortium.\n', 'meaning': 'https://github.com/linkml/valuesets', 'annotations': {'website': 'https://w3id.org/valuesets/'}, 'aliases': ['LinkML Valuesets']},
}

__all__ = [
    "ValueSetStewardEnum",
]