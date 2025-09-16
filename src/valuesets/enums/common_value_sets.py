"""
valuesets

A collection of commonly used value sets

Generated from: valuesets.yaml
"""

from __future__ import annotations

from typing import Dict, Any, Optional
from valuesets.generators.rich_enum import RichEnum

class RelativeTimeEnum(RichEnum):
    # Enum members
    BEFORE = "BEFORE"
    AFTER = "AFTER"
    AT_SAME_TIME_AS = "AT_SAME_TIME_AS"

# Set metadata after class creation
RelativeTimeEnum._metadata = {
}

class PresenceEnum(RichEnum):
    # Enum members
    PRESENT = "PRESENT"
    ABSENT = "ABSENT"
    BELOW_DETECTION_LIMIT = "BELOW_DETECTION_LIMIT"
    ABOVE_DETECTION_LIMIT = "ABOVE_DETECTION_LIMIT"

# Set metadata after class creation
PresenceEnum._metadata = {
    "PRESENT": {'description': 'The entity is present'},
    "ABSENT": {'description': 'The entity is absent'},
    "BELOW_DETECTION_LIMIT": {'description': 'The entity is below the detection limit'},
    "ABOVE_DETECTION_LIMIT": {'description': 'The entity is above the detection limit'},
}

class DataAbsentEnum(RichEnum):
    """
    Used to specify why the normally expected content of the data element is missing.
    """
    # Enum members
    UNKNOWN = "unknown"
    ASKED_UNKNOWN = "asked-unknown"
    TEMP_UNKNOWN = "temp-unknown"
    NOT_ASKED = "not-asked"
    ASKED_DECLINED = "asked-declined"
    MASKED = "masked"
    NOT_APPLICABLE = "not-applicable"
    UNSUPPORTED = "unsupported"
    AS_TEXT = "as-text"
    ERROR = "error"
    NOT_A_NUMBER = "not-a-number"
    NEGATIVE_INFINITY = "negative-infinity"
    POSITIVE_INFINITY = "positive-infinity"
    NOT_PERFORMED = "not-performed"
    NOT_PERMITTED = "not-permitted"

# Set metadata after class creation
DataAbsentEnum._metadata = {
    "UNKNOWN": {'description': 'The value is expected to exist but is not known.', 'meaning': 'fhir_data_absent_reason:unknown'},
    "ASKED_UNKNOWN": {'description': 'The source was asked but does not know the value.', 'meaning': 'fhir_data_absent_reason:asked-unknown'},
    "TEMP_UNKNOWN": {'description': 'There is reason to expect (from the workflow) that the value may become known.', 'meaning': 'fhir_data_absent_reason:temp-unknown'},
    "NOT_ASKED": {'description': "The workflow didn't lead to this value being known.", 'meaning': 'fhir_data_absent_reason:not-asked'},
    "ASKED_DECLINED": {'description': 'The source was asked but declined to answer.', 'meaning': 'fhir_data_absent_reason:asked-declined'},
    "MASKED": {'description': 'The information is not available due to security, privacy or related reasons.', 'meaning': 'fhir_data_absent_reason:masked'},
    "NOT_APPLICABLE": {'description': 'There is no proper value for this element (e.g. last menstrual period for a male).', 'meaning': 'fhir_data_absent_reason:not-applicable'},
    "UNSUPPORTED": {'description': "The source system wasn't capable of supporting this element.", 'meaning': 'fhir_data_absent_reason:unsupported'},
    "AS_TEXT": {'description': 'The content of the data is represented in the resource narrative.', 'meaning': 'fhir_data_absent_reason:as-text'},
    "ERROR": {'description': 'Some system or workflow process error means that the information is not available.', 'meaning': 'fhir_data_absent_reason:error'},
    "NOT_A_NUMBER": {'description': 'The numeric value is undefined or unrepresentable due to a floating point processing error.', 'meaning': 'fhir_data_absent_reason:not-a-number'},
    "NEGATIVE_INFINITY": {'description': 'The numeric value is excessively low and unrepresentable due to a floating point processing        error.', 'meaning': 'fhir_data_absent_reason:negative-infinity'},
    "POSITIVE_INFINITY": {'description': 'The numeric value is excessively high and unrepresentable due to a floating point processing        error.', 'meaning': 'fhir_data_absent_reason:positive-infinity'},
    "NOT_PERFORMED": {'description': 'The value is not available because the observation procedure (test, etc.) was not performed.', 'meaning': 'fhir_data_absent_reason:not-performed'},
    "NOT_PERMITTED": {'description': 'The value is not permitted in this context (e.g. due to profiles, or the base data types).', 'meaning': 'fhir_data_absent_reason:not-permitted'},
}

class PredictionOutcomeType(RichEnum):
    # Enum members
    TP = "TP"
    FP = "FP"
    TN = "TN"
    FN = "FN"

# Set metadata after class creation
PredictionOutcomeType._metadata = {
    "TP": {'description': 'True Positive'},
    "FP": {'description': 'False Positive'},
    "TN": {'description': 'True Negative'},
    "FN": {'description': 'False Negative'},
}

class VitalStatusEnum(RichEnum):
    """
    The vital status of a person or organism
    """
    # Enum members
    ALIVE = "ALIVE"
    DECEASED = "DECEASED"
    UNKNOWN = "UNKNOWN"
    PRESUMED_ALIVE = "PRESUMED_ALIVE"
    PRESUMED_DECEASED = "PRESUMED_DECEASED"

# Set metadata after class creation
VitalStatusEnum._metadata = {
    "ALIVE": {'description': 'The person is living', 'meaning': 'NCIT:C37987'},
    "DECEASED": {'description': 'The person has died', 'meaning': 'NCIT:C28554'},
    "UNKNOWN": {'description': 'The vital status is not known', 'meaning': 'NCIT:C17998'},
    "PRESUMED_ALIVE": {'description': 'The person is presumed to be alive based on available information'},
    "PRESUMED_DECEASED": {'description': 'The person is presumed to be deceased based on available information'},
}

class HealthcareEncounterClassification(RichEnum):
    # Enum members
    INPATIENT_VISIT = "Inpatient Visit"
    EMERGENCY_ROOM_VISIT = "Emergency Room Visit"
    EMERGENCY_ROOM_AND_INPATIENT_VISIT = "Emergency Room and Inpatient Visit"
    NON_HOSPITAL_INSTITUTION_VISIT = "Non-hospital institution Visit"
    OUTPATIENT_VISIT = "Outpatient Visit"
    HOME_VISIT = "Home Visit"
    TELEHEALTH_VISIT = "Telehealth Visit"
    PHARMACY_VISIT = "Pharmacy Visit"
    LABORATORY_VISIT = "Laboratory Visit"
    AMBULANCE_VISIT = "Ambulance Visit"
    CASE_MANAGEMENT_VISIT = "Case Management Visit"

# Set metadata after class creation
HealthcareEncounterClassification._metadata = {
    "INPATIENT_VISIT": {'description': 'Person visiting hospital, at a Care Site, in bed, for duration of more than one day, with physicians and other Providers permanently available to deliver service around the clock'},
    "EMERGENCY_ROOM_VISIT": {'description': 'Person visiting dedicated healthcare institution for treating emergencies, at a Care Site, within one day, with physicians and Providers permanently available to deliver service around the clock'},
    "EMERGENCY_ROOM_AND_INPATIENT_VISIT": {'description': 'Person visiting ER followed by a subsequent Inpatient Visit, where Emergency department is part of hospital, and transition from the ER to other hospital departments is undefined'},
    "NON_HOSPITAL_INSTITUTION_VISIT": {'description': 'Person visiting dedicated institution for reasons of poor health, at a Care Site, long-term or permanently, with no physician but possibly other Providers permanently available to deliver service around the clock'},
    "OUTPATIENT_VISIT": {'description': 'Person visiting dedicated ambulatory healthcare institution, at a Care Site, within one day, without bed, with physicians or medical Providers delivering service during Visit'},
    "HOME_VISIT": {'description': 'Provider visiting Person, without a Care Site, within one day, delivering service'},
    "TELEHEALTH_VISIT": {'description': 'Patient engages with Provider through communication media'},
    "PHARMACY_VISIT": {'description': 'Person visiting pharmacy for dispensing of Drug, at a Care Site, within one day'},
    "LABORATORY_VISIT": {'description': 'Patient visiting dedicated institution, at a Care Site, within one day, for the purpose of a Measurement.'},
    "AMBULANCE_VISIT": {'description': 'Person using transportation service for the purpose of initiating one of the other Visits, without a Care Site, within one day, potentially with Providers accompanying the Visit and delivering service'},
    "CASE_MANAGEMENT_VISIT": {'description': 'Person interacting with healthcare system, without a Care Site, within a day, with no Providers involved, for administrative purposes'},
}

class CaseOrControlEnum(RichEnum):
    # Enum members
    CASE = "CASE"
    CONTROL = "CONTROL"

# Set metadata after class creation
CaseOrControlEnum._metadata = {
    "CASE": {'meaning': 'OBI:0002492'},
    "CONTROL": {'meaning': 'OBI:0002493'},
}

class GOEvidenceCode(RichEnum):
    """
    Gene Ontology evidence codes mapped to Evidence and Conclusion Ontology (ECO) terms
    """
    # Enum members
    EXP = "EXP"
    IDA = "IDA"
    IPI = "IPI"
    IMP = "IMP"
    IGI = "IGI"
    IEP = "IEP"
    HTP = "HTP"
    HDA = "HDA"
    HMP = "HMP"
    HGI = "HGI"
    HEP = "HEP"
    IBA = "IBA"
    IBD = "IBD"
    IKR = "IKR"
    IRD = "IRD"
    ISS = "ISS"
    ISO = "ISO"
    ISA = "ISA"
    ISM = "ISM"
    IGC = "IGC"
    RCA = "RCA"
    TAS = "TAS"
    NAS = "NAS"
    IC = "IC"
    ND = "ND"
    IEA = "IEA"

# Set metadata after class creation
GOEvidenceCode._metadata = {
    "EXP": {'meaning': 'ECO:0000269', 'aliases': ['experimental evidence used in manual assertion']},
    "IDA": {'meaning': 'ECO:0000314', 'aliases': ['direct assay evidence used in manual assertion']},
    "IPI": {'meaning': 'ECO:0000353', 'aliases': ['physical interaction evidence used in manual assertion']},
    "IMP": {'meaning': 'ECO:0000315', 'aliases': ['mutant phenotype evidence used in manual assertion']},
    "IGI": {'meaning': 'ECO:0000316', 'aliases': ['genetic interaction evidence used in manual assertion']},
    "IEP": {'meaning': 'ECO:0000270', 'aliases': ['expression pattern evidence used in manual assertion']},
    "HTP": {'meaning': 'ECO:0006056', 'aliases': ['high throughput evidence used in manual assertion']},
    "HDA": {'meaning': 'ECO:0007005', 'aliases': ['high throughput direct assay evidence used in manual assertion']},
    "HMP": {'meaning': 'ECO:0007001', 'aliases': ['high throughput mutant phenotypic evidence used in manual assertion']},
    "HGI": {'meaning': 'ECO:0007003', 'aliases': ['high throughput genetic interaction phenotypic evidence used in manual assertion']},
    "HEP": {'meaning': 'ECO:0007007', 'aliases': ['high throughput expression pattern evidence used in manual assertion']},
    "IBA": {'meaning': 'ECO:0000318', 'aliases': ['biological aspect of ancestor evidence used in manual assertion']},
    "IBD": {'meaning': 'ECO:0000319', 'aliases': ['biological aspect of descendant evidence used in manual assertion']},
    "IKR": {'meaning': 'ECO:0000320', 'aliases': ['phylogenetic determination of loss of key residues evidence used in manual assertion']},
    "IRD": {'meaning': 'ECO:0000321', 'aliases': ['rapid divergence from ancestral sequence evidence used in manual assertion']},
    "ISS": {'meaning': 'ECO:0000250', 'aliases': ['sequence similarity evidence used in manual assertion']},
    "ISO": {'meaning': 'ECO:0000266', 'aliases': ['sequence orthology evidence used in manual assertion']},
    "ISA": {'meaning': 'ECO:0000247', 'aliases': ['sequence alignment evidence used in manual assertion']},
    "ISM": {'meaning': 'ECO:0000255', 'aliases': ['match to sequence model evidence used in manual assertion']},
    "IGC": {'meaning': 'ECO:0000317', 'aliases': ['genomic context evidence used in manual assertion']},
    "RCA": {'meaning': 'ECO:0000245', 'aliases': ['automatically integrated combinatorial evidence used in manual assertion']},
    "TAS": {'meaning': 'ECO:0000304', 'aliases': ['author statement supported by traceable reference used in manual assertion']},
    "NAS": {'meaning': 'ECO:0000303', 'aliases': ['author statement without traceable support used in manual assertion']},
    "IC": {'meaning': 'ECO:0000305', 'aliases': ['curator inference used in manual assertion']},
    "ND": {'meaning': 'ECO:0000307', 'aliases': ['no evidence data found used in manual assertion']},
    "IEA": {'meaning': 'ECO:0000501', 'aliases': ['evidence used in automatic assertion']},
}

class GOElectronicMethods(RichEnum):
    """
    Electronic annotation methods used in Gene Ontology, identified by GO_REF codes
    """
    # Enum members
    INTERPRO2GO = "INTERPRO2GO"
    EC2GO = "EC2GO"
    UNIPROTKB_KW2GO = "UNIPROTKB_KW2GO"
    UNIPROTKB_SUBCELL2GO = "UNIPROTKB_SUBCELL2GO"
    HAMAP_RULE2GO = "HAMAP_RULE2GO"
    UNIPATHWAY2GO = "UNIPATHWAY2GO"
    UNIRULE2GO = "UNIRULE2GO"
    RHEA2GO = "RHEA2GO"
    ENSEMBL_COMPARA = "ENSEMBL_COMPARA"
    PANTHER = "PANTHER"
    REACTOME = "REACTOME"
    RFAM2GO = "RFAM2GO"
    DICTYBASE = "DICTYBASE"
    MGI = "MGI"
    ZFIN = "ZFIN"
    FLYBASE = "FLYBASE"
    WORMBASE = "WORMBASE"
    SGD = "SGD"
    POMBASE = "POMBASE"
    METACYC2GO = "METACYC2GO"

# Set metadata after class creation
GOElectronicMethods._metadata = {
    "INTERPRO2GO": {'meaning': 'GO_REF:0000002'},
    "EC2GO": {'meaning': 'GO_REF:0000003'},
    "UNIPROTKB_KW2GO": {'meaning': 'GO_REF:0000004'},
    "UNIPROTKB_SUBCELL2GO": {'meaning': 'GO_REF:0000023'},
    "HAMAP_RULE2GO": {'meaning': 'GO_REF:0000020'},
    "UNIPATHWAY2GO": {'meaning': 'GO_REF:0000041'},
    "UNIRULE2GO": {'meaning': 'GO_REF:0000104'},
    "RHEA2GO": {'meaning': 'GO_REF:0000116'},
    "ENSEMBL_COMPARA": {'meaning': 'GO_REF:0000107'},
    "PANTHER": {'meaning': 'GO_REF:0000033'},
    "REACTOME": {'meaning': 'GO_REF:0000018'},
    "RFAM2GO": {'meaning': 'GO_REF:0000115'},
    "DICTYBASE": {'meaning': 'GO_REF:0000015'},
    "MGI": {'meaning': 'GO_REF:0000096'},
    "ZFIN": {'meaning': 'GO_REF:0000031'},
    "FLYBASE": {'meaning': 'GO_REF:0000047'},
    "WORMBASE": {'meaning': 'GO_REF:0000003'},
    "SGD": {'meaning': 'GO_REF:0000100'},
    "POMBASE": {'meaning': 'GO_REF:0000024'},
    "METACYC2GO": {'meaning': 'GO_REF:0000112'},
}

class CommonOrganismTaxaEnum(RichEnum):
    """
    Common model organisms used in biological research, mapped to NCBI Taxonomy IDs
    """
    # Enum members
    BACTERIA = "BACTERIA"
    ARCHAEA = "ARCHAEA"
    EUKARYOTA = "EUKARYOTA"
    VIRUSES = "VIRUSES"
    VERTEBRATA = "VERTEBRATA"
    MAMMALIA = "MAMMALIA"
    PRIMATES = "PRIMATES"
    RODENTIA = "RODENTIA"
    CARNIVORA = "CARNIVORA"
    ARTIODACTYLA = "ARTIODACTYLA"
    AVES = "AVES"
    ACTINOPTERYGII = "ACTINOPTERYGII"
    AMPHIBIA = "AMPHIBIA"
    ARTHROPODA = "ARTHROPODA"
    INSECTA = "INSECTA"
    NEMATODA = "NEMATODA"
    FUNGI = "FUNGI"
    ASCOMYCOTA = "ASCOMYCOTA"
    VIRIDIPLANTAE = "VIRIDIPLANTAE"
    MAGNOLIOPHYTA = "MAGNOLIOPHYTA"
    PROTEOBACTERIA = "PROTEOBACTERIA"
    GAMMAPROTEOBACTERIA = "GAMMAPROTEOBACTERIA"
    FIRMICUTES = "FIRMICUTES"
    ACTINOBACTERIA = "ACTINOBACTERIA"
    EURYARCHAEOTA = "EURYARCHAEOTA"
    APICOMPLEXA = "APICOMPLEXA"
    HUMAN = "HUMAN"
    MOUSE = "MOUSE"
    RAT = "RAT"
    RHESUS = "RHESUS"
    CHIMP = "CHIMP"
    DOG = "DOG"
    COW = "COW"
    PIG = "PIG"
    CHICKEN = "CHICKEN"
    ZEBRAFISH = "ZEBRAFISH"
    MEDAKA = "MEDAKA"
    PUFFERFISH = "PUFFERFISH"
    XENOPUS_TROPICALIS = "XENOPUS_TROPICALIS"
    XENOPUS_LAEVIS = "XENOPUS_LAEVIS"
    DROSOPHILA = "DROSOPHILA"
    C_ELEGANS = "C_ELEGANS"
    S_CEREVISIAE = "S_CEREVISIAE"
    S_CEREVISIAE_S288C = "S_CEREVISIAE_S288C"
    S_POMBE = "S_POMBE"
    C_ALBICANS = "C_ALBICANS"
    A_NIDULANS = "A_NIDULANS"
    N_CRASSA = "N_CRASSA"
    ARABIDOPSIS = "ARABIDOPSIS"
    RICE = "RICE"
    MAIZE = "MAIZE"
    TOMATO = "TOMATO"
    TOBACCO = "TOBACCO"
    E_COLI = "E_COLI"
    E_COLI_K12 = "E_COLI_K12"
    B_SUBTILIS = "B_SUBTILIS"
    M_TUBERCULOSIS = "M_TUBERCULOSIS"
    P_AERUGINOSA = "P_AERUGINOSA"
    S_AUREUS = "S_AUREUS"
    S_PNEUMONIAE = "S_PNEUMONIAE"
    H_PYLORI = "H_PYLORI"
    M_JANNASCHII = "M_JANNASCHII"
    H_SALINARUM = "H_SALINARUM"
    P_FALCIPARUM = "P_FALCIPARUM"
    T_GONDII = "T_GONDII"
    T_BRUCEI = "T_BRUCEI"
    DICTYOSTELIUM = "DICTYOSTELIUM"
    TETRAHYMENA = "TETRAHYMENA"
    PARAMECIUM = "PARAMECIUM"
    CHLAMYDOMONAS = "CHLAMYDOMONAS"
    PHAGE_LAMBDA = "PHAGE_LAMBDA"
    HIV1 = "HIV1"
    INFLUENZA_A = "INFLUENZA_A"
    SARS_COV_2 = "SARS_COV_2"

# Set metadata after class creation
CommonOrganismTaxaEnum._metadata = {
    "BACTERIA": {'description': 'Bacteria domain', 'meaning': 'NCBITaxon:2'},
    "ARCHAEA": {'description': 'Archaea domain', 'meaning': 'NCBITaxon:2157'},
    "EUKARYOTA": {'description': 'Eukaryota domain', 'meaning': 'NCBITaxon:2759'},
    "VIRUSES": {'description': 'Viruses (not a true domain)', 'meaning': 'NCBITaxon:10239'},
    "VERTEBRATA": {'description': 'Vertebrates', 'meaning': 'NCBITaxon:7742'},
    "MAMMALIA": {'description': 'Mammals', 'meaning': 'NCBITaxon:40674'},
    "PRIMATES": {'description': 'Primates', 'meaning': 'NCBITaxon:9443'},
    "RODENTIA": {'description': 'Rodents', 'meaning': 'NCBITaxon:9989'},
    "CARNIVORA": {'description': 'Carnivores', 'meaning': 'NCBITaxon:33554'},
    "ARTIODACTYLA": {'description': 'Even-toed ungulates', 'meaning': 'NCBITaxon:91561'},
    "AVES": {'description': 'Birds', 'meaning': 'NCBITaxon:8782'},
    "ACTINOPTERYGII": {'description': 'Ray-finned fishes', 'meaning': 'NCBITaxon:7898'},
    "AMPHIBIA": {'description': 'Amphibians', 'meaning': 'NCBITaxon:8292'},
    "ARTHROPODA": {'description': 'Arthropods', 'meaning': 'NCBITaxon:6656'},
    "INSECTA": {'description': 'Insects', 'meaning': 'NCBITaxon:50557'},
    "NEMATODA": {'description': 'Roundworms', 'meaning': 'NCBITaxon:6231'},
    "FUNGI": {'description': 'Fungal kingdom', 'meaning': 'NCBITaxon:4751'},
    "ASCOMYCOTA": {'description': 'Sac fungi', 'meaning': 'NCBITaxon:4890'},
    "VIRIDIPLANTAE": {'description': 'Green plants', 'meaning': 'NCBITaxon:33090'},
    "MAGNOLIOPHYTA": {'description': 'Flowering plants', 'meaning': 'NCBITaxon:3398'},
    "PROTEOBACTERIA": {'description': 'Proteobacteria', 'meaning': 'NCBITaxon:1224'},
    "GAMMAPROTEOBACTERIA": {'description': 'Gamma proteobacteria', 'meaning': 'NCBITaxon:1236'},
    "FIRMICUTES": {'description': 'Firmicutes (Gram-positive bacteria)', 'meaning': 'NCBITaxon:1239'},
    "ACTINOBACTERIA": {'description': 'Actinobacteria', 'meaning': 'NCBITaxon:201174'},
    "EURYARCHAEOTA": {'description': 'Euryarchaeota', 'meaning': 'NCBITaxon:28890'},
    "APICOMPLEXA": {'description': 'Apicomplexan parasites', 'meaning': 'NCBITaxon:5794'},
    "HUMAN": {'description': 'Homo sapiens (human)', 'meaning': 'NCBITaxon:9606'},
    "MOUSE": {'description': 'Mus musculus (house mouse)', 'meaning': 'NCBITaxon:10090'},
    "RAT": {'description': 'Rattus norvegicus (Norway rat)', 'meaning': 'NCBITaxon:10116'},
    "RHESUS": {'description': 'Macaca mulatta (rhesus macaque)', 'meaning': 'NCBITaxon:9544'},
    "CHIMP": {'description': 'Pan troglodytes (chimpanzee)', 'meaning': 'NCBITaxon:9598'},
    "DOG": {'description': 'Canis lupus familiaris (dog)', 'meaning': 'NCBITaxon:9615'},
    "COW": {'description': 'Bos taurus (cattle)', 'meaning': 'NCBITaxon:9913'},
    "PIG": {'description': 'Sus scrofa (pig)', 'meaning': 'NCBITaxon:9823'},
    "CHICKEN": {'description': 'Gallus gallus (chicken)', 'meaning': 'NCBITaxon:9031'},
    "ZEBRAFISH": {'description': 'Danio rerio (zebrafish)', 'meaning': 'NCBITaxon:7955'},
    "MEDAKA": {'description': 'Oryzias latipes (Japanese medaka)', 'meaning': 'NCBITaxon:8090'},
    "PUFFERFISH": {'description': 'Takifugu rubripes (torafugu)', 'meaning': 'NCBITaxon:31033'},
    "XENOPUS_TROPICALIS": {'description': 'Xenopus tropicalis (western clawed frog)', 'meaning': 'NCBITaxon:8364'},
    "XENOPUS_LAEVIS": {'description': 'Xenopus laevis (African clawed frog)', 'meaning': 'NCBITaxon:8355'},
    "DROSOPHILA": {'description': 'Drosophila melanogaster (fruit fly)', 'meaning': 'NCBITaxon:7227'},
    "C_ELEGANS": {'description': 'Caenorhabditis elegans (roundworm)', 'meaning': 'NCBITaxon:6239'},
    "S_CEREVISIAE": {'description': "Saccharomyces cerevisiae (baker's yeast)", 'meaning': 'NCBITaxon:4932'},
    "S_CEREVISIAE_S288C": {'description': 'Saccharomyces cerevisiae S288C (reference strain)', 'meaning': 'NCBITaxon:559292'},
    "S_POMBE": {'description': 'Schizosaccharomyces pombe (fission yeast)', 'meaning': 'NCBITaxon:4896'},
    "C_ALBICANS": {'description': 'Candida albicans (pathogenic yeast)', 'meaning': 'NCBITaxon:5476'},
    "A_NIDULANS": {'description': 'Aspergillus nidulans (filamentous fungus)', 'meaning': 'NCBITaxon:162425'},
    "N_CRASSA": {'description': 'Neurospora crassa (red bread mold)', 'meaning': 'NCBITaxon:5141'},
    "ARABIDOPSIS": {'description': 'Arabidopsis thaliana (thale cress)', 'meaning': 'NCBITaxon:3702'},
    "RICE": {'description': 'Oryza sativa (rice)', 'meaning': 'NCBITaxon:4530'},
    "MAIZE": {'description': 'Zea mays (corn)', 'meaning': 'NCBITaxon:4577'},
    "TOMATO": {'description': 'Solanum lycopersicum (tomato)', 'meaning': 'NCBITaxon:4081'},
    "TOBACCO": {'description': 'Nicotiana tabacum (tobacco)', 'meaning': 'NCBITaxon:4097'},
    "E_COLI": {'description': 'Escherichia coli', 'meaning': 'NCBITaxon:562'},
    "E_COLI_K12": {'description': 'Escherichia coli str. K-12', 'meaning': 'NCBITaxon:83333'},
    "B_SUBTILIS": {'description': 'Bacillus subtilis', 'meaning': 'NCBITaxon:1423'},
    "M_TUBERCULOSIS": {'description': 'Mycobacterium tuberculosis', 'meaning': 'NCBITaxon:1773'},
    "P_AERUGINOSA": {'description': 'Pseudomonas aeruginosa', 'meaning': 'NCBITaxon:287'},
    "S_AUREUS": {'description': 'Staphylococcus aureus', 'meaning': 'NCBITaxon:1280'},
    "S_PNEUMONIAE": {'description': 'Streptococcus pneumoniae', 'meaning': 'NCBITaxon:1313'},
    "H_PYLORI": {'description': 'Helicobacter pylori', 'meaning': 'NCBITaxon:210'},
    "M_JANNASCHII": {'description': 'Methanocaldococcus jannaschii', 'meaning': 'NCBITaxon:2190'},
    "H_SALINARUM": {'description': 'Halobacterium salinarum', 'meaning': 'NCBITaxon:2242'},
    "P_FALCIPARUM": {'description': 'Plasmodium falciparum (malaria parasite)', 'meaning': 'NCBITaxon:5833'},
    "T_GONDII": {'description': 'Toxoplasma gondii', 'meaning': 'NCBITaxon:5811'},
    "T_BRUCEI": {'description': 'Trypanosoma brucei', 'meaning': 'NCBITaxon:5691'},
    "DICTYOSTELIUM": {'description': 'Dictyostelium discoideum (slime mold)', 'meaning': 'NCBITaxon:44689'},
    "TETRAHYMENA": {'description': 'Tetrahymena thermophila', 'meaning': 'NCBITaxon:5911'},
    "PARAMECIUM": {'description': 'Paramecium tetraurelia', 'meaning': 'NCBITaxon:5888'},
    "CHLAMYDOMONAS": {'description': 'Chlamydomonas reinhardtii (green alga)', 'meaning': 'NCBITaxon:3055'},
    "PHAGE_LAMBDA": {'description': 'Escherichia phage lambda', 'meaning': 'NCBITaxon:10710'},
    "HIV1": {'description': 'Human immunodeficiency virus 1', 'meaning': 'NCBITaxon:11676'},
    "INFLUENZA_A": {'description': 'Influenza A virus', 'meaning': 'NCBITaxon:11320'},
    "SARS_COV_2": {'description': 'Severe acute respiratory syndrome coronavirus 2', 'meaning': 'NCBITaxon:2697049'},
}

class TaxonomicRank(RichEnum):
    """
    Standard taxonomic ranks used in biological classification
    """
    # Enum members
    DOMAIN = "DOMAIN"
    KINGDOM = "KINGDOM"
    PHYLUM = "PHYLUM"
    CLASS = "CLASS"
    ORDER = "ORDER"
    FAMILY = "FAMILY"
    GENUS = "GENUS"
    SPECIES = "SPECIES"
    SUBSPECIES = "SUBSPECIES"
    STRAIN = "STRAIN"
    VARIETY = "VARIETY"
    FORM = "FORM"
    CULTIVAR = "CULTIVAR"

# Set metadata after class creation
TaxonomicRank._metadata = {
    "DOMAIN": {'description': 'Domain (highest rank)', 'meaning': 'TAXRANK:0000037'},
    "KINGDOM": {'description': 'Kingdom', 'meaning': 'TAXRANK:0000017'},
    "PHYLUM": {'description': 'Phylum (animals, plants, fungi) or Division (plants)', 'meaning': 'TAXRANK:0000001'},
    "CLASS": {'description': 'Class', 'meaning': 'TAXRANK:0000002'},
    "ORDER": {'description': 'Order', 'meaning': 'TAXRANK:0000003'},
    "FAMILY": {'description': 'Family', 'meaning': 'TAXRANK:0000004'},
    "GENUS": {'description': 'Genus', 'meaning': 'TAXRANK:0000005'},
    "SPECIES": {'description': 'Species', 'meaning': 'TAXRANK:0000006'},
    "SUBSPECIES": {'description': 'Subspecies', 'meaning': 'TAXRANK:0000023'},
    "STRAIN": {'description': 'Strain (especially for microorganisms)', 'meaning': 'TAXRANK:0001001'},
    "VARIETY": {'description': 'Variety (mainly plants)', 'meaning': 'TAXRANK:0000016'},
    "FORM": {'description': 'Form (mainly plants)', 'meaning': 'TAXRANK:0000026'},
    "CULTIVAR": {'description': 'Cultivar (cultivated variety)', 'meaning': 'TAXRANK:0000034'},
}

class BiologicalKingdom(RichEnum):
    """
    Major kingdoms/domains of life
    """
    # Enum members
    BACTERIA = "BACTERIA"
    ARCHAEA = "ARCHAEA"
    EUKARYOTA = "EUKARYOTA"
    ANIMALIA = "ANIMALIA"
    PLANTAE = "PLANTAE"
    FUNGI = "FUNGI"
    PROTISTA = "PROTISTA"
    VIRUSES = "VIRUSES"

# Set metadata after class creation
BiologicalKingdom._metadata = {
    "BACTERIA": {'description': 'Bacteria domain', 'meaning': 'NCBITaxon:2'},
    "ARCHAEA": {'description': 'Archaea domain', 'meaning': 'NCBITaxon:2157'},
    "EUKARYOTA": {'description': 'Eukaryota domain', 'meaning': 'NCBITaxon:2759'},
    "ANIMALIA": {'description': 'Animal kingdom', 'meaning': 'NCBITaxon:33208'},
    "PLANTAE": {'description': 'Plant kingdom (Viridiplantae)', 'meaning': 'NCBITaxon:33090'},
    "FUNGI": {'description': 'Fungal kingdom', 'meaning': 'NCBITaxon:4751'},
    "PROTISTA": {'description': 'Protist kingdom (polyphyletic group)'},
    "VIRUSES": {'description': 'Viruses (not a true kingdom)', 'meaning': 'NCBITaxon:10239'},
}

class CellCyclePhase(RichEnum):
    """
    Major phases of the eukaryotic cell cycle
    """
    # Enum members
    G0 = "G0"
    G1 = "G1"
    S = "S"
    G2 = "G2"
    M = "M"
    INTERPHASE = "INTERPHASE"

# Set metadata after class creation
CellCyclePhase._metadata = {
    "G0": {'description': 'G0 phase (quiescent/resting phase)', 'meaning': 'GO:0044838', 'annotations': {'aliases': 'quiescent phase, resting phase'}},
    "G1": {'description': 'G1 phase (Gap 1)', 'meaning': 'GO:0051318', 'annotations': {'aliases': 'Gap 1, first gap phase', 'duration': 'variable (hours to years)'}},
    "S": {'description': 'S phase (DNA synthesis)', 'meaning': 'GO:0051320', 'annotations': {'aliases': 'synthesis phase, DNA replication phase', 'duration': '6-8 hours'}},
    "G2": {'description': 'G2 phase (Gap 2)', 'meaning': 'GO:0051319', 'annotations': {'aliases': 'Gap 2, second gap phase', 'duration': '3-4 hours'}},
    "M": {'description': 'M phase (mitosis and cytokinesis)', 'meaning': 'GO:0000279', 'annotations': {'aliases': 'mitotic phase, division phase', 'duration': '~1 hour'}},
    "INTERPHASE": {'description': 'Interphase (G1, S, and G2 phases combined)', 'meaning': 'GO:0051325', 'annotations': {'includes': 'G1, S, G2'}},
}

class MitoticPhase(RichEnum):
    """
    Stages of mitosis (M phase)
    """
    # Enum members
    PROPHASE = "PROPHASE"
    PROMETAPHASE = "PROMETAPHASE"
    METAPHASE = "METAPHASE"
    ANAPHASE = "ANAPHASE"
    TELOPHASE = "TELOPHASE"
    CYTOKINESIS = "CYTOKINESIS"

# Set metadata after class creation
MitoticPhase._metadata = {
    "PROPHASE": {'description': 'Prophase', 'meaning': 'GO:0051324', 'annotations': {'order': 1, 'features': 'chromatin condensation, spindle formation begins'}},
    "PROMETAPHASE": {'description': 'Prometaphase', 'meaning': 'GO:0007080', 'annotations': {'order': 2, 'features': 'nuclear envelope breakdown, kinetochore attachment'}},
    "METAPHASE": {'description': 'Metaphase', 'meaning': 'GO:0051323', 'annotations': {'order': 3, 'features': 'chromosomes aligned at metaphase plate'}},
    "ANAPHASE": {'description': 'Anaphase', 'meaning': 'GO:0051322', 'annotations': {'order': 4, 'features': 'sister chromatid separation'}},
    "TELOPHASE": {'description': 'Telophase', 'meaning': 'GO:0051326', 'annotations': {'order': 5, 'features': 'nuclear envelope reformation'}},
    "CYTOKINESIS": {'description': 'Cytokinesis', 'meaning': 'GO:0000910', 'annotations': {'order': 6, 'features': 'cytoplasmic division'}},
}

class CellCycleCheckpoint(RichEnum):
    """
    Cell cycle checkpoints that regulate progression
    """
    # Enum members
    G1_S_CHECKPOINT = "G1_S_CHECKPOINT"
    INTRA_S_CHECKPOINT = "INTRA_S_CHECKPOINT"
    G2_M_CHECKPOINT = "G2_M_CHECKPOINT"
    SPINDLE_CHECKPOINT = "SPINDLE_CHECKPOINT"

# Set metadata after class creation
CellCycleCheckpoint._metadata = {
    "G1_S_CHECKPOINT": {'description': 'G1/S checkpoint (Restriction point)', 'meaning': 'GO:0000082', 'annotations': {'aliases': 'Start checkpoint, Restriction point, R point', 'regulator': 'p53, Rb'}},
    "INTRA_S_CHECKPOINT": {'description': 'Intra-S checkpoint', 'meaning': 'GO:0031573', 'annotations': {'function': 'monitors DNA replication', 'regulator': 'ATR, CHK1'}},
    "G2_M_CHECKPOINT": {'description': 'G2/M checkpoint', 'meaning': 'GO:0031571', 'annotations': {'function': 'ensures DNA properly replicated', 'regulator': 'p53, CHK1, CHK2'}},
    "SPINDLE_CHECKPOINT": {'description': 'Spindle checkpoint (M checkpoint)', 'meaning': 'GO:0031577', 'annotations': {'aliases': 'SAC, spindle assembly checkpoint', 'function': 'ensures proper chromosome attachment', 'regulator': 'MAD2, BubR1'}},
}

class MeioticPhase(RichEnum):
    """
    Phases specific to meiotic cell division
    """
    # Enum members
    MEIOSIS_I = "MEIOSIS_I"
    PROPHASE_I = "PROPHASE_I"
    METAPHASE_I = "METAPHASE_I"
    ANAPHASE_I = "ANAPHASE_I"
    TELOPHASE_I = "TELOPHASE_I"
    MEIOSIS_II = "MEIOSIS_II"
    PROPHASE_II = "PROPHASE_II"
    METAPHASE_II = "METAPHASE_II"
    ANAPHASE_II = "ANAPHASE_II"
    TELOPHASE_II = "TELOPHASE_II"

# Set metadata after class creation
MeioticPhase._metadata = {
    "MEIOSIS_I": {'description': 'Meiosis I (reductional division)', 'meaning': 'GO:0007126', 'annotations': {'result': 'reduction from diploid to haploid'}},
    "PROPHASE_I": {'description': 'Prophase I', 'meaning': 'GO:0007128', 'annotations': {'substages': 'leptotene, zygotene, pachytene, diplotene, diakinesis'}},
    "METAPHASE_I": {'description': 'Metaphase I', 'meaning': 'GO:0007132', 'annotations': {'feature': 'homologous pairs align'}},
    "ANAPHASE_I": {'description': 'Anaphase I', 'meaning': 'GO:0007133', 'annotations': {'feature': 'homologous chromosomes separate'}},
    "TELOPHASE_I": {'description': 'Telophase I', 'meaning': 'GO:0007134'},
    "MEIOSIS_II": {'description': 'Meiosis II (equational division)', 'meaning': 'GO:0007135', 'annotations': {'similarity': 'similar to mitosis'}},
    "PROPHASE_II": {'description': 'Prophase II', 'meaning': 'GO:0007136'},
    "METAPHASE_II": {'description': 'Metaphase II', 'meaning': 'GO:0007137'},
    "ANAPHASE_II": {'description': 'Anaphase II', 'meaning': 'GO:0007138', 'annotations': {'feature': 'sister chromatids separate'}},
    "TELOPHASE_II": {'description': 'Telophase II', 'meaning': 'GO:0007139'},
}

class CellCycleRegulator(RichEnum):
    """
    Types of cell cycle regulatory molecules
    """
    # Enum members
    CYCLIN = "CYCLIN"
    CDK = "CDK"
    CDK_INHIBITOR = "CDK_INHIBITOR"
    CHECKPOINT_KINASE = "CHECKPOINT_KINASE"
    TUMOR_SUPPRESSOR = "TUMOR_SUPPRESSOR"
    E3_UBIQUITIN_LIGASE = "E3_UBIQUITIN_LIGASE"
    PHOSPHATASE = "PHOSPHATASE"

# Set metadata after class creation
CellCycleRegulator._metadata = {
    "CYCLIN": {'description': 'Cyclin proteins', 'meaning': 'GO:0016538', 'annotations': {'examples': 'Cyclin A, B, D, E'}},
    "CDK": {'description': 'Cyclin-dependent kinase', 'meaning': 'GO:0004693', 'annotations': {'examples': 'CDK1, CDK2, CDK4, CDK6'}},
    "CDK_INHIBITOR": {'description': 'CDK inhibitor', 'meaning': 'GO:0004861', 'annotations': {'examples': 'p21, p27, p57'}},
    "CHECKPOINT_KINASE": {'description': 'Checkpoint kinase', 'meaning': 'GO:0000077', 'annotations': {'examples': 'CHK1, CHK2, ATR, ATM'}},
    "TUMOR_SUPPRESSOR": {'description': 'Tumor suppressor involved in cell cycle', 'meaning': 'GO:0051726', 'annotations': {'examples': 'p53, Rb, BRCA1, BRCA2'}},
    "E3_UBIQUITIN_LIGASE": {'description': 'E3 ubiquitin ligase (cell cycle)', 'meaning': 'GO:0051437', 'annotations': {'examples': 'APC/C, SCF'}},
    "PHOSPHATASE": {'description': 'Cell cycle phosphatase', 'meaning': 'GO:0004721', 'annotations': {'examples': 'CDC25A, CDC25B, CDC25C'}},
}

class CellProliferationState(RichEnum):
    """
    Cell proliferation and growth states
    """
    # Enum members
    PROLIFERATING = "PROLIFERATING"
    QUIESCENT = "QUIESCENT"
    SENESCENT = "SENESCENT"
    DIFFERENTIATED = "DIFFERENTIATED"
    APOPTOTIC = "APOPTOTIC"
    NECROTIC = "NECROTIC"

# Set metadata after class creation
CellProliferationState._metadata = {
    "PROLIFERATING": {'description': 'Actively proliferating cells', 'meaning': 'GO:0008283'},
    "QUIESCENT": {'description': 'Quiescent cells (reversibly non-dividing)', 'meaning': 'GO:0044838', 'annotations': {'phase': 'G0', 'reversible': True}},
    "SENESCENT": {'description': 'Senescent cells (permanently non-dividing)', 'meaning': 'GO:0090398', 'annotations': {'reversible': False, 'markers': 'SA-β-gal, p16'}},
    "DIFFERENTIATED": {'description': 'Terminally differentiated cells', 'meaning': 'GO:0030154', 'annotations': {'examples': 'neurons, cardiomyocytes'}},
    "APOPTOTIC": {'description': 'Cells undergoing apoptosis', 'meaning': 'GO:0006915', 'annotations': {'aliases': 'programmed cell death'}},
    "NECROTIC": {'description': 'Cells undergoing necrosis', 'meaning': 'GO:0070265', 'annotations': {'type': 'uncontrolled cell death'}},
}

class DNADamageResponse(RichEnum):
    """
    DNA damage response pathways during cell cycle
    """
    # Enum members
    CELL_CYCLE_ARREST = "CELL_CYCLE_ARREST"
    DNA_REPAIR = "DNA_REPAIR"
    APOPTOSIS_INDUCTION = "APOPTOSIS_INDUCTION"
    SENESCENCE_INDUCTION = "SENESCENCE_INDUCTION"
    CHECKPOINT_ADAPTATION = "CHECKPOINT_ADAPTATION"

# Set metadata after class creation
DNADamageResponse._metadata = {
    "CELL_CYCLE_ARREST": {'description': 'Cell cycle arrest', 'meaning': 'GO:0007050'},
    "DNA_REPAIR": {'description': 'DNA repair', 'meaning': 'GO:0006281'},
    "APOPTOSIS_INDUCTION": {'description': 'Induction of apoptosis', 'meaning': 'GO:0006917'},
    "SENESCENCE_INDUCTION": {'description': 'Induction of senescence', 'meaning': 'GO:0090400'},
    "CHECKPOINT_ADAPTATION": {'description': 'Checkpoint adaptation', 'annotations': {'description': 'override of checkpoint despite damage'}},
}

class GenomeFeatureType(RichEnum):
    """
    Genome feature types from SOFA (Sequence Ontology Feature Annotation).
    This is the subset of Sequence Ontology terms used in GFF3 files.
    Organized hierarchically following the Sequence Ontology structure.
    """
    # Enum members
    REGION = "REGION"
    BIOLOGICAL_REGION = "BIOLOGICAL_REGION"
    GENE = "GENE"
    TRANSCRIPT = "TRANSCRIPT"
    PRIMARY_TRANSCRIPT = "PRIMARY_TRANSCRIPT"
    MRNA = "MRNA"
    EXON = "EXON"
    CDS = "CDS"
    INTRON = "INTRON"
    FIVE_PRIME_UTR = "FIVE_PRIME_UTR"
    THREE_PRIME_UTR = "THREE_PRIME_UTR"
    NCRNA = "NCRNA"
    RRNA = "RRNA"
    TRNA = "TRNA"
    SNRNA = "SNRNA"
    SNORNA = "SNORNA"
    MIRNA = "MIRNA"
    LNCRNA = "LNCRNA"
    RIBOZYME = "RIBOZYME"
    ANTISENSE_RNA = "ANTISENSE_RNA"
    PSEUDOGENE = "PSEUDOGENE"
    PROCESSED_PSEUDOGENE = "PROCESSED_PSEUDOGENE"
    REGULATORY_REGION = "REGULATORY_REGION"
    PROMOTER = "PROMOTER"
    ENHANCER = "ENHANCER"
    SILENCER = "SILENCER"
    TERMINATOR = "TERMINATOR"
    ATTENUATOR = "ATTENUATOR"
    POLYA_SIGNAL_SEQUENCE = "POLYA_SIGNAL_SEQUENCE"
    BINDING_SITE = "BINDING_SITE"
    TFBS = "TFBS"
    RIBOSOME_ENTRY_SITE = "RIBOSOME_ENTRY_SITE"
    POLYA_SITE = "POLYA_SITE"
    REPEAT_REGION = "REPEAT_REGION"
    DISPERSED_REPEAT = "DISPERSED_REPEAT"
    TANDEM_REPEAT = "TANDEM_REPEAT"
    INVERTED_REPEAT = "INVERTED_REPEAT"
    TRANSPOSABLE_ELEMENT = "TRANSPOSABLE_ELEMENT"
    MOBILE_ELEMENT = "MOBILE_ELEMENT"
    SEQUENCE_ALTERATION = "SEQUENCE_ALTERATION"
    INSERTION = "INSERTION"
    DELETION = "DELETION"
    INVERSION = "INVERSION"
    DUPLICATION = "DUPLICATION"
    SUBSTITUTION = "SUBSTITUTION"
    ORIGIN_OF_REPLICATION = "ORIGIN_OF_REPLICATION"
    POLYC_TRACT = "POLYC_TRACT"
    GAP = "GAP"
    ASSEMBLY_GAP = "ASSEMBLY_GAP"
    CHROMOSOME = "CHROMOSOME"
    SUPERCONTIG = "SUPERCONTIG"
    CONTIG = "CONTIG"
    SCAFFOLD = "SCAFFOLD"
    CLONE = "CLONE"
    PLASMID = "PLASMID"
    POLYPEPTIDE = "POLYPEPTIDE"
    MATURE_PROTEIN_REGION = "MATURE_PROTEIN_REGION"
    SIGNAL_PEPTIDE = "SIGNAL_PEPTIDE"
    TRANSIT_PEPTIDE = "TRANSIT_PEPTIDE"
    PROPEPTIDE = "PROPEPTIDE"
    OPERON = "OPERON"
    STEM_LOOP = "STEM_LOOP"
    D_LOOP = "D_LOOP"
    MATCH = "MATCH"
    CDNA_MATCH = "CDNA_MATCH"
    EST_MATCH = "EST_MATCH"
    PROTEIN_MATCH = "PROTEIN_MATCH"
    NUCLEOTIDE_MATCH = "NUCLEOTIDE_MATCH"
    JUNCTION_FEATURE = "JUNCTION_FEATURE"
    SPLICE_SITE = "SPLICE_SITE"
    FIVE_PRIME_SPLICE_SITE = "FIVE_PRIME_SPLICE_SITE"
    THREE_PRIME_SPLICE_SITE = "THREE_PRIME_SPLICE_SITE"
    START_CODON = "START_CODON"
    STOP_CODON = "STOP_CODON"
    CENTROMERE = "CENTROMERE"
    TELOMERE = "TELOMERE"

# Set metadata after class creation
GenomeFeatureType._metadata = {
    "REGION": {'description': 'A sequence feature with an extent greater than zero', 'meaning': 'SO:0000001'},
    "BIOLOGICAL_REGION": {'description': 'A region defined by its biological properties', 'meaning': 'SO:0001411'},
    "GENE": {'description': 'A region (or regions) that includes all of the sequence elements necessary to encode a functional transcript', 'meaning': 'SO:0000704'},
    "TRANSCRIPT": {'description': 'An RNA synthesized on a DNA or RNA template by an RNA polymerase', 'meaning': 'SO:0000673'},
    "PRIMARY_TRANSCRIPT": {'description': 'A transcript that has not been processed', 'meaning': 'SO:0000185'},
    "MRNA": {'description': "Messenger RNA; includes 5'UTR, coding sequences and 3'UTR", 'meaning': 'SO:0000234'},
    "EXON": {'description': 'A region of the transcript sequence within a gene which is not removed from the primary RNA transcript by RNA splicing', 'meaning': 'SO:0000147'},
    "CDS": {'description': 'Coding sequence; sequence of nucleotides that corresponds with the sequence of amino acids in a protein', 'meaning': 'SO:0000316'},
    "INTRON": {'description': 'A region of a primary transcript that is transcribed, but removed from within the transcript by splicing', 'meaning': 'SO:0000188'},
    "FIVE_PRIME_UTR": {'description': "5' untranslated region", 'meaning': 'SO:0000204'},
    "THREE_PRIME_UTR": {'description': "3' untranslated region", 'meaning': 'SO:0000205'},
    "NCRNA": {'description': 'Non-protein coding RNA', 'meaning': 'SO:0000655'},
    "RRNA": {'description': 'Ribosomal RNA', 'meaning': 'SO:0000252'},
    "TRNA": {'description': 'Transfer RNA', 'meaning': 'SO:0000253'},
    "SNRNA": {'description': 'Small nuclear RNA', 'meaning': 'SO:0000274'},
    "SNORNA": {'description': 'Small nucleolar RNA', 'meaning': 'SO:0000275'},
    "MIRNA": {'description': 'MicroRNA', 'meaning': 'SO:0000276'},
    "LNCRNA": {'description': 'Long non-coding RNA', 'meaning': 'SO:0001877'},
    "RIBOZYME": {'description': 'An RNA with catalytic activity', 'meaning': 'SO:0000374'},
    "ANTISENSE_RNA": {'description': 'RNA that is complementary to other RNA', 'meaning': 'SO:0000644'},
    "PSEUDOGENE": {'description': 'A sequence that closely resembles a known functional gene but does not produce a functional product', 'meaning': 'SO:0000336'},
    "PROCESSED_PSEUDOGENE": {'description': 'A pseudogene arising from reverse transcription of mRNA', 'meaning': 'SO:0000043'},
    "REGULATORY_REGION": {'description': 'A region involved in the control of the process of gene expression', 'meaning': 'SO:0005836'},
    "PROMOTER": {'description': 'A regulatory region initiating transcription', 'meaning': 'SO:0000167'},
    "ENHANCER": {'description': 'A cis-acting sequence that increases transcription', 'meaning': 'SO:0000165'},
    "SILENCER": {'description': 'A regulatory region which upon binding of transcription factors, suppresses transcription', 'meaning': 'SO:0000625'},
    "TERMINATOR": {'description': 'The sequence of DNA located either at the end of the transcript that causes RNA polymerase to terminate transcription', 'meaning': 'SO:0000141'},
    "ATTENUATOR": {'description': 'A sequence that causes transcription termination', 'meaning': 'SO:0000140'},
    "POLYA_SIGNAL_SEQUENCE": {'description': 'The recognition sequence for the cleavage and polyadenylation machinery', 'meaning': 'SO:0000551'},
    "BINDING_SITE": {'description': 'A region on a molecule that binds to another molecule', 'meaning': 'SO:0000409'},
    "TFBS": {'description': 'Transcription factor binding site', 'meaning': 'SO:0000235'},
    "RIBOSOME_ENTRY_SITE": {'description': 'Region where ribosome assembles on mRNA', 'meaning': 'SO:0000139'},
    "POLYA_SITE": {'description': 'Polyadenylation site', 'meaning': 'SO:0000553'},
    "REPEAT_REGION": {'description': 'A region of sequence containing one or more repeat units', 'meaning': 'SO:0000657'},
    "DISPERSED_REPEAT": {'description': 'A repeat that is interspersed in the genome', 'meaning': 'SO:0000658'},
    "TANDEM_REPEAT": {'description': 'A repeat where the same sequence is repeated in the same orientation', 'meaning': 'SO:0000705'},
    "INVERTED_REPEAT": {'description': 'A repeat where the sequence is repeated in the opposite orientation', 'meaning': 'SO:0000294'},
    "TRANSPOSABLE_ELEMENT": {'description': 'A DNA segment that can change its position within the genome', 'meaning': 'SO:0000101'},
    "MOBILE_ELEMENT": {'description': 'A nucleotide region with the ability to move from one place in the genome to another', 'meaning': 'SO:0001037'},
    "SEQUENCE_ALTERATION": {'description': 'A sequence that deviates from the reference sequence', 'meaning': 'SO:0001059'},
    "INSERTION": {'description': 'The sequence of one or more nucleotides added between two adjacent nucleotides', 'meaning': 'SO:0000667'},
    "DELETION": {'description': 'The removal of a sequences of nucleotides from the genome', 'meaning': 'SO:0000159'},
    "INVERSION": {'description': 'A continuous nucleotide sequence is inverted in the same position', 'meaning': 'SO:1000036'},
    "DUPLICATION": {'description': 'One or more nucleotides are added between two adjacent nucleotides', 'meaning': 'SO:1000035'},
    "SUBSTITUTION": {'description': 'A sequence alteration where one nucleotide replaced by another', 'meaning': 'SO:1000002'},
    "ORIGIN_OF_REPLICATION": {'description': 'The origin of replication; starting site for duplication of a nucleic acid molecule', 'meaning': 'SO:0000296'},
    "POLYC_TRACT": {'description': 'A sequence of Cs'},
    "GAP": {'description': 'A gap in the sequence', 'meaning': 'SO:0000730'},
    "ASSEMBLY_GAP": {'description': 'A gap between two sequences in an assembly', 'meaning': 'SO:0000730'},
    "CHROMOSOME": {'description': 'Structural unit composed of DNA and proteins', 'meaning': 'SO:0000340'},
    "SUPERCONTIG": {'description': 'One or more contigs that have been ordered and oriented using end-read information', 'meaning': 'SO:0000148'},
    "CONTIG": {'description': 'A contiguous sequence derived from sequence assembly', 'meaning': 'SO:0000149'},
    "SCAFFOLD": {'description': 'One or more contigs that have been ordered and oriented', 'meaning': 'SO:0000148'},
    "CLONE": {'description': 'A piece of DNA that has been inserted into a vector', 'meaning': 'SO:0000151'},
    "PLASMID": {'description': 'A self-replicating circular DNA molecule', 'meaning': 'SO:0000155'},
    "POLYPEPTIDE": {'description': 'A sequence of amino acids linked by peptide bonds', 'meaning': 'SO:0000104'},
    "MATURE_PROTEIN_REGION": {'description': 'The polypeptide sequence that remains after post-translational processing', 'meaning': 'SO:0000419'},
    "SIGNAL_PEPTIDE": {'description': 'A peptide region that targets a polypeptide to a specific location', 'meaning': 'SO:0000418'},
    "TRANSIT_PEPTIDE": {'description': 'A peptide that directs the transport of a protein to an organelle', 'meaning': 'SO:0000725'},
    "PROPEPTIDE": {'description': 'A peptide region that is cleaved during maturation', 'meaning': 'SO:0001062'},
    "OPERON": {'description': 'A group of contiguous genes transcribed as a single unit', 'meaning': 'SO:0000178'},
    "STEM_LOOP": {'description': 'A double-helical region formed by base-pairing between adjacent sequences', 'meaning': 'SO:0000313'},
    "D_LOOP": {'description': 'Displacement loop; a region where DNA is displaced by an invading strand', 'meaning': 'SO:0000297'},
    "MATCH": {'description': 'A region of sequence similarity', 'meaning': 'SO:0000343'},
    "CDNA_MATCH": {'description': 'A match to a cDNA sequence', 'meaning': 'SO:0000689'},
    "EST_MATCH": {'description': 'A match to an EST sequence', 'meaning': 'SO:0000668'},
    "PROTEIN_MATCH": {'description': 'A match to a protein sequence', 'meaning': 'SO:0000349'},
    "NUCLEOTIDE_MATCH": {'description': 'A match to a nucleotide sequence', 'meaning': 'SO:0000347'},
    "JUNCTION_FEATURE": {'description': 'A boundary or junction between sequence regions', 'meaning': 'SO:0000699'},
    "SPLICE_SITE": {'description': 'The position where intron is excised', 'meaning': 'SO:0000162'},
    "FIVE_PRIME_SPLICE_SITE": {'description': "The 5' splice site (donor site)", 'meaning': 'SO:0000163'},
    "THREE_PRIME_SPLICE_SITE": {'description': "The 3' splice site (acceptor site)", 'meaning': 'SO:0000164'},
    "START_CODON": {'description': 'The first codon to be translated', 'meaning': 'SO:0000318'},
    "STOP_CODON": {'description': 'The codon that terminates translation', 'meaning': 'SO:0000319'},
    "CENTROMERE": {'description': 'A region where chromatids are held together', 'meaning': 'SO:0000577'},
    "TELOMERE": {'description': 'The terminal region of a linear chromosome', 'meaning': 'SO:0000624'},
}

class SampleType(RichEnum):
    """
    Types of biological samples used in structural biology
    """
    # Enum members
    PROTEIN = "PROTEIN"
    NUCLEIC_ACID = "NUCLEIC_ACID"
    PROTEIN_COMPLEX = "PROTEIN_COMPLEX"
    MEMBRANE_PROTEIN = "MEMBRANE_PROTEIN"
    VIRUS = "VIRUS"
    ORGANELLE = "ORGANELLE"
    CELL = "CELL"
    TISSUE = "TISSUE"

# Set metadata after class creation
SampleType._metadata = {
    "PROTEIN": {'description': 'Purified protein sample'},
    "NUCLEIC_ACID": {'description': 'Nucleic acid sample (DNA or RNA)'},
    "PROTEIN_COMPLEX": {'description': 'Protein-protein or protein-nucleic acid complex'},
    "MEMBRANE_PROTEIN": {'description': 'Membrane-associated protein sample'},
    "VIRUS": {'description': 'Viral particle or capsid'},
    "ORGANELLE": {'description': 'Cellular organelle (mitochondria, chloroplast, etc.)'},
    "CELL": {'description': 'Whole cell sample'},
    "TISSUE": {'description': 'Tissue sample'},
}

class StructuralBiologyTechnique(RichEnum):
    """
    Structural biology experimental techniques
    """
    # Enum members
    CRYO_EM = "CRYO_EM"
    CRYO_ET = "CRYO_ET"
    X_RAY_CRYSTALLOGRAPHY = "X_RAY_CRYSTALLOGRAPHY"
    NEUTRON_CRYSTALLOGRAPHY = "NEUTRON_CRYSTALLOGRAPHY"
    SAXS = "SAXS"
    SANS = "SANS"
    WAXS = "WAXS"
    NMR = "NMR"
    MASS_SPECTROMETRY = "MASS_SPECTROMETRY"
    NEGATIVE_STAIN_EM = "NEGATIVE_STAIN_EM"

# Set metadata after class creation
StructuralBiologyTechnique._metadata = {
    "CRYO_EM": {'description': 'Cryo-electron microscopy', 'meaning': 'CHMO:0002413', 'annotations': {'resolution_range': '2-30 Å typical', 'aliases': 'cryoEM, electron cryo-microscopy'}},
    "CRYO_ET": {'description': 'Cryo-electron tomography', 'annotations': {'resolution_range': '20-100 Å typical', 'aliases': 'cryoET, electron cryo-tomography'}},
    "X_RAY_CRYSTALLOGRAPHY": {'description': 'X-ray crystallography', 'meaning': 'CHMO:0000159', 'annotations': {'resolution_range': '1-4 Å typical', 'aliases': 'XRC, macromolecular crystallography'}},
    "NEUTRON_CRYSTALLOGRAPHY": {'description': 'Neutron crystallography', 'annotations': {'advantages': 'hydrogen positions, deuteration studies'}},
    "SAXS": {'description': 'Small-angle X-ray scattering', 'meaning': 'CHMO:0000204', 'annotations': {'information': 'low-resolution structure, conformational changes'}},
    "SANS": {'description': 'Small-angle neutron scattering', 'annotations': {'advantages': 'contrast variation with deuteration'}},
    "WAXS": {'description': 'Wide-angle X-ray scattering'},
    "NMR": {'description': 'Nuclear magnetic resonance spectroscopy', 'meaning': 'CHMO:0000591', 'annotations': {'information': 'solution structure, dynamics'}},
    "MASS_SPECTROMETRY": {'description': 'Mass spectrometry', 'meaning': 'CHMO:0000470', 'annotations': {'applications': 'native MS, crosslinking, HDX'}},
    "NEGATIVE_STAIN_EM": {'description': 'Negative stain electron microscopy', 'annotations': {'resolution_range': '15-30 Å typical'}},
}

class CryoEMPreparationType(RichEnum):
    """
    Types of cryo-EM sample preparation
    """
    # Enum members
    VITREOUS_ICE = "VITREOUS_ICE"
    CRYO_SECTIONING = "CRYO_SECTIONING"
    FREEZE_SUBSTITUTION = "FREEZE_SUBSTITUTION"
    HIGH_PRESSURE_FREEZING = "HIGH_PRESSURE_FREEZING"

# Set metadata after class creation
CryoEMPreparationType._metadata = {
    "VITREOUS_ICE": {'description': 'Sample embedded in vitreous ice'},
    "CRYO_SECTIONING": {'description': 'Cryo-sectioned sample'},
    "FREEZE_SUBSTITUTION": {'description': 'Freeze-substituted sample'},
    "HIGH_PRESSURE_FREEZING": {'description': 'High-pressure frozen sample'},
}

class CryoEMGridType(RichEnum):
    """
    Types of electron microscopy grids
    """
    # Enum members
    C_FLAT = "C_FLAT"
    QUANTIFOIL = "QUANTIFOIL"
    LACEY_CARBON = "LACEY_CARBON"
    ULTRATHIN_CARBON = "ULTRATHIN_CARBON"
    GOLD_GRID = "GOLD_GRID"
    GRAPHENE_OXIDE = "GRAPHENE_OXIDE"

# Set metadata after class creation
CryoEMGridType._metadata = {
    "C_FLAT": {'description': 'C-flat holey carbon grid', 'annotations': {'hole_sizes': '1.2/1.3, 2/1, 2/2 μm common', 'manufacturer': 'Protochips'}},
    "QUANTIFOIL": {'description': 'Quantifoil holey carbon grid', 'annotations': {'hole_sizes': '1.2/1.3, 2/1, 2/2 μm common', 'manufacturer': 'Quantifoil'}},
    "LACEY_CARBON": {'description': 'Lacey carbon support film', 'annotations': {'structure': 'irregular holes, thin carbon film'}},
    "ULTRATHIN_CARBON": {'description': 'Ultrathin carbon film on holey support', 'annotations': {'thickness': '3-5 nm typical'}},
    "GOLD_GRID": {'description': 'Pure gold grid', 'annotations': {'advantages': 'inert, high-resolution imaging'}},
    "GRAPHENE_OXIDE": {'description': 'Graphene oxide support', 'annotations': {'advantages': 'atomically thin, good contrast'}},
}

class VitrificationMethod(RichEnum):
    """
    Methods for sample vitrification
    """
    # Enum members
    PLUNGE_FREEZING = "PLUNGE_FREEZING"
    HIGH_PRESSURE_FREEZING = "HIGH_PRESSURE_FREEZING"
    SLAM_FREEZING = "SLAM_FREEZING"
    SPRAY_FREEZING = "SPRAY_FREEZING"

# Set metadata after class creation
VitrificationMethod._metadata = {
    "PLUNGE_FREEZING": {'description': 'Plunge freezing in liquid ethane', 'annotations': {'temperature': '-180°C ethane', 'equipment': 'Vitrobot, Leica GP'}},
    "HIGH_PRESSURE_FREEZING": {'description': 'High pressure freezing', 'annotations': {'pressure': '2100 bar typical', 'advantages': 'thick samples, no ice crystals'}},
    "SLAM_FREEZING": {'description': 'Slam freezing against metal block', 'annotations': {'cooling_rate': '10,000 K/s'}},
    "SPRAY_FREEZING": {'description': 'Spray freezing into liquid nitrogen', 'annotations': {'applications': 'large samples, tissues'}},
}

class CrystallizationMethod(RichEnum):
    """
    Methods for protein crystallization
    """
    # Enum members
    VAPOR_DIFFUSION_HANGING = "VAPOR_DIFFUSION_HANGING"
    VAPOR_DIFFUSION_SITTING = "VAPOR_DIFFUSION_SITTING"
    MICROBATCH = "MICROBATCH"
    DIALYSIS = "DIALYSIS"
    FREE_INTERFACE_DIFFUSION = "FREE_INTERFACE_DIFFUSION"
    LCP = "LCP"

# Set metadata after class creation
CrystallizationMethod._metadata = {
    "VAPOR_DIFFUSION_HANGING": {'description': 'Vapor diffusion hanging drop method', 'annotations': {'volume': '2-10 μL drops typical', 'advantages': 'visual monitoring, easy optimization'}},
    "VAPOR_DIFFUSION_SITTING": {'description': 'Vapor diffusion sitting drop method', 'annotations': {'advantages': 'automated setup, stable drops'}},
    "MICROBATCH": {'description': 'Microbatch under oil method', 'annotations': {'oil_type': 'paraffin, silicone oil', 'advantages': 'prevents evaporation'}},
    "DIALYSIS": {'description': 'Dialysis crystallization', 'annotations': {'applications': 'large volume samples, gentle conditions'}},
    "FREE_INTERFACE_DIFFUSION": {'description': 'Free interface diffusion', 'annotations': {'setup': 'capillary tubes, gel interface'}},
    "LCP": {'description': 'Lipidic cubic phase crystallization', 'annotations': {'applications': 'membrane proteins', 'lipid': 'monoolein most common'}},
}

class XRaySource(RichEnum):
    """
    Types of X-ray sources
    """
    # Enum members
    SYNCHROTRON = "SYNCHROTRON"
    ROTATING_ANODE = "ROTATING_ANODE"
    MICROFOCUS = "MICROFOCUS"
    METAL_JET = "METAL_JET"

# Set metadata after class creation
XRaySource._metadata = {
    "SYNCHROTRON": {'description': 'Synchrotron radiation source', 'annotations': {'advantages': 'high intensity, tunable wavelength', 'brightness': '10^15-10^18 photons/s/mm²/mrad²'}},
    "ROTATING_ANODE": {'description': 'Rotating anode generator', 'annotations': {'power': '3-18 kW typical', 'target': 'copper, molybdenum common'}},
    "MICROFOCUS": {'description': 'Microfocus sealed tube', 'annotations': {'spot_size': '10-50 μm', 'applications': 'small crystals, in-house screening'}},
    "METAL_JET": {'description': 'Liquid metal jet source', 'annotations': {'advantages': 'higher power density, longer lifetime', 'metals': 'gallium, indium'}},
}

class Detector(RichEnum):
    """
    Types of detectors for structural biology
    """
    # Enum members
    DIRECT_ELECTRON = "DIRECT_ELECTRON"
    CCD = "CCD"
    CMOS = "CMOS"
    HYBRID_PIXEL = "HYBRID_PIXEL"
    PHOTOSTIMULABLE_PHOSPHOR = "PHOTOSTIMULABLE_PHOSPHOR"

# Set metadata after class creation
Detector._metadata = {
    "DIRECT_ELECTRON": {'description': 'Direct electron detector (DED)', 'annotations': {'examples': 'K2, K3, Falcon, DE-series', 'advantages': 'high DQE, fast readout'}},
    "CCD": {'description': 'Charge-coupled device camera', 'annotations': {'applications': 'legacy EM, some crystallography'}},
    "CMOS": {'description': 'Complementary metal-oxide semiconductor detector', 'annotations': {'advantages': 'fast readout, low noise'}},
    "HYBRID_PIXEL": {'description': 'Hybrid pixel detector', 'annotations': {'examples': 'Pilatus, Eiger', 'advantages': 'photon counting, zero noise'}},
    "PHOTOSTIMULABLE_PHOSPHOR": {'description': 'Photostimulable phosphor (image plate)', 'annotations': {'applications': 'legacy crystallography'}},
}

class WorkflowType(RichEnum):
    """
    Types of computational processing workflows
    """
    # Enum members
    MOTION_CORRECTION = "MOTION_CORRECTION"
    CTF_ESTIMATION = "CTF_ESTIMATION"
    PARTICLE_PICKING = "PARTICLE_PICKING"
    CLASSIFICATION_2D = "CLASSIFICATION_2D"
    CLASSIFICATION_3D = "CLASSIFICATION_3D"
    REFINEMENT_3D = "REFINEMENT_3D"
    MODEL_BUILDING = "MODEL_BUILDING"
    MODEL_REFINEMENT = "MODEL_REFINEMENT"
    PHASING = "PHASING"
    DATA_INTEGRATION = "DATA_INTEGRATION"
    DATA_SCALING = "DATA_SCALING"
    SAXS_ANALYSIS = "SAXS_ANALYSIS"

# Set metadata after class creation
WorkflowType._metadata = {
    "MOTION_CORRECTION": {'description': 'Motion correction for cryo-EM movies', 'annotations': {'software': 'MotionCorr, Unblur, RELION'}},
    "CTF_ESTIMATION": {'description': 'Contrast transfer function estimation', 'annotations': {'software': 'CTFFIND, Gctf, RELION'}},
    "PARTICLE_PICKING": {'description': 'Particle picking from micrographs', 'annotations': {'methods': 'template matching, deep learning', 'software': 'RELION, cryoSPARC, Topaz'}},
    "CLASSIFICATION_2D": {'description': '2D classification of particles', 'annotations': {'purpose': 'sorting, cleaning particle dataset'}},
    "CLASSIFICATION_3D": {'description': '3D classification of particles', 'annotations': {'purpose': 'conformational sorting, resolution improvement'}},
    "REFINEMENT_3D": {'description': '3D refinement of particle orientations', 'annotations': {'algorithms': 'expectation maximization, gradient descent'}},
    "MODEL_BUILDING": {'description': 'Atomic model building into density', 'annotations': {'software': 'Coot, ChimeraX, Isolde'}},
    "MODEL_REFINEMENT": {'description': 'Atomic model refinement', 'annotations': {'software': 'PHENIX, REFMAC, Buster'}},
    "PHASING": {'description': 'Phase determination for crystallography', 'annotations': {'methods': 'SAD, MAD, MR, MIR'}},
    "DATA_INTEGRATION": {'description': 'Integration of diffraction data', 'annotations': {'software': 'XDS, DIALS, HKL'}},
    "DATA_SCALING": {'description': 'Scaling and merging of diffraction data', 'annotations': {'software': 'SCALA, AIMLESS, XSCALE'}},
    "SAXS_ANALYSIS": {'description': 'SAXS data analysis and modeling', 'annotations': {'software': 'PRIMUS, CRYSOL, FoXS'}},
}

class FileFormat(RichEnum):
    """
    File formats used in structural biology
    """
    # Enum members
    MRC = "MRC"
    TIFF = "TIFF"
    HDF5 = "HDF5"
    STAR = "STAR"
    PDB = "PDB"
    MMCIF = "MMCIF"
    MTZ = "MTZ"
    CBF = "CBF"
    DM3 = "DM3"
    SER = "SER"

# Set metadata after class creation
FileFormat._metadata = {
    "MRC": {'description': 'MRC format for EM density maps', 'annotations': {'extension': '.mrc, .map', 'applications': 'EM volumes, tomograms'}},
    "TIFF": {'description': 'Tagged Image File Format', 'annotations': {'extension': '.tif, .tiff', 'applications': 'micrographs, general imaging'}},
    "HDF5": {'description': 'Hierarchical Data Format 5', 'annotations': {'extension': '.h5, .hdf5', 'applications': 'large datasets, metadata storage'}},
    "STAR": {'description': 'Self-defining Text Archival and Retrieval format', 'annotations': {'extension': '.star', 'applications': 'RELION metadata, particle parameters'}},
    "PDB": {'description': 'Protein Data Bank coordinate format', 'annotations': {'extension': '.pdb', 'applications': 'atomic coordinates, legacy format'}},
    "MMCIF": {'description': 'Macromolecular Crystallographic Information File', 'annotations': {'extension': '.cif', 'applications': 'atomic coordinates, modern PDB format'}},
    "MTZ": {'description': 'MTZ reflection data format', 'annotations': {'extension': '.mtz', 'applications': 'crystallographic reflections, phases'}},
    "CBF": {'description': 'Crystallographic Binary Format', 'annotations': {'extension': '.cbf', 'applications': 'detector images, diffraction data'}},
    "DM3": {'description': 'Digital Micrograph format', 'annotations': {'extension': '.dm3, .dm4', 'applications': 'FEI/Thermo Fisher EM data'}},
    "SER": {'description': 'FEI series format', 'annotations': {'extension': '.ser', 'applications': 'FEI movie stacks'}},
}

class DataType(RichEnum):
    """
    Types of structural biology data
    """
    # Enum members
    MICROGRAPH = "MICROGRAPH"
    MOVIE = "MOVIE"
    DIFFRACTION = "DIFFRACTION"
    SCATTERING = "SCATTERING"
    PARTICLES = "PARTICLES"
    VOLUME = "VOLUME"
    TOMOGRAM = "TOMOGRAM"
    MODEL = "MODEL"
    METADATA = "METADATA"

# Set metadata after class creation
DataType._metadata = {
    "MICROGRAPH": {'description': 'Electron micrograph image', 'annotations': {'typical_size': '4k x 4k pixels'}},
    "MOVIE": {'description': 'Movie stack of frames', 'annotations': {'applications': 'motion correction, dose fractionation'}},
    "DIFFRACTION": {'description': 'X-ray diffraction pattern', 'annotations': {'information': 'structure factors, crystal lattice'}},
    "SCATTERING": {'description': 'Small-angle scattering data', 'annotations': {'information': 'I(q) vs scattering vector'}},
    "PARTICLES": {'description': 'Particle stack for single particle analysis', 'annotations': {'format': 'boxed particles, aligned'}},
    "VOLUME": {'description': '3D electron density volume', 'annotations': {'applications': 'cryo-EM maps, crystallographic maps'}},
    "TOMOGRAM": {'description': '3D tomographic reconstruction', 'annotations': {'resolution': '5-50 Å typical'}},
    "MODEL": {'description': 'Atomic coordinate model', 'annotations': {'formats': 'PDB, mmCIF'}},
    "METADATA": {'description': 'Associated metadata file', 'annotations': {'formats': 'STAR, XML, JSON'}},
}

class ProcessingStatus(RichEnum):
    """
    Status of data processing workflows
    """
    # Enum members
    RAW = "RAW"
    PREPROCESSING = "PREPROCESSING"
    PROCESSING = "PROCESSING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    QUEUED = "QUEUED"
    PAUSED = "PAUSED"
    CANCELLED = "CANCELLED"

# Set metadata after class creation
ProcessingStatus._metadata = {
    "RAW": {'description': 'Raw unprocessed data'},
    "PREPROCESSING": {'description': 'Initial preprocessing in progress'},
    "PROCESSING": {'description': 'Main processing workflow running'},
    "COMPLETED": {'description': 'Processing completed successfully'},
    "FAILED": {'description': 'Processing failed with errors'},
    "QUEUED": {'description': 'Queued for processing'},
    "PAUSED": {'description': 'Processing paused by user'},
    "CANCELLED": {'description': 'Processing cancelled by user'},
}

class InsdcMissingValueEnum(RichEnum):
    """
    INSDC (International Nucleotide Sequence Database Collaboration) controlled vocabulary for missing values in sequence records
    """
    # Enum members
    NOT_APPLICABLE = "NOT_APPLICABLE"
    MISSING = "MISSING"
    NOT_COLLECTED = "NOT_COLLECTED"
    NOT_PROVIDED = "NOT_PROVIDED"
    RESTRICTED_ACCESS = "RESTRICTED_ACCESS"
    MISSING_CONTROL_SAMPLE = "MISSING_CONTROL_SAMPLE"
    MISSING_SAMPLE_GROUP = "MISSING_SAMPLE_GROUP"
    MISSING_SYNTHETIC_CONSTRUCT = "MISSING_SYNTHETIC_CONSTRUCT"
    MISSING_LAB_STOCK = "MISSING_LAB_STOCK"
    MISSING_THIRD_PARTY_DATA = "MISSING_THIRD_PARTY_DATA"
    MISSING_DATA_AGREEMENT_ESTABLISHED_PRE_2023 = "MISSING_DATA_AGREEMENT_ESTABLISHED_PRE_2023"
    MISSING_ENDANGERED_SPECIES = "MISSING_ENDANGERED_SPECIES"
    MISSING_HUMAN_IDENTIFIABLE = "MISSING_HUMAN_IDENTIFIABLE"

# Set metadata after class creation
InsdcMissingValueEnum._metadata = {
    "NOT_APPLICABLE": {'description': 'Information is inappropriate to report, can indicate that the standard itself fails to model or represent the information appropriately', 'meaning': 'NCIT:C48660'},
    "MISSING": {'description': 'Not stated explicitly or implied by any other means', 'meaning': 'NCIT:C54031'},
    "NOT_COLLECTED": {'description': 'Information of an expected format was not given because it has never been collected', 'meaning': 'NCIT:C142610', 'annotations': {'note': 'NCIT:C142610 represents Missing Data which encompasses data not collected'}},
    "NOT_PROVIDED": {'description': 'Information of an expected format was not given, a value may be given at the later stage', 'meaning': 'NCIT:C126101', 'annotations': {'note': 'Using NCIT:C126101 (Not Available) as a general term for data not provided'}},
    "RESTRICTED_ACCESS": {'description': 'Information exists but cannot be released openly because of privacy concerns', 'meaning': 'NCIT:C67110', 'annotations': {'note': 'NCIT:C67110 represents Data Not Releasable due to confidentiality'}},
    "MISSING_CONTROL_SAMPLE": {'description': 'Information is not applicable to control samples, negative control samples (e.g. blank sample or clear sample)', 'annotations': {'note': 'No specific ontology term found for missing control sample data'}},
    "MISSING_SAMPLE_GROUP": {'description': 'Information can not be provided for a sample group where a selection of samples is used to represent a species, location or some other attribute/metric', 'annotations': {'note': 'No specific ontology term found for missing sample group data'}},
    "MISSING_SYNTHETIC_CONSTRUCT": {'description': 'Information does not exist for a synthetic construct', 'annotations': {'note': 'No specific ontology term found for missing synthetic construct data'}},
    "MISSING_LAB_STOCK": {'description': 'Information is not collected for a lab stock and its cultivation, e.g. stock centers, culture collections, seed banks', 'annotations': {'note': 'No specific ontology term found for missing lab stock data'}},
    "MISSING_THIRD_PARTY_DATA": {'description': 'Information has not been revealed by another party', 'meaning': 'NCIT:C67329', 'annotations': {'note': 'NCIT:C67329 represents Source Data Not Available'}},
    "MISSING_DATA_AGREEMENT_ESTABLISHED_PRE_2023": {'description': 'Information can not be reported due to a data agreement established before metadata standards were introduced in 2023', 'annotations': {'note': 'No specific ontology term for data missing due to pre-2023 agreements'}},
    "MISSING_ENDANGERED_SPECIES": {'description': 'Information can not be reported due to endangered species concerns', 'annotations': {'note': 'No specific ontology term for data withheld due to endangered species'}},
    "MISSING_HUMAN_IDENTIFIABLE": {'description': 'Information can not be reported due to identifiable human data concerns', 'annotations': {'note': 'No specific ontology term for data withheld due to human identifiability'}},
}

class ViralGenomeTypeEnum(RichEnum):
    """
    Types of viral genomes based on Baltimore classification
    """
    # Enum members
    DNA = "DNA"
    DSDNA = "DSDNA"
    SSDNA = "SSDNA"
    RNA = "RNA"
    DSRNA = "DSRNA"
    SSRNA = "SSRNA"
    SSRNA_POSITIVE = "SSRNA_POSITIVE"
    SSRNA_NEGATIVE = "SSRNA_NEGATIVE"
    SSRNA_RT = "SSRNA_RT"
    DSDNA_RT = "DSDNA_RT"
    MIXED = "MIXED"
    UNCHARACTERIZED = "UNCHARACTERIZED"

# Set metadata after class creation
ViralGenomeTypeEnum._metadata = {
    "DNA": {'description': 'Viral genome composed of DNA', 'meaning': 'CHEBI:16991'},
    "DSDNA": {'description': 'Double-stranded DNA viral genome', 'meaning': 'NCIT:C14348', 'aliases': ['Baltimore Group I', 'Group I']},
    "SSDNA": {'description': 'Single-stranded DNA viral genome', 'meaning': 'NCIT:C14350', 'aliases': ['Baltimore Group II', 'Group II']},
    "RNA": {'description': 'Viral genome composed of RNA', 'meaning': 'CHEBI:33697'},
    "DSRNA": {'description': 'Double-stranded RNA viral genome', 'meaning': 'NCIT:C28518', 'aliases': ['Baltimore Group III', 'Group III']},
    "SSRNA": {'description': 'Single-stranded RNA viral genome', 'meaning': 'NCIT:C95939'},
    "SSRNA_POSITIVE": {'description': 'Positive-sense single-stranded RNA viral genome', 'meaning': 'NCIT:C14351', 'aliases': ['Baltimore Group IV', 'Group IV', '(+)ssRNA']},
    "SSRNA_NEGATIVE": {'description': 'Negative-sense single-stranded RNA viral genome', 'meaning': 'NCIT:C14346', 'aliases': ['Baltimore Group V', 'Group V', '(-)ssRNA']},
    "SSRNA_RT": {'description': 'Single-stranded RNA viruses that replicate through a DNA intermediate (retroviruses)', 'meaning': 'NCIT:C14347', 'aliases': ['Baltimore Group VI', 'Group VI', 'Retroviruses']},
    "DSDNA_RT": {'description': 'Double-stranded DNA viruses that replicate through a single-stranded RNA intermediate (pararetroviruses)', 'meaning': 'NCIT:C14349', 'aliases': ['Baltimore Group VII', 'Group VII', 'Pararetroviruses']},
    "MIXED": {'description': 'Mixed or hybrid viral genome type', 'meaning': 'NCIT:C128790'},
    "UNCHARACTERIZED": {'description': 'Viral genome type not yet characterized', 'meaning': 'NCIT:C17998'},
}

class PlantSexEnum(RichEnum):
    """
    Plant reproductive and sexual system types
    """
    # Enum members
    ANDRODIOECIOUS = "ANDRODIOECIOUS"
    ANDROECIOUS = "ANDROECIOUS"
    ANDROGYNOMONOECIOUS = "ANDROGYNOMONOECIOUS"
    ANDROGYNOUS = "ANDROGYNOUS"
    ANDROMONOECIOUS = "ANDROMONOECIOUS"
    BISEXUAL = "BISEXUAL"
    DICHOGAMOUS = "DICHOGAMOUS"
    DICLINOUS = "DICLINOUS"
    DIOECIOUS = "DIOECIOUS"
    GYNODIOECIOUS = "GYNODIOECIOUS"
    GYNOECIOUS = "GYNOECIOUS"
    GYNOMONOECIOUS = "GYNOMONOECIOUS"
    HERMAPHRODITIC = "HERMAPHRODITIC"
    IMPERFECT = "IMPERFECT"
    MONOCLINOUS = "MONOCLINOUS"
    MONOECIOUS = "MONOECIOUS"
    PERFECT = "PERFECT"
    POLYGAMODIOECIOUS = "POLYGAMODIOECIOUS"
    POLYGAMOMONOECIOUS = "POLYGAMOMONOECIOUS"
    POLYGAMOUS = "POLYGAMOUS"
    PROTANDROUS = "PROTANDROUS"
    PROTOGYNOUS = "PROTOGYNOUS"
    SUBANDROECIOUS = "SUBANDROECIOUS"
    SUBDIOECIOUS = "SUBDIOECIOUS"
    SUBGYNOECIOUS = "SUBGYNOECIOUS"
    SYNOECIOUS = "SYNOECIOUS"
    TRIMONOECIOUS = "TRIMONOECIOUS"
    TRIOECIOUS = "TRIOECIOUS"
    UNISEXUAL = "UNISEXUAL"

# Set metadata after class creation
PlantSexEnum._metadata = {
    "ANDRODIOECIOUS": {'description': 'Having male and hermaphrodite flowers on separate plants'},
    "ANDROECIOUS": {'description': 'Having only male flowers'},
    "ANDROGYNOMONOECIOUS": {'description': 'Having male, female, and hermaphrodite flowers on the same plant'},
    "ANDROGYNOUS": {'description': 'Having both male and female reproductive organs in the same flower'},
    "ANDROMONOECIOUS": {'description': 'Having male and hermaphrodite flowers on the same plant'},
    "BISEXUAL": {'description': 'Having both male and female reproductive organs'},
    "DICHOGAMOUS": {'description': 'Male and female organs mature at different times'},
    "DICLINOUS": {'description': 'Having male and female reproductive organs in separate flowers'},
    "DIOECIOUS": {'description': 'Having male and female flowers on separate plants', 'meaning': 'GSSO:011872'},
    "GYNODIOECIOUS": {'description': 'Having female and hermaphrodite flowers on separate plants'},
    "GYNOECIOUS": {'description': 'Having only female flowers'},
    "GYNOMONOECIOUS": {'description': 'Having female and hermaphrodite flowers on the same plant'},
    "HERMAPHRODITIC": {'description': 'Having both male and female reproductive organs', 'meaning': 'UBERON:0007197'},
    "IMPERFECT": {'description': 'Flower lacking either male or female reproductive organs'},
    "MONOCLINOUS": {'description': 'Having both male and female reproductive organs in the same flower'},
    "MONOECIOUS": {'description': 'Having male and female flowers on the same plant', 'meaning': 'GSSO:011868'},
    "PERFECT": {'description': 'Flower having both male and female reproductive organs'},
    "POLYGAMODIOECIOUS": {'description': 'Having male, female, and hermaphrodite flowers on separate plants'},
    "POLYGAMOMONOECIOUS": {'description': 'Having male, female, and hermaphrodite flowers on the same plant'},
    "POLYGAMOUS": {'description': 'Having male, female, and hermaphrodite flowers'},
    "PROTANDROUS": {'description': 'Male organs mature before female organs'},
    "PROTOGYNOUS": {'description': 'Female organs mature before male organs'},
    "SUBANDROECIOUS": {'description': 'Mostly male flowers with occasional hermaphrodite flowers'},
    "SUBDIOECIOUS": {'description': 'Mostly dioecious with occasional hermaphrodite flowers'},
    "SUBGYNOECIOUS": {'description': 'Mostly female flowers with occasional hermaphrodite flowers'},
    "SYNOECIOUS": {'description': 'Having male and female organs fused together'},
    "TRIMONOECIOUS": {'description': 'Having male, female, and hermaphrodite flowers on the same plant'},
    "TRIOECIOUS": {'description': 'Having male, female, and hermaphrodite flowers on separate plants'},
    "UNISEXUAL": {'description': 'Having only one sex of reproductive organs'},
}

class RelToOxygenEnum(RichEnum):
    """
    Organism's relationship to oxygen for growth and survival
    """
    # Enum members
    AEROBE = "AEROBE"
    ANAEROBE = "ANAEROBE"
    FACULTATIVE = "FACULTATIVE"
    MICROAEROPHILIC = "MICROAEROPHILIC"
    MICROANAEROBE = "MICROANAEROBE"
    OBLIGATE_AEROBE = "OBLIGATE_AEROBE"
    OBLIGATE_ANAEROBE = "OBLIGATE_ANAEROBE"

# Set metadata after class creation
RelToOxygenEnum._metadata = {
    "AEROBE": {'description': 'Organism that can survive and grow in an oxygenated environment', 'meaning': 'ECOCORE:00000173'},
    "ANAEROBE": {'description': 'Organism that does not require oxygen for growth', 'meaning': 'ECOCORE:00000172'},
    "FACULTATIVE": {'description': 'Organism that can grow with or without oxygen', 'meaning': 'ECOCORE:00000177', 'annotations': {'note': 'Maps to facultative anaerobe in ECOCORE'}},
    "MICROAEROPHILIC": {'description': 'Organism that requires oxygen at lower concentrations than atmospheric', 'meaning': 'MICRO:0000515'},
    "MICROANAEROBE": {'description': 'Organism that can tolerate very small amounts of oxygen'},
    "OBLIGATE_AEROBE": {'description': 'Organism that requires oxygen to grow', 'meaning': 'ECOCORE:00000179'},
    "OBLIGATE_ANAEROBE": {'description': 'Organism that cannot grow in the presence of oxygen', 'meaning': 'ECOCORE:00000178'},
}

class TrophicLevelEnum(RichEnum):
    """
    Trophic levels are the feeding position in a food chain
    """
    # Enum members
    AUTOTROPH = "AUTOTROPH"
    CARBOXYDOTROPH = "CARBOXYDOTROPH"
    CHEMOAUTOLITHOTROPH = "CHEMOAUTOLITHOTROPH"
    CHEMOAUTOTROPH = "CHEMOAUTOTROPH"
    CHEMOHETEROTROPH = "CHEMOHETEROTROPH"
    CHEMOLITHOAUTOTROPH = "CHEMOLITHOAUTOTROPH"
    CHEMOLITHOTROPH = "CHEMOLITHOTROPH"
    CHEMOORGANOHETEROTROPH = "CHEMOORGANOHETEROTROPH"
    CHEMOORGANOTROPH = "CHEMOORGANOTROPH"
    CHEMOSYNTHETIC = "CHEMOSYNTHETIC"
    CHEMOTROPH = "CHEMOTROPH"
    COPIOTROPH = "COPIOTROPH"
    DIAZOTROPH = "DIAZOTROPH"
    FACULTATIVE = "FACULTATIVE"
    HETEROTROPH = "HETEROTROPH"
    LITHOAUTOTROPH = "LITHOAUTOTROPH"
    LITHOHETEROTROPH = "LITHOHETEROTROPH"
    LITHOTROPH = "LITHOTROPH"
    METHANOTROPH = "METHANOTROPH"
    METHYLOTROPH = "METHYLOTROPH"
    MIXOTROPH = "MIXOTROPH"
    OBLIGATE = "OBLIGATE"
    OLIGOTROPH = "OLIGOTROPH"
    ORGANOHETEROTROPH = "ORGANOHETEROTROPH"
    ORGANOTROPH = "ORGANOTROPH"
    PHOTOAUTOTROPH = "PHOTOAUTOTROPH"
    PHOTOHETEROTROPH = "PHOTOHETEROTROPH"
    PHOTOLITHOAUTOTROPH = "PHOTOLITHOAUTOTROPH"
    PHOTOLITHOTROPH = "PHOTOLITHOTROPH"
    PHOTOSYNTHETIC = "PHOTOSYNTHETIC"
    PHOTOTROPH = "PHOTOTROPH"

# Set metadata after class creation
TrophicLevelEnum._metadata = {
    "AUTOTROPH": {'description': 'Organism capable of synthesizing its own food from inorganic substances', 'meaning': 'ECOCORE:00000023'},
    "CARBOXYDOTROPH": {'description': 'Organism that uses carbon monoxide as a source of carbon and energy'},
    "CHEMOAUTOLITHOTROPH": {'description': 'Autotroph that obtains energy from inorganic compounds'},
    "CHEMOAUTOTROPH": {'description': 'Organism that obtains energy by oxidizing inorganic compounds', 'meaning': 'ECOCORE:00000129'},
    "CHEMOHETEROTROPH": {'description': 'Organism that obtains energy from organic compounds', 'meaning': 'ECOCORE:00000132'},
    "CHEMOLITHOAUTOTROPH": {'description': 'Organism that uses inorganic compounds as electron donors'},
    "CHEMOLITHOTROPH": {'description': 'Organism that obtains energy from oxidation of inorganic compounds'},
    "CHEMOORGANOHETEROTROPH": {'description': 'Organism that uses organic compounds as both carbon and energy source'},
    "CHEMOORGANOTROPH": {'description': 'Organism that obtains energy from organic compounds', 'meaning': 'ECOCORE:00000133'},
    "CHEMOSYNTHETIC": {'description': 'Relating to organisms that produce organic matter through chemosynthesis'},
    "CHEMOTROPH": {'description': 'Organism that obtains energy from chemical compounds'},
    "COPIOTROPH": {'description': 'Organism that thrives in nutrient-rich environments'},
    "DIAZOTROPH": {'description': 'Organism capable of fixing atmospheric nitrogen'},
    "FACULTATIVE": {'description': 'Organism that can switch between different metabolic modes'},
    "HETEROTROPH": {'description': 'Organism that obtains carbon from organic compounds', 'meaning': 'ECOCORE:00000010'},
    "LITHOAUTOTROPH": {'description': 'Autotroph that uses inorganic compounds as electron donors'},
    "LITHOHETEROTROPH": {'description': 'Heterotroph that uses inorganic compounds as electron donors'},
    "LITHOTROPH": {'description': 'Organism that uses inorganic substrates as electron donors'},
    "METHANOTROPH": {'description': 'Organism that uses methane as carbon and energy source'},
    "METHYLOTROPH": {'description': 'Organism that uses single-carbon compounds'},
    "MIXOTROPH": {'description': 'Organism that can use both autotrophic and heterotrophic methods'},
    "OBLIGATE": {'description': 'Organism restricted to a particular metabolic mode'},
    "OLIGOTROPH": {'description': 'Organism that thrives in nutrient-poor environments', 'meaning': 'ECOCORE:00000138'},
    "ORGANOHETEROTROPH": {'description': 'Organism that uses organic compounds as carbon source'},
    "ORGANOTROPH": {'description': 'Organism that uses organic compounds as electron donors'},
    "PHOTOAUTOTROPH": {'description': 'Organism that uses light energy to synthesize organic compounds', 'meaning': 'ECOCORE:00000130'},
    "PHOTOHETEROTROPH": {'description': 'Organism that uses light for energy but organic compounds for carbon', 'meaning': 'ECOCORE:00000131'},
    "PHOTOLITHOAUTOTROPH": {'description': 'Photoautotroph that uses inorganic electron donors'},
    "PHOTOLITHOTROPH": {'description': 'Organism that uses light energy and inorganic electron donors'},
    "PHOTOSYNTHETIC": {'description': 'Relating to organisms that produce organic matter through photosynthesis'},
    "PHOTOTROPH": {'description': 'Organism that obtains energy from light'},
}

class DayOfWeek(RichEnum):
    """
    Days of the week following ISO 8601 standard (Monday = 1)
    """
    # Enum members
    MONDAY = "MONDAY"
    TUESDAY = "TUESDAY"
    WEDNESDAY = "WEDNESDAY"
    THURSDAY = "THURSDAY"
    FRIDAY = "FRIDAY"
    SATURDAY = "SATURDAY"
    SUNDAY = "SUNDAY"

# Set metadata after class creation
DayOfWeek._metadata = {
    "MONDAY": {'description': 'Monday (first day of week in ISO 8601)', 'meaning': 'TIME:Monday', 'annotations': {'iso_number': 1, 'abbreviation': 'Mon'}},
    "TUESDAY": {'description': 'Tuesday', 'meaning': 'TIME:Tuesday', 'annotations': {'iso_number': 2, 'abbreviation': 'Tue'}},
    "WEDNESDAY": {'description': 'Wednesday', 'meaning': 'TIME:Wednesday', 'annotations': {'iso_number': 3, 'abbreviation': 'Wed'}},
    "THURSDAY": {'description': 'Thursday', 'meaning': 'TIME:Thursday', 'annotations': {'iso_number': 4, 'abbreviation': 'Thu'}},
    "FRIDAY": {'description': 'Friday', 'meaning': 'TIME:Friday', 'annotations': {'iso_number': 5, 'abbreviation': 'Fri'}},
    "SATURDAY": {'description': 'Saturday', 'meaning': 'TIME:Saturday', 'annotations': {'iso_number': 6, 'abbreviation': 'Sat'}},
    "SUNDAY": {'description': 'Sunday (last day of week in ISO 8601)', 'meaning': 'TIME:Sunday', 'annotations': {'iso_number': 7, 'abbreviation': 'Sun'}},
}

class Month(RichEnum):
    """
    Months of the year
    """
    # Enum members
    JANUARY = "JANUARY"
    FEBRUARY = "FEBRUARY"
    MARCH = "MARCH"
    APRIL = "APRIL"
    MAY = "MAY"
    JUNE = "JUNE"
    JULY = "JULY"
    AUGUST = "AUGUST"
    SEPTEMBER = "SEPTEMBER"
    OCTOBER = "OCTOBER"
    NOVEMBER = "NOVEMBER"
    DECEMBER = "DECEMBER"

# Set metadata after class creation
Month._metadata = {
    "JANUARY": {'description': 'January', 'meaning': 'greg:January', 'annotations': {'month_number': 1, 'abbreviation': 'Jan', 'days': 31}},
    "FEBRUARY": {'description': 'February', 'meaning': 'greg:February', 'annotations': {'month_number': 2, 'abbreviation': 'Feb', 'days': '28/29'}},
    "MARCH": {'description': 'March', 'meaning': 'greg:March', 'annotations': {'month_number': 3, 'abbreviation': 'Mar', 'days': 31}},
    "APRIL": {'description': 'April', 'meaning': 'greg:April', 'annotations': {'month_number': 4, 'abbreviation': 'Apr', 'days': 30}},
    "MAY": {'description': 'May', 'meaning': 'greg:May', 'annotations': {'month_number': 5, 'abbreviation': 'May', 'days': 31}},
    "JUNE": {'description': 'June', 'meaning': 'greg:June', 'annotations': {'month_number': 6, 'abbreviation': 'Jun', 'days': 30}},
    "JULY": {'description': 'July', 'meaning': 'greg:July', 'annotations': {'month_number': 7, 'abbreviation': 'Jul', 'days': 31}},
    "AUGUST": {'description': 'August', 'meaning': 'greg:August', 'annotations': {'month_number': 8, 'abbreviation': 'Aug', 'days': 31}},
    "SEPTEMBER": {'description': 'September', 'meaning': 'greg:September', 'annotations': {'month_number': 9, 'abbreviation': 'Sep', 'days': 30}},
    "OCTOBER": {'description': 'October', 'meaning': 'greg:October', 'annotations': {'month_number': 10, 'abbreviation': 'Oct', 'days': 31}},
    "NOVEMBER": {'description': 'November', 'meaning': 'greg:November', 'annotations': {'month_number': 11, 'abbreviation': 'Nov', 'days': 30}},
    "DECEMBER": {'description': 'December', 'meaning': 'greg:December', 'annotations': {'month_number': 12, 'abbreviation': 'Dec', 'days': 31}},
}

class Quarter(RichEnum):
    """
    Calendar quarters
    """
    # Enum members
    Q1 = "Q1"
    Q2 = "Q2"
    Q3 = "Q3"
    Q4 = "Q4"

# Set metadata after class creation
Quarter._metadata = {
    "Q1": {'description': 'First quarter (January-March)', 'annotations': {'months': 'Jan-Mar'}},
    "Q2": {'description': 'Second quarter (April-June)', 'annotations': {'months': 'Apr-Jun'}},
    "Q3": {'description': 'Third quarter (July-September)', 'annotations': {'months': 'Jul-Sep'}},
    "Q4": {'description': 'Fourth quarter (October-December)', 'annotations': {'months': 'Oct-Dec'}},
}

class Season(RichEnum):
    """
    Seasons of the year (Northern Hemisphere)
    """
    # Enum members
    SPRING = "SPRING"
    SUMMER = "SUMMER"
    AUTUMN = "AUTUMN"
    WINTER = "WINTER"

# Set metadata after class creation
Season._metadata = {
    "SPRING": {'description': 'Spring season', 'meaning': 'NCIT:C94731', 'annotations': {'months': 'Mar-May', 'astronomical_start': '~Mar 20'}},
    "SUMMER": {'description': 'Summer season', 'meaning': 'NCIT:C94732', 'annotations': {'months': 'Jun-Aug', 'astronomical_start': '~Jun 21'}},
    "AUTUMN": {'description': 'Autumn/Fall season', 'meaning': 'NCIT:C94733', 'annotations': {'months': 'Sep-Nov', 'astronomical_start': '~Sep 22', 'aliases': 'Fall'}},
    "WINTER": {'description': 'Winter season', 'meaning': 'NCIT:C94730', 'annotations': {'months': 'Dec-Feb', 'astronomical_start': '~Dec 21'}},
}

class TimePeriod(RichEnum):
    """
    Common time periods and intervals
    """
    # Enum members
    HOURLY = "HOURLY"
    DAILY = "DAILY"
    WEEKLY = "WEEKLY"
    BIWEEKLY = "BIWEEKLY"
    MONTHLY = "MONTHLY"
    QUARTERLY = "QUARTERLY"
    SEMIANNUALLY = "SEMIANNUALLY"
    ANNUALLY = "ANNUALLY"
    BIANNUALLY = "BIANNUALLY"

# Set metadata after class creation
TimePeriod._metadata = {
    "HOURLY": {'description': 'Every hour', 'annotations': {'ucum': 'h'}},
    "DAILY": {'description': 'Every day', 'annotations': {'ucum': 'd'}},
    "WEEKLY": {'description': 'Every week', 'annotations': {'ucum': 'wk'}},
    "BIWEEKLY": {'description': 'Every two weeks', 'annotations': {'ucum': '2.wk'}},
    "MONTHLY": {'description': 'Every month', 'annotations': {'ucum': 'mo'}},
    "QUARTERLY": {'description': 'Every quarter (3 months)', 'annotations': {'ucum': '3.mo'}},
    "SEMIANNUALLY": {'description': 'Every six months', 'annotations': {'ucum': '6.mo'}},
    "ANNUALLY": {'description': 'Every year', 'annotations': {'ucum': 'a'}},
    "BIANNUALLY": {'description': 'Every two years', 'annotations': {'ucum': '2.a'}},
}

class TimeUnit(RichEnum):
    """
    Units of time measurement
    """
    # Enum members
    NANOSECOND = "NANOSECOND"
    MICROSECOND = "MICROSECOND"
    MILLISECOND = "MILLISECOND"
    SECOND = "SECOND"
    MINUTE = "MINUTE"
    HOUR = "HOUR"
    DAY = "DAY"
    WEEK = "WEEK"
    MONTH = "MONTH"
    YEAR = "YEAR"
    DECADE = "DECADE"
    CENTURY = "CENTURY"
    MILLENNIUM = "MILLENNIUM"

# Set metadata after class creation
TimeUnit._metadata = {
    "NANOSECOND": {'description': 'Nanosecond (10^-9 seconds)', 'annotations': {'symbol': 'ns', 'ucum': 'ns', 'seconds': '1e-9'}},
    "MICROSECOND": {'description': 'Microsecond (10^-6 seconds)', 'annotations': {'symbol': 'μs', 'ucum': 'us', 'seconds': '1e-6'}},
    "MILLISECOND": {'description': 'Millisecond (10^-3 seconds)', 'annotations': {'symbol': 'ms', 'ucum': 'ms', 'seconds': 0.001}},
    "SECOND": {'description': 'Second (SI base unit)', 'meaning': 'TIME:unitSecond', 'annotations': {'symbol': 's', 'ucum': 's', 'seconds': 1}},
    "MINUTE": {'description': 'Minute (60 seconds)', 'meaning': 'TIME:unitMinute', 'annotations': {'symbol': 'min', 'ucum': 'min', 'seconds': 60}},
    "HOUR": {'description': 'Hour (60 minutes)', 'meaning': 'TIME:unitHour', 'annotations': {'symbol': 'h', 'ucum': 'h', 'seconds': 3600}},
    "DAY": {'description': 'Day (24 hours)', 'meaning': 'TIME:unitDay', 'annotations': {'symbol': 'd', 'ucum': 'd', 'seconds': 86400}},
    "WEEK": {'description': 'Week (7 days)', 'meaning': 'TIME:unitWeek', 'annotations': {'symbol': 'wk', 'ucum': 'wk', 'seconds': 604800}},
    "MONTH": {'description': 'Month (approximately 30.44 days)', 'meaning': 'TIME:unitMonth', 'annotations': {'symbol': 'mo', 'ucum': 'mo', 'seconds': '~2629800'}},
    "YEAR": {'description': 'Year (365.25 days)', 'meaning': 'TIME:unitYear', 'annotations': {'symbol': 'yr', 'ucum': 'a', 'seconds': 31557600}},
    "DECADE": {'description': 'Decade (10 years)', 'meaning': 'TIME:unitDecade', 'annotations': {'ucum': '10.a', 'years': 10}},
    "CENTURY": {'description': 'Century (100 years)', 'meaning': 'TIME:unitCentury', 'annotations': {'ucum': '100.a', 'years': 100}},
    "MILLENNIUM": {'description': 'Millennium (1000 years)', 'meaning': 'TIME:unitMillennium', 'annotations': {'ucum': '1000.a', 'years': 1000}},
}

class TimeOfDay(RichEnum):
    """
    Common times of day
    """
    # Enum members
    DAWN = "DAWN"
    MORNING = "MORNING"
    NOON = "NOON"
    AFTERNOON = "AFTERNOON"
    EVENING = "EVENING"
    NIGHT = "NIGHT"
    MIDNIGHT = "MIDNIGHT"

# Set metadata after class creation
TimeOfDay._metadata = {
    "DAWN": {'description': 'Dawn (first light)', 'annotations': {'typical_time': '05:00-06:00'}},
    "MORNING": {'description': 'Morning', 'annotations': {'typical_time': '06:00-12:00'}},
    "NOON": {'description': 'Noon/Midday', 'annotations': {'typical_time': 720}},
    "AFTERNOON": {'description': 'Afternoon', 'annotations': {'typical_time': '12:00-18:00'}},
    "EVENING": {'description': 'Evening', 'annotations': {'typical_time': '18:00-21:00'}},
    "NIGHT": {'description': 'Night', 'annotations': {'typical_time': '21:00-05:00'}},
    "MIDNIGHT": {'description': 'Midnight', 'annotations': {'typical_time': '00:00'}},
}

class BusinessTimeFrame(RichEnum):
    """
    Common business and financial time frames
    """
    # Enum members
    REAL_TIME = "REAL_TIME"
    INTRADAY = "INTRADAY"
    T_PLUS_1 = "T_PLUS_1"
    T_PLUS_2 = "T_PLUS_2"
    T_PLUS_3 = "T_PLUS_3"
    END_OF_DAY = "END_OF_DAY"
    END_OF_WEEK = "END_OF_WEEK"
    END_OF_MONTH = "END_OF_MONTH"
    END_OF_QUARTER = "END_OF_QUARTER"
    END_OF_YEAR = "END_OF_YEAR"
    YEAR_TO_DATE = "YEAR_TO_DATE"
    MONTH_TO_DATE = "MONTH_TO_DATE"
    QUARTER_TO_DATE = "QUARTER_TO_DATE"

# Set metadata after class creation
BusinessTimeFrame._metadata = {
    "REAL_TIME": {'description': 'Real-time/instantaneous'},
    "INTRADAY": {'description': 'Within the same day'},
    "T_PLUS_1": {'description': 'Trade date plus one business day', 'annotations': {'abbreviation': 'T+1'}},
    "T_PLUS_2": {'description': 'Trade date plus two business days', 'annotations': {'abbreviation': 'T+2'}},
    "T_PLUS_3": {'description': 'Trade date plus three business days', 'annotations': {'abbreviation': 'T+3'}},
    "END_OF_DAY": {'description': 'End of business day', 'annotations': {'abbreviation': 'EOD'}},
    "END_OF_WEEK": {'description': 'End of business week', 'annotations': {'abbreviation': 'EOW'}},
    "END_OF_MONTH": {'description': 'End of calendar month', 'annotations': {'abbreviation': 'EOM'}},
    "END_OF_QUARTER": {'description': 'End of calendar quarter', 'annotations': {'abbreviation': 'EOQ'}},
    "END_OF_YEAR": {'description': 'End of calendar year', 'annotations': {'abbreviation': 'EOY'}},
    "YEAR_TO_DATE": {'description': 'From beginning of year to current date', 'annotations': {'abbreviation': 'YTD'}},
    "MONTH_TO_DATE": {'description': 'From beginning of month to current date', 'annotations': {'abbreviation': 'MTD'}},
    "QUARTER_TO_DATE": {'description': 'From beginning of quarter to current date', 'annotations': {'abbreviation': 'QTD'}},
}

class GeologicalEra(RichEnum):
    """
    Major geological eras
    """
    # Enum members
    PRECAMBRIAN = "PRECAMBRIAN"
    PALEOZOIC = "PALEOZOIC"
    MESOZOIC = "MESOZOIC"
    CENOZOIC = "CENOZOIC"

# Set metadata after class creation
GeologicalEra._metadata = {
    "PRECAMBRIAN": {'description': 'Precambrian (4.6 billion - 541 million years ago)'},
    "PALEOZOIC": {'description': 'Paleozoic Era (541 - 252 million years ago)'},
    "MESOZOIC": {'description': 'Mesozoic Era (252 - 66 million years ago)'},
    "CENOZOIC": {'description': 'Cenozoic Era (66 million years ago - present)'},
}

class HistoricalPeriod(RichEnum):
    """
    Major historical periods
    """
    # Enum members
    PREHISTORIC = "PREHISTORIC"
    ANCIENT = "ANCIENT"
    CLASSICAL_ANTIQUITY = "CLASSICAL_ANTIQUITY"
    MIDDLE_AGES = "MIDDLE_AGES"
    RENAISSANCE = "RENAISSANCE"
    EARLY_MODERN = "EARLY_MODERN"
    INDUSTRIAL_AGE = "INDUSTRIAL_AGE"
    MODERN = "MODERN"
    CONTEMPORARY = "CONTEMPORARY"
    DIGITAL_AGE = "DIGITAL_AGE"

# Set metadata after class creation
HistoricalPeriod._metadata = {
    "PREHISTORIC": {'description': 'Before written records'},
    "ANCIENT": {'description': 'Ancient history (3000 BCE - 500 CE)'},
    "CLASSICAL_ANTIQUITY": {'description': 'Classical antiquity (8th century BCE - 6th century CE)'},
    "MIDDLE_AGES": {'description': 'Middle Ages (5th - 15th century)'},
    "RENAISSANCE": {'description': 'Renaissance (14th - 17th century)'},
    "EARLY_MODERN": {'description': 'Early modern period (15th - 18th century)'},
    "INDUSTRIAL_AGE": {'description': 'Industrial age (1760 - 1840)'},
    "MODERN": {'description': 'Modern era (19th century - mid 20th century)'},
    "CONTEMPORARY": {'description': 'Contemporary period (mid 20th century - present)'},
    "DIGITAL_AGE": {'description': 'Digital/Information age (1950s - present)'},
}

class PublicationType(RichEnum):
    """
    Types of academic and research publications
    """
    # Enum members
    JOURNAL_ARTICLE = "JOURNAL_ARTICLE"
    REVIEW_ARTICLE = "REVIEW_ARTICLE"
    RESEARCH_ARTICLE = "RESEARCH_ARTICLE"
    SHORT_COMMUNICATION = "SHORT_COMMUNICATION"
    EDITORIAL = "EDITORIAL"
    LETTER = "LETTER"
    COMMENTARY = "COMMENTARY"
    PERSPECTIVE = "PERSPECTIVE"
    CASE_REPORT = "CASE_REPORT"
    TECHNICAL_NOTE = "TECHNICAL_NOTE"
    BOOK = "BOOK"
    BOOK_CHAPTER = "BOOK_CHAPTER"
    EDITED_BOOK = "EDITED_BOOK"
    REFERENCE_BOOK = "REFERENCE_BOOK"
    TEXTBOOK = "TEXTBOOK"
    CONFERENCE_PAPER = "CONFERENCE_PAPER"
    CONFERENCE_ABSTRACT = "CONFERENCE_ABSTRACT"
    CONFERENCE_POSTER = "CONFERENCE_POSTER"
    CONFERENCE_PROCEEDINGS = "CONFERENCE_PROCEEDINGS"
    PHD_THESIS = "PHD_THESIS"
    MASTERS_THESIS = "MASTERS_THESIS"
    BACHELORS_THESIS = "BACHELORS_THESIS"
    TECHNICAL_REPORT = "TECHNICAL_REPORT"
    WORKING_PAPER = "WORKING_PAPER"
    WHITE_PAPER = "WHITE_PAPER"
    POLICY_BRIEF = "POLICY_BRIEF"
    DATASET = "DATASET"
    SOFTWARE = "SOFTWARE"
    DATA_PAPER = "DATA_PAPER"
    SOFTWARE_PAPER = "SOFTWARE_PAPER"
    PROTOCOL = "PROTOCOL"
    PREPRINT = "PREPRINT"
    POSTPRINT = "POSTPRINT"
    PUBLISHED_VERSION = "PUBLISHED_VERSION"
    PATENT = "PATENT"
    STANDARD = "STANDARD"
    BLOG_POST = "BLOG_POST"
    PRESENTATION = "PRESENTATION"
    LECTURE = "LECTURE"
    ANNOTATION = "ANNOTATION"

# Set metadata after class creation
PublicationType._metadata = {
    "JOURNAL_ARTICLE": {'description': 'Peer-reviewed journal article', 'meaning': 'FABIO:JournalArticle'},
    "REVIEW_ARTICLE": {'description': 'Review article synthesizing existing research', 'meaning': 'FABIO:ReviewArticle'},
    "RESEARCH_ARTICLE": {'description': 'Original research article', 'meaning': 'FABIO:ResearchPaper'},
    "SHORT_COMMUNICATION": {'description': 'Brief communication or short report', 'meaning': 'FABIO:BriefCommunication'},
    "EDITORIAL": {'description': 'Editorial or opinion piece', 'meaning': 'FABIO:Editorial'},
    "LETTER": {'description': 'Letter to the editor', 'meaning': 'FABIO:Letter'},
    "COMMENTARY": {'description': 'Commentary on existing work', 'meaning': 'FABIO:Comment'},
    "PERSPECTIVE": {'description': 'Perspective or viewpoint article', 'meaning': 'FABIO:Comment'},
    "CASE_REPORT": {'description': 'Clinical or scientific case report', 'meaning': 'FABIO:CaseReport'},
    "TECHNICAL_NOTE": {'description': 'Technical or methodological note', 'meaning': 'FABIO:BriefCommunication'},
    "BOOK": {'description': 'Complete book or monograph', 'meaning': 'FABIO:Book'},
    "BOOK_CHAPTER": {'description': 'Chapter in an edited book', 'meaning': 'FABIO:BookChapter'},
    "EDITED_BOOK": {'description': 'Edited collection or anthology', 'meaning': 'FABIO:EditedBook'},
    "REFERENCE_BOOK": {'description': 'Reference work or encyclopedia', 'meaning': 'FABIO:ReferenceBook'},
    "TEXTBOOK": {'description': 'Educational textbook', 'meaning': 'FABIO:Textbook'},
    "CONFERENCE_PAPER": {'description': 'Full conference paper', 'meaning': 'FABIO:ConferencePaper'},
    "CONFERENCE_ABSTRACT": {'description': 'Conference abstract', 'meaning': 'FABIO:ConferenceAbstract'},
    "CONFERENCE_POSTER": {'description': 'Conference poster', 'meaning': 'FABIO:ConferencePoster'},
    "CONFERENCE_PROCEEDINGS": {'description': 'Complete conference proceedings', 'meaning': 'FABIO:ConferenceProceedings'},
    "PHD_THESIS": {'description': 'Doctoral dissertation', 'meaning': 'FABIO:DoctoralThesis'},
    "MASTERS_THESIS": {'description': "Master's thesis", 'meaning': 'FABIO:MastersThesis'},
    "BACHELORS_THESIS": {'description': "Bachelor's or undergraduate thesis", 'meaning': 'FABIO:BachelorsThesis'},
    "TECHNICAL_REPORT": {'description': 'Technical or research report', 'meaning': 'FABIO:TechnicalReport'},
    "WORKING_PAPER": {'description': 'Working paper or discussion paper', 'meaning': 'FABIO:WorkingPaper'},
    "WHITE_PAPER": {'description': 'White paper or position paper', 'meaning': 'FABIO:WhitePaper'},
    "POLICY_BRIEF": {'description': 'Policy brief or recommendation', 'meaning': 'FABIO:PolicyBrief'},
    "DATASET": {'description': 'Research dataset', 'meaning': 'DCMITYPE:Dataset'},
    "SOFTWARE": {'description': 'Research software or code', 'meaning': 'DCMITYPE:Software'},
    "DATA_PAPER": {'description': 'Data descriptor or data paper', 'meaning': 'FABIO:DataPaper'},
    "SOFTWARE_PAPER": {'description': 'Software or tools paper', 'meaning': 'FABIO:ResearchPaper'},
    "PROTOCOL": {'description': 'Research protocol or methodology', 'meaning': 'FABIO:Protocol'},
    "PREPRINT": {'description': 'Preprint or unrefereed manuscript', 'meaning': 'FABIO:Preprint'},
    "POSTPRINT": {'description': 'Accepted manuscript after peer review', 'meaning': 'FABIO:Preprint'},
    "PUBLISHED_VERSION": {'description': 'Final published version', 'meaning': 'IAO:0000311'},
    "PATENT": {'description': 'Patent or patent application', 'meaning': 'FABIO:Patent'},
    "STANDARD": {'description': 'Technical standard or specification', 'meaning': 'FABIO:Standard'},
    "BLOG_POST": {'description': 'Academic blog post', 'meaning': 'FABIO:BlogPost'},
    "PRESENTATION": {'description': 'Presentation slides or talk', 'meaning': 'FABIO:Presentation'},
    "LECTURE": {'description': 'Lecture or educational material', 'meaning': 'FABIO:Presentation'},
    "ANNOTATION": {'description': 'Annotation or scholarly note', 'meaning': 'FABIO:Annotation'},
}

class PeerReviewStatus(RichEnum):
    """
    Status of peer review process
    """
    # Enum members
    NOT_PEER_REVIEWED = "NOT_PEER_REVIEWED"
    SUBMITTED = "SUBMITTED"
    UNDER_REVIEW = "UNDER_REVIEW"
    REVIEW_COMPLETE = "REVIEW_COMPLETE"
    MAJOR_REVISION = "MAJOR_REVISION"
    MINOR_REVISION = "MINOR_REVISION"
    ACCEPTED = "ACCEPTED"
    ACCEPTED_WITH_REVISIONS = "ACCEPTED_WITH_REVISIONS"
    REJECTED = "REJECTED"
    WITHDRAWN = "WITHDRAWN"
    PUBLISHED = "PUBLISHED"

# Set metadata after class creation
PeerReviewStatus._metadata = {
    "NOT_PEER_REVIEWED": {'description': 'Not peer reviewed'},
    "SUBMITTED": {'description': 'Submitted for review'},
    "UNDER_REVIEW": {'description': 'Currently under peer review', 'meaning': 'SIO:000035'},
    "REVIEW_COMPLETE": {'description': 'Peer review complete', 'meaning': 'SIO:000034'},
    "MAJOR_REVISION": {'description': 'Major revisions requested'},
    "MINOR_REVISION": {'description': 'Minor revisions requested'},
    "ACCEPTED": {'description': 'Accepted for publication'},
    "ACCEPTED_WITH_REVISIONS": {'description': 'Conditionally accepted pending revisions'},
    "REJECTED": {'description': 'Rejected after review'},
    "WITHDRAWN": {'description': 'Withdrawn by authors'},
    "PUBLISHED": {'description': 'Published after review', 'meaning': 'IAO:0000311'},
}

class AcademicDegree(RichEnum):
    """
    Academic degrees and qualifications
    """
    # Enum members
    BA = "BA"
    BS = "BS"
    BSC = "BSC"
    BENG = "BENG"
    BFA = "BFA"
    LLB = "LLB"
    MBBS = "MBBS"
    MA = "MA"
    MS = "MS"
    MSC = "MSC"
    MBA = "MBA"
    MFA = "MFA"
    MPH = "MPH"
    MENG = "MENG"
    MED = "MED"
    LLM = "LLM"
    MPHIL = "MPHIL"
    PHD = "PHD"
    MD = "MD"
    JD = "JD"
    EDD = "EDD"
    PSYD = "PSYD"
    DBA = "DBA"
    DPHIL = "DPHIL"
    SCD = "SCD"
    POSTDOC = "POSTDOC"

# Set metadata after class creation
AcademicDegree._metadata = {
    "BA": {'meaning': 'NCIT:C71345', 'annotations': {'level': 'undergraduate'}},
    "BS": {'description': 'Bachelor of Science', 'meaning': 'NCIT:C71351', 'annotations': {'level': 'undergraduate'}, 'aliases': ['Bachelor of Science']},
    "BSC": {'description': 'Bachelor of Science (British)', 'meaning': 'NCIT:C71351', 'annotations': {'level': 'undergraduate'}, 'aliases': ['Bachelor of Science']},
    "BENG": {'description': 'Bachelor of Engineering', 'meaning': 'NCIT:C71347', 'annotations': {'level': 'undergraduate'}, 'aliases': ['Bachelor of Engineering']},
    "BFA": {'description': 'Bachelor of Fine Arts', 'meaning': 'NCIT:C71349', 'annotations': {'level': 'undergraduate'}, 'aliases': ['Bachelor of Fine Arts']},
    "LLB": {'description': 'Bachelor of Laws', 'meaning': 'NCIT:C71352', 'annotations': {'level': 'undergraduate'}, 'aliases': ['Bachelor of Science in Law']},
    "MBBS": {'description': 'Bachelor of Medicine, Bachelor of Surgery', 'meaning': 'NCIT:C39383', 'annotations': {'level': 'undergraduate'}, 'aliases': ['Doctor of Medicine']},
    "MA": {'description': 'Master of Arts', 'meaning': 'NCIT:C71364', 'annotations': {'level': 'graduate'}, 'aliases': ['Master of Arts']},
    "MS": {'description': 'Master of Science', 'meaning': 'NCIT:C39452', 'annotations': {'level': 'graduate'}, 'aliases': ['Master of Science']},
    "MSC": {'description': 'Master of Science (British)', 'meaning': 'NCIT:C39452', 'annotations': {'level': 'graduate'}, 'aliases': ['Master of Science']},
    "MBA": {'description': 'Master of Business Administration', 'meaning': 'NCIT:C39449', 'annotations': {'level': 'graduate'}, 'aliases': ['Master of Business Administration']},
    "MFA": {'description': 'Master of Fine Arts', 'annotations': {'level': 'graduate'}},
    "MPH": {'description': 'Master of Public Health', 'meaning': 'NCIT:C39451', 'annotations': {'level': 'graduate'}, 'aliases': ['Master of Public Health']},
    "MENG": {'description': 'Master of Engineering', 'meaning': 'NCIT:C71368', 'annotations': {'level': 'graduate'}, 'aliases': ['Master of Engineering']},
    "MED": {'description': 'Master of Education', 'meaning': 'NCIT:C71369', 'annotations': {'level': 'graduate'}, 'aliases': ['Master of Education']},
    "LLM": {'description': 'Master of Laws', 'meaning': 'NCIT:C71363', 'annotations': {'level': 'graduate'}, 'aliases': ['Master of Law']},
    "MPHIL": {'description': 'Master of Philosophy', 'annotations': {'level': 'graduate'}},
    "PHD": {'description': 'Doctor of Philosophy', 'meaning': 'NCIT:C39387', 'annotations': {'level': 'doctoral'}, 'aliases': ['Doctor of Philosophy']},
    "MD": {'description': 'Doctor of Medicine', 'meaning': 'NCIT:C39383', 'annotations': {'level': 'doctoral'}, 'aliases': ['Doctor of Medicine']},
    "JD": {'description': 'Juris Doctor', 'meaning': 'NCIT:C71361', 'annotations': {'level': 'doctoral'}, 'aliases': ['Doctor of Law']},
    "EDD": {'description': 'Doctor of Education', 'meaning': 'NCIT:C71359', 'annotations': {'level': 'doctoral'}, 'aliases': ['Doctor of Education']},
    "PSYD": {'description': 'Doctor of Psychology', 'annotations': {'level': 'doctoral'}},
    "DBA": {'description': 'Doctor of Business Administration', 'annotations': {'level': 'doctoral'}},
    "DPHIL": {'description': 'Doctor of Philosophy (Oxford/Sussex)', 'meaning': 'NCIT:C39387', 'annotations': {'level': 'doctoral'}, 'aliases': ['Doctor of Philosophy']},
    "SCD": {'description': 'Doctor of Science', 'meaning': 'NCIT:C71379', 'annotations': {'level': 'doctoral'}, 'aliases': ['Doctor of Science']},
    "POSTDOC": {'description': 'Postdoctoral researcher', 'annotations': {'level': 'postdoctoral'}},
}

class LicenseType(RichEnum):
    """
    Common software and content licenses
    """
    # Enum members
    MIT = "MIT"
    APACHE_2_0 = "APACHE_2_0"
    BSD_3_CLAUSE = "BSD_3_CLAUSE"
    BSD_2_CLAUSE = "BSD_2_CLAUSE"
    ISC = "ISC"
    GPL_3_0 = "GPL_3_0"
    GPL_2_0 = "GPL_2_0"
    LGPL_3_0 = "LGPL_3_0"
    LGPL_2_1 = "LGPL_2_1"
    AGPL_3_0 = "AGPL_3_0"
    MPL_2_0 = "MPL_2_0"
    CC_BY_4_0 = "CC_BY_4_0"
    CC_BY_SA_4_0 = "CC_BY_SA_4_0"
    CC_BY_NC_4_0 = "CC_BY_NC_4_0"
    CC_BY_NC_SA_4_0 = "CC_BY_NC_SA_4_0"
    CC_BY_ND_4_0 = "CC_BY_ND_4_0"
    CC0_1_0 = "CC0_1_0"
    UNLICENSE = "UNLICENSE"
    PROPRIETARY = "PROPRIETARY"
    CUSTOM = "CUSTOM"

# Set metadata after class creation
LicenseType._metadata = {
    "MIT": {'description': 'MIT License', 'meaning': 'SPDX:MIT'},
    "APACHE_2_0": {'description': 'Apache License 2.0', 'meaning': 'SPDX:Apache-2.0'},
    "BSD_3_CLAUSE": {'description': 'BSD 3-Clause License', 'meaning': 'SPDX:BSD-3-Clause'},
    "BSD_2_CLAUSE": {'description': 'BSD 2-Clause License', 'meaning': 'SPDX:BSD-2-Clause'},
    "ISC": {'description': 'ISC License', 'meaning': 'SPDX:ISC'},
    "GPL_3_0": {'description': 'GNU General Public License v3.0', 'meaning': 'SPDX:GPL-3.0'},
    "GPL_2_0": {'description': 'GNU General Public License v2.0', 'meaning': 'SPDX:GPL-2.0'},
    "LGPL_3_0": {'description': 'GNU Lesser General Public License v3.0', 'meaning': 'SPDX:LGPL-3.0'},
    "LGPL_2_1": {'description': 'GNU Lesser General Public License v2.1', 'meaning': 'SPDX:LGPL-2.1'},
    "AGPL_3_0": {'description': 'GNU Affero General Public License v3.0', 'meaning': 'SPDX:AGPL-3.0'},
    "MPL_2_0": {'description': 'Mozilla Public License 2.0', 'meaning': 'SPDX:MPL-2.0'},
    "CC_BY_4_0": {'description': 'Creative Commons Attribution 4.0', 'meaning': 'SPDX:CC-BY-4.0'},
    "CC_BY_SA_4_0": {'description': 'Creative Commons Attribution-ShareAlike 4.0', 'meaning': 'SPDX:CC-BY-SA-4.0'},
    "CC_BY_NC_4_0": {'description': 'Creative Commons Attribution-NonCommercial 4.0', 'meaning': 'SPDX:CC-BY-NC-4.0'},
    "CC_BY_NC_SA_4_0": {'description': 'Creative Commons Attribution-NonCommercial-ShareAlike 4.0', 'meaning': 'SPDX:CC-BY-NC-SA-4.0'},
    "CC_BY_ND_4_0": {'description': 'Creative Commons Attribution-NoDerivatives 4.0', 'meaning': 'SPDX:CC-BY-ND-4.0'},
    "CC0_1_0": {'description': 'Creative Commons Zero v1.0 Universal', 'meaning': 'SPDX:CC0-1.0'},
    "UNLICENSE": {'description': 'The Unlicense', 'meaning': 'SPDX:Unlicense'},
    "PROPRIETARY": {'description': 'Proprietary/All rights reserved'},
    "CUSTOM": {'description': 'Custom license terms'},
}

class ResearchField(RichEnum):
    """
    Major research fields and disciplines
    """
    # Enum members
    PHYSICS = "PHYSICS"
    CHEMISTRY = "CHEMISTRY"
    BIOLOGY = "BIOLOGY"
    MATHEMATICS = "MATHEMATICS"
    EARTH_SCIENCES = "EARTH_SCIENCES"
    ASTRONOMY = "ASTRONOMY"
    MEDICINE = "MEDICINE"
    NEUROSCIENCE = "NEUROSCIENCE"
    GENETICS = "GENETICS"
    ECOLOGY = "ECOLOGY"
    MICROBIOLOGY = "MICROBIOLOGY"
    BIOCHEMISTRY = "BIOCHEMISTRY"
    COMPUTER_SCIENCE = "COMPUTER_SCIENCE"
    ENGINEERING = "ENGINEERING"
    MATERIALS_SCIENCE = "MATERIALS_SCIENCE"
    ARTIFICIAL_INTELLIGENCE = "ARTIFICIAL_INTELLIGENCE"
    ROBOTICS = "ROBOTICS"
    PSYCHOLOGY = "PSYCHOLOGY"
    SOCIOLOGY = "SOCIOLOGY"
    ECONOMICS = "ECONOMICS"
    POLITICAL_SCIENCE = "POLITICAL_SCIENCE"
    ANTHROPOLOGY = "ANTHROPOLOGY"
    EDUCATION = "EDUCATION"
    HISTORY = "HISTORY"
    PHILOSOPHY = "PHILOSOPHY"
    LITERATURE = "LITERATURE"
    LINGUISTICS = "LINGUISTICS"
    ART = "ART"
    MUSIC = "MUSIC"
    BIOINFORMATICS = "BIOINFORMATICS"
    COMPUTATIONAL_BIOLOGY = "COMPUTATIONAL_BIOLOGY"
    DATA_SCIENCE = "DATA_SCIENCE"
    COGNITIVE_SCIENCE = "COGNITIVE_SCIENCE"
    ENVIRONMENTAL_SCIENCE = "ENVIRONMENTAL_SCIENCE"
    PUBLIC_HEALTH = "PUBLIC_HEALTH"

# Set metadata after class creation
ResearchField._metadata = {
    "PHYSICS": {'description': 'Physics', 'meaning': 'NCIT:C16989'},
    "CHEMISTRY": {'description': 'Chemistry', 'meaning': 'NCIT:C16414'},
    "BIOLOGY": {'description': 'Biology', 'meaning': 'NCIT:C16345'},
    "MATHEMATICS": {'description': 'Mathematics', 'meaning': 'NCIT:C16825'},
    "EARTH_SCIENCES": {'description': 'Earth sciences and geology'},
    "ASTRONOMY": {'description': 'Astronomy and astrophysics'},
    "MEDICINE": {'description': 'Medicine and health sciences', 'meaning': 'NCIT:C16833'},
    "NEUROSCIENCE": {'description': 'Neuroscience', 'meaning': 'NCIT:C15817'},
    "GENETICS": {'description': 'Genetics and genomics', 'meaning': 'NCIT:C16624'},
    "ECOLOGY": {'description': 'Ecology and environmental science', 'meaning': 'NCIT:C16526'},
    "MICROBIOLOGY": {'meaning': 'NCIT:C16851'},
    "BIOCHEMISTRY": {'meaning': 'NCIT:C16337'},
    "COMPUTER_SCIENCE": {'description': 'Computer science'},
    "ENGINEERING": {'description': 'Engineering'},
    "MATERIALS_SCIENCE": {'description': 'Materials science'},
    "ARTIFICIAL_INTELLIGENCE": {'description': 'Artificial intelligence and machine learning'},
    "ROBOTICS": {'description': 'Robotics'},
    "PSYCHOLOGY": {'description': 'Psychology'},
    "SOCIOLOGY": {'description': 'Sociology'},
    "ECONOMICS": {'description': 'Economics'},
    "POLITICAL_SCIENCE": {'description': 'Political science'},
    "ANTHROPOLOGY": {'description': 'Anthropology'},
    "EDUCATION": {'description': 'Education'},
    "HISTORY": {'description': 'History'},
    "PHILOSOPHY": {'description': 'Philosophy'},
    "LITERATURE": {'description': 'Literature'},
    "LINGUISTICS": {'description': 'Linguistics'},
    "ART": {'description': 'Art and art history'},
    "MUSIC": {'description': 'Music and musicology'},
    "BIOINFORMATICS": {'description': 'Bioinformatics'},
    "COMPUTATIONAL_BIOLOGY": {'description': 'Computational biology'},
    "DATA_SCIENCE": {'description': 'Data science'},
    "COGNITIVE_SCIENCE": {'description': 'Cognitive science'},
    "ENVIRONMENTAL_SCIENCE": {'description': 'Environmental science'},
    "PUBLIC_HEALTH": {'description': 'Public health'},
}

class FundingType(RichEnum):
    """
    Types of research funding
    """
    # Enum members
    GRANT = "GRANT"
    CONTRACT = "CONTRACT"
    FELLOWSHIP = "FELLOWSHIP"
    AWARD = "AWARD"
    GIFT = "GIFT"
    INTERNAL = "INTERNAL"
    INDUSTRY = "INDUSTRY"
    GOVERNMENT = "GOVERNMENT"
    FOUNDATION = "FOUNDATION"
    CROWDFUNDING = "CROWDFUNDING"

# Set metadata after class creation
FundingType._metadata = {
    "GRANT": {'description': 'Research grant'},
    "CONTRACT": {'description': 'Research contract'},
    "FELLOWSHIP": {'description': 'Fellowship or scholarship', 'meaning': 'NCIT:C20003'},
    "AWARD": {'description': 'Prize or award'},
    "GIFT": {'description': 'Gift or donation'},
    "INTERNAL": {'description': 'Internal/institutional funding'},
    "INDUSTRY": {'description': 'Industry sponsorship'},
    "GOVERNMENT": {'description': 'Government funding'},
    "FOUNDATION": {'description': 'Foundation or charity funding'},
    "CROWDFUNDING": {'description': 'Crowdfunded research'},
}

class ManuscriptSection(RichEnum):
    """
    Sections of a scientific manuscript or publication
    """
    # Enum members
    TITLE = "TITLE"
    AUTHORS = "AUTHORS"
    ABSTRACT = "ABSTRACT"
    KEYWORDS = "KEYWORDS"
    INTRODUCTION = "INTRODUCTION"
    LITERATURE_REVIEW = "LITERATURE_REVIEW"
    METHODS = "METHODS"
    RESULTS = "RESULTS"
    DISCUSSION = "DISCUSSION"
    CONCLUSIONS = "CONCLUSIONS"
    RESULTS_AND_DISCUSSION = "RESULTS_AND_DISCUSSION"
    ACKNOWLEDGMENTS = "ACKNOWLEDGMENTS"
    REFERENCES = "REFERENCES"
    APPENDICES = "APPENDICES"
    SUPPLEMENTARY_MATERIAL = "SUPPLEMENTARY_MATERIAL"
    DATA_AVAILABILITY = "DATA_AVAILABILITY"
    CODE_AVAILABILITY = "CODE_AVAILABILITY"
    AUTHOR_CONTRIBUTIONS = "AUTHOR_CONTRIBUTIONS"
    CONFLICT_OF_INTEREST = "CONFLICT_OF_INTEREST"
    FUNDING = "FUNDING"
    ETHICS_STATEMENT = "ETHICS_STATEMENT"
    SYSTEMATIC_REVIEW_METHODS = "SYSTEMATIC_REVIEW_METHODS"
    META_ANALYSIS = "META_ANALYSIS"
    STUDY_PROTOCOL = "STUDY_PROTOCOL"
    CONSORT_FLOW_DIAGRAM = "CONSORT_FLOW_DIAGRAM"
    HIGHLIGHTS = "HIGHLIGHTS"
    GRAPHICAL_ABSTRACT = "GRAPHICAL_ABSTRACT"
    LAY_SUMMARY = "LAY_SUMMARY"
    BOX = "BOX"
    CASE_PRESENTATION = "CASE_PRESENTATION"
    LIMITATIONS = "LIMITATIONS"
    FUTURE_DIRECTIONS = "FUTURE_DIRECTIONS"
    GLOSSARY = "GLOSSARY"
    ABBREVIATIONS = "ABBREVIATIONS"
    OTHER_MAIN_TEXT = "OTHER_MAIN_TEXT"
    OTHER_SUPPLEMENTARY = "OTHER_SUPPLEMENTARY"

# Set metadata after class creation
ManuscriptSection._metadata = {
    "TITLE": {'meaning': 'IAO:0000305', 'annotations': {'order': 1}},
    "AUTHORS": {'description': 'Authors and affiliations', 'meaning': 'IAO:0000321', 'annotations': {'order': 2}},
    "ABSTRACT": {'description': 'Abstract', 'meaning': 'IAO:0000315', 'annotations': {'order': 3, 'typical_length': '150-300 words'}},
    "KEYWORDS": {'meaning': 'IAO:0000630', 'annotations': {'order': 4}},
    "INTRODUCTION": {'description': 'Introduction/Background', 'meaning': 'IAO:0000316', 'annotations': {'order': 5}, 'aliases': ['Background']},
    "LITERATURE_REVIEW": {'description': 'Literature review', 'meaning': 'IAO:0000639', 'annotations': {'order': 6, 'optional': True}},
    "METHODS": {'description': 'Methods/Materials and Methods', 'meaning': 'IAO:0000317', 'annotations': {'order': 7}, 'aliases': ['Materials and Methods', 'Methodology', 'Experimental']},
    "RESULTS": {'meaning': 'IAO:0000318', 'annotations': {'order': 8}, 'aliases': ['Findings']},
    "DISCUSSION": {'meaning': 'IAO:0000319', 'annotations': {'order': 9}},
    "CONCLUSIONS": {'description': 'Conclusions', 'meaning': 'IAO:0000615', 'annotations': {'order': 10}, 'aliases': ['Conclusion']},
    "RESULTS_AND_DISCUSSION": {'description': 'Combined Results and Discussion', 'annotations': {'order': 8, 'note': 'alternative to separate sections'}},
    "ACKNOWLEDGMENTS": {'description': 'Acknowledgments', 'meaning': 'IAO:0000324', 'annotations': {'order': 11}, 'aliases': ['Acknowledgements']},
    "REFERENCES": {'description': 'References/Bibliography', 'meaning': 'IAO:0000320', 'annotations': {'order': 12}, 'aliases': ['Bibliography', 'Literature Cited', 'Works Cited']},
    "APPENDICES": {'description': 'Appendices', 'meaning': 'IAO:0000326', 'annotations': {'order': 13}, 'aliases': ['Appendix']},
    "SUPPLEMENTARY_MATERIAL": {'description': 'Supplementary material', 'meaning': 'IAO:0000326', 'annotations': {'order': 14, 'location': 'often online-only'}, 'aliases': ['Supporting Information', 'Supplemental Data']},
    "DATA_AVAILABILITY": {'description': 'Data availability statement', 'meaning': 'IAO:0000611', 'annotations': {'order': 11.1, 'required_by': 'many journals'}},
    "CODE_AVAILABILITY": {'description': 'Code availability statement', 'meaning': 'IAO:0000611', 'annotations': {'order': 11.2}},
    "AUTHOR_CONTRIBUTIONS": {'description': 'Author contributions', 'meaning': 'IAO:0000323', 'annotations': {'order': 11.3}, 'aliases': ['CRediT statement']},
    "CONFLICT_OF_INTEREST": {'description': 'Conflict of interest statement', 'meaning': 'IAO:0000616', 'annotations': {'order': 11.4}, 'aliases': ['Competing Interests', 'Declaration of Interests']},
    "FUNDING": {'description': 'Funding information', 'meaning': 'IAO:0000623', 'annotations': {'order': 11.5}, 'aliases': ['Financial Support', 'Grant Information']},
    "ETHICS_STATEMENT": {'description': 'Ethics approval statement', 'meaning': 'IAO:0000620', 'annotations': {'order': 11.6}},
    "SYSTEMATIC_REVIEW_METHODS": {'description': 'Systematic review methodology (PRISMA)', 'annotations': {'specific_to': 'systematic reviews'}},
    "META_ANALYSIS": {'description': 'Meta-analysis section', 'annotations': {'specific_to': 'meta-analyses'}},
    "STUDY_PROTOCOL": {'description': 'Study protocol', 'annotations': {'specific_to': 'clinical trials'}},
    "CONSORT_FLOW_DIAGRAM": {'description': 'CONSORT flow diagram', 'annotations': {'specific_to': 'randomized trials'}},
    "HIGHLIGHTS": {'description': 'Highlights/Key points', 'annotations': {'order': 3.5, 'typical_length': '3-5 bullet points'}},
    "GRAPHICAL_ABSTRACT": {'description': 'Graphical abstract', 'meaning': 'IAO:0000707', 'annotations': {'order': 3.6, 'format': 'visual'}},
    "LAY_SUMMARY": {'description': 'Lay summary/Plain language summary', 'meaning': 'IAO:0000609', 'annotations': {'order': 3.7, 'audience': 'general public'}},
    "BOX": {'description': 'Box/Sidebar with supplementary information', 'annotations': {'placement': 'variable'}},
    "CASE_PRESENTATION": {'description': 'Case presentation (for case reports)', 'meaning': 'IAO:0000613', 'annotations': {'specific_to': 'case reports'}},
    "LIMITATIONS": {'description': 'Limitations section', 'meaning': 'IAO:0000631', 'annotations': {'often_part_of': 'Discussion'}},
    "FUTURE_DIRECTIONS": {'description': 'Future directions/Future work', 'meaning': 'IAO:0000625', 'annotations': {'often_part_of': 'Discussion or Conclusions'}},
    "GLOSSARY": {'description': 'Glossary of terms', 'annotations': {'placement': 'front or back matter'}},
    "ABBREVIATIONS": {'description': 'List of abbreviations', 'meaning': 'IAO:0000606', 'annotations': {'placement': 'front matter'}},
    "OTHER_MAIN_TEXT": {'description': 'Other main text section', 'annotations': {'catch_all': True}},
    "OTHER_SUPPLEMENTARY": {'description': 'Other supplementary section', 'annotations': {'catch_all': True}},
}

class ResearchRole(RichEnum):
    """
    Roles in research and authorship
    """
    # Enum members
    CONCEPTUALIZATION = "CONCEPTUALIZATION"
    DATA_CURATION = "DATA_CURATION"
    FORMAL_ANALYSIS = "FORMAL_ANALYSIS"
    FUNDING_ACQUISITION = "FUNDING_ACQUISITION"
    INVESTIGATION = "INVESTIGATION"
    METHODOLOGY = "METHODOLOGY"
    PROJECT_ADMINISTRATION = "PROJECT_ADMINISTRATION"
    RESOURCES = "RESOURCES"
    SOFTWARE = "SOFTWARE"
    SUPERVISION = "SUPERVISION"
    VALIDATION = "VALIDATION"
    VISUALIZATION = "VISUALIZATION"
    WRITING_ORIGINAL = "WRITING_ORIGINAL"
    WRITING_REVIEW = "WRITING_REVIEW"
    FIRST_AUTHOR = "FIRST_AUTHOR"
    CORRESPONDING_AUTHOR = "CORRESPONDING_AUTHOR"
    SENIOR_AUTHOR = "SENIOR_AUTHOR"
    CO_AUTHOR = "CO_AUTHOR"
    PRINCIPAL_INVESTIGATOR = "PRINCIPAL_INVESTIGATOR"
    CO_INVESTIGATOR = "CO_INVESTIGATOR"
    COLLABORATOR = "COLLABORATOR"

# Set metadata after class creation
ResearchRole._metadata = {
    "CONCEPTUALIZATION": {'description': 'Ideas; formulation of research goals', 'meaning': 'CRediT:conceptualization'},
    "DATA_CURATION": {'description': 'Data management and annotation', 'meaning': 'CRediT:data-curation'},
    "FORMAL_ANALYSIS": {'description': 'Statistical and mathematical analysis', 'meaning': 'CRediT:formal-analysis'},
    "FUNDING_ACQUISITION": {'description': 'Acquisition of financial support', 'meaning': 'CRediT:funding-acquisition'},
    "INVESTIGATION": {'description': 'Conducting research and data collection', 'meaning': 'CRediT:investigation'},
    "METHODOLOGY": {'description': 'Development of methodology', 'meaning': 'CRediT:methodology'},
    "PROJECT_ADMINISTRATION": {'description': 'Project management and coordination', 'meaning': 'CRediT:project-administration'},
    "RESOURCES": {'description': 'Provision of materials and tools', 'meaning': 'CRediT:resources'},
    "SOFTWARE": {'description': 'Programming and software development', 'meaning': 'CRediT:software'},
    "SUPERVISION": {'description': 'Oversight and mentorship', 'meaning': 'CRediT:supervision'},
    "VALIDATION": {'description': 'Verification of results', 'meaning': 'CRediT:validation'},
    "VISUALIZATION": {'description': 'Data presentation and visualization', 'meaning': 'CRediT:visualization'},
    "WRITING_ORIGINAL": {'description': 'Writing - original draft', 'meaning': 'CRediT:writing-original-draft'},
    "WRITING_REVIEW": {'description': 'Writing - review and editing', 'meaning': 'CRediT:writing-review-editing'},
    "FIRST_AUTHOR": {'description': 'First/lead author', 'meaning': 'MS:1002034'},
    "CORRESPONDING_AUTHOR": {'meaning': 'NCIT:C164481'},
    "SENIOR_AUTHOR": {'description': 'Senior/last author', 'annotations': {'note': 'Often the PI or lab head'}},
    "CO_AUTHOR": {'description': 'Co-author', 'meaning': 'NCIT:C42781'},
    "PRINCIPAL_INVESTIGATOR": {'description': 'Principal investigator (PI)', 'meaning': 'NCIT:C19924'},
    "CO_INVESTIGATOR": {'meaning': 'NCIT:C51812'},
    "COLLABORATOR": {'meaning': 'NCIT:C84336'},
}

class OpenAccessType(RichEnum):
    """
    Types of open access publishing
    """
    # Enum members
    GOLD = "GOLD"
    GREEN = "GREEN"
    HYBRID = "HYBRID"
    DIAMOND = "DIAMOND"
    BRONZE = "BRONZE"
    CLOSED = "CLOSED"
    EMBARGO = "EMBARGO"

# Set metadata after class creation
OpenAccessType._metadata = {
    "GOLD": {'description': 'Gold open access (published OA)'},
    "GREEN": {'description': 'Green open access (self-archived)'},
    "HYBRID": {'description': 'Hybrid journal with OA option'},
    "DIAMOND": {'description': 'Diamond/platinum OA (no fees)'},
    "BRONZE": {'description': 'Free to read but no license'},
    "CLOSED": {'description': 'Closed access/subscription only'},
    "EMBARGO": {'description': 'Under embargo period'},
}

class CitationStyle(RichEnum):
    """
    Common citation and reference styles
    """
    # Enum members
    APA = "APA"
    MLA = "MLA"
    CHICAGO = "CHICAGO"
    HARVARD = "HARVARD"
    VANCOUVER = "VANCOUVER"
    IEEE = "IEEE"
    ACS = "ACS"
    AMA = "AMA"
    NATURE = "NATURE"
    SCIENCE = "SCIENCE"
    CELL = "CELL"

# Set metadata after class creation
CitationStyle._metadata = {
    "APA": {'description': 'American Psychological Association'},
    "MLA": {'description': 'Modern Language Association'},
    "CHICAGO": {'description': 'Chicago Manual of Style'},
    "HARVARD": {'description': 'Harvard referencing'},
    "VANCOUVER": {'description': 'Vancouver style (biomedical)'},
    "IEEE": {'description': 'Institute of Electrical and Electronics Engineers'},
    "ACS": {'description': 'American Chemical Society'},
    "AMA": {'description': 'American Medical Association'},
    "NATURE": {'description': 'Nature style'},
    "SCIENCE": {'description': 'Science style'},
    "CELL": {'description': 'Cell Press style'},
}

class EnergySource(RichEnum):
    """
    Types of energy sources and generation methods
    """
    # Enum members
    SOLAR = "SOLAR"
    WIND = "WIND"
    HYDROELECTRIC = "HYDROELECTRIC"
    GEOTHERMAL = "GEOTHERMAL"
    BIOMASS = "BIOMASS"
    BIOFUEL = "BIOFUEL"
    TIDAL = "TIDAL"
    HYDROGEN = "HYDROGEN"
    COAL = "COAL"
    NATURAL_GAS = "NATURAL_GAS"
    PETROLEUM = "PETROLEUM"
    DIESEL = "DIESEL"
    GASOLINE = "GASOLINE"
    PROPANE = "PROPANE"
    NUCLEAR_FISSION = "NUCLEAR_FISSION"
    NUCLEAR_FUSION = "NUCLEAR_FUSION"
    GRID_MIX = "GRID_MIX"
    BATTERY_STORAGE = "BATTERY_STORAGE"

# Set metadata after class creation
EnergySource._metadata = {
    "SOLAR": {'meaning': 'ENVO:01001862', 'annotations': {'renewable': True, 'emission_free': True}, 'aliases': ['Solar radiation']},
    "WIND": {'annotations': {'renewable': True, 'emission_free': True}, 'aliases': ['wind wave energy']},
    "HYDROELECTRIC": {'annotations': {'renewable': True, 'emission_free': True}, 'aliases': ['hydroelectric dam']},
    "GEOTHERMAL": {'meaning': 'ENVO:2000034', 'annotations': {'renewable': True, 'emission_free': True}, 'aliases': ['geothermal energy']},
    "BIOMASS": {'annotations': {'renewable': True, 'emission_free': False}, 'aliases': ['organic material']},
    "BIOFUEL": {'annotations': {'renewable': True, 'emission_free': False}},
    "TIDAL": {'annotations': {'renewable': True, 'emission_free': True}},
    "HYDROGEN": {'meaning': 'CHEBI:18276', 'annotations': {'renewable': 'depends', 'emission_free': True}, 'aliases': ['dihydrogen']},
    "COAL": {'meaning': 'ENVO:02000091', 'annotations': {'renewable': False, 'emission_free': False, 'fossil_fuel': True}},
    "NATURAL_GAS": {'meaning': 'ENVO:01000552', 'annotations': {'renewable': False, 'emission_free': False, 'fossil_fuel': True}},
    "PETROLEUM": {'meaning': 'ENVO:00002984', 'annotations': {'renewable': False, 'emission_free': False, 'fossil_fuel': True}},
    "DIESEL": {'meaning': 'ENVO:03510006', 'annotations': {'renewable': False, 'emission_free': False, 'fossil_fuel': True}, 'aliases': ['diesel fuel']},
    "GASOLINE": {'annotations': {'renewable': False, 'emission_free': False, 'fossil_fuel': True}, 'aliases': ['fuel oil']},
    "PROPANE": {'meaning': 'ENVO:01000553', 'annotations': {'renewable': False, 'emission_free': False, 'fossil_fuel': True}, 'aliases': ['liquefied petroleum gas']},
    "NUCLEAR_FISSION": {'annotations': {'renewable': False, 'emission_free': True}, 'aliases': ['nuclear energy']},
    "NUCLEAR_FUSION": {'annotations': {'renewable': False, 'emission_free': True}, 'aliases': ['nuclear energy']},
    "GRID_MIX": {'annotations': {'renewable': 'partial'}},
    "BATTERY_STORAGE": {'description': 'Battery storage systems', 'annotations': {'storage': True}},
}

class EnergyUnit(RichEnum):
    """
    Units for measuring energy
    """
    # Enum members
    JOULE = "JOULE"
    KILOJOULE = "KILOJOULE"
    MEGAJOULE = "MEGAJOULE"
    GIGAJOULE = "GIGAJOULE"
    WATT_HOUR = "WATT_HOUR"
    KILOWATT_HOUR = "KILOWATT_HOUR"
    MEGAWATT_HOUR = "MEGAWATT_HOUR"
    GIGAWATT_HOUR = "GIGAWATT_HOUR"
    TERAWATT_HOUR = "TERAWATT_HOUR"
    CALORIE = "CALORIE"
    KILOCALORIE = "KILOCALORIE"
    BTU = "BTU"
    THERM = "THERM"
    ELECTRON_VOLT = "ELECTRON_VOLT"
    TOE = "TOE"
    TCE = "TCE"

# Set metadata after class creation
EnergyUnit._metadata = {
    "JOULE": {'description': 'Joule (J)', 'meaning': 'QUDT:J', 'annotations': {'symbol': 'J', 'ucum': 'J', 'si_base': True}},
    "KILOJOULE": {'description': 'Kilojoule (kJ)', 'meaning': 'QUDT:KiloJ', 'annotations': {'symbol': 'kJ', 'ucum': 'kJ', 'joules': 1000}},
    "MEGAJOULE": {'description': 'Megajoule (MJ)', 'meaning': 'QUDT:MegaJ', 'annotations': {'symbol': 'MJ', 'ucum': 'MJ', 'joules': '1e6'}},
    "GIGAJOULE": {'description': 'Gigajoule (GJ)', 'meaning': 'QUDT:GigaJ', 'annotations': {'symbol': 'GJ', 'ucum': 'GJ', 'joules': '1e9'}},
    "WATT_HOUR": {'description': 'Watt-hour (Wh)', 'meaning': 'QUDT:W-HR', 'annotations': {'symbol': 'Wh', 'ucum': 'W.h', 'joules': 3600}},
    "KILOWATT_HOUR": {'description': 'Kilowatt-hour (kWh)', 'meaning': 'QUDT:KiloW-HR', 'annotations': {'symbol': 'kWh', 'ucum': 'kW.h', 'joules': '3.6e6'}},
    "MEGAWATT_HOUR": {'description': 'Megawatt-hour (MWh)', 'meaning': 'QUDT:MegaW-HR', 'annotations': {'symbol': 'MWh', 'ucum': 'MW.h', 'joules': '3.6e9'}},
    "GIGAWATT_HOUR": {'description': 'Gigawatt-hour (GWh)', 'meaning': 'QUDT:GigaW-HR', 'annotations': {'symbol': 'GWh', 'ucum': 'GW.h', 'joules': '3.6e12'}},
    "TERAWATT_HOUR": {'description': 'Terawatt-hour (TWh)', 'meaning': 'QUDT:TeraW-HR', 'annotations': {'symbol': 'TWh', 'ucum': 'TW.h', 'joules': '3.6e15'}},
    "CALORIE": {'description': 'Calorie (cal)', 'meaning': 'QUDT:CAL', 'annotations': {'symbol': 'cal', 'ucum': 'cal', 'joules': 4.184}},
    "KILOCALORIE": {'description': 'Kilocalorie (kcal)', 'meaning': 'QUDT:KiloCAL', 'annotations': {'symbol': 'kcal', 'ucum': 'kcal', 'joules': 4184}},
    "BTU": {'description': 'British thermal unit', 'meaning': 'QUDT:BTU_IT', 'annotations': {'symbol': 'BTU', 'ucum': '[Btu_IT]', 'joules': 1055.06}},
    "THERM": {'description': 'Therm', 'meaning': 'QUDT:THM_US', 'annotations': {'symbol': 'thm', 'ucum': '[thm_us]', 'joules': '1.055e8'}},
    "ELECTRON_VOLT": {'description': 'Electron volt (eV)', 'meaning': 'QUDT:EV', 'annotations': {'symbol': 'eV', 'ucum': 'eV', 'joules': 1.602e-19}},
    "TOE": {'description': 'Tonne of oil equivalent', 'meaning': 'QUDT:TOE', 'annotations': {'symbol': 'toe', 'ucum': 'toe', 'joules': '4.187e10'}},
    "TCE": {'description': 'Tonne of coal equivalent', 'annotations': {'symbol': 'tce', 'ucum': 'tce', 'joules': '2.93e10'}},
}

class PowerUnit(RichEnum):
    """
    Units for measuring power (energy per time)
    """
    # Enum members
    WATT = "WATT"
    KILOWATT = "KILOWATT"
    MEGAWATT = "MEGAWATT"
    GIGAWATT = "GIGAWATT"
    TERAWATT = "TERAWATT"
    HORSEPOWER = "HORSEPOWER"
    BTU_PER_HOUR = "BTU_PER_HOUR"

# Set metadata after class creation
PowerUnit._metadata = {
    "WATT": {'description': 'Watt (W)', 'meaning': 'QUDT:W', 'annotations': {'symbol': 'W', 'ucum': 'W', 'si_base': True}},
    "KILOWATT": {'description': 'Kilowatt (kW)', 'meaning': 'QUDT:KiloW', 'annotations': {'symbol': 'kW', 'ucum': 'kW', 'watts': 1000}},
    "MEGAWATT": {'description': 'Megawatt (MW)', 'meaning': 'QUDT:MegaW', 'annotations': {'symbol': 'MW', 'ucum': 'MW', 'watts': '1e6'}},
    "GIGAWATT": {'description': 'Gigawatt (GW)', 'meaning': 'QUDT:GigaW', 'annotations': {'symbol': 'GW', 'ucum': 'GW', 'watts': '1e9'}},
    "TERAWATT": {'description': 'Terawatt (TW)', 'meaning': 'QUDT:TeraW', 'annotations': {'symbol': 'TW', 'ucum': 'TW', 'watts': '1e12'}},
    "HORSEPOWER": {'description': 'Horsepower', 'meaning': 'QUDT:HP', 'annotations': {'symbol': 'hp', 'ucum': '[HP]', 'watts': 745.7}},
    "BTU_PER_HOUR": {'description': 'BTU per hour', 'annotations': {'symbol': 'BTU/h', 'ucum': '[Btu_IT]/h', 'watts': 0.293}},
}

class EnergyEfficiencyRating(RichEnum):
    """
    Energy efficiency ratings and standards
    """
    # Enum members
    A_PLUS_PLUS_PLUS = "A_PLUS_PLUS_PLUS"
    A_PLUS_PLUS = "A_PLUS_PLUS"
    A_PLUS = "A_PLUS"
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    E = "E"
    F = "F"
    G = "G"
    ENERGY_STAR = "ENERGY_STAR"
    ENERGY_STAR_MOST_EFFICIENT = "ENERGY_STAR_MOST_EFFICIENT"

# Set metadata after class creation
EnergyEfficiencyRating._metadata = {
    "A_PLUS_PLUS_PLUS": {'description': 'A+++ (highest efficiency)', 'annotations': {'rank': 1, 'region': 'EU'}},
    "A_PLUS_PLUS": {'description': 'A++', 'annotations': {'rank': 2, 'region': 'EU'}},
    "A_PLUS": {'description': 'A+', 'annotations': {'rank': 3, 'region': 'EU'}},
    "A": {'description': 'A', 'annotations': {'rank': 4, 'region': 'EU'}},
    "B": {'description': 'B', 'annotations': {'rank': 5, 'region': 'EU'}},
    "C": {'description': 'C', 'annotations': {'rank': 6, 'region': 'EU'}},
    "D": {'description': 'D', 'annotations': {'rank': 7, 'region': 'EU'}},
    "E": {'description': 'E', 'annotations': {'rank': 8, 'region': 'EU'}},
    "F": {'description': 'F', 'annotations': {'rank': 9, 'region': 'EU'}},
    "G": {'description': 'G (lowest efficiency)', 'annotations': {'rank': 10, 'region': 'EU'}},
    "ENERGY_STAR": {'description': 'Energy Star certified', 'annotations': {'region': 'US'}},
    "ENERGY_STAR_MOST_EFFICIENT": {'description': 'Energy Star Most Efficient', 'annotations': {'region': 'US'}},
}

class BuildingEnergyStandard(RichEnum):
    """
    Building energy efficiency standards and certifications
    """
    # Enum members
    PASSIVE_HOUSE = "PASSIVE_HOUSE"
    LEED_PLATINUM = "LEED_PLATINUM"
    LEED_GOLD = "LEED_GOLD"
    LEED_SILVER = "LEED_SILVER"
    LEED_CERTIFIED = "LEED_CERTIFIED"
    BREEAM_OUTSTANDING = "BREEAM_OUTSTANDING"
    BREEAM_EXCELLENT = "BREEAM_EXCELLENT"
    BREEAM_VERY_GOOD = "BREEAM_VERY_GOOD"
    BREEAM_GOOD = "BREEAM_GOOD"
    BREEAM_PASS = "BREEAM_PASS"
    NET_ZERO = "NET_ZERO"
    ENERGY_POSITIVE = "ENERGY_POSITIVE"
    ZERO_CARBON = "ZERO_CARBON"

# Set metadata after class creation
BuildingEnergyStandard._metadata = {
    "PASSIVE_HOUSE": {'description': 'Passive House (Passivhaus) standard'},
    "LEED_PLATINUM": {'description': 'LEED Platinum certification'},
    "LEED_GOLD": {'description': 'LEED Gold certification'},
    "LEED_SILVER": {'description': 'LEED Silver certification'},
    "LEED_CERTIFIED": {'description': 'LEED Certified'},
    "BREEAM_OUTSTANDING": {'description': 'BREEAM Outstanding'},
    "BREEAM_EXCELLENT": {'description': 'BREEAM Excellent'},
    "BREEAM_VERY_GOOD": {'description': 'BREEAM Very Good'},
    "BREEAM_GOOD": {'description': 'BREEAM Good'},
    "BREEAM_PASS": {'description': 'BREEAM Pass'},
    "NET_ZERO": {'description': 'Net Zero Energy Building'},
    "ENERGY_POSITIVE": {'description': 'Energy Positive Building'},
    "ZERO_CARBON": {'description': 'Zero Carbon Building'},
}

class GridType(RichEnum):
    """
    Types of electrical grid systems
    """
    # Enum members
    MAIN_GRID = "MAIN_GRID"
    MICROGRID = "MICROGRID"
    OFF_GRID = "OFF_GRID"
    SMART_GRID = "SMART_GRID"
    MINI_GRID = "MINI_GRID"
    VIRTUAL_POWER_PLANT = "VIRTUAL_POWER_PLANT"

# Set metadata after class creation
GridType._metadata = {
    "MAIN_GRID": {'description': 'Main utility grid'},
    "MICROGRID": {'description': 'Microgrid'},
    "OFF_GRID": {'description': 'Off-grid/standalone'},
    "SMART_GRID": {'description': 'Smart grid'},
    "MINI_GRID": {'description': 'Mini-grid'},
    "VIRTUAL_POWER_PLANT": {'description': 'Virtual power plant'},
}

class EnergyStorageType(RichEnum):
    """
    Types of energy storage systems
    """
    # Enum members
    LITHIUM_ION_BATTERY = "LITHIUM_ION_BATTERY"
    LEAD_ACID_BATTERY = "LEAD_ACID_BATTERY"
    FLOW_BATTERY = "FLOW_BATTERY"
    SOLID_STATE_BATTERY = "SOLID_STATE_BATTERY"
    SODIUM_ION_BATTERY = "SODIUM_ION_BATTERY"
    PUMPED_HYDRO = "PUMPED_HYDRO"
    COMPRESSED_AIR = "COMPRESSED_AIR"
    FLYWHEEL = "FLYWHEEL"
    GRAVITY_STORAGE = "GRAVITY_STORAGE"
    MOLTEN_SALT = "MOLTEN_SALT"
    ICE_STORAGE = "ICE_STORAGE"
    PHASE_CHANGE = "PHASE_CHANGE"
    HYDROGEN_STORAGE = "HYDROGEN_STORAGE"
    SYNTHETIC_FUEL = "SYNTHETIC_FUEL"
    SUPERCAPACITOR = "SUPERCAPACITOR"
    SUPERCONDUCTING = "SUPERCONDUCTING"

# Set metadata after class creation
EnergyStorageType._metadata = {
    "LITHIUM_ION_BATTERY": {'description': 'Lithium-ion battery', 'annotations': {'category': 'electrochemical'}},
    "LEAD_ACID_BATTERY": {'description': 'Lead-acid battery', 'annotations': {'category': 'electrochemical'}},
    "FLOW_BATTERY": {'description': 'Flow battery (e.g., vanadium redox)', 'annotations': {'category': 'electrochemical'}},
    "SOLID_STATE_BATTERY": {'description': 'Solid-state battery', 'annotations': {'category': 'electrochemical'}},
    "SODIUM_ION_BATTERY": {'description': 'Sodium-ion battery', 'annotations': {'category': 'electrochemical'}},
    "PUMPED_HYDRO": {'description': 'Pumped hydroelectric storage', 'annotations': {'category': 'mechanical'}},
    "COMPRESSED_AIR": {'description': 'Compressed air energy storage (CAES)', 'annotations': {'category': 'mechanical'}},
    "FLYWHEEL": {'description': 'Flywheel energy storage', 'annotations': {'category': 'mechanical'}},
    "GRAVITY_STORAGE": {'description': 'Gravity-based storage', 'annotations': {'category': 'mechanical'}},
    "MOLTEN_SALT": {'description': 'Molten salt thermal storage', 'annotations': {'category': 'thermal'}},
    "ICE_STORAGE": {'description': 'Ice thermal storage', 'annotations': {'category': 'thermal'}},
    "PHASE_CHANGE": {'description': 'Phase change materials', 'annotations': {'category': 'thermal'}},
    "HYDROGEN_STORAGE": {'description': 'Hydrogen storage', 'annotations': {'category': 'chemical'}},
    "SYNTHETIC_FUEL": {'description': 'Synthetic fuel storage', 'annotations': {'category': 'chemical'}},
    "SUPERCAPACITOR": {'description': 'Supercapacitor', 'annotations': {'category': 'electrical'}},
    "SUPERCONDUCTING": {'description': 'Superconducting magnetic energy storage (SMES)', 'annotations': {'category': 'electrical'}},
}

class EmissionScope(RichEnum):
    """
    Greenhouse gas emission scopes (GHG Protocol)
    """
    # Enum members
    SCOPE_1 = "SCOPE_1"
    SCOPE_2 = "SCOPE_2"
    SCOPE_3 = "SCOPE_3"
    SCOPE_3_UPSTREAM = "SCOPE_3_UPSTREAM"
    SCOPE_3_DOWNSTREAM = "SCOPE_3_DOWNSTREAM"

# Set metadata after class creation
EmissionScope._metadata = {
    "SCOPE_1": {'description': 'Direct emissions from owned or controlled sources', 'annotations': {'ghg_protocol': 'Scope 1'}},
    "SCOPE_2": {'description': 'Indirect emissions from purchased energy', 'annotations': {'ghg_protocol': 'Scope 2'}},
    "SCOPE_3": {'description': 'All other indirect emissions in value chain', 'annotations': {'ghg_protocol': 'Scope 3'}},
    "SCOPE_3_UPSTREAM": {'description': 'Upstream Scope 3 emissions', 'annotations': {'ghg_protocol': 'Scope 3'}},
    "SCOPE_3_DOWNSTREAM": {'description': 'Downstream Scope 3 emissions', 'annotations': {'ghg_protocol': 'Scope 3'}},
}

class CarbonIntensity(RichEnum):
    """
    Carbon intensity levels for energy sources
    """
    # Enum members
    ZERO_CARBON = "ZERO_CARBON"
    VERY_LOW_CARBON = "VERY_LOW_CARBON"
    LOW_CARBON = "LOW_CARBON"
    MEDIUM_CARBON = "MEDIUM_CARBON"
    HIGH_CARBON = "HIGH_CARBON"
    VERY_HIGH_CARBON = "VERY_HIGH_CARBON"

# Set metadata after class creation
CarbonIntensity._metadata = {
    "ZERO_CARBON": {'description': 'Zero carbon emissions', 'annotations': {'gCO2_per_kWh': 0}},
    "VERY_LOW_CARBON": {'description': 'Very low carbon (< 50 gCO2/kWh)', 'annotations': {'gCO2_per_kWh': '0-50'}},
    "LOW_CARBON": {'description': 'Low carbon (50-200 gCO2/kWh)', 'annotations': {'gCO2_per_kWh': '50-200'}},
    "MEDIUM_CARBON": {'description': 'Medium carbon (200-500 gCO2/kWh)', 'annotations': {'gCO2_per_kWh': '200-500'}},
    "HIGH_CARBON": {'description': 'High carbon (500-1000 gCO2/kWh)', 'annotations': {'gCO2_per_kWh': '500-1000'}},
    "VERY_HIGH_CARBON": {'description': 'Very high carbon (> 1000 gCO2/kWh)', 'annotations': {'gCO2_per_kWh': '1000+'}},
}

class ElectricityMarket(RichEnum):
    """
    Types of electricity markets and pricing
    """
    # Enum members
    SPOT_MARKET = "SPOT_MARKET"
    DAY_AHEAD = "DAY_AHEAD"
    INTRADAY = "INTRADAY"
    FUTURES = "FUTURES"
    CAPACITY_MARKET = "CAPACITY_MARKET"
    ANCILLARY_SERVICES = "ANCILLARY_SERVICES"
    BILATERAL = "BILATERAL"
    FEED_IN_TARIFF = "FEED_IN_TARIFF"
    NET_METERING = "NET_METERING"
    POWER_PURCHASE_AGREEMENT = "POWER_PURCHASE_AGREEMENT"

# Set metadata after class creation
ElectricityMarket._metadata = {
    "SPOT_MARKET": {'description': 'Spot market/real-time pricing'},
    "DAY_AHEAD": {'description': 'Day-ahead market'},
    "INTRADAY": {'description': 'Intraday market'},
    "FUTURES": {'description': 'Futures market'},
    "CAPACITY_MARKET": {'description': 'Capacity market'},
    "ANCILLARY_SERVICES": {'description': 'Ancillary services market'},
    "BILATERAL": {'description': 'Bilateral contracts'},
    "FEED_IN_TARIFF": {'description': 'Feed-in tariff'},
    "NET_METERING": {'description': 'Net metering'},
    "POWER_PURCHASE_AGREEMENT": {'description': 'Power purchase agreement (PPA)'},
}

class FossilFuelTypeEnum(RichEnum):
    """
    Types of fossil fuels used for energy generation
    """
    # Enum members
    COAL = "COAL"
    NATURAL_GAS = "NATURAL_GAS"
    PETROLEUM = "PETROLEUM"

# Set metadata after class creation
FossilFuelTypeEnum._metadata = {
    "COAL": {'description': 'Coal', 'meaning': 'ENVO:02000091'},
    "NATURAL_GAS": {'description': 'Natural gas', 'meaning': 'ENVO:01000552'},
    "PETROLEUM": {'description': 'Petroleum', 'meaning': 'ENVO:00002984'},
}

class MiningType(RichEnum):
    """
    Types of mining operations
    """
    # Enum members
    OPEN_PIT = "OPEN_PIT"
    STRIP_MINING = "STRIP_MINING"
    MOUNTAINTOP_REMOVAL = "MOUNTAINTOP_REMOVAL"
    QUARRYING = "QUARRYING"
    PLACER = "PLACER"
    DREDGING = "DREDGING"
    SHAFT_MINING = "SHAFT_MINING"
    DRIFT_MINING = "DRIFT_MINING"
    SLOPE_MINING = "SLOPE_MINING"
    ROOM_AND_PILLAR = "ROOM_AND_PILLAR"
    LONGWALL = "LONGWALL"
    BLOCK_CAVING = "BLOCK_CAVING"
    SOLUTION_MINING = "SOLUTION_MINING"
    HYDRAULIC_MINING = "HYDRAULIC_MINING"
    ARTISANAL = "ARTISANAL"
    DEEP_SEA = "DEEP_SEA"

# Set metadata after class creation
MiningType._metadata = {
    "OPEN_PIT": {'description': 'Open-pit mining', 'meaning': 'ENVO:00000284', 'annotations': {'category': 'surface', 'depth': 'shallow to deep'}},
    "STRIP_MINING": {'description': 'Strip mining', 'meaning': 'ENVO:01001441', 'annotations': {'category': 'surface', 'aliases': 'surface mining, opencast mining'}},
    "MOUNTAINTOP_REMOVAL": {'description': 'Mountaintop removal mining', 'annotations': {'category': 'surface', 'region': 'primarily Appalachian'}},
    "QUARRYING": {'description': 'Quarrying', 'meaning': 'ENVO:00000284', 'annotations': {'category': 'surface', 'materials': 'stone, sand, gravel'}},
    "PLACER": {'description': 'Placer mining', 'meaning': 'ENVO:01001204', 'annotations': {'category': 'surface', 'target': 'alluvial deposits'}},
    "DREDGING": {'description': 'Dredging', 'annotations': {'category': 'surface/underwater', 'environment': 'rivers, harbors, seas'}},
    "SHAFT_MINING": {'description': 'Shaft mining', 'annotations': {'category': 'underground', 'access': 'vertical shaft'}},
    "DRIFT_MINING": {'description': 'Drift mining', 'annotations': {'category': 'underground', 'access': 'horizontal tunnel'}},
    "SLOPE_MINING": {'description': 'Slope mining', 'annotations': {'category': 'underground', 'access': 'inclined shaft'}},
    "ROOM_AND_PILLAR": {'description': 'Room and pillar mining', 'annotations': {'category': 'underground', 'method': 'leaves pillars for support'}},
    "LONGWALL": {'description': 'Longwall mining', 'annotations': {'category': 'underground', 'method': 'progressive slice extraction'}},
    "BLOCK_CAVING": {'description': 'Block caving', 'annotations': {'category': 'underground', 'method': 'gravity-assisted'}},
    "SOLUTION_MINING": {'description': 'Solution mining (in-situ leaching)', 'annotations': {'category': 'specialized', 'method': 'chemical dissolution'}},
    "HYDRAULIC_MINING": {'description': 'Hydraulic mining', 'annotations': {'category': 'specialized', 'method': 'high-pressure water'}},
    "ARTISANAL": {'description': 'Artisanal and small-scale mining', 'annotations': {'category': 'small-scale', 'equipment': 'minimal mechanization'}},
    "DEEP_SEA": {'description': 'Deep sea mining', 'annotations': {'category': 'marine', 'depth': 'ocean floor'}},
}

class MineralCategory(RichEnum):
    """
    Categories of minerals and materials
    """
    # Enum members
    PRECIOUS_METALS = "PRECIOUS_METALS"
    BASE_METALS = "BASE_METALS"
    FERROUS_METALS = "FERROUS_METALS"
    RARE_EARTH_ELEMENTS = "RARE_EARTH_ELEMENTS"
    RADIOACTIVE = "RADIOACTIVE"
    INDUSTRIAL_MINERALS = "INDUSTRIAL_MINERALS"
    GEMSTONES = "GEMSTONES"
    ENERGY_MINERALS = "ENERGY_MINERALS"
    CONSTRUCTION_MATERIALS = "CONSTRUCTION_MATERIALS"
    CHEMICAL_MINERALS = "CHEMICAL_MINERALS"

# Set metadata after class creation
MineralCategory._metadata = {
    "PRECIOUS_METALS": {'description': 'Precious metals', 'annotations': {'examples': 'gold, silver, platinum'}},
    "BASE_METALS": {'description': 'Base metals', 'annotations': {'examples': 'copper, lead, zinc, tin'}},
    "FERROUS_METALS": {'description': 'Ferrous metals', 'annotations': {'examples': 'iron, steel, manganese'}},
    "RARE_EARTH_ELEMENTS": {'description': 'Rare earth elements', 'annotations': {'examples': 'neodymium, dysprosium, cerium', 'count': '17 elements'}},
    "RADIOACTIVE": {'description': 'Radioactive minerals', 'annotations': {'examples': 'uranium, thorium, radium'}},
    "INDUSTRIAL_MINERALS": {'description': 'Industrial minerals', 'annotations': {'examples': 'limestone, gypsum, salt'}},
    "GEMSTONES": {'description': 'Gemstones', 'annotations': {'examples': 'diamond, ruby, emerald'}},
    "ENERGY_MINERALS": {'description': 'Energy minerals', 'annotations': {'examples': 'coal, oil shale, tar sands'}},
    "CONSTRUCTION_MATERIALS": {'description': 'Construction materials', 'annotations': {'examples': 'sand, gravel, crushed stone'}},
    "CHEMICAL_MINERALS": {'description': 'Chemical and fertilizer minerals', 'annotations': {'examples': 'phosphate, potash, sulfur'}},
}

class CriticalMineral(RichEnum):
    """
    Critical minerals essential for economic and national security,
    particularly for clean energy, defense, and technology applications.
    Based on US Geological Survey and EU critical raw materials lists.
    """
    # Enum members
    LITHIUM = "LITHIUM"
    COBALT = "COBALT"
    NICKEL = "NICKEL"
    GRAPHITE = "GRAPHITE"
    MANGANESE = "MANGANESE"
    NEODYMIUM = "NEODYMIUM"
    DYSPROSIUM = "DYSPROSIUM"
    PRASEODYMIUM = "PRASEODYMIUM"
    TERBIUM = "TERBIUM"
    EUROPIUM = "EUROPIUM"
    YTTRIUM = "YTTRIUM"
    CERIUM = "CERIUM"
    LANTHANUM = "LANTHANUM"
    GALLIUM = "GALLIUM"
    GERMANIUM = "GERMANIUM"
    INDIUM = "INDIUM"
    TELLURIUM = "TELLURIUM"
    ARSENIC = "ARSENIC"
    TITANIUM = "TITANIUM"
    VANADIUM = "VANADIUM"
    CHROMIUM = "CHROMIUM"
    TUNGSTEN = "TUNGSTEN"
    TANTALUM = "TANTALUM"
    NIOBIUM = "NIOBIUM"
    ZIRCONIUM = "ZIRCONIUM"
    HAFNIUM = "HAFNIUM"
    PLATINUM = "PLATINUM"
    PALLADIUM = "PALLADIUM"
    RHODIUM = "RHODIUM"
    IRIDIUM = "IRIDIUM"
    RUTHENIUM = "RUTHENIUM"
    ANTIMONY = "ANTIMONY"
    BISMUTH = "BISMUTH"
    BERYLLIUM = "BERYLLIUM"
    MAGNESIUM = "MAGNESIUM"
    ALUMINUM = "ALUMINUM"
    TIN = "TIN"
    FLUORSPAR = "FLUORSPAR"
    BARITE = "BARITE"
    HELIUM = "HELIUM"
    POTASH = "POTASH"
    PHOSPHATE_ROCK = "PHOSPHATE_ROCK"
    SCANDIUM = "SCANDIUM"
    STRONTIUM = "STRONTIUM"

# Set metadata after class creation
CriticalMineral._metadata = {
    "LITHIUM": {'description': 'Lithium (Li) - essential for batteries', 'meaning': 'CHEBI:30145', 'annotations': {'symbol': 'Li', 'atomic_number': 3, 'applications': 'batteries, ceramics, glass'}},
    "COBALT": {'description': 'Cobalt (Co) - battery cathodes and superalloys', 'meaning': 'CHEBI:27638', 'annotations': {'symbol': 'Co', 'atomic_number': 27, 'applications': 'batteries, superalloys, magnets'}},
    "NICKEL": {'description': 'Nickel (Ni) - stainless steel and batteries', 'meaning': 'CHEBI:28112', 'annotations': {'symbol': 'Ni', 'atomic_number': 28, 'applications': 'stainless steel, batteries, alloys'}},
    "GRAPHITE": {'description': 'Graphite - battery anodes and refractories', 'meaning': 'CHEBI:33418', 'annotations': {'formula': 'C', 'applications': 'batteries, lubricants, refractories'}},
    "MANGANESE": {'description': 'Manganese (Mn) - steel and battery production', 'meaning': 'CHEBI:18291', 'annotations': {'symbol': 'Mn', 'atomic_number': 25, 'applications': 'steel, batteries, aluminum alloys'}},
    "NEODYMIUM": {'description': 'Neodymium (Nd) - permanent magnets', 'meaning': 'CHEBI:33372', 'annotations': {'symbol': 'Nd', 'atomic_number': 60, 'category': 'light rare earth', 'applications': 'magnets, lasers, glass'}},
    "DYSPROSIUM": {'description': 'Dysprosium (Dy) - high-performance magnets', 'meaning': 'CHEBI:33377', 'annotations': {'symbol': 'Dy', 'atomic_number': 66, 'category': 'heavy rare earth', 'applications': 'magnets, nuclear control rods'}},
    "PRASEODYMIUM": {'description': 'Praseodymium (Pr) - magnets and alloys', 'meaning': 'CHEBI:49828', 'annotations': {'symbol': 'Pr', 'atomic_number': 59, 'category': 'light rare earth', 'applications': 'magnets, aircraft engines, glass'}},
    "TERBIUM": {'description': 'Terbium (Tb) - phosphors and magnets', 'meaning': 'CHEBI:33376', 'annotations': {'symbol': 'Tb', 'atomic_number': 65, 'category': 'heavy rare earth', 'applications': 'solid-state devices, fuel cells'}},
    "EUROPIUM": {'description': 'Europium (Eu) - phosphors and nuclear control', 'meaning': 'CHEBI:32999', 'annotations': {'symbol': 'Eu', 'atomic_number': 63, 'category': 'heavy rare earth', 'applications': 'LED phosphors, lasers'}},
    "YTTRIUM": {'description': 'Yttrium (Y) - phosphors and ceramics', 'meaning': 'CHEBI:33331', 'annotations': {'symbol': 'Y', 'atomic_number': 39, 'applications': 'LEDs, superconductors, ceramics'}},
    "CERIUM": {'description': 'Cerium (Ce) - catalysts and glass polishing', 'meaning': 'CHEBI:33369', 'annotations': {'symbol': 'Ce', 'atomic_number': 58, 'category': 'light rare earth', 'applications': 'catalysts, glass polishing, alloys'}},
    "LANTHANUM": {'description': 'Lanthanum (La) - catalysts and optics', 'meaning': 'CHEBI:33336', 'annotations': {'symbol': 'La', 'atomic_number': 57, 'category': 'light rare earth', 'applications': 'catalysts, optical glass, batteries'}},
    "GALLIUM": {'description': 'Gallium (Ga) - semiconductors and LEDs', 'meaning': 'CHEBI:49631', 'annotations': {'symbol': 'Ga', 'atomic_number': 31, 'applications': 'semiconductors, LEDs, solar cells'}},
    "GERMANIUM": {'description': 'Germanium (Ge) - fiber optics and infrared', 'meaning': 'CHEBI:30441', 'annotations': {'symbol': 'Ge', 'atomic_number': 32, 'applications': 'fiber optics, infrared optics, solar cells'}},
    "INDIUM": {'description': 'Indium (In) - displays and semiconductors', 'meaning': 'CHEBI:30430', 'annotations': {'symbol': 'In', 'atomic_number': 49, 'applications': 'LCD displays, semiconductors, solar panels'}},
    "TELLURIUM": {'description': 'Tellurium (Te) - solar panels and thermoelectrics', 'meaning': 'CHEBI:30452', 'annotations': {'symbol': 'Te', 'atomic_number': 52, 'applications': 'solar panels, thermoelectrics, alloys'}},
    "ARSENIC": {'description': 'Arsenic (As) - semiconductors and alloys', 'meaning': 'CHEBI:27563', 'annotations': {'symbol': 'As', 'atomic_number': 33, 'applications': 'semiconductors, wood preservatives'}},
    "TITANIUM": {'description': 'Titanium (Ti) - aerospace and defense', 'meaning': 'CHEBI:33341', 'annotations': {'symbol': 'Ti', 'atomic_number': 22, 'applications': 'aerospace, medical implants, pigments'}},
    "VANADIUM": {'description': 'Vanadium (V) - steel alloys and batteries', 'meaning': 'CHEBI:27698', 'annotations': {'symbol': 'V', 'atomic_number': 23, 'applications': 'steel alloys, flow batteries, catalysts'}},
    "CHROMIUM": {'description': 'Chromium (Cr) - stainless steel and alloys', 'meaning': 'CHEBI:28073', 'annotations': {'symbol': 'Cr', 'atomic_number': 24, 'applications': 'stainless steel, superalloys, plating'}},
    "TUNGSTEN": {'description': 'Tungsten (W) - hard metals and electronics', 'meaning': 'CHEBI:27998', 'annotations': {'symbol': 'W', 'atomic_number': 74, 'applications': 'cutting tools, electronics, alloys'}},
    "TANTALUM": {'description': 'Tantalum (Ta) - capacitors and superalloys', 'meaning': 'CHEBI:33348', 'annotations': {'symbol': 'Ta', 'atomic_number': 73, 'applications': 'capacitors, medical implants, superalloys'}},
    "NIOBIUM": {'description': 'Niobium (Nb) - steel alloys and superconductors', 'meaning': 'CHEBI:33344', 'annotations': {'symbol': 'Nb', 'atomic_number': 41, 'applications': 'steel alloys, superconductors, capacitors'}},
    "ZIRCONIUM": {'description': 'Zirconium (Zr) - nuclear and ceramics', 'meaning': 'CHEBI:33342', 'annotations': {'symbol': 'Zr', 'atomic_number': 40, 'applications': 'nuclear reactors, ceramics, alloys'}},
    "HAFNIUM": {'description': 'Hafnium (Hf) - nuclear and semiconductors', 'meaning': 'CHEBI:33343', 'annotations': {'symbol': 'Hf', 'atomic_number': 72, 'applications': 'nuclear control rods, superalloys'}},
    "PLATINUM": {'description': 'Platinum (Pt) - catalysts and electronics', 'meaning': 'CHEBI:33400', 'annotations': {'symbol': 'Pt', 'atomic_number': 78, 'category': 'PGM', 'applications': 'catalysts, jewelry, electronics'}},
    "PALLADIUM": {'description': 'Palladium (Pd) - catalysts and electronics', 'meaning': 'CHEBI:33363', 'annotations': {'symbol': 'Pd', 'atomic_number': 46, 'category': 'PGM', 'applications': 'catalysts, electronics, dentistry'}},
    "RHODIUM": {'description': 'Rhodium (Rh) - catalysts and electronics', 'meaning': 'CHEBI:33359', 'annotations': {'symbol': 'Rh', 'atomic_number': 45, 'category': 'PGM', 'applications': 'catalysts, electronics, glass'}},
    "IRIDIUM": {'description': 'Iridium (Ir) - electronics and catalysts', 'meaning': 'CHEBI:49666', 'annotations': {'symbol': 'Ir', 'atomic_number': 77, 'category': 'PGM', 'applications': 'spark plugs, electronics, catalysts'}},
    "RUTHENIUM": {'description': 'Ruthenium (Ru) - electronics and catalysts', 'meaning': 'CHEBI:30682', 'annotations': {'symbol': 'Ru', 'atomic_number': 44, 'category': 'PGM', 'applications': 'electronics, catalysts, solar cells'}},
    "ANTIMONY": {'description': 'Antimony (Sb) - flame retardants and batteries', 'meaning': 'CHEBI:30513', 'annotations': {'symbol': 'Sb', 'atomic_number': 51, 'applications': 'flame retardants, batteries, alloys'}},
    "BISMUTH": {'description': 'Bismuth (Bi) - pharmaceuticals and alloys', 'meaning': 'CHEBI:33301', 'annotations': {'symbol': 'Bi', 'atomic_number': 83, 'applications': 'pharmaceuticals, cosmetics, alloys'}},
    "BERYLLIUM": {'description': 'Beryllium (Be) - aerospace and defense', 'meaning': 'CHEBI:30501', 'annotations': {'symbol': 'Be', 'atomic_number': 4, 'applications': 'aerospace, defense, nuclear'}},
    "MAGNESIUM": {'description': 'Magnesium (Mg) - lightweight alloys', 'meaning': 'CHEBI:25107', 'annotations': {'symbol': 'Mg', 'atomic_number': 12, 'applications': 'alloys, automotive, aerospace'}},
    "ALUMINUM": {'description': 'Aluminum (Al) - construction and transportation', 'meaning': 'CHEBI:28984', 'annotations': {'symbol': 'Al', 'atomic_number': 13, 'applications': 'construction, transportation, packaging'}},
    "TIN": {'description': 'Tin (Sn) - solders and coatings', 'meaning': 'CHEBI:27007', 'annotations': {'symbol': 'Sn', 'atomic_number': 50, 'applications': 'solders, coatings, alloys'}},
    "FLUORSPAR": {'description': 'Fluorspar (CaF2) - steel and aluminum production', 'meaning': 'CHEBI:35437', 'annotations': {'formula': 'CaF2', 'mineral_name': 'fluorite', 'applications': 'steel, aluminum, refrigerants'}},
    "BARITE": {'description': 'Barite (BaSO4) - drilling and chemicals', 'meaning': 'CHEBI:133326', 'annotations': {'formula': 'BaSO4', 'applications': 'oil drilling, chemicals, radiation shielding'}},
    "HELIUM": {'description': 'Helium (He) - cryogenics and electronics', 'meaning': 'CHEBI:33681', 'annotations': {'symbol': 'He', 'atomic_number': 2, 'applications': 'MRI, semiconductors, aerospace'}},
    "POTASH": {'description': 'Potash (K2O) - fertilizers and chemicals', 'meaning': 'CHEBI:88321', 'annotations': {'formula': 'K2O', 'applications': 'fertilizers, chemicals, glass'}},
    "PHOSPHATE_ROCK": {'description': 'Phosphate rock - fertilizers and chemicals', 'meaning': 'CHEBI:26020', 'annotations': {'applications': 'fertilizers, food additives, chemicals'}},
    "SCANDIUM": {'description': 'Scandium (Sc) - aerospace alloys', 'meaning': 'CHEBI:33330', 'annotations': {'symbol': 'Sc', 'atomic_number': 21, 'applications': 'aerospace alloys, solid oxide fuel cells'}},
    "STRONTIUM": {'description': 'Strontium (Sr) - magnets and pyrotechnics', 'meaning': 'CHEBI:33324', 'annotations': {'symbol': 'Sr', 'atomic_number': 38, 'applications': 'magnets, pyrotechnics, medical'}},
}

class CommonMineral(RichEnum):
    """
    Common minerals extracted through mining
    """
    # Enum members
    GOLD = "GOLD"
    SILVER = "SILVER"
    PLATINUM = "PLATINUM"
    COPPER = "COPPER"
    IRON = "IRON"
    ALUMINUM = "ALUMINUM"
    ZINC = "ZINC"
    LEAD = "LEAD"
    NICKEL = "NICKEL"
    TIN = "TIN"
    COAL = "COAL"
    URANIUM = "URANIUM"
    LIMESTONE = "LIMESTONE"
    SALT = "SALT"
    PHOSPHATE = "PHOSPHATE"
    POTASH = "POTASH"
    LITHIUM = "LITHIUM"
    COBALT = "COBALT"
    DIAMOND = "DIAMOND"

# Set metadata after class creation
CommonMineral._metadata = {
    "GOLD": {'description': 'Gold (Au)', 'meaning': 'CHEBI:29287', 'annotations': {'symbol': 'Au', 'atomic_number': 79}},
    "SILVER": {'description': 'Silver (Ag)', 'meaning': 'CHEBI:30512', 'annotations': {'symbol': 'Ag', 'atomic_number': 47}},
    "PLATINUM": {'description': 'Platinum (Pt)', 'meaning': 'CHEBI:49202', 'annotations': {'symbol': 'Pt', 'atomic_number': 78}},
    "COPPER": {'description': 'Copper (Cu)', 'meaning': 'CHEBI:28694', 'annotations': {'symbol': 'Cu', 'atomic_number': 29}},
    "IRON": {'description': 'Iron (Fe)', 'meaning': 'CHEBI:18248', 'annotations': {'symbol': 'Fe', 'atomic_number': 26}},
    "ALUMINUM": {'description': 'Aluminum (Al)', 'meaning': 'CHEBI:28984', 'annotations': {'symbol': 'Al', 'atomic_number': 13, 'ore': 'bauxite'}},
    "ZINC": {'description': 'Zinc (Zn)', 'meaning': 'CHEBI:27363', 'annotations': {'symbol': 'Zn', 'atomic_number': 30}},
    "LEAD": {'description': 'Lead (Pb)', 'meaning': 'CHEBI:25016', 'annotations': {'symbol': 'Pb', 'atomic_number': 82}},
    "NICKEL": {'description': 'Nickel (Ni)', 'meaning': 'CHEBI:28112', 'annotations': {'symbol': 'Ni', 'atomic_number': 28}},
    "TIN": {'description': 'Tin (Sn)', 'meaning': 'CHEBI:27007', 'annotations': {'symbol': 'Sn', 'atomic_number': 50}},
    "COAL": {'description': 'Coal', 'meaning': 'ENVO:02000091', 'annotations': {'types': 'anthracite, bituminous, lignite'}},
    "URANIUM": {'description': 'Uranium (U)', 'meaning': 'CHEBI:27214', 'annotations': {'symbol': 'U', 'atomic_number': 92}},
    "LIMESTONE": {'description': 'Limestone (CaCO3)', 'meaning': 'ENVO:00002053', 'annotations': {'formula': 'CaCO3', 'use': 'cement, steel production'}},
    "SALT": {'description': 'Salt (NaCl)', 'meaning': 'CHEBI:24866', 'annotations': {'formula': 'NaCl', 'aliases': 'halite, rock salt'}},
    "PHOSPHATE": {'description': 'Phosphate rock', 'meaning': 'CHEBI:26020', 'annotations': {'use': 'fertilizer production'}},
    "POTASH": {'description': 'Potash (K2O)', 'meaning': 'CHEBI:88321', 'annotations': {'formula': 'K2O', 'use': 'fertilizer'}},
    "LITHIUM": {'description': 'Lithium (Li)', 'meaning': 'CHEBI:30145', 'annotations': {'symbol': 'Li', 'atomic_number': 3, 'use': 'batteries'}},
    "COBALT": {'description': 'Cobalt (Co)', 'meaning': 'CHEBI:27638', 'annotations': {'symbol': 'Co', 'atomic_number': 27, 'use': 'batteries, alloys'}},
    "DIAMOND": {'description': 'Diamond (C)', 'meaning': 'CHEBI:33417', 'annotations': {'formula': 'C', 'use': 'gemstone, industrial'}},
}

class MiningEquipment(RichEnum):
    """
    Types of mining equipment
    """
    # Enum members
    DRILL_RIG = "DRILL_RIG"
    JUMBO_DRILL = "JUMBO_DRILL"
    EXCAVATOR = "EXCAVATOR"
    DRAGLINE = "DRAGLINE"
    BUCKET_WHEEL_EXCAVATOR = "BUCKET_WHEEL_EXCAVATOR"
    HAUL_TRUCK = "HAUL_TRUCK"
    LOADER = "LOADER"
    CONVEYOR = "CONVEYOR"
    CRUSHER = "CRUSHER"
    BALL_MILL = "BALL_MILL"
    FLOTATION_CELL = "FLOTATION_CELL"
    CONTINUOUS_MINER = "CONTINUOUS_MINER"
    ROOF_BOLTER = "ROOF_BOLTER"
    SHUTTLE_CAR = "SHUTTLE_CAR"

# Set metadata after class creation
MiningEquipment._metadata = {
    "DRILL_RIG": {'description': 'Drilling rig', 'annotations': {'category': 'drilling'}},
    "JUMBO_DRILL": {'description': 'Jumbo drill', 'annotations': {'category': 'drilling', 'use': 'underground'}},
    "EXCAVATOR": {'description': 'Excavator', 'annotations': {'category': 'excavation'}},
    "DRAGLINE": {'description': 'Dragline excavator', 'annotations': {'category': 'excavation', 'size': 'large-scale'}},
    "BUCKET_WHEEL_EXCAVATOR": {'description': 'Bucket-wheel excavator', 'annotations': {'category': 'excavation', 'use': 'continuous mining'}},
    "HAUL_TRUCK": {'description': 'Haul truck', 'annotations': {'category': 'hauling', 'capacity': 'up to 400 tons'}},
    "LOADER": {'description': 'Loader', 'annotations': {'category': 'loading'}},
    "CONVEYOR": {'description': 'Conveyor system', 'annotations': {'category': 'transport'}},
    "CRUSHER": {'description': 'Crusher', 'annotations': {'category': 'processing', 'types': 'jaw, cone, impact'}},
    "BALL_MILL": {'description': 'Ball mill', 'annotations': {'category': 'processing', 'use': 'grinding'}},
    "FLOTATION_CELL": {'description': 'Flotation cell', 'annotations': {'category': 'processing', 'use': 'mineral separation'}},
    "CONTINUOUS_MINER": {'description': 'Continuous miner', 'annotations': {'category': 'underground'}},
    "ROOF_BOLTER": {'description': 'Roof bolter', 'annotations': {'category': 'underground', 'use': 'support installation'}},
    "SHUTTLE_CAR": {'description': 'Shuttle car', 'annotations': {'category': 'underground transport'}},
}

class OreGrade(RichEnum):
    """
    Classification of ore grades
    """
    # Enum members
    HIGH_GRADE = "HIGH_GRADE"
    MEDIUM_GRADE = "MEDIUM_GRADE"
    LOW_GRADE = "LOW_GRADE"
    MARGINAL = "MARGINAL"
    SUB_ECONOMIC = "SUB_ECONOMIC"
    WASTE = "WASTE"

# Set metadata after class creation
OreGrade._metadata = {
    "HIGH_GRADE": {'description': 'High-grade ore', 'annotations': {'concentration': 'high', 'processing': 'minimal required'}},
    "MEDIUM_GRADE": {'description': 'Medium-grade ore', 'annotations': {'concentration': 'moderate'}},
    "LOW_GRADE": {'description': 'Low-grade ore', 'annotations': {'concentration': 'low', 'processing': 'extensive required'}},
    "MARGINAL": {'description': 'Marginal ore', 'annotations': {'economics': 'borderline profitable'}},
    "SUB_ECONOMIC": {'description': 'Sub-economic ore', 'annotations': {'economics': 'not currently profitable'}},
    "WASTE": {'description': 'Waste rock', 'annotations': {'concentration': 'below cutoff'}},
}

class MiningPhase(RichEnum):
    """
    Phases of mining operations
    """
    # Enum members
    EXPLORATION = "EXPLORATION"
    DEVELOPMENT = "DEVELOPMENT"
    PRODUCTION = "PRODUCTION"
    PROCESSING = "PROCESSING"
    CLOSURE = "CLOSURE"
    RECLAMATION = "RECLAMATION"
    POST_CLOSURE = "POST_CLOSURE"

# Set metadata after class creation
MiningPhase._metadata = {
    "EXPLORATION": {'description': 'Exploration phase', 'annotations': {'activities': 'prospecting, sampling, drilling'}},
    "DEVELOPMENT": {'description': 'Development phase', 'annotations': {'activities': 'infrastructure, access roads'}},
    "PRODUCTION": {'description': 'Production/extraction phase', 'annotations': {'activities': 'active mining'}},
    "PROCESSING": {'description': 'Processing/beneficiation phase', 'annotations': {'activities': 'crushing, milling, concentration'}},
    "CLOSURE": {'description': 'Closure phase', 'annotations': {'activities': 'decommissioning, capping'}},
    "RECLAMATION": {'description': 'Reclamation phase', 'annotations': {'activities': 'restoration, revegetation'}},
    "POST_CLOSURE": {'description': 'Post-closure monitoring', 'annotations': {'activities': 'long-term monitoring'}},
}

class MiningHazard(RichEnum):
    """
    Mining-related hazards and risks
    """
    # Enum members
    CAVE_IN = "CAVE_IN"
    GAS_EXPLOSION = "GAS_EXPLOSION"
    FLOODING = "FLOODING"
    DUST_EXPOSURE = "DUST_EXPOSURE"
    CHEMICAL_EXPOSURE = "CHEMICAL_EXPOSURE"
    RADIATION = "RADIATION"
    NOISE = "NOISE"
    VIBRATION = "VIBRATION"
    HEAT_STRESS = "HEAT_STRESS"
    EQUIPMENT_ACCIDENT = "EQUIPMENT_ACCIDENT"

# Set metadata after class creation
MiningHazard._metadata = {
    "CAVE_IN": {'description': 'Cave-in/roof collapse', 'annotations': {'type': 'structural'}},
    "GAS_EXPLOSION": {'description': 'Gas explosion', 'annotations': {'type': 'chemical', 'gases': 'methane, coal dust'}},
    "FLOODING": {'description': 'Mine flooding', 'annotations': {'type': 'water'}},
    "DUST_EXPOSURE": {'description': 'Dust exposure', 'annotations': {'type': 'respiratory', 'diseases': 'silicosis, pneumoconiosis'}},
    "CHEMICAL_EXPOSURE": {'description': 'Chemical exposure', 'annotations': {'type': 'toxic', 'chemicals': 'mercury, cyanide, acids'}},
    "RADIATION": {'description': 'Radiation exposure', 'annotations': {'type': 'radioactive', 'source': 'uranium, radon'}},
    "NOISE": {'description': 'Noise exposure', 'annotations': {'type': 'physical'}},
    "VIBRATION": {'description': 'Vibration exposure', 'annotations': {'type': 'physical'}},
    "HEAT_STRESS": {'description': 'Heat stress', 'annotations': {'type': 'thermal'}},
    "EQUIPMENT_ACCIDENT": {'description': 'Equipment-related accident', 'annotations': {'type': 'mechanical'}},
}

class EnvironmentalImpact(RichEnum):
    """
    Environmental impacts of mining
    """
    # Enum members
    HABITAT_DESTRUCTION = "HABITAT_DESTRUCTION"
    WATER_POLLUTION = "WATER_POLLUTION"
    AIR_POLLUTION = "AIR_POLLUTION"
    SOIL_CONTAMINATION = "SOIL_CONTAMINATION"
    DEFORESTATION = "DEFORESTATION"
    EROSION = "EROSION"
    ACID_MINE_DRAINAGE = "ACID_MINE_DRAINAGE"
    TAILINGS = "TAILINGS"
    SUBSIDENCE = "SUBSIDENCE"
    BIODIVERSITY_LOSS = "BIODIVERSITY_LOSS"

# Set metadata after class creation
EnvironmentalImpact._metadata = {
    "HABITAT_DESTRUCTION": {'description': 'Habitat destruction', 'meaning': 'ExO:0000012'},
    "WATER_POLLUTION": {'description': 'Water pollution', 'meaning': 'ENVO:02500039', 'annotations': {'types': 'acid mine drainage, heavy metals'}},
    "AIR_POLLUTION": {'description': 'Air pollution', 'meaning': 'ENVO:02500037', 'annotations': {'sources': 'dust, emissions'}},
    "SOIL_CONTAMINATION": {'description': 'Soil contamination', 'meaning': 'ENVO:00002116'},
    "DEFORESTATION": {'description': 'Deforestation', 'meaning': 'ENVO:02500012'},
    "EROSION": {'description': 'Erosion and sedimentation', 'meaning': 'ENVO:01001346'},
    "ACID_MINE_DRAINAGE": {'description': 'Acid mine drainage', 'meaning': 'ENVO:00001997'},
    "TAILINGS": {'description': 'Tailings contamination', 'annotations': {'storage': 'tailings ponds, dams'}},
    "SUBSIDENCE": {'description': 'Ground subsidence', 'annotations': {'cause': 'underground voids'}},
    "BIODIVERSITY_LOSS": {'description': 'Biodiversity loss', 'annotations': {'impact': 'species extinction, ecosystem disruption'}},
}

class ExtractiveIndustryFacilityTypeEnum(RichEnum):
    """
    Types of extractive industry facilities
    """
    # Enum members
    MINING_FACILITY = "MINING_FACILITY"
    WELL_FACILITY = "WELL_FACILITY"
    QUARRY_FACILITY = "QUARRY_FACILITY"

# Set metadata after class creation
ExtractiveIndustryFacilityTypeEnum._metadata = {
    "MINING_FACILITY": {'description': 'A facility where mineral resources are extracted'},
    "WELL_FACILITY": {'description': 'A facility where fluid resources are extracted'},
    "QUARRY_FACILITY": {'description': 'A facility where stone, sand, or gravel are extracted'},
}

class ExtractiveIndustryProductTypeEnum(RichEnum):
    """
    Types of products extracted from extractive industry facilities
    """
    # Enum members
    MINERAL = "MINERAL"
    METAL = "METAL"
    COAL = "COAL"
    OIL = "OIL"
    GAS = "GAS"
    STONE = "STONE"
    SAND = "SAND"
    GRAVEL = "GRAVEL"

# Set metadata after class creation
ExtractiveIndustryProductTypeEnum._metadata = {
    "MINERAL": {'description': 'A solid inorganic substance'},
    "METAL": {'description': 'A solid metallic substance'},
    "COAL": {'description': 'A combustible black or brownish-black sedimentary rock'},
    "OIL": {'description': 'A liquid petroleum resource'},
    "GAS": {'description': 'A gaseous petroleum resource'},
    "STONE": {'description': 'A solid aggregate of minerals'},
    "SAND": {'description': 'A granular material composed of finely divided rock and mineral particles'},
    "GRAVEL": {'description': 'A loose aggregation of rock fragments'},
}

class MiningMethodEnum(RichEnum):
    """
    Methods used for extracting minerals from the earth
    """
    # Enum members
    UNDERGROUND = "UNDERGROUND"
    OPEN_PIT = "OPEN_PIT"
    PLACER = "PLACER"
    IN_SITU = "IN_SITU"

# Set metadata after class creation
MiningMethodEnum._metadata = {
    "UNDERGROUND": {'description': "Extraction occurs beneath the earth's surface"},
    "OPEN_PIT": {'description': "Extraction occurs on the earth's surface"},
    "PLACER": {'description': 'Extraction of valuable minerals from alluvial deposits'},
    "IN_SITU": {'description': 'Extraction without removing the ore from its original location'},
}

class WellTypeEnum(RichEnum):
    """
    Types of wells used for extracting fluid resources
    """
    # Enum members
    OIL = "OIL"
    GAS = "GAS"
    WATER = "WATER"
    INJECTION = "INJECTION"

# Set metadata after class creation
WellTypeEnum._metadata = {
    "OIL": {'description': 'A well that primarily extracts crude oil'},
    "GAS": {'description': 'A well that primarily extracts natural gas'},
    "WATER": {'description': 'A well that extracts water for various purposes'},
    "INJECTION": {'description': 'A well used to inject fluids into underground formations'},
}

class OutcomeTypeEnum(RichEnum):
    """
    Types of prediction outcomes for classification tasks
    """
    # Enum members
    TP = "TP"
    FP = "FP"
    TN = "TN"
    FN = "FN"

# Set metadata after class creation
OutcomeTypeEnum._metadata = {
    "TP": {'description': 'True Positive'},
    "FP": {'description': 'False Positive'},
    "TN": {'description': 'True Negative'},
    "FN": {'description': 'False Negative'},
}

class PersonStatusEnum(RichEnum):
    """
    Vital status of a person (living or deceased)
    """
    # Enum members
    ALIVE = "ALIVE"
    DEAD = "DEAD"
    UNKNOWN = "UNKNOWN"

# Set metadata after class creation
PersonStatusEnum._metadata = {
    "ALIVE": {'description': 'The person is living', 'meaning': 'PATO:0001421'},
    "DEAD": {'description': 'The person is deceased', 'meaning': 'PATO:0001422'},
    "UNKNOWN": {'description': 'The vital status is not known', 'meaning': 'NCIT:C17998'},
}

class MaritalStatusEnum(RichEnum):
    """
    Marital or civil status of a person
    """
    # Enum members
    SINGLE = "SINGLE"
    MARRIED = "MARRIED"
    DIVORCED = "DIVORCED"
    WIDOWED = "WIDOWED"
    SEPARATED = "SEPARATED"
    DOMESTIC_PARTNERSHIP = "DOMESTIC_PARTNERSHIP"
    CIVIL_UNION = "CIVIL_UNION"
    UNKNOWN = "UNKNOWN"
    PREFER_NOT_TO_SAY = "PREFER_NOT_TO_SAY"

# Set metadata after class creation
MaritalStatusEnum._metadata = {
    "SINGLE": {'description': 'Never married', 'meaning': 'NCIT:C51774'},
    "MARRIED": {'description': 'Currently married or in civil partnership', 'meaning': 'NCIT:C51773'},
    "DIVORCED": {'description': 'Marriage legally dissolved', 'meaning': 'NCIT:C51776'},
    "WIDOWED": {'description': 'Marriage ended due to death of spouse', 'meaning': 'NCIT:C51775'},
    "SEPARATED": {'description': 'Living apart from spouse', 'meaning': 'NCIT:C51777'},
    "DOMESTIC_PARTNERSHIP": {'description': 'In a domestic partnership', 'meaning': 'NCIT:C53262'},
    "CIVIL_UNION": {'description': 'In a civil union', 'meaning': 'NCIT:C25188'},
    "UNKNOWN": {'description': 'Marital status not known', 'meaning': 'NCIT:C17998'},
    "PREFER_NOT_TO_SAY": {'description': 'Prefers not to disclose marital status', 'meaning': 'NCIT:C150742'},
}

class EmploymentStatusEnum(RichEnum):
    """
    Employment status of a person
    """
    # Enum members
    EMPLOYED_FULL_TIME = "EMPLOYED_FULL_TIME"
    EMPLOYED_PART_TIME = "EMPLOYED_PART_TIME"
    SELF_EMPLOYED = "SELF_EMPLOYED"
    UNEMPLOYED = "UNEMPLOYED"
    STUDENT = "STUDENT"
    RETIRED = "RETIRED"
    HOMEMAKER = "HOMEMAKER"
    DISABLED = "DISABLED"
    OTHER = "OTHER"
    UNKNOWN = "UNKNOWN"

# Set metadata after class creation
EmploymentStatusEnum._metadata = {
    "EMPLOYED_FULL_TIME": {'description': 'Employed full-time', 'meaning': 'NCIT:C52658'},
    "EMPLOYED_PART_TIME": {'description': 'Employed part-time', 'meaning': 'NCIT:C75562'},
    "SELF_EMPLOYED": {'description': 'Self-employed', 'meaning': 'NCIT:C116000'},
    "UNEMPLOYED": {'description': 'Unemployed', 'meaning': 'NCIT:C75563'},
    "STUDENT": {'description': 'Student', 'meaning': 'NCIT:C75561'},
    "RETIRED": {'description': 'Retired', 'meaning': 'NCIT:C148257'},
    "HOMEMAKER": {'description': 'Homemaker', 'meaning': 'NCIT:C75560'},
    "DISABLED": {'description': 'Unable to work due to disability', 'meaning': 'NCIT:C63367'},
    "OTHER": {'description': 'Other employment status', 'meaning': 'NCIT:C25172'},
    "UNKNOWN": {'description': 'Employment status not known', 'meaning': 'NCIT:C17998'},
}

class MimeType(RichEnum):
    """
    Common MIME types for various file formats
    """
    # Enum members
    APPLICATION_JSON = "APPLICATION_JSON"
    APPLICATION_XML = "APPLICATION_XML"
    APPLICATION_PDF = "APPLICATION_PDF"
    APPLICATION_ZIP = "APPLICATION_ZIP"
    APPLICATION_GZIP = "APPLICATION_GZIP"
    APPLICATION_OCTET_STREAM = "APPLICATION_OCTET_STREAM"
    APPLICATION_X_WWW_FORM_URLENCODED = "APPLICATION_X_WWW_FORM_URLENCODED"
    APPLICATION_VND_MS_EXCEL = "APPLICATION_VND_MS_EXCEL"
    APPLICATION_VND_OPENXMLFORMATS_SPREADSHEET = "APPLICATION_VND_OPENXMLFORMATS_SPREADSHEET"
    APPLICATION_VND_MS_POWERPOINT = "APPLICATION_VND_MS_POWERPOINT"
    APPLICATION_MSWORD = "APPLICATION_MSWORD"
    APPLICATION_VND_OPENXMLFORMATS_DOCUMENT = "APPLICATION_VND_OPENXMLFORMATS_DOCUMENT"
    APPLICATION_JAVASCRIPT = "APPLICATION_JAVASCRIPT"
    APPLICATION_TYPESCRIPT = "APPLICATION_TYPESCRIPT"
    APPLICATION_SQL = "APPLICATION_SQL"
    APPLICATION_GRAPHQL = "APPLICATION_GRAPHQL"
    APPLICATION_LD_JSON = "APPLICATION_LD_JSON"
    APPLICATION_WASM = "APPLICATION_WASM"
    TEXT_PLAIN = "TEXT_PLAIN"
    TEXT_HTML = "TEXT_HTML"
    TEXT_CSS = "TEXT_CSS"
    TEXT_CSV = "TEXT_CSV"
    TEXT_MARKDOWN = "TEXT_MARKDOWN"
    TEXT_YAML = "TEXT_YAML"
    TEXT_X_PYTHON = "TEXT_X_PYTHON"
    TEXT_X_JAVA = "TEXT_X_JAVA"
    TEXT_X_C = "TEXT_X_C"
    TEXT_X_CPP = "TEXT_X_CPP"
    TEXT_X_CSHARP = "TEXT_X_CSHARP"
    TEXT_X_GO = "TEXT_X_GO"
    TEXT_X_RUST = "TEXT_X_RUST"
    TEXT_X_RUBY = "TEXT_X_RUBY"
    TEXT_X_SHELLSCRIPT = "TEXT_X_SHELLSCRIPT"
    IMAGE_JPEG = "IMAGE_JPEG"
    IMAGE_PNG = "IMAGE_PNG"
    IMAGE_GIF = "IMAGE_GIF"
    IMAGE_SVG_XML = "IMAGE_SVG_XML"
    IMAGE_WEBP = "IMAGE_WEBP"
    IMAGE_BMP = "IMAGE_BMP"
    IMAGE_ICO = "IMAGE_ICO"
    IMAGE_TIFF = "IMAGE_TIFF"
    IMAGE_AVIF = "IMAGE_AVIF"
    AUDIO_MPEG = "AUDIO_MPEG"
    AUDIO_WAV = "AUDIO_WAV"
    AUDIO_OGG = "AUDIO_OGG"
    AUDIO_WEBM = "AUDIO_WEBM"
    AUDIO_AAC = "AUDIO_AAC"
    VIDEO_MP4 = "VIDEO_MP4"
    VIDEO_MPEG = "VIDEO_MPEG"
    VIDEO_WEBM = "VIDEO_WEBM"
    VIDEO_OGG = "VIDEO_OGG"
    VIDEO_QUICKTIME = "VIDEO_QUICKTIME"
    VIDEO_AVI = "VIDEO_AVI"
    FONT_WOFF = "FONT_WOFF"
    FONT_WOFF2 = "FONT_WOFF2"
    FONT_TTF = "FONT_TTF"
    FONT_OTF = "FONT_OTF"
    MULTIPART_FORM_DATA = "MULTIPART_FORM_DATA"
    MULTIPART_MIXED = "MULTIPART_MIXED"

# Set metadata after class creation
MimeType._metadata = {
    "APPLICATION_JSON": {'description': 'JSON format', 'meaning': 'iana:application/json'},
    "APPLICATION_XML": {'description': 'XML format', 'meaning': 'iana:application/xml'},
    "APPLICATION_PDF": {'description': 'Adobe Portable Document Format', 'meaning': 'iana:application/pdf'},
    "APPLICATION_ZIP": {'description': 'ZIP archive', 'meaning': 'iana:application/zip'},
    "APPLICATION_GZIP": {'description': 'GZIP compressed archive', 'meaning': 'iana:application/gzip'},
    "APPLICATION_OCTET_STREAM": {'description': 'Binary data', 'meaning': 'iana:application/octet-stream'},
    "APPLICATION_X_WWW_FORM_URLENCODED": {'description': 'Form data encoded', 'meaning': 'iana:application/x-www-form-urlencoded'},
    "APPLICATION_VND_MS_EXCEL": {'description': 'Microsoft Excel', 'meaning': 'iana:application/vnd.ms-excel'},
    "APPLICATION_VND_OPENXMLFORMATS_SPREADSHEET": {'description': 'Microsoft Excel (OpenXML)', 'meaning': 'iana:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'},
    "APPLICATION_VND_MS_POWERPOINT": {'description': 'Microsoft PowerPoint', 'meaning': 'iana:application/vnd.ms-powerpoint'},
    "APPLICATION_MSWORD": {'description': 'Microsoft Word', 'meaning': 'iana:application/msword'},
    "APPLICATION_VND_OPENXMLFORMATS_DOCUMENT": {'description': 'Microsoft Word (OpenXML)', 'meaning': 'iana:application/vnd.openxmlformats-officedocument.wordprocessingml.document'},
    "APPLICATION_JAVASCRIPT": {'description': 'JavaScript', 'meaning': 'iana:application/javascript'},
    "APPLICATION_TYPESCRIPT": {'description': 'TypeScript source code', 'meaning': 'iana:application/typescript'},
    "APPLICATION_SQL": {'description': 'SQL database format', 'meaning': 'iana:application/sql'},
    "APPLICATION_GRAPHQL": {'description': 'GraphQL query language', 'meaning': 'iana:application/graphql'},
    "APPLICATION_LD_JSON": {'description': 'JSON-LD format', 'meaning': 'iana:application/ld+json'},
    "APPLICATION_WASM": {'description': 'WebAssembly binary format', 'meaning': 'iana:application/wasm'},
    "TEXT_PLAIN": {'description': 'Plain text', 'meaning': 'iana:text/plain'},
    "TEXT_HTML": {'description': 'HTML document', 'meaning': 'iana:text/html'},
    "TEXT_CSS": {'description': 'Cascading Style Sheets', 'meaning': 'iana:text/css'},
    "TEXT_CSV": {'description': 'Comma-separated values', 'meaning': 'iana:text/csv'},
    "TEXT_MARKDOWN": {'description': 'Markdown format', 'meaning': 'iana:text/markdown'},
    "TEXT_YAML": {'description': 'YAML format', 'meaning': 'iana:text/yaml'},
    "TEXT_X_PYTHON": {'description': 'Python source code', 'meaning': 'iana:text/x-python'},
    "TEXT_X_JAVA": {'description': 'Java source code', 'meaning': 'iana:text/x-java-source'},
    "TEXT_X_C": {'description': 'C source code', 'meaning': 'iana:text/x-c'},
    "TEXT_X_CPP": {'description': 'C++ source code', 'meaning': 'iana:text/x-c++'},
    "TEXT_X_CSHARP": {'description': 'C# source code', 'meaning': 'iana:text/x-csharp'},
    "TEXT_X_GO": {'description': 'Go source code', 'meaning': 'iana:text/x-go'},
    "TEXT_X_RUST": {'description': 'Rust source code', 'meaning': 'iana:text/x-rust'},
    "TEXT_X_RUBY": {'description': 'Ruby source code', 'meaning': 'iana:text/x-ruby'},
    "TEXT_X_SHELLSCRIPT": {'description': 'Shell script', 'meaning': 'iana:text/x-shellscript'},
    "IMAGE_JPEG": {'description': 'JPEG image', 'meaning': 'iana:image/jpeg'},
    "IMAGE_PNG": {'description': 'PNG image', 'meaning': 'iana:image/png'},
    "IMAGE_GIF": {'description': 'GIF image', 'meaning': 'iana:image/gif'},
    "IMAGE_SVG_XML": {'description': 'SVG vector image', 'meaning': 'iana:image/svg+xml'},
    "IMAGE_WEBP": {'description': 'WebP image', 'meaning': 'iana:image/webp'},
    "IMAGE_BMP": {'description': 'Bitmap image', 'meaning': 'iana:image/bmp'},
    "IMAGE_ICO": {'description': 'Icon format', 'meaning': 'iana:image/vnd.microsoft.icon'},
    "IMAGE_TIFF": {'description': 'TIFF image', 'meaning': 'iana:image/tiff'},
    "IMAGE_AVIF": {'description': 'AVIF image format', 'meaning': 'iana:image/avif'},
    "AUDIO_MPEG": {'description': 'MP3 audio', 'meaning': 'iana:audio/mpeg'},
    "AUDIO_WAV": {'description': 'WAV audio', 'meaning': 'iana:audio/wav'},
    "AUDIO_OGG": {'description': 'OGG audio', 'meaning': 'iana:audio/ogg'},
    "AUDIO_WEBM": {'description': 'WebM audio', 'meaning': 'iana:audio/webm'},
    "AUDIO_AAC": {'description': 'AAC audio', 'meaning': 'iana:audio/aac'},
    "VIDEO_MP4": {'description': 'MP4 video', 'meaning': 'iana:video/mp4'},
    "VIDEO_MPEG": {'description': 'MPEG video', 'meaning': 'iana:video/mpeg'},
    "VIDEO_WEBM": {'description': 'WebM video', 'meaning': 'iana:video/webm'},
    "VIDEO_OGG": {'description': 'OGG video', 'meaning': 'iana:video/ogg'},
    "VIDEO_QUICKTIME": {'description': 'QuickTime video', 'meaning': 'iana:video/quicktime'},
    "VIDEO_AVI": {'description': 'AVI video', 'meaning': 'iana:video/x-msvideo'},
    "FONT_WOFF": {'description': 'Web Open Font Format', 'meaning': 'iana:font/woff'},
    "FONT_WOFF2": {'description': 'Web Open Font Format 2', 'meaning': 'iana:font/woff2'},
    "FONT_TTF": {'description': 'TrueType Font', 'meaning': 'iana:font/ttf'},
    "FONT_OTF": {'description': 'OpenType Font', 'meaning': 'iana:font/otf'},
    "MULTIPART_FORM_DATA": {'description': 'Form data with file upload', 'meaning': 'iana:multipart/form-data'},
    "MULTIPART_MIXED": {'description': 'Mixed multipart message', 'meaning': 'iana:multipart/mixed'},
}

class MimeTypeCategory(RichEnum):
    """
    Categories of MIME types
    """
    # Enum members
    APPLICATION = "APPLICATION"
    TEXT = "TEXT"
    IMAGE = "IMAGE"
    AUDIO = "AUDIO"
    VIDEO = "VIDEO"
    FONT = "FONT"
    MULTIPART = "MULTIPART"
    MESSAGE = "MESSAGE"
    MODEL = "MODEL"

# Set metadata after class creation
MimeTypeCategory._metadata = {
    "APPLICATION": {'description': 'Application data'},
    "TEXT": {'description': 'Text documents'},
    "IMAGE": {'description': 'Image files'},
    "AUDIO": {'description': 'Audio files'},
    "VIDEO": {'description': 'Video files'},
    "FONT": {'description': 'Font files'},
    "MULTIPART": {'description': 'Multipart messages'},
    "MESSAGE": {'description': 'Message formats'},
    "MODEL": {'description': '3D models and similar'},
}

class TextCharset(RichEnum):
    """
    Character encodings for text content
    """
    # Enum members
    UTF_8 = "UTF_8"
    UTF_16 = "UTF_16"
    UTF_32 = "UTF_32"
    ASCII = "ASCII"
    ISO_8859_1 = "ISO_8859_1"
    ISO_8859_2 = "ISO_8859_2"
    WINDOWS_1252 = "WINDOWS_1252"
    GB2312 = "GB2312"
    SHIFT_JIS = "SHIFT_JIS"
    EUC_KR = "EUC_KR"
    BIG5 = "BIG5"

# Set metadata after class creation
TextCharset._metadata = {
    "UTF_8": {'description': 'UTF-8 Unicode encoding'},
    "UTF_16": {'description': 'UTF-16 Unicode encoding'},
    "UTF_32": {'description': 'UTF-32 Unicode encoding'},
    "ASCII": {'description': 'ASCII encoding'},
    "ISO_8859_1": {'description': 'ISO-8859-1 (Latin-1) encoding'},
    "ISO_8859_2": {'description': 'ISO-8859-2 (Latin-2) encoding'},
    "WINDOWS_1252": {'description': 'Windows-1252 encoding'},
    "GB2312": {'description': 'Simplified Chinese encoding'},
    "SHIFT_JIS": {'description': 'Japanese encoding'},
    "EUC_KR": {'description': 'Korean encoding'},
    "BIG5": {'description': 'Traditional Chinese encoding'},
}

class CompressionType(RichEnum):
    """
    Compression types used with Content-Encoding
    """
    # Enum members
    GZIP = "GZIP"
    DEFLATE = "DEFLATE"
    BR = "BR"
    COMPRESS = "COMPRESS"
    IDENTITY = "IDENTITY"

# Set metadata after class creation
CompressionType._metadata = {
    "GZIP": {'description': 'GZIP compression'},
    "DEFLATE": {'description': 'DEFLATE compression'},
    "BR": {'description': 'Brotli compression'},
    "COMPRESS": {'description': 'Unix compress'},
    "IDENTITY": {'description': 'No compression'},
}

class StateOfMatterEnum(RichEnum):
    """
    The physical state or phase of matter
    """
    # Enum members
    SOLID = "SOLID"
    LIQUID = "LIQUID"
    GAS = "GAS"
    PLASMA = "PLASMA"
    BOSE_EINSTEIN_CONDENSATE = "BOSE_EINSTEIN_CONDENSATE"
    FERMIONIC_CONDENSATE = "FERMIONIC_CONDENSATE"
    SUPERCRITICAL_FLUID = "SUPERCRITICAL_FLUID"
    SUPERFLUID = "SUPERFLUID"
    SUPERSOLID = "SUPERSOLID"
    QUARK_GLUON_PLASMA = "QUARK_GLUON_PLASMA"

# Set metadata after class creation
StateOfMatterEnum._metadata = {
    "SOLID": {'description': 'A state of matter where particles are closely packed together with fixed positions', 'meaning': 'AFO:AFQ_0000112'},
    "LIQUID": {'description': 'A nearly incompressible fluid that conforms to the shape of its container', 'meaning': 'AFO:AFQ_0000113'},
    "GAS": {'description': 'A compressible fluid that expands to fill its container', 'meaning': 'AFO:AFQ_0000114'},
    "PLASMA": {'description': 'An ionized gas with freely moving charged particles', 'meaning': 'AFO:AFQ_0000115'},
    "BOSE_EINSTEIN_CONDENSATE": {'description': 'A state of matter formed at extremely low temperatures where particles occupy the same quantum state'},
    "FERMIONIC_CONDENSATE": {'description': 'A superfluid phase formed by fermionic particles at extremely low temperatures'},
    "SUPERCRITICAL_FLUID": {'description': 'A state where distinct liquid and gas phases do not exist'},
    "SUPERFLUID": {'description': 'A phase of matter with zero viscosity'},
    "SUPERSOLID": {'description': 'A spatially ordered material with superfluid properties'},
    "QUARK_GLUON_PLASMA": {'description': 'An extremely hot phase where quarks and gluons are not confined'},
}

class AirPollutantEnum(RichEnum):
    """
    Common air pollutants and air quality indicators
    """
    # Enum members
    PM2_5 = "PM2_5"
    PM10 = "PM10"
    ULTRAFINE_PARTICLES = "ULTRAFINE_PARTICLES"
    OZONE = "OZONE"
    NITROGEN_DIOXIDE = "NITROGEN_DIOXIDE"
    SULFUR_DIOXIDE = "SULFUR_DIOXIDE"
    CARBON_MONOXIDE = "CARBON_MONOXIDE"
    LEAD = "LEAD"
    BENZENE = "BENZENE"
    FORMALDEHYDE = "FORMALDEHYDE"
    VOLATILE_ORGANIC_COMPOUNDS = "VOLATILE_ORGANIC_COMPOUNDS"
    POLYCYCLIC_AROMATIC_HYDROCARBONS = "POLYCYCLIC_AROMATIC_HYDROCARBONS"

# Set metadata after class creation
AirPollutantEnum._metadata = {
    "PM2_5": {'description': 'Fine particulate matter with diameter less than 2.5 micrometers', 'meaning': 'ENVO:01000415'},
    "PM10": {'description': 'Respirable particulate matter with diameter less than 10 micrometers', 'meaning': 'ENVO:01000405'},
    "ULTRAFINE_PARTICLES": {'description': 'Ultrafine particles with diameter less than 100 nanometers', 'meaning': 'ENVO:01000416'},
    "OZONE": {'description': 'Ground-level ozone (O3)', 'meaning': 'CHEBI:25812'},
    "NITROGEN_DIOXIDE": {'description': 'Nitrogen dioxide (NO2)', 'meaning': 'CHEBI:33101'},
    "SULFUR_DIOXIDE": {'description': 'Sulfur dioxide (SO2)', 'meaning': 'CHEBI:18422'},
    "CARBON_MONOXIDE": {'description': 'Carbon monoxide (CO)', 'meaning': 'CHEBI:17245'},
    "LEAD": {'description': 'Airborne lead particles', 'meaning': 'NCIT:C44396'},
    "BENZENE": {'description': 'Benzene vapor', 'meaning': 'CHEBI:16716'},
    "FORMALDEHYDE": {'description': 'Formaldehyde gas', 'meaning': 'CHEBI:16842'},
    "VOLATILE_ORGANIC_COMPOUNDS": {'description': 'Volatile organic compounds (VOCs)', 'meaning': 'CHEBI:134179'},
    "POLYCYCLIC_AROMATIC_HYDROCARBONS": {'description': 'Polycyclic aromatic hydrocarbons (PAHs)', 'meaning': 'CHEBI:33848'},
}

class PesticideTypeEnum(RichEnum):
    """
    Categories of pesticides by target organism or chemical class
    """
    # Enum members
    HERBICIDE = "HERBICIDE"
    INSECTICIDE = "INSECTICIDE"
    FUNGICIDE = "FUNGICIDE"
    RODENTICIDE = "RODENTICIDE"
    ORGANOPHOSPHATE = "ORGANOPHOSPHATE"
    ORGANOCHLORINE = "ORGANOCHLORINE"
    PYRETHROID = "PYRETHROID"
    CARBAMATE = "CARBAMATE"
    NEONICOTINOID = "NEONICOTINOID"
    GLYPHOSATE = "GLYPHOSATE"

# Set metadata after class creation
PesticideTypeEnum._metadata = {
    "HERBICIDE": {'description': 'Chemical used to kill unwanted plants', 'meaning': 'CHEBI:24527'},
    "INSECTICIDE": {'description': 'Chemical used to kill insects', 'meaning': 'CHEBI:24852'},
    "FUNGICIDE": {'description': 'Chemical used to kill fungi', 'meaning': 'CHEBI:24127'},
    "RODENTICIDE": {'description': 'Chemical used to kill rodents', 'meaning': 'CHEBI:33288'},
    "ORGANOPHOSPHATE": {'description': 'Organophosphate pesticide', 'meaning': 'CHEBI:25708'},
    "ORGANOCHLORINE": {'description': 'Organochlorine pesticide', 'meaning': 'CHEBI:25705'},
    "PYRETHROID": {'description': 'Pyrethroid pesticide', 'meaning': 'CHEBI:26413'},
    "CARBAMATE": {'description': 'Carbamate pesticide', 'meaning': 'CHEBI:38461'},
    "NEONICOTINOID": {'description': 'Neonicotinoid pesticide', 'meaning': 'CHEBI:25540'},
    "GLYPHOSATE": {'description': 'Glyphosate herbicide', 'meaning': 'CHEBI:27744'},
}

class HeavyMetalEnum(RichEnum):
    """
    Heavy metals of environmental health concern
    """
    # Enum members
    LEAD = "LEAD"
    MERCURY = "MERCURY"
    CADMIUM = "CADMIUM"
    ARSENIC = "ARSENIC"
    CHROMIUM = "CHROMIUM"
    NICKEL = "NICKEL"
    COPPER = "COPPER"
    ZINC = "ZINC"
    MANGANESE = "MANGANESE"
    COBALT = "COBALT"

# Set metadata after class creation
HeavyMetalEnum._metadata = {
    "LEAD": {'description': 'Lead (Pb)', 'meaning': 'NCIT:C44396'},
    "MERCURY": {'description': 'Mercury (Hg)', 'meaning': 'NCIT:C66842'},
    "CADMIUM": {'description': 'Cadmium (Cd)', 'meaning': 'NCIT:C44348'},
    "ARSENIC": {'description': 'Arsenic (As)', 'meaning': 'NCIT:C28131'},
    "CHROMIUM": {'description': 'Chromium (Cr)', 'meaning': 'NCIT:C370'},
    "NICKEL": {'description': 'Nickel (Ni)', 'meaning': 'CHEBI:28112'},
    "COPPER": {'description': 'Copper (Cu)', 'meaning': 'CHEBI:28694'},
    "ZINC": {'description': 'Zinc (Zn)', 'meaning': 'CHEBI:27363'},
    "MANGANESE": {'description': 'Manganese (Mn)', 'meaning': 'CHEBI:18291'},
    "COBALT": {'description': 'Cobalt (Co)', 'meaning': 'CHEBI:27638'},
}

class ExposureRouteEnum(RichEnum):
    """
    Routes by which exposure to environmental agents occurs
    """
    # Enum members
    INHALATION = "INHALATION"
    INGESTION = "INGESTION"
    DERMAL = "DERMAL"
    INJECTION = "INJECTION"
    TRANSPLACENTAL = "TRANSPLACENTAL"
    OCULAR = "OCULAR"
    MULTIPLE_ROUTES = "MULTIPLE_ROUTES"

# Set metadata after class creation
ExposureRouteEnum._metadata = {
    "INHALATION": {'description': 'Exposure through breathing', 'meaning': 'NCIT:C38284'},
    "INGESTION": {'description': 'Exposure through eating or drinking', 'meaning': 'NCIT:C38288'},
    "DERMAL": {'description': 'Exposure through skin contact', 'meaning': 'NCIT:C38675'},
    "INJECTION": {'description': 'Exposure through injection', 'meaning': 'NCIT:C38276'},
    "TRANSPLACENTAL": {'description': 'Exposure through placental transfer', 'meaning': 'NCIT:C38307'},
    "OCULAR": {'description': 'Exposure through the eyes', 'meaning': 'NCIT:C38287'},
    "MULTIPLE_ROUTES": {'description': 'Exposure through multiple pathways'},
}

class ExposureSourceEnum(RichEnum):
    """
    Common sources of environmental exposures
    """
    # Enum members
    AMBIENT_AIR = "AMBIENT_AIR"
    INDOOR_AIR = "INDOOR_AIR"
    DRINKING_WATER = "DRINKING_WATER"
    SOIL = "SOIL"
    FOOD = "FOOD"
    OCCUPATIONAL = "OCCUPATIONAL"
    CONSUMER_PRODUCTS = "CONSUMER_PRODUCTS"
    INDUSTRIAL_EMISSIONS = "INDUSTRIAL_EMISSIONS"
    AGRICULTURAL = "AGRICULTURAL"
    TRAFFIC = "TRAFFIC"
    TOBACCO_SMOKE = "TOBACCO_SMOKE"
    CONSTRUCTION = "CONSTRUCTION"
    MINING = "MINING"

# Set metadata after class creation
ExposureSourceEnum._metadata = {
    "AMBIENT_AIR": {'description': 'Outdoor air pollution'},
    "INDOOR_AIR": {'description': 'Indoor air pollution'},
    "DRINKING_WATER": {'description': 'Contaminated drinking water'},
    "SOIL": {'description': 'Contaminated soil', 'meaning': 'ENVO:00002116'},
    "FOOD": {'description': 'Contaminated food'},
    "OCCUPATIONAL": {'description': 'Workplace exposure', 'meaning': 'ENVO:03501332'},
    "CONSUMER_PRODUCTS": {'description': 'Household and consumer products'},
    "INDUSTRIAL_EMISSIONS": {'description': 'Industrial facility emissions'},
    "AGRICULTURAL": {'description': 'Agricultural activities'},
    "TRAFFIC": {'description': 'Traffic-related pollution'},
    "TOBACCO_SMOKE": {'description': 'Active or passive tobacco smoke exposure', 'meaning': 'NCIT:C17140'},
    "CONSTRUCTION": {'description': 'Construction-related exposure'},
    "MINING": {'description': 'Mining-related exposure'},
}

class WaterContaminantEnum(RichEnum):
    """
    Common water contaminants
    """
    # Enum members
    LEAD = "LEAD"
    ARSENIC = "ARSENIC"
    NITRATES = "NITRATES"
    FLUORIDE = "FLUORIDE"
    CHLORINE = "CHLORINE"
    BACTERIA = "BACTERIA"
    VIRUSES = "VIRUSES"
    PARASITES = "PARASITES"
    PFAS = "PFAS"
    MICROPLASTICS = "MICROPLASTICS"
    PHARMACEUTICALS = "PHARMACEUTICALS"
    PESTICIDES = "PESTICIDES"

# Set metadata after class creation
WaterContaminantEnum._metadata = {
    "LEAD": {'description': 'Lead contamination', 'meaning': 'NCIT:C44396'},
    "ARSENIC": {'description': 'Arsenic contamination', 'meaning': 'NCIT:C28131'},
    "NITRATES": {'description': 'Nitrate contamination', 'meaning': 'CHEBI:17632'},
    "FLUORIDE": {'description': 'Fluoride levels', 'meaning': 'CHEBI:17051'},
    "CHLORINE": {'description': 'Chlorine and chlorination byproducts', 'meaning': 'NCIT:C28140'},
    "BACTERIA": {'description': 'Bacterial contamination', 'meaning': 'NCIT:C14187'},
    "VIRUSES": {'description': 'Viral contamination', 'meaning': 'NCIT:C14283'},
    "PARASITES": {'description': 'Parasitic contamination', 'meaning': 'NCIT:C28176'},
    "PFAS": {'description': 'Per- and polyfluoroalkyl substances', 'meaning': 'CHEBI:172397'},
    "MICROPLASTICS": {'description': 'Microplastic particles', 'meaning': 'ENVO:01000944'},
    "PHARMACEUTICALS": {'description': 'Pharmaceutical residues', 'meaning': 'CHEBI:52217'},
    "PESTICIDES": {'description': 'Pesticide residues', 'meaning': 'CHEBI:25944'},
}

class EndocrineDisruptorEnum(RichEnum):
    """
    Common endocrine disrupting chemicals
    """
    # Enum members
    BPA = "BPA"
    PHTHALATES = "PHTHALATES"
    PFAS = "PFAS"
    PCB = "PCB"
    DIOXINS = "DIOXINS"
    DDT = "DDT"
    PARABENS = "PARABENS"
    TRICLOSAN = "TRICLOSAN"
    FLAME_RETARDANTS = "FLAME_RETARDANTS"

# Set metadata after class creation
EndocrineDisruptorEnum._metadata = {
    "BPA": {'description': 'Bisphenol A', 'meaning': 'CHEBI:33216'},
    "PHTHALATES": {'description': 'Phthalates', 'meaning': 'CHEBI:26092'},
    "PFAS": {'description': 'Per- and polyfluoroalkyl substances', 'meaning': 'CHEBI:172397'},
    "PCB": {'description': 'Polychlorinated biphenyls', 'meaning': 'CHEBI:53156'},
    "DIOXINS": {'description': 'Dioxins', 'meaning': 'NCIT:C442'},
    "DDT": {'description': 'Dichlorodiphenyltrichloroethane and metabolites', 'meaning': 'CHEBI:16130'},
    "PARABENS": {'description': 'Parabens', 'meaning': 'CHEBI:85122'},
    "TRICLOSAN": {'description': 'Triclosan', 'meaning': 'CHEBI:164200'},
    "FLAME_RETARDANTS": {'description': 'Brominated flame retardants', 'meaning': 'CHEBI:172368'},
}

class ExposureDurationEnum(RichEnum):
    """
    Duration categories for environmental exposures
    """
    # Enum members
    ACUTE = "ACUTE"
    SUBACUTE = "SUBACUTE"
    SUBCHRONIC = "SUBCHRONIC"
    CHRONIC = "CHRONIC"
    LIFETIME = "LIFETIME"
    PRENATAL = "PRENATAL"
    POSTNATAL = "POSTNATAL"
    DEVELOPMENTAL = "DEVELOPMENTAL"

# Set metadata after class creation
ExposureDurationEnum._metadata = {
    "ACUTE": {'description': 'Single or short-term exposure (hours to days)'},
    "SUBACUTE": {'description': 'Repeated exposure over weeks'},
    "SUBCHRONIC": {'description': 'Repeated exposure over months'},
    "CHRONIC": {'description': 'Long-term exposure over years'},
    "LIFETIME": {'description': 'Exposure over entire lifetime'},
    "PRENATAL": {'description': 'Exposure during pregnancy'},
    "POSTNATAL": {'description': 'Exposure after birth'},
    "DEVELOPMENTAL": {'description': 'Exposure during critical developmental periods'},
}

class CountryCodeISO2Enum(RichEnum):
    """
    ISO 3166-1 alpha-2 country codes (2-letter codes)
    """
    # Enum members
    US = "US"
    CA = "CA"
    MX = "MX"
    GB = "GB"
    FR = "FR"
    DE = "DE"
    IT = "IT"
    ES = "ES"
    PT = "PT"
    NL = "NL"
    BE = "BE"
    CH = "CH"
    AT = "AT"
    SE = "SE"
    FALSE = "False"
    DK = "DK"
    FI = "FI"
    PL = "PL"
    RU = "RU"
    UA = "UA"
    CN = "CN"
    JP = "JP"
    KR = "KR"
    IN = "IN"
    AU = "AU"
    NZ = "NZ"
    BR = "BR"
    AR = "AR"
    CL = "CL"
    CO = "CO"
    PE = "PE"
    VE = "VE"
    ZA = "ZA"
    EG = "EG"
    NG = "NG"
    KE = "KE"
    IL = "IL"
    SA = "SA"
    AE = "AE"
    TR = "TR"
    GR = "GR"
    IE = "IE"
    SG = "SG"
    MY = "MY"
    TH = "TH"
    ID = "ID"
    PH = "PH"
    VN = "VN"
    PK = "PK"
    BD = "BD"

# Set metadata after class creation
CountryCodeISO2Enum._metadata = {
    "US": {'description': 'United States of America'},
    "CA": {'description': 'Canada'},
    "MX": {'description': 'Mexico'},
    "GB": {'description': 'United Kingdom'},
    "FR": {'description': 'France'},
    "DE": {'description': 'Germany'},
    "IT": {'description': 'Italy'},
    "ES": {'description': 'Spain'},
    "PT": {'description': 'Portugal'},
    "NL": {'description': 'Netherlands'},
    "BE": {'description': 'Belgium'},
    "CH": {'description': 'Switzerland'},
    "AT": {'description': 'Austria'},
    "SE": {'description': 'Sweden'},
    "FALSE": {'description': 'Norway'},
    "DK": {'description': 'Denmark'},
    "FI": {'description': 'Finland'},
    "PL": {'description': 'Poland'},
    "RU": {'description': 'Russian Federation'},
    "UA": {'description': 'Ukraine'},
    "CN": {'description': 'China'},
    "JP": {'description': 'Japan'},
    "KR": {'description': 'South Korea'},
    "IN": {'description': 'India'},
    "AU": {'description': 'Australia'},
    "NZ": {'description': 'New Zealand'},
    "BR": {'description': 'Brazil'},
    "AR": {'description': 'Argentina'},
    "CL": {'description': 'Chile'},
    "CO": {'description': 'Colombia'},
    "PE": {'description': 'Peru'},
    "VE": {'description': 'Venezuela'},
    "ZA": {'description': 'South Africa'},
    "EG": {'description': 'Egypt'},
    "NG": {'description': 'Nigeria'},
    "KE": {'description': 'Kenya'},
    "IL": {'description': 'Israel'},
    "SA": {'description': 'Saudi Arabia'},
    "AE": {'description': 'United Arab Emirates'},
    "TR": {'description': 'Turkey'},
    "GR": {'description': 'Greece'},
    "IE": {'description': 'Ireland'},
    "SG": {'description': 'Singapore'},
    "MY": {'description': 'Malaysia'},
    "TH": {'description': 'Thailand'},
    "ID": {'description': 'Indonesia'},
    "PH": {'description': 'Philippines'},
    "VN": {'description': 'Vietnam'},
    "PK": {'description': 'Pakistan'},
    "BD": {'description': 'Bangladesh'},
}

class CountryCodeISO3Enum(RichEnum):
    """
    ISO 3166-1 alpha-3 country codes (3-letter codes)
    """
    # Enum members
    USA = "USA"
    CAN = "CAN"
    MEX = "MEX"
    GBR = "GBR"
    FRA = "FRA"
    DEU = "DEU"
    ITA = "ITA"
    ESP = "ESP"
    PRT = "PRT"
    NLD = "NLD"
    BEL = "BEL"
    CHE = "CHE"
    AUT = "AUT"
    SWE = "SWE"
    NOR = "NOR"
    DNK = "DNK"
    FIN = "FIN"
    POL = "POL"
    RUS = "RUS"
    UKR = "UKR"
    CHN = "CHN"
    JPN = "JPN"
    KOR = "KOR"
    IND = "IND"
    AUS = "AUS"
    NZL = "NZL"
    BRA = "BRA"
    ARG = "ARG"
    CHL = "CHL"
    COL = "COL"

# Set metadata after class creation
CountryCodeISO3Enum._metadata = {
    "USA": {'description': 'United States of America'},
    "CAN": {'description': 'Canada'},
    "MEX": {'description': 'Mexico'},
    "GBR": {'description': 'United Kingdom'},
    "FRA": {'description': 'France'},
    "DEU": {'description': 'Germany'},
    "ITA": {'description': 'Italy'},
    "ESP": {'description': 'Spain'},
    "PRT": {'description': 'Portugal'},
    "NLD": {'description': 'Netherlands'},
    "BEL": {'description': 'Belgium'},
    "CHE": {'description': 'Switzerland'},
    "AUT": {'description': 'Austria'},
    "SWE": {'description': 'Sweden'},
    "NOR": {'description': 'Norway'},
    "DNK": {'description': 'Denmark'},
    "FIN": {'description': 'Finland'},
    "POL": {'description': 'Poland'},
    "RUS": {'description': 'Russian Federation'},
    "UKR": {'description': 'Ukraine'},
    "CHN": {'description': 'China'},
    "JPN": {'description': 'Japan'},
    "KOR": {'description': 'South Korea'},
    "IND": {'description': 'India'},
    "AUS": {'description': 'Australia'},
    "NZL": {'description': 'New Zealand'},
    "BRA": {'description': 'Brazil'},
    "ARG": {'description': 'Argentina'},
    "CHL": {'description': 'Chile'},
    "COL": {'description': 'Colombia'},
}

class USStateCodeEnum(RichEnum):
    """
    United States state and territory codes
    """
    # Enum members
    AL = "AL"
    AK = "AK"
    AZ = "AZ"
    AR = "AR"
    CA = "CA"
    CO = "CO"
    CT = "CT"
    DE = "DE"
    FL = "FL"
    GA = "GA"
    HI = "HI"
    ID = "ID"
    IL = "IL"
    IN = "IN"
    IA = "IA"
    KS = "KS"
    KY = "KY"
    LA = "LA"
    ME = "ME"
    MD = "MD"
    MA = "MA"
    MI = "MI"
    MN = "MN"
    MS = "MS"
    MO = "MO"
    MT = "MT"
    NE = "NE"
    NV = "NV"
    NH = "NH"
    NJ = "NJ"
    NM = "NM"
    NY = "NY"
    NC = "NC"
    ND = "ND"
    OH = "OH"
    OK = "OK"
    OR = "OR"
    PA = "PA"
    RI = "RI"
    SC = "SC"
    SD = "SD"
    TN = "TN"
    TX = "TX"
    UT = "UT"
    VT = "VT"
    VA = "VA"
    WA = "WA"
    WV = "WV"
    WI = "WI"
    WY = "WY"
    DC = "DC"
    PR = "PR"
    VI = "VI"
    GU = "GU"
    AS = "AS"
    MP = "MP"

# Set metadata after class creation
USStateCodeEnum._metadata = {
    "AL": {'description': 'Alabama'},
    "AK": {'description': 'Alaska'},
    "AZ": {'description': 'Arizona'},
    "AR": {'description': 'Arkansas'},
    "CA": {'description': 'California'},
    "CO": {'description': 'Colorado'},
    "CT": {'description': 'Connecticut'},
    "DE": {'description': 'Delaware'},
    "FL": {'description': 'Florida'},
    "GA": {'description': 'Georgia'},
    "HI": {'description': 'Hawaii'},
    "ID": {'description': 'Idaho'},
    "IL": {'description': 'Illinois'},
    "IN": {'description': 'Indiana'},
    "IA": {'description': 'Iowa'},
    "KS": {'description': 'Kansas'},
    "KY": {'description': 'Kentucky'},
    "LA": {'description': 'Louisiana'},
    "ME": {'description': 'Maine'},
    "MD": {'description': 'Maryland'},
    "MA": {'description': 'Massachusetts'},
    "MI": {'description': 'Michigan'},
    "MN": {'description': 'Minnesota'},
    "MS": {'description': 'Mississippi'},
    "MO": {'description': 'Missouri'},
    "MT": {'description': 'Montana'},
    "NE": {'description': 'Nebraska'},
    "NV": {'description': 'Nevada'},
    "NH": {'description': 'New Hampshire'},
    "NJ": {'description': 'New Jersey'},
    "NM": {'description': 'New Mexico'},
    "NY": {'description': 'New York'},
    "NC": {'description': 'North Carolina'},
    "ND": {'description': 'North Dakota'},
    "OH": {'description': 'Ohio'},
    "OK": {'description': 'Oklahoma'},
    "OR": {'description': 'Oregon'},
    "PA": {'description': 'Pennsylvania'},
    "RI": {'description': 'Rhode Island'},
    "SC": {'description': 'South Carolina'},
    "SD": {'description': 'South Dakota'},
    "TN": {'description': 'Tennessee'},
    "TX": {'description': 'Texas'},
    "UT": {'description': 'Utah'},
    "VT": {'description': 'Vermont'},
    "VA": {'description': 'Virginia'},
    "WA": {'description': 'Washington'},
    "WV": {'description': 'West Virginia'},
    "WI": {'description': 'Wisconsin'},
    "WY": {'description': 'Wyoming'},
    "DC": {'description': 'District of Columbia'},
    "PR": {'description': 'Puerto Rico'},
    "VI": {'description': 'U.S. Virgin Islands'},
    "GU": {'description': 'Guam'},
    "AS": {'description': 'American Samoa'},
    "MP": {'description': 'Northern Mariana Islands'},
}

class CanadianProvinceCodeEnum(RichEnum):
    """
    Canadian province and territory codes
    """
    # Enum members
    AB = "AB"
    BC = "BC"
    MB = "MB"
    NB = "NB"
    NL = "NL"
    NS = "NS"
    NT = "NT"
    NU = "NU"
    TRUE = "True"
    PE = "PE"
    QC = "QC"
    SK = "SK"
    YT = "YT"

# Set metadata after class creation
CanadianProvinceCodeEnum._metadata = {
    "AB": {'description': 'Alberta'},
    "BC": {'description': 'British Columbia'},
    "MB": {'description': 'Manitoba'},
    "NB": {'description': 'New Brunswick'},
    "NL": {'description': 'Newfoundland and Labrador'},
    "NS": {'description': 'Nova Scotia'},
    "NT": {'description': 'Northwest Territories'},
    "NU": {'description': 'Nunavut'},
    "TRUE": {'description': 'Ontario'},
    "PE": {'description': 'Prince Edward Island'},
    "QC": {'description': 'Quebec'},
    "SK": {'description': 'Saskatchewan'},
    "YT": {'description': 'Yukon'},
}

class CompassDirection(RichEnum):
    """
    Cardinal and intercardinal compass directions
    """
    # Enum members
    NORTH = "NORTH"
    EAST = "EAST"
    SOUTH = "SOUTH"
    WEST = "WEST"
    NORTHEAST = "NORTHEAST"
    SOUTHEAST = "SOUTHEAST"
    SOUTHWEST = "SOUTHWEST"
    NORTHWEST = "NORTHWEST"
    NORTH_NORTHEAST = "NORTH_NORTHEAST"
    EAST_NORTHEAST = "EAST_NORTHEAST"
    EAST_SOUTHEAST = "EAST_SOUTHEAST"
    SOUTH_SOUTHEAST = "SOUTH_SOUTHEAST"
    SOUTH_SOUTHWEST = "SOUTH_SOUTHWEST"
    WEST_SOUTHWEST = "WEST_SOUTHWEST"
    WEST_NORTHWEST = "WEST_NORTHWEST"
    NORTH_NORTHWEST = "NORTH_NORTHWEST"

# Set metadata after class creation
CompassDirection._metadata = {
    "NORTH": {'description': 'North (0°/360°)', 'annotations': {'abbreviation': 'N', 'degrees': 0}},
    "EAST": {'description': 'East (90°)', 'annotations': {'abbreviation': 'E', 'degrees': 90}},
    "SOUTH": {'description': 'South (180°)', 'annotations': {'abbreviation': 'S', 'degrees': 180}},
    "WEST": {'description': 'West (270°)', 'annotations': {'abbreviation': 'W', 'degrees': 270}},
    "NORTHEAST": {'description': 'Northeast (45°)', 'annotations': {'abbreviation': 'NE', 'degrees': 45}},
    "SOUTHEAST": {'description': 'Southeast (135°)', 'annotations': {'abbreviation': 'SE', 'degrees': 135}},
    "SOUTHWEST": {'description': 'Southwest (225°)', 'annotations': {'abbreviation': 'SW', 'degrees': 225}},
    "NORTHWEST": {'description': 'Northwest (315°)', 'annotations': {'abbreviation': 'NW', 'degrees': 315}},
    "NORTH_NORTHEAST": {'description': 'North-northeast (22.5°)', 'annotations': {'abbreviation': 'NNE', 'degrees': 22.5}},
    "EAST_NORTHEAST": {'description': 'East-northeast (67.5°)', 'annotations': {'abbreviation': 'ENE', 'degrees': 67.5}},
    "EAST_SOUTHEAST": {'description': 'East-southeast (112.5°)', 'annotations': {'abbreviation': 'ESE', 'degrees': 112.5}},
    "SOUTH_SOUTHEAST": {'description': 'South-southeast (157.5°)', 'annotations': {'abbreviation': 'SSE', 'degrees': 157.5}},
    "SOUTH_SOUTHWEST": {'description': 'South-southwest (202.5°)', 'annotations': {'abbreviation': 'SSW', 'degrees': 202.5}},
    "WEST_SOUTHWEST": {'description': 'West-southwest (247.5°)', 'annotations': {'abbreviation': 'WSW', 'degrees': 247.5}},
    "WEST_NORTHWEST": {'description': 'West-northwest (292.5°)', 'annotations': {'abbreviation': 'WNW', 'degrees': 292.5}},
    "NORTH_NORTHWEST": {'description': 'North-northwest (337.5°)', 'annotations': {'abbreviation': 'NNW', 'degrees': 337.5}},
}

class RelativeDirection(RichEnum):
    """
    Relative directional terms
    """
    # Enum members
    FORWARD = "FORWARD"
    BACKWARD = "BACKWARD"
    LEFT = "LEFT"
    RIGHT = "RIGHT"
    UP = "UP"
    DOWN = "DOWN"
    INWARD = "INWARD"
    OUTWARD = "OUTWARD"
    CLOCKWISE = "CLOCKWISE"
    COUNTERCLOCKWISE = "COUNTERCLOCKWISE"

# Set metadata after class creation
RelativeDirection._metadata = {
    "FORWARD": {'description': 'Forward/Ahead', 'annotations': {'aliases': 'ahead, front'}},
    "BACKWARD": {'description': 'Backward/Behind', 'annotations': {'aliases': 'behind, back, rear'}},
    "LEFT": {'description': 'Left', 'annotations': {'aliases': 'port (nautical)'}},
    "RIGHT": {'description': 'Right', 'annotations': {'aliases': 'starboard (nautical)'}},
    "UP": {'description': 'Up/Above', 'annotations': {'aliases': 'above, upward'}},
    "DOWN": {'description': 'Down/Below', 'annotations': {'aliases': 'below, downward'}},
    "INWARD": {'description': 'Inward/Toward center', 'annotations': {'aliases': 'toward center, centripetal'}},
    "OUTWARD": {'description': 'Outward/Away from center', 'annotations': {'aliases': 'away from center, centrifugal'}},
    "CLOCKWISE": {'description': 'Clockwise rotation', 'annotations': {'abbreviation': 'CW'}},
    "COUNTERCLOCKWISE": {'description': 'Counterclockwise rotation', 'annotations': {'abbreviation': 'CCW', 'aliases': 'anticlockwise'}},
}

class WindDirection(RichEnum):
    """
    Wind direction nomenclature (named for where wind comes FROM)
    """
    # Enum members
    NORTHERLY = "NORTHERLY"
    NORTHEASTERLY = "NORTHEASTERLY"
    EASTERLY = "EASTERLY"
    SOUTHEASTERLY = "SOUTHEASTERLY"
    SOUTHERLY = "SOUTHERLY"
    SOUTHWESTERLY = "SOUTHWESTERLY"
    WESTERLY = "WESTERLY"
    NORTHWESTERLY = "NORTHWESTERLY"
    VARIABLE = "VARIABLE"

# Set metadata after class creation
WindDirection._metadata = {
    "NORTHERLY": {'description': 'Wind from the north', 'annotations': {'from_direction': 'north', 'toward_direction': 'south'}},
    "NORTHEASTERLY": {'description': 'Wind from the northeast', 'annotations': {'from_direction': 'northeast', 'toward_direction': 'southwest'}},
    "EASTERLY": {'description': 'Wind from the east', 'annotations': {'from_direction': 'east', 'toward_direction': 'west'}},
    "SOUTHEASTERLY": {'description': 'Wind from the southeast', 'annotations': {'from_direction': 'southeast', 'toward_direction': 'northwest'}},
    "SOUTHERLY": {'description': 'Wind from the south', 'annotations': {'from_direction': 'south', 'toward_direction': 'north'}},
    "SOUTHWESTERLY": {'description': 'Wind from the southwest', 'annotations': {'from_direction': 'southwest', 'toward_direction': 'northeast'}},
    "WESTERLY": {'description': 'Wind from the west', 'annotations': {'from_direction': 'west', 'toward_direction': 'east'}},
    "NORTHWESTERLY": {'description': 'Wind from the northwest', 'annotations': {'from_direction': 'northwest', 'toward_direction': 'southeast'}},
    "VARIABLE": {'description': 'Variable wind direction', 'annotations': {'note': 'changing or inconsistent direction'}},
}

class ContinentEnum(RichEnum):
    """
    Continental regions
    """
    # Enum members
    AFRICA = "AFRICA"
    ANTARCTICA = "ANTARCTICA"
    ASIA = "ASIA"
    EUROPE = "EUROPE"
    NORTH_AMERICA = "NORTH_AMERICA"
    OCEANIA = "OCEANIA"
    SOUTH_AMERICA = "SOUTH_AMERICA"

# Set metadata after class creation
ContinentEnum._metadata = {
    "AFRICA": {'description': 'Africa'},
    "ANTARCTICA": {'description': 'Antarctica'},
    "ASIA": {'description': 'Asia'},
    "EUROPE": {'description': 'Europe'},
    "NORTH_AMERICA": {'description': 'North America'},
    "OCEANIA": {'description': 'Oceania (including Australia)'},
    "SOUTH_AMERICA": {'description': 'South America'},
}

class UNRegionEnum(RichEnum):
    """
    United Nations regional classifications
    """
    # Enum members
    EASTERN_AFRICA = "EASTERN_AFRICA"
    MIDDLE_AFRICA = "MIDDLE_AFRICA"
    NORTHERN_AFRICA = "NORTHERN_AFRICA"
    SOUTHERN_AFRICA = "SOUTHERN_AFRICA"
    WESTERN_AFRICA = "WESTERN_AFRICA"
    CARIBBEAN = "CARIBBEAN"
    CENTRAL_AMERICA = "CENTRAL_AMERICA"
    NORTHERN_AMERICA = "NORTHERN_AMERICA"
    SOUTH_AMERICA = "SOUTH_AMERICA"
    CENTRAL_ASIA = "CENTRAL_ASIA"
    EASTERN_ASIA = "EASTERN_ASIA"
    SOUTHERN_ASIA = "SOUTHERN_ASIA"
    SOUTH_EASTERN_ASIA = "SOUTH_EASTERN_ASIA"
    WESTERN_ASIA = "WESTERN_ASIA"
    EASTERN_EUROPE = "EASTERN_EUROPE"
    NORTHERN_EUROPE = "NORTHERN_EUROPE"
    SOUTHERN_EUROPE = "SOUTHERN_EUROPE"
    WESTERN_EUROPE = "WESTERN_EUROPE"
    AUSTRALIA_NEW_ZEALAND = "AUSTRALIA_NEW_ZEALAND"
    MELANESIA = "MELANESIA"
    MICRONESIA = "MICRONESIA"
    POLYNESIA = "POLYNESIA"

# Set metadata after class creation
UNRegionEnum._metadata = {
    "EASTERN_AFRICA": {'description': 'Eastern Africa'},
    "MIDDLE_AFRICA": {'description': 'Middle Africa'},
    "NORTHERN_AFRICA": {'description': 'Northern Africa'},
    "SOUTHERN_AFRICA": {'description': 'Southern Africa'},
    "WESTERN_AFRICA": {'description': 'Western Africa'},
    "CARIBBEAN": {'description': 'Caribbean'},
    "CENTRAL_AMERICA": {'description': 'Central America'},
    "NORTHERN_AMERICA": {'description': 'Northern America'},
    "SOUTH_AMERICA": {'description': 'South America'},
    "CENTRAL_ASIA": {'description': 'Central Asia'},
    "EASTERN_ASIA": {'description': 'Eastern Asia'},
    "SOUTHERN_ASIA": {'description': 'Southern Asia'},
    "SOUTH_EASTERN_ASIA": {'description': 'South-Eastern Asia'},
    "WESTERN_ASIA": {'description': 'Western Asia'},
    "EASTERN_EUROPE": {'description': 'Eastern Europe'},
    "NORTHERN_EUROPE": {'description': 'Northern Europe'},
    "SOUTHERN_EUROPE": {'description': 'Southern Europe'},
    "WESTERN_EUROPE": {'description': 'Western Europe'},
    "AUSTRALIA_NEW_ZEALAND": {'description': 'Australia and New Zealand'},
    "MELANESIA": {'description': 'Melanesia'},
    "MICRONESIA": {'description': 'Micronesia'},
    "POLYNESIA": {'description': 'Polynesia'},
}

class LanguageCodeISO6391enum(RichEnum):
    """
    ISO 639-1 two-letter language codes
    """
    # Enum members
    EN = "EN"
    ES = "ES"
    FR = "FR"
    DE = "DE"
    IT = "IT"
    PT = "PT"
    RU = "RU"
    ZH = "ZH"
    JA = "JA"
    KO = "KO"
    AR = "AR"
    HI = "HI"
    BN = "BN"
    PA = "PA"
    UR = "UR"
    NL = "NL"
    PL = "PL"
    TR = "TR"
    VI = "VI"
    TH = "TH"
    SV = "SV"
    DA = "DA"
    FALSE = "False"
    FI = "FI"
    EL = "EL"
    HE = "HE"
    CS = "CS"
    HU = "HU"
    RO = "RO"
    UK = "UK"

# Set metadata after class creation
LanguageCodeISO6391enum._metadata = {
    "EN": {'description': 'English'},
    "ES": {'description': 'Spanish'},
    "FR": {'description': 'French'},
    "DE": {'description': 'German'},
    "IT": {'description': 'Italian'},
    "PT": {'description': 'Portuguese'},
    "RU": {'description': 'Russian'},
    "ZH": {'description': 'Chinese'},
    "JA": {'description': 'Japanese'},
    "KO": {'description': 'Korean'},
    "AR": {'description': 'Arabic'},
    "HI": {'description': 'Hindi'},
    "BN": {'description': 'Bengali'},
    "PA": {'description': 'Punjabi'},
    "UR": {'description': 'Urdu'},
    "NL": {'description': 'Dutch'},
    "PL": {'description': 'Polish'},
    "TR": {'description': 'Turkish'},
    "VI": {'description': 'Vietnamese'},
    "TH": {'description': 'Thai'},
    "SV": {'description': 'Swedish'},
    "DA": {'description': 'Danish'},
    "FALSE": {'description': 'Norwegian'},
    "FI": {'description': 'Finnish'},
    "EL": {'description': 'Greek'},
    "HE": {'description': 'Hebrew'},
    "CS": {'description': 'Czech'},
    "HU": {'description': 'Hungarian'},
    "RO": {'description': 'Romanian'},
    "UK": {'description': 'Ukrainian'},
}

class TimeZoneEnum(RichEnum):
    """
    Common time zones
    """
    # Enum members
    UTC = "UTC"
    EST = "EST"
    EDT = "EDT"
    CST = "CST"
    CDT = "CDT"
    MST = "MST"
    MDT = "MDT"
    PST = "PST"
    PDT = "PDT"
    GMT = "GMT"
    BST = "BST"
    CET = "CET"
    CEST = "CEST"
    EET = "EET"
    EEST = "EEST"
    JST = "JST"
    CST_CHINA = "CST_CHINA"
    IST = "IST"
    AEST = "AEST"
    AEDT = "AEDT"
    NZST = "NZST"
    NZDT = "NZDT"

# Set metadata after class creation
TimeZoneEnum._metadata = {
    "UTC": {'description': 'Coordinated Universal Time'},
    "EST": {'description': 'Eastern Standard Time (UTC-5)'},
    "EDT": {'description': 'Eastern Daylight Time (UTC-4)'},
    "CST": {'description': 'Central Standard Time (UTC-6)'},
    "CDT": {'description': 'Central Daylight Time (UTC-5)'},
    "MST": {'description': 'Mountain Standard Time (UTC-7)'},
    "MDT": {'description': 'Mountain Daylight Time (UTC-6)'},
    "PST": {'description': 'Pacific Standard Time (UTC-8)'},
    "PDT": {'description': 'Pacific Daylight Time (UTC-7)'},
    "GMT": {'description': 'Greenwich Mean Time (UTC+0)'},
    "BST": {'description': 'British Summer Time (UTC+1)'},
    "CET": {'description': 'Central European Time (UTC+1)'},
    "CEST": {'description': 'Central European Summer Time (UTC+2)'},
    "EET": {'description': 'Eastern European Time (UTC+2)'},
    "EEST": {'description': 'Eastern European Summer Time (UTC+3)'},
    "JST": {'description': 'Japan Standard Time (UTC+9)'},
    "CST_CHINA": {'description': 'China Standard Time (UTC+8)'},
    "IST": {'description': 'India Standard Time (UTC+5:30)'},
    "AEST": {'description': 'Australian Eastern Standard Time (UTC+10)'},
    "AEDT": {'description': 'Australian Eastern Daylight Time (UTC+11)'},
    "NZST": {'description': 'New Zealand Standard Time (UTC+12)'},
    "NZDT": {'description': 'New Zealand Daylight Time (UTC+13)'},
}

class CurrencyCodeISO4217Enum(RichEnum):
    """
    ISO 4217 currency codes
    """
    # Enum members
    USD = "USD"
    EUR = "EUR"
    GBP = "GBP"
    JPY = "JPY"
    CNY = "CNY"
    CHF = "CHF"
    CAD = "CAD"
    AUD = "AUD"
    NZD = "NZD"
    SEK = "SEK"
    NOK = "NOK"
    DKK = "DKK"
    PLN = "PLN"
    RUB = "RUB"
    INR = "INR"
    BRL = "BRL"
    MXN = "MXN"
    ZAR = "ZAR"
    KRW = "KRW"
    SGD = "SGD"
    HKD = "HKD"
    TWD = "TWD"
    THB = "THB"
    MYR = "MYR"
    IDR = "IDR"
    PHP = "PHP"
    VND = "VND"
    TRY = "TRY"
    AED = "AED"
    SAR = "SAR"
    ILS = "ILS"
    EGP = "EGP"

# Set metadata after class creation
CurrencyCodeISO4217Enum._metadata = {
    "USD": {'description': 'United States Dollar'},
    "EUR": {'description': 'Euro'},
    "GBP": {'description': 'British Pound Sterling'},
    "JPY": {'description': 'Japanese Yen'},
    "CNY": {'description': 'Chinese Yuan Renminbi'},
    "CHF": {'description': 'Swiss Franc'},
    "CAD": {'description': 'Canadian Dollar'},
    "AUD": {'description': 'Australian Dollar'},
    "NZD": {'description': 'New Zealand Dollar'},
    "SEK": {'description': 'Swedish Krona'},
    "NOK": {'description': 'Norwegian Krone'},
    "DKK": {'description': 'Danish Krone'},
    "PLN": {'description': 'Polish Zloty'},
    "RUB": {'description': 'Russian Ruble'},
    "INR": {'description': 'Indian Rupee'},
    "BRL": {'description': 'Brazilian Real'},
    "MXN": {'description': 'Mexican Peso'},
    "ZAR": {'description': 'South African Rand'},
    "KRW": {'description': 'South Korean Won'},
    "SGD": {'description': 'Singapore Dollar'},
    "HKD": {'description': 'Hong Kong Dollar'},
    "TWD": {'description': 'Taiwan Dollar'},
    "THB": {'description': 'Thai Baht'},
    "MYR": {'description': 'Malaysian Ringgit'},
    "IDR": {'description': 'Indonesian Rupiah'},
    "PHP": {'description': 'Philippine Peso'},
    "VND": {'description': 'Vietnamese Dong'},
    "TRY": {'description': 'Turkish Lira'},
    "AED": {'description': 'UAE Dirham'},
    "SAR": {'description': 'Saudi Riyal'},
    "ILS": {'description': 'Israeli Shekel'},
    "EGP": {'description': 'Egyptian Pound'},
}

class SentimentClassificationEnum(RichEnum):
    """
    Standard labels for sentiment analysis classification tasks
    """
    # Enum members
    POSITIVE = "POSITIVE"
    NEGATIVE = "NEGATIVE"
    NEUTRAL = "NEUTRAL"

# Set metadata after class creation
SentimentClassificationEnum._metadata = {
    "POSITIVE": {'description': 'Positive sentiment or opinion', 'meaning': 'NCIT:C38758', 'aliases': ['pos', '1', '+']},
    "NEGATIVE": {'description': 'Negative sentiment or opinion', 'meaning': 'NCIT:C35681', 'aliases': ['neg', '0', '-']},
    "NEUTRAL": {'description': 'Neutral sentiment, neither positive nor negative', 'meaning': 'NCIT:C14165', 'aliases': ['neu', '2']},
}

class FineSentimentClassificationEnum(RichEnum):
    """
    Fine-grained sentiment analysis labels with intensity levels
    """
    # Enum members
    VERY_POSITIVE = "VERY_POSITIVE"
    POSITIVE = "POSITIVE"
    NEUTRAL = "NEUTRAL"
    NEGATIVE = "NEGATIVE"
    VERY_NEGATIVE = "VERY_NEGATIVE"

# Set metadata after class creation
FineSentimentClassificationEnum._metadata = {
    "VERY_POSITIVE": {'description': 'Strongly positive sentiment', 'meaning': 'NCIT:C38758', 'aliases': ['5', '++']},
    "POSITIVE": {'description': 'Positive sentiment', 'meaning': 'NCIT:C38758', 'aliases': ['4', '+']},
    "NEUTRAL": {'description': 'Neutral sentiment', 'meaning': 'NCIT:C14165', 'aliases': ['3', '0']},
    "NEGATIVE": {'description': 'Negative sentiment', 'meaning': 'NCIT:C35681', 'aliases': ['2', '-']},
    "VERY_NEGATIVE": {'description': 'Strongly negative sentiment', 'meaning': 'NCIT:C35681', 'aliases': ['1', '--']},
}

class BinaryClassificationEnum(RichEnum):
    """
    Generic binary classification labels
    """
    # Enum members
    POSITIVE = "POSITIVE"
    NEGATIVE = "NEGATIVE"

# Set metadata after class creation
BinaryClassificationEnum._metadata = {
    "POSITIVE": {'description': 'Positive class', 'meaning': 'NCIT:C38758', 'aliases': ['1', 'true', 'yes', 'T']},
    "NEGATIVE": {'description': 'Negative class', 'meaning': 'NCIT:C35681', 'aliases': ['0', 'false', 'no', 'F']},
}

class SpamClassificationEnum(RichEnum):
    """
    Standard labels for spam/ham email classification
    """
    # Enum members
    SPAM = "SPAM"
    HAM = "HAM"

# Set metadata after class creation
SpamClassificationEnum._metadata = {
    "SPAM": {'description': 'Unwanted or unsolicited message', 'annotations': {'note': 'No appropriate ontology term found for spam concept'}, 'aliases': ['junk', '1']},
    "HAM": {'description': 'Legitimate, wanted message', 'annotations': {'note': 'No appropriate ontology term found for ham concept'}, 'aliases': ['not_spam', 'legitimate', '0']},
}

class AnomalyDetectionEnum(RichEnum):
    """
    Labels for anomaly detection tasks
    """
    # Enum members
    NORMAL = "NORMAL"
    ANOMALY = "ANOMALY"

# Set metadata after class creation
AnomalyDetectionEnum._metadata = {
    "NORMAL": {'description': 'Normal, expected behavior or pattern', 'meaning': 'NCIT:C14165', 'aliases': ['inlier', 'regular', '0']},
    "ANOMALY": {'description': 'Abnormal, unexpected behavior or pattern', 'meaning': 'STATO:0000036', 'aliases': ['outlier', 'abnormal', 'irregular', '1']},
}

class ChurnClassificationEnum(RichEnum):
    """
    Customer churn prediction labels
    """
    # Enum members
    RETAINED = "RETAINED"
    CHURNED = "CHURNED"

# Set metadata after class creation
ChurnClassificationEnum._metadata = {
    "RETAINED": {'description': 'Customer continues using the service', 'annotations': {'note': 'No appropriate ontology term found for customer retention'}, 'aliases': ['active', 'staying', '0']},
    "CHURNED": {'description': 'Customer stopped using the service', 'annotations': {'note': 'No appropriate ontology term found for customer churn'}, 'aliases': ['lost', 'inactive', 'attrited', '1']},
}

class FraudDetectionEnum(RichEnum):
    """
    Fraud detection classification labels
    """
    # Enum members
    LEGITIMATE = "LEGITIMATE"
    FRAUDULENT = "FRAUDULENT"

# Set metadata after class creation
FraudDetectionEnum._metadata = {
    "LEGITIMATE": {'description': 'Legitimate, non-fraudulent transaction or activity', 'meaning': 'NCIT:C14165', 'aliases': ['genuine', 'valid', '0']},
    "FRAUDULENT": {'description': 'Fraudulent transaction or activity', 'meaning': 'NCIT:C121839', 'aliases': ['fraud', 'invalid', '1']},
}

class QualityControlEnum(RichEnum):
    """
    Quality control classification labels
    """
    # Enum members
    PASS = "PASS"
    FAIL = "FAIL"

# Set metadata after class creation
QualityControlEnum._metadata = {
    "PASS": {'description': 'Item meets quality standards', 'meaning': 'NCIT:C81275', 'aliases': ['passed', 'acceptable', 'ok', '1']},
    "FAIL": {'description': 'Item does not meet quality standards', 'meaning': 'NCIT:C44281', 'aliases': ['failed', 'reject', 'defective', '0']},
}

class DefectClassificationEnum(RichEnum):
    """
    Manufacturing defect classification
    """
    # Enum members
    NO_DEFECT = "NO_DEFECT"
    MINOR_DEFECT = "MINOR_DEFECT"
    MAJOR_DEFECT = "MAJOR_DEFECT"
    CRITICAL_DEFECT = "CRITICAL_DEFECT"

# Set metadata after class creation
DefectClassificationEnum._metadata = {
    "NO_DEFECT": {'description': 'No defect detected', 'meaning': 'NCIT:C14165', 'aliases': ['good', 'normal', '0']},
    "MINOR_DEFECT": {'description': "Minor defect that doesn't affect functionality", 'aliases': ['minor', 'cosmetic', '1']},
    "MAJOR_DEFECT": {'description': 'Major defect affecting functionality', 'aliases': ['major', 'functional', '2']},
    "CRITICAL_DEFECT": {'description': 'Critical defect rendering item unusable or unsafe', 'aliases': ['critical', 'severe', '3']},
}

class BasicEmotionEnum(RichEnum):
    """
    Ekman's six basic emotions commonly used in emotion recognition
    """
    # Enum members
    ANGER = "ANGER"
    DISGUST = "DISGUST"
    FEAR = "FEAR"
    HAPPINESS = "HAPPINESS"
    SADNESS = "SADNESS"
    SURPRISE = "SURPRISE"

# Set metadata after class creation
BasicEmotionEnum._metadata = {
    "ANGER": {'description': 'Feeling of displeasure or hostility', 'meaning': 'MFOEM:000009', 'aliases': ['angry', 'mad']},
    "DISGUST": {'description': 'Feeling of revulsion or strong disapproval', 'meaning': 'MFOEM:000019', 'aliases': ['disgusted', 'repulsed']},
    "FEAR": {'description': 'Feeling of anxiety or apprehension', 'meaning': 'MFOEM:000026', 'aliases': ['afraid', 'scared']},
    "HAPPINESS": {'description': 'Feeling of pleasure or contentment', 'meaning': 'MFOEM:000042', 'aliases': ['happy', 'joy', 'joyful']},
    "SADNESS": {'description': 'Feeling of sorrow or unhappiness', 'meaning': 'MFOEM:000056', 'aliases': ['sad', 'sorrow']},
    "SURPRISE": {'description': 'Feeling of mild astonishment or shock', 'meaning': 'MFOEM:000032', 'aliases': ['surprised', 'shocked']},
}

class ExtendedEmotionEnum(RichEnum):
    """
    Extended emotion set including complex emotions
    """
    # Enum members
    ANGER = "ANGER"
    DISGUST = "DISGUST"
    FEAR = "FEAR"
    HAPPINESS = "HAPPINESS"
    SADNESS = "SADNESS"
    SURPRISE = "SURPRISE"
    CONTEMPT = "CONTEMPT"
    ANTICIPATION = "ANTICIPATION"
    TRUST = "TRUST"
    LOVE = "LOVE"

# Set metadata after class creation
ExtendedEmotionEnum._metadata = {
    "ANGER": {'description': 'Feeling of displeasure or hostility', 'meaning': 'MFOEM:000009'},
    "DISGUST": {'description': 'Feeling of revulsion', 'meaning': 'MFOEM:000019'},
    "FEAR": {'description': 'Feeling of anxiety', 'meaning': 'MFOEM:000026'},
    "HAPPINESS": {'description': 'Feeling of pleasure', 'meaning': 'MFOEM:000042'},
    "SADNESS": {'description': 'Feeling of sorrow', 'meaning': 'MFOEM:000056'},
    "SURPRISE": {'description': 'Feeling of astonishment', 'meaning': 'MFOEM:000032'},
    "CONTEMPT": {'description': 'Feeling that something is worthless', 'meaning': 'MFOEM:000018'},
    "ANTICIPATION": {'description': 'Feeling of excitement about something that will happen', 'meaning': 'MFOEM:000175', 'aliases': ['expectation', 'expectant']},
    "TRUST": {'description': 'Feeling of confidence in someone or something', 'meaning': 'MFOEM:000224'},
    "LOVE": {'description': 'Feeling of deep affection', 'meaning': 'MFOEM:000048'},
}

class PriorityLevelEnum(RichEnum):
    """
    Standard priority levels for task/issue classification
    """
    # Enum members
    CRITICAL = "CRITICAL"
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"
    TRIVIAL = "TRIVIAL"

# Set metadata after class creation
PriorityLevelEnum._metadata = {
    "CRITICAL": {'description': 'Highest priority, requires immediate attention', 'aliases': ['P0', 'urgent', 'blocker', '1']},
    "HIGH": {'description': 'High priority, should be addressed soon', 'aliases': ['P1', 'important', '2']},
    "MEDIUM": {'description': 'Medium priority, normal workflow', 'aliases': ['P2', 'normal', '3']},
    "LOW": {'description': 'Low priority, can be deferred', 'aliases': ['P3', 'minor', '4']},
    "TRIVIAL": {'description': 'Lowest priority, nice to have', 'aliases': ['P4', 'cosmetic', '5']},
}

class SeverityLevelEnum(RichEnum):
    """
    Severity levels for incident/bug classification
    """
    # Enum members
    CRITICAL = "CRITICAL"
    MAJOR = "MAJOR"
    MINOR = "MINOR"
    TRIVIAL = "TRIVIAL"

# Set metadata after class creation
SeverityLevelEnum._metadata = {
    "CRITICAL": {'description': 'System is unusable, data loss possible', 'aliases': ['S1', 'blocker', 'showstopper']},
    "MAJOR": {'description': 'Major functionality impaired', 'aliases': ['S2', 'severe', 'high']},
    "MINOR": {'description': 'Minor functionality impaired', 'aliases': ['S3', 'moderate', 'medium']},
    "TRIVIAL": {'description': 'Cosmetic issue, minimal impact', 'aliases': ['S4', 'cosmetic', 'low']},
}

class ConfidenceLevelEnum(RichEnum):
    """
    Confidence levels for predictions and classifications
    """
    # Enum members
    VERY_HIGH = "VERY_HIGH"
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"
    VERY_LOW = "VERY_LOW"

# Set metadata after class creation
ConfidenceLevelEnum._metadata = {
    "VERY_HIGH": {'description': 'Very high confidence (>95%)', 'aliases': ['certain', '5']},
    "HIGH": {'description': 'High confidence (80-95%)', 'aliases': ['confident', '4']},
    "MEDIUM": {'description': 'Medium confidence (60-80%)', 'aliases': ['moderate', '3']},
    "LOW": {'description': 'Low confidence (40-60%)', 'aliases': ['uncertain', '2']},
    "VERY_LOW": {'description': 'Very low confidence (<40%)', 'aliases': ['guess', '1']},
}

class NewsTopicCategoryEnum(RichEnum):
    """
    Common news article topic categories
    """
    # Enum members
    POLITICS = "POLITICS"
    BUSINESS = "BUSINESS"
    TECHNOLOGY = "TECHNOLOGY"
    SPORTS = "SPORTS"
    ENTERTAINMENT = "ENTERTAINMENT"
    SCIENCE = "SCIENCE"
    HEALTH = "HEALTH"
    WORLD = "WORLD"
    LOCAL = "LOCAL"

# Set metadata after class creation
NewsTopicCategoryEnum._metadata = {
    "POLITICS": {'description': 'Political news and government affairs'},
    "BUSINESS": {'description': 'Business, finance, and economic news', 'aliases': ['finance', 'economy']},
    "TECHNOLOGY": {'description': 'Technology and computing news', 'aliases': ['tech', 'IT']},
    "SPORTS": {'description': 'Sports news and events'},
    "ENTERTAINMENT": {'description': 'Entertainment and celebrity news', 'aliases': ['showbiz']},
    "SCIENCE": {'description': 'Scientific discoveries and research'},
    "HEALTH": {'description': 'Health, medicine, and wellness news', 'aliases': ['medical']},
    "WORLD": {'description': 'International news and events', 'aliases': ['international', 'global']},
    "LOCAL": {'description': 'Local and regional news', 'aliases': ['regional']},
}

class ToxicityClassificationEnum(RichEnum):
    """
    Text toxicity classification labels
    """
    # Enum members
    NON_TOXIC = "NON_TOXIC"
    TOXIC = "TOXIC"
    SEVERE_TOXIC = "SEVERE_TOXIC"
    OBSCENE = "OBSCENE"
    THREAT = "THREAT"
    INSULT = "INSULT"
    IDENTITY_HATE = "IDENTITY_HATE"

# Set metadata after class creation
ToxicityClassificationEnum._metadata = {
    "NON_TOXIC": {'description': 'Text is appropriate and non-harmful', 'meaning': 'SIO:001010', 'aliases': ['safe', 'clean', '0']},
    "TOXIC": {'description': 'Text contains harmful or inappropriate content', 'aliases': ['harmful', 'inappropriate', '1']},
    "SEVERE_TOXIC": {'description': 'Text contains severely harmful content'},
    "OBSCENE": {'description': 'Text contains obscene content'},
    "THREAT": {'description': 'Text contains threatening content'},
    "INSULT": {'description': 'Text contains insulting content'},
    "IDENTITY_HATE": {'description': 'Text contains identity-based hate'},
}

class IntentClassificationEnum(RichEnum):
    """
    Common chatbot/NLU intent categories
    """
    # Enum members
    GREETING = "GREETING"
    GOODBYE = "GOODBYE"
    THANKS = "THANKS"
    HELP = "HELP"
    INFORMATION = "INFORMATION"
    COMPLAINT = "COMPLAINT"
    FEEDBACK = "FEEDBACK"
    PURCHASE = "PURCHASE"
    CANCEL = "CANCEL"
    REFUND = "REFUND"

# Set metadata after class creation
IntentClassificationEnum._metadata = {
    "GREETING": {'description': 'User greeting or hello'},
    "GOODBYE": {'description': 'User saying goodbye'},
    "THANKS": {'description': 'User expressing gratitude'},
    "HELP": {'description': 'User requesting help or assistance'},
    "INFORMATION": {'description': 'User requesting information'},
    "COMPLAINT": {'description': 'User expressing dissatisfaction'},
    "FEEDBACK": {'description': 'User providing feedback'},
    "PURCHASE": {'description': 'User intent to buy or purchase'},
    "CANCEL": {'description': 'User intent to cancel'},
    "REFUND": {'description': 'User requesting refund'},
}

class SimpleSpatialDirection(RichEnum):
    """
    Basic spatial directional terms for general use
    """
    # Enum members
    LEFT = "LEFT"
    RIGHT = "RIGHT"
    FORWARD = "FORWARD"
    BACKWARD = "BACKWARD"
    UP = "UP"
    DOWN = "DOWN"
    INWARD = "INWARD"
    OUTWARD = "OUTWARD"
    TOP = "TOP"
    BOTTOM = "BOTTOM"
    MIDDLE = "MIDDLE"

# Set metadata after class creation
SimpleSpatialDirection._metadata = {
    "LEFT": {'description': 'To the left side'},
    "RIGHT": {'description': 'To the right side'},
    "FORWARD": {'description': 'In the forward direction', 'annotations': {'aliases': 'ahead, front'}},
    "BACKWARD": {'description': 'In the backward direction', 'annotations': {'aliases': 'back, behind, rear'}},
    "UP": {'description': 'In the upward direction', 'annotations': {'aliases': 'above, upward'}},
    "DOWN": {'description': 'In the downward direction', 'annotations': {'aliases': 'below, downward'}},
    "INWARD": {'description': 'Toward the center or interior', 'annotations': {'aliases': 'medial, toward center'}},
    "OUTWARD": {'description': 'Away from the center or exterior', 'annotations': {'aliases': 'peripheral, away from center'}},
    "TOP": {'description': 'At or toward the top', 'annotations': {'aliases': 'upper, uppermost'}},
    "BOTTOM": {'description': 'At or toward the bottom', 'annotations': {'aliases': 'lower, lowermost'}},
    "MIDDLE": {'description': 'At or toward the middle', 'annotations': {'aliases': 'center, central'}},
}

class AnatomicalSide(RichEnum):
    """
    Anatomical sides as defined in the Biological Spatial Ontology (BSPO).
    An anatomical region bounded by a plane perpendicular to an axis through the middle.
    """
    # Enum members
    LEFT = "LEFT"
    RIGHT = "RIGHT"
    ANTERIOR = "ANTERIOR"
    POSTERIOR = "POSTERIOR"
    DORSAL = "DORSAL"
    VENTRAL = "VENTRAL"
    LATERAL = "LATERAL"
    MEDIAL = "MEDIAL"
    PROXIMAL = "PROXIMAL"
    DISTAL = "DISTAL"
    APICAL = "APICAL"
    BASAL = "BASAL"
    SUPERFICIAL = "SUPERFICIAL"
    DEEP = "DEEP"
    SUPERIOR = "SUPERIOR"
    INFERIOR = "INFERIOR"
    IPSILATERAL = "IPSILATERAL"
    CONTRALATERAL = "CONTRALATERAL"
    CENTRAL = "CENTRAL"

# Set metadata after class creation
AnatomicalSide._metadata = {
    "LEFT": {'meaning': 'BSPO:0000000', 'aliases': ['left side']},
    "RIGHT": {'meaning': 'BSPO:0000007', 'aliases': ['right side']},
    "ANTERIOR": {'meaning': 'BSPO:0000055', 'annotations': {'aliases': 'front, rostral, cranial (in head region)'}, 'aliases': ['anterior side']},
    "POSTERIOR": {'meaning': 'BSPO:0000056', 'annotations': {'aliases': 'back, caudal'}, 'aliases': ['posterior side']},
    "DORSAL": {'meaning': 'BSPO:0000063', 'annotations': {'aliases': 'back (in vertebrates), upper (in humans)'}, 'aliases': ['dorsal side']},
    "VENTRAL": {'meaning': 'BSPO:0000068', 'annotations': {'aliases': 'belly, front (in vertebrates), lower (in humans)'}, 'aliases': ['ventral side']},
    "LATERAL": {'meaning': 'BSPO:0000066', 'annotations': {'aliases': 'side, outer'}, 'aliases': ['lateral side']},
    "MEDIAL": {'meaning': 'BSPO:0000067', 'annotations': {'aliases': 'inner, middle'}, 'aliases': ['medial side']},
    "PROXIMAL": {'meaning': 'BSPO:0000061', 'annotations': {'context': 'commonly used for limbs'}, 'aliases': ['proximal side']},
    "DISTAL": {'meaning': 'BSPO:0000062', 'annotations': {'context': 'commonly used for limbs'}, 'aliases': ['distal side']},
    "APICAL": {'meaning': 'BSPO:0000057', 'annotations': {'context': 'cells, organs, organisms'}, 'aliases': ['apical side']},
    "BASAL": {'meaning': 'BSPO:0000058', 'annotations': {'context': 'cells, organs, organisms'}, 'aliases': ['basal side']},
    "SUPERFICIAL": {'meaning': 'BSPO:0000004', 'annotations': {'aliases': 'external, outer'}, 'aliases': ['superficial side']},
    "DEEP": {'meaning': 'BSPO:0000003', 'annotations': {'aliases': 'internal, inner'}, 'aliases': ['deep side']},
    "SUPERIOR": {'meaning': 'BSPO:0000022', 'annotations': {'aliases': 'cranial (toward head), upper'}, 'aliases': ['superior side']},
    "INFERIOR": {'meaning': 'BSPO:0000025', 'annotations': {'aliases': 'caudal (toward tail), lower'}, 'aliases': ['inferior side']},
    "IPSILATERAL": {'meaning': 'BSPO:0000065', 'annotations': {'context': 'relative to a reference point'}, 'aliases': ['ipsilateral side']},
    "CONTRALATERAL": {'meaning': 'BSPO:0000060', 'annotations': {'context': 'relative to a reference point'}, 'aliases': ['contralateral side']},
    "CENTRAL": {'meaning': 'BSPO:0000059', 'annotations': {'aliases': 'middle'}, 'aliases': ['central side']},
}

class AnatomicalRegion(RichEnum):
    """
    Anatomical regions based on spatial position
    """
    # Enum members
    ANTERIOR_REGION = "ANTERIOR_REGION"
    POSTERIOR_REGION = "POSTERIOR_REGION"
    DORSAL_REGION = "DORSAL_REGION"
    VENTRAL_REGION = "VENTRAL_REGION"
    LATERAL_REGION = "LATERAL_REGION"
    MEDIAL_REGION = "MEDIAL_REGION"
    PROXIMAL_REGION = "PROXIMAL_REGION"
    DISTAL_REGION = "DISTAL_REGION"
    APICAL_REGION = "APICAL_REGION"
    BASAL_REGION = "BASAL_REGION"
    CENTRAL_REGION = "CENTRAL_REGION"
    PERIPHERAL_REGION = "PERIPHERAL_REGION"

# Set metadata after class creation
AnatomicalRegion._metadata = {
    "ANTERIOR_REGION": {'meaning': 'BSPO:0000071', 'aliases': ['anterior region']},
    "POSTERIOR_REGION": {'meaning': 'BSPO:0000072', 'aliases': ['posterior region']},
    "DORSAL_REGION": {'meaning': 'BSPO:0000079', 'aliases': ['dorsal region']},
    "VENTRAL_REGION": {'meaning': 'BSPO:0000084', 'aliases': ['ventral region']},
    "LATERAL_REGION": {'meaning': 'BSPO:0000082', 'aliases': ['lateral region']},
    "MEDIAL_REGION": {'meaning': 'BSPO:0000083', 'aliases': ['medial region']},
    "PROXIMAL_REGION": {'meaning': 'BSPO:0000077', 'aliases': ['proximal region']},
    "DISTAL_REGION": {'meaning': 'BSPO:0000078', 'aliases': ['distal region']},
    "APICAL_REGION": {'meaning': 'BSPO:0000073', 'aliases': ['apical region']},
    "BASAL_REGION": {'meaning': 'BSPO:0000074', 'aliases': ['basal region']},
    "CENTRAL_REGION": {'meaning': 'BSPO:0000075', 'aliases': ['central region']},
    "PERIPHERAL_REGION": {'meaning': 'BSPO:0000127', 'aliases': ['peripheral region']},
}

class AnatomicalAxis(RichEnum):
    """
    Anatomical axes defining spatial organization
    """
    # Enum members
    ANTERIOR_POSTERIOR = "ANTERIOR_POSTERIOR"
    DORSAL_VENTRAL = "DORSAL_VENTRAL"
    LEFT_RIGHT = "LEFT_RIGHT"
    PROXIMAL_DISTAL = "PROXIMAL_DISTAL"
    APICAL_BASAL = "APICAL_BASAL"

# Set metadata after class creation
AnatomicalAxis._metadata = {
    "ANTERIOR_POSTERIOR": {'meaning': 'BSPO:0000013', 'annotations': {'aliases': 'AP axis, rostrocaudal axis'}, 'aliases': ['anterior-posterior axis']},
    "DORSAL_VENTRAL": {'meaning': 'BSPO:0000016', 'annotations': {'aliases': 'DV axis'}, 'aliases': ['dorsal-ventral axis']},
    "LEFT_RIGHT": {'meaning': 'BSPO:0000017', 'annotations': {'aliases': 'LR axis, mediolateral axis'}, 'aliases': ['left-right axis']},
    "PROXIMAL_DISTAL": {'meaning': 'BSPO:0000018', 'annotations': {'context': 'commonly used for appendages'}, 'aliases': ['transverse plane']},
    "APICAL_BASAL": {'meaning': 'BSPO:0000023', 'annotations': {'context': 'epithelial cells, plant structures'}, 'aliases': ['apical-basal gradient']},
}

class AnatomicalPlane(RichEnum):
    """
    Standard anatomical planes for sectioning
    """
    # Enum members
    SAGITTAL = "SAGITTAL"
    MIDSAGITTAL = "MIDSAGITTAL"
    PARASAGITTAL = "PARASAGITTAL"
    CORONAL = "CORONAL"
    TRANSVERSE = "TRANSVERSE"
    OBLIQUE = "OBLIQUE"

# Set metadata after class creation
AnatomicalPlane._metadata = {
    "SAGITTAL": {'meaning': 'BSPO:0000417', 'annotations': {'orientation': 'parallel to the median plane'}, 'aliases': ['sagittal plane']},
    "MIDSAGITTAL": {'meaning': 'BSPO:0000009', 'annotations': {'aliases': 'median plane', 'note': 'divides body into equal left and right halves'}, 'aliases': ['midsagittal plane']},
    "PARASAGITTAL": {'meaning': 'BSPO:0000008', 'annotations': {'note': 'any sagittal plane not at midline'}, 'aliases': ['parasagittal plane']},
    "CORONAL": {'meaning': 'BSPO:0000019', 'annotations': {'aliases': 'frontal plane', 'orientation': 'perpendicular to sagittal plane'}, 'aliases': ['horizontal plane']},
    "TRANSVERSE": {'meaning': 'BSPO:0000018', 'annotations': {'aliases': 'horizontal plane, axial plane', 'orientation': 'perpendicular to longitudinal axis'}, 'aliases': ['transverse plane']},
    "OBLIQUE": {'description': 'Any plane not parallel to sagittal, coronal, or transverse planes', 'annotations': {'note': 'angled section'}},
}

class SpatialRelationship(RichEnum):
    """
    Spatial relationships between anatomical structures
    """
    # Enum members
    ADJACENT_TO = "ADJACENT_TO"
    ANTERIOR_TO = "ANTERIOR_TO"
    POSTERIOR_TO = "POSTERIOR_TO"
    DORSAL_TO = "DORSAL_TO"
    VENTRAL_TO = "VENTRAL_TO"
    LATERAL_TO = "LATERAL_TO"
    MEDIAL_TO = "MEDIAL_TO"
    PROXIMAL_TO = "PROXIMAL_TO"
    DISTAL_TO = "DISTAL_TO"
    SUPERFICIAL_TO = "SUPERFICIAL_TO"
    DEEP_TO = "DEEP_TO"
    SURROUNDS = "SURROUNDS"
    WITHIN = "WITHIN"
    BETWEEN = "BETWEEN"

# Set metadata after class creation
SpatialRelationship._metadata = {
    "ADJACENT_TO": {'meaning': 'RO:0002220', 'aliases': ['adjacent to']},
    "ANTERIOR_TO": {'meaning': 'BSPO:0000096', 'aliases': ['anterior to']},
    "POSTERIOR_TO": {'meaning': 'BSPO:0000099', 'aliases': ['posterior to']},
    "DORSAL_TO": {'meaning': 'BSPO:0000098', 'aliases': ['dorsal to']},
    "VENTRAL_TO": {'meaning': 'BSPO:0000102', 'aliases': ['ventral to']},
    "LATERAL_TO": {'meaning': 'BSPO:0000114', 'aliases': ['lateral to']},
    "MEDIAL_TO": {'meaning': 'BSPO:0000115', 'aliases': ['X medial to y if x is closer to the midsagittal plane than y.']},
    "PROXIMAL_TO": {'meaning': 'BSPO:0000100', 'aliases': ['proximal to']},
    "DISTAL_TO": {'meaning': 'BSPO:0000097', 'aliases': ['distal to']},
    "SUPERFICIAL_TO": {'meaning': 'BSPO:0000108', 'aliases': ['superficial to']},
    "DEEP_TO": {'meaning': 'BSPO:0000107', 'aliases': ['deep to']},
    "SURROUNDS": {'meaning': 'RO:0002221', 'aliases': ['surrounds']},
    "WITHIN": {'description': 'Inside or contained by', 'annotations': {'inverse_of': 'contains'}},
    "BETWEEN": {'description': 'In the space separating two structures', 'annotations': {'note': 'requires two reference points'}},
}

class CellPolarity(RichEnum):
    """
    Spatial polarity in cells and tissues
    """
    # Enum members
    APICAL = "APICAL"
    BASAL = "BASAL"
    LATERAL = "LATERAL"
    APICAL_LATERAL = "APICAL_LATERAL"
    BASAL_LATERAL = "BASAL_LATERAL"
    LEADING_EDGE = "LEADING_EDGE"
    TRAILING_EDGE = "TRAILING_EDGE"
    PROXIMAL_POLE = "PROXIMAL_POLE"
    DISTAL_POLE = "DISTAL_POLE"

# Set metadata after class creation
CellPolarity._metadata = {
    "APICAL": {'description': 'The free surface of an epithelial cell', 'annotations': {'location': 'typically faces lumen or external environment'}},
    "BASAL": {'description': 'The attached surface of an epithelial cell', 'annotations': {'location': 'typically attached to basement membrane'}},
    "LATERAL": {'description': 'The sides of an epithelial cell', 'annotations': {'location': 'faces neighboring cells'}},
    "APICAL_LATERAL": {'description': 'Junction between apical and lateral surfaces'},
    "BASAL_LATERAL": {'description': 'Junction between basal and lateral surfaces'},
    "LEADING_EDGE": {'description': 'Front of a migrating cell', 'annotations': {'context': 'cell migration'}},
    "TRAILING_EDGE": {'description': 'Rear of a migrating cell', 'annotations': {'context': 'cell migration'}},
    "PROXIMAL_POLE": {'description': 'Pole closer to the cell body', 'annotations': {'context': 'neurons, polarized cells'}},
    "DISTAL_POLE": {'description': 'Pole further from the cell body', 'annotations': {'context': 'neurons, polarized cells'}},
}

class CrystalSystemEnum(RichEnum):
    """
    The seven crystal systems in crystallography
    """
    # Enum members
    TRICLINIC = "TRICLINIC"
    MONOCLINIC = "MONOCLINIC"
    ORTHORHOMBIC = "ORTHORHOMBIC"
    TETRAGONAL = "TETRAGONAL"
    TRIGONAL = "TRIGONAL"
    HEXAGONAL = "HEXAGONAL"
    CUBIC = "CUBIC"

# Set metadata after class creation
CrystalSystemEnum._metadata = {
    "TRICLINIC": {'description': 'Crystal system with no symmetry constraints (a≠b≠c, α≠β≠γ≠90°)', 'meaning': 'ENM:9000022', 'aliases': ['anorthic']},
    "MONOCLINIC": {'description': 'Crystal system with one twofold axis of symmetry (a≠b≠c, α=γ=90°≠β)', 'meaning': 'ENM:9000029'},
    "ORTHORHOMBIC": {'description': 'Crystal system with three mutually perpendicular axes (a≠b≠c, α=β=γ=90°)', 'meaning': 'ENM:9000031', 'aliases': ['rhombic']},
    "TETRAGONAL": {'description': 'Crystal system with one fourfold axis (a=b≠c, α=β=γ=90°)', 'meaning': 'ENM:9000032'},
    "TRIGONAL": {'description': 'Crystal system with one threefold axis (a=b=c, α=β=γ≠90°)', 'meaning': 'ENM:9000054', 'aliases': ['rhombohedral']},
    "HEXAGONAL": {'description': 'Crystal system with one sixfold axis (a=b≠c, α=β=90°, γ=120°)', 'meaning': 'PATO:0002509'},
    "CUBIC": {'description': 'Crystal system with four threefold axes (a=b=c, α=β=γ=90°)', 'meaning': 'ENM:9000035', 'aliases': ['isometric']},
}

class BravaisLatticeEnum(RichEnum):
    """
    The 14 Bravais lattices describing all possible crystal lattices
    """
    # Enum members
    PRIMITIVE_TRICLINIC = "PRIMITIVE_TRICLINIC"
    PRIMITIVE_MONOCLINIC = "PRIMITIVE_MONOCLINIC"
    BASE_CENTERED_MONOCLINIC = "BASE_CENTERED_MONOCLINIC"
    PRIMITIVE_ORTHORHOMBIC = "PRIMITIVE_ORTHORHOMBIC"
    BASE_CENTERED_ORTHORHOMBIC = "BASE_CENTERED_ORTHORHOMBIC"
    BODY_CENTERED_ORTHORHOMBIC = "BODY_CENTERED_ORTHORHOMBIC"
    FACE_CENTERED_ORTHORHOMBIC = "FACE_CENTERED_ORTHORHOMBIC"
    PRIMITIVE_TETRAGONAL = "PRIMITIVE_TETRAGONAL"
    BODY_CENTERED_TETRAGONAL = "BODY_CENTERED_TETRAGONAL"
    PRIMITIVE_TRIGONAL = "PRIMITIVE_TRIGONAL"
    PRIMITIVE_HEXAGONAL = "PRIMITIVE_HEXAGONAL"
    PRIMITIVE_CUBIC = "PRIMITIVE_CUBIC"
    BODY_CENTERED_CUBIC = "BODY_CENTERED_CUBIC"
    FACE_CENTERED_CUBIC = "FACE_CENTERED_CUBIC"

# Set metadata after class creation
BravaisLatticeEnum._metadata = {
    "PRIMITIVE_TRICLINIC": {'description': 'Primitive triclinic lattice (aP)', 'aliases': ['aP']},
    "PRIMITIVE_MONOCLINIC": {'description': 'Primitive monoclinic lattice (mP)', 'aliases': ['mP']},
    "BASE_CENTERED_MONOCLINIC": {'description': 'Base-centered monoclinic lattice (mC)', 'aliases': ['mC', 'mS']},
    "PRIMITIVE_ORTHORHOMBIC": {'description': 'Primitive orthorhombic lattice (oP)', 'aliases': ['oP']},
    "BASE_CENTERED_ORTHORHOMBIC": {'description': 'Base-centered orthorhombic lattice (oC)', 'aliases': ['oC', 'oS']},
    "BODY_CENTERED_ORTHORHOMBIC": {'description': 'Body-centered orthorhombic lattice (oI)', 'aliases': ['oI']},
    "FACE_CENTERED_ORTHORHOMBIC": {'description': 'Face-centered orthorhombic lattice (oF)', 'aliases': ['oF']},
    "PRIMITIVE_TETRAGONAL": {'description': 'Primitive tetragonal lattice (tP)', 'aliases': ['tP']},
    "BODY_CENTERED_TETRAGONAL": {'description': 'Body-centered tetragonal lattice (tI)', 'aliases': ['tI']},
    "PRIMITIVE_TRIGONAL": {'description': 'Primitive trigonal/rhombohedral lattice (hR)', 'aliases': ['hR']},
    "PRIMITIVE_HEXAGONAL": {'description': 'Primitive hexagonal lattice (hP)', 'aliases': ['hP']},
    "PRIMITIVE_CUBIC": {'description': 'Simple cubic lattice (cP)', 'aliases': ['cP', 'SC']},
    "BODY_CENTERED_CUBIC": {'description': 'Body-centered cubic lattice (cI)', 'aliases': ['cI', 'BCC']},
    "FACE_CENTERED_CUBIC": {'description': 'Face-centered cubic lattice (cF)', 'aliases': ['cF', 'FCC']},
}

class ElectricalConductivityEnum(RichEnum):
    """
    Classification of materials by electrical conductivity
    """
    # Enum members
    CONDUCTOR = "CONDUCTOR"
    SEMICONDUCTOR = "SEMICONDUCTOR"
    INSULATOR = "INSULATOR"
    SUPERCONDUCTOR = "SUPERCONDUCTOR"

# Set metadata after class creation
ElectricalConductivityEnum._metadata = {
    "CONDUCTOR": {'description': 'Material with high electrical conductivity (resistivity < 10^-5 Ω·m)', 'aliases': ['metal']},
    "SEMICONDUCTOR": {'description': 'Material with intermediate electrical conductivity (10^-5 to 10^8 Ω·m)', 'meaning': 'NCIT:C172788', 'aliases': ['semi']},
    "INSULATOR": {'description': 'Material with very low electrical conductivity (resistivity > 10^8 Ω·m)', 'aliases': ['dielectric']},
    "SUPERCONDUCTOR": {'description': 'Material with zero electrical resistance below critical temperature'},
}

class MagneticPropertyEnum(RichEnum):
    """
    Classification of materials by magnetic properties
    """
    # Enum members
    DIAMAGNETIC = "DIAMAGNETIC"
    PARAMAGNETIC = "PARAMAGNETIC"
    FERROMAGNETIC = "FERROMAGNETIC"
    FERRIMAGNETIC = "FERRIMAGNETIC"
    ANTIFERROMAGNETIC = "ANTIFERROMAGNETIC"

# Set metadata after class creation
MagneticPropertyEnum._metadata = {
    "DIAMAGNETIC": {'description': 'Weakly repelled by magnetic fields'},
    "PARAMAGNETIC": {'description': 'Weakly attracted to magnetic fields'},
    "FERROMAGNETIC": {'description': 'Strongly attracted to magnetic fields, can be permanently magnetized'},
    "FERRIMAGNETIC": {'description': 'Similar to ferromagnetic but with opposing magnetic moments'},
    "ANTIFERROMAGNETIC": {'description': 'Adjacent magnetic moments cancel each other'},
}

class OpticalPropertyEnum(RichEnum):
    """
    Optical properties of materials
    """
    # Enum members
    TRANSPARENT = "TRANSPARENT"
    TRANSLUCENT = "TRANSLUCENT"
    OPAQUE = "OPAQUE"
    REFLECTIVE = "REFLECTIVE"
    ABSORBING = "ABSORBING"
    FLUORESCENT = "FLUORESCENT"
    PHOSPHORESCENT = "PHOSPHORESCENT"

# Set metadata after class creation
OpticalPropertyEnum._metadata = {
    "TRANSPARENT": {'description': 'Allows light to pass through with minimal scattering', 'meaning': 'PATO:0000964'},
    "TRANSLUCENT": {'description': 'Allows light to pass through but with significant scattering'},
    "OPAQUE": {'description': 'Does not allow light to pass through', 'meaning': 'PATO:0000963'},
    "REFLECTIVE": {'description': 'Reflects most incident light'},
    "ABSORBING": {'description': 'Absorbs most incident light'},
    "FLUORESCENT": {'description': 'Emits light when excited by radiation'},
    "PHOSPHORESCENT": {'description': 'Continues to emit light after excitation stops'},
}

class ThermalConductivityEnum(RichEnum):
    """
    Classification by thermal conductivity
    """
    # Enum members
    HIGH_THERMAL_CONDUCTOR = "HIGH_THERMAL_CONDUCTOR"
    MODERATE_THERMAL_CONDUCTOR = "MODERATE_THERMAL_CONDUCTOR"
    THERMAL_INSULATOR = "THERMAL_INSULATOR"

# Set metadata after class creation
ThermalConductivityEnum._metadata = {
    "HIGH_THERMAL_CONDUCTOR": {'description': 'High thermal conductivity (>100 W/m·K)', 'aliases': ['thermal conductor']},
    "MODERATE_THERMAL_CONDUCTOR": {'description': 'Moderate thermal conductivity (1-100 W/m·K)'},
    "THERMAL_INSULATOR": {'description': 'Low thermal conductivity (<1 W/m·K)', 'aliases': ['thermal barrier']},
}

class MechanicalBehaviorEnum(RichEnum):
    """
    Mechanical behavior of materials under stress
    """
    # Enum members
    ELASTIC = "ELASTIC"
    PLASTIC = "PLASTIC"
    BRITTLE = "BRITTLE"
    DUCTILE = "DUCTILE"
    MALLEABLE = "MALLEABLE"
    TOUGH = "TOUGH"
    VISCOELASTIC = "VISCOELASTIC"

# Set metadata after class creation
MechanicalBehaviorEnum._metadata = {
    "ELASTIC": {'description': 'Returns to original shape after stress removal', 'meaning': 'PATO:0001171'},
    "PLASTIC": {'description': 'Undergoes permanent deformation under stress', 'meaning': 'PATO:0001172'},
    "BRITTLE": {'description': 'Breaks without significant plastic deformation', 'meaning': 'PATO:0002477'},
    "DUCTILE": {'description': 'Can be drawn into wires, undergoes large plastic deformation'},
    "MALLEABLE": {'description': 'Can be hammered into sheets'},
    "TOUGH": {'description': 'High resistance to fracture'},
    "VISCOELASTIC": {'description': 'Exhibits both viscous and elastic characteristics'},
}

class MicroscopyMethodEnum(RichEnum):
    """
    Microscopy techniques for material characterization
    """
    # Enum members
    SEM = "SEM"
    TEM = "TEM"
    STEM = "STEM"
    AFM = "AFM"
    STM = "STM"
    OPTICAL = "OPTICAL"
    CONFOCAL = "CONFOCAL"

# Set metadata after class creation
MicroscopyMethodEnum._metadata = {
    "SEM": {'description': 'Scanning Electron Microscopy', 'meaning': 'CHMO:0000073', 'aliases': ['Scanning Electron Microscopy', 'SEM']},
    "TEM": {'description': 'Transmission Electron Microscopy', 'meaning': 'CHMO:0000080', 'aliases': ['Transmission Electron Microscopy', 'TEM']},
    "STEM": {'description': 'Scanning Transmission Electron Microscopy', 'aliases': ['Scanning Transmission Electron Microscopy']},
    "AFM": {'description': 'Atomic Force Microscopy', 'meaning': 'CHMO:0000113', 'aliases': ['Atomic Force Microscopy', 'AFM']},
    "STM": {'description': 'Scanning Tunneling Microscopy', 'meaning': 'CHMO:0000132', 'aliases': ['Scanning Tunneling Microscopy', 'STM']},
    "OPTICAL": {'description': 'Optical/Light Microscopy', 'meaning': 'CHMO:0000102', 'aliases': ['Light Microscopy', 'Optical Microscopy', 'OPTICAL']},
    "CONFOCAL": {'description': 'Confocal Laser Scanning Microscopy', 'meaning': 'CHMO:0000089', 'aliases': ['CLSM', 'CONFOCAL', 'Confocal']},
}

class SpectroscopyMethodEnum(RichEnum):
    """
    Spectroscopy techniques for material analysis
    """
    # Enum members
    XRD = "XRD"
    XPS = "XPS"
    EDS = "EDS"
    FTIR = "FTIR"
    RAMAN = "RAMAN"
    UV_VIS = "UV_VIS"
    NMR = "NMR"
    XRF = "XRF"

# Set metadata after class creation
SpectroscopyMethodEnum._metadata = {
    "XRD": {'description': 'X-ray Diffraction', 'meaning': 'CHMO:0000156', 'aliases': ['X-ray Diffraction']},
    "XPS": {'description': 'X-ray Photoelectron Spectroscopy', 'meaning': 'CHMO:0000404', 'aliases': ['ESCA', 'X-ray Photoelectron Spectroscopy']},
    "EDS": {'description': 'Energy Dispersive X-ray Spectroscopy', 'meaning': 'CHMO:0000309', 'aliases': ['EDX', 'EDXS', 'EDS']},
    "FTIR": {'description': 'Fourier Transform Infrared Spectroscopy', 'meaning': 'CHMO:0000636', 'aliases': ['FT-IR', 'FTIR']},
    "RAMAN": {'description': 'Raman Spectroscopy', 'meaning': 'CHMO:0000656', 'aliases': ['Raman Spectroscopy']},
    "UV_VIS": {'description': 'Ultraviolet-Visible Spectroscopy', 'meaning': 'CHMO:0000292', 'aliases': ['UV-Visible', 'UV-Vis', 'UV_VIS']},
    "NMR": {'description': 'Nuclear Magnetic Resonance Spectroscopy', 'meaning': 'CHMO:0000591', 'aliases': ['Nuclear Magnetic Resonance', 'NMR']},
    "XRF": {'description': 'X-ray Fluorescence Spectroscopy', 'meaning': 'CHMO:0000307', 'aliases': ['X-ray Fluorescence', 'XRF']},
}

class ThermalAnalysisMethodEnum(RichEnum):
    """
    Thermal analysis techniques
    """
    # Enum members
    DSC = "DSC"
    TGA = "TGA"
    DTA = "DTA"
    TMA = "TMA"
    DMTA = "DMTA"

# Set metadata after class creation
ThermalAnalysisMethodEnum._metadata = {
    "DSC": {'description': 'Differential Scanning Calorimetry', 'meaning': 'CHMO:0000684', 'aliases': ['Differential Scanning Calorimetry']},
    "TGA": {'description': 'Thermogravimetric Analysis', 'meaning': 'CHMO:0000690', 'aliases': ['Thermogravimetric Analysis', 'TGA']},
    "DTA": {'description': 'Differential Thermal Analysis', 'meaning': 'CHMO:0000687', 'aliases': ['Differential Thermal Analysis']},
    "TMA": {'description': 'Thermomechanical Analysis', 'aliases': ['Thermomechanical Analysis']},
    "DMTA": {'description': 'Dynamic Mechanical Thermal Analysis', 'aliases': ['DMA', 'Dynamic Mechanical Analysis']},
}

class MechanicalTestingMethodEnum(RichEnum):
    """
    Mechanical testing methods
    """
    # Enum members
    TENSILE = "TENSILE"
    COMPRESSION = "COMPRESSION"
    HARDNESS = "HARDNESS"
    IMPACT = "IMPACT"
    FATIGUE = "FATIGUE"
    CREEP = "CREEP"
    FRACTURE_TOUGHNESS = "FRACTURE_TOUGHNESS"
    NANOINDENTATION = "NANOINDENTATION"

# Set metadata after class creation
MechanicalTestingMethodEnum._metadata = {
    "TENSILE": {'description': 'Tensile strength testing'},
    "COMPRESSION": {'description': 'Compression strength testing'},
    "HARDNESS": {'description': 'Hardness testing (Vickers, Rockwell, Brinell)'},
    "IMPACT": {'description': 'Impact resistance testing (Charpy, Izod)'},
    "FATIGUE": {'description': 'Fatigue testing under cyclic loading'},
    "CREEP": {'description': 'Creep testing under sustained load'},
    "FRACTURE_TOUGHNESS": {'description': 'Fracture toughness testing'},
    "NANOINDENTATION": {'description': 'Nanoindentation for nanoscale mechanical properties'},
}

class MaterialClassEnum(RichEnum):
    """
    Major classes of materials
    """
    # Enum members
    METAL = "METAL"
    CERAMIC = "CERAMIC"
    POLYMER = "POLYMER"
    COMPOSITE = "COMPOSITE"
    SEMICONDUCTOR = "SEMICONDUCTOR"
    BIOMATERIAL = "BIOMATERIAL"
    NANOMATERIAL = "NANOMATERIAL"

# Set metadata after class creation
MaterialClassEnum._metadata = {
    "METAL": {'description': 'Metallic materials with metallic bonding', 'meaning': 'ENVO:01001069', 'aliases': ['Metal', 'METAL']},
    "CERAMIC": {'description': 'Inorganic non-metallic materials', 'meaning': 'ENVO:03501307'},
    "POLYMER": {'description': 'Large molecules composed of repeating units', 'meaning': 'CHEBI:60027'},
    "COMPOSITE": {'description': 'Materials made from two or more constituent materials', 'meaning': 'NCIT:C61520'},
    "SEMICONDUCTOR": {'description': 'Materials with electrical conductivity between conductors and insulators', 'meaning': 'NCIT:C172788'},
    "BIOMATERIAL": {'description': 'Materials designed to interact with biological systems', 'meaning': 'NCIT:C16338', 'aliases': ['Biomaterial', 'BIOMATERIAL']},
    "NANOMATERIAL": {'description': 'Materials with at least one dimension in nanoscale (1-100 nm)', 'meaning': 'NCIT:C62371'},
}

class PolymerTypeEnum(RichEnum):
    """
    Types of polymer materials
    """
    # Enum members
    THERMOPLASTIC = "THERMOPLASTIC"
    THERMOSET = "THERMOSET"
    ELASTOMER = "ELASTOMER"
    BIOPOLYMER = "BIOPOLYMER"
    CONDUCTING_POLYMER = "CONDUCTING_POLYMER"

# Set metadata after class creation
PolymerTypeEnum._metadata = {
    "THERMOPLASTIC": {'description': 'Polymer that becomes moldable above specific temperature', 'meaning': 'PATO:0040070'},
    "THERMOSET": {'description': 'Polymer that irreversibly hardens when cured', 'meaning': 'ENVO:06105005', 'aliases': ['thermosetting polymer', 'Thermoset', 'THERMOSET']},
    "ELASTOMER": {'description': 'Polymer with elastic properties', 'meaning': 'SNOMED:261777007', 'aliases': ['rubber']},
    "BIOPOLYMER": {'description': 'Polymer produced by living organisms', 'meaning': 'NCIT:C73478'},
    "CONDUCTING_POLYMER": {'description': 'Polymer that conducts electricity', 'aliases': ['conducting polymer']},
}

class MetalTypeEnum(RichEnum):
    """
    Types of metallic materials
    """
    # Enum members
    FERROUS = "FERROUS"
    NON_FERROUS = "NON_FERROUS"
    NOBLE_METAL = "NOBLE_METAL"
    REFRACTORY_METAL = "REFRACTORY_METAL"
    LIGHT_METAL = "LIGHT_METAL"
    HEAVY_METAL = "HEAVY_METAL"

# Set metadata after class creation
MetalTypeEnum._metadata = {
    "FERROUS": {'description': 'Iron-based metals and alloys', 'meaning': 'SNOMED:264354006', 'aliases': ['iron-based']},
    "NON_FERROUS": {'description': 'Metals and alloys not containing iron', 'meaning': 'SNOMED:264879001'},
    "NOBLE_METAL": {'description': 'Metals resistant to corrosion and oxidation'},
    "REFRACTORY_METAL": {'description': 'Metals with very high melting points (>2000°C)'},
    "LIGHT_METAL": {'description': 'Low density metals (density < 5 g/cm³)', 'meaning': 'SNOMED:65436002'},
    "HEAVY_METAL": {'description': 'High density metals (density > 5 g/cm³)', 'meaning': 'CHEBI:5631'},
}

class CompositeTypeEnum(RichEnum):
    """
    Types of composite materials
    """
    # Enum members
    FIBER_REINFORCED = "FIBER_REINFORCED"
    PARTICLE_REINFORCED = "PARTICLE_REINFORCED"
    LAMINAR_COMPOSITE = "LAMINAR_COMPOSITE"
    METAL_MATRIX_COMPOSITE = "METAL_MATRIX_COMPOSITE"
    CERAMIC_MATRIX_COMPOSITE = "CERAMIC_MATRIX_COMPOSITE"
    POLYMER_MATRIX_COMPOSITE = "POLYMER_MATRIX_COMPOSITE"

# Set metadata after class creation
CompositeTypeEnum._metadata = {
    "FIBER_REINFORCED": {'description': 'Composite with fiber reinforcement', 'aliases': ['FRC']},
    "PARTICLE_REINFORCED": {'description': 'Composite with particle reinforcement'},
    "LAMINAR_COMPOSITE": {'description': 'Composite with layered structure', 'aliases': ['laminate']},
    "METAL_MATRIX_COMPOSITE": {'description': 'Composite with metal matrix', 'aliases': ['MMC']},
    "CERAMIC_MATRIX_COMPOSITE": {'description': 'Composite with ceramic matrix', 'aliases': ['CMC']},
    "POLYMER_MATRIX_COMPOSITE": {'description': 'Composite with polymer matrix', 'aliases': ['PMC']},
}

class SynthesisMethodEnum(RichEnum):
    """
    Common material synthesis and processing methods
    """
    # Enum members
    SOL_GEL = "SOL_GEL"
    HYDROTHERMAL = "HYDROTHERMAL"
    SOLVOTHERMAL = "SOLVOTHERMAL"
    CVD = "CVD"
    PVD = "PVD"
    ALD = "ALD"
    ELECTRODEPOSITION = "ELECTRODEPOSITION"
    BALL_MILLING = "BALL_MILLING"
    PRECIPITATION = "PRECIPITATION"
    SINTERING = "SINTERING"
    MELT_PROCESSING = "MELT_PROCESSING"
    SOLUTION_CASTING = "SOLUTION_CASTING"
    SPIN_COATING = "SPIN_COATING"
    DIP_COATING = "DIP_COATING"
    SPRAY_COATING = "SPRAY_COATING"

# Set metadata after class creation
SynthesisMethodEnum._metadata = {
    "SOL_GEL": {'description': 'Synthesis from solution through gel formation', 'aliases': ['sol-gel process']},
    "HYDROTHERMAL": {'description': 'Synthesis using high temperature aqueous solutions', 'aliases': ['hydrothermal synthesis']},
    "SOLVOTHERMAL": {'description': 'Synthesis using non-aqueous solvents at high temperature/pressure'},
    "CVD": {'description': 'Chemical Vapor Deposition', 'meaning': 'CHMO:0001314', 'aliases': ['Chemical Vapor Deposition', 'CVD']},
    "PVD": {'description': 'Physical Vapor Deposition', 'meaning': 'CHMO:0001356', 'aliases': ['Physical Vapor Deposition', 'PVD']},
    "ALD": {'description': 'Atomic Layer Deposition', 'aliases': ['Atomic Layer Deposition']},
    "ELECTRODEPOSITION": {'description': 'Deposition using electric current', 'meaning': 'CHMO:0001331', 'aliases': ['electroplating', 'Electrodeposition', 'ELECTRODEPOSITION']},
    "BALL_MILLING": {'description': 'Mechanical alloying using ball mill', 'aliases': ['mechanical alloying']},
    "PRECIPITATION": {'description': 'Formation of solid from solution', 'meaning': 'CHMO:0001688', 'aliases': ['Precipitation', 'PRECIPITATION']},
    "SINTERING": {'description': 'Compacting and forming solid mass by heat/pressure'},
    "MELT_PROCESSING": {'description': 'Processing from molten state', 'aliases': ['melt casting']},
    "SOLUTION_CASTING": {'description': 'Casting from solution'},
    "SPIN_COATING": {'description': 'Coating by spinning substrate', 'meaning': 'CHMO:0001472'},
    "DIP_COATING": {'description': 'Coating by dipping in solution', 'meaning': 'CHMO:0001471'},
    "SPRAY_COATING": {'description': 'Coating by spraying'},
}

class CrystalGrowthMethodEnum(RichEnum):
    """
    Methods for growing single crystals
    """
    # Enum members
    CZOCHRALSKI = "CZOCHRALSKI"
    BRIDGMAN = "BRIDGMAN"
    FLOAT_ZONE = "FLOAT_ZONE"
    FLUX_GROWTH = "FLUX_GROWTH"
    VAPOR_TRANSPORT = "VAPOR_TRANSPORT"
    HYDROTHERMAL_GROWTH = "HYDROTHERMAL_GROWTH"
    LPE = "LPE"
    MBE = "MBE"
    MOCVD = "MOCVD"

# Set metadata after class creation
CrystalGrowthMethodEnum._metadata = {
    "CZOCHRALSKI": {'description': 'Crystal pulling from melt', 'aliases': ['CZ', 'crystal pulling']},
    "BRIDGMAN": {'description': 'Directional solidification method', 'aliases': ['Bridgman-Stockbarger']},
    "FLOAT_ZONE": {'description': 'Zone melting without crucible', 'aliases': ['FZ', 'zone refining']},
    "FLUX_GROWTH": {'description': 'Crystal growth from high temperature solution'},
    "VAPOR_TRANSPORT": {'description': 'Crystal growth via vapor phase transport', 'aliases': ['CVT']},
    "HYDROTHERMAL_GROWTH": {'description': 'Crystal growth in aqueous solution under pressure'},
    "LPE": {'description': 'Liquid Phase Epitaxy', 'aliases': ['Liquid Phase Epitaxy']},
    "MBE": {'description': 'Molecular Beam Epitaxy', 'meaning': 'CHMO:0001341', 'aliases': ['Molecular Beam Epitaxy', 'MBE']},
    "MOCVD": {'description': 'Metal-Organic Chemical Vapor Deposition', 'aliases': ['MOVPE']},
}

class AdditiveManufacturingEnum(RichEnum):
    """
    3D printing and additive manufacturing methods
    """
    # Enum members
    FDM = "FDM"
    SLA = "SLA"
    SLS = "SLS"
    SLM = "SLM"
    EBM = "EBM"
    BINDER_JETTING = "BINDER_JETTING"
    MATERIAL_JETTING = "MATERIAL_JETTING"
    DED = "DED"

# Set metadata after class creation
AdditiveManufacturingEnum._metadata = {
    "FDM": {'description': 'Fused Deposition Modeling', 'aliases': ['FFF', 'Fused Filament Fabrication']},
    "SLA": {'description': 'Stereolithography', 'aliases': ['Stereolithography']},
    "SLS": {'description': 'Selective Laser Sintering', 'aliases': ['Selective Laser Sintering']},
    "SLM": {'description': 'Selective Laser Melting', 'aliases': ['Selective Laser Melting']},
    "EBM": {'description': 'Electron Beam Melting', 'aliases': ['Electron Beam Melting']},
    "BINDER_JETTING": {'description': 'Powder bed with liquid binder'},
    "MATERIAL_JETTING": {'description': 'Droplet deposition of materials', 'aliases': ['PolyJet']},
    "DED": {'description': 'Directed Energy Deposition', 'aliases': ['Directed Energy Deposition']},
}

class TraditionalPigmentEnum(RichEnum):
    """
    Traditional artist pigments and their colors
    """
    # Enum members
    TITANIUM_WHITE = "TITANIUM_WHITE"
    ZINC_WHITE = "ZINC_WHITE"
    LEAD_WHITE = "LEAD_WHITE"
    CADMIUM_YELLOW = "CADMIUM_YELLOW"
    CHROME_YELLOW = "CHROME_YELLOW"
    NAPLES_YELLOW = "NAPLES_YELLOW"
    YELLOW_OCHRE = "YELLOW_OCHRE"
    CADMIUM_ORANGE = "CADMIUM_ORANGE"
    CADMIUM_RED = "CADMIUM_RED"
    VERMILION = "VERMILION"
    ALIZARIN_CRIMSON = "ALIZARIN_CRIMSON"
    CARMINE = "CARMINE"
    BURNT_SIENNA = "BURNT_SIENNA"
    RAW_SIENNA = "RAW_SIENNA"
    BURNT_UMBER = "BURNT_UMBER"
    RAW_UMBER = "RAW_UMBER"
    VAN_DYKE_BROWN = "VAN_DYKE_BROWN"
    PRUSSIAN_BLUE = "PRUSSIAN_BLUE"
    ULTRAMARINE = "ULTRAMARINE"
    COBALT_BLUE = "COBALT_BLUE"
    CERULEAN_BLUE = "CERULEAN_BLUE"
    PHTHALO_BLUE = "PHTHALO_BLUE"
    VIRIDIAN = "VIRIDIAN"
    CHROME_GREEN = "CHROME_GREEN"
    PHTHALO_GREEN = "PHTHALO_GREEN"
    TERRE_VERTE = "TERRE_VERTE"
    TYRIAN_PURPLE = "TYRIAN_PURPLE"
    MANGANESE_VIOLET = "MANGANESE_VIOLET"
    MARS_BLACK = "MARS_BLACK"
    IVORY_BLACK = "IVORY_BLACK"
    LAMP_BLACK = "LAMP_BLACK"

# Set metadata after class creation
TraditionalPigmentEnum._metadata = {
    "TITANIUM_WHITE": {'description': 'Titanium white (Titanium dioxide)', 'meaning': 'CHEBI:51050', 'annotations': {'hex': 'FFFFFF', 'chemical': 'TiO2', 'discovered': '1916'}},
    "ZINC_WHITE": {'description': 'Zinc white (Zinc oxide)', 'meaning': 'CHEBI:36560', 'annotations': {'hex': 'FEFEFE', 'chemical': 'ZnO'}},
    "LEAD_WHITE": {'description': 'Lead white (Basic lead carbonate) - toxic', 'annotations': {'hex': 'F8F8F8', 'chemical': '2PbCO3·Pb(OH)2', 'warning': 'highly toxic, historical use'}},
    "CADMIUM_YELLOW": {'description': 'Cadmium yellow (Cadmium sulfide)', 'meaning': 'CHEBI:50834', 'annotations': {'hex': 'FFF600', 'chemical': 'CdS', 'warning': 'toxic'}},
    "CHROME_YELLOW": {'description': 'Chrome yellow (Lead chromate) - toxic', 'annotations': {'hex': 'FFC200', 'chemical': 'PbCrO4', 'warning': 'highly toxic'}},
    "NAPLES_YELLOW": {'description': 'Naples yellow (Lead antimonate)', 'annotations': {'hex': 'FDD5B1', 'chemical': 'Pb(SbO3)2', 'historical': 'ancient pigment'}},
    "YELLOW_OCHRE": {'description': 'Yellow ochre (Iron oxide hydroxide)', 'annotations': {'hex': 'CC7722', 'chemical': 'FeO(OH)·nH2O', 'natural': 'earth pigment'}},
    "CADMIUM_ORANGE": {'description': 'Cadmium orange (Cadmium selenide)', 'annotations': {'hex': 'FF6600', 'chemical': 'CdS·CdSe', 'warning': 'toxic'}},
    "CADMIUM_RED": {'description': 'Cadmium red (Cadmium selenide)', 'meaning': 'CHEBI:50835', 'annotations': {'hex': 'E30022', 'chemical': 'CdSe', 'warning': 'toxic'}},
    "VERMILION": {'description': 'Vermilion/Cinnabar (Mercury sulfide)', 'annotations': {'hex': 'E34234', 'chemical': 'HgS', 'warning': 'highly toxic'}},
    "ALIZARIN_CRIMSON": {'description': 'Alizarin crimson (synthetic)', 'meaning': 'CHEBI:16866', 'annotations': {'hex': 'E32636', 'chemical': 'C14H8O4', 'organic': 'synthetic organic'}},
    "CARMINE": {'description': 'Carmine (from cochineal insects)', 'annotations': {'hex': '960018', 'source': 'cochineal insects', 'natural': 'organic pigment'}},
    "BURNT_SIENNA": {'description': 'Burnt sienna (heated iron oxide)', 'annotations': {'hex': 'E97451', 'chemical': 'Fe2O3', 'process': 'calcined raw sienna'}},
    "RAW_SIENNA": {'description': 'Raw sienna (Iron oxide with clay)', 'annotations': {'hex': 'C69D52', 'chemical': 'Fe2O3 with clay', 'natural': 'earth pigment'}},
    "BURNT_UMBER": {'description': 'Burnt umber (heated iron/manganese oxide)', 'annotations': {'hex': '8B4513', 'chemical': 'Fe2O3 + MnO2', 'process': 'calcined raw umber'}},
    "RAW_UMBER": {'description': 'Raw umber (Iron/manganese oxide)', 'annotations': {'hex': '734A12', 'chemical': 'Fe2O3 + MnO2', 'natural': 'earth pigment'}},
    "VAN_DYKE_BROWN": {'description': 'Van Dyke brown (organic earth)', 'annotations': {'hex': '664228', 'source': 'peat, lignite', 'warning': 'fugitive color'}},
    "PRUSSIAN_BLUE": {'description': 'Prussian blue (Ferric ferrocyanide)', 'meaning': 'CHEBI:30069', 'annotations': {'hex': '003153', 'chemical': 'Fe4[Fe(CN)6]3', 'discovered': '1706'}},
    "ULTRAMARINE": {'description': 'Ultramarine blue (originally lapis lazuli)', 'annotations': {'hex': '120A8F', 'chemical': 'Na8[Al6Si6O24]Sn', 'historical': 'most expensive pigment'}},
    "COBALT_BLUE": {'description': 'Cobalt blue (Cobalt aluminate)', 'annotations': {'hex': '0047AB', 'chemical': 'CoAl2O4'}},
    "CERULEAN_BLUE": {'description': 'Cerulean blue (Cobalt stannate)', 'annotations': {'hex': '2A52BE', 'chemical': 'Co2SnO4'}},
    "PHTHALO_BLUE": {'description': 'Phthalocyanine blue', 'annotations': {'hex': '000F89', 'chemical': 'C32H16CuN8', 'modern': 'synthetic organic'}},
    "VIRIDIAN": {'description': 'Viridian (Chromium oxide green)', 'annotations': {'hex': '40826D', 'chemical': 'Cr2O3·2H2O'}},
    "CHROME_GREEN": {'description': 'Chrome oxide green', 'annotations': {'hex': '2E5E26', 'chemical': 'Cr2O3'}},
    "PHTHALO_GREEN": {'description': 'Phthalocyanine green', 'annotations': {'hex': '123524', 'chemical': 'C32H16ClCuN8', 'modern': 'synthetic organic'}},
    "TERRE_VERTE": {'description': 'Terre verte/Green earth', 'annotations': {'hex': '6B7F59', 'chemical': 'complex silicate', 'natural': 'earth pigment'}},
    "TYRIAN_PURPLE": {'description': 'Tyrian purple (from murex snails)', 'annotations': {'hex': '66023C', 'source': 'murex snails', 'historical': 'ancient royal purple'}},
    "MANGANESE_VIOLET": {'description': 'Manganese violet', 'annotations': {'hex': '8B3E5F', 'chemical': 'NH4MnP2O7'}},
    "MARS_BLACK": {'description': 'Mars black (Synthetic iron oxide)', 'annotations': {'hex': '010101', 'chemical': 'Fe3O4', 'synthetic': 'iron oxide'}},
    "IVORY_BLACK": {'description': 'Ivory black (Bone char)', 'annotations': {'hex': '1B1B1B', 'source': 'charred bones'}},
    "LAMP_BLACK": {'description': 'Lamp black (Carbon black)', 'annotations': {'hex': '2B2B2B', 'chemical': 'C', 'source': 'soot'}},
}

class IndustrialDyeEnum(RichEnum):
    """
    Industrial and textile dyes
    """
    # Enum members
    INDIGO = "INDIGO"
    ANILINE_BLACK = "ANILINE_BLACK"
    METHYLENE_BLUE = "METHYLENE_BLUE"
    CONGO_RED = "CONGO_RED"
    MALACHITE_GREEN = "MALACHITE_GREEN"
    CRYSTAL_VIOLET = "CRYSTAL_VIOLET"
    EOSIN = "EOSIN"
    SAFRANIN = "SAFRANIN"
    ACID_ORANGE_7 = "ACID_ORANGE_7"
    REACTIVE_BLACK_5 = "REACTIVE_BLACK_5"
    DISPERSE_BLUE_1 = "DISPERSE_BLUE_1"
    VAT_BLUE_1 = "VAT_BLUE_1"

# Set metadata after class creation
IndustrialDyeEnum._metadata = {
    "INDIGO": {'description': 'Indigo dye', 'annotations': {'hex': '4B0082', 'source': 'originally plant-based, now synthetic', 'use': 'denim, textiles'}},
    "ANILINE_BLACK": {'description': 'Aniline black', 'annotations': {'hex': '000000', 'chemical': 'polyaniline', 'use': 'cotton dyeing'}},
    "METHYLENE_BLUE": {'description': 'Methylene blue', 'annotations': {'hex': '1E90FF', 'chemical': 'C16H18ClN3S', 'use': 'biological stain, medical'}},
    "CONGO_RED": {'description': 'Congo red', 'meaning': 'CHEBI:34653', 'annotations': {'hex': 'CC0000', 'chemical': 'C32H22N6Na2O6S2', 'use': 'pH indicator, textile'}},
    "MALACHITE_GREEN": {'description': 'Malachite green', 'meaning': 'CHEBI:11174', 'annotations': {'hex': '0BDA51', 'chemical': 'C23H25ClN2', 'use': 'biological stain'}},
    "CRYSTAL_VIOLET": {'description': 'Crystal violet/Gentian violet', 'meaning': 'CHEBI:41688', 'annotations': {'hex': '9400D3', 'chemical': 'C25H30ClN3', 'use': 'gram staining'}},
    "EOSIN": {'description': 'Eosin Y', 'meaning': 'CHEBI:87199', 'annotations': {'hex': 'FF6B6B', 'chemical': 'C20H6Br4Na2O5', 'use': 'histology stain'}},
    "SAFRANIN": {'description': 'Safranin O', 'annotations': {'hex': 'FF0066', 'chemical': 'C20H19ClN4', 'use': 'biological stain'}},
    "ACID_ORANGE_7": {'description': 'Acid Orange 7 (Orange II)', 'annotations': {'hex': 'FF7F00', 'chemical': 'C16H11N2NaO4S', 'use': 'wool, silk dyeing'}},
    "REACTIVE_BLACK_5": {'description': 'Reactive Black 5', 'annotations': {'hex': '000000', 'use': 'cotton reactive dye'}},
    "DISPERSE_BLUE_1": {'description': 'Disperse Blue 1', 'annotations': {'hex': '1560BD', 'use': 'polyester dyeing'}},
    "VAT_BLUE_1": {'description': 'Vat Blue 1 (Indanthrene blue)', 'annotations': {'hex': '002F5C', 'use': 'cotton vat dyeing'}},
}

class FoodColoringEnum(RichEnum):
    """
    Food coloring and natural food dyes
    """
    # Enum members
    FD_C_RED_40 = "FD_C_RED_40"
    FD_C_YELLOW_5 = "FD_C_YELLOW_5"
    FD_C_YELLOW_6 = "FD_C_YELLOW_6"
    FD_C_BLUE_1 = "FD_C_BLUE_1"
    FD_C_BLUE_2 = "FD_C_BLUE_2"
    FD_C_GREEN_3 = "FD_C_GREEN_3"
    CARAMEL_COLOR = "CARAMEL_COLOR"
    ANNATTO = "ANNATTO"
    TURMERIC = "TURMERIC"
    BEETROOT_RED = "BEETROOT_RED"
    CHLOROPHYLL = "CHLOROPHYLL"
    ANTHOCYANINS = "ANTHOCYANINS"
    PAPRIKA_EXTRACT = "PAPRIKA_EXTRACT"
    SPIRULINA_BLUE = "SPIRULINA_BLUE"

# Set metadata after class creation
FoodColoringEnum._metadata = {
    "FD_C_RED_40": {'description': 'FD&C Red No. 40 (Allura Red)', 'annotations': {'hex': 'E40000', 'E_number': 'E129', 'use': 'beverages, candies'}},
    "FD_C_YELLOW_5": {'description': 'FD&C Yellow No. 5 (Tartrazine)', 'annotations': {'hex': 'FFFF00', 'E_number': 'E102', 'use': 'beverages, desserts'}},
    "FD_C_YELLOW_6": {'description': 'FD&C Yellow No. 6 (Sunset Yellow)', 'annotations': {'hex': 'FFA500', 'E_number': 'E110', 'use': 'snacks, beverages'}},
    "FD_C_BLUE_1": {'description': 'FD&C Blue No. 1 (Brilliant Blue)', 'meaning': 'CHEBI:82411', 'annotations': {'hex': '0033FF', 'E_number': 'E133', 'use': 'beverages, candies'}},
    "FD_C_BLUE_2": {'description': 'FD&C Blue No. 2 (Indigo Carmine)', 'annotations': {'hex': '4B0082', 'E_number': 'E132', 'use': 'beverages, confections'}},
    "FD_C_GREEN_3": {'description': 'FD&C Green No. 3 (Fast Green)', 'annotations': {'hex': '00FF00', 'E_number': 'E143', 'use': 'beverages, desserts'}},
    "CARAMEL_COLOR": {'description': 'Caramel coloring', 'annotations': {'hex': '8B4513', 'E_number': 'E150', 'use': 'cola, sauces'}},
    "ANNATTO": {'description': 'Annatto (natural orange)', 'meaning': 'CHEBI:3150', 'annotations': {'hex': 'FF6600', 'E_number': 'E160b', 'source': 'achiote seeds'}},
    "TURMERIC": {'description': 'Turmeric/Curcumin (natural yellow)', 'meaning': 'CHEBI:3962', 'annotations': {'hex': 'F0E442', 'E_number': 'E100', 'source': 'turmeric root'}},
    "BEETROOT_RED": {'description': 'Beetroot red/Betanin', 'meaning': 'CHEBI:15060', 'annotations': {'hex': 'BC2A4D', 'E_number': 'E162', 'source': 'beets'}},
    "CHLOROPHYLL": {'description': 'Chlorophyll (natural green)', 'meaning': 'CHEBI:28966', 'annotations': {'hex': '4D7C0F', 'E_number': 'E140', 'source': 'plants'}},
    "ANTHOCYANINS": {'description': 'Anthocyanins (natural purple/red)', 'annotations': {'hex': '6B3AA0', 'E_number': 'E163', 'source': 'berries, grapes'}},
    "PAPRIKA_EXTRACT": {'description': 'Paprika extract', 'annotations': {'hex': 'E85D00', 'E_number': 'E160c', 'source': 'paprika peppers'}},
    "SPIRULINA_BLUE": {'description': 'Spirulina extract (phycocyanin)', 'annotations': {'hex': '1E88E5', 'source': 'spirulina algae', 'natural': 'true'}},
}

class AutomobilePaintColorEnum(RichEnum):
    """
    Common automobile paint colors
    """
    # Enum members
    ARCTIC_WHITE = "ARCTIC_WHITE"
    MIDNIGHT_BLACK = "MIDNIGHT_BLACK"
    SILVER_METALLIC = "SILVER_METALLIC"
    GUNMETAL_GRAY = "GUNMETAL_GRAY"
    RACING_RED = "RACING_RED"
    CANDY_APPLE_RED = "CANDY_APPLE_RED"
    ELECTRIC_BLUE = "ELECTRIC_BLUE"
    BRITISH_RACING_GREEN = "BRITISH_RACING_GREEN"
    PEARL_WHITE = "PEARL_WHITE"
    CHAMPAGNE_GOLD = "CHAMPAGNE_GOLD"
    COPPER_BRONZE = "COPPER_BRONZE"
    MIAMI_BLUE = "MIAMI_BLUE"

# Set metadata after class creation
AutomobilePaintColorEnum._metadata = {
    "ARCTIC_WHITE": {'description': 'Arctic White', 'meaning': 'HEX:FFFFFF', 'annotations': {'type': 'solid'}},
    "MIDNIGHT_BLACK": {'description': 'Midnight Black', 'meaning': 'HEX:000000', 'annotations': {'type': 'metallic'}},
    "SILVER_METALLIC": {'description': 'Silver Metallic', 'meaning': 'HEX:C0C0C0', 'annotations': {'type': 'metallic'}},
    "GUNMETAL_GRAY": {'description': 'Gunmetal Gray', 'meaning': 'HEX:2A3439', 'annotations': {'type': 'metallic'}},
    "RACING_RED": {'description': 'Racing Red', 'meaning': 'HEX:CE1620', 'annotations': {'type': 'solid'}},
    "CANDY_APPLE_RED": {'description': 'Candy Apple Red', 'meaning': 'HEX:FF0800', 'annotations': {'type': 'metallic'}},
    "ELECTRIC_BLUE": {'description': 'Electric Blue', 'meaning': 'HEX:7DF9FF', 'annotations': {'type': 'metallic'}},
    "BRITISH_RACING_GREEN": {'description': 'British Racing Green', 'meaning': 'HEX:004225', 'annotations': {'type': 'solid', 'historical': 'British racing color'}},
    "PEARL_WHITE": {'description': 'Pearl White', 'meaning': 'HEX:F8F8FF', 'annotations': {'type': 'pearl', 'finish': 'pearlescent'}},
    "CHAMPAGNE_GOLD": {'description': 'Champagne Gold', 'meaning': 'HEX:D4AF37', 'annotations': {'type': 'metallic'}},
    "COPPER_BRONZE": {'description': 'Copper Bronze', 'meaning': 'HEX:B87333', 'annotations': {'type': 'metallic'}},
    "MIAMI_BLUE": {'description': 'Miami Blue', 'meaning': 'HEX:00BFFF', 'annotations': {'type': 'metallic', 'brand': 'Porsche'}},
}

class BasicColorEnum(RichEnum):
    """
    Basic color names commonly used in everyday language
    """
    # Enum members
    RED = "RED"
    GREEN = "GREEN"
    BLUE = "BLUE"
    YELLOW = "YELLOW"
    ORANGE = "ORANGE"
    PURPLE = "PURPLE"
    BLACK = "BLACK"
    WHITE = "WHITE"
    GRAY = "GRAY"
    BROWN = "BROWN"
    PINK = "PINK"
    CYAN = "CYAN"
    MAGENTA = "MAGENTA"

# Set metadata after class creation
BasicColorEnum._metadata = {
    "RED": {'description': 'Primary red color', 'meaning': 'HEX:FF0000', 'annotations': {'wavelength': '700 nm', 'rgb': '255,0,0'}},
    "GREEN": {'description': 'Primary green color', 'meaning': 'HEX:008000', 'annotations': {'wavelength': '550 nm', 'rgb': '0,128,0'}},
    "BLUE": {'description': 'Primary blue color', 'meaning': 'HEX:0000FF', 'annotations': {'wavelength': '450 nm', 'rgb': '0,0,255'}},
    "YELLOW": {'description': 'Secondary yellow color', 'meaning': 'HEX:FFFF00', 'annotations': {'wavelength': '580 nm', 'rgb': '255,255,0'}},
    "ORANGE": {'description': 'Secondary orange color', 'meaning': 'HEX:FFA500', 'annotations': {'wavelength': '600 nm', 'rgb': '255,165,0'}},
    "PURPLE": {'description': 'Secondary purple color', 'meaning': 'HEX:800080', 'annotations': {'wavelength': '420 nm', 'rgb': '128,0,128'}},
    "BLACK": {'description': 'Absence of color', 'meaning': 'HEX:000000', 'annotations': {'rgb': '0,0,0'}},
    "WHITE": {'description': 'All colors combined', 'meaning': 'HEX:FFFFFF', 'annotations': {'rgb': '255,255,255'}},
    "GRAY": {'description': 'Neutral gray', 'meaning': 'HEX:808080', 'annotations': {'rgb': '128,128,128', 'aliases': 'grey'}},
    "BROWN": {'description': 'Brown color', 'meaning': 'HEX:A52A2A', 'annotations': {'rgb': '165,42,42'}},
    "PINK": {'description': 'Light red/pink color', 'meaning': 'HEX:FFC0CB', 'annotations': {'rgb': '255,192,203'}},
    "CYAN": {'description': 'Cyan/aqua color', 'meaning': 'HEX:00FFFF', 'annotations': {'wavelength': '490 nm', 'rgb': '0,255,255'}},
    "MAGENTA": {'description': 'Magenta color', 'meaning': 'HEX:FF00FF', 'annotations': {'rgb': '255,0,255'}},
}

class WebColorEnum(RichEnum):
    """
    Standard HTML/CSS named colors (147 colors)
    """
    # Enum members
    INDIAN_RED = "INDIAN_RED"
    LIGHT_CORAL = "LIGHT_CORAL"
    SALMON = "SALMON"
    DARK_SALMON = "DARK_SALMON"
    CRIMSON = "CRIMSON"
    FIREBRICK = "FIREBRICK"
    DARK_RED = "DARK_RED"
    HOT_PINK = "HOT_PINK"
    DEEP_PINK = "DEEP_PINK"
    LIGHT_PINK = "LIGHT_PINK"
    PALE_VIOLET_RED = "PALE_VIOLET_RED"
    CORAL = "CORAL"
    TOMATO = "TOMATO"
    ORANGE_RED = "ORANGE_RED"
    DARK_ORANGE = "DARK_ORANGE"
    GOLD = "GOLD"
    LIGHT_YELLOW = "LIGHT_YELLOW"
    LEMON_CHIFFON = "LEMON_CHIFFON"
    PAPAYA_WHIP = "PAPAYA_WHIP"
    MOCCASIN = "MOCCASIN"
    PEACH_PUFF = "PEACH_PUFF"
    KHAKI = "KHAKI"
    LAVENDER = "LAVENDER"
    THISTLE = "THISTLE"
    PLUM = "PLUM"
    VIOLET = "VIOLET"
    ORCHID = "ORCHID"
    FUCHSIA = "FUCHSIA"
    MEDIUM_ORCHID = "MEDIUM_ORCHID"
    MEDIUM_PURPLE = "MEDIUM_PURPLE"
    BLUE_VIOLET = "BLUE_VIOLET"
    DARK_VIOLET = "DARK_VIOLET"
    DARK_ORCHID = "DARK_ORCHID"
    DARK_MAGENTA = "DARK_MAGENTA"
    INDIGO = "INDIGO"
    GREEN_YELLOW = "GREEN_YELLOW"
    CHARTREUSE = "CHARTREUSE"
    LAWN_GREEN = "LAWN_GREEN"
    LIME = "LIME"
    LIME_GREEN = "LIME_GREEN"
    PALE_GREEN = "PALE_GREEN"
    LIGHT_GREEN = "LIGHT_GREEN"
    MEDIUM_SPRING_GREEN = "MEDIUM_SPRING_GREEN"
    SPRING_GREEN = "SPRING_GREEN"
    MEDIUM_SEA_GREEN = "MEDIUM_SEA_GREEN"
    SEA_GREEN = "SEA_GREEN"
    FOREST_GREEN = "FOREST_GREEN"
    DARK_GREEN = "DARK_GREEN"
    YELLOW_GREEN = "YELLOW_GREEN"
    OLIVE_DRAB = "OLIVE_DRAB"
    OLIVE = "OLIVE"
    DARK_OLIVE_GREEN = "DARK_OLIVE_GREEN"
    AQUA = "AQUA"
    CYAN = "CYAN"
    LIGHT_CYAN = "LIGHT_CYAN"
    PALE_TURQUOISE = "PALE_TURQUOISE"
    AQUAMARINE = "AQUAMARINE"
    TURQUOISE = "TURQUOISE"
    MEDIUM_TURQUOISE = "MEDIUM_TURQUOISE"
    DARK_TURQUOISE = "DARK_TURQUOISE"
    LIGHT_SEA_GREEN = "LIGHT_SEA_GREEN"
    CADET_BLUE = "CADET_BLUE"
    DARK_CYAN = "DARK_CYAN"
    TEAL = "TEAL"
    LIGHT_STEEL_BLUE = "LIGHT_STEEL_BLUE"
    POWDER_BLUE = "POWDER_BLUE"
    LIGHT_BLUE = "LIGHT_BLUE"
    SKY_BLUE = "SKY_BLUE"
    LIGHT_SKY_BLUE = "LIGHT_SKY_BLUE"
    DEEP_SKY_BLUE = "DEEP_SKY_BLUE"
    DODGER_BLUE = "DODGER_BLUE"
    CORNFLOWER_BLUE = "CORNFLOWER_BLUE"
    STEEL_BLUE = "STEEL_BLUE"
    ROYAL_BLUE = "ROYAL_BLUE"
    MEDIUM_BLUE = "MEDIUM_BLUE"
    DARK_BLUE = "DARK_BLUE"
    NAVY = "NAVY"
    MIDNIGHT_BLUE = "MIDNIGHT_BLUE"
    CORNSILK = "CORNSILK"
    BLANCHED_ALMOND = "BLANCHED_ALMOND"
    BISQUE = "BISQUE"
    NAVAJO_WHITE = "NAVAJO_WHITE"
    WHEAT = "WHEAT"
    BURLYWOOD = "BURLYWOOD"
    TAN = "TAN"
    ROSY_BROWN = "ROSY_BROWN"
    SANDY_BROWN = "SANDY_BROWN"
    GOLDENROD = "GOLDENROD"
    DARK_GOLDENROD = "DARK_GOLDENROD"
    PERU = "PERU"
    CHOCOLATE = "CHOCOLATE"
    SADDLE_BROWN = "SADDLE_BROWN"
    SIENNA = "SIENNA"
    MAROON = "MAROON"
    SNOW = "SNOW"
    HONEYDEW = "HONEYDEW"
    MINT_CREAM = "MINT_CREAM"
    AZURE = "AZURE"
    ALICE_BLUE = "ALICE_BLUE"
    GHOST_WHITE = "GHOST_WHITE"
    WHITE_SMOKE = "WHITE_SMOKE"
    SEASHELL = "SEASHELL"
    BEIGE = "BEIGE"
    OLD_LACE = "OLD_LACE"
    FLORAL_WHITE = "FLORAL_WHITE"
    IVORY = "IVORY"
    ANTIQUE_WHITE = "ANTIQUE_WHITE"
    LINEN = "LINEN"
    LAVENDER_BLUSH = "LAVENDER_BLUSH"
    MISTY_ROSE = "MISTY_ROSE"
    GAINSBORO = "GAINSBORO"
    LIGHT_GRAY = "LIGHT_GRAY"
    SILVER = "SILVER"
    DARK_GRAY = "DARK_GRAY"
    DIM_GRAY = "DIM_GRAY"
    LIGHT_SLATE_GRAY = "LIGHT_SLATE_GRAY"
    SLATE_GRAY = "SLATE_GRAY"
    DARK_SLATE_GRAY = "DARK_SLATE_GRAY"

# Set metadata after class creation
WebColorEnum._metadata = {
    "INDIAN_RED": {'description': 'Indian red', 'meaning': 'HEX:CD5C5C', 'annotations': {'rgb': '205,92,92'}},
    "LIGHT_CORAL": {'description': 'Light coral', 'meaning': 'HEX:F08080', 'annotations': {'rgb': '240,128,128'}},
    "SALMON": {'description': 'Salmon', 'meaning': 'HEX:FA8072', 'annotations': {'rgb': '250,128,114'}},
    "DARK_SALMON": {'description': 'Dark salmon', 'meaning': 'HEX:E9967A', 'annotations': {'rgb': '233,150,122'}},
    "CRIMSON": {'description': 'Crimson', 'meaning': 'HEX:DC143C', 'annotations': {'rgb': '220,20,60'}},
    "FIREBRICK": {'description': 'Firebrick', 'meaning': 'HEX:B22222', 'annotations': {'rgb': '178,34,34'}},
    "DARK_RED": {'description': 'Dark red', 'meaning': 'HEX:8B0000', 'annotations': {'rgb': '139,0,0'}},
    "HOT_PINK": {'description': 'Hot pink', 'meaning': 'HEX:FF69B4', 'annotations': {'rgb': '255,105,180'}},
    "DEEP_PINK": {'description': 'Deep pink', 'meaning': 'HEX:FF1493', 'annotations': {'rgb': '255,20,147'}},
    "LIGHT_PINK": {'description': 'Light pink', 'meaning': 'HEX:FFB6C1', 'annotations': {'rgb': '255,182,193'}},
    "PALE_VIOLET_RED": {'description': 'Pale violet red', 'meaning': 'HEX:DB7093', 'annotations': {'rgb': '219,112,147'}},
    "CORAL": {'description': 'Coral', 'meaning': 'HEX:FF7F50', 'annotations': {'rgb': '255,127,80'}},
    "TOMATO": {'description': 'Tomato', 'meaning': 'HEX:FF6347', 'annotations': {'rgb': '255,99,71'}},
    "ORANGE_RED": {'description': 'Orange red', 'meaning': 'HEX:FF4500', 'annotations': {'rgb': '255,69,0'}},
    "DARK_ORANGE": {'description': 'Dark orange', 'meaning': 'HEX:FF8C00', 'annotations': {'rgb': '255,140,0'}},
    "GOLD": {'description': 'Gold', 'meaning': 'HEX:FFD700', 'annotations': {'rgb': '255,215,0'}},
    "LIGHT_YELLOW": {'description': 'Light yellow', 'meaning': 'HEX:FFFFE0', 'annotations': {'rgb': '255,255,224'}},
    "LEMON_CHIFFON": {'description': 'Lemon chiffon', 'meaning': 'HEX:FFFACD', 'annotations': {'rgb': '255,250,205'}},
    "PAPAYA_WHIP": {'description': 'Papaya whip', 'meaning': 'HEX:FFEFD5', 'annotations': {'rgb': '255,239,213'}},
    "MOCCASIN": {'description': 'Moccasin', 'meaning': 'HEX:FFE4B5', 'annotations': {'rgb': '255,228,181'}},
    "PEACH_PUFF": {'description': 'Peach puff', 'meaning': 'HEX:FFDAB9', 'annotations': {'rgb': '255,218,185'}},
    "KHAKI": {'description': 'Khaki', 'meaning': 'HEX:F0E68C', 'annotations': {'rgb': '240,230,140'}},
    "LAVENDER": {'description': 'Lavender', 'meaning': 'HEX:E6E6FA', 'annotations': {'rgb': '230,230,250'}},
    "THISTLE": {'description': 'Thistle', 'meaning': 'HEX:D8BFD8', 'annotations': {'rgb': '216,191,216'}},
    "PLUM": {'description': 'Plum', 'meaning': 'HEX:DDA0DD', 'annotations': {'rgb': '221,160,221'}},
    "VIOLET": {'description': 'Violet', 'meaning': 'HEX:EE82EE', 'annotations': {'rgb': '238,130,238'}},
    "ORCHID": {'description': 'Orchid', 'meaning': 'HEX:DA70D6', 'annotations': {'rgb': '218,112,214'}},
    "FUCHSIA": {'description': 'Fuchsia', 'meaning': 'HEX:FF00FF', 'annotations': {'rgb': '255,0,255'}},
    "MEDIUM_ORCHID": {'description': 'Medium orchid', 'meaning': 'HEX:BA55D3', 'annotations': {'rgb': '186,85,211'}},
    "MEDIUM_PURPLE": {'description': 'Medium purple', 'meaning': 'HEX:9370DB', 'annotations': {'rgb': '147,112,219'}},
    "BLUE_VIOLET": {'description': 'Blue violet', 'meaning': 'HEX:8A2BE2', 'annotations': {'rgb': '138,43,226'}},
    "DARK_VIOLET": {'description': 'Dark violet', 'meaning': 'HEX:9400D3', 'annotations': {'rgb': '148,0,211'}},
    "DARK_ORCHID": {'description': 'Dark orchid', 'meaning': 'HEX:9932CC', 'annotations': {'rgb': '153,50,204'}},
    "DARK_MAGENTA": {'description': 'Dark magenta', 'meaning': 'HEX:8B008B', 'annotations': {'rgb': '139,0,139'}},
    "INDIGO": {'description': 'Indigo', 'meaning': 'HEX:4B0082', 'annotations': {'rgb': '75,0,130'}},
    "GREEN_YELLOW": {'description': 'Green yellow', 'meaning': 'HEX:ADFF2F', 'annotations': {'rgb': '173,255,47'}},
    "CHARTREUSE": {'description': 'Chartreuse', 'meaning': 'HEX:7FFF00', 'annotations': {'rgb': '127,255,0'}},
    "LAWN_GREEN": {'description': 'Lawn green', 'meaning': 'HEX:7CFC00', 'annotations': {'rgb': '124,252,0'}},
    "LIME": {'description': 'Lime', 'meaning': 'HEX:00FF00', 'annotations': {'rgb': '0,255,0'}},
    "LIME_GREEN": {'description': 'Lime green', 'meaning': 'HEX:32CD32', 'annotations': {'rgb': '50,205,50'}},
    "PALE_GREEN": {'description': 'Pale green', 'meaning': 'HEX:98FB98', 'annotations': {'rgb': '152,251,152'}},
    "LIGHT_GREEN": {'description': 'Light green', 'meaning': 'HEX:90EE90', 'annotations': {'rgb': '144,238,144'}},
    "MEDIUM_SPRING_GREEN": {'description': 'Medium spring green', 'meaning': 'HEX:00FA9A', 'annotations': {'rgb': '0,250,154'}},
    "SPRING_GREEN": {'description': 'Spring green', 'meaning': 'HEX:00FF7F', 'annotations': {'rgb': '0,255,127'}},
    "MEDIUM_SEA_GREEN": {'description': 'Medium sea green', 'meaning': 'HEX:3CB371', 'annotations': {'rgb': '60,179,113'}},
    "SEA_GREEN": {'description': 'Sea green', 'meaning': 'HEX:2E8B57', 'annotations': {'rgb': '46,139,87'}},
    "FOREST_GREEN": {'description': 'Forest green', 'meaning': 'HEX:228B22', 'annotations': {'rgb': '34,139,34'}},
    "DARK_GREEN": {'description': 'Dark green', 'meaning': 'HEX:006400', 'annotations': {'rgb': '0,100,0'}},
    "YELLOW_GREEN": {'description': 'Yellow green', 'meaning': 'HEX:9ACD32', 'annotations': {'rgb': '154,205,50'}},
    "OLIVE_DRAB": {'description': 'Olive drab', 'meaning': 'HEX:6B8E23', 'annotations': {'rgb': '107,142,35'}},
    "OLIVE": {'description': 'Olive', 'meaning': 'HEX:808000', 'annotations': {'rgb': '128,128,0'}},
    "DARK_OLIVE_GREEN": {'description': 'Dark olive green', 'meaning': 'HEX:556B2F', 'annotations': {'rgb': '85,107,47'}},
    "AQUA": {'description': 'Aqua', 'meaning': 'HEX:00FFFF', 'annotations': {'rgb': '0,255,255'}},
    "CYAN": {'description': 'Cyan', 'meaning': 'HEX:00FFFF', 'annotations': {'rgb': '0,255,255'}},
    "LIGHT_CYAN": {'description': 'Light cyan', 'meaning': 'HEX:E0FFFF', 'annotations': {'rgb': '224,255,255'}},
    "PALE_TURQUOISE": {'description': 'Pale turquoise', 'meaning': 'HEX:AFEEEE', 'annotations': {'rgb': '175,238,238'}},
    "AQUAMARINE": {'description': 'Aquamarine', 'meaning': 'HEX:7FFFD4', 'annotations': {'rgb': '127,255,212'}},
    "TURQUOISE": {'description': 'Turquoise', 'meaning': 'HEX:40E0D0', 'annotations': {'rgb': '64,224,208'}},
    "MEDIUM_TURQUOISE": {'description': 'Medium turquoise', 'meaning': 'HEX:48D1CC', 'annotations': {'rgb': '72,209,204'}},
    "DARK_TURQUOISE": {'description': 'Dark turquoise', 'meaning': 'HEX:00CED1', 'annotations': {'rgb': '0,206,209'}},
    "LIGHT_SEA_GREEN": {'description': 'Light sea green', 'meaning': 'HEX:20B2AA', 'annotations': {'rgb': '32,178,170'}},
    "CADET_BLUE": {'description': 'Cadet blue', 'meaning': 'HEX:5F9EA0', 'annotations': {'rgb': '95,158,160'}},
    "DARK_CYAN": {'description': 'Dark cyan', 'meaning': 'HEX:008B8B', 'annotations': {'rgb': '0,139,139'}},
    "TEAL": {'description': 'Teal', 'meaning': 'HEX:008080', 'annotations': {'rgb': '0,128,128'}},
    "LIGHT_STEEL_BLUE": {'description': 'Light steel blue', 'meaning': 'HEX:B0C4DE', 'annotations': {'rgb': '176,196,222'}},
    "POWDER_BLUE": {'description': 'Powder blue', 'meaning': 'HEX:B0E0E6', 'annotations': {'rgb': '176,224,230'}},
    "LIGHT_BLUE": {'description': 'Light blue', 'meaning': 'HEX:ADD8E6', 'annotations': {'rgb': '173,216,230'}},
    "SKY_BLUE": {'description': 'Sky blue', 'meaning': 'HEX:87CEEB', 'annotations': {'rgb': '135,206,235'}},
    "LIGHT_SKY_BLUE": {'description': 'Light sky blue', 'meaning': 'HEX:87CEFA', 'annotations': {'rgb': '135,206,250'}},
    "DEEP_SKY_BLUE": {'description': 'Deep sky blue', 'meaning': 'HEX:00BFFF', 'annotations': {'rgb': '0,191,255'}},
    "DODGER_BLUE": {'description': 'Dodger blue', 'meaning': 'HEX:1E90FF', 'annotations': {'rgb': '30,144,255'}},
    "CORNFLOWER_BLUE": {'description': 'Cornflower blue', 'meaning': 'HEX:6495ED', 'annotations': {'rgb': '100,149,237'}},
    "STEEL_BLUE": {'description': 'Steel blue', 'meaning': 'HEX:4682B4', 'annotations': {'rgb': '70,130,180'}},
    "ROYAL_BLUE": {'description': 'Royal blue', 'meaning': 'HEX:4169E1', 'annotations': {'rgb': '65,105,225'}},
    "MEDIUM_BLUE": {'description': 'Medium blue', 'meaning': 'HEX:0000CD', 'annotations': {'rgb': '0,0,205'}},
    "DARK_BLUE": {'description': 'Dark blue', 'meaning': 'HEX:00008B', 'annotations': {'rgb': '0,0,139'}},
    "NAVY": {'description': 'Navy', 'meaning': 'HEX:000080', 'annotations': {'rgb': '0,0,128'}},
    "MIDNIGHT_BLUE": {'description': 'Midnight blue', 'meaning': 'HEX:191970', 'annotations': {'rgb': '25,25,112'}},
    "CORNSILK": {'description': 'Cornsilk', 'meaning': 'HEX:FFF8DC', 'annotations': {'rgb': '255,248,220'}},
    "BLANCHED_ALMOND": {'description': 'Blanched almond', 'meaning': 'HEX:FFEBCD', 'annotations': {'rgb': '255,235,205'}},
    "BISQUE": {'description': 'Bisque', 'meaning': 'HEX:FFE4C4', 'annotations': {'rgb': '255,228,196'}},
    "NAVAJO_WHITE": {'description': 'Navajo white', 'meaning': 'HEX:FFDEAD', 'annotations': {'rgb': '255,222,173'}},
    "WHEAT": {'description': 'Wheat', 'meaning': 'HEX:F5DEB3', 'annotations': {'rgb': '245,222,179'}},
    "BURLYWOOD": {'description': 'Burlywood', 'meaning': 'HEX:DEB887', 'annotations': {'rgb': '222,184,135'}},
    "TAN": {'description': 'Tan', 'meaning': 'HEX:D2B48C', 'annotations': {'rgb': '210,180,140'}},
    "ROSY_BROWN": {'description': 'Rosy brown', 'meaning': 'HEX:BC8F8F', 'annotations': {'rgb': '188,143,143'}},
    "SANDY_BROWN": {'description': 'Sandy brown', 'meaning': 'HEX:F4A460', 'annotations': {'rgb': '244,164,96'}},
    "GOLDENROD": {'description': 'Goldenrod', 'meaning': 'HEX:DAA520', 'annotations': {'rgb': '218,165,32'}},
    "DARK_GOLDENROD": {'description': 'Dark goldenrod', 'meaning': 'HEX:B8860B', 'annotations': {'rgb': '184,134,11'}},
    "PERU": {'description': 'Peru', 'meaning': 'HEX:CD853F', 'annotations': {'rgb': '205,133,63'}},
    "CHOCOLATE": {'description': 'Chocolate', 'meaning': 'HEX:D2691E', 'annotations': {'rgb': '210,105,30'}},
    "SADDLE_BROWN": {'description': 'Saddle brown', 'meaning': 'HEX:8B4513', 'annotations': {'rgb': '139,69,19'}},
    "SIENNA": {'description': 'Sienna', 'meaning': 'HEX:A0522D', 'annotations': {'rgb': '160,82,45'}},
    "MAROON": {'description': 'Maroon', 'meaning': 'HEX:800000', 'annotations': {'rgb': '128,0,0'}},
    "SNOW": {'description': 'Snow', 'meaning': 'HEX:FFFAFA', 'annotations': {'rgb': '255,250,250'}},
    "HONEYDEW": {'description': 'Honeydew', 'meaning': 'HEX:F0FFF0', 'annotations': {'rgb': '240,255,240'}},
    "MINT_CREAM": {'description': 'Mint cream', 'meaning': 'HEX:F5FFFA', 'annotations': {'rgb': '245,255,250'}},
    "AZURE": {'description': 'Azure', 'meaning': 'HEX:F0FFFF', 'annotations': {'rgb': '240,255,255'}},
    "ALICE_BLUE": {'description': 'Alice blue', 'meaning': 'HEX:F0F8FF', 'annotations': {'rgb': '240,248,255'}},
    "GHOST_WHITE": {'description': 'Ghost white', 'meaning': 'HEX:F8F8FF', 'annotations': {'rgb': '248,248,255'}},
    "WHITE_SMOKE": {'description': 'White smoke', 'meaning': 'HEX:F5F5F5', 'annotations': {'rgb': '245,245,245'}},
    "SEASHELL": {'description': 'Seashell', 'meaning': 'HEX:FFF5EE', 'annotations': {'rgb': '255,245,238'}},
    "BEIGE": {'description': 'Beige', 'meaning': 'HEX:F5F5DC', 'annotations': {'rgb': '245,245,220'}},
    "OLD_LACE": {'description': 'Old lace', 'meaning': 'HEX:FDF5E6', 'annotations': {'rgb': '253,245,230'}},
    "FLORAL_WHITE": {'description': 'Floral white', 'meaning': 'HEX:FFFAF0', 'annotations': {'rgb': '255,250,240'}},
    "IVORY": {'description': 'Ivory', 'meaning': 'HEX:FFFFF0', 'annotations': {'rgb': '255,255,240'}},
    "ANTIQUE_WHITE": {'description': 'Antique white', 'meaning': 'HEX:FAEBD7', 'annotations': {'rgb': '250,235,215'}},
    "LINEN": {'description': 'Linen', 'meaning': 'HEX:FAF0E6', 'annotations': {'rgb': '250,240,230'}},
    "LAVENDER_BLUSH": {'description': 'Lavender blush', 'meaning': 'HEX:FFF0F5', 'annotations': {'rgb': '255,240,245'}},
    "MISTY_ROSE": {'description': 'Misty rose', 'meaning': 'HEX:FFE4E1', 'annotations': {'rgb': '255,228,225'}},
    "GAINSBORO": {'description': 'Gainsboro', 'meaning': 'HEX:DCDCDC', 'annotations': {'rgb': '220,220,220'}},
    "LIGHT_GRAY": {'description': 'Light gray', 'meaning': 'HEX:D3D3D3', 'annotations': {'rgb': '211,211,211'}},
    "SILVER": {'description': 'Silver', 'meaning': 'HEX:C0C0C0', 'annotations': {'rgb': '192,192,192'}},
    "DARK_GRAY": {'description': 'Dark gray', 'meaning': 'HEX:A9A9A9', 'annotations': {'rgb': '169,169,169'}},
    "DIM_GRAY": {'description': 'Dim gray', 'meaning': 'HEX:696969', 'annotations': {'rgb': '105,105,105'}},
    "LIGHT_SLATE_GRAY": {'description': 'Light slate gray', 'meaning': 'HEX:778899', 'annotations': {'rgb': '119,136,153'}},
    "SLATE_GRAY": {'description': 'Slate gray', 'meaning': 'HEX:708090', 'annotations': {'rgb': '112,128,144'}},
    "DARK_SLATE_GRAY": {'description': 'Dark slate gray', 'meaning': 'HEX:2F4F4F', 'annotations': {'rgb': '47,79,79'}},
}

class X11ColorEnum(RichEnum):
    """
    X11/Unix system colors (extended set)
    """
    # Enum members
    X11_AQUA = "X11_AQUA"
    X11_GRAY0 = "X11_GRAY0"
    X11_GRAY25 = "X11_GRAY25"
    X11_GRAY50 = "X11_GRAY50"
    X11_GRAY75 = "X11_GRAY75"
    X11_GRAY100 = "X11_GRAY100"
    X11_GREEN1 = "X11_GREEN1"
    X11_GREEN2 = "X11_GREEN2"
    X11_GREEN3 = "X11_GREEN3"
    X11_GREEN4 = "X11_GREEN4"
    X11_BLUE1 = "X11_BLUE1"
    X11_BLUE2 = "X11_BLUE2"
    X11_BLUE3 = "X11_BLUE3"
    X11_BLUE4 = "X11_BLUE4"
    X11_RED1 = "X11_RED1"
    X11_RED2 = "X11_RED2"
    X11_RED3 = "X11_RED3"
    X11_RED4 = "X11_RED4"

# Set metadata after class creation
X11ColorEnum._metadata = {
    "X11_AQUA": {'description': 'X11 Aqua', 'meaning': 'HEX:00FFFF'},
    "X11_GRAY0": {'description': 'X11 Gray 0 (black)', 'meaning': 'HEX:000000'},
    "X11_GRAY25": {'description': 'X11 Gray 25%', 'meaning': 'HEX:404040'},
    "X11_GRAY50": {'description': 'X11 Gray 50%', 'meaning': 'HEX:808080'},
    "X11_GRAY75": {'description': 'X11 Gray 75%', 'meaning': 'HEX:BFBFBF'},
    "X11_GRAY100": {'description': 'X11 Gray 100 (white)', 'meaning': 'HEX:FFFFFF'},
    "X11_GREEN1": {'description': 'X11 Green 1', 'meaning': 'HEX:00FF00'},
    "X11_GREEN2": {'description': 'X11 Green 2', 'meaning': 'HEX:00EE00'},
    "X11_GREEN3": {'description': 'X11 Green 3', 'meaning': 'HEX:00CD00'},
    "X11_GREEN4": {'description': 'X11 Green 4', 'meaning': 'HEX:008B00'},
    "X11_BLUE1": {'description': 'X11 Blue 1', 'meaning': 'HEX:0000FF'},
    "X11_BLUE2": {'description': 'X11 Blue 2', 'meaning': 'HEX:0000EE'},
    "X11_BLUE3": {'description': 'X11 Blue 3', 'meaning': 'HEX:0000CD'},
    "X11_BLUE4": {'description': 'X11 Blue 4', 'meaning': 'HEX:00008B'},
    "X11_RED1": {'description': 'X11 Red 1', 'meaning': 'HEX:FF0000'},
    "X11_RED2": {'description': 'X11 Red 2', 'meaning': 'HEX:EE0000'},
    "X11_RED3": {'description': 'X11 Red 3', 'meaning': 'HEX:CD0000'},
    "X11_RED4": {'description': 'X11 Red 4', 'meaning': 'HEX:8B0000'},
}

class ColorSpaceEnum(RichEnum):
    """
    Color space and model types
    """
    # Enum members
    RGB = "RGB"
    CMYK = "CMYK"
    HSL = "HSL"
    HSV = "HSV"
    LAB = "LAB"
    PANTONE = "PANTONE"
    RAL = "RAL"
    NCS = "NCS"
    MUNSELL = "MUNSELL"

# Set metadata after class creation
ColorSpaceEnum._metadata = {
    "RGB": {'description': 'Red Green Blue color model'},
    "CMYK": {'description': 'Cyan Magenta Yellow Key (black) color model'},
    "HSL": {'description': 'Hue Saturation Lightness color model'},
    "HSV": {'description': 'Hue Saturation Value color model'},
    "LAB": {'description': 'CIELAB color space'},
    "PANTONE": {'description': 'Pantone Matching System'},
    "RAL": {'description': 'RAL color standard'},
    "NCS": {'description': 'Natural Color System'},
    "MUNSELL": {'description': 'Munsell color system'},
}

class EyeColorEnum(RichEnum):
    """
    Human eye color phenotypes
    """
    # Enum members
    BROWN = "BROWN"
    BLUE = "BLUE"
    GREEN = "GREEN"
    HAZEL = "HAZEL"
    AMBER = "AMBER"
    GRAY = "GRAY"
    HETEROCHROMIA = "HETEROCHROMIA"
    RED_PINK = "RED_PINK"
    VIOLET = "VIOLET"

# Set metadata after class creation
EyeColorEnum._metadata = {
    "BROWN": {'description': 'Brown eyes', 'annotations': {'hex_range': '663300-8B4513', 'prevalence': '79% worldwide'}},
    "BLUE": {'description': 'Blue eyes', 'meaning': 'HP:0000635', 'annotations': {'hex_range': '4169E1-87CEEB', 'prevalence': '8-10% worldwide'}},
    "GREEN": {'description': 'Green eyes', 'annotations': {'hex_range': '2E8B57-90EE90', 'prevalence': '2% worldwide'}},
    "HAZEL": {'description': 'Hazel eyes (brown-green mix)', 'annotations': {'hex_range': '8B7355-C9A878', 'prevalence': '5% worldwide'}},
    "AMBER": {'description': 'Amber/golden eyes', 'annotations': {'hex_range': 'FFBF00-FFB300', 'prevalence': 'rare'}},
    "GRAY": {'description': 'Gray eyes', 'meaning': 'HP:0007730', 'annotations': {'hex_range': '778899-C0C0C0', 'prevalence': '<1% worldwide'}},
    "HETEROCHROMIA": {'description': 'Different colored eyes', 'meaning': 'HP:0001100', 'annotations': {'note': 'complete or sectoral heterochromia'}},
    "RED_PINK": {'description': 'Red/pink eyes (albinism)', 'annotations': {'condition': 'associated with albinism'}},
    "VIOLET": {'description': 'Violet eyes (extremely rare)', 'annotations': {'hex_range': '8B7AB8-9370DB', 'prevalence': 'extremely rare'}},
}

class HairColorEnum(RichEnum):
    """
    Human hair color phenotypes
    """
    # Enum members
    BLACK = "BLACK"
    BROWN = "BROWN"
    DARK_BROWN = "DARK_BROWN"
    LIGHT_BROWN = "LIGHT_BROWN"
    BLONDE = "BLONDE"
    DARK_BLONDE = "DARK_BLONDE"
    LIGHT_BLONDE = "LIGHT_BLONDE"
    PLATINUM_BLONDE = "PLATINUM_BLONDE"
    STRAWBERRY_BLONDE = "STRAWBERRY_BLONDE"
    RED = "RED"
    AUBURN = "AUBURN"
    GINGER = "GINGER"
    GRAY = "GRAY"
    WHITE = "WHITE"
    SILVER = "SILVER"

# Set metadata after class creation
HairColorEnum._metadata = {
    "BLACK": {'description': 'Black hair', 'annotations': {'hex': '000000', 'prevalence': 'most common worldwide'}},
    "BROWN": {'description': 'Brown hair', 'annotations': {'hex_range': '654321-8B4513'}},
    "DARK_BROWN": {'description': 'Dark brown hair', 'annotations': {'hex': '3B2F2F'}},
    "LIGHT_BROWN": {'description': 'Light brown hair', 'annotations': {'hex': '977961'}},
    "BLONDE": {'description': 'Blonde/blond hair', 'meaning': 'HP:0002286', 'annotations': {'hex_range': 'FAF0BE-FFF8DC'}},
    "DARK_BLONDE": {'description': 'Dark blonde hair', 'annotations': {'hex': '9F8F71'}},
    "LIGHT_BLONDE": {'description': 'Light blonde hair', 'annotations': {'hex': 'FFF8DC'}},
    "PLATINUM_BLONDE": {'description': 'Platinum blonde hair', 'annotations': {'hex': 'E5E5E5'}},
    "STRAWBERRY_BLONDE": {'description': 'Strawberry blonde hair', 'annotations': {'hex': 'FF9966'}},
    "RED": {'description': 'Red hair', 'meaning': 'HP:0002297', 'annotations': {'hex_range': '922724-FF4500', 'prevalence': '1-2% worldwide'}},
    "AUBURN": {'description': 'Auburn hair (reddish-brown)', 'annotations': {'hex': 'A52A2A'}},
    "GINGER": {'description': 'Ginger hair (orange-red)', 'annotations': {'hex': 'FF6600'}},
    "GRAY": {'description': 'Gray hair', 'meaning': 'HP:0002216', 'annotations': {'hex_range': '808080-C0C0C0'}},
    "WHITE": {'description': 'White hair', 'meaning': 'HP:0011364', 'annotations': {'hex': 'FFFFFF'}},
    "SILVER": {'description': 'Silver hair', 'annotations': {'hex': 'C0C0C0'}},
}

class FlowerColorEnum(RichEnum):
    """
    Common flower colors
    """
    # Enum members
    RED = "RED"
    PINK = "PINK"
    ORANGE = "ORANGE"
    YELLOW = "YELLOW"
    WHITE = "WHITE"
    PURPLE = "PURPLE"
    VIOLET = "VIOLET"
    BLUE = "BLUE"
    LAVENDER = "LAVENDER"
    MAGENTA = "MAGENTA"
    BURGUNDY = "BURGUNDY"
    CORAL = "CORAL"
    PEACH = "PEACH"
    CREAM = "CREAM"
    BICOLOR = "BICOLOR"
    MULTICOLOR = "MULTICOLOR"

# Set metadata after class creation
FlowerColorEnum._metadata = {
    "RED": {'description': 'Red flowers', 'annotations': {'hex': 'FF0000', 'examples': 'roses, tulips, poppies'}},
    "PINK": {'description': 'Pink flowers', 'annotations': {'hex': 'FFC0CB', 'examples': 'peonies, cherry blossoms'}},
    "ORANGE": {'description': 'Orange flowers', 'annotations': {'hex': 'FFA500', 'examples': 'marigolds, zinnias'}},
    "YELLOW": {'description': 'Yellow flowers', 'annotations': {'hex': 'FFFF00', 'examples': 'sunflowers, daffodils'}},
    "WHITE": {'description': 'White flowers', 'annotations': {'hex': 'FFFFFF', 'examples': 'lilies, daisies'}},
    "PURPLE": {'description': 'Purple flowers', 'annotations': {'hex': '800080', 'examples': 'lavender, violets'}},
    "VIOLET": {'description': 'Violet flowers', 'annotations': {'hex': '7F00FF', 'examples': 'violets, pansies'}},
    "BLUE": {'description': 'Blue flowers', 'annotations': {'hex': '0000FF', 'examples': 'forget-me-nots, cornflowers'}},
    "LAVENDER": {'description': 'Lavender flowers', 'annotations': {'hex': 'E6E6FA', 'examples': 'lavender, wisteria'}},
    "MAGENTA": {'description': 'Magenta flowers', 'annotations': {'hex': 'FF00FF', 'examples': 'fuchsias, bougainvillea'}},
    "BURGUNDY": {'description': 'Burgundy/deep red flowers', 'annotations': {'hex': '800020', 'examples': 'dahlias, chrysanthemums'}},
    "CORAL": {'description': 'Coral flowers', 'annotations': {'hex': 'FF7F50', 'examples': 'coral bells, begonias'}},
    "PEACH": {'description': 'Peach flowers', 'annotations': {'hex': 'FFDAB9', 'examples': 'roses, dahlias'}},
    "CREAM": {'description': 'Cream flowers', 'annotations': {'hex': 'FFFDD0', 'examples': 'roses, tulips'}},
    "BICOLOR": {'description': 'Two-colored flowers', 'annotations': {'note': 'flowers with two distinct colors'}},
    "MULTICOLOR": {'description': 'Multi-colored flowers', 'annotations': {'note': 'flowers with more than two colors'}},
}

class AnimalCoatColorEnum(RichEnum):
    """
    Animal coat/fur colors
    """
    # Enum members
    BLACK = "BLACK"
    WHITE = "WHITE"
    BROWN = "BROWN"
    TAN = "TAN"
    CREAM = "CREAM"
    GRAY = "GRAY"
    RED = "RED"
    GOLDEN = "GOLDEN"
    FAWN = "FAWN"
    BRINDLE = "BRINDLE"
    SPOTTED = "SPOTTED"
    MERLE = "MERLE"
    PIEBALD = "PIEBALD"
    CALICO = "CALICO"
    TABBY = "TABBY"
    TORTOISESHELL = "TORTOISESHELL"
    ROAN = "ROAN"
    PALOMINO = "PALOMINO"
    CHESTNUT = "CHESTNUT"
    BAY = "BAY"

# Set metadata after class creation
AnimalCoatColorEnum._metadata = {
    "BLACK": {'description': 'Black coat', 'annotations': {'hex': '000000'}},
    "WHITE": {'description': 'White coat', 'annotations': {'hex': 'FFFFFF'}},
    "BROWN": {'description': 'Brown coat', 'annotations': {'hex': '964B00'}},
    "TAN": {'description': 'Tan coat', 'annotations': {'hex': 'D2B48C'}},
    "CREAM": {'description': 'Cream coat', 'annotations': {'hex': 'FFFDD0'}},
    "GRAY": {'description': 'Gray coat', 'annotations': {'hex': '808080'}},
    "RED": {'description': 'Red/rust coat', 'annotations': {'hex': 'B22222'}},
    "GOLDEN": {'description': 'Golden coat', 'annotations': {'hex': 'FFD700'}},
    "FAWN": {'description': 'Fawn coat', 'annotations': {'hex': 'E5AA70'}},
    "BRINDLE": {'description': 'Brindle pattern (striped)', 'annotations': {'pattern': 'striped mixture of colors'}},
    "SPOTTED": {'description': 'Spotted pattern', 'annotations': {'pattern': 'spots on base color'}},
    "MERLE": {'description': 'Merle pattern (mottled)', 'annotations': {'pattern': 'mottled patches'}},
    "PIEBALD": {'description': 'Piebald pattern (patches)', 'annotations': {'pattern': 'irregular patches'}},
    "CALICO": {'description': 'Calico pattern (tri-color)', 'annotations': {'pattern': 'tri-color patches', 'species': 'primarily cats'}},
    "TABBY": {'description': 'Tabby pattern (striped)', 'annotations': {'pattern': 'striped or spotted', 'species': 'primarily cats'}},
    "TORTOISESHELL": {'description': 'Tortoiseshell pattern', 'annotations': {'pattern': 'mottled orange and black', 'species': 'primarily cats'}},
    "ROAN": {'description': 'Roan pattern (mixed white)', 'annotations': {'pattern': 'white mixed with base color', 'species': 'primarily horses'}},
    "PALOMINO": {'description': 'Palomino (golden with white mane)', 'annotations': {'hex': 'DEC05F', 'species': 'horses'}},
    "CHESTNUT": {'description': 'Chestnut/sorrel', 'annotations': {'hex': 'CD5C5C', 'species': 'horses'}},
    "BAY": {'description': 'Bay (brown with black points)', 'annotations': {'species': 'horses'}},
}

class SkinToneEnum(RichEnum):
    """
    Human skin tone classifications (Fitzpatrick scale based)
    """
    # Enum members
    TYPE_I = "TYPE_I"
    TYPE_II = "TYPE_II"
    TYPE_III = "TYPE_III"
    TYPE_IV = "TYPE_IV"
    TYPE_V = "TYPE_V"
    TYPE_VI = "TYPE_VI"

# Set metadata after class creation
SkinToneEnum._metadata = {
    "TYPE_I": {'description': 'Very pale white skin', 'annotations': {'fitzpatrick': 'Type I', 'hex_range': 'FFE0BD-FFDFC4', 'sun_reaction': 'always burns, never tans'}},
    "TYPE_II": {'description': 'Fair white skin', 'annotations': {'fitzpatrick': 'Type II', 'hex_range': 'F0D5BE-E8C5A0', 'sun_reaction': 'burns easily, tans minimally'}},
    "TYPE_III": {'description': 'Light brown skin', 'annotations': {'fitzpatrick': 'Type III', 'hex_range': 'DDA582-CD9766', 'sun_reaction': 'burns moderately, tans gradually'}},
    "TYPE_IV": {'description': 'Moderate brown skin', 'annotations': {'fitzpatrick': 'Type IV', 'hex_range': 'B87659-A47148', 'sun_reaction': 'burns minimally, tans easily'}},
    "TYPE_V": {'description': 'Dark brown skin', 'annotations': {'fitzpatrick': 'Type V', 'hex_range': '935D37-7C4E2A', 'sun_reaction': 'rarely burns, tans darkly'}},
    "TYPE_VI": {'description': 'Very dark brown to black skin', 'annotations': {'fitzpatrick': 'Type VI', 'hex_range': '5C3A1E-3D2314', 'sun_reaction': 'never burns, always tans darkly'}},
}

class PlantLeafColorEnum(RichEnum):
    """
    Plant leaf colors (including seasonal changes)
    """
    # Enum members
    GREEN = "GREEN"
    DARK_GREEN = "DARK_GREEN"
    LIGHT_GREEN = "LIGHT_GREEN"
    YELLOW_GREEN = "YELLOW_GREEN"
    YELLOW = "YELLOW"
    ORANGE = "ORANGE"
    RED = "RED"
    PURPLE = "PURPLE"
    BRONZE = "BRONZE"
    SILVER = "SILVER"
    VARIEGATED = "VARIEGATED"
    BROWN = "BROWN"

# Set metadata after class creation
PlantLeafColorEnum._metadata = {
    "GREEN": {'description': 'Green leaves (healthy/summer)', 'meaning': 'PATO:0000320', 'annotations': {'hex_range': '228B22-90EE90', 'season': 'spring/summer'}},
    "DARK_GREEN": {'description': 'Dark green leaves', 'annotations': {'hex': '006400'}},
    "LIGHT_GREEN": {'description': 'Light green leaves', 'annotations': {'hex': '90EE90'}},
    "YELLOW_GREEN": {'description': 'Yellow-green leaves', 'annotations': {'hex': '9ACD32', 'condition': 'new growth or nutrient deficiency'}},
    "YELLOW": {'description': 'Yellow leaves (autumn or chlorosis)', 'meaning': 'PATO:0000324', 'annotations': {'hex': 'FFD700', 'season': 'autumn'}},
    "ORANGE": {'description': 'Orange leaves (autumn)', 'annotations': {'hex': 'FF8C00', 'season': 'autumn'}},
    "RED": {'description': 'Red leaves (autumn or certain species)', 'meaning': 'PATO:0000322', 'annotations': {'hex': 'DC143C', 'season': 'autumn'}},
    "PURPLE": {'description': 'Purple leaves (certain species)', 'annotations': {'hex': '800080', 'examples': 'purple basil, Japanese maple'}},
    "BRONZE": {'description': 'Bronze leaves', 'annotations': {'hex': 'CD7F32'}},
    "SILVER": {'description': 'Silver/gray leaves', 'annotations': {'hex': 'C0C0C0', 'examples': 'dusty miller, artemisia'}},
    "VARIEGATED": {'description': 'Variegated leaves (multiple colors)', 'annotations': {'pattern': 'mixed colors/patterns'}},
    "BROWN": {'description': 'Brown leaves (dead/dying)', 'annotations': {'hex': '964B00', 'condition': 'senescent or dead'}},
}

class DNABaseEnum(RichEnum):
    """
    Standard DNA nucleotide bases (canonical)
    """
    # Enum members
    A = "A"
    C = "C"
    G = "G"
    T = "T"

# Set metadata after class creation
DNABaseEnum._metadata = {
    "A": {'meaning': 'CHEBI:16708', 'annotations': {'complement': 'T', 'purine': 'true', 'chemical_formula': 'C5H5N5'}, 'aliases': ['adenine']},
    "C": {'meaning': 'CHEBI:16040', 'annotations': {'complement': 'G', 'pyrimidine': 'true', 'chemical_formula': 'C4H5N3O'}, 'aliases': ['cytosine']},
    "G": {'meaning': 'CHEBI:16235', 'annotations': {'complement': 'C', 'purine': 'true', 'chemical_formula': 'C5H5N5O'}, 'aliases': ['guanine']},
    "T": {'meaning': 'CHEBI:17821', 'annotations': {'complement': 'A', 'pyrimidine': 'true', 'chemical_formula': 'C5H6N2O2'}, 'aliases': ['thymine']},
}

class DNABaseExtendedEnum(RichEnum):
    """
    Extended DNA alphabet with IUPAC ambiguity codes
    """
    # Enum members
    A = "A"
    C = "C"
    G = "G"
    T = "T"
    R = "R"
    Y = "Y"
    S = "S"
    W = "W"
    K = "K"
    M = "M"
    B = "B"
    D = "D"
    H = "H"
    V = "V"
    N = "N"
    GAP = "GAP"

# Set metadata after class creation
DNABaseExtendedEnum._metadata = {
    "A": {'meaning': 'CHEBI:16708', 'annotations': {'represents': 'A'}, 'aliases': ['adenine']},
    "C": {'meaning': 'CHEBI:16040', 'annotations': {'represents': 'C'}, 'aliases': ['cytosine']},
    "G": {'meaning': 'CHEBI:16235', 'annotations': {'represents': 'G'}, 'aliases': ['guanine']},
    "T": {'meaning': 'CHEBI:17821', 'annotations': {'represents': 'T'}, 'aliases': ['thymine']},
    "R": {'annotations': {'represents': 'A,G', 'iupac': 'true'}},
    "Y": {'annotations': {'represents': 'C,T', 'iupac': 'true'}},
    "S": {'annotations': {'represents': 'G,C', 'iupac': 'true', 'bond_strength': 'strong (3 H-bonds)'}},
    "W": {'annotations': {'represents': 'A,T', 'iupac': 'true', 'bond_strength': 'weak (2 H-bonds)'}},
    "K": {'annotations': {'represents': 'G,T', 'iupac': 'true'}},
    "M": {'annotations': {'represents': 'A,C', 'iupac': 'true'}},
    "B": {'annotations': {'represents': 'C,G,T', 'iupac': 'true'}},
    "D": {'annotations': {'represents': 'A,G,T', 'iupac': 'true'}},
    "H": {'annotations': {'represents': 'A,C,T', 'iupac': 'true'}},
    "V": {'annotations': {'represents': 'A,C,G', 'iupac': 'true'}},
    "N": {'annotations': {'represents': 'A,C,G,T', 'iupac': 'true'}},
    "GAP": {'annotations': {'symbol': '-', 'represents': 'gap'}},
}

class RNABaseEnum(RichEnum):
    """
    Standard RNA nucleotide bases (canonical)
    """
    # Enum members
    A = "A"
    C = "C"
    G = "G"
    U = "U"

# Set metadata after class creation
RNABaseEnum._metadata = {
    "A": {'meaning': 'CHEBI:16708', 'annotations': {'complement': 'U', 'purine': 'true', 'chemical_formula': 'C5H5N5'}, 'aliases': ['adenine']},
    "C": {'meaning': 'CHEBI:16040', 'annotations': {'complement': 'G', 'pyrimidine': 'true', 'chemical_formula': 'C4H5N3O'}, 'aliases': ['cytosine']},
    "G": {'meaning': 'CHEBI:16235', 'annotations': {'complement': 'C', 'purine': 'true', 'chemical_formula': 'C5H5N5O'}, 'aliases': ['guanine']},
    "U": {'meaning': 'CHEBI:17568', 'annotations': {'complement': 'A', 'pyrimidine': 'true', 'chemical_formula': 'C4H4N2O2'}, 'aliases': ['uracil']},
}

class RNABaseExtendedEnum(RichEnum):
    """
    Extended RNA alphabet with IUPAC ambiguity codes
    """
    # Enum members
    A = "A"
    C = "C"
    G = "G"
    U = "U"
    R = "R"
    Y = "Y"
    S = "S"
    W = "W"
    K = "K"
    M = "M"
    B = "B"
    D = "D"
    H = "H"
    V = "V"
    N = "N"
    GAP = "GAP"

# Set metadata after class creation
RNABaseExtendedEnum._metadata = {
    "A": {'meaning': 'CHEBI:16708', 'annotations': {'represents': 'A'}, 'aliases': ['adenine']},
    "C": {'meaning': 'CHEBI:16040', 'annotations': {'represents': 'C'}, 'aliases': ['cytosine']},
    "G": {'meaning': 'CHEBI:16235', 'annotations': {'represents': 'G'}, 'aliases': ['guanine']},
    "U": {'meaning': 'CHEBI:17568', 'annotations': {'represents': 'U'}, 'aliases': ['uracil']},
    "R": {'annotations': {'represents': 'A,G', 'iupac': 'true'}},
    "Y": {'annotations': {'represents': 'C,U', 'iupac': 'true'}},
    "S": {'annotations': {'represents': 'G,C', 'iupac': 'true'}},
    "W": {'annotations': {'represents': 'A,U', 'iupac': 'true'}},
    "K": {'annotations': {'represents': 'G,U', 'iupac': 'true'}},
    "M": {'annotations': {'represents': 'A,C', 'iupac': 'true'}},
    "B": {'annotations': {'represents': 'C,G,U', 'iupac': 'true'}},
    "D": {'annotations': {'represents': 'A,G,U', 'iupac': 'true'}},
    "H": {'annotations': {'represents': 'A,C,U', 'iupac': 'true'}},
    "V": {'annotations': {'represents': 'A,C,G', 'iupac': 'true'}},
    "N": {'annotations': {'represents': 'A,C,G,U', 'iupac': 'true'}},
    "GAP": {'annotations': {'symbol': '-', 'represents': 'gap'}},
}

class AminoAcidEnum(RichEnum):
    """
    Standard amino acid single letter codes
    """
    # Enum members
    A = "A"
    C = "C"
    D = "D"
    E = "E"
    F = "F"
    G = "G"
    H = "H"
    I = "I"
    K = "K"
    L = "L"
    M = "M"
    N = "N"
    P = "P"
    Q = "Q"
    R = "R"
    S = "S"
    T = "T"
    V = "V"
    W = "W"
    Y = "Y"

# Set metadata after class creation
AminoAcidEnum._metadata = {
    "A": {'meaning': 'CHEBI:16449', 'annotations': {'three_letter': 'Ala', 'polarity': 'nonpolar', 'essential': 'false', 'molecular_weight': '89.09'}, 'aliases': ['alanine']},
    "C": {'meaning': 'CHEBI:17561', 'annotations': {'three_letter': 'Cys', 'polarity': 'polar', 'essential': 'false', 'molecular_weight': '121.15', 'special': 'forms disulfide bonds'}, 'aliases': ['L-cysteine']},
    "D": {'meaning': 'CHEBI:17053', 'annotations': {'three_letter': 'Asp', 'polarity': 'acidic', 'essential': 'false', 'molecular_weight': '133.10', 'charge': 'negative'}, 'aliases': ['L-aspartic acid']},
    "E": {'meaning': 'CHEBI:16015', 'annotations': {'three_letter': 'Glu', 'polarity': 'acidic', 'essential': 'false', 'molecular_weight': '147.13', 'charge': 'negative'}, 'aliases': ['L-glutamic acid']},
    "F": {'meaning': 'CHEBI:17295', 'annotations': {'three_letter': 'Phe', 'polarity': 'nonpolar', 'essential': 'true', 'molecular_weight': '165.19', 'aromatic': 'true'}, 'aliases': ['L-phenylalanine']},
    "G": {'meaning': 'CHEBI:15428', 'annotations': {'three_letter': 'Gly', 'polarity': 'nonpolar', 'essential': 'false', 'molecular_weight': '75.07', 'special': 'smallest, most flexible'}, 'aliases': ['glycine']},
    "H": {'meaning': 'CHEBI:15971', 'annotations': {'three_letter': 'His', 'polarity': 'basic', 'essential': 'true', 'molecular_weight': '155.16', 'charge': 'positive'}, 'aliases': ['L-histidine']},
    "I": {'meaning': 'CHEBI:17191', 'annotations': {'three_letter': 'Ile', 'polarity': 'nonpolar', 'essential': 'true', 'molecular_weight': '131.17', 'branched': 'true'}, 'aliases': ['L-isoleucine']},
    "K": {'meaning': 'CHEBI:18019', 'annotations': {'three_letter': 'Lys', 'polarity': 'basic', 'essential': 'true', 'molecular_weight': '146.19', 'charge': 'positive'}, 'aliases': ['L-lysine']},
    "L": {'meaning': 'CHEBI:15603', 'annotations': {'three_letter': 'Leu', 'polarity': 'nonpolar', 'essential': 'true', 'molecular_weight': '131.17', 'branched': 'true'}, 'aliases': ['L-leucine']},
    "M": {'meaning': 'CHEBI:16643', 'annotations': {'three_letter': 'Met', 'polarity': 'nonpolar', 'essential': 'true', 'molecular_weight': '149.21', 'special': 'start codon'}, 'aliases': ['L-methionine']},
    "N": {'meaning': 'CHEBI:17196', 'annotations': {'three_letter': 'Asn', 'polarity': 'polar', 'essential': 'false', 'molecular_weight': '132.12'}, 'aliases': ['L-asparagine']},
    "P": {'meaning': 'CHEBI:17203', 'annotations': {'three_letter': 'Pro', 'polarity': 'nonpolar', 'essential': 'false', 'molecular_weight': '115.13', 'special': 'helix breaker, rigid'}, 'aliases': ['L-proline']},
    "Q": {'meaning': 'CHEBI:18050', 'annotations': {'three_letter': 'Gln', 'polarity': 'polar', 'essential': 'false', 'molecular_weight': '146.15'}, 'aliases': ['L-glutamine']},
    "R": {'meaning': 'CHEBI:16467', 'annotations': {'three_letter': 'Arg', 'polarity': 'basic', 'essential': 'false', 'molecular_weight': '174.20', 'charge': 'positive'}, 'aliases': ['L-arginine']},
    "S": {'meaning': 'CHEBI:17115', 'annotations': {'three_letter': 'Ser', 'polarity': 'polar', 'essential': 'false', 'molecular_weight': '105.09', 'hydroxyl': 'true'}, 'aliases': ['L-serine']},
    "T": {'meaning': 'CHEBI:16857', 'annotations': {'three_letter': 'Thr', 'polarity': 'polar', 'essential': 'true', 'molecular_weight': '119.12', 'hydroxyl': 'true'}, 'aliases': ['L-threonine']},
    "V": {'meaning': 'CHEBI:16414', 'annotations': {'three_letter': 'Val', 'polarity': 'nonpolar', 'essential': 'true', 'molecular_weight': '117.15', 'branched': 'true'}, 'aliases': ['L-valine']},
    "W": {'meaning': 'CHEBI:16828', 'annotations': {'three_letter': 'Trp', 'polarity': 'nonpolar', 'essential': 'true', 'molecular_weight': '204.23', 'aromatic': 'true', 'special': 'largest'}, 'aliases': ['L-tryptophan']},
    "Y": {'meaning': 'CHEBI:17895', 'annotations': {'three_letter': 'Tyr', 'polarity': 'polar', 'essential': 'false', 'molecular_weight': '181.19', 'aromatic': 'true', 'hydroxyl': 'true'}, 'aliases': ['L-tyrosine']},
}

class AminoAcidExtendedEnum(RichEnum):
    """
    Extended amino acid alphabet with ambiguity codes and special characters
    """
    # Enum members
    A = "A"
    C = "C"
    D = "D"
    E = "E"
    F = "F"
    G = "G"
    H = "H"
    I = "I"
    K = "K"
    L = "L"
    M = "M"
    N = "N"
    P = "P"
    Q = "Q"
    R = "R"
    S = "S"
    T = "T"
    V = "V"
    W = "W"
    Y = "Y"
    B = "B"
    Z = "Z"
    J = "J"
    X = "X"
    STOP = "STOP"
    GAP = "GAP"
    U = "U"
    O = "O"

# Set metadata after class creation
AminoAcidExtendedEnum._metadata = {
    "A": {'meaning': 'CHEBI:16449', 'annotations': {'three_letter': 'Ala'}, 'aliases': ['alanine']},
    "C": {'meaning': 'CHEBI:17561', 'annotations': {'three_letter': 'Cys'}, 'aliases': ['L-cysteine']},
    "D": {'meaning': 'CHEBI:17053', 'annotations': {'three_letter': 'Asp'}, 'aliases': ['L-aspartic acid']},
    "E": {'meaning': 'CHEBI:16015', 'annotations': {'three_letter': 'Glu'}, 'aliases': ['L-glutamic acid']},
    "F": {'meaning': 'CHEBI:17295', 'annotations': {'three_letter': 'Phe'}, 'aliases': ['L-phenylalanine']},
    "G": {'meaning': 'CHEBI:15428', 'annotations': {'three_letter': 'Gly'}, 'aliases': ['glycine']},
    "H": {'meaning': 'CHEBI:15971', 'annotations': {'three_letter': 'His'}, 'aliases': ['L-histidine']},
    "I": {'meaning': 'CHEBI:17191', 'annotations': {'three_letter': 'Ile'}, 'aliases': ['L-isoleucine']},
    "K": {'meaning': 'CHEBI:18019', 'annotations': {'three_letter': 'Lys'}, 'aliases': ['L-lysine']},
    "L": {'meaning': 'CHEBI:15603', 'annotations': {'three_letter': 'Leu'}, 'aliases': ['L-leucine']},
    "M": {'meaning': 'CHEBI:16643', 'annotations': {'three_letter': 'Met'}, 'aliases': ['L-methionine']},
    "N": {'meaning': 'CHEBI:17196', 'annotations': {'three_letter': 'Asn'}, 'aliases': ['L-asparagine']},
    "P": {'meaning': 'CHEBI:17203', 'annotations': {'three_letter': 'Pro'}, 'aliases': ['L-proline']},
    "Q": {'meaning': 'CHEBI:18050', 'annotations': {'three_letter': 'Gln'}, 'aliases': ['L-glutamine']},
    "R": {'meaning': 'CHEBI:16467', 'annotations': {'three_letter': 'Arg'}, 'aliases': ['L-arginine']},
    "S": {'meaning': 'CHEBI:17115', 'annotations': {'three_letter': 'Ser'}, 'aliases': ['L-serine']},
    "T": {'meaning': 'CHEBI:16857', 'annotations': {'three_letter': 'Thr'}, 'aliases': ['L-threonine']},
    "V": {'meaning': 'CHEBI:16414', 'annotations': {'three_letter': 'Val'}, 'aliases': ['L-valine']},
    "W": {'meaning': 'CHEBI:16828', 'annotations': {'three_letter': 'Trp'}, 'aliases': ['L-tryptophan']},
    "Y": {'meaning': 'CHEBI:17895', 'annotations': {'three_letter': 'Tyr'}, 'aliases': ['L-tyrosine']},
    "B": {'annotations': {'three_letter': 'Asx', 'represents': 'D,N', 'ambiguity': 'true'}, 'aliases': ['L-aspartic acid or Asparagine (D or N)']},
    "Z": {'annotations': {'three_letter': 'Glx', 'represents': 'E,Q', 'ambiguity': 'true'}, 'aliases': ['L-glutamic acid or Glutamine (E or Q)']},
    "J": {'annotations': {'three_letter': 'Xle', 'represents': 'L,I', 'ambiguity': 'true'}, 'aliases': ['L-leucine or Isoleucine (L or I)']},
    "X": {'annotations': {'three_letter': 'Xaa', 'represents': 'any', 'ambiguity': 'true'}},
    "STOP": {'annotations': {'symbol': '*', 'three_letter': 'Ter', 'represents': 'stop codon'}},
    "GAP": {'annotations': {'symbol': '-', 'represents': 'gap'}},
    "U": {'meaning': 'CHEBI:16633', 'annotations': {'three_letter': 'Sec', 'special': '21st amino acid', 'codon': 'UGA with SECIS element'}, 'aliases': ['L-selenocysteine']},
    "O": {'meaning': 'CHEBI:21786', 'annotations': {'three_letter': 'Pyl', 'special': '22nd amino acid', 'codon': 'UAG in certain archaea/bacteria'}},
}

class CodonEnum(RichEnum):
    """
    Standard genetic code codons (DNA)
    """
    # Enum members
    TTT = "TTT"
    TTC = "TTC"
    TTA = "TTA"
    TTG = "TTG"
    CTT = "CTT"
    CTC = "CTC"
    CTA = "CTA"
    CTG = "CTG"
    ATT = "ATT"
    ATC = "ATC"
    ATA = "ATA"
    ATG = "ATG"
    GTT = "GTT"
    GTC = "GTC"
    GTA = "GTA"
    GTG = "GTG"
    TCT = "TCT"
    TCC = "TCC"
    TCA = "TCA"
    TCG = "TCG"
    AGT = "AGT"
    AGC = "AGC"
    CCT = "CCT"
    CCC = "CCC"
    CCA = "CCA"
    CCG = "CCG"
    ACT = "ACT"
    ACC = "ACC"
    ACA = "ACA"
    ACG = "ACG"
    GCT = "GCT"
    GCC = "GCC"
    GCA = "GCA"
    GCG = "GCG"
    TAT = "TAT"
    TAC = "TAC"
    TAA = "TAA"
    TAG = "TAG"
    TGA = "TGA"
    CAT = "CAT"
    CAC = "CAC"
    CAA = "CAA"
    CAG = "CAG"
    AAT = "AAT"
    AAC = "AAC"
    AAA = "AAA"
    AAG = "AAG"
    GAT = "GAT"
    GAC = "GAC"
    GAA = "GAA"
    GAG = "GAG"
    TGT = "TGT"
    TGC = "TGC"
    TGG = "TGG"
    CGT = "CGT"
    CGC = "CGC"
    CGA = "CGA"
    CGG = "CGG"
    AGA = "AGA"
    AGG = "AGG"
    GGT = "GGT"
    GGC = "GGC"
    GGA = "GGA"
    GGG = "GGG"

# Set metadata after class creation
CodonEnum._metadata = {
    "TTT": {'annotations': {'amino_acid': 'F', 'amino_acid_name': 'Phenylalanine'}},
    "TTC": {'annotations': {'amino_acid': 'F', 'amino_acid_name': 'Phenylalanine'}},
    "TTA": {'annotations': {'amino_acid': 'L', 'amino_acid_name': 'Leucine'}},
    "TTG": {'annotations': {'amino_acid': 'L', 'amino_acid_name': 'Leucine'}},
    "CTT": {'annotations': {'amino_acid': 'L', 'amino_acid_name': 'Leucine'}},
    "CTC": {'annotations': {'amino_acid': 'L', 'amino_acid_name': 'Leucine'}},
    "CTA": {'annotations': {'amino_acid': 'L', 'amino_acid_name': 'Leucine'}},
    "CTG": {'annotations': {'amino_acid': 'L', 'amino_acid_name': 'Leucine'}},
    "ATT": {'annotations': {'amino_acid': 'I', 'amino_acid_name': 'Isoleucine'}},
    "ATC": {'annotations': {'amino_acid': 'I', 'amino_acid_name': 'Isoleucine'}},
    "ATA": {'annotations': {'amino_acid': 'I', 'amino_acid_name': 'Isoleucine'}},
    "ATG": {'annotations': {'amino_acid': 'M', 'amino_acid_name': 'Methionine', 'special': 'start codon'}},
    "GTT": {'annotations': {'amino_acid': 'V', 'amino_acid_name': 'Valine'}},
    "GTC": {'annotations': {'amino_acid': 'V', 'amino_acid_name': 'Valine'}},
    "GTA": {'annotations': {'amino_acid': 'V', 'amino_acid_name': 'Valine'}},
    "GTG": {'annotations': {'amino_acid': 'V', 'amino_acid_name': 'Valine'}},
    "TCT": {'annotations': {'amino_acid': 'S', 'amino_acid_name': 'Serine'}},
    "TCC": {'annotations': {'amino_acid': 'S', 'amino_acid_name': 'Serine'}},
    "TCA": {'annotations': {'amino_acid': 'S', 'amino_acid_name': 'Serine'}},
    "TCG": {'annotations': {'amino_acid': 'S', 'amino_acid_name': 'Serine'}},
    "AGT": {'annotations': {'amino_acid': 'S', 'amino_acid_name': 'Serine'}},
    "AGC": {'annotations': {'amino_acid': 'S', 'amino_acid_name': 'Serine'}},
    "CCT": {'annotations': {'amino_acid': 'P', 'amino_acid_name': 'Proline'}},
    "CCC": {'annotations': {'amino_acid': 'P', 'amino_acid_name': 'Proline'}},
    "CCA": {'annotations': {'amino_acid': 'P', 'amino_acid_name': 'Proline'}},
    "CCG": {'annotations': {'amino_acid': 'P', 'amino_acid_name': 'Proline'}},
    "ACT": {'annotations': {'amino_acid': 'T', 'amino_acid_name': 'Threonine'}},
    "ACC": {'annotations': {'amino_acid': 'T', 'amino_acid_name': 'Threonine'}},
    "ACA": {'annotations': {'amino_acid': 'T', 'amino_acid_name': 'Threonine'}},
    "ACG": {'annotations': {'amino_acid': 'T', 'amino_acid_name': 'Threonine'}},
    "GCT": {'annotations': {'amino_acid': 'A', 'amino_acid_name': 'Alanine'}},
    "GCC": {'annotations': {'amino_acid': 'A', 'amino_acid_name': 'Alanine'}},
    "GCA": {'annotations': {'amino_acid': 'A', 'amino_acid_name': 'Alanine'}},
    "GCG": {'annotations': {'amino_acid': 'A', 'amino_acid_name': 'Alanine'}},
    "TAT": {'annotations': {'amino_acid': 'Y', 'amino_acid_name': 'Tyrosine'}},
    "TAC": {'annotations': {'amino_acid': 'Y', 'amino_acid_name': 'Tyrosine'}},
    "TAA": {'annotations': {'amino_acid': '*', 'name': 'ochre', 'special': 'stop codon'}},
    "TAG": {'annotations': {'amino_acid': '*', 'name': 'amber', 'special': 'stop codon'}},
    "TGA": {'annotations': {'amino_acid': '*', 'name': 'opal', 'special': 'stop codon or selenocysteine'}},
    "CAT": {'annotations': {'amino_acid': 'H', 'amino_acid_name': 'Histidine'}},
    "CAC": {'annotations': {'amino_acid': 'H', 'amino_acid_name': 'Histidine'}},
    "CAA": {'annotations': {'amino_acid': 'Q', 'amino_acid_name': 'Glutamine'}},
    "CAG": {'annotations': {'amino_acid': 'Q', 'amino_acid_name': 'Glutamine'}},
    "AAT": {'annotations': {'amino_acid': 'N', 'amino_acid_name': 'Asparagine'}},
    "AAC": {'annotations': {'amino_acid': 'N', 'amino_acid_name': 'Asparagine'}},
    "AAA": {'annotations': {'amino_acid': 'K', 'amino_acid_name': 'Lysine'}},
    "AAG": {'annotations': {'amino_acid': 'K', 'amino_acid_name': 'Lysine'}},
    "GAT": {'annotations': {'amino_acid': 'D', 'amino_acid_name': 'Aspartic acid'}},
    "GAC": {'annotations': {'amino_acid': 'D', 'amino_acid_name': 'Aspartic acid'}},
    "GAA": {'annotations': {'amino_acid': 'E', 'amino_acid_name': 'Glutamic acid'}},
    "GAG": {'annotations': {'amino_acid': 'E', 'amino_acid_name': 'Glutamic acid'}},
    "TGT": {'annotations': {'amino_acid': 'C', 'amino_acid_name': 'Cysteine'}},
    "TGC": {'annotations': {'amino_acid': 'C', 'amino_acid_name': 'Cysteine'}},
    "TGG": {'annotations': {'amino_acid': 'W', 'amino_acid_name': 'Tryptophan'}},
    "CGT": {'annotations': {'amino_acid': 'R', 'amino_acid_name': 'Arginine'}},
    "CGC": {'annotations': {'amino_acid': 'R', 'amino_acid_name': 'Arginine'}},
    "CGA": {'annotations': {'amino_acid': 'R', 'amino_acid_name': 'Arginine'}},
    "CGG": {'annotations': {'amino_acid': 'R', 'amino_acid_name': 'Arginine'}},
    "AGA": {'annotations': {'amino_acid': 'R', 'amino_acid_name': 'Arginine'}},
    "AGG": {'annotations': {'amino_acid': 'R', 'amino_acid_name': 'Arginine'}},
    "GGT": {'annotations': {'amino_acid': 'G', 'amino_acid_name': 'Glycine'}},
    "GGC": {'annotations': {'amino_acid': 'G', 'amino_acid_name': 'Glycine'}},
    "GGA": {'annotations': {'amino_acid': 'G', 'amino_acid_name': 'Glycine'}},
    "GGG": {'annotations': {'amino_acid': 'G', 'amino_acid_name': 'Glycine'}},
}

class NucleotideModificationEnum(RichEnum):
    """
    Common nucleotide modifications
    """
    # Enum members
    FIVE_METHYL_C = "FIVE_METHYL_C"
    SIX_METHYL_A = "SIX_METHYL_A"
    PSEUDOURIDINE = "PSEUDOURIDINE"
    INOSINE = "INOSINE"
    DIHYDROURIDINE = "DIHYDROURIDINE"
    SEVEN_METHYL_G = "SEVEN_METHYL_G"
    FIVE_HYDROXY_METHYL_C = "FIVE_HYDROXY_METHYL_C"
    EIGHT_OXO_G = "EIGHT_OXO_G"

# Set metadata after class creation
NucleotideModificationEnum._metadata = {
    "FIVE_METHYL_C": {'description': '5-methylcytosine', 'meaning': 'CHEBI:27551', 'annotations': {'symbol': 'm5C', 'type': 'DNA methylation', 'function': 'gene regulation'}},
    "SIX_METHYL_A": {'description': 'N6-methyladenosine', 'meaning': 'CHEBI:21891', 'annotations': {'symbol': 'm6A', 'type': 'RNA modification', 'function': 'RNA stability, translation'}},
    "PSEUDOURIDINE": {'description': 'Pseudouridine', 'meaning': 'CHEBI:17802', 'annotations': {'symbol': 'Ψ', 'type': 'RNA modification', 'function': 'RNA stability'}},
    "INOSINE": {'description': 'Inosine', 'meaning': 'CHEBI:17596', 'annotations': {'symbol': 'I', 'type': 'RNA editing', 'pairs_with': 'A, C, U'}},
    "DIHYDROURIDINE": {'description': 'Dihydrouridine', 'meaning': 'CHEBI:23774', 'annotations': {'symbol': 'D', 'type': 'tRNA modification'}},
    "SEVEN_METHYL_G": {'description': '7-methylguanosine', 'meaning': 'CHEBI:20794', 'annotations': {'symbol': 'm7G', 'type': 'mRNA cap', 'function': 'translation initiation'}},
    "FIVE_HYDROXY_METHYL_C": {'description': '5-hydroxymethylcytosine', 'meaning': 'CHEBI:76792', 'annotations': {'symbol': 'hmC', 'type': 'DNA modification', 'function': 'demethylation intermediate'}},
    "EIGHT_OXO_G": {'description': '8-oxoguanine', 'meaning': 'CHEBI:44605', 'annotations': {'symbol': '8-oxoG', 'type': 'oxidative damage', 'pairs_with': 'A or C'}},
}

class SequenceQualityEnum(RichEnum):
    """
    Sequence quality indicators (Phred scores)
    """
    # Enum members
    Q0 = "Q0"
    Q10 = "Q10"
    Q20 = "Q20"
    Q30 = "Q30"
    Q40 = "Q40"
    Q50 = "Q50"
    Q60 = "Q60"

# Set metadata after class creation
SequenceQualityEnum._metadata = {
    "Q0": {'description': 'Phred quality 0 (100% error probability)', 'annotations': {'phred_score': '0', 'error_probability': '1.0', 'ascii_char': '!'}},
    "Q10": {'description': 'Phred quality 10 (10% error probability)', 'annotations': {'phred_score': '10', 'error_probability': '0.1', 'ascii_char': '+'}},
    "Q20": {'description': 'Phred quality 20 (1% error probability)', 'annotations': {'phred_score': '20', 'error_probability': '0.01', 'ascii_char': '5'}},
    "Q30": {'description': 'Phred quality 30 (0.1% error probability)', 'annotations': {'phred_score': '30', 'error_probability': '0.001', 'ascii_char': '?'}},
    "Q40": {'description': 'Phred quality 40 (0.01% error probability)', 'annotations': {'phred_score': '40', 'error_probability': '0.0001', 'ascii_char': 'I'}},
    "Q50": {'description': 'Phred quality 50 (0.001% error probability)', 'annotations': {'phred_score': '50', 'error_probability': '0.00001', 'ascii_char': 'S'}},
    "Q60": {'description': 'Phred quality 60 (0.0001% error probability)', 'annotations': {'phred_score': '60', 'error_probability': '0.000001', 'ascii_char': ']'}},
}

class SubatomicParticleEnum(RichEnum):
    """
    Fundamental and composite subatomic particles
    """
    # Enum members
    ELECTRON = "ELECTRON"
    POSITRON = "POSITRON"
    MUON = "MUON"
    TAU_LEPTON = "TAU_LEPTON"
    ELECTRON_NEUTRINO = "ELECTRON_NEUTRINO"
    MUON_NEUTRINO = "MUON_NEUTRINO"
    TAU_NEUTRINO = "TAU_NEUTRINO"
    UP_QUARK = "UP_QUARK"
    DOWN_QUARK = "DOWN_QUARK"
    CHARM_QUARK = "CHARM_QUARK"
    STRANGE_QUARK = "STRANGE_QUARK"
    TOP_QUARK = "TOP_QUARK"
    BOTTOM_QUARK = "BOTTOM_QUARK"
    PHOTON = "PHOTON"
    W_BOSON = "W_BOSON"
    Z_BOSON = "Z_BOSON"
    GLUON = "GLUON"
    HIGGS_BOSON = "HIGGS_BOSON"
    PROTON = "PROTON"
    NEUTRON = "NEUTRON"
    ALPHA_PARTICLE = "ALPHA_PARTICLE"
    DEUTERON = "DEUTERON"
    TRITON = "TRITON"

# Set metadata after class creation
SubatomicParticleEnum._metadata = {
    "ELECTRON": {'description': 'Elementary particle with -1 charge, spin 1/2', 'meaning': 'CHEBI:10545', 'annotations': {'mass': '0.51099895 MeV/c²', 'charge': '-1', 'spin': '1/2', 'type': 'lepton'}},
    "POSITRON": {'description': 'Antiparticle of electron with +1 charge', 'meaning': 'CHEBI:30225', 'annotations': {'mass': '0.51099895 MeV/c²', 'charge': '+1', 'spin': '1/2', 'type': 'lepton'}},
    "MUON": {'description': 'Heavy lepton with -1 charge', 'meaning': 'CHEBI:36356', 'annotations': {'mass': '105.658 MeV/c²', 'charge': '-1', 'spin': '1/2', 'type': 'lepton'}},
    "TAU_LEPTON": {'description': 'Heaviest lepton with -1 charge', 'meaning': 'CHEBI:36355', 'annotations': {'mass': '1777.05 MeV/c²', 'charge': '-1', 'spin': '1/2', 'type': 'lepton'}},
    "ELECTRON_NEUTRINO": {'description': 'Electron neutrino, nearly massless', 'meaning': 'CHEBI:30223', 'annotations': {'mass': '<2.2 eV/c²', 'charge': '0', 'spin': '1/2', 'type': 'lepton'}},
    "MUON_NEUTRINO": {'description': 'Muon neutrino', 'meaning': 'CHEBI:36353', 'annotations': {'mass': '<0.17 MeV/c²', 'charge': '0', 'spin': '1/2', 'type': 'lepton'}},
    "TAU_NEUTRINO": {'description': 'Tau neutrino', 'meaning': 'CHEBI:36354', 'annotations': {'mass': '<15.5 MeV/c²', 'charge': '0', 'spin': '1/2', 'type': 'lepton'}},
    "UP_QUARK": {'description': 'First generation quark with +2/3 charge', 'meaning': 'CHEBI:36366', 'annotations': {'mass': '2.16 MeV/c²', 'charge': '+2/3', 'spin': '1/2', 'type': 'quark', 'generation': '1'}},
    "DOWN_QUARK": {'description': 'First generation quark with -1/3 charge', 'meaning': 'CHEBI:36367', 'annotations': {'mass': '4.67 MeV/c²', 'charge': '-1/3', 'spin': '1/2', 'type': 'quark', 'generation': '1'}},
    "CHARM_QUARK": {'description': 'Second generation quark with +2/3 charge', 'meaning': 'CHEBI:36369', 'annotations': {'mass': '1.27 GeV/c²', 'charge': '+2/3', 'spin': '1/2', 'type': 'quark', 'generation': '2'}},
    "STRANGE_QUARK": {'description': 'Second generation quark with -1/3 charge', 'meaning': 'CHEBI:36368', 'annotations': {'mass': '93.4 MeV/c²', 'charge': '-1/3', 'spin': '1/2', 'type': 'quark', 'generation': '2'}},
    "TOP_QUARK": {'description': 'Third generation quark with +2/3 charge', 'meaning': 'CHEBI:36371', 'annotations': {'mass': '172.76 GeV/c²', 'charge': '+2/3', 'spin': '1/2', 'type': 'quark', 'generation': '3'}},
    "BOTTOM_QUARK": {'description': 'Third generation quark with -1/3 charge', 'meaning': 'CHEBI:36370', 'annotations': {'mass': '4.18 GeV/c²', 'charge': '-1/3', 'spin': '1/2', 'type': 'quark', 'generation': '3'}},
    "PHOTON": {'description': 'Force carrier for electromagnetic interaction', 'meaning': 'CHEBI:30212', 'annotations': {'mass': '0', 'charge': '0', 'spin': '1', 'type': 'gauge boson'}},
    "W_BOSON": {'description': 'Force carrier for weak interaction', 'meaning': 'CHEBI:36343', 'annotations': {'mass': '80.379 GeV/c²', 'charge': '±1', 'spin': '1', 'type': 'gauge boson'}},
    "Z_BOSON": {'description': 'Force carrier for weak interaction', 'meaning': 'CHEBI:36344', 'annotations': {'mass': '91.1876 GeV/c²', 'charge': '0', 'spin': '1', 'type': 'gauge boson'}},
    "GLUON": {'description': 'Force carrier for strong interaction', 'annotations': {'mass': '0', 'charge': '0', 'spin': '1', 'type': 'gauge boson', 'color_charge': 'yes'}},
    "HIGGS_BOSON": {'description': 'Scalar boson responsible for mass', 'meaning': 'CHEBI:146278', 'annotations': {'mass': '125.25 GeV/c²', 'charge': '0', 'spin': '0', 'type': 'scalar boson'}},
    "PROTON": {'description': 'Positively charged nucleon', 'meaning': 'CHEBI:24636', 'annotations': {'mass': '938.272 MeV/c²', 'charge': '+1', 'spin': '1/2', 'type': 'baryon', 'composition': 'uud'}},
    "NEUTRON": {'description': 'Neutral nucleon', 'meaning': 'CHEBI:33254', 'annotations': {'mass': '939.565 MeV/c²', 'charge': '0', 'spin': '1/2', 'type': 'baryon', 'composition': 'udd'}},
    "ALPHA_PARTICLE": {'description': 'Helium-4 nucleus', 'meaning': 'CHEBI:30216', 'annotations': {'mass': '3727.379 MeV/c²', 'charge': '+2', 'composition': '2 protons, 2 neutrons'}},
    "DEUTERON": {'description': 'Hydrogen-2 nucleus', 'meaning': 'CHEBI:29233', 'annotations': {'mass': '1875.613 MeV/c²', 'charge': '+1', 'composition': '1 proton, 1 neutron'}},
    "TRITON": {'description': 'Hydrogen-3 nucleus', 'meaning': 'CHEBI:29234', 'annotations': {'mass': '2808.921 MeV/c²', 'charge': '+1', 'composition': '1 proton, 2 neutrons'}},
}

class BondTypeEnum(RichEnum):
    """
    Types of chemical bonds
    """
    # Enum members
    SINGLE = "SINGLE"
    DOUBLE = "DOUBLE"
    TRIPLE = "TRIPLE"
    QUADRUPLE = "QUADRUPLE"
    AROMATIC = "AROMATIC"
    IONIC = "IONIC"
    HYDROGEN = "HYDROGEN"
    METALLIC = "METALLIC"
    VAN_DER_WAALS = "VAN_DER_WAALS"
    COORDINATE = "COORDINATE"
    PI = "PI"
    SIGMA = "SIGMA"

# Set metadata after class creation
BondTypeEnum._metadata = {
    "SINGLE": {'description': 'Single covalent bond', 'meaning': 'gc:Single', 'annotations': {'bond_order': '1', 'electrons_shared': '2'}},
    "DOUBLE": {'description': 'Double covalent bond', 'meaning': 'gc:Double', 'annotations': {'bond_order': '2', 'electrons_shared': '4'}},
    "TRIPLE": {'description': 'Triple covalent bond', 'meaning': 'gc:Triple', 'annotations': {'bond_order': '3', 'electrons_shared': '6'}},
    "QUADRUPLE": {'description': 'Quadruple bond (rare, in transition metals)', 'meaning': 'gc:Quadruple', 'annotations': {'bond_order': '4', 'electrons_shared': '8'}},
    "AROMATIC": {'description': 'Aromatic bond', 'meaning': 'gc:AromaticBond', 'annotations': {'bond_order': '1.5', 'delocalized': 'true'}},
    "IONIC": {'description': 'Ionic bond', 'meaning': 'CHEBI:50860', 'annotations': {'type': 'electrostatic'}},
    "HYDROGEN": {'description': 'Hydrogen bond', 'meaning': 'CHEBI:50839', 'annotations': {'type': 'weak interaction', 'energy': '5-30 kJ/mol'}},
    "METALLIC": {'description': 'Metallic bond', 'annotations': {'type': 'delocalized electrons'}},
    "VAN_DER_WAALS": {'description': 'Van der Waals interaction', 'annotations': {'type': 'weak interaction', 'energy': '0.4-4 kJ/mol'}},
    "COORDINATE": {'description': 'Coordinate/dative covalent bond', 'meaning': 'CHEBI:33240', 'annotations': {'electrons_from': 'one atom'}},
    "PI": {'description': 'Pi bond', 'annotations': {'orbital_overlap': 'side-to-side'}},
    "SIGMA": {'description': 'Sigma bond', 'annotations': {'orbital_overlap': 'head-to-head'}},
}

class PeriodicTableBlockEnum(RichEnum):
    """
    Blocks of the periodic table
    """
    # Enum members
    S_BLOCK = "S_BLOCK"
    P_BLOCK = "P_BLOCK"
    D_BLOCK = "D_BLOCK"
    F_BLOCK = "F_BLOCK"

# Set metadata after class creation
PeriodicTableBlockEnum._metadata = {
    "S_BLOCK": {'description': 's-block elements (groups 1 and 2)', 'meaning': 'CHEBI:33674', 'annotations': {'valence_orbital': 's', 'groups': '1,2'}},
    "P_BLOCK": {'description': 'p-block elements (groups 13-18)', 'meaning': 'CHEBI:33675', 'annotations': {'valence_orbital': 'p', 'groups': '13,14,15,16,17,18'}},
    "D_BLOCK": {'description': 'd-block elements (transition metals)', 'meaning': 'CHEBI:33561', 'annotations': {'valence_orbital': 'd', 'groups': '3-12'}},
    "F_BLOCK": {'description': 'f-block elements (lanthanides and actinides)', 'meaning': 'CHEBI:33562', 'annotations': {'valence_orbital': 'f', 'series': 'lanthanides, actinides'}},
}

class ElementFamilyEnum(RichEnum):
    """
    Chemical element families/groups
    """
    # Enum members
    ALKALI_METALS = "ALKALI_METALS"
    ALKALINE_EARTH_METALS = "ALKALINE_EARTH_METALS"
    TRANSITION_METALS = "TRANSITION_METALS"
    LANTHANIDES = "LANTHANIDES"
    ACTINIDES = "ACTINIDES"
    CHALCOGENS = "CHALCOGENS"
    HALOGENS = "HALOGENS"
    NOBLE_GASES = "NOBLE_GASES"
    METALLOIDS = "METALLOIDS"
    POST_TRANSITION_METALS = "POST_TRANSITION_METALS"
    NONMETALS = "NONMETALS"

# Set metadata after class creation
ElementFamilyEnum._metadata = {
    "ALKALI_METALS": {'description': 'Group 1 elements (except hydrogen)', 'meaning': 'CHEBI:22314', 'annotations': {'group': '1', 'elements': 'Li, Na, K, Rb, Cs, Fr'}},
    "ALKALINE_EARTH_METALS": {'description': 'Group 2 elements', 'meaning': 'CHEBI:22315', 'annotations': {'group': '2', 'elements': 'Be, Mg, Ca, Sr, Ba, Ra'}},
    "TRANSITION_METALS": {'description': 'd-block elements', 'meaning': 'CHEBI:27081', 'annotations': {'groups': '3-12'}},
    "LANTHANIDES": {'description': 'Lanthanide series', 'meaning': 'CHEBI:33768', 'annotations': {'atomic_numbers': '57-71'}},
    "ACTINIDES": {'description': 'Actinide series', 'meaning': 'CHEBI:33769', 'annotations': {'atomic_numbers': '89-103'}},
    "CHALCOGENS": {'description': 'Group 16 elements', 'meaning': 'CHEBI:33303', 'annotations': {'group': '16', 'elements': 'O, S, Se, Te, Po'}},
    "HALOGENS": {'description': 'Group 17 elements', 'meaning': 'CHEBI:47902', 'annotations': {'group': '17', 'elements': 'F, Cl, Br, I, At'}},
    "NOBLE_GASES": {'description': 'Group 18 elements', 'meaning': 'CHEBI:33310', 'annotations': {'group': '18', 'elements': 'He, Ne, Ar, Kr, Xe, Rn'}},
    "METALLOIDS": {'description': 'Elements with intermediate properties', 'meaning': 'CHEBI:33559', 'annotations': {'elements': 'B, Si, Ge, As, Sb, Te, Po'}},
    "POST_TRANSITION_METALS": {'description': 'Metals after the transition series', 'annotations': {'elements': 'Al, Ga, In, Tl, Sn, Pb, Bi'}},
    "NONMETALS": {'description': 'Non-metallic elements', 'meaning': 'CHEBI:25585', 'annotations': {'elements': 'H, C, N, O, F, P, S, Cl, Se, Br, I'}},
}

class ElementMetallicClassificationEnum(RichEnum):
    """
    Metallic character classification
    """
    # Enum members
    METALLIC = "METALLIC"
    NON_METALLIC = "NON_METALLIC"
    SEMI_METALLIC = "SEMI_METALLIC"

# Set metadata after class creation
ElementMetallicClassificationEnum._metadata = {
    "METALLIC": {'description': 'Metallic elements', 'meaning': 'damlpt:Metallic', 'annotations': {'properties': 'conductive, malleable, ductile'}},
    "NON_METALLIC": {'description': 'Non-metallic elements', 'meaning': 'damlpt:Non-Metallic', 'annotations': {'properties': 'poor conductors, brittle'}},
    "SEMI_METALLIC": {'description': 'Semi-metallic/metalloid elements', 'meaning': 'damlpt:Semi-Metallic', 'annotations': {'properties': 'intermediate properties'}},
}

class HardOrSoftEnum(RichEnum):
    """
    HSAB (Hard Soft Acid Base) classification
    """
    # Enum members
    HARD = "HARD"
    SOFT = "SOFT"
    BORDERLINE = "BORDERLINE"

# Set metadata after class creation
HardOrSoftEnum._metadata = {
    "HARD": {'description': 'Hard acids/bases (small, high charge density)', 'annotations': {'examples': 'H+, Li+, Mg2+, Al3+, F-, OH-', 'polarizability': 'low'}},
    "SOFT": {'description': 'Soft acids/bases (large, low charge density)', 'annotations': {'examples': 'Cu+, Ag+, Au+, I-, S2-', 'polarizability': 'high'}},
    "BORDERLINE": {'description': 'Borderline acids/bases', 'annotations': {'examples': 'Fe2+, Co2+, Ni2+, Cu2+, Zn2+', 'polarizability': 'intermediate'}},
}

class BronstedAcidBaseRoleEnum(RichEnum):
    """
    Brønsted-Lowry acid-base roles
    """
    # Enum members
    ACID = "ACID"
    BASE = "BASE"
    AMPHOTERIC = "AMPHOTERIC"

# Set metadata after class creation
BronstedAcidBaseRoleEnum._metadata = {
    "ACID": {'description': 'Proton donor', 'meaning': 'CHEBI:39141', 'annotations': {'definition': 'species that donates H+'}},
    "BASE": {'description': 'Proton acceptor', 'meaning': 'CHEBI:39142', 'annotations': {'definition': 'species that accepts H+'}},
    "AMPHOTERIC": {'description': 'Can act as both acid and base', 'annotations': {'definition': 'species that can donate or accept H+', 'examples': 'H2O, HSO4-, H2PO4-'}},
}

class LewisAcidBaseRoleEnum(RichEnum):
    """
    Lewis acid-base roles
    """
    # Enum members
    LEWIS_ACID = "LEWIS_ACID"
    LEWIS_BASE = "LEWIS_BASE"

# Set metadata after class creation
LewisAcidBaseRoleEnum._metadata = {
    "LEWIS_ACID": {'description': 'Electron pair acceptor', 'annotations': {'definition': 'species that accepts electron pair', 'examples': 'BF3, AlCl3, H+'}},
    "LEWIS_BASE": {'description': 'Electron pair donor', 'annotations': {'definition': 'species that donates electron pair', 'examples': 'NH3, OH-, H2O'}},
}

class OxidationStateEnum(RichEnum):
    """
    Common oxidation states
    """
    # Enum members
    MINUS_4 = "MINUS_4"
    MINUS_3 = "MINUS_3"
    MINUS_2 = "MINUS_2"
    MINUS_1 = "MINUS_1"
    ZERO = "ZERO"
    PLUS_1 = "PLUS_1"
    PLUS_2 = "PLUS_2"
    PLUS_3 = "PLUS_3"
    PLUS_4 = "PLUS_4"
    PLUS_5 = "PLUS_5"
    PLUS_6 = "PLUS_6"
    PLUS_7 = "PLUS_7"
    PLUS_8 = "PLUS_8"

# Set metadata after class creation
OxidationStateEnum._metadata = {
    "MINUS_4": {'description': 'Oxidation state -4', 'annotations': {'value': '-4', 'example': 'C in CH4'}},
    "MINUS_3": {'description': 'Oxidation state -3', 'annotations': {'value': '-3', 'example': 'N in NH3'}},
    "MINUS_2": {'description': 'Oxidation state -2', 'annotations': {'value': '-2', 'example': 'O in H2O'}},
    "MINUS_1": {'description': 'Oxidation state -1', 'annotations': {'value': '-1', 'example': 'Cl in NaCl'}},
    "ZERO": {'description': 'Oxidation state 0', 'annotations': {'value': '0', 'example': 'elemental forms'}},
    "PLUS_1": {'description': 'Oxidation state +1', 'annotations': {'value': '+1', 'example': 'Na in NaCl'}},
    "PLUS_2": {'description': 'Oxidation state +2', 'annotations': {'value': '+2', 'example': 'Ca in CaCl2'}},
    "PLUS_3": {'description': 'Oxidation state +3', 'annotations': {'value': '+3', 'example': 'Al in Al2O3'}},
    "PLUS_4": {'description': 'Oxidation state +4', 'annotations': {'value': '+4', 'example': 'C in CO2'}},
    "PLUS_5": {'description': 'Oxidation state +5', 'annotations': {'value': '+5', 'example': 'P in PO4³⁻'}},
    "PLUS_6": {'description': 'Oxidation state +6', 'annotations': {'value': '+6', 'example': 'S in SO4²⁻'}},
    "PLUS_7": {'description': 'Oxidation state +7', 'annotations': {'value': '+7', 'example': 'Mn in MnO4⁻'}},
    "PLUS_8": {'description': 'Oxidation state +8', 'annotations': {'value': '+8', 'example': 'Os in OsO4'}},
}

class ChiralityEnum(RichEnum):
    """
    Chirality/stereochemistry descriptors
    """
    # Enum members
    R = "R"
    S = "S"
    D = "D"
    L = "L"
    RACEMIC = "RACEMIC"
    MESO = "MESO"
    E = "E"
    Z = "Z"

# Set metadata after class creation
ChiralityEnum._metadata = {
    "R": {'description': 'Rectus (right) configuration', 'annotations': {'cahn_ingold_prelog': 'true'}},
    "S": {'description': 'Sinister (left) configuration', 'annotations': {'cahn_ingold_prelog': 'true'}},
    "D": {'description': 'Dextrorotatory', 'annotations': {'fischer_projection': 'true', 'optical_rotation': 'positive'}},
    "L": {'description': 'Levorotatory', 'annotations': {'fischer_projection': 'true', 'optical_rotation': 'negative'}},
    "RACEMIC": {'description': 'Racemic mixture (50:50 of enantiomers)', 'annotations': {'optical_rotation': 'zero'}},
    "MESO": {'description': 'Meso compound (achiral despite stereocenters)', 'annotations': {'internal_symmetry': 'true'}},
    "E": {'description': 'Entgegen (opposite) configuration', 'annotations': {'geometric_isomer': 'true'}},
    "Z": {'description': 'Zusammen (together) configuration', 'annotations': {'geometric_isomer': 'true'}},
}

class NanostructureMorphologyEnum(RichEnum):
    """
    Types of nanostructure morphologies
    """
    # Enum members
    NANOTUBE = "NANOTUBE"
    NANOPARTICLE = "NANOPARTICLE"
    NANOROD = "NANOROD"
    QUANTUM_DOT = "QUANTUM_DOT"
    NANOWIRE = "NANOWIRE"
    NANOSHEET = "NANOSHEET"
    NANOFIBER = "NANOFIBER"

# Set metadata after class creation
NanostructureMorphologyEnum._metadata = {
    "NANOTUBE": {'description': 'Cylindrical nanostructure', 'meaning': 'CHEBI:50796', 'annotations': {'dimensions': '1D', 'examples': 'carbon nanotubes'}},
    "NANOPARTICLE": {'description': 'Particle with nanoscale dimensions', 'meaning': 'CHEBI:50803', 'annotations': {'dimensions': '0D', 'size_range': '1-100 nm'}},
    "NANOROD": {'description': 'Rod-shaped nanostructure', 'meaning': 'CHEBI:50805', 'annotations': {'dimensions': '1D', 'aspect_ratio': '3-20'}},
    "QUANTUM_DOT": {'description': 'Semiconductor nanocrystal', 'meaning': 'CHEBI:50853', 'annotations': {'dimensions': '0D', 'property': 'quantum confinement'}},
    "NANOWIRE": {'description': 'Wire with nanoscale diameter', 'annotations': {'dimensions': '1D', 'diameter': '<100 nm'}},
    "NANOSHEET": {'description': 'Two-dimensional nanostructure', 'annotations': {'dimensions': '2D', 'thickness': '<100 nm'}},
    "NANOFIBER": {'description': 'Fiber with nanoscale diameter', 'annotations': {'dimensions': '1D', 'diameter': '<1000 nm'}},
}

class ReactionTypeEnum(RichEnum):
    """
    Types of chemical reactions
    """
    # Enum members
    SYNTHESIS = "SYNTHESIS"
    DECOMPOSITION = "DECOMPOSITION"
    SINGLE_DISPLACEMENT = "SINGLE_DISPLACEMENT"
    DOUBLE_DISPLACEMENT = "DOUBLE_DISPLACEMENT"
    COMBUSTION = "COMBUSTION"
    SUBSTITUTION = "SUBSTITUTION"
    ELIMINATION = "ELIMINATION"
    ADDITION = "ADDITION"
    REARRANGEMENT = "REARRANGEMENT"
    OXIDATION = "OXIDATION"
    REDUCTION = "REDUCTION"
    DIELS_ALDER = "DIELS_ALDER"
    FRIEDEL_CRAFTS = "FRIEDEL_CRAFTS"
    GRIGNARD = "GRIGNARD"
    WITTIG = "WITTIG"
    ALDOL = "ALDOL"
    MICHAEL_ADDITION = "MICHAEL_ADDITION"

# Set metadata after class creation
ReactionTypeEnum._metadata = {
    "SYNTHESIS": {'description': 'Combination reaction (A + B → AB)', 'annotations': {'aliases': 'combination, addition', 'pattern': 'A + B → AB'}},
    "DECOMPOSITION": {'description': 'Breakdown reaction (AB → A + B)', 'annotations': {'aliases': 'analysis', 'pattern': 'AB → A + B'}},
    "SINGLE_DISPLACEMENT": {'description': 'Single replacement reaction (A + BC → AC + B)', 'annotations': {'aliases': 'single replacement', 'pattern': 'A + BC → AC + B'}},
    "DOUBLE_DISPLACEMENT": {'description': 'Double replacement reaction (AB + CD → AD + CB)', 'annotations': {'aliases': 'double replacement, metathesis', 'pattern': 'AB + CD → AD + CB'}},
    "COMBUSTION": {'description': 'Reaction with oxygen producing heat and light', 'annotations': {'reactant': 'oxygen', 'products': 'usually CO2 and H2O'}},
    "SUBSTITUTION": {'description': 'Replacement of one group by another', 'meaning': 'MOP:0000790', 'annotations': {'subtypes': 'SN1, SN2, SNAr'}},
    "ELIMINATION": {'description': 'Removal of atoms/groups forming double bond', 'meaning': 'MOP:0000656', 'annotations': {'subtypes': 'E1, E2, E1cB'}},
    "ADDITION": {'description': 'Addition to multiple bond', 'meaning': 'MOP:0000642', 'annotations': {'subtypes': 'electrophilic, nucleophilic, radical'}},
    "REARRANGEMENT": {'description': 'Reorganization of molecular structure', 'annotations': {'examples': 'Claisen, Cope, Wagner-Meerwein'}},
    "OXIDATION": {'description': 'Loss of electrons or increase in oxidation state', 'annotations': {'electron_change': 'loss'}},
    "REDUCTION": {'description': 'Gain of electrons or decrease in oxidation state', 'annotations': {'electron_change': 'gain'}},
    "DIELS_ALDER": {'description': '[4+2] cycloaddition reaction', 'meaning': 'RXNO:0000006', 'annotations': {'type': 'pericyclic', 'components': 'diene + dienophile'}},
    "FRIEDEL_CRAFTS": {'description': 'Electrophilic aromatic substitution', 'meaning': 'RXNO:0000369', 'annotations': {'subtypes': 'alkylation, acylation'}},
    "GRIGNARD": {'description': 'Organometallic addition reaction', 'meaning': 'RXNO:0000014', 'annotations': {'reagent': 'RMgX'}},
    "WITTIG": {'description': 'Alkene formation from phosphonium ylide', 'meaning': 'RXNO:0000015', 'annotations': {'product': 'alkene'}},
    "ALDOL": {'description': 'Condensation forming β-hydroxy carbonyl', 'meaning': 'RXNO:0000017', 'annotations': {'mechanism': 'enolate addition'}},
    "MICHAEL_ADDITION": {'description': '1,4-addition to α,β-unsaturated carbonyl', 'meaning': 'RXNO:0000009', 'annotations': {'type': 'conjugate addition'}},
}

class ReactionMechanismEnum(RichEnum):
    """
    Reaction mechanism types
    """
    # Enum members
    SN1 = "SN1"
    SN2 = "SN2"
    E1 = "E1"
    E2 = "E2"
    E1CB = "E1CB"
    RADICAL = "RADICAL"
    PERICYCLIC = "PERICYCLIC"
    ELECTROPHILIC_AROMATIC = "ELECTROPHILIC_AROMATIC"
    NUCLEOPHILIC_AROMATIC = "NUCLEOPHILIC_AROMATIC"
    ADDITION_ELIMINATION = "ADDITION_ELIMINATION"

# Set metadata after class creation
ReactionMechanismEnum._metadata = {
    "SN1": {'description': 'Unimolecular nucleophilic substitution', 'annotations': {'rate_determining': 'carbocation formation', 'stereochemistry': 'racemization'}},
    "SN2": {'description': 'Bimolecular nucleophilic substitution', 'annotations': {'rate_determining': 'concerted', 'stereochemistry': 'inversion'}},
    "E1": {'description': 'Unimolecular elimination', 'annotations': {'intermediate': 'carbocation'}},
    "E2": {'description': 'Bimolecular elimination', 'annotations': {'requirement': 'antiperiplanar'}},
    "E1CB": {'description': 'Elimination via conjugate base', 'annotations': {'intermediate': 'carbanion'}},
    "RADICAL": {'description': 'Free radical mechanism', 'annotations': {'initiation': 'homolytic cleavage'}},
    "PERICYCLIC": {'description': 'Concerted cyclic electron reorganization', 'annotations': {'examples': 'Diels-Alder, Cope'}},
    "ELECTROPHILIC_AROMATIC": {'description': 'Electrophilic aromatic substitution', 'annotations': {'intermediate': 'arenium ion'}},
    "NUCLEOPHILIC_AROMATIC": {'description': 'Nucleophilic aromatic substitution', 'annotations': {'requirement': 'electron-withdrawing groups'}},
    "ADDITION_ELIMINATION": {'description': 'Addition followed by elimination', 'annotations': {'intermediate': 'tetrahedral'}},
}

class CatalystTypeEnum(RichEnum):
    """
    Types of catalysts
    """
    # Enum members
    HOMOGENEOUS = "HOMOGENEOUS"
    HETEROGENEOUS = "HETEROGENEOUS"
    ENZYME = "ENZYME"
    ORGANOCATALYST = "ORGANOCATALYST"
    PHOTOCATALYST = "PHOTOCATALYST"
    PHASE_TRANSFER = "PHASE_TRANSFER"
    ACID = "ACID"
    BASE = "BASE"
    METAL = "METAL"
    BIFUNCTIONAL = "BIFUNCTIONAL"

# Set metadata after class creation
CatalystTypeEnum._metadata = {
    "HOMOGENEOUS": {'description': 'Catalyst in same phase as reactants', 'annotations': {'phase': 'same as reactants', 'examples': 'acid, base, metal complexes'}},
    "HETEROGENEOUS": {'description': 'Catalyst in different phase from reactants', 'annotations': {'phase': 'different from reactants', 'examples': 'Pt/Pd on carbon, zeolites'}},
    "ENZYME": {'description': 'Biological catalyst', 'meaning': 'CHEBI:23357', 'annotations': {'type': 'protein', 'specificity': 'high'}},
    "ORGANOCATALYST": {'description': 'Small organic molecule catalyst', 'annotations': {'metal_free': 'true', 'examples': 'proline, thiourea'}},
    "PHOTOCATALYST": {'description': 'Light-activated catalyst', 'annotations': {'activation': 'light', 'examples': 'TiO2, Ru complexes'}},
    "PHASE_TRANSFER": {'description': 'Catalyst facilitating reaction between phases', 'annotations': {'function': 'transfers reactant between phases'}},
    "ACID": {'description': 'Acid catalyst', 'annotations': {'mechanism': 'proton donation'}},
    "BASE": {'description': 'Base catalyst', 'annotations': {'mechanism': 'proton abstraction'}},
    "METAL": {'description': 'Metal catalyst', 'annotations': {'examples': 'Pd, Pt, Ni, Ru'}},
    "BIFUNCTIONAL": {'description': 'Catalyst with two active sites', 'annotations': {'sites': 'multiple'}},
}

class ReactionConditionEnum(RichEnum):
    """
    Reaction conditions
    """
    # Enum members
    ROOM_TEMPERATURE = "ROOM_TEMPERATURE"
    REFLUX = "REFLUX"
    CRYOGENIC = "CRYOGENIC"
    HIGH_PRESSURE = "HIGH_PRESSURE"
    VACUUM = "VACUUM"
    INERT_ATMOSPHERE = "INERT_ATMOSPHERE"
    MICROWAVE = "MICROWAVE"
    ULTRASOUND = "ULTRASOUND"
    PHOTOCHEMICAL = "PHOTOCHEMICAL"
    ELECTROCHEMICAL = "ELECTROCHEMICAL"
    FLOW = "FLOW"
    BATCH = "BATCH"

# Set metadata after class creation
ReactionConditionEnum._metadata = {
    "ROOM_TEMPERATURE": {'description': 'Standard room temperature (20-25°C)', 'annotations': {'temperature': '20-25°C'}},
    "REFLUX": {'description': 'Boiling with condensation return', 'annotations': {'temperature': 'solvent boiling point'}},
    "CRYOGENIC": {'description': 'Very low temperature conditions', 'annotations': {'temperature': '<-150°C', 'examples': 'liquid N2, liquid He'}},
    "HIGH_PRESSURE": {'description': 'Elevated pressure conditions', 'annotations': {'pressure': '>10 atm'}},
    "VACUUM": {'description': 'Reduced pressure conditions', 'annotations': {'pressure': '<1 atm'}},
    "INERT_ATMOSPHERE": {'description': 'Non-reactive gas atmosphere', 'annotations': {'gases': 'N2, Ar'}},
    "MICROWAVE": {'description': 'Microwave heating', 'annotations': {'heating': 'microwave irradiation'}},
    "ULTRASOUND": {'description': 'Ultrasonic conditions', 'annotations': {'activation': 'ultrasound'}},
    "PHOTOCHEMICAL": {'description': 'Light-induced conditions', 'annotations': {'activation': 'UV or visible light'}},
    "ELECTROCHEMICAL": {'description': 'Electrically driven conditions', 'annotations': {'activation': 'electric current'}},
    "FLOW": {'description': 'Continuous flow conditions', 'annotations': {'type': 'continuous process'}},
    "BATCH": {'description': 'Batch reaction conditions', 'annotations': {'type': 'batch process'}},
}

class ReactionRateOrderEnum(RichEnum):
    """
    Reaction rate orders
    """
    # Enum members
    ZERO_ORDER = "ZERO_ORDER"
    FIRST_ORDER = "FIRST_ORDER"
    SECOND_ORDER = "SECOND_ORDER"
    PSEUDO_FIRST_ORDER = "PSEUDO_FIRST_ORDER"
    FRACTIONAL_ORDER = "FRACTIONAL_ORDER"
    MIXED_ORDER = "MIXED_ORDER"

# Set metadata after class creation
ReactionRateOrderEnum._metadata = {
    "ZERO_ORDER": {'description': 'Rate independent of concentration', 'annotations': {'rate_law': 'rate = k', 'integrated': '[A] = [A]₀ - kt'}},
    "FIRST_ORDER": {'description': 'Rate proportional to concentration', 'annotations': {'rate_law': 'rate = k[A]', 'integrated': 'ln[A] = ln[A]₀ - kt'}},
    "SECOND_ORDER": {'description': 'Rate proportional to concentration squared', 'annotations': {'rate_law': 'rate = k[A]²', 'integrated': '1/[A] = 1/[A]₀ + kt'}},
    "PSEUDO_FIRST_ORDER": {'description': 'Apparent first order (excess reagent)', 'annotations': {'condition': 'one reagent in large excess'}},
    "FRACTIONAL_ORDER": {'description': 'Non-integer order', 'annotations': {'indicates': 'complex mechanism'}},
    "MIXED_ORDER": {'description': 'Different orders for different reactants', 'annotations': {'example': 'rate = k[A][B]²'}},
}

class EnzymeClassEnum(RichEnum):
    """
    EC enzyme classification
    """
    # Enum members
    OXIDOREDUCTASE = "OXIDOREDUCTASE"
    TRANSFERASE = "TRANSFERASE"
    HYDROLASE = "HYDROLASE"
    LYASE = "LYASE"
    ISOMERASE = "ISOMERASE"
    LIGASE = "LIGASE"
    TRANSLOCASE = "TRANSLOCASE"

# Set metadata after class creation
EnzymeClassEnum._metadata = {
    "OXIDOREDUCTASE": {'description': 'Catalyzes oxidation-reduction reactions', 'meaning': 'EC:1', 'annotations': {'EC_class': '1', 'examples': 'dehydrogenases, oxidases'}},
    "TRANSFERASE": {'description': 'Catalyzes group transfer reactions', 'meaning': 'EC:2', 'annotations': {'EC_class': '2', 'examples': 'kinases, transaminases'}},
    "HYDROLASE": {'description': 'Catalyzes hydrolysis reactions', 'meaning': 'EC:3', 'annotations': {'EC_class': '3', 'examples': 'proteases, lipases'}},
    "LYASE": {'description': 'Catalyzes non-hydrolytic additions/removals', 'meaning': 'EC:4', 'annotations': {'EC_class': '4', 'examples': 'decarboxylases, aldolases'}},
    "ISOMERASE": {'description': 'Catalyzes isomerization reactions', 'meaning': 'EC:5', 'annotations': {'EC_class': '5', 'examples': 'racemases, epimerases'}},
    "LIGASE": {'description': 'Catalyzes formation of bonds with ATP', 'meaning': 'EC:6', 'annotations': {'EC_class': '6', 'examples': 'synthetases, carboxylases'}},
    "TRANSLOCASE": {'description': 'Catalyzes movement across membranes', 'meaning': 'EC:7', 'annotations': {'EC_class': '7', 'examples': 'ATPases, ion pumps'}},
}

class SolventClassEnum(RichEnum):
    """
    Classes of solvents
    """
    # Enum members
    PROTIC = "PROTIC"
    APROTIC_POLAR = "APROTIC_POLAR"
    APROTIC_NONPOLAR = "APROTIC_NONPOLAR"
    IONIC_LIQUID = "IONIC_LIQUID"
    SUPERCRITICAL = "SUPERCRITICAL"
    AQUEOUS = "AQUEOUS"
    ORGANIC = "ORGANIC"
    GREEN = "GREEN"

# Set metadata after class creation
SolventClassEnum._metadata = {
    "PROTIC": {'description': 'Solvents with acidic hydrogen', 'annotations': {'H_bonding': 'donor', 'examples': 'water, alcohols, acids'}},
    "APROTIC_POLAR": {'description': 'Polar solvents without acidic H', 'annotations': {'H_bonding': 'acceptor only', 'examples': 'DMSO, DMF, acetone'}},
    "APROTIC_NONPOLAR": {'description': 'Nonpolar solvents', 'annotations': {'H_bonding': 'none', 'examples': 'hexane, benzene, CCl4'}},
    "IONIC_LIQUID": {'description': 'Room temperature ionic liquids', 'annotations': {'state': 'liquid salt', 'examples': 'imidazolium salts'}},
    "SUPERCRITICAL": {'description': 'Supercritical fluids', 'annotations': {'state': 'supercritical', 'examples': 'scCO2, scH2O'}},
    "AQUEOUS": {'description': 'Water-based solvents', 'annotations': {'base': 'water'}},
    "ORGANIC": {'description': 'Organic solvents', 'annotations': {'base': 'organic compounds'}},
    "GREEN": {'description': 'Environmentally friendly solvents', 'annotations': {'property': 'low environmental impact', 'examples': 'water, ethanol, scCO2'}},
}

class ThermodynamicParameterEnum(RichEnum):
    """
    Thermodynamic parameters
    """
    # Enum members
    ENTHALPY = "ENTHALPY"
    ENTROPY = "ENTROPY"
    GIBBS_ENERGY = "GIBBS_ENERGY"
    ACTIVATION_ENERGY = "ACTIVATION_ENERGY"
    HEAT_CAPACITY = "HEAT_CAPACITY"
    INTERNAL_ENERGY = "INTERNAL_ENERGY"

# Set metadata after class creation
ThermodynamicParameterEnum._metadata = {
    "ENTHALPY": {'description': 'Heat content (ΔH)', 'annotations': {'symbol': 'ΔH', 'units': 'kJ/mol'}},
    "ENTROPY": {'description': 'Disorder (ΔS)', 'annotations': {'symbol': 'ΔS', 'units': 'J/mol·K'}},
    "GIBBS_ENERGY": {'description': 'Free energy (ΔG)', 'annotations': {'symbol': 'ΔG', 'units': 'kJ/mol'}},
    "ACTIVATION_ENERGY": {'description': 'Energy barrier (Ea)', 'annotations': {'symbol': 'Ea', 'units': 'kJ/mol'}},
    "HEAT_CAPACITY": {'description': 'Heat capacity (Cp)', 'annotations': {'symbol': 'Cp', 'units': 'J/mol·K'}},
    "INTERNAL_ENERGY": {'description': 'Internal energy (ΔU)', 'annotations': {'symbol': 'ΔU', 'units': 'kJ/mol'}},
}

class SafetyColorEnum(RichEnum):
    """
    ANSI/ISO standard safety colors
    """
    # Enum members
    SAFETY_RED = "SAFETY_RED"
    SAFETY_ORANGE = "SAFETY_ORANGE"
    SAFETY_YELLOW = "SAFETY_YELLOW"
    SAFETY_GREEN = "SAFETY_GREEN"
    SAFETY_BLUE = "SAFETY_BLUE"
    SAFETY_PURPLE = "SAFETY_PURPLE"
    SAFETY_BLACK = "SAFETY_BLACK"
    SAFETY_WHITE = "SAFETY_WHITE"
    SAFETY_GRAY = "SAFETY_GRAY"
    SAFETY_BROWN = "SAFETY_BROWN"

# Set metadata after class creation
SafetyColorEnum._metadata = {
    "SAFETY_RED": {'description': 'Safety red - danger, stop, prohibition', 'meaning': 'HEX:C8102E', 'annotations': {'standard': 'ANSI Z535.1', 'pantone': 'PMS 186 C', 'usage': 'fire equipment, stop signs, danger signs'}},
    "SAFETY_ORANGE": {'description': 'Safety orange - warning of dangerous parts', 'meaning': 'HEX:FF6900', 'annotations': {'standard': 'ANSI Z535.1', 'pantone': 'PMS 151 C', 'usage': 'machine parts, exposed edges'}},
    "SAFETY_YELLOW": {'description': 'Safety yellow - caution, physical hazards', 'meaning': 'HEX:F6D04D', 'annotations': {'standard': 'ANSI Z535.1', 'pantone': 'PMS 116 C', 'usage': 'caution signs, physical hazards, stumbling'}},
    "SAFETY_GREEN": {'description': 'Safety green - safety, first aid, emergency egress', 'meaning': 'HEX:00843D', 'annotations': {'standard': 'ANSI Z535.1', 'pantone': 'PMS 355 C', 'usage': 'first aid, safety equipment, emergency exits'}},
    "SAFETY_BLUE": {'description': 'Safety blue - mandatory, information', 'meaning': 'HEX:005EB8', 'annotations': {'standard': 'ANSI Z535.1', 'pantone': 'PMS 285 C', 'usage': 'mandatory signs, information signs'}},
    "SAFETY_PURPLE": {'description': 'Safety purple - radiation hazards', 'meaning': 'HEX:652D90', 'annotations': {'standard': 'ANSI Z535.1', 'pantone': 'PMS 2685 C', 'usage': 'radiation hazards, x-ray equipment'}},
    "SAFETY_BLACK": {'description': 'Safety black - traffic/housekeeping markings', 'meaning': 'HEX:000000', 'annotations': {'standard': 'ANSI Z535.1', 'usage': 'traffic control, housekeeping markers'}},
    "SAFETY_WHITE": {'description': 'Safety white - traffic/housekeeping markings', 'meaning': 'HEX:FFFFFF', 'annotations': {'standard': 'ANSI Z535.1', 'usage': 'traffic lanes, housekeeping boundaries'}},
    "SAFETY_GRAY": {'description': 'Safety gray - inactive/out of service', 'meaning': 'HEX:919191', 'annotations': {'standard': 'ANSI Z535.1', 'usage': 'out of service equipment'}},
    "SAFETY_BROWN": {'description': 'Safety brown - no special hazard (background)', 'meaning': 'HEX:795548', 'annotations': {'usage': 'background color for signs'}},
}

class TrafficLightColorEnum(RichEnum):
    """
    Traffic signal colors (international)
    """
    # Enum members
    RED = "RED"
    AMBER = "AMBER"
    GREEN = "GREEN"
    FLASHING_RED = "FLASHING_RED"
    FLASHING_AMBER = "FLASHING_AMBER"
    WHITE = "WHITE"

# Set metadata after class creation
TrafficLightColorEnum._metadata = {
    "RED": {'description': 'Red - stop', 'meaning': 'HEX:FF0000', 'annotations': {'wavelength': '630-700 nm', 'meaning_universal': 'stop, do not proceed'}},
    "AMBER": {'description': 'Amber/yellow - caution', 'meaning': 'HEX:FFBF00', 'annotations': {'wavelength': '590 nm', 'meaning_universal': 'prepare to stop, caution'}},
    "GREEN": {'description': 'Green - go', 'meaning': 'HEX:00FF00', 'annotations': {'wavelength': '510-570 nm', 'meaning_universal': 'proceed, safe to go'}},
    "FLASHING_RED": {'description': 'Flashing red - stop then proceed', 'meaning': 'HEX:FF0000', 'annotations': {'pattern': 'flashing', 'meaning_universal': 'stop, then proceed when safe'}},
    "FLASHING_AMBER": {'description': 'Flashing amber - proceed with caution', 'meaning': 'HEX:FFBF00', 'annotations': {'pattern': 'flashing', 'meaning_universal': 'proceed with caution'}},
    "WHITE": {'description': 'White - special situations (transit)', 'meaning': 'HEX:FFFFFF', 'annotations': {'usage': 'transit priority signals'}},
}

class HazmatColorEnum(RichEnum):
    """
    Hazardous materials placarding colors (DOT/UN)
    """
    # Enum members
    ORANGE = "ORANGE"
    RED = "RED"
    GREEN = "GREEN"
    YELLOW = "YELLOW"
    WHITE = "WHITE"
    BLACK_WHITE_STRIPES = "BLACK_WHITE_STRIPES"
    BLUE = "BLUE"
    WHITE_RED_STRIPES = "WHITE_RED_STRIPES"

# Set metadata after class creation
HazmatColorEnum._metadata = {
    "ORANGE": {'description': 'Orange - explosives (Class 1)', 'meaning': 'HEX:FF6600', 'annotations': {'class': '1', 'hazard': 'explosives'}},
    "RED": {'description': 'Red - flammable (Classes 2.1, 3)', 'meaning': 'HEX:FF0000', 'annotations': {'class': '2.1, 3', 'hazard': 'flammable gas, flammable liquid'}},
    "GREEN": {'description': 'Green - non-flammable gas (Class 2.2)', 'meaning': 'HEX:00FF00', 'annotations': {'class': '2.2', 'hazard': 'non-flammable gas'}},
    "YELLOW": {'description': 'Yellow - oxidizer, organic peroxide (Classes 5.1, 5.2)', 'meaning': 'HEX:FFFF00', 'annotations': {'class': '5.1, 5.2', 'hazard': 'oxidizing substances, organic peroxides'}},
    "WHITE": {'description': 'White - poison/toxic (Class 6.1)', 'meaning': 'HEX:FFFFFF', 'annotations': {'class': '6.1', 'hazard': 'toxic/poisonous substances'}},
    "BLACK_WHITE_STRIPES": {'description': 'Black and white stripes - corrosive (Class 8)', 'annotations': {'class': '8', 'hazard': 'corrosive substances', 'pattern': 'black and white vertical stripes'}},
    "BLUE": {'description': 'Blue - dangerous when wet (Class 4.3)', 'meaning': 'HEX:0000FF', 'annotations': {'class': '4.3', 'hazard': 'dangerous when wet'}},
    "WHITE_RED_STRIPES": {'description': 'White with red stripes - flammable solid (Class 4.1)', 'annotations': {'class': '4.1', 'hazard': 'flammable solid', 'pattern': 'white with red vertical stripes'}},
}

class FireSafetyColorEnum(RichEnum):
    """
    Fire safety equipment and signage colors
    """
    # Enum members
    FIRE_RED = "FIRE_RED"
    PHOTOLUMINESCENT_GREEN = "PHOTOLUMINESCENT_GREEN"
    YELLOW_BLACK_STRIPES = "YELLOW_BLACK_STRIPES"
    WHITE = "WHITE"
    BLUE = "BLUE"

# Set metadata after class creation
FireSafetyColorEnum._metadata = {
    "FIRE_RED": {'description': 'Fire red - fire equipment', 'meaning': 'HEX:C8102E', 'annotations': {'usage': 'fire extinguishers, alarms, hose reels', 'standard': 'ISO 7010'}},
    "PHOTOLUMINESCENT_GREEN": {'description': 'Photoluminescent green - emergency escape', 'meaning': 'HEX:7FFF00', 'annotations': {'usage': 'emergency exit signs, escape routes', 'property': 'glows in dark'}},
    "YELLOW_BLACK_STRIPES": {'description': 'Yellow with black stripes - fire hazard area', 'annotations': {'pattern': 'diagonal stripes', 'usage': 'fire hazard zones'}},
    "WHITE": {'description': 'White - fire protection water', 'meaning': 'HEX:FFFFFF', 'annotations': {'usage': 'water for fire protection'}},
    "BLUE": {'description': 'Blue - mandatory fire safety', 'meaning': 'HEX:005EB8', 'annotations': {'usage': 'mandatory fire safety equipment'}},
}

class MaritimeSignalColorEnum(RichEnum):
    """
    Maritime signal and navigation colors
    """
    # Enum members
    PORT_RED = "PORT_RED"
    STARBOARD_GREEN = "STARBOARD_GREEN"
    STERN_WHITE = "STERN_WHITE"
    MASTHEAD_WHITE = "MASTHEAD_WHITE"
    ALL_ROUND_WHITE = "ALL_ROUND_WHITE"
    YELLOW_TOWING = "YELLOW_TOWING"
    BLUE_FLASHING = "BLUE_FLASHING"

# Set metadata after class creation
MaritimeSignalColorEnum._metadata = {
    "PORT_RED": {'description': 'Port (left) red light', 'meaning': 'HEX:FF0000', 'annotations': {'side': 'port (left)', 'wavelength': '625-740 nm'}},
    "STARBOARD_GREEN": {'description': 'Starboard (right) green light', 'meaning': 'HEX:00FF00', 'annotations': {'side': 'starboard (right)', 'wavelength': '500-565 nm'}},
    "STERN_WHITE": {'description': 'Stern white light', 'meaning': 'HEX:FFFFFF', 'annotations': {'position': 'stern (rear)'}},
    "MASTHEAD_WHITE": {'description': 'Masthead white light', 'meaning': 'HEX:FFFFFF', 'annotations': {'position': 'masthead (forward)'}},
    "ALL_ROUND_WHITE": {'description': 'All-round white light', 'meaning': 'HEX:FFFFFF', 'annotations': {'visibility': '360 degrees'}},
    "YELLOW_TOWING": {'description': 'Yellow towing light', 'meaning': 'HEX:FFFF00', 'annotations': {'usage': 'vessel towing'}},
    "BLUE_FLASHING": {'description': 'Blue flashing light', 'meaning': 'HEX:0000FF', 'annotations': {'usage': 'law enforcement vessels', 'pattern': 'flashing'}},
}

class AviationLightColorEnum(RichEnum):
    """
    Aviation lighting colors
    """
    # Enum members
    RED_BEACON = "RED_BEACON"
    WHITE_STROBE = "WHITE_STROBE"
    GREEN_NAVIGATION = "GREEN_NAVIGATION"
    RED_NAVIGATION = "RED_NAVIGATION"
    WHITE_NAVIGATION = "WHITE_NAVIGATION"
    BLUE_TAXIWAY = "BLUE_TAXIWAY"
    YELLOW_RUNWAY = "YELLOW_RUNWAY"
    GREEN_THRESHOLD = "GREEN_THRESHOLD"
    RED_RUNWAY_END = "RED_RUNWAY_END"

# Set metadata after class creation
AviationLightColorEnum._metadata = {
    "RED_BEACON": {'description': 'Red obstruction light', 'meaning': 'HEX:FF0000', 'annotations': {'usage': 'obstruction marking', 'intensity': 'high intensity'}},
    "WHITE_STROBE": {'description': 'White anti-collision strobe', 'meaning': 'HEX:FFFFFF', 'annotations': {'usage': 'anti-collision', 'pattern': 'strobe'}},
    "GREEN_NAVIGATION": {'description': 'Green navigation light (right wing)', 'meaning': 'HEX:00FF00', 'annotations': {'position': 'right wing tip'}},
    "RED_NAVIGATION": {'description': 'Red navigation light (left wing)', 'meaning': 'HEX:FF0000', 'annotations': {'position': 'left wing tip'}},
    "WHITE_NAVIGATION": {'description': 'White navigation light (tail)', 'meaning': 'HEX:FFFFFF', 'annotations': {'position': 'tail'}},
    "BLUE_TAXIWAY": {'description': 'Blue taxiway edge lights', 'meaning': 'HEX:0000FF', 'annotations': {'usage': 'taxiway edges'}},
    "YELLOW_RUNWAY": {'description': 'Yellow runway markings', 'meaning': 'HEX:FFFF00', 'annotations': {'usage': 'runway centerline, hold positions'}},
    "GREEN_THRESHOLD": {'description': 'Green runway threshold lights', 'meaning': 'HEX:00FF00', 'annotations': {'usage': 'runway threshold'}},
    "RED_RUNWAY_END": {'description': 'Red runway end lights', 'meaning': 'HEX:FF0000', 'annotations': {'usage': 'runway end'}},
}

class ElectricalWireColorEnum(RichEnum):
    """
    Electrical wire color codes (US/International)
    """
    # Enum members
    BLACK_HOT = "BLACK_HOT"
    RED_HOT = "RED_HOT"
    BLUE_HOT = "BLUE_HOT"
    WHITE_NEUTRAL = "WHITE_NEUTRAL"
    GREEN_GROUND = "GREEN_GROUND"
    GREEN_YELLOW_GROUND = "GREEN_YELLOW_GROUND"
    BROWN_LIVE = "BROWN_LIVE"
    BLUE_NEUTRAL = "BLUE_NEUTRAL"
    GRAY_NEUTRAL = "GRAY_NEUTRAL"

# Set metadata after class creation
ElectricalWireColorEnum._metadata = {
    "BLACK_HOT": {'description': 'Black - hot/live wire (US)', 'meaning': 'HEX:000000', 'annotations': {'voltage': '120/240V', 'region': 'North America'}},
    "RED_HOT": {'description': 'Red - hot/live wire (US secondary)', 'meaning': 'HEX:FF0000', 'annotations': {'voltage': '120/240V', 'region': 'North America'}},
    "BLUE_HOT": {'description': 'Blue - hot/live wire (US tertiary)', 'meaning': 'HEX:0000FF', 'annotations': {'voltage': '120/240V', 'region': 'North America'}},
    "WHITE_NEUTRAL": {'description': 'White - neutral wire (US)', 'meaning': 'HEX:FFFFFF', 'annotations': {'function': 'neutral', 'region': 'North America'}},
    "GREEN_GROUND": {'description': 'Green - ground/earth wire', 'meaning': 'HEX:00FF00', 'annotations': {'function': 'ground/earth', 'region': 'universal'}},
    "GREEN_YELLOW_GROUND": {'description': 'Green with yellow stripe - ground/earth (International)', 'annotations': {'function': 'ground/earth', 'region': 'IEC standard', 'pattern': 'green with yellow stripe'}},
    "BROWN_LIVE": {'description': 'Brown - live wire (EU/IEC)', 'meaning': 'HEX:964B00', 'annotations': {'voltage': '230V', 'region': 'Europe/IEC'}},
    "BLUE_NEUTRAL": {'description': 'Blue - neutral wire (EU/IEC)', 'meaning': 'HEX:0000FF', 'annotations': {'function': 'neutral', 'region': 'Europe/IEC'}},
    "GRAY_NEUTRAL": {'description': 'Gray - neutral wire (alternative)', 'meaning': 'HEX:808080', 'annotations': {'function': 'neutral', 'region': 'some installations'}},
}

class BloodTypeEnum(RichEnum):
    """
    ABO and Rh blood group classifications
    """
    # Enum members
    A_POSITIVE = "A_POSITIVE"
    A_NEGATIVE = "A_NEGATIVE"
    B_POSITIVE = "B_POSITIVE"
    B_NEGATIVE = "B_NEGATIVE"
    AB_POSITIVE = "AB_POSITIVE"
    AB_NEGATIVE = "AB_NEGATIVE"
    O_POSITIVE = "O_POSITIVE"
    O_NEGATIVE = "O_NEGATIVE"

# Set metadata after class creation
BloodTypeEnum._metadata = {
    "A_POSITIVE": {'description': 'Blood type A, Rh positive', 'meaning': 'SNOMED:278149003', 'annotations': {'abo': 'A', 'rh': 'positive', 'can_receive': 'A+, A-, O+, O-', 'can_donate': 'A+, AB+'}},
    "A_NEGATIVE": {'description': 'Blood type A, Rh negative', 'meaning': 'SNOMED:278152006', 'annotations': {'abo': 'A', 'rh': 'negative', 'can_receive': 'A-, O-', 'can_donate': 'A+, A-, AB+, AB-'}},
    "B_POSITIVE": {'description': 'Blood type B, Rh positive', 'meaning': 'SNOMED:278150003', 'annotations': {'abo': 'B', 'rh': 'positive', 'can_receive': 'B+, B-, O+, O-', 'can_donate': 'B+, AB+'}},
    "B_NEGATIVE": {'description': 'Blood type B, Rh negative', 'meaning': 'SNOMED:278153001', 'annotations': {'abo': 'B', 'rh': 'negative', 'can_receive': 'B-, O-', 'can_donate': 'B+, B-, AB+, AB-'}},
    "AB_POSITIVE": {'description': 'Blood type AB, Rh positive (universal recipient)', 'meaning': 'SNOMED:278151004', 'annotations': {'abo': 'AB', 'rh': 'positive', 'can_receive': 'all types', 'can_donate': 'AB+', 'special': 'universal recipient'}},
    "AB_NEGATIVE": {'description': 'Blood type AB, Rh negative', 'meaning': 'SNOMED:278154007', 'annotations': {'abo': 'AB', 'rh': 'negative', 'can_receive': 'A-, B-, AB-, O-', 'can_donate': 'AB+, AB-'}},
    "O_POSITIVE": {'description': 'Blood type O, Rh positive', 'meaning': 'SNOMED:278147001', 'annotations': {'abo': 'O', 'rh': 'positive', 'can_receive': 'O+, O-', 'can_donate': 'A+, B+, AB+, O+'}},
    "O_NEGATIVE": {'description': 'Blood type O, Rh negative (universal donor)', 'meaning': 'SNOMED:278148006', 'annotations': {'abo': 'O', 'rh': 'negative', 'can_receive': 'O-', 'can_donate': 'all types', 'special': 'universal donor'}},
}

class AnatomicalSystemEnum(RichEnum):
    """
    Major anatomical systems of the body
    """
    # Enum members
    CARDIOVASCULAR = "CARDIOVASCULAR"
    RESPIRATORY = "RESPIRATORY"
    NERVOUS = "NERVOUS"
    DIGESTIVE = "DIGESTIVE"
    MUSCULOSKELETAL = "MUSCULOSKELETAL"
    INTEGUMENTARY = "INTEGUMENTARY"
    ENDOCRINE = "ENDOCRINE"
    URINARY = "URINARY"
    REPRODUCTIVE = "REPRODUCTIVE"
    IMMUNE = "IMMUNE"
    HEMATOLOGIC = "HEMATOLOGIC"

# Set metadata after class creation
AnatomicalSystemEnum._metadata = {
    "CARDIOVASCULAR": {'meaning': 'UBERON:0004535', 'annotations': {'components': 'heart, arteries, veins, capillaries'}, 'aliases': ['cardiovascular system']},
    "RESPIRATORY": {'meaning': 'UBERON:0001004', 'annotations': {'components': 'lungs, trachea, bronchi, diaphragm'}, 'aliases': ['respiratory system']},
    "NERVOUS": {'meaning': 'UBERON:0001016', 'annotations': {'components': 'brain, spinal cord, nerves'}, 'aliases': ['nervous system']},
    "DIGESTIVE": {'meaning': 'UBERON:0001007', 'annotations': {'components': 'mouth, esophagus, stomach, intestines, liver, pancreas'}, 'aliases': ['digestive system']},
    "MUSCULOSKELETAL": {'meaning': 'UBERON:0002204', 'annotations': {'components': 'bones, muscles, tendons, ligaments, cartilage'}, 'aliases': ['musculoskeletal system']},
    "INTEGUMENTARY": {'meaning': 'UBERON:0002416', 'annotations': {'components': 'skin, hair, nails, glands'}, 'aliases': ['integumental system']},
    "ENDOCRINE": {'meaning': 'UBERON:0000949', 'annotations': {'components': 'pituitary, thyroid, adrenals, pancreas'}, 'aliases': ['endocrine system']},
    "URINARY": {'meaning': 'UBERON:0001008', 'annotations': {'components': 'kidneys, ureters, bladder, urethra'}, 'aliases': ['renal system']},
    "REPRODUCTIVE": {'meaning': 'UBERON:0000990', 'annotations': {'components': 'gonads, ducts, external genitalia'}, 'aliases': ['reproductive system']},
    "IMMUNE": {'meaning': 'UBERON:0002405', 'annotations': {'components': 'lymph nodes, spleen, thymus, bone marrow'}, 'aliases': ['immune system']},
    "HEMATOLOGIC": {'meaning': 'UBERON:0002390', 'annotations': {'components': 'blood, bone marrow, spleen'}, 'aliases': ['hematopoietic system']},
}

class MedicalSpecialtyEnum(RichEnum):
    # Enum members
    ANESTHESIOLOGY = "ANESTHESIOLOGY"
    CARDIOLOGY = "CARDIOLOGY"
    DERMATOLOGY = "DERMATOLOGY"
    EMERGENCY_MEDICINE = "EMERGENCY_MEDICINE"
    ENDOCRINOLOGY = "ENDOCRINOLOGY"
    FAMILY_MEDICINE = "FAMILY_MEDICINE"
    GASTROENTEROLOGY = "GASTROENTEROLOGY"
    HEMATOLOGY = "HEMATOLOGY"
    INFECTIOUS_DISEASE = "INFECTIOUS_DISEASE"
    INTERNAL_MEDICINE = "INTERNAL_MEDICINE"
    NEPHROLOGY = "NEPHROLOGY"
    NEUROLOGY = "NEUROLOGY"
    OBSTETRICS_GYNECOLOGY = "OBSTETRICS_GYNECOLOGY"
    ONCOLOGY = "ONCOLOGY"
    OPHTHALMOLOGY = "OPHTHALMOLOGY"
    ORTHOPEDICS = "ORTHOPEDICS"
    OTOLARYNGOLOGY = "OTOLARYNGOLOGY"
    PATHOLOGY = "PATHOLOGY"
    PEDIATRICS = "PEDIATRICS"
    PSYCHIATRY = "PSYCHIATRY"
    PULMONOLOGY = "PULMONOLOGY"
    RADIOLOGY = "RADIOLOGY"
    RHEUMATOLOGY = "RHEUMATOLOGY"
    SURGERY = "SURGERY"
    UROLOGY = "UROLOGY"

# Set metadata after class creation
MedicalSpecialtyEnum._metadata = {
}

class DrugRouteEnum(RichEnum):
    # Enum members
    ORAL = "ORAL"
    INTRAVENOUS = "INTRAVENOUS"
    INTRAMUSCULAR = "INTRAMUSCULAR"
    SUBCUTANEOUS = "SUBCUTANEOUS"
    TOPICAL = "TOPICAL"
    INHALATION = "INHALATION"
    RECTAL = "RECTAL"
    INTRANASAL = "INTRANASAL"
    TRANSDERMAL = "TRANSDERMAL"
    SUBLINGUAL = "SUBLINGUAL"
    EPIDURAL = "EPIDURAL"
    INTRATHECAL = "INTRATHECAL"
    OPHTHALMIC = "OPHTHALMIC"
    OTIC = "OTIC"

# Set metadata after class creation
DrugRouteEnum._metadata = {
    "ORAL": {'meaning': 'NCIT:C38288', 'annotations': {'abbreviation': 'PO', 'absorption': 'GI tract'}, 'aliases': ['Oral Route of Administration']},
    "INTRAVENOUS": {'meaning': 'NCIT:C38276', 'annotations': {'abbreviation': 'IV', 'onset': 'immediate'}, 'aliases': ['Intravenous Route of Administration']},
    "INTRAMUSCULAR": {'meaning': 'NCIT:C28161', 'annotations': {'abbreviation': 'IM', 'sites': 'deltoid, gluteus, vastus lateralis'}, 'aliases': ['Intramuscular Route of Administration']},
    "SUBCUTANEOUS": {'meaning': 'NCIT:C38299', 'annotations': {'abbreviation': 'SC, SubQ', 'absorption': 'slow'}, 'aliases': ['Subcutaneous Route of Administration']},
    "TOPICAL": {'meaning': 'NCIT:C38304', 'annotations': {'forms': 'cream, ointment, gel'}, 'aliases': ['Topical Route of Administration']},
    "INHALATION": {'meaning': 'NCIT:C38216', 'annotations': {'devices': 'inhaler, nebulizer'}, 'aliases': ['Inhalation Route of Administration']},
    "RECTAL": {'meaning': 'NCIT:C38295', 'annotations': {'forms': 'suppository, enema'}, 'aliases': ['Rectal Route of Administration']},
    "INTRANASAL": {'meaning': 'NCIT:C38284', 'annotations': {'forms': 'spray, drops'}, 'aliases': ['Nasal Route of Administration']},
    "TRANSDERMAL": {'meaning': 'NCIT:C38305', 'annotations': {'forms': 'patch'}, 'aliases': ['Transdermal Route of Administration']},
    "SUBLINGUAL": {'meaning': 'NCIT:C38300', 'annotations': {'absorption': 'rapid'}, 'aliases': ['Sublingual Route of Administration']},
    "EPIDURAL": {'meaning': 'NCIT:C38243', 'annotations': {'use': 'anesthesia, analgesia'}, 'aliases': ['Intraepidermal Route of Administration']},
    "INTRATHECAL": {'meaning': 'NCIT:C38277', 'annotations': {'use': 'CNS drugs'}, 'aliases': ['Intraventricular Route of Administration']},
    "OPHTHALMIC": {'meaning': 'NCIT:C38287', 'annotations': {'forms': 'drops, ointment'}, 'aliases': ['Ophthalmic Route of Administration']},
    "OTIC": {'meaning': 'NCIT:C38192', 'annotations': {'forms': 'drops'}, 'aliases': ['Auricular Route of Administration']},
}

class VitalSignEnum(RichEnum):
    # Enum members
    HEART_RATE = "HEART_RATE"
    BLOOD_PRESSURE_SYSTOLIC = "BLOOD_PRESSURE_SYSTOLIC"
    BLOOD_PRESSURE_DIASTOLIC = "BLOOD_PRESSURE_DIASTOLIC"
    RESPIRATORY_RATE = "RESPIRATORY_RATE"
    TEMPERATURE = "TEMPERATURE"
    OXYGEN_SATURATION = "OXYGEN_SATURATION"
    PAIN_SCALE = "PAIN_SCALE"

# Set metadata after class creation
VitalSignEnum._metadata = {
    "HEART_RATE": {'meaning': 'LOINC:8867-4', 'annotations': {'normal_range': '60-100 bpm', 'units': 'beats/min'}},
    "BLOOD_PRESSURE_SYSTOLIC": {'meaning': 'LOINC:8480-6', 'annotations': {'normal_range': '<120 mmHg', 'units': 'mmHg'}},
    "BLOOD_PRESSURE_DIASTOLIC": {'meaning': 'LOINC:8462-4', 'annotations': {'normal_range': '<80 mmHg', 'units': 'mmHg'}},
    "RESPIRATORY_RATE": {'meaning': 'LOINC:9279-1', 'annotations': {'normal_range': '12-20 breaths/min', 'units': 'breaths/min'}},
    "TEMPERATURE": {'meaning': 'LOINC:8310-5', 'annotations': {'normal_range': '36.5-37.5°C', 'units': '°C or °F'}},
    "OXYGEN_SATURATION": {'meaning': 'LOINC:2708-6', 'annotations': {'normal_range': '95-100%', 'units': '%'}},
    "PAIN_SCALE": {'meaning': 'LOINC:38208-5', 'annotations': {'scale': '0-10', 'type': 'subjective'}},
}

class DiagnosticTestTypeEnum(RichEnum):
    # Enum members
    BLOOD_TEST = "BLOOD_TEST"
    URINE_TEST = "URINE_TEST"
    IMAGING_XRAY = "IMAGING_XRAY"
    IMAGING_CT = "IMAGING_CT"
    IMAGING_MRI = "IMAGING_MRI"
    IMAGING_ULTRASOUND = "IMAGING_ULTRASOUND"
    IMAGING_PET = "IMAGING_PET"
    ECG = "ECG"
    EEG = "EEG"
    BIOPSY = "BIOPSY"
    ENDOSCOPY = "ENDOSCOPY"
    GENETIC_TEST = "GENETIC_TEST"

# Set metadata after class creation
DiagnosticTestTypeEnum._metadata = {
    "BLOOD_TEST": {'meaning': 'NCIT:C15189', 'annotations': {'samples': 'serum, plasma, whole blood'}, 'aliases': ['Biopsy Procedure']},
    "URINE_TEST": {'annotations': {'types': 'urinalysis, culture, drug screen'}, 'aliases': ['Tissue Factor']},
    "IMAGING_XRAY": {'meaning': 'NCIT:C17262', 'annotations': {'radiation': 'yes'}, 'aliases': ['X-Ray']},
    "IMAGING_CT": {'meaning': 'NCIT:C17204', 'annotations': {'radiation': 'yes'}, 'aliases': ['Computed Tomography']},
    "IMAGING_MRI": {'meaning': 'NCIT:C16809', 'annotations': {'radiation': 'no'}, 'aliases': ['Magnetic Resonance Imaging']},
    "IMAGING_ULTRASOUND": {'meaning': 'NCIT:C17230', 'annotations': {'radiation': 'no'}, 'aliases': ['Ultrasound Imaging']},
    "IMAGING_PET": {'meaning': 'NCIT:C17007', 'annotations': {'uses': 'radiotracer'}, 'aliases': ['Positron Emission Tomography']},
    "ECG": {'meaning': 'NCIT:C38054', 'annotations': {'measures': 'heart electrical activity'}, 'aliases': ['Electroencephalography']},
    "EEG": {'annotations': {'measures': 'brain electrical activity'}, 'aliases': ['Djibouti']},
    "BIOPSY": {'meaning': 'NCIT:C15189', 'annotations': {'invasive': 'yes'}, 'aliases': ['Biopsy Procedure']},
    "ENDOSCOPY": {'meaning': 'NCIT:C16546', 'annotations': {'types': 'colonoscopy, gastroscopy, bronchoscopy'}, 'aliases': ['Endoscopic Procedure']},
    "GENETIC_TEST": {'meaning': 'NCIT:C15709', 'annotations': {'types': 'karyotype, sequencing, PCR'}, 'aliases': ['Genetic Testing']},
}

class SymptomSeverityEnum(RichEnum):
    # Enum members
    ABSENT = "ABSENT"
    MILD = "MILD"
    MODERATE = "MODERATE"
    SEVERE = "SEVERE"
    LIFE_THREATENING = "LIFE_THREATENING"

# Set metadata after class creation
SymptomSeverityEnum._metadata = {
    "ABSENT": {'annotations': {'grade': '0'}, 'aliases': ['Blood group B']},
    "MILD": {'meaning': 'HP:0012825', 'annotations': {'grade': '1', 'impact': 'minimal daily activity limitation'}},
    "MODERATE": {'meaning': 'HP:0012826', 'annotations': {'grade': '2', 'impact': 'some daily activity limitation'}},
    "SEVERE": {'meaning': 'HP:0012828', 'annotations': {'grade': '3', 'impact': 'significant daily activity limitation'}},
    "LIFE_THREATENING": {'annotations': {'grade': '4', 'impact': 'urgent intervention required'}, 'aliases': ['Profound']},
}

class AllergyTypeEnum(RichEnum):
    # Enum members
    DRUG = "DRUG"
    FOOD = "FOOD"
    ENVIRONMENTAL = "ENVIRONMENTAL"
    CONTACT = "CONTACT"
    INSECT = "INSECT"
    ANAPHYLAXIS = "ANAPHYLAXIS"

# Set metadata after class creation
AllergyTypeEnum._metadata = {
    "DRUG": {'meaning': 'NCIT:C3114', 'annotations': {'examples': 'penicillin, sulfa drugs'}, 'aliases': ['Hypersensitivity']},
    "FOOD": {'annotations': {'common': 'nuts, shellfish, eggs, milk'}},
    "ENVIRONMENTAL": {'annotations': {'examples': 'pollen, dust, mold'}},
    "CONTACT": {'annotations': {'examples': 'latex, nickel, poison ivy'}},
    "INSECT": {'annotations': {'examples': 'bee, wasp, hornet'}},
    "ANAPHYLAXIS": {'annotations': {'severity': 'life-threatening'}},
}

class VaccineTypeEnum(RichEnum):
    # Enum members
    LIVE_ATTENUATED = "LIVE_ATTENUATED"
    INACTIVATED = "INACTIVATED"
    SUBUNIT = "SUBUNIT"
    TOXOID = "TOXOID"
    MRNA = "MRNA"
    VIRAL_VECTOR = "VIRAL_VECTOR"

# Set metadata after class creation
VaccineTypeEnum._metadata = {
    "LIVE_ATTENUATED": {'annotations': {'examples': 'MMR, varicella, yellow fever'}},
    "INACTIVATED": {'annotations': {'examples': 'flu shot, hepatitis A, rabies'}},
    "SUBUNIT": {'annotations': {'examples': 'hepatitis B, HPV, pertussis'}},
    "TOXOID": {'annotations': {'examples': 'diphtheria, tetanus'}},
    "MRNA": {'annotations': {'examples': 'COVID-19 (Pfizer, Moderna)'}},
    "VIRAL_VECTOR": {'annotations': {'examples': 'COVID-19 (J&J, AstraZeneca)'}},
}

class BMIClassificationEnum(RichEnum):
    # Enum members
    UNDERWEIGHT = "UNDERWEIGHT"
    NORMAL_WEIGHT = "NORMAL_WEIGHT"
    OVERWEIGHT = "OVERWEIGHT"
    OBESE_CLASS_I = "OBESE_CLASS_I"
    OBESE_CLASS_II = "OBESE_CLASS_II"
    OBESE_CLASS_III = "OBESE_CLASS_III"

# Set metadata after class creation
BMIClassificationEnum._metadata = {
    "UNDERWEIGHT": {'annotations': {'bmi_range': '<18.5'}},
    "NORMAL_WEIGHT": {'annotations': {'bmi_range': '18.5-24.9'}},
    "OVERWEIGHT": {'annotations': {'bmi_range': '25.0-29.9'}},
    "OBESE_CLASS_I": {'annotations': {'bmi_range': '30.0-34.9'}},
    "OBESE_CLASS_II": {'annotations': {'bmi_range': '35.0-39.9'}},
    "OBESE_CLASS_III": {'annotations': {'bmi_range': '≥40.0', 'aliases': 'morbid obesity'}},
}

class RaceOMB1997Enum(RichEnum):
    """
    Race categories following OMB 1997 standards used by NIH and federal agencies.
    Respondents may select multiple races.
    """
    # Enum members
    AMERICAN_INDIAN_OR_ALASKA_NATIVE = "AMERICAN_INDIAN_OR_ALASKA_NATIVE"
    ASIAN = "ASIAN"
    BLACK_OR_AFRICAN_AMERICAN = "BLACK_OR_AFRICAN_AMERICAN"
    NATIVE_HAWAIIAN_OR_OTHER_PACIFIC_ISLANDER = "NATIVE_HAWAIIAN_OR_OTHER_PACIFIC_ISLANDER"
    WHITE = "WHITE"
    MORE_THAN_ONE_RACE = "MORE_THAN_ONE_RACE"
    UNKNOWN_OR_NOT_REPORTED = "UNKNOWN_OR_NOT_REPORTED"

# Set metadata after class creation
RaceOMB1997Enum._metadata = {
    "AMERICAN_INDIAN_OR_ALASKA_NATIVE": {'description': 'A person having origins in any of the original peoples of North and South America (including Central America), and who maintains tribal affiliation or community attachment', 'meaning': 'NCIT:C41259', 'annotations': {'omb_code': '1002-5'}},
    "ASIAN": {'description': 'A person having origins in any of the original peoples of the Far East, Southeast Asia, or the Indian subcontinent', 'meaning': 'NCIT:C41260', 'annotations': {'omb_code': '2028-9', 'includes': 'Cambodia, China, India, Japan, Korea, Malaysia, Pakistan, Philippine Islands, Thailand, Vietnam'}},
    "BLACK_OR_AFRICAN_AMERICAN": {'description': 'A person having origins in any of the black racial groups of Africa', 'meaning': 'NCIT:C16352', 'annotations': {'omb_code': '2054-5'}},
    "NATIVE_HAWAIIAN_OR_OTHER_PACIFIC_ISLANDER": {'description': 'A person having origins in any of the original peoples of Hawaii, Guam, Samoa, or other Pacific Islands', 'meaning': 'NCIT:C41219', 'annotations': {'omb_code': '2076-8'}},
    "WHITE": {'description': 'A person having origins in any of the original peoples of Europe, the Middle East, or North Africa', 'meaning': 'NCIT:C41261', 'annotations': {'omb_code': '2106-3'}},
    "MORE_THAN_ONE_RACE": {'description': 'Person identifies with more than one race category', 'meaning': 'NCIT:C67109', 'annotations': {'note': 'Added after 1997 revision to allow multiple race reporting'}},
    "UNKNOWN_OR_NOT_REPORTED": {'description': 'Race not known, not reported, or declined to answer', 'meaning': 'NCIT:C17998', 'annotations': {'aliases': 'Unknown, Not Reported, Prefer not to answer'}},
}

class EthnicityOMB1997Enum(RichEnum):
    """
    Ethnicity categories following OMB 1997 standards used by NIH and federal agencies
    """
    # Enum members
    HISPANIC_OR_LATINO = "HISPANIC_OR_LATINO"
    NOT_HISPANIC_OR_LATINO = "NOT_HISPANIC_OR_LATINO"
    UNKNOWN_OR_NOT_REPORTED = "UNKNOWN_OR_NOT_REPORTED"

# Set metadata after class creation
EthnicityOMB1997Enum._metadata = {
    "HISPANIC_OR_LATINO": {'description': 'A person of Cuban, Mexican, Puerto Rican, South or Central American, or other Spanish culture or origin, regardless of race', 'meaning': 'NCIT:C17459', 'annotations': {'omb_code': '2135-2'}},
    "NOT_HISPANIC_OR_LATINO": {'description': 'A person not of Hispanic or Latino origin', 'meaning': 'NCIT:C41222', 'annotations': {'omb_code': '2186-5'}},
    "UNKNOWN_OR_NOT_REPORTED": {'description': 'Ethnicity not known, not reported, or declined to answer', 'meaning': 'NCIT:C17998', 'annotations': {'aliases': 'Unknown, Not Reported, Prefer not to answer'}},
}

class BiologicalSexEnum(RichEnum):
    """
    Biological sex assigned at birth based on anatomical and physiological traits.
    Required by NIH as a biological variable in research.
    """
    # Enum members
    MALE = "MALE"
    FEMALE = "FEMALE"
    INTERSEX = "INTERSEX"
    UNKNOWN_OR_NOT_REPORTED = "UNKNOWN_OR_NOT_REPORTED"

# Set metadata after class creation
BiologicalSexEnum._metadata = {
    "MALE": {'description': 'Male sex assigned at birth', 'meaning': 'PATO:0000384'},
    "FEMALE": {'description': 'Female sex assigned at birth', 'meaning': 'PATO:0000383'},
    "INTERSEX": {'description': "Born with reproductive or sexual anatomy that doesn't fit typical definitions of male or female", 'meaning': 'NCIT:C45908', 'annotations': {'prevalence': '0.018% to 1.7%', 'note': 'May be assigned male or female at birth'}},
    "UNKNOWN_OR_NOT_REPORTED": {'description': 'Sex not known, not reported, or declined to answer', 'meaning': 'NCIT:C17998'},
}

class GenderIdentityEnum(RichEnum):
    """
    Current gender identity, which may differ from sex assigned at birth
    """
    # Enum members
    MAN = "MAN"
    WOMAN = "WOMAN"
    TRANSGENDER_MAN = "TRANSGENDER_MAN"
    TRANSGENDER_WOMAN = "TRANSGENDER_WOMAN"
    NON_BINARY = "NON_BINARY"
    OTHER = "OTHER"
    PREFER_NOT_TO_ANSWER = "PREFER_NOT_TO_ANSWER"

# Set metadata after class creation
GenderIdentityEnum._metadata = {
    "MAN": {'description': 'Identifies as man', 'meaning': 'GSSO:009292', 'annotations': {'aliases': 'Male'}},
    "WOMAN": {'description': 'Identifies as woman', 'meaning': 'GSSO:009293', 'annotations': {'aliases': 'Female'}},
    "TRANSGENDER_MAN": {'description': 'Identifies as transgender man/trans man/female-to-male', 'meaning': 'GSSO:000372', 'annotations': {'definition': 'Assigned female at birth but identifies as man'}},
    "TRANSGENDER_WOMAN": {'description': 'Identifies as transgender woman/trans woman/male-to-female', 'meaning': 'GSSO:000384', 'annotations': {'definition': 'Assigned male at birth but identifies as woman'}},
    "NON_BINARY": {'description': 'Gender identity outside the man/woman binary', 'meaning': 'GSSO:002403', 'annotations': {'aliases': 'Genderqueer, Gender non-conforming'}},
    "OTHER": {'description': 'Other gender identity', 'annotations': {'note': 'Free text may be collected'}},
    "PREFER_NOT_TO_ANSWER": {'description': 'Prefers not to disclose gender identity', 'meaning': 'NCIT:C132222'},
}

class AgeGroupEnum(RichEnum):
    """
    Standard age groups used in NIH clinical research, particularly NINDS CDEs
    """
    # Enum members
    NEONATE = "NEONATE"
    INFANT = "INFANT"
    YOUNG_PEDIATRIC = "YOUNG_PEDIATRIC"
    PEDIATRIC = "PEDIATRIC"
    ADOLESCENT = "ADOLESCENT"
    YOUNG_ADULT = "YOUNG_ADULT"
    ADULT = "ADULT"
    OLDER_ADULT = "OLDER_ADULT"

# Set metadata after class creation
AgeGroupEnum._metadata = {
    "NEONATE": {'description': 'Birth to 28 days', 'meaning': 'NCIT:C16731', 'annotations': {'max_age_days': 28}},
    "INFANT": {'description': '29 days to less than 1 year', 'meaning': 'NCIT:C27956', 'annotations': {'min_age_days': 29, 'max_age_years': 1}},
    "YOUNG_PEDIATRIC": {'description': '0 to 5 years (NINDS CDE definition)', 'meaning': 'NCIT:C39299', 'annotations': {'min_age_years': 0, 'max_age_years': 5, 'ninds_category': True}},
    "PEDIATRIC": {'description': '6 to 12 years (NINDS CDE definition)', 'meaning': 'NCIT:C16423', 'annotations': {'min_age_years': 6, 'max_age_years': 12, 'ninds_category': True}},
    "ADOLESCENT": {'description': '13 to 17 years', 'meaning': 'NCIT:C27954', 'annotations': {'min_age_years': 13, 'max_age_years': 17}},
    "YOUNG_ADULT": {'description': '18 to 24 years', 'meaning': 'NCIT:C91107', 'annotations': {'min_age_years': 18, 'max_age_years': 24}},
    "ADULT": {'description': '25 to 64 years', 'meaning': 'NCIT:C17600', 'annotations': {'min_age_years': 25, 'max_age_years': 64}},
    "OLDER_ADULT": {'description': '65 years and older', 'meaning': 'NCIT:C16268', 'annotations': {'min_age_years': 65, 'aliases': 'Geriatric, Elderly, Senior'}},
}

class ParticipantVitalStatusEnum(RichEnum):
    """
    Vital status of a research participant in clinical studies
    """
    # Enum members
    ALIVE = "ALIVE"
    DECEASED = "DECEASED"
    UNKNOWN = "UNKNOWN"

# Set metadata after class creation
ParticipantVitalStatusEnum._metadata = {
    "ALIVE": {'description': 'Participant is living', 'meaning': 'NCIT:C37987'},
    "DECEASED": {'description': 'Participant is deceased', 'meaning': 'NCIT:C28554'},
    "UNKNOWN": {'description': 'Vital status unknown or lost to follow-up', 'meaning': 'NCIT:C17998'},
}

class RecruitmentStatusEnum(RichEnum):
    """
    Clinical trial or study recruitment status per NIH/ClinicalTrials.gov
    """
    # Enum members
    NOT_YET_RECRUITING = "NOT_YET_RECRUITING"
    RECRUITING = "RECRUITING"
    ENROLLING_BY_INVITATION = "ENROLLING_BY_INVITATION"
    ACTIVE_NOT_RECRUITING = "ACTIVE_NOT_RECRUITING"
    SUSPENDED = "SUSPENDED"
    TERMINATED = "TERMINATED"
    COMPLETED = "COMPLETED"
    WITHDRAWN = "WITHDRAWN"

# Set metadata after class creation
RecruitmentStatusEnum._metadata = {
    "NOT_YET_RECRUITING": {'description': 'Study has not started recruiting participants', 'meaning': 'NCIT:C211610'},
    "RECRUITING": {'description': 'Currently recruiting participants', 'meaning': 'NCIT:C142621'},
    "ENROLLING_BY_INVITATION": {'description': 'Enrolling participants by invitation only', 'meaning': 'NCIT:C211611'},
    "ACTIVE_NOT_RECRUITING": {'description': 'Study ongoing but not recruiting new participants', 'meaning': 'NCIT:C211612'},
    "SUSPENDED": {'description': 'Study temporarily stopped', 'meaning': 'NCIT:C211613'},
    "TERMINATED": {'description': 'Study stopped early and will not resume', 'meaning': 'NCIT:C70757'},
    "COMPLETED": {'description': 'Study has ended normally', 'meaning': 'NCIT:C70756'},
    "WITHDRAWN": {'description': 'Study withdrawn before enrollment', 'meaning': 'NCIT:C70758'},
}

class StudyPhaseEnum(RichEnum):
    """
    Clinical trial phases per FDA and NIH definitions
    """
    # Enum members
    EARLY_PHASE_1 = "EARLY_PHASE_1"
    PHASE_1 = "PHASE_1"
    PHASE_1_2 = "PHASE_1_2"
    PHASE_2 = "PHASE_2"
    PHASE_2_3 = "PHASE_2_3"
    PHASE_3 = "PHASE_3"
    PHASE_4 = "PHASE_4"
    NOT_APPLICABLE = "NOT_APPLICABLE"

# Set metadata after class creation
StudyPhaseEnum._metadata = {
    "EARLY_PHASE_1": {'description': 'Exploratory trials before traditional Phase 1', 'meaning': 'NCIT:C54721', 'annotations': {'aliases': 'Phase 0'}},
    "PHASE_1": {'description': 'Initial safety and dosage studies', 'meaning': 'NCIT:C15600', 'annotations': {'participants': '20-100'}},
    "PHASE_1_2": {'description': 'Combined Phase 1 and Phase 2 trial', 'meaning': 'NCIT:C15694'},
    "PHASE_2": {'description': 'Efficacy and side effects studies', 'meaning': 'NCIT:C15601', 'annotations': {'participants': '100-300'}},
    "PHASE_2_3": {'description': 'Combined Phase 2 and Phase 3 trial', 'meaning': 'NCIT:C49686'},
    "PHASE_3": {'description': 'Efficacy comparison with standard treatment', 'meaning': 'NCIT:C15602', 'annotations': {'participants': '300-3000'}},
    "PHASE_4": {'description': 'Post-marketing surveillance', 'meaning': 'NCIT:C15603', 'annotations': {'note': 'After FDA approval'}},
    "NOT_APPLICABLE": {'description': 'Not a phased clinical trial', 'meaning': 'NCIT:C48660', 'annotations': {'note': 'For observational studies, device trials, etc.'}},
}

class EducationLevelEnum(RichEnum):
    """
    Highest level of education completed, following NIH demographics standards
    """
    # Enum members
    NO_FORMAL_EDUCATION = "NO_FORMAL_EDUCATION"
    ELEMENTARY = "ELEMENTARY"
    MIDDLE_SCHOOL = "MIDDLE_SCHOOL"
    SOME_HIGH_SCHOOL = "SOME_HIGH_SCHOOL"
    HIGH_SCHOOL_GRADUATE = "HIGH_SCHOOL_GRADUATE"
    SOME_COLLEGE = "SOME_COLLEGE"
    ASSOCIATE_DEGREE = "ASSOCIATE_DEGREE"
    BACHELORS_DEGREE = "BACHELORS_DEGREE"
    MASTERS_DEGREE = "MASTERS_DEGREE"
    PROFESSIONAL_DEGREE = "PROFESSIONAL_DEGREE"
    DOCTORATE_DEGREE = "DOCTORATE_DEGREE"
    UNKNOWN_OR_NOT_REPORTED = "UNKNOWN_OR_NOT_REPORTED"

# Set metadata after class creation
EducationLevelEnum._metadata = {
    "NO_FORMAL_EDUCATION": {'description': 'No formal schooling completed', 'meaning': 'NCIT:C173723'},
    "ELEMENTARY": {'description': 'Elementary school (grades 1-6)', 'meaning': 'NCIT:C80410', 'annotations': {'grades': '1-6'}},
    "MIDDLE_SCHOOL": {'description': 'Middle/Junior high school (grades 7-8)', 'meaning': 'NCIT:C205685', 'annotations': {'grades': '7-8'}},
    "SOME_HIGH_SCHOOL": {'description': 'Some high school, no diploma', 'meaning': 'NCIT:C198650', 'annotations': {'grades': '9-11'}},
    "HIGH_SCHOOL_GRADUATE": {'description': 'High school graduate or GED', 'meaning': 'NCIT:C67136', 'annotations': {'includes': 'GED, High school diploma'}},
    "SOME_COLLEGE": {'description': 'Some college credit, no degree', 'meaning': 'NCIT:C67137'},
    "ASSOCIATE_DEGREE": {'description': 'Associate degree (2-year)', 'meaning': 'NCIT:C71340', 'annotations': {'duration': '2 years'}},
    "BACHELORS_DEGREE": {'description': "Bachelor's degree (4-year)", 'meaning': 'NCIT:C39327', 'annotations': {'duration': '4 years'}},
    "MASTERS_DEGREE": {'description': "Master's degree", 'meaning': 'NCIT:C39453'},
    "PROFESSIONAL_DEGREE": {'description': 'Professional degree (MD, JD, etc.)', 'meaning': 'NCIT:C67143', 'annotations': {'examples': 'MD, JD, DDS, DVM'}},
    "DOCTORATE_DEGREE": {'description': 'Doctorate degree (PhD, EdD, etc.)', 'meaning': 'NCIT:C39392', 'annotations': {'examples': 'PhD, EdD, DrPH'}},
    "UNKNOWN_OR_NOT_REPORTED": {'description': 'Education level not known or not reported', 'meaning': 'NCIT:C17998'},
}

class KaryotypicSexEnum(RichEnum):
    """
    Karyotypic sex of an individual based on chromosome composition
    """
    # Enum members
    XX = "XX"
    XY = "XY"
    XO = "XO"
    XXY = "XXY"
    XXX = "XXX"
    XXXY = "XXXY"
    XXXX = "XXXX"
    XXYY = "XXYY"
    XYY = "XYY"
    OTHER_KARYOTYPE = "OTHER_KARYOTYPE"
    UNKNOWN_KARYOTYPE = "UNKNOWN_KARYOTYPE"

# Set metadata after class creation
KaryotypicSexEnum._metadata = {
    "XX": {'description': 'Female karyotype (46,XX)', 'meaning': 'NCIT:C45976', 'annotations': {'chromosome_count': 46, 'typical_phenotypic_sex': 'female'}},
    "XY": {'description': 'Male karyotype (46,XY)', 'meaning': 'NCIT:C45977', 'annotations': {'chromosome_count': 46, 'typical_phenotypic_sex': 'male'}},
    "XO": {'description': 'Turner syndrome karyotype (45,X)', 'meaning': 'NCIT:C176780', 'annotations': {'chromosome_count': 45, 'condition': 'Turner syndrome'}},
    "XXY": {'description': 'Klinefelter syndrome karyotype (47,XXY)', 'meaning': 'NCIT:C176784', 'annotations': {'chromosome_count': 47, 'condition': 'Klinefelter syndrome'}},
    "XXX": {'description': 'Triple X syndrome karyotype (47,XXX)', 'meaning': 'NCIT:C176785', 'annotations': {'chromosome_count': 47, 'condition': 'Triple X syndrome'}},
    "XXXY": {'description': 'XXXY syndrome karyotype (48,XXXY)', 'meaning': 'NCIT:C176786', 'annotations': {'chromosome_count': 48, 'condition': 'XXXY syndrome'}},
    "XXXX": {'description': 'Tetrasomy X karyotype (48,XXXX)', 'meaning': 'NCIT:C176787', 'annotations': {'chromosome_count': 48, 'condition': 'Tetrasomy X'}},
    "XXYY": {'description': 'XXYY syndrome karyotype (48,XXYY)', 'meaning': 'NCIT:C89801', 'annotations': {'chromosome_count': 48, 'condition': 'XXYY syndrome'}},
    "XYY": {'description': "Jacob's syndrome karyotype (47,XYY)", 'meaning': 'NCIT:C176782', 'annotations': {'chromosome_count': 47, 'condition': "Jacob's syndrome"}},
    "OTHER_KARYOTYPE": {'description': 'Other karyotypic sex not listed', 'annotations': {'note': 'May include complex chromosomal arrangements'}},
    "UNKNOWN_KARYOTYPE": {'description': 'Karyotype not determined or unknown', 'meaning': 'NCIT:C17998'},
}

class PhenotypicSexEnum(RichEnum):
    """
    Phenotypic sex of an individual based on observable characteristics.
    FHIR mapping: AdministrativeGender
    """
    # Enum members
    MALE = "MALE"
    FEMALE = "FEMALE"
    OTHER_SEX = "OTHER_SEX"
    UNKNOWN_SEX = "UNKNOWN_SEX"

# Set metadata after class creation
PhenotypicSexEnum._metadata = {
    "MALE": {'description': 'Male phenotypic sex', 'meaning': 'PATO:0000384'},
    "FEMALE": {'description': 'Female phenotypic sex', 'meaning': 'PATO:0000383'},
    "OTHER_SEX": {'description': 'Sex characteristics not clearly male or female', 'meaning': 'NCIT:C45908', 'annotations': {'note': 'Includes differences of sex development (DSD)'}},
    "UNKNOWN_SEX": {'description': 'Sex not assessed or not available', 'meaning': 'NCIT:C17998'},
}

class AllelicStateEnum(RichEnum):
    """
    Allelic state/zygosity of a variant or genetic feature
    """
    # Enum members
    HETEROZYGOUS = "HETEROZYGOUS"
    HOMOZYGOUS = "HOMOZYGOUS"
    HEMIZYGOUS = "HEMIZYGOUS"
    COMPOUND_HETEROZYGOUS = "COMPOUND_HETEROZYGOUS"
    HOMOZYGOUS_REFERENCE = "HOMOZYGOUS_REFERENCE"
    HOMOZYGOUS_ALTERNATE = "HOMOZYGOUS_ALTERNATE"

# Set metadata after class creation
AllelicStateEnum._metadata = {
    "HETEROZYGOUS": {'description': 'Different alleles at a locus', 'meaning': 'GENO:0000135', 'annotations': {'symbol': 'het'}},
    "HOMOZYGOUS": {'description': 'Identical alleles at a locus', 'meaning': 'GENO:0000136', 'annotations': {'symbol': 'hom'}},
    "HEMIZYGOUS": {'description': 'Only one allele present (e.g., X-linked in males)', 'meaning': 'GENO:0000134', 'annotations': {'symbol': 'hemi', 'note': 'Common for X-linked genes in males'}},
    "COMPOUND_HETEROZYGOUS": {'description': 'Two different heterozygous variants in same gene', 'meaning': 'GENO:0000402', 'annotations': {'symbol': 'comp het'}},
    "HOMOZYGOUS_REFERENCE": {'description': 'Two reference/wild-type alleles', 'meaning': 'GENO:0000036', 'annotations': {'symbol': 'hom ref'}},
    "HOMOZYGOUS_ALTERNATE": {'description': 'Two alternate/variant alleles', 'meaning': 'GENO:0000002', 'annotations': {'symbol': 'hom alt'}},
}

class LateralityEnum(RichEnum):
    """
    Laterality/sidedness of a finding or anatomical structure
    """
    # Enum members
    RIGHT = "RIGHT"
    LEFT = "LEFT"
    BILATERAL = "BILATERAL"
    UNILATERAL = "UNILATERAL"
    MIDLINE = "MIDLINE"

# Set metadata after class creation
LateralityEnum._metadata = {
    "RIGHT": {'description': 'Right side', 'meaning': 'HP:0012834', 'annotations': {'anatomical_term': 'dexter'}},
    "LEFT": {'description': 'Left side', 'meaning': 'HP:0012835', 'annotations': {'anatomical_term': 'sinister'}},
    "BILATERAL": {'description': 'Both sides', 'meaning': 'HP:0012832', 'annotations': {'note': 'Affecting both left and right'}},
    "UNILATERAL": {'description': 'One side (unspecified which)', 'meaning': 'HP:0012833', 'annotations': {'note': 'Affecting only one side'}},
    "MIDLINE": {'description': 'In the midline/center', 'meaning': 'UBERON:0005231', 'annotations': {'note': "Along the body's central axis"}},
}

class OnsetTimingEnum(RichEnum):
    """
    Timing of disease or phenotype onset relative to developmental stages
    """
    # Enum members
    ANTENATAL_ONSET = "ANTENATAL_ONSET"
    EMBRYONAL_ONSET = "EMBRYONAL_ONSET"
    FETAL_ONSET = "FETAL_ONSET"
    CONGENITAL_ONSET = "CONGENITAL_ONSET"
    NEONATAL_ONSET = "NEONATAL_ONSET"
    INFANTILE_ONSET = "INFANTILE_ONSET"
    CHILDHOOD_ONSET = "CHILDHOOD_ONSET"
    JUVENILE_ONSET = "JUVENILE_ONSET"
    YOUNG_ADULT_ONSET = "YOUNG_ADULT_ONSET"
    MIDDLE_AGE_ONSET = "MIDDLE_AGE_ONSET"
    LATE_ONSET = "LATE_ONSET"

# Set metadata after class creation
OnsetTimingEnum._metadata = {
    "ANTENATAL_ONSET": {'description': 'Before birth (prenatal)', 'meaning': 'HP:0030674', 'annotations': {'period': 'Before birth'}},
    "EMBRYONAL_ONSET": {'description': 'During embryonic period (0-8 weeks)', 'meaning': 'HP:0011460', 'annotations': {'period': '0-8 weeks gestation'}},
    "FETAL_ONSET": {'description': 'During fetal period (8 weeks to birth)', 'meaning': 'HP:0011461', 'annotations': {'period': '8 weeks to birth'}},
    "CONGENITAL_ONSET": {'description': 'Present at birth', 'meaning': 'HP:0003577', 'annotations': {'period': 'At birth'}},
    "NEONATAL_ONSET": {'description': 'Within first 28 days of life', 'meaning': 'HP:0003623', 'annotations': {'period': '0-28 days'}},
    "INFANTILE_ONSET": {'description': 'Between 28 days and 1 year', 'meaning': 'HP:0003593', 'annotations': {'period': '28 days to 1 year'}},
    "CHILDHOOD_ONSET": {'description': 'Between 1 year and 16 years', 'meaning': 'HP:0011463', 'annotations': {'period': '1-16 years'}},
    "JUVENILE_ONSET": {'description': 'Between 5 years and 16 years', 'meaning': 'HP:0003621', 'annotations': {'period': '5-16 years'}},
    "YOUNG_ADULT_ONSET": {'description': 'Between 16 years and 40 years', 'meaning': 'HP:0011462', 'annotations': {'period': '16-40 years'}},
    "MIDDLE_AGE_ONSET": {'description': 'Between 40 years and 60 years', 'meaning': 'HP:0003596', 'annotations': {'period': '40-60 years'}},
    "LATE_ONSET": {'description': 'After 60 years', 'meaning': 'HP:0003584', 'annotations': {'period': '>60 years'}},
}

class ACMGPathogenicityEnum(RichEnum):
    """
    ACMG/AMP variant pathogenicity classification for clinical genetics
    """
    # Enum members
    PATHOGENIC = "PATHOGENIC"
    LIKELY_PATHOGENIC = "LIKELY_PATHOGENIC"
    UNCERTAIN_SIGNIFICANCE = "UNCERTAIN_SIGNIFICANCE"
    LIKELY_BENIGN = "LIKELY_BENIGN"
    BENIGN = "BENIGN"

# Set metadata after class creation
ACMGPathogenicityEnum._metadata = {
    "PATHOGENIC": {'description': 'Pathogenic variant', 'meaning': 'NCIT:C168799', 'annotations': {'abbreviation': 'P', 'clinical_significance': 'Disease-causing'}},
    "LIKELY_PATHOGENIC": {'description': 'Likely pathogenic variant', 'meaning': 'NCIT:C168800', 'annotations': {'abbreviation': 'LP', 'probability': '>90% certain'}},
    "UNCERTAIN_SIGNIFICANCE": {'description': 'Variant of uncertain significance', 'meaning': 'NCIT:C94187', 'annotations': {'abbreviation': 'VUS', 'note': 'Insufficient evidence'}},
    "LIKELY_BENIGN": {'description': 'Likely benign variant', 'meaning': 'NCIT:C168801', 'annotations': {'abbreviation': 'LB', 'probability': '>90% certain benign'}},
    "BENIGN": {'description': 'Benign variant', 'meaning': 'NCIT:C168802', 'annotations': {'abbreviation': 'B', 'clinical_significance': 'Not disease-causing'}},
}

class TherapeuticActionabilityEnum(RichEnum):
    """
    Clinical actionability of a genetic finding for treatment decisions
    """
    # Enum members
    ACTIONABLE = "ACTIONABLE"
    NOT_ACTIONABLE = "NOT_ACTIONABLE"
    UNKNOWN_ACTIONABILITY = "UNKNOWN_ACTIONABILITY"

# Set metadata after class creation
TherapeuticActionabilityEnum._metadata = {
    "ACTIONABLE": {'description': 'Finding has direct therapeutic implications', 'meaning': 'NCIT:C206303', 'annotations': {'note': 'Can guide treatment selection'}},
    "NOT_ACTIONABLE": {'description': 'No current therapeutic implications', 'meaning': 'NCIT:C206304', 'annotations': {'note': 'No treatment changes indicated'}},
    "UNKNOWN_ACTIONABILITY": {'description': 'Therapeutic implications unclear', 'meaning': 'NCIT:C17998'},
}

class InterpretationProgressEnum(RichEnum):
    """
    Progress status of clinical interpretation or diagnosis
    """
    # Enum members
    SOLVED = "SOLVED"
    UNSOLVED = "UNSOLVED"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    UNKNOWN_PROGRESS = "UNKNOWN_PROGRESS"

# Set metadata after class creation
InterpretationProgressEnum._metadata = {
    "SOLVED": {'description': 'Diagnosis achieved/case solved', 'meaning': 'NCIT:C20826', 'annotations': {'note': 'Molecular cause identified'}},
    "UNSOLVED": {'description': 'No diagnosis achieved', 'meaning': 'NCIT:C125009', 'annotations': {'note': 'Molecular cause not identified'}},
    "IN_PROGRESS": {'description': 'Analysis ongoing', 'meaning': 'NCIT:C25630'},
    "COMPLETED": {'description': 'Analysis completed', 'meaning': 'NCIT:C216251', 'annotations': {'note': 'May be solved or unsolved'}},
    "UNKNOWN_PROGRESS": {'description': 'Progress status unknown', 'meaning': 'NCIT:C17998'},
}

class RegimenStatusEnum(RichEnum):
    """
    Status of a therapeutic regimen or treatment protocol
    """
    # Enum members
    NOT_STARTED = "NOT_STARTED"
    STARTED = "STARTED"
    COMPLETED = "COMPLETED"
    DISCONTINUED_ADVERSE_EVENT = "DISCONTINUED_ADVERSE_EVENT"
    DISCONTINUED_LACK_OF_EFFICACY = "DISCONTINUED_LACK_OF_EFFICACY"
    DISCONTINUED_PHYSICIAN_DECISION = "DISCONTINUED_PHYSICIAN_DECISION"
    DISCONTINUED_PATIENT_DECISION = "DISCONTINUED_PATIENT_DECISION"
    UNKNOWN_STATUS = "UNKNOWN_STATUS"

# Set metadata after class creation
RegimenStatusEnum._metadata = {
    "NOT_STARTED": {'description': 'Treatment not yet begun', 'meaning': 'NCIT:C53601'},
    "STARTED": {'description': 'Treatment initiated', 'meaning': 'NCIT:C165209'},
    "COMPLETED": {'description': 'Treatment finished as planned', 'meaning': 'NCIT:C105740'},
    "DISCONTINUED_ADVERSE_EVENT": {'description': 'Stopped due to adverse event', 'meaning': 'NCIT:C41331', 'annotations': {'reason': 'Toxicity or side effects'}},
    "DISCONTINUED_LACK_OF_EFFICACY": {'description': 'Stopped due to lack of efficacy', 'meaning': 'NCIT:C49502', 'annotations': {'reason': 'Treatment not effective'}},
    "DISCONTINUED_PHYSICIAN_DECISION": {'description': 'Stopped by physician decision', 'meaning': 'NCIT:C49502'},
    "DISCONTINUED_PATIENT_DECISION": {'description': 'Stopped by patient choice', 'meaning': 'NCIT:C48271'},
    "UNKNOWN_STATUS": {'description': 'Treatment status unknown', 'meaning': 'NCIT:C17998'},
}

class DrugResponseEnum(RichEnum):
    """
    Response categories for drug treatment outcomes
    """
    # Enum members
    FAVORABLE = "FAVORABLE"
    UNFAVORABLE = "UNFAVORABLE"
    RESPONSIVE = "RESPONSIVE"
    RESISTANT = "RESISTANT"
    PARTIALLY_RESPONSIVE = "PARTIALLY_RESPONSIVE"
    UNKNOWN_RESPONSE = "UNKNOWN_RESPONSE"

# Set metadata after class creation
DrugResponseEnum._metadata = {
    "FAVORABLE": {'description': 'Favorable response to treatment', 'meaning': 'NCIT:C123584', 'annotations': {'note': 'Better than expected response'}},
    "UNFAVORABLE": {'description': 'Unfavorable response to treatment', 'meaning': 'NCIT:C102561', 'annotations': {'note': 'Worse than expected response'}},
    "RESPONSIVE": {'description': 'Responsive to treatment', 'meaning': 'NCIT:C165206', 'annotations': {'note': 'Shows expected response'}},
    "RESISTANT": {'description': 'Resistant to treatment', 'meaning': 'NCIT:C16523', 'annotations': {'note': 'No response to treatment'}},
    "PARTIALLY_RESPONSIVE": {'description': 'Partial response to treatment', 'meaning': 'NCIT:C18213', 'annotations': {'note': 'Some but not complete response'}},
    "UNKNOWN_RESPONSE": {'description': 'Treatment response unknown', 'meaning': 'NCIT:C17998'},
}

class ProcessScaleEnum(RichEnum):
    """
    Scale of bioprocessing operations from lab bench to commercial production
    """
    # Enum members
    BENCH_SCALE = "BENCH_SCALE"
    PILOT_SCALE = "PILOT_SCALE"
    DEMONSTRATION_SCALE = "DEMONSTRATION_SCALE"
    PRODUCTION_SCALE = "PRODUCTION_SCALE"
    MICROFLUIDIC_SCALE = "MICROFLUIDIC_SCALE"

# Set metadata after class creation
ProcessScaleEnum._metadata = {
    "BENCH_SCALE": {'description': 'Laboratory bench scale (typically < 10 L)', 'annotations': {'volume_range': '0.1-10 L', 'typical_volume': '1-5 L', 'purpose': 'Initial development and screening'}},
    "PILOT_SCALE": {'description': 'Pilot plant scale (10-1000 L)', 'annotations': {'volume_range': '10-1000 L', 'typical_volume': '50-500 L', 'purpose': 'Process development and optimization'}},
    "DEMONSTRATION_SCALE": {'description': 'Demonstration scale (1000-10000 L)', 'annotations': {'volume_range': '1000-10000 L', 'typical_volume': '2000-5000 L', 'purpose': 'Technology demonstration and validation'}},
    "PRODUCTION_SCALE": {'description': 'Commercial production scale (>10000 L)', 'annotations': {'volume_range': '>10000 L', 'typical_volume': '20000-200000 L', 'purpose': 'Commercial manufacturing'}},
    "MICROFLUIDIC_SCALE": {'description': 'Microfluidic scale (<1 mL)', 'annotations': {'volume_range': '<1 mL', 'typical_volume': '1-1000 μL', 'purpose': 'High-throughput screening'}},
}

class BioreactorTypeEnum(RichEnum):
    """
    Types of bioreactors used in fermentation and cell culture
    """
    # Enum members
    STIRRED_TANK = "STIRRED_TANK"
    AIRLIFT = "AIRLIFT"
    BUBBLE_COLUMN = "BUBBLE_COLUMN"
    PACKED_BED = "PACKED_BED"
    FLUIDIZED_BED = "FLUIDIZED_BED"
    MEMBRANE = "MEMBRANE"
    WAVE_BAG = "WAVE_BAG"
    HOLLOW_FIBER = "HOLLOW_FIBER"
    PHOTOBIOREACTOR = "PHOTOBIOREACTOR"

# Set metadata after class creation
BioreactorTypeEnum._metadata = {
    "STIRRED_TANK": {'description': 'Stirred tank reactor (STR/CSTR)', 'annotations': {'mixing': 'Mechanical agitation', 'common_volumes': '1-200000 L'}},
    "AIRLIFT": {'description': 'Airlift bioreactor', 'annotations': {'mixing': 'Gas sparging', 'advantages': 'Low shear, no mechanical parts'}},
    "BUBBLE_COLUMN": {'description': 'Bubble column bioreactor', 'annotations': {'mixing': 'Gas bubbling', 'advantages': 'Simple design, good mass transfer'}},
    "PACKED_BED": {'description': 'Packed bed bioreactor', 'annotations': {'configuration': 'Fixed bed of immobilized cells/enzymes', 'flow': 'Continuous'}},
    "FLUIDIZED_BED": {'description': 'Fluidized bed bioreactor', 'annotations': {'configuration': 'Suspended solid particles', 'mixing': 'Fluid flow'}},
    "MEMBRANE": {'description': 'Membrane bioreactor', 'meaning': 'ENVO:03600010', 'annotations': {'feature': 'Integrated membrane separation', 'application': 'Cell retention, product separation'}},
    "WAVE_BAG": {'description': 'Wave/rocking bioreactor', 'annotations': {'mixing': 'Rocking motion', 'advantages': 'Single-use, low shear'}},
    "HOLLOW_FIBER": {'description': 'Hollow fiber bioreactor', 'annotations': {'configuration': 'Hollow fiber membranes', 'application': 'High-density cell culture'}},
    "PHOTOBIOREACTOR": {'description': 'Photobioreactor for photosynthetic organisms', 'annotations': {'light_source': 'Required', 'organisms': 'Algae, cyanobacteria'}},
}

class FermentationModeEnum(RichEnum):
    """
    Modes of fermentation operation
    """
    # Enum members
    BATCH = "BATCH"
    FED_BATCH = "FED_BATCH"
    CONTINUOUS = "CONTINUOUS"
    PERFUSION = "PERFUSION"
    REPEATED_BATCH = "REPEATED_BATCH"
    SEMI_CONTINUOUS = "SEMI_CONTINUOUS"

# Set metadata after class creation
FermentationModeEnum._metadata = {
    "BATCH": {'description': 'Batch fermentation', 'meaning': 'MSIO:0000181', 'annotations': {'operation': 'All nutrients added at start', 'duration': 'Fixed time period'}},
    "FED_BATCH": {'description': 'Fed-batch fermentation', 'annotations': {'operation': 'Nutrients added during run', 'advantage': 'Control of growth rate'}},
    "CONTINUOUS": {'description': 'Continuous fermentation (chemostat)', 'meaning': 'MSIO:0000155', 'annotations': {'operation': 'Continuous feed and harvest', 'steady_state': True}},
    "PERFUSION": {'description': 'Perfusion culture', 'annotations': {'operation': 'Continuous media exchange with cell retention', 'application': 'High-density cell culture'}},
    "REPEATED_BATCH": {'description': 'Repeated batch fermentation', 'annotations': {'operation': 'Sequential batches with partial harvest', 'advantage': 'Reduced downtime'}},
    "SEMI_CONTINUOUS": {'description': 'Semi-continuous operation', 'annotations': {'operation': 'Periodic harvest and refill', 'advantage': 'Extended production'}},
}

class OxygenationStrategyEnum(RichEnum):
    """
    Oxygen supply strategies for fermentation
    """
    # Enum members
    AEROBIC = "AEROBIC"
    ANAEROBIC = "ANAEROBIC"
    MICROAEROBIC = "MICROAEROBIC"
    FACULTATIVE = "FACULTATIVE"

# Set metadata after class creation
OxygenationStrategyEnum._metadata = {
    "AEROBIC": {'description': 'Aerobic with active aeration', 'annotations': {'oxygen': 'Required', 'typical_DO': '20-80% saturation'}},
    "ANAEROBIC": {'description': 'Anaerobic (no oxygen)', 'annotations': {'oxygen': 'Excluded', 'atmosphere': 'N2 or CO2'}},
    "MICROAEROBIC": {'description': 'Microaerobic (limited oxygen)', 'annotations': {'oxygen': 'Limited', 'typical_DO': '<5% saturation'}},
    "FACULTATIVE": {'description': 'Facultative (with/without oxygen)', 'annotations': {'oxygen': 'Optional', 'flexibility': 'Organism-dependent'}},
}

class AgitationTypeEnum(RichEnum):
    """
    Types of agitation/mixing in bioreactors
    """
    # Enum members
    RUSHTON_TURBINE = "RUSHTON_TURBINE"
    PITCHED_BLADE = "PITCHED_BLADE"
    MARINE_PROPELLER = "MARINE_PROPELLER"
    ANCHOR = "ANCHOR"
    HELICAL_RIBBON = "HELICAL_RIBBON"
    MAGNETIC_BAR = "MAGNETIC_BAR"
    ORBITAL_SHAKING = "ORBITAL_SHAKING"
    NO_AGITATION = "NO_AGITATION"

# Set metadata after class creation
AgitationTypeEnum._metadata = {
    "RUSHTON_TURBINE": {'description': 'Rushton turbine impeller', 'annotations': {'type': 'Radial flow', 'power_number': '5-6'}},
    "PITCHED_BLADE": {'description': 'Pitched blade turbine', 'annotations': {'type': 'Axial flow', 'angle': '45 degrees'}},
    "MARINE_PROPELLER": {'description': 'Marine propeller', 'annotations': {'type': 'Axial flow', 'low_shear': True}},
    "ANCHOR": {'description': 'Anchor impeller', 'annotations': {'type': 'Close clearance', 'viscous_fluids': True}},
    "HELICAL_RIBBON": {'description': 'Helical ribbon impeller', 'annotations': {'type': 'Close clearance', 'high_viscosity': True}},
    "MAGNETIC_BAR": {'description': 'Magnetic stir bar', 'annotations': {'scale': 'Laboratory', 'volume': '<5 L'}},
    "ORBITAL_SHAKING": {'description': 'Orbital shaking', 'annotations': {'type': 'Platform shaker', 'application': 'Shake flasks'}},
    "NO_AGITATION": {'description': 'No mechanical agitation', 'annotations': {'mixing': 'Gas sparging or static'}},
}

class DownstreamProcessEnum(RichEnum):
    """
    Downstream processing unit operations
    """
    # Enum members
    CENTRIFUGATION = "CENTRIFUGATION"
    FILTRATION = "FILTRATION"
    CHROMATOGRAPHY = "CHROMATOGRAPHY"
    EXTRACTION = "EXTRACTION"
    PRECIPITATION = "PRECIPITATION"
    EVAPORATION = "EVAPORATION"
    DISTILLATION = "DISTILLATION"
    DRYING = "DRYING"
    HOMOGENIZATION = "HOMOGENIZATION"

# Set metadata after class creation
DownstreamProcessEnum._metadata = {
    "CENTRIFUGATION": {'description': 'Centrifugal separation', 'meaning': 'CHMO:0002010', 'annotations': {'principle': 'Density difference', 'types': 'Disk stack, tubular, decanter'}},
    "FILTRATION": {'description': 'Filtration (micro/ultra/nano)', 'meaning': 'CHMO:0001640', 'annotations': {'types': 'Dead-end, crossflow, depth'}},
    "CHROMATOGRAPHY": {'description': 'Chromatographic separation', 'meaning': 'CHMO:0001000', 'annotations': {'types': 'Ion exchange, affinity, size exclusion'}},
    "EXTRACTION": {'description': 'Liquid-liquid extraction', 'meaning': 'CHMO:0001577', 'annotations': {'principle': 'Partitioning between phases'}},
    "PRECIPITATION": {'description': 'Precipitation/crystallization', 'meaning': 'CHMO:0001688', 'annotations': {'agents': 'Salts, solvents, pH'}},
    "EVAPORATION": {'description': 'Evaporation/concentration', 'meaning': 'CHMO:0001574', 'annotations': {'types': 'Falling film, MVR, TVR'}},
    "DISTILLATION": {'description': 'Distillation', 'meaning': 'CHMO:0001534', 'annotations': {'principle': 'Boiling point difference'}},
    "DRYING": {'description': 'Drying operations', 'meaning': 'CHMO:0001551', 'annotations': {'types': 'Spray, freeze, vacuum'}},
    "HOMOGENIZATION": {'description': 'Cell disruption/homogenization', 'annotations': {'methods': 'High pressure, bead mill'}},
}

class FeedstockTypeEnum(RichEnum):
    """
    Types of feedstocks for bioprocessing
    """
    # Enum members
    GLUCOSE = "GLUCOSE"
    SUCROSE = "SUCROSE"
    GLYCEROL = "GLYCEROL"
    MOLASSES = "MOLASSES"
    CORN_STEEP_LIQUOR = "CORN_STEEP_LIQUOR"
    YEAST_EXTRACT = "YEAST_EXTRACT"
    LIGNOCELLULOSIC = "LIGNOCELLULOSIC"
    METHANOL = "METHANOL"
    WASTE_STREAM = "WASTE_STREAM"

# Set metadata after class creation
FeedstockTypeEnum._metadata = {
    "GLUCOSE": {'description': 'Glucose/dextrose', 'meaning': 'CHEBI:17234', 'annotations': {'source': 'Corn, sugarcane', 'carbon_source': True}},
    "SUCROSE": {'description': 'Sucrose', 'meaning': 'CHEBI:17992', 'annotations': {'source': 'Sugarcane, sugar beet', 'carbon_source': True}},
    "GLYCEROL": {'description': 'Glycerol', 'meaning': 'CHEBI:17754', 'annotations': {'source': 'Biodiesel byproduct', 'carbon_source': True}},
    "MOLASSES": {'description': 'Molasses', 'meaning': 'CHEBI:83163', 'annotations': {'source': 'Sugar processing byproduct', 'complex_medium': True}},
    "CORN_STEEP_LIQUOR": {'description': 'Corn steep liquor', 'annotations': {'source': 'Corn wet milling', 'nitrogen_source': True}},
    "YEAST_EXTRACT": {'description': 'Yeast extract', 'meaning': 'FOODON:03315426', 'annotations': {'source': 'Autolyzed yeast', 'complex_nutrient': True}},
    "LIGNOCELLULOSIC": {'description': 'Lignocellulosic biomass', 'annotations': {'source': 'Agricultural residues, wood', 'pretreatment': 'Required'}},
    "METHANOL": {'description': 'Methanol', 'meaning': 'CHEBI:17790', 'annotations': {'carbon_source': True, 'methylotrophic': True}},
    "WASTE_STREAM": {'description': 'Industrial waste stream', 'annotations': {'variable_composition': True, 'sustainability': 'Circular economy'}},
}

class ProductTypeEnum(RichEnum):
    """
    Types of products from bioprocessing
    """
    # Enum members
    BIOFUEL = "BIOFUEL"
    PROTEIN = "PROTEIN"
    ENZYME = "ENZYME"
    ORGANIC_ACID = "ORGANIC_ACID"
    AMINO_ACID = "AMINO_ACID"
    ANTIBIOTIC = "ANTIBIOTIC"
    VITAMIN = "VITAMIN"
    BIOPOLYMER = "BIOPOLYMER"
    BIOMASS = "BIOMASS"
    SECONDARY_METABOLITE = "SECONDARY_METABOLITE"

# Set metadata after class creation
ProductTypeEnum._metadata = {
    "BIOFUEL": {'description': 'Biofuel (ethanol, biodiesel, etc.)', 'meaning': 'CHEBI:33292', 'annotations': {'category': 'Energy'}},
    "PROTEIN": {'description': 'Recombinant protein', 'meaning': 'NCIT:C17021', 'annotations': {'category': 'Biopharmaceutical'}},
    "ENZYME": {'description': 'Industrial enzyme', 'meaning': 'NCIT:C16554', 'annotations': {'category': 'Biocatalyst'}},
    "ORGANIC_ACID": {'description': 'Organic acid (citric, lactic, etc.)', 'meaning': 'CHEBI:64709', 'annotations': {'category': 'Chemical'}},
    "AMINO_ACID": {'description': 'Amino acid', 'meaning': 'CHEBI:33709', 'annotations': {'category': 'Nutritional'}},
    "ANTIBIOTIC": {'description': 'Antibiotic', 'meaning': 'CHEBI:33281', 'annotations': {'category': 'Pharmaceutical'}},
    "VITAMIN": {'description': 'Vitamin', 'meaning': 'CHEBI:33229', 'annotations': {'category': 'Nutritional'}},
    "BIOPOLYMER": {'description': 'Biopolymer (PHA, PLA, etc.)', 'meaning': 'CHEBI:33694', 'annotations': {'category': 'Material'}},
    "BIOMASS": {'description': 'Microbial biomass', 'meaning': 'ENVO:01000155', 'annotations': {'category': 'Feed/food'}},
    "SECONDARY_METABOLITE": {'description': 'Secondary metabolite', 'meaning': 'CHEBI:25212', 'annotations': {'category': 'Specialty chemical'}},
}

class SterilizationMethodEnum(RichEnum):
    """
    Methods for sterilization in bioprocessing
    """
    # Enum members
    STEAM_IN_PLACE = "STEAM_IN_PLACE"
    AUTOCLAVE = "AUTOCLAVE"
    FILTER_STERILIZATION = "FILTER_STERILIZATION"
    GAMMA_IRRADIATION = "GAMMA_IRRADIATION"
    ETHYLENE_OXIDE = "ETHYLENE_OXIDE"
    UV_STERILIZATION = "UV_STERILIZATION"
    CHEMICAL_STERILIZATION = "CHEMICAL_STERILIZATION"

# Set metadata after class creation
SterilizationMethodEnum._metadata = {
    "STEAM_IN_PLACE": {'description': 'Steam in place (SIP)', 'annotations': {'temperature': '121-134°C', 'time': '15-30 min'}},
    "AUTOCLAVE": {'description': 'Autoclave sterilization', 'meaning': 'CHMO:0002846', 'annotations': {'temperature': '121°C', 'pressure': '15 psi'}},
    "FILTER_STERILIZATION": {'description': 'Filter sterilization (0.2 μm)', 'annotations': {'pore_size': '0.2 μm', 'heat_labile': True}},
    "GAMMA_IRRADIATION": {'description': 'Gamma irradiation', 'annotations': {'dose': '25-40 kGy', 'single_use': True}},
    "ETHYLENE_OXIDE": {'description': 'Ethylene oxide sterilization', 'annotations': {'temperature': '30-60°C', 'plastic_compatible': True}},
    "UV_STERILIZATION": {'description': 'UV sterilization', 'annotations': {'wavelength': '254 nm', 'surface_only': True}},
    "CHEMICAL_STERILIZATION": {'description': 'Chemical sterilization', 'annotations': {'agents': 'Bleach, alcohol, peroxide', 'contact_time': 'Variable'}},
}

class LengthUnitEnum(RichEnum):
    """
    Units of length/distance measurement
    """
    # Enum members
    METER = "METER"
    KILOMETER = "KILOMETER"
    CENTIMETER = "CENTIMETER"
    MILLIMETER = "MILLIMETER"
    MICROMETER = "MICROMETER"
    NANOMETER = "NANOMETER"
    ANGSTROM = "ANGSTROM"
    INCH = "INCH"
    FOOT = "FOOT"
    YARD = "YARD"
    MILE = "MILE"
    NAUTICAL_MILE = "NAUTICAL_MILE"

# Set metadata after class creation
LengthUnitEnum._metadata = {
    "METER": {'description': 'Meter (SI base unit)', 'meaning': 'UO:0000008', 'annotations': {'symbol': 'm', 'system': 'SI'}},
    "KILOMETER": {'description': 'Kilometer (1000 meters)', 'meaning': 'UO:0010066', 'annotations': {'symbol': 'km', 'conversion_to_meter': '1000'}},
    "CENTIMETER": {'description': 'Centimeter (0.01 meter)', 'meaning': 'UO:0000015', 'annotations': {'symbol': 'cm', 'conversion_to_meter': '0.01'}},
    "MILLIMETER": {'description': 'Millimeter (0.001 meter)', 'meaning': 'UO:0000016', 'annotations': {'symbol': 'mm', 'conversion_to_meter': '0.001'}},
    "MICROMETER": {'description': 'Micrometer/micron (10^-6 meter)', 'meaning': 'UO:0000017', 'annotations': {'symbol': 'μm', 'conversion_to_meter': '1e-6'}},
    "NANOMETER": {'description': 'Nanometer (10^-9 meter)', 'meaning': 'UO:0000018', 'annotations': {'symbol': 'nm', 'conversion_to_meter': '1e-9'}},
    "ANGSTROM": {'description': 'Angstrom (10^-10 meter)', 'meaning': 'UO:0000019', 'annotations': {'symbol': 'Å', 'conversion_to_meter': '1e-10'}},
    "INCH": {'description': 'Inch (imperial)', 'meaning': 'UO:0010011', 'annotations': {'symbol': 'in', 'conversion_to_meter': '0.0254', 'system': 'imperial'}},
    "FOOT": {'description': 'Foot (imperial)', 'meaning': 'UO:0010013', 'annotations': {'symbol': 'ft', 'conversion_to_meter': '0.3048', 'system': 'imperial'}},
    "YARD": {'description': 'Yard (imperial)', 'meaning': 'UO:0010014', 'annotations': {'symbol': 'yd', 'conversion_to_meter': '0.9144', 'system': 'imperial'}},
    "MILE": {'description': 'Mile (imperial)', 'meaning': 'UO:0010017', 'annotations': {'symbol': 'mi', 'conversion_to_meter': '1609.344', 'system': 'imperial'}},
    "NAUTICAL_MILE": {'description': 'Nautical mile', 'meaning': 'UO:0010022', 'annotations': {'symbol': 'nmi', 'conversion_to_meter': '1852'}},
}

class MassUnitEnum(RichEnum):
    """
    Units of mass measurement
    """
    # Enum members
    KILOGRAM = "KILOGRAM"
    GRAM = "GRAM"
    MILLIGRAM = "MILLIGRAM"
    MICROGRAM = "MICROGRAM"
    NANOGRAM = "NANOGRAM"
    METRIC_TON = "METRIC_TON"
    POUND = "POUND"
    OUNCE = "OUNCE"
    STONE = "STONE"
    DALTON = "DALTON"

# Set metadata after class creation
MassUnitEnum._metadata = {
    "KILOGRAM": {'description': 'Kilogram (SI base unit)', 'meaning': 'UO:0000009', 'annotations': {'symbol': 'kg', 'system': 'SI'}},
    "GRAM": {'description': 'Gram (0.001 kilogram)', 'meaning': 'UO:0000021', 'annotations': {'symbol': 'g', 'conversion_to_kg': '0.001'}},
    "MILLIGRAM": {'description': 'Milligram (10^-6 kilogram)', 'meaning': 'UO:0000022', 'annotations': {'symbol': 'mg', 'conversion_to_kg': '1e-6'}},
    "MICROGRAM": {'description': 'Microgram (10^-9 kilogram)', 'meaning': 'UO:0000023', 'annotations': {'symbol': 'μg', 'conversion_to_kg': '1e-9'}},
    "NANOGRAM": {'description': 'Nanogram (10^-12 kilogram)', 'meaning': 'UO:0000024', 'annotations': {'symbol': 'ng', 'conversion_to_kg': '1e-12'}},
    "METRIC_TON": {'description': 'Metric ton/tonne (1000 kilograms)', 'meaning': 'UO:0010038', 'annotations': {'symbol': 't', 'conversion_to_kg': '1000'}, 'aliases': ['ton']},
    "POUND": {'description': 'Pound (imperial)', 'meaning': 'UO:0010034', 'annotations': {'symbol': 'lb', 'conversion_to_kg': '0.453592', 'system': 'imperial'}},
    "OUNCE": {'description': 'Ounce (imperial)', 'meaning': 'UO:0010033', 'annotations': {'symbol': 'oz', 'conversion_to_kg': '0.0283495', 'system': 'imperial'}},
    "STONE": {'description': 'Stone (imperial)', 'meaning': 'UO:0010035', 'annotations': {'symbol': 'st', 'conversion_to_kg': '6.35029', 'system': 'imperial'}},
    "DALTON": {'description': 'Dalton/atomic mass unit', 'meaning': 'UO:0000221', 'annotations': {'symbol': 'Da', 'conversion_to_kg': '1.66054e-27', 'use': 'molecular mass'}},
}

class VolumeUnitEnum(RichEnum):
    """
    Units of volume measurement
    """
    # Enum members
    LITER = "LITER"
    MILLILITER = "MILLILITER"
    MICROLITER = "MICROLITER"
    CUBIC_METER = "CUBIC_METER"
    CUBIC_CENTIMETER = "CUBIC_CENTIMETER"
    GALLON_US = "GALLON_US"
    GALLON_UK = "GALLON_UK"
    FLUID_OUNCE_US = "FLUID_OUNCE_US"
    PINT_US = "PINT_US"
    QUART_US = "QUART_US"
    CUP_US = "CUP_US"
    TABLESPOON = "TABLESPOON"
    TEASPOON = "TEASPOON"

# Set metadata after class creation
VolumeUnitEnum._metadata = {
    "LITER": {'description': 'Liter (SI derived)', 'meaning': 'UO:0000099', 'annotations': {'symbol': 'L', 'conversion_to_m3': '0.001'}},
    "MILLILITER": {'description': 'Milliliter (0.001 liter)', 'meaning': 'UO:0000098', 'annotations': {'symbol': 'mL', 'conversion_to_m3': '1e-6'}},
    "MICROLITER": {'description': 'Microliter (10^-6 liter)', 'meaning': 'UO:0000101', 'annotations': {'symbol': 'μL', 'conversion_to_m3': '1e-9'}},
    "CUBIC_METER": {'description': 'Cubic meter (SI derived)', 'meaning': 'UO:0000096', 'annotations': {'symbol': 'm³', 'system': 'SI'}},
    "CUBIC_CENTIMETER": {'description': 'Cubic centimeter', 'meaning': 'UO:0000097', 'annotations': {'symbol': 'cm³', 'conversion_to_m3': '1e-6'}},
    "GALLON_US": {'description': 'US gallon', 'annotations': {'symbol': 'gal', 'conversion_to_m3': '0.00378541', 'system': 'US'}},
    "GALLON_UK": {'description': 'UK/Imperial gallon', 'meaning': 'UO:0010030', 'annotations': {'symbol': 'gal', 'conversion_to_m3': '0.00454609', 'system': 'imperial'}, 'aliases': ['imperial gallon']},
    "FLUID_OUNCE_US": {'description': 'US fluid ounce', 'meaning': 'UO:0010026', 'annotations': {'symbol': 'fl oz', 'conversion_to_m3': '2.95735e-5', 'system': 'US'}, 'aliases': ['imperial fluid ounce']},
    "PINT_US": {'description': 'US pint', 'meaning': 'UO:0010028', 'annotations': {'symbol': 'pt', 'conversion_to_m3': '0.000473176', 'system': 'US'}, 'aliases': ['imperial pint']},
    "QUART_US": {'description': 'US quart', 'meaning': 'UO:0010029', 'annotations': {'symbol': 'qt', 'conversion_to_m3': '0.000946353', 'system': 'US'}, 'aliases': ['imperial quart']},
    "CUP_US": {'description': 'US cup', 'meaning': 'UO:0010046', 'annotations': {'symbol': 'cup', 'conversion_to_m3': '0.000236588', 'system': 'US'}},
    "TABLESPOON": {'description': 'Tablespoon', 'meaning': 'UO:0010044', 'annotations': {'symbol': 'tbsp', 'conversion_to_m3': '1.47868e-5'}},
    "TEASPOON": {'description': 'Teaspoon', 'meaning': 'UO:0010041', 'annotations': {'symbol': 'tsp', 'conversion_to_m3': '4.92892e-6'}},
}

class TemperatureUnitEnum(RichEnum):
    """
    Units of temperature measurement
    """
    # Enum members
    KELVIN = "KELVIN"
    CELSIUS = "CELSIUS"
    FAHRENHEIT = "FAHRENHEIT"
    RANKINE = "RANKINE"

# Set metadata after class creation
TemperatureUnitEnum._metadata = {
    "KELVIN": {'description': 'Kelvin (SI base unit)', 'meaning': 'UO:0000012', 'annotations': {'symbol': 'K', 'system': 'SI', 'absolute': 'true'}},
    "CELSIUS": {'description': 'Celsius/Centigrade', 'meaning': 'UO:0000027', 'annotations': {'symbol': '°C', 'conversion': 'K - 273.15'}},
    "FAHRENHEIT": {'description': 'Fahrenheit', 'meaning': 'UO:0000195', 'annotations': {'symbol': '°F', 'conversion': '(K - 273.15) * 9/5 + 32', 'system': 'imperial'}},
    "RANKINE": {'description': 'Rankine', 'annotations': {'symbol': '°R', 'conversion': 'K * 9/5', 'absolute': 'true'}},
}

class TimeUnitEnum(RichEnum):
    """
    Units of time measurement
    """
    # Enum members
    SECOND = "SECOND"
    MILLISECOND = "MILLISECOND"
    MICROSECOND = "MICROSECOND"
    NANOSECOND = "NANOSECOND"
    MINUTE = "MINUTE"
    HOUR = "HOUR"
    DAY = "DAY"
    WEEK = "WEEK"
    MONTH = "MONTH"
    YEAR = "YEAR"

# Set metadata after class creation
TimeUnitEnum._metadata = {
    "SECOND": {'description': 'Second (SI base unit)', 'meaning': 'UO:0000010', 'annotations': {'symbol': 's', 'system': 'SI'}},
    "MILLISECOND": {'description': 'Millisecond (0.001 second)', 'meaning': 'UO:0000028', 'annotations': {'symbol': 'ms', 'conversion_to_second': '0.001'}},
    "MICROSECOND": {'description': 'Microsecond (10^-6 second)', 'meaning': 'UO:0000029', 'annotations': {'symbol': 'μs', 'conversion_to_second': '1e-6'}},
    "NANOSECOND": {'description': 'Nanosecond (10^-9 second)', 'meaning': 'UO:0000150', 'annotations': {'symbol': 'ns', 'conversion_to_second': '1e-9'}},
    "MINUTE": {'description': 'Minute (60 seconds)', 'meaning': 'UO:0000031', 'annotations': {'symbol': 'min', 'conversion_to_second': '60'}},
    "HOUR": {'description': 'Hour (3600 seconds)', 'meaning': 'UO:0000032', 'annotations': {'symbol': 'h', 'conversion_to_second': '3600'}},
    "DAY": {'description': 'Day (86400 seconds)', 'meaning': 'UO:0000033', 'annotations': {'symbol': 'd', 'conversion_to_second': '86400'}},
    "WEEK": {'description': 'Week (7 days)', 'meaning': 'UO:0000034', 'annotations': {'symbol': 'wk', 'conversion_to_second': '604800'}},
    "MONTH": {'description': 'Month (approximately 30 days)', 'meaning': 'UO:0000035', 'annotations': {'symbol': 'mo', 'conversion_to_second': '2592000', 'note': 'approximate, varies by month'}},
    "YEAR": {'description': 'Year (365.25 days)', 'meaning': 'UO:0000036', 'annotations': {'symbol': 'yr', 'conversion_to_second': '31557600', 'note': 'accounts for leap years'}},
}

class PressureUnitEnum(RichEnum):
    """
    Units of pressure measurement
    """
    # Enum members
    PASCAL = "PASCAL"
    KILOPASCAL = "KILOPASCAL"
    MEGAPASCAL = "MEGAPASCAL"
    BAR = "BAR"
    MILLIBAR = "MILLIBAR"
    ATMOSPHERE = "ATMOSPHERE"
    TORR = "TORR"
    PSI = "PSI"
    MM_HG = "MM_HG"

# Set metadata after class creation
PressureUnitEnum._metadata = {
    "PASCAL": {'description': 'Pascal (SI derived unit)', 'meaning': 'UO:0000110', 'annotations': {'symbol': 'Pa', 'system': 'SI', 'definition': 'N/m²'}},
    "KILOPASCAL": {'description': 'Kilopascal (1000 pascals)', 'annotations': {'symbol': 'kPa', 'conversion_to_pascal': '1000'}},
    "MEGAPASCAL": {'description': 'Megapascal (10^6 pascals)', 'annotations': {'symbol': 'MPa', 'conversion_to_pascal': '1e6'}},
    "BAR": {'description': 'Bar', 'annotations': {'symbol': 'bar', 'conversion_to_pascal': '100000'}},
    "MILLIBAR": {'description': 'Millibar', 'annotations': {'symbol': 'mbar', 'conversion_to_pascal': '100'}},
    "ATMOSPHERE": {'description': 'Standard atmosphere', 'annotations': {'symbol': 'atm', 'conversion_to_pascal': '101325'}},
    "TORR": {'description': 'Torr (millimeter of mercury)', 'annotations': {'symbol': 'Torr', 'conversion_to_pascal': '133.322'}},
    "PSI": {'description': 'Pounds per square inch', 'meaning': 'UO:0010052', 'annotations': {'symbol': 'psi', 'conversion_to_pascal': '6894.76', 'system': 'imperial'}, 'aliases': ['pound-force per square inch']},
    "MM_HG": {'description': 'Millimeters of mercury', 'meaning': 'UO:0000272', 'annotations': {'symbol': 'mmHg', 'conversion_to_pascal': '133.322', 'use': 'medical blood pressure'}},
}

class ConcentrationUnitEnum(RichEnum):
    """
    Units of concentration measurement
    """
    # Enum members
    MOLAR = "MOLAR"
    MILLIMOLAR = "MILLIMOLAR"
    MICROMOLAR = "MICROMOLAR"
    NANOMOLAR = "NANOMOLAR"
    PICOMOLAR = "PICOMOLAR"
    MG_PER_ML = "MG_PER_ML"
    UG_PER_ML = "UG_PER_ML"
    NG_PER_ML = "NG_PER_ML"
    PERCENT = "PERCENT"
    PPM = "PPM"
    PPB = "PPB"

# Set metadata after class creation
ConcentrationUnitEnum._metadata = {
    "MOLAR": {'description': 'Molar (moles per liter)', 'meaning': 'UO:0000062', 'annotations': {'symbol': 'M', 'definition': 'mol/L'}},
    "MILLIMOLAR": {'description': 'Millimolar (10^-3 molar)', 'meaning': 'UO:0000063', 'annotations': {'symbol': 'mM', 'conversion_to_molar': '0.001'}},
    "MICROMOLAR": {'description': 'Micromolar (10^-6 molar)', 'meaning': 'UO:0000064', 'annotations': {'symbol': 'μM', 'conversion_to_molar': '1e-6'}},
    "NANOMOLAR": {'description': 'Nanomolar (10^-9 molar)', 'meaning': 'UO:0000065', 'annotations': {'symbol': 'nM', 'conversion_to_molar': '1e-9'}},
    "PICOMOLAR": {'description': 'Picomolar (10^-12 molar)', 'meaning': 'UO:0000066', 'annotations': {'symbol': 'pM', 'conversion_to_molar': '1e-12'}},
    "MG_PER_ML": {'description': 'Milligrams per milliliter', 'meaning': 'UO:0000176', 'annotations': {'symbol': 'mg/mL'}},
    "UG_PER_ML": {'description': 'Micrograms per milliliter', 'meaning': 'UO:0000274', 'annotations': {'symbol': 'μg/mL'}},
    "NG_PER_ML": {'description': 'Nanograms per milliliter', 'meaning': 'UO:0000275', 'annotations': {'symbol': 'ng/mL'}},
    "PERCENT": {'description': 'Percent (parts per hundred)', 'meaning': 'UO:0000187', 'annotations': {'symbol': '%', 'conversion_to_fraction': '0.01'}},
    "PPM": {'description': 'Parts per million', 'meaning': 'UO:0000169', 'annotations': {'symbol': 'ppm', 'conversion_to_fraction': '1e-6'}},
    "PPB": {'description': 'Parts per billion', 'meaning': 'UO:0000170', 'annotations': {'symbol': 'ppb', 'conversion_to_fraction': '1e-9'}},
}

class FrequencyUnitEnum(RichEnum):
    """
    Units of frequency measurement
    """
    # Enum members
    HERTZ = "HERTZ"
    KILOHERTZ = "KILOHERTZ"
    MEGAHERTZ = "MEGAHERTZ"
    GIGAHERTZ = "GIGAHERTZ"
    RPM = "RPM"
    BPM = "BPM"

# Set metadata after class creation
FrequencyUnitEnum._metadata = {
    "HERTZ": {'description': 'Hertz (cycles per second)', 'meaning': 'UO:0000106', 'annotations': {'symbol': 'Hz', 'system': 'SI'}},
    "KILOHERTZ": {'description': 'Kilohertz (1000 Hz)', 'annotations': {'symbol': 'kHz', 'conversion_to_hz': '1000'}},
    "MEGAHERTZ": {'description': 'Megahertz (10^6 Hz)', 'meaning': 'UO:0000325', 'annotations': {'symbol': 'MHz', 'conversion_to_hz': '1e6'}},
    "GIGAHERTZ": {'description': 'Gigahertz (10^9 Hz)', 'annotations': {'symbol': 'GHz', 'conversion_to_hz': '1e9'}},
    "RPM": {'description': 'Revolutions per minute', 'annotations': {'symbol': 'rpm', 'conversion_to_hz': '0.0166667'}},
    "BPM": {'description': 'Beats per minute', 'annotations': {'symbol': 'bpm', 'conversion_to_hz': '0.0166667', 'use': 'heart rate'}},
}

class AngleUnitEnum(RichEnum):
    """
    Units of angle measurement
    """
    # Enum members
    RADIAN = "RADIAN"
    DEGREE = "DEGREE"
    MINUTE_OF_ARC = "MINUTE_OF_ARC"
    SECOND_OF_ARC = "SECOND_OF_ARC"
    GRADIAN = "GRADIAN"
    TURN = "TURN"

# Set metadata after class creation
AngleUnitEnum._metadata = {
    "RADIAN": {'description': 'Radian (SI derived unit)', 'meaning': 'UO:0000123', 'annotations': {'symbol': 'rad', 'system': 'SI'}},
    "DEGREE": {'description': 'Degree', 'meaning': 'UO:0000185', 'annotations': {'symbol': '°', 'conversion_to_radian': '0.0174533'}},
    "MINUTE_OF_ARC": {'description': 'Minute of arc/arcminute', 'annotations': {'symbol': "'", 'conversion_to_degree': '0.0166667'}},
    "SECOND_OF_ARC": {'description': 'Second of arc/arcsecond', 'annotations': {'symbol': '"', 'conversion_to_degree': '0.000277778'}},
    "GRADIAN": {'description': 'Gradian/gon', 'annotations': {'symbol': 'gon', 'conversion_to_degree': '0.9'}},
    "TURN": {'description': 'Turn/revolution', 'annotations': {'symbol': 'turn', 'conversion_to_radian': '6.28319'}},
}

class DataSizeUnitEnum(RichEnum):
    """
    Units of digital data size
    """
    # Enum members
    BIT = "BIT"
    BYTE = "BYTE"
    KILOBYTE = "KILOBYTE"
    MEGABYTE = "MEGABYTE"
    GIGABYTE = "GIGABYTE"
    TERABYTE = "TERABYTE"
    PETABYTE = "PETABYTE"
    KIBIBYTE = "KIBIBYTE"
    MEBIBYTE = "MEBIBYTE"
    GIBIBYTE = "GIBIBYTE"
    TEBIBYTE = "TEBIBYTE"

# Set metadata after class creation
DataSizeUnitEnum._metadata = {
    "BIT": {'description': 'Bit (binary digit)', 'annotations': {'symbol': 'bit', 'base': 'binary'}},
    "BYTE": {'description': 'Byte (8 bits)', 'meaning': 'UO:0000233', 'annotations': {'symbol': 'B', 'conversion_to_bit': '8'}},
    "KILOBYTE": {'description': 'Kilobyte (1000 bytes)', 'meaning': 'UO:0000234', 'annotations': {'symbol': 'KB', 'conversion_to_byte': '1000', 'standard': 'decimal'}},
    "MEGABYTE": {'description': 'Megabyte (10^6 bytes)', 'meaning': 'UO:0000235', 'annotations': {'symbol': 'MB', 'conversion_to_byte': '1e6', 'standard': 'decimal'}},
    "GIGABYTE": {'description': 'Gigabyte (10^9 bytes)', 'annotations': {'symbol': 'GB', 'conversion_to_byte': '1e9', 'standard': 'decimal'}},
    "TERABYTE": {'description': 'Terabyte (10^12 bytes)', 'annotations': {'symbol': 'TB', 'conversion_to_byte': '1e12', 'standard': 'decimal'}},
    "PETABYTE": {'description': 'Petabyte (10^15 bytes)', 'annotations': {'symbol': 'PB', 'conversion_to_byte': '1e15', 'standard': 'decimal'}},
    "KIBIBYTE": {'description': 'Kibibyte (1024 bytes)', 'annotations': {'symbol': 'KiB', 'conversion_to_byte': '1024', 'standard': 'binary'}},
    "MEBIBYTE": {'description': 'Mebibyte (2^20 bytes)', 'annotations': {'symbol': 'MiB', 'conversion_to_byte': '1048576', 'standard': 'binary'}},
    "GIBIBYTE": {'description': 'Gibibyte (2^30 bytes)', 'annotations': {'symbol': 'GiB', 'conversion_to_byte': '1073741824', 'standard': 'binary'}},
    "TEBIBYTE": {'description': 'Tebibyte (2^40 bytes)', 'annotations': {'symbol': 'TiB', 'conversion_to_byte': '1099511627776', 'standard': 'binary'}},
}

class ImageFileFormatEnum(RichEnum):
    """
    Common image file formats
    """
    # Enum members
    JPEG = "JPEG"
    PNG = "PNG"
    GIF = "GIF"
    BMP = "BMP"
    TIFF = "TIFF"
    SVG = "SVG"
    WEBP = "WEBP"
    HEIC = "HEIC"
    RAW = "RAW"
    ICO = "ICO"

# Set metadata after class creation
ImageFileFormatEnum._metadata = {
    "JPEG": {'description': 'Joint Photographic Experts Group', 'meaning': 'EDAM:format_3579', 'annotations': {'extension': '.jpg, .jpeg', 'mime_type': 'image/jpeg', 'compression': 'lossy'}, 'aliases': ['JPG']},
    "PNG": {'description': 'Portable Network Graphics', 'meaning': 'EDAM:format_3603', 'annotations': {'extension': '.png', 'mime_type': 'image/png', 'compression': 'lossless'}},
    "GIF": {'description': 'Graphics Interchange Format', 'meaning': 'EDAM:format_3467', 'annotations': {'extension': '.gif', 'mime_type': 'image/gif', 'features': 'animation support'}},
    "BMP": {'description': 'Bitmap Image File', 'meaning': 'EDAM:format_3592', 'annotations': {'extension': '.bmp', 'mime_type': 'image/bmp', 'compression': 'uncompressed'}},
    "TIFF": {'description': 'Tagged Image File Format', 'meaning': 'EDAM:format_3591', 'annotations': {'extension': '.tif, .tiff', 'mime_type': 'image/tiff', 'use': 'professional photography, scanning'}},
    "SVG": {'description': 'Scalable Vector Graphics', 'meaning': 'EDAM:format_3604', 'annotations': {'extension': '.svg', 'mime_type': 'image/svg+xml', 'type': 'vector'}},
    "WEBP": {'description': 'WebP image format', 'annotations': {'extension': '.webp', 'mime_type': 'image/webp', 'compression': 'lossy and lossless'}},
    "HEIC": {'description': 'High Efficiency Image Container', 'annotations': {'extension': '.heic, .heif', 'mime_type': 'image/heic', 'use': 'Apple devices'}},
    "RAW": {'description': 'Raw image format', 'annotations': {'extension': '.raw, .cr2, .nef, .arw', 'type': 'unprocessed sensor data'}},
    "ICO": {'description': 'Icon file format', 'annotations': {'extension': '.ico', 'mime_type': 'image/x-icon', 'use': 'favicons, app icons'}},
}

class DocumentFormatEnum(RichEnum):
    """
    Document and text file formats
    """
    # Enum members
    PDF = "PDF"
    DOCX = "DOCX"
    DOC = "DOC"
    TXT = "TXT"
    RTF = "RTF"
    ODT = "ODT"
    LATEX = "LATEX"
    MARKDOWN = "MARKDOWN"
    HTML = "HTML"
    XML = "XML"
    EPUB = "EPUB"

# Set metadata after class creation
DocumentFormatEnum._metadata = {
    "PDF": {'description': 'Portable Document Format', 'meaning': 'EDAM:format_3508', 'annotations': {'extension': '.pdf', 'mime_type': 'application/pdf', 'creator': 'Adobe'}},
    "DOCX": {'description': 'Microsoft Word Open XML', 'annotations': {'extension': '.docx', 'mime_type': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document', 'application': 'Microsoft Word'}},
    "DOC": {'description': 'Microsoft Word legacy format', 'annotations': {'extension': '.doc', 'mime_type': 'application/msword', 'application': 'Microsoft Word (legacy)'}},
    "TXT": {'description': 'Plain text file', 'meaning': 'EDAM:format_1964', 'annotations': {'extension': '.txt', 'mime_type': 'text/plain', 'encoding': 'UTF-8, ASCII'}, 'aliases': ['plain text format (unformatted)']},
    "RTF": {'description': 'Rich Text Format', 'annotations': {'extension': '.rtf', 'mime_type': 'application/rtf'}},
    "ODT": {'description': 'OpenDocument Text', 'annotations': {'extension': '.odt', 'mime_type': 'application/vnd.oasis.opendocument.text', 'application': 'LibreOffice, OpenOffice'}},
    "LATEX": {'description': 'LaTeX document', 'meaning': 'EDAM:format_3817', 'annotations': {'extension': '.tex', 'mime_type': 'application/x-latex', 'use': 'scientific documents'}, 'aliases': ['latex', 'LaTeX']},
    "MARKDOWN": {'description': 'Markdown formatted text', 'annotations': {'extension': '.md, .markdown', 'mime_type': 'text/markdown'}},
    "HTML": {'description': 'HyperText Markup Language', 'meaning': 'EDAM:format_2331', 'annotations': {'extension': '.html, .htm', 'mime_type': 'text/html'}},
    "XML": {'description': 'Extensible Markup Language', 'meaning': 'EDAM:format_2332', 'annotations': {'extension': '.xml', 'mime_type': 'application/xml'}},
    "EPUB": {'description': 'Electronic Publication', 'annotations': {'extension': '.epub', 'mime_type': 'application/epub+zip', 'use': 'e-books'}},
}

class DataFormatEnum(RichEnum):
    """
    Structured data file formats
    """
    # Enum members
    JSON = "JSON"
    CSV = "CSV"
    TSV = "TSV"
    YAML = "YAML"
    TOML = "TOML"
    XLSX = "XLSX"
    XLS = "XLS"
    ODS = "ODS"
    PARQUET = "PARQUET"
    AVRO = "AVRO"
    HDF5 = "HDF5"
    NETCDF = "NETCDF"
    SQLITE = "SQLITE"

# Set metadata after class creation
DataFormatEnum._metadata = {
    "JSON": {'description': 'JavaScript Object Notation', 'meaning': 'EDAM:format_3464', 'annotations': {'extension': '.json', 'mime_type': 'application/json', 'type': 'text-based'}},
    "CSV": {'description': 'Comma-Separated Values', 'meaning': 'EDAM:format_3752', 'annotations': {'extension': '.csv', 'mime_type': 'text/csv', 'delimiter': 'comma'}},
    "TSV": {'description': 'Tab-Separated Values', 'meaning': 'EDAM:format_3475', 'annotations': {'extension': '.tsv, .tab', 'mime_type': 'text/tab-separated-values', 'delimiter': 'tab'}},
    "YAML": {'description': "YAML Ain't Markup Language", 'meaning': 'EDAM:format_3750', 'annotations': {'extension': '.yaml, .yml', 'mime_type': 'application/x-yaml'}},
    "TOML": {'description': "Tom's Obvious Minimal Language", 'annotations': {'extension': '.toml', 'mime_type': 'application/toml', 'use': 'configuration files'}},
    "XLSX": {'description': 'Microsoft Excel Open XML', 'annotations': {'extension': '.xlsx', 'mime_type': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'}},
    "XLS": {'description': 'Microsoft Excel legacy format', 'annotations': {'extension': '.xls', 'mime_type': 'application/vnd.ms-excel'}},
    "ODS": {'description': 'OpenDocument Spreadsheet', 'annotations': {'extension': '.ods', 'mime_type': 'application/vnd.oasis.opendocument.spreadsheet'}},
    "PARQUET": {'description': 'Apache Parquet columnar format', 'annotations': {'extension': '.parquet', 'mime_type': 'application/parquet', 'type': 'columnar storage'}},
    "AVRO": {'description': 'Apache Avro data serialization', 'annotations': {'extension': '.avro', 'mime_type': 'application/avro', 'features': 'schema evolution'}},
    "HDF5": {'description': 'Hierarchical Data Format version 5', 'meaning': 'EDAM:format_3590', 'annotations': {'extension': '.h5, .hdf5', 'mime_type': 'application/x-hdf', 'use': 'scientific data'}},
    "NETCDF": {'description': 'Network Common Data Form', 'meaning': 'EDAM:format_3650', 'annotations': {'extension': '.nc, .nc4', 'mime_type': 'application/x-netcdf', 'use': 'array-oriented scientific data'}},
    "SQLITE": {'description': 'SQLite database', 'annotations': {'extension': '.db, .sqlite, .sqlite3', 'mime_type': 'application/x-sqlite3', 'type': 'embedded database'}},
}

class ArchiveFormatEnum(RichEnum):
    """
    Archive and compression formats
    """
    # Enum members
    ZIP = "ZIP"
    TAR = "TAR"
    GZIP = "GZIP"
    TAR_GZ = "TAR_GZ"
    BZIP2 = "BZIP2"
    TAR_BZ2 = "TAR_BZ2"
    XZ = "XZ"
    TAR_XZ = "TAR_XZ"
    SEVEN_ZIP = "SEVEN_ZIP"
    RAR = "RAR"

# Set metadata after class creation
ArchiveFormatEnum._metadata = {
    "ZIP": {'description': 'ZIP archive', 'annotations': {'extension': '.zip', 'mime_type': 'application/zip', 'compression': 'DEFLATE'}},
    "TAR": {'description': 'Tape Archive', 'annotations': {'extension': '.tar', 'mime_type': 'application/x-tar', 'compression': 'none (archive only)'}},
    "GZIP": {'description': 'GNU zip', 'annotations': {'extension': '.gz', 'mime_type': 'application/gzip', 'compression': 'DEFLATE'}},
    "TAR_GZ": {'description': 'Gzipped tar archive', 'annotations': {'extension': '.tar.gz, .tgz', 'mime_type': 'application/x-gtar', 'compression': 'tar + gzip'}},
    "BZIP2": {'description': 'Bzip2 compression', 'annotations': {'extension': '.bz2', 'mime_type': 'application/x-bzip2', 'compression': 'Burrows-Wheeler'}},
    "TAR_BZ2": {'description': 'Bzip2 compressed tar archive', 'annotations': {'extension': '.tar.bz2, .tbz2', 'mime_type': 'application/x-bzip2'}},
    "XZ": {'description': 'XZ compression', 'annotations': {'extension': '.xz', 'mime_type': 'application/x-xz', 'compression': 'LZMA2'}},
    "TAR_XZ": {'description': 'XZ compressed tar archive', 'annotations': {'extension': '.tar.xz, .txz', 'mime_type': 'application/x-xz'}},
    "SEVEN_ZIP": {'description': '7-Zip archive', 'annotations': {'extension': '.7z', 'mime_type': 'application/x-7z-compressed', 'compression': 'LZMA'}},
    "RAR": {'description': 'RAR archive', 'annotations': {'extension': '.rar', 'mime_type': 'application/vnd.rar', 'proprietary': 'true'}},
}

class VideoFormatEnum(RichEnum):
    """
    Video file formats
    """
    # Enum members
    MP4 = "MP4"
    AVI = "AVI"
    MOV = "MOV"
    MKV = "MKV"
    WEBM = "WEBM"
    FLV = "FLV"
    WMV = "WMV"
    MPEG = "MPEG"

# Set metadata after class creation
VideoFormatEnum._metadata = {
    "MP4": {'description': 'MPEG-4 Part 14', 'annotations': {'extension': '.mp4', 'mime_type': 'video/mp4', 'codec': 'H.264, H.265'}},
    "AVI": {'description': 'Audio Video Interleave', 'annotations': {'extension': '.avi', 'mime_type': 'video/x-msvideo', 'creator': 'Microsoft'}},
    "MOV": {'description': 'QuickTime Movie', 'annotations': {'extension': '.mov', 'mime_type': 'video/quicktime', 'creator': 'Apple'}},
    "MKV": {'description': 'Matroska Video', 'annotations': {'extension': '.mkv', 'mime_type': 'video/x-matroska', 'features': 'multiple tracks'}},
    "WEBM": {'description': 'WebM video', 'annotations': {'extension': '.webm', 'mime_type': 'video/webm', 'codec': 'VP8, VP9'}},
    "FLV": {'description': 'Flash Video', 'annotations': {'extension': '.flv', 'mime_type': 'video/x-flv', 'status': 'legacy'}},
    "WMV": {'description': 'Windows Media Video', 'annotations': {'extension': '.wmv', 'mime_type': 'video/x-ms-wmv', 'creator': 'Microsoft'}},
    "MPEG": {'description': 'Moving Picture Experts Group', 'annotations': {'extension': '.mpeg, .mpg', 'mime_type': 'video/mpeg'}},
}

class AudioFormatEnum(RichEnum):
    """
    Audio file formats
    """
    # Enum members
    MP3 = "MP3"
    WAV = "WAV"
    FLAC = "FLAC"
    AAC = "AAC"
    OGG = "OGG"
    M4A = "M4A"
    WMA = "WMA"
    OPUS = "OPUS"
    AIFF = "AIFF"

# Set metadata after class creation
AudioFormatEnum._metadata = {
    "MP3": {'description': 'MPEG Audio Layer 3', 'annotations': {'extension': '.mp3', 'mime_type': 'audio/mpeg', 'compression': 'lossy'}},
    "WAV": {'description': 'Waveform Audio File Format', 'annotations': {'extension': '.wav', 'mime_type': 'audio/wav', 'compression': 'uncompressed'}},
    "FLAC": {'description': 'Free Lossless Audio Codec', 'annotations': {'extension': '.flac', 'mime_type': 'audio/flac', 'compression': 'lossless'}},
    "AAC": {'description': 'Advanced Audio Coding', 'annotations': {'extension': '.aac', 'mime_type': 'audio/aac', 'compression': 'lossy'}},
    "OGG": {'description': 'Ogg Vorbis', 'annotations': {'extension': '.ogg', 'mime_type': 'audio/ogg', 'compression': 'lossy'}},
    "M4A": {'description': 'MPEG-4 Audio', 'annotations': {'extension': '.m4a', 'mime_type': 'audio/mp4', 'compression': 'lossy or lossless'}},
    "WMA": {'description': 'Windows Media Audio', 'annotations': {'extension': '.wma', 'mime_type': 'audio/x-ms-wma', 'creator': 'Microsoft'}},
    "OPUS": {'description': 'Opus Interactive Audio Codec', 'annotations': {'extension': '.opus', 'mime_type': 'audio/opus', 'use': 'streaming, VoIP'}},
    "AIFF": {'description': 'Audio Interchange File Format', 'annotations': {'extension': '.aiff, .aif', 'mime_type': 'audio/aiff', 'creator': 'Apple'}},
}

class ProgrammingLanguageFileEnum(RichEnum):
    """
    Programming language source file extensions
    """
    # Enum members
    PYTHON = "PYTHON"
    JAVASCRIPT = "JAVASCRIPT"
    TYPESCRIPT = "TYPESCRIPT"
    JAVA = "JAVA"
    C = "C"
    CPP = "CPP"
    C_SHARP = "C_SHARP"
    GO = "GO"
    RUST = "RUST"
    RUBY = "RUBY"
    PHP = "PHP"
    SWIFT = "SWIFT"
    KOTLIN = "KOTLIN"
    R = "R"
    MATLAB = "MATLAB"
    JULIA = "JULIA"
    SHELL = "SHELL"

# Set metadata after class creation
ProgrammingLanguageFileEnum._metadata = {
    "PYTHON": {'description': 'Python source file', 'annotations': {'extension': '.py', 'mime_type': 'text/x-python'}},
    "JAVASCRIPT": {'description': 'JavaScript source file', 'annotations': {'extension': '.js', 'mime_type': 'text/javascript'}},
    "TYPESCRIPT": {'description': 'TypeScript source file', 'annotations': {'extension': '.ts', 'mime_type': 'text/typescript'}},
    "JAVA": {'description': 'Java source file', 'annotations': {'extension': '.java', 'mime_type': 'text/x-java-source'}},
    "C": {'description': 'C source file', 'annotations': {'extension': '.c', 'mime_type': 'text/x-c'}},
    "CPP": {'description': 'C++ source file', 'annotations': {'extension': '.cpp, .cc, .cxx', 'mime_type': 'text/x-c++'}},
    "C_SHARP": {'description': 'C# source file', 'annotations': {'extension': '.cs', 'mime_type': 'text/x-csharp'}},
    "GO": {'description': 'Go source file', 'annotations': {'extension': '.go', 'mime_type': 'text/x-go'}},
    "RUST": {'description': 'Rust source file', 'annotations': {'extension': '.rs', 'mime_type': 'text/x-rust'}},
    "RUBY": {'description': 'Ruby source file', 'annotations': {'extension': '.rb', 'mime_type': 'text/x-ruby'}},
    "PHP": {'description': 'PHP source file', 'annotations': {'extension': '.php', 'mime_type': 'text/x-php'}},
    "SWIFT": {'description': 'Swift source file', 'annotations': {'extension': '.swift', 'mime_type': 'text/x-swift'}},
    "KOTLIN": {'description': 'Kotlin source file', 'annotations': {'extension': '.kt', 'mime_type': 'text/x-kotlin'}},
    "R": {'description': 'R source file', 'annotations': {'extension': '.r, .R', 'mime_type': 'text/x-r'}},
    "MATLAB": {'description': 'MATLAB source file', 'annotations': {'extension': '.m', 'mime_type': 'text/x-matlab'}},
    "JULIA": {'description': 'Julia source file', 'annotations': {'extension': '.jl', 'mime_type': 'text/x-julia'}},
    "SHELL": {'description': 'Shell script', 'annotations': {'extension': '.sh, .bash', 'mime_type': 'text/x-shellscript'}},
}

class NetworkProtocolEnum(RichEnum):
    """
    Network communication protocols
    """
    # Enum members
    HTTP = "HTTP"
    HTTPS = "HTTPS"
    FTP = "FTP"
    SFTP = "SFTP"
    SSH = "SSH"
    TELNET = "TELNET"
    SMTP = "SMTP"
    POP3 = "POP3"
    IMAP = "IMAP"
    DNS = "DNS"
    DHCP = "DHCP"
    TCP = "TCP"
    UDP = "UDP"
    WEBSOCKET = "WEBSOCKET"
    MQTT = "MQTT"
    AMQP = "AMQP"
    GRPC = "GRPC"

# Set metadata after class creation
NetworkProtocolEnum._metadata = {
    "HTTP": {'description': 'Hypertext Transfer Protocol', 'annotations': {'port': '80', 'layer': 'application', 'version': '1.0, 1.1, 2, 3'}},
    "HTTPS": {'description': 'HTTP Secure', 'annotations': {'port': '443', 'layer': 'application', 'encryption': 'TLS/SSL'}},
    "FTP": {'description': 'File Transfer Protocol', 'annotations': {'port': '21', 'layer': 'application', 'use': 'file transfer'}},
    "SFTP": {'description': 'SSH File Transfer Protocol', 'annotations': {'port': '22', 'layer': 'application', 'encryption': 'SSH'}},
    "SSH": {'description': 'Secure Shell', 'annotations': {'port': '22', 'layer': 'application', 'use': 'secure remote access'}},
    "TELNET": {'description': 'Telnet protocol', 'annotations': {'port': '23', 'layer': 'application', 'security': 'unencrypted'}},
    "SMTP": {'description': 'Simple Mail Transfer Protocol', 'annotations': {'port': '25, 587', 'layer': 'application', 'use': 'email sending'}},
    "POP3": {'description': 'Post Office Protocol version 3', 'annotations': {'port': '110, 995', 'layer': 'application', 'use': 'email retrieval'}},
    "IMAP": {'description': 'Internet Message Access Protocol', 'annotations': {'port': '143, 993', 'layer': 'application', 'use': 'email access'}},
    "DNS": {'description': 'Domain Name System', 'annotations': {'port': '53', 'layer': 'application', 'use': 'name resolution'}},
    "DHCP": {'description': 'Dynamic Host Configuration Protocol', 'annotations': {'port': '67, 68', 'layer': 'application', 'use': 'IP assignment'}},
    "TCP": {'description': 'Transmission Control Protocol', 'annotations': {'layer': 'transport', 'type': 'connection-oriented'}},
    "UDP": {'description': 'User Datagram Protocol', 'annotations': {'layer': 'transport', 'type': 'connectionless'}},
    "WEBSOCKET": {'description': 'WebSocket protocol', 'annotations': {'port': '80, 443', 'layer': 'application', 'use': 'bidirectional communication'}},
    "MQTT": {'description': 'Message Queuing Telemetry Transport', 'annotations': {'port': '1883, 8883', 'layer': 'application', 'use': 'IoT messaging'}},
    "AMQP": {'description': 'Advanced Message Queuing Protocol', 'annotations': {'port': '5672', 'layer': 'application', 'use': 'message queuing'}},
    "GRPC": {'description': 'gRPC Remote Procedure Call', 'annotations': {'transport': 'HTTP/2', 'use': 'RPC framework'}},
}

__all__ = [
    "RelativeTimeEnum",
    "PresenceEnum",
    "DataAbsentEnum",
    "PredictionOutcomeType",
    "VitalStatusEnum",
    "HealthcareEncounterClassification",
    "CaseOrControlEnum",
    "GOEvidenceCode",
    "GOElectronicMethods",
    "CommonOrganismTaxaEnum",
    "TaxonomicRank",
    "BiologicalKingdom",
    "CellCyclePhase",
    "MitoticPhase",
    "CellCycleCheckpoint",
    "MeioticPhase",
    "CellCycleRegulator",
    "CellProliferationState",
    "DNADamageResponse",
    "GenomeFeatureType",
    "SampleType",
    "StructuralBiologyTechnique",
    "CryoEMPreparationType",
    "CryoEMGridType",
    "VitrificationMethod",
    "CrystallizationMethod",
    "XRaySource",
    "Detector",
    "WorkflowType",
    "FileFormat",
    "DataType",
    "ProcessingStatus",
    "InsdcMissingValueEnum",
    "ViralGenomeTypeEnum",
    "PlantSexEnum",
    "RelToOxygenEnum",
    "TrophicLevelEnum",
    "DayOfWeek",
    "Month",
    "Quarter",
    "Season",
    "TimePeriod",
    "TimeUnit",
    "TimeOfDay",
    "BusinessTimeFrame",
    "GeologicalEra",
    "HistoricalPeriod",
    "PublicationType",
    "PeerReviewStatus",
    "AcademicDegree",
    "LicenseType",
    "ResearchField",
    "FundingType",
    "ManuscriptSection",
    "ResearchRole",
    "OpenAccessType",
    "CitationStyle",
    "EnergySource",
    "EnergyUnit",
    "PowerUnit",
    "EnergyEfficiencyRating",
    "BuildingEnergyStandard",
    "GridType",
    "EnergyStorageType",
    "EmissionScope",
    "CarbonIntensity",
    "ElectricityMarket",
    "FossilFuelTypeEnum",
    "MiningType",
    "MineralCategory",
    "CriticalMineral",
    "CommonMineral",
    "MiningEquipment",
    "OreGrade",
    "MiningPhase",
    "MiningHazard",
    "EnvironmentalImpact",
    "ExtractiveIndustryFacilityTypeEnum",
    "ExtractiveIndustryProductTypeEnum",
    "MiningMethodEnum",
    "WellTypeEnum",
    "OutcomeTypeEnum",
    "PersonStatusEnum",
    "MaritalStatusEnum",
    "EmploymentStatusEnum",
    "MimeType",
    "MimeTypeCategory",
    "TextCharset",
    "CompressionType",
    "StateOfMatterEnum",
    "AirPollutantEnum",
    "PesticideTypeEnum",
    "HeavyMetalEnum",
    "ExposureRouteEnum",
    "ExposureSourceEnum",
    "WaterContaminantEnum",
    "EndocrineDisruptorEnum",
    "ExposureDurationEnum",
    "CountryCodeISO2Enum",
    "CountryCodeISO3Enum",
    "USStateCodeEnum",
    "CanadianProvinceCodeEnum",
    "CompassDirection",
    "RelativeDirection",
    "WindDirection",
    "ContinentEnum",
    "UNRegionEnum",
    "LanguageCodeISO6391enum",
    "TimeZoneEnum",
    "CurrencyCodeISO4217Enum",
    "SentimentClassificationEnum",
    "FineSentimentClassificationEnum",
    "BinaryClassificationEnum",
    "SpamClassificationEnum",
    "AnomalyDetectionEnum",
    "ChurnClassificationEnum",
    "FraudDetectionEnum",
    "QualityControlEnum",
    "DefectClassificationEnum",
    "BasicEmotionEnum",
    "ExtendedEmotionEnum",
    "PriorityLevelEnum",
    "SeverityLevelEnum",
    "ConfidenceLevelEnum",
    "NewsTopicCategoryEnum",
    "ToxicityClassificationEnum",
    "IntentClassificationEnum",
    "SimpleSpatialDirection",
    "AnatomicalSide",
    "AnatomicalRegion",
    "AnatomicalAxis",
    "AnatomicalPlane",
    "SpatialRelationship",
    "CellPolarity",
    "CrystalSystemEnum",
    "BravaisLatticeEnum",
    "ElectricalConductivityEnum",
    "MagneticPropertyEnum",
    "OpticalPropertyEnum",
    "ThermalConductivityEnum",
    "MechanicalBehaviorEnum",
    "MicroscopyMethodEnum",
    "SpectroscopyMethodEnum",
    "ThermalAnalysisMethodEnum",
    "MechanicalTestingMethodEnum",
    "MaterialClassEnum",
    "PolymerTypeEnum",
    "MetalTypeEnum",
    "CompositeTypeEnum",
    "SynthesisMethodEnum",
    "CrystalGrowthMethodEnum",
    "AdditiveManufacturingEnum",
    "TraditionalPigmentEnum",
    "IndustrialDyeEnum",
    "FoodColoringEnum",
    "AutomobilePaintColorEnum",
    "BasicColorEnum",
    "WebColorEnum",
    "X11ColorEnum",
    "ColorSpaceEnum",
    "EyeColorEnum",
    "HairColorEnum",
    "FlowerColorEnum",
    "AnimalCoatColorEnum",
    "SkinToneEnum",
    "PlantLeafColorEnum",
    "DNABaseEnum",
    "DNABaseExtendedEnum",
    "RNABaseEnum",
    "RNABaseExtendedEnum",
    "AminoAcidEnum",
    "AminoAcidExtendedEnum",
    "CodonEnum",
    "NucleotideModificationEnum",
    "SequenceQualityEnum",
    "SubatomicParticleEnum",
    "BondTypeEnum",
    "PeriodicTableBlockEnum",
    "ElementFamilyEnum",
    "ElementMetallicClassificationEnum",
    "HardOrSoftEnum",
    "BronstedAcidBaseRoleEnum",
    "LewisAcidBaseRoleEnum",
    "OxidationStateEnum",
    "ChiralityEnum",
    "NanostructureMorphologyEnum",
    "ReactionTypeEnum",
    "ReactionMechanismEnum",
    "CatalystTypeEnum",
    "ReactionConditionEnum",
    "ReactionRateOrderEnum",
    "EnzymeClassEnum",
    "SolventClassEnum",
    "ThermodynamicParameterEnum",
    "SafetyColorEnum",
    "TrafficLightColorEnum",
    "HazmatColorEnum",
    "FireSafetyColorEnum",
    "MaritimeSignalColorEnum",
    "AviationLightColorEnum",
    "ElectricalWireColorEnum",
    "BloodTypeEnum",
    "AnatomicalSystemEnum",
    "MedicalSpecialtyEnum",
    "DrugRouteEnum",
    "VitalSignEnum",
    "DiagnosticTestTypeEnum",
    "SymptomSeverityEnum",
    "AllergyTypeEnum",
    "VaccineTypeEnum",
    "BMIClassificationEnum",
    "RaceOMB1997Enum",
    "EthnicityOMB1997Enum",
    "BiologicalSexEnum",
    "GenderIdentityEnum",
    "AgeGroupEnum",
    "ParticipantVitalStatusEnum",
    "RecruitmentStatusEnum",
    "StudyPhaseEnum",
    "EducationLevelEnum",
    "KaryotypicSexEnum",
    "PhenotypicSexEnum",
    "AllelicStateEnum",
    "LateralityEnum",
    "OnsetTimingEnum",
    "ACMGPathogenicityEnum",
    "TherapeuticActionabilityEnum",
    "InterpretationProgressEnum",
    "RegimenStatusEnum",
    "DrugResponseEnum",
    "ProcessScaleEnum",
    "BioreactorTypeEnum",
    "FermentationModeEnum",
    "OxygenationStrategyEnum",
    "AgitationTypeEnum",
    "DownstreamProcessEnum",
    "FeedstockTypeEnum",
    "ProductTypeEnum",
    "SterilizationMethodEnum",
    "LengthUnitEnum",
    "MassUnitEnum",
    "VolumeUnitEnum",
    "TemperatureUnitEnum",
    "TimeUnitEnum",
    "PressureUnitEnum",
    "ConcentrationUnitEnum",
    "FrequencyUnitEnum",
    "AngleUnitEnum",
    "DataSizeUnitEnum",
    "ImageFileFormatEnum",
    "DocumentFormatEnum",
    "DataFormatEnum",
    "ArchiveFormatEnum",
    "VideoFormatEnum",
    "AudioFormatEnum",
    "ProgrammingLanguageFileEnum",
    "NetworkProtocolEnum",
]
