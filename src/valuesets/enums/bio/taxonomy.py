"""
Taxonomic Classifications

Value sets for taxonomic classifications and model organisms

Generated from: bio/taxonomy.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

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

__all__ = [
    "CommonOrganismTaxaEnum",
    "TaxonomicRank",
    "BiologicalKingdom",
]