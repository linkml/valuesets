"""
Genome Assemblies and Chromosomes

Value sets for reference genome builds (assemblies) and chromosome names/codes for human and common model organisms. Chromosome terms are mapped to the Monochrom Ontology (CHR, https://github.com/monarch-initiative/monochrom), which provides OWL classes for chromosomes and chromosome bands derived from UCSC cytoband files. Genome builds are mapped to their INSDC (GenBank) assembly accessions; the paired RefSeq accession and UCSC database name are given as annotations.

Generated from: bio/genome_assemblies.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class HumanGenomeBuild(RichEnum):
    """
    Human (Homo sapiens) reference genome assemblies. Permissible value names follow the Genome Reference Consortium (GRC) / NCBI assembly names; UCSC database names (hg38, hg19, ...) are given as aliases. Meanings are the INSDC assembly accessions for the base (unpatched) release; patch releases share the same coordinate system.
    """
    # Enum members
    GRCH38 = "GRCh38"
    GRCH37 = "GRCh37"
    NCBI36 = "NCBI36"
    T2T_CHM13V2 = "T2T_CHM13v2"

# Set metadata after class creation
HumanGenomeBuild._metadata = {
    "GRCH38": {'description': 'Genome Reference Consortium Human Build 38, released December 2013. Current primary human reference assembly (latest patch GRCh38.p14, GCA_000001405.29).', 'meaning': 'insdc.gca:GCA_000001405.15', 'annotations': {'ucsc_name': 'hg38', 'refseq_accession': 'GCF_000001405.26', 'ncbi_assembly_name': 'GRCh38'}, 'aliases': ['hg38', 'GRCh38', 'GRCh38.p14']},
    "GRCH37": {'description': 'Genome Reference Consortium Human Build 37, released February 2009. UCSC hg19 is largely equivalent but uses a different mitochondrial sequence (NC_001807 rather than the rCRS NC_012920) and "chr"-prefixed sequence names.', 'meaning': 'insdc.gca:GCA_000001405.1', 'annotations': {'ucsc_name': 'hg19', 'refseq_accession': 'GCF_000001405.13', 'ncbi_assembly_name': 'GRCh37'}, 'aliases': ['hg19', 'GRCh37', 'GRCh37.p13', 'b37']},
    "NCBI36": {'description': 'NCBI Build 36.1 of the human genome, released March 2006. Superseded.', 'annotations': {'ucsc_name': 'hg18', 'refseq_accession': 'GCF_000001405.12', 'ncbi_assembly_name': 'NCBI36'}, 'aliases': ['hg18', 'NCBI Build 36']},
    "T2T_CHM13V2": {'description': 'Telomere-to-Telomere Consortium complete gapless assembly of the CHM13 hydatidiform mole cell line, version 2.0 (adds chrY from HG002), released 2022.', 'meaning': 'insdc.gca:GCA_009914755.4', 'annotations': {'ucsc_name': 'hs1', 'refseq_accession': 'GCF_009914755.1', 'ncbi_assembly_name': 'T2T-CHM13v2.0'}, 'aliases': ['T2T-CHM13v2.0', 'CHM13v2.0', 'hs1']},
}

class ModelOrganismGenomeBuild(RichEnum):
    """
    Reference genome assemblies for common model organisms, including all non-human builds used by the Monochrom Ontology. Permissible value names follow the NCBI assembly names (with dots replaced by underscores); UCSC database names are given as aliases.
    """
    # Enum members
    GRCM39 = "GRCm39"
    GRCM38 = "GRCm38"
    MRATBN7_2 = "mRatBN7_2"
    RNOR_6_0 = "Rnor_6_0"
    GRCZ11 = "GRCz11"
    GRCZ10 = "GRCz10"
    GRCG6A = "GRCg6a"
    WBCEL235 = "WBcel235"
    BDGP6 = "BDGP6"
    CALLITHRIX_JACCHUS_CJ1700_1_1 = "Callithrix_jacchus_cj1700_1_1"

# Set metadata after class creation
ModelOrganismGenomeBuild._metadata = {
    "GRCM39": {'description': 'Genome Reference Consortium Mouse Build 39 (Mus musculus), released 2020', 'meaning': 'insdc.gca:GCA_000001635.9', 'annotations': {'ucsc_name': 'mm39', 'refseq_accession': 'GCF_000001635.27', 'taxon': 'NCBITaxon:10090'}, 'aliases': ['mm39']},
    "GRCM38": {'description': 'Genome Reference Consortium Mouse Build 38 (Mus musculus), released 2011', 'meaning': 'insdc.gca:GCA_000001635.2', 'annotations': {'ucsc_name': 'mm10', 'refseq_accession': 'GCF_000001635.20', 'taxon': 'NCBITaxon:10090'}, 'aliases': ['mm10']},
    "MRATBN7_2": {'description': 'Rat (Rattus norvegicus) reference assembly mRatBN7.2, released 2020', 'meaning': 'insdc.gca:GCA_015227675.2', 'annotations': {'ucsc_name': 'rn7', 'refseq_accession': 'GCF_015227675.2', 'taxon': 'NCBITaxon:10116'}, 'aliases': ['rn7', 'mRatBN7.2']},
    "RNOR_6_0": {'description': 'Rat (Rattus norvegicus) reference assembly Rnor_6.0, released 2014', 'meaning': 'insdc.gca:GCA_000001895.4', 'annotations': {'ucsc_name': 'rn6', 'refseq_accession': 'GCF_000001895.5', 'taxon': 'NCBITaxon:10116'}, 'aliases': ['rn6', 'Rnor_6.0']},
    "GRCZ11": {'description': 'Genome Reference Consortium Zebrafish Build 11 (Danio rerio), released 2017', 'meaning': 'insdc.gca:GCA_000002035.4', 'annotations': {'ucsc_name': 'danRer11', 'refseq_accession': 'GCF_000002035.6', 'taxon': 'NCBITaxon:7955'}, 'aliases': ['danRer11']},
    "GRCZ10": {'description': 'Genome Reference Consortium Zebrafish Build 10 (Danio rerio), released 2014', 'meaning': 'insdc.gca:GCA_000002035.3', 'annotations': {'ucsc_name': 'danRer10', 'refseq_accession': 'GCF_000002035.5', 'taxon': 'NCBITaxon:7955'}, 'aliases': ['danRer10']},
    "GRCG6A": {'description': 'Genome Reference Consortium Chicken Build 6a (Gallus gallus), released 2018', 'meaning': 'insdc.gca:GCA_000002315.5', 'annotations': {'ucsc_name': 'galGal6', 'refseq_accession': 'GCF_000002315.6', 'taxon': 'NCBITaxon:9031'}, 'aliases': ['galGal6']},
    "WBCEL235": {'description': 'WormBase Caenorhabditis elegans reference assembly WBcel235, released 2013', 'meaning': 'insdc.gca:GCA_000002985.3', 'annotations': {'ucsc_name': 'ce11', 'refseq_accession': 'GCF_000002985.6', 'taxon': 'NCBITaxon:6239'}, 'aliases': ['ce11']},
    "BDGP6": {'description': 'Drosophila melanogaster reference assembly, Release 6 plus ISO1 mitochondrial genome', 'meaning': 'insdc.gca:GCA_000001215.4', 'annotations': {'ucsc_name': 'dm6', 'refseq_accession': 'GCF_000001215.4', 'taxon': 'NCBITaxon:7227'}, 'aliases': ['dm6', 'Release 6 plus ISO1 MT']},
    "CALLITHRIX_JACCHUS_CJ1700_1_1": {'description': 'Common marmoset (Callithrix jacchus) reference assembly cj1700_1.1, released 2019', 'meaning': 'insdc.gca:GCA_009663435.2', 'annotations': {'ucsc_name': 'calJac4', 'refseq_accession': 'GCF_009663435.1', 'taxon': 'NCBITaxon:9483'}, 'aliases': ['calJac4', 'Callithrix_jacchus_cj1700_1.1']},
}

class HumanChromosome(RichEnum):
    """
    Nuclear and mitochondrial chromosomes of Homo sapiens (human), as represented in the Monochrom Ontology (CHR). Sequence lengths and accessions are from the UCSC hg38 assembly.
    """
    # Enum members
    CHR1 = "CHR1"
    CHR2 = "CHR2"
    CHR3 = "CHR3"
    CHR4 = "CHR4"
    CHR5 = "CHR5"
    CHR6 = "CHR6"
    CHR7 = "CHR7"
    CHR8 = "CHR8"
    CHR9 = "CHR9"
    CHR10 = "CHR10"
    CHR11 = "CHR11"
    CHR12 = "CHR12"
    CHR13 = "CHR13"
    CHR14 = "CHR14"
    CHR15 = "CHR15"
    CHR16 = "CHR16"
    CHR17 = "CHR17"
    CHR18 = "CHR18"
    CHR19 = "CHR19"
    CHR20 = "CHR20"
    CHR21 = "CHR21"
    CHR22 = "CHR22"
    CHRX = "CHRX"
    CHRY = "CHRY"
    CHRM = "CHRM"

# Set metadata after class creation
HumanChromosome._metadata = {
    "CHR1": {'description': 'chromosome 1 (Human)', 'meaning': 'CHR:9606-chr1', 'annotations': {'refseq_accession': 'NC_000001.11', 'genbank_accession': 'CM000663.2', 'length_bp': 248956422}, 'aliases': ['chr1']},
    "CHR2": {'description': 'chromosome 2 (Human)', 'meaning': 'CHR:9606-chr2', 'annotations': {'refseq_accession': 'NC_000002.12', 'genbank_accession': 'CM000664.2', 'length_bp': 242193529}, 'aliases': ['chr2']},
    "CHR3": {'description': 'chromosome 3 (Human)', 'meaning': 'CHR:9606-chr3', 'annotations': {'refseq_accession': 'NC_000003.12', 'genbank_accession': 'CM000665.2', 'length_bp': 198295559}, 'aliases': ['chr3']},
    "CHR4": {'description': 'chromosome 4 (Human)', 'meaning': 'CHR:9606-chr4', 'annotations': {'refseq_accession': 'NC_000004.12', 'genbank_accession': 'CM000666.2', 'length_bp': 190214555}, 'aliases': ['chr4']},
    "CHR5": {'description': 'chromosome 5 (Human)', 'meaning': 'CHR:9606-chr5', 'annotations': {'refseq_accession': 'NC_000005.10', 'genbank_accession': 'CM000667.2', 'length_bp': 181538259}, 'aliases': ['chr5']},
    "CHR6": {'description': 'chromosome 6 (Human)', 'meaning': 'CHR:9606-chr6', 'annotations': {'refseq_accession': 'NC_000006.12', 'genbank_accession': 'CM000668.2', 'length_bp': 170805979}, 'aliases': ['chr6']},
    "CHR7": {'description': 'chromosome 7 (Human)', 'meaning': 'CHR:9606-chr7', 'annotations': {'refseq_accession': 'NC_000007.14', 'genbank_accession': 'CM000669.2', 'length_bp': 159345973}, 'aliases': ['chr7']},
    "CHR8": {'description': 'chromosome 8 (Human)', 'meaning': 'CHR:9606-chr8', 'annotations': {'refseq_accession': 'NC_000008.11', 'genbank_accession': 'CM000670.2', 'length_bp': 145138636}, 'aliases': ['chr8']},
    "CHR9": {'description': 'chromosome 9 (Human)', 'meaning': 'CHR:9606-chr9', 'annotations': {'refseq_accession': 'NC_000009.12', 'genbank_accession': 'CM000671.2', 'length_bp': 138394717}, 'aliases': ['chr9']},
    "CHR10": {'description': 'chromosome 10 (Human)', 'meaning': 'CHR:9606-chr10', 'annotations': {'refseq_accession': 'NC_000010.11', 'genbank_accession': 'CM000672.2', 'length_bp': 133797422}, 'aliases': ['chr10']},
    "CHR11": {'description': 'chromosome 11 (Human)', 'meaning': 'CHR:9606-chr11', 'annotations': {'refseq_accession': 'NC_000011.10', 'genbank_accession': 'CM000673.2', 'length_bp': 135086622}, 'aliases': ['chr11']},
    "CHR12": {'description': 'chromosome 12 (Human)', 'meaning': 'CHR:9606-chr12', 'annotations': {'refseq_accession': 'NC_000012.12', 'genbank_accession': 'CM000674.2', 'length_bp': 133275309}, 'aliases': ['chr12']},
    "CHR13": {'description': 'chromosome 13 (Human)', 'meaning': 'CHR:9606-chr13', 'annotations': {'refseq_accession': 'NC_000013.11', 'genbank_accession': 'CM000675.2', 'length_bp': 114364328}, 'aliases': ['chr13']},
    "CHR14": {'description': 'chromosome 14 (Human)', 'meaning': 'CHR:9606-chr14', 'annotations': {'refseq_accession': 'NC_000014.9', 'genbank_accession': 'CM000676.2', 'length_bp': 107043718}, 'aliases': ['chr14']},
    "CHR15": {'description': 'chromosome 15 (Human)', 'meaning': 'CHR:9606-chr15', 'annotations': {'refseq_accession': 'NC_000015.10', 'genbank_accession': 'CM000677.2', 'length_bp': 101991189}, 'aliases': ['chr15']},
    "CHR16": {'description': 'chromosome 16 (Human)', 'meaning': 'CHR:9606-chr16', 'annotations': {'refseq_accession': 'NC_000016.10', 'genbank_accession': 'CM000678.2', 'length_bp': 90338345}, 'aliases': ['chr16']},
    "CHR17": {'description': 'chromosome 17 (Human)', 'meaning': 'CHR:9606-chr17', 'annotations': {'refseq_accession': 'NC_000017.11', 'genbank_accession': 'CM000679.2', 'length_bp': 83257441}, 'aliases': ['chr17']},
    "CHR18": {'description': 'chromosome 18 (Human)', 'meaning': 'CHR:9606-chr18', 'annotations': {'refseq_accession': 'NC_000018.10', 'genbank_accession': 'CM000680.2', 'length_bp': 80373285}, 'aliases': ['chr18']},
    "CHR19": {'description': 'chromosome 19 (Human)', 'meaning': 'CHR:9606-chr19', 'annotations': {'refseq_accession': 'NC_000019.10', 'genbank_accession': 'CM000681.2', 'length_bp': 58617616}, 'aliases': ['chr19']},
    "CHR20": {'description': 'chromosome 20 (Human)', 'meaning': 'CHR:9606-chr20', 'annotations': {'refseq_accession': 'NC_000020.11', 'genbank_accession': 'CM000682.2', 'length_bp': 64444167}, 'aliases': ['chr20']},
    "CHR21": {'description': 'chromosome 21 (Human)', 'meaning': 'CHR:9606-chr21', 'annotations': {'refseq_accession': 'NC_000021.9', 'genbank_accession': 'CM000683.2', 'length_bp': 46709983}, 'aliases': ['chr21']},
    "CHR22": {'description': 'chromosome 22 (Human)', 'meaning': 'CHR:9606-chr22', 'annotations': {'refseq_accession': 'NC_000022.11', 'genbank_accession': 'CM000684.2', 'length_bp': 50818468}, 'aliases': ['chr22']},
    "CHRX": {'description': 'chromosome X (Human)', 'meaning': 'CHR:9606-chrX', 'annotations': {'refseq_accession': 'NC_000023.11', 'genbank_accession': 'CM000685.2', 'length_bp': 156040895}, 'aliases': ['chrX']},
    "CHRY": {'description': 'chromosome Y (Human)', 'meaning': 'CHR:9606-chrY', 'annotations': {'refseq_accession': 'NC_000024.10', 'genbank_accession': 'CM000686.2', 'length_bp': 57227415}, 'aliases': ['chrY']},
    "CHRM": {'description': 'chromosome M (Human)', 'meaning': 'CHR:9606-chrM', 'annotations': {'refseq_accession': 'NC_012920.1', 'genbank_accession': 'J01415.2', 'length_bp': 16569}, 'aliases': ['chrM', 'MT', 'chrMT']},
}

class MouseChromosome(RichEnum):
    """
    Nuclear and mitochondrial chromosomes of Mus musculus (mouse), as represented in the Monochrom Ontology (CHR). Sequence lengths and accessions are from the UCSC mm39 assembly.
    """
    # Enum members
    CHR1 = "CHR1"
    CHR2 = "CHR2"
    CHR3 = "CHR3"
    CHR4 = "CHR4"
    CHR5 = "CHR5"
    CHR6 = "CHR6"
    CHR7 = "CHR7"
    CHR8 = "CHR8"
    CHR9 = "CHR9"
    CHR10 = "CHR10"
    CHR11 = "CHR11"
    CHR12 = "CHR12"
    CHR13 = "CHR13"
    CHR14 = "CHR14"
    CHR15 = "CHR15"
    CHR16 = "CHR16"
    CHR17 = "CHR17"
    CHR18 = "CHR18"
    CHR19 = "CHR19"
    CHRX = "CHRX"
    CHRY = "CHRY"
    CHRM = "CHRM"

# Set metadata after class creation
MouseChromosome._metadata = {
    "CHR1": {'description': 'chromosome 1 (Mouse)', 'meaning': 'CHR:10090-chr1', 'annotations': {'refseq_accession': 'NC_000067.7', 'genbank_accession': 'CM000994.3', 'length_bp': 195154279}, 'aliases': ['chr1']},
    "CHR2": {'description': 'chromosome 2 (Mouse)', 'meaning': 'CHR:10090-chr2', 'annotations': {'refseq_accession': 'NC_000068.8', 'genbank_accession': 'CM000995.3', 'length_bp': 181755017}, 'aliases': ['chr2']},
    "CHR3": {'description': 'chromosome 3 (Mouse)', 'meaning': 'CHR:10090-chr3', 'annotations': {'refseq_accession': 'NC_000069.7', 'genbank_accession': 'CM000996.3', 'length_bp': 159745316}, 'aliases': ['chr3']},
    "CHR4": {'description': 'chromosome 4 (Mouse)', 'meaning': 'CHR:10090-chr4', 'annotations': {'refseq_accession': 'NC_000070.7', 'genbank_accession': 'CM000997.3', 'length_bp': 156860686}, 'aliases': ['chr4']},
    "CHR5": {'description': 'chromosome 5 (Mouse)', 'meaning': 'CHR:10090-chr5', 'annotations': {'refseq_accession': 'NC_000071.7', 'genbank_accession': 'CM000998.3', 'length_bp': 151758149}, 'aliases': ['chr5']},
    "CHR6": {'description': 'chromosome 6 (Mouse)', 'meaning': 'CHR:10090-chr6', 'annotations': {'refseq_accession': 'NC_000072.7', 'genbank_accession': 'CM000999.3', 'length_bp': 149588044}, 'aliases': ['chr6']},
    "CHR7": {'description': 'chromosome 7 (Mouse)', 'meaning': 'CHR:10090-chr7', 'annotations': {'refseq_accession': 'NC_000073.7', 'genbank_accession': 'CM001000.3', 'length_bp': 144995196}, 'aliases': ['chr7']},
    "CHR8": {'description': 'chromosome 8 (Mouse)', 'meaning': 'CHR:10090-chr8', 'annotations': {'refseq_accession': 'NC_000074.7', 'genbank_accession': 'CM001001.3', 'length_bp': 130127694}, 'aliases': ['chr8']},
    "CHR9": {'description': 'chromosome 9 (Mouse)', 'meaning': 'CHR:10090-chr9', 'annotations': {'refseq_accession': 'NC_000075.7', 'genbank_accession': 'CM001002.3', 'length_bp': 124359700}, 'aliases': ['chr9']},
    "CHR10": {'description': 'chromosome 10 (Mouse)', 'meaning': 'CHR:10090-chr10', 'annotations': {'refseq_accession': 'NC_000076.7', 'genbank_accession': 'CM001003.3', 'length_bp': 130530862}, 'aliases': ['chr10']},
    "CHR11": {'description': 'chromosome 11 (Mouse)', 'meaning': 'CHR:10090-chr11', 'annotations': {'refseq_accession': 'NC_000077.7', 'genbank_accession': 'CM001004.3', 'length_bp': 121973369}, 'aliases': ['chr11']},
    "CHR12": {'description': 'chromosome 12 (Mouse)', 'meaning': 'CHR:10090-chr12', 'annotations': {'refseq_accession': 'NC_000078.7', 'genbank_accession': 'CM001005.3', 'length_bp': 120092757}, 'aliases': ['chr12']},
    "CHR13": {'description': 'chromosome 13 (Mouse)', 'meaning': 'CHR:10090-chr13', 'annotations': {'refseq_accession': 'NC_000079.7', 'genbank_accession': 'CM001006.3', 'length_bp': 120883175}, 'aliases': ['chr13']},
    "CHR14": {'description': 'chromosome 14 (Mouse)', 'meaning': 'CHR:10090-chr14', 'annotations': {'refseq_accession': 'NC_000080.7', 'genbank_accession': 'CM001007.3', 'length_bp': 125139656}, 'aliases': ['chr14']},
    "CHR15": {'description': 'chromosome 15 (Mouse)', 'meaning': 'CHR:10090-chr15', 'annotations': {'refseq_accession': 'NC_000081.7', 'genbank_accession': 'CM001008.3', 'length_bp': 104073951}, 'aliases': ['chr15']},
    "CHR16": {'description': 'chromosome 16 (Mouse)', 'meaning': 'CHR:10090-chr16', 'annotations': {'refseq_accession': 'NC_000082.7', 'genbank_accession': 'CM001009.3', 'length_bp': 98008968}, 'aliases': ['chr16']},
    "CHR17": {'description': 'chromosome 17 (Mouse)', 'meaning': 'CHR:10090-chr17', 'annotations': {'refseq_accession': 'NC_000083.7', 'genbank_accession': 'CM001010.3', 'length_bp': 95294699}, 'aliases': ['chr17']},
    "CHR18": {'description': 'chromosome 18 (Mouse)', 'meaning': 'CHR:10090-chr18', 'annotations': {'refseq_accession': 'NC_000084.7', 'genbank_accession': 'CM001011.3', 'length_bp': 90720763}, 'aliases': ['chr18']},
    "CHR19": {'description': 'chromosome 19 (Mouse)', 'meaning': 'CHR:10090-chr19', 'annotations': {'refseq_accession': 'NC_000085.7', 'genbank_accession': 'CM001012.3', 'length_bp': 61420004}, 'aliases': ['chr19']},
    "CHRX": {'description': 'chromosome X (Mouse)', 'meaning': 'CHR:10090-chrX', 'annotations': {'refseq_accession': 'NC_000086.8', 'genbank_accession': 'CM001013.3', 'length_bp': 169476592}, 'aliases': ['chrX']},
    "CHRY": {'description': 'chromosome Y (Mouse)', 'meaning': 'CHR:10090-chrY', 'annotations': {'refseq_accession': 'NC_000087.8', 'genbank_accession': 'CM001014.3', 'length_bp': 91455967}, 'aliases': ['chrY']},
    "CHRM": {'description': 'chromosome M (Mouse)', 'meaning': 'CHR:10090-chrM', 'annotations': {'refseq_accession': 'NC_005089.1', 'genbank_accession': 'AY172335.1', 'length_bp': 16299}, 'aliases': ['chrM', 'MT', 'chrMT']},
}

class RatChromosome(RichEnum):
    """
    Nuclear and mitochondrial chromosomes of Rattus norvegicus (rat), as represented in the Monochrom Ontology (CHR). Sequence lengths and accessions are from the UCSC rn6 assembly.
    """
    # Enum members
    CHR1 = "CHR1"
    CHR2 = "CHR2"
    CHR3 = "CHR3"
    CHR4 = "CHR4"
    CHR5 = "CHR5"
    CHR6 = "CHR6"
    CHR7 = "CHR7"
    CHR8 = "CHR8"
    CHR9 = "CHR9"
    CHR10 = "CHR10"
    CHR11 = "CHR11"
    CHR12 = "CHR12"
    CHR13 = "CHR13"
    CHR14 = "CHR14"
    CHR15 = "CHR15"
    CHR16 = "CHR16"
    CHR17 = "CHR17"
    CHR18 = "CHR18"
    CHR19 = "CHR19"
    CHR20 = "CHR20"
    CHRX = "CHRX"
    CHRY = "CHRY"
    CHRM = "CHRM"

# Set metadata after class creation
RatChromosome._metadata = {
    "CHR1": {'description': 'chromosome 1 (Rat)', 'meaning': 'CHR:10116-chr1', 'annotations': {'refseq_accession': 'NC_005100.4', 'genbank_accession': 'CM000072.5', 'length_bp': 282763074}, 'aliases': ['chr1']},
    "CHR2": {'description': 'chromosome 2 (Rat)', 'meaning': 'CHR:10116-chr2', 'annotations': {'refseq_accession': 'NC_005101.4', 'genbank_accession': 'CM000073.5', 'length_bp': 266435125}, 'aliases': ['chr2']},
    "CHR3": {'description': 'chromosome 3 (Rat)', 'meaning': 'CHR:10116-chr3', 'annotations': {'refseq_accession': 'NC_005102.4', 'genbank_accession': 'CM000074.5', 'length_bp': 177699992}, 'aliases': ['chr3']},
    "CHR4": {'description': 'chromosome 4 (Rat)', 'meaning': 'CHR:10116-chr4', 'annotations': {'refseq_accession': 'NC_005103.4', 'genbank_accession': 'CM000075.5', 'length_bp': 184226339}, 'aliases': ['chr4']},
    "CHR5": {'description': 'chromosome 5 (Rat)', 'meaning': 'CHR:10116-chr5', 'annotations': {'refseq_accession': 'NC_005104.4', 'genbank_accession': 'CM000076.5', 'length_bp': 173707219}, 'aliases': ['chr5']},
    "CHR6": {'description': 'chromosome 6 (Rat)', 'meaning': 'CHR:10116-chr6', 'annotations': {'refseq_accession': 'NC_005105.4', 'genbank_accession': 'CM000077.5', 'length_bp': 147991367}, 'aliases': ['chr6']},
    "CHR7": {'description': 'chromosome 7 (Rat)', 'meaning': 'CHR:10116-chr7', 'annotations': {'refseq_accession': 'NC_005106.4', 'genbank_accession': 'CM000078.5', 'length_bp': 145729302}, 'aliases': ['chr7']},
    "CHR8": {'description': 'chromosome 8 (Rat)', 'meaning': 'CHR:10116-chr8', 'annotations': {'refseq_accession': 'NC_005107.4', 'genbank_accession': 'CM000079.5', 'length_bp': 133307652}, 'aliases': ['chr8']},
    "CHR9": {'description': 'chromosome 9 (Rat)', 'meaning': 'CHR:10116-chr9', 'annotations': {'refseq_accession': 'NC_005108.4', 'genbank_accession': 'CM000080.5', 'length_bp': 122095297}, 'aliases': ['chr9']},
    "CHR10": {'description': 'chromosome 10 (Rat)', 'meaning': 'CHR:10116-chr10', 'annotations': {'refseq_accession': 'NC_005109.4', 'genbank_accession': 'CM000081.5', 'length_bp': 112626471}, 'aliases': ['chr10']},
    "CHR11": {'description': 'chromosome 11 (Rat)', 'meaning': 'CHR:10116-chr11', 'annotations': {'refseq_accession': 'NC_005110.4', 'genbank_accession': 'CM000082.5', 'length_bp': 90463843}, 'aliases': ['chr11']},
    "CHR12": {'description': 'chromosome 12 (Rat)', 'meaning': 'CHR:10116-chr12', 'annotations': {'refseq_accession': 'NC_005111.4', 'genbank_accession': 'CM000083.5', 'length_bp': 52716770}, 'aliases': ['chr12']},
    "CHR13": {'description': 'chromosome 13 (Rat)', 'meaning': 'CHR:10116-chr13', 'annotations': {'refseq_accession': 'NC_005112.4', 'genbank_accession': 'CM000084.5', 'length_bp': 114033958}, 'aliases': ['chr13']},
    "CHR14": {'description': 'chromosome 14 (Rat)', 'meaning': 'CHR:10116-chr14', 'annotations': {'refseq_accession': 'NC_005113.4', 'genbank_accession': 'CM000085.5', 'length_bp': 115493446}, 'aliases': ['chr14']},
    "CHR15": {'description': 'chromosome 15 (Rat)', 'meaning': 'CHR:10116-chr15', 'annotations': {'refseq_accession': 'NC_005114.4', 'genbank_accession': 'CM000086.5', 'length_bp': 111246239}, 'aliases': ['chr15']},
    "CHR16": {'description': 'chromosome 16 (Rat)', 'meaning': 'CHR:10116-chr16', 'annotations': {'refseq_accession': 'NC_005115.4', 'genbank_accession': 'CM000087.5', 'length_bp': 90668790}, 'aliases': ['chr16']},
    "CHR17": {'description': 'chromosome 17 (Rat)', 'meaning': 'CHR:10116-chr17', 'annotations': {'refseq_accession': 'NC_005116.4', 'genbank_accession': 'CM000088.5', 'length_bp': 90843779}, 'aliases': ['chr17']},
    "CHR18": {'description': 'chromosome 18 (Rat)', 'meaning': 'CHR:10116-chr18', 'annotations': {'refseq_accession': 'NC_005117.4', 'genbank_accession': 'CM000089.5', 'length_bp': 88201929}, 'aliases': ['chr18']},
    "CHR19": {'description': 'chromosome 19 (Rat)', 'meaning': 'CHR:10116-chr19', 'annotations': {'refseq_accession': 'NC_005118.4', 'genbank_accession': 'CM000090.5', 'length_bp': 62275575}, 'aliases': ['chr19']},
    "CHR20": {'description': 'chromosome 20 (Rat)', 'meaning': 'CHR:10116-chr20', 'annotations': {'refseq_accession': 'NC_005119.4', 'genbank_accession': 'CM000091.5', 'length_bp': 56205956}, 'aliases': ['chr20']},
    "CHRX": {'description': 'chromosome X (Rat)', 'meaning': 'CHR:10116-chrX', 'annotations': {'refseq_accession': 'NC_005120.4', 'genbank_accession': 'CM000092.5', 'length_bp': 159970021}, 'aliases': ['chrX']},
    "CHRY": {'description': 'chromosome Y (Rat)', 'meaning': 'CHR:10116-chrY', 'annotations': {'refseq_accession': 'NC_024475.1', 'genbank_accession': 'CM002824.1', 'length_bp': 3310458}, 'aliases': ['chrY']},
    "CHRM": {'description': 'chromosome M (Rat)', 'meaning': 'CHR:10116-chrM', 'annotations': {'refseq_accession': 'NC_001665.2', 'genbank_accession': 'AY172581.1', 'length_bp': 16313}, 'aliases': ['chrM', 'MT', 'chrMT']},
}

class ZebrafishChromosome(RichEnum):
    """
    Nuclear and mitochondrial chromosomes of Danio rerio (zebrafish), as represented in the Monochrom Ontology (CHR). Sequence lengths and accessions are from the UCSC danRer11 assembly.
    """
    # Enum members
    CHR1 = "CHR1"
    CHR2 = "CHR2"
    CHR3 = "CHR3"
    CHR4 = "CHR4"
    CHR5 = "CHR5"
    CHR6 = "CHR6"
    CHR7 = "CHR7"
    CHR8 = "CHR8"
    CHR9 = "CHR9"
    CHR10 = "CHR10"
    CHR11 = "CHR11"
    CHR12 = "CHR12"
    CHR13 = "CHR13"
    CHR14 = "CHR14"
    CHR15 = "CHR15"
    CHR16 = "CHR16"
    CHR17 = "CHR17"
    CHR18 = "CHR18"
    CHR19 = "CHR19"
    CHR20 = "CHR20"
    CHR21 = "CHR21"
    CHR22 = "CHR22"
    CHR23 = "CHR23"
    CHR24 = "CHR24"
    CHR25 = "CHR25"
    CHRM = "CHRM"

# Set metadata after class creation
ZebrafishChromosome._metadata = {
    "CHR1": {'description': 'chromosome 1 (Danio rerio)', 'meaning': 'CHR:7955-chr1', 'annotations': {'refseq_accession': 'NC_007112.7', 'genbank_accession': 'CM002885.2', 'length_bp': 59578282}, 'aliases': ['chr1']},
    "CHR2": {'description': 'chromosome 2 (Danio rerio)', 'meaning': 'CHR:7955-chr2', 'annotations': {'refseq_accession': 'NC_007113.7', 'genbank_accession': 'CM002886.2', 'length_bp': 59640629}, 'aliases': ['chr2']},
    "CHR3": {'description': 'chromosome 3 (Danio rerio)', 'meaning': 'CHR:7955-chr3', 'annotations': {'refseq_accession': 'NC_007114.7', 'genbank_accession': 'CM002887.2', 'length_bp': 62628489}, 'aliases': ['chr3']},
    "CHR4": {'description': 'chromosome 4 (Danio rerio)', 'meaning': 'CHR:7955-chr4', 'annotations': {'refseq_accession': 'NC_007115.7', 'genbank_accession': 'CM002888.2', 'length_bp': 78093715}, 'aliases': ['chr4']},
    "CHR5": {'description': 'chromosome 5 (Danio rerio)', 'meaning': 'CHR:7955-chr5', 'annotations': {'refseq_accession': 'NC_007116.7', 'genbank_accession': 'CM002889.2', 'length_bp': 72500376}, 'aliases': ['chr5']},
    "CHR6": {'description': 'chromosome 6 (Danio rerio)', 'meaning': 'CHR:7955-chr6', 'annotations': {'refseq_accession': 'NC_007117.7', 'genbank_accession': 'CM002890.2', 'length_bp': 60270059}, 'aliases': ['chr6']},
    "CHR7": {'description': 'chromosome 7 (Danio rerio)', 'meaning': 'CHR:7955-chr7', 'annotations': {'refseq_accession': 'NC_007118.7', 'genbank_accession': 'CM002891.2', 'length_bp': 74282399}, 'aliases': ['chr7']},
    "CHR8": {'description': 'chromosome 8 (Danio rerio)', 'meaning': 'CHR:7955-chr8', 'annotations': {'refseq_accession': 'NC_007119.7', 'genbank_accession': 'CM002892.2', 'length_bp': 54304671}, 'aliases': ['chr8']},
    "CHR9": {'description': 'chromosome 9 (Danio rerio)', 'meaning': 'CHR:7955-chr9', 'annotations': {'refseq_accession': 'NC_007120.7', 'genbank_accession': 'CM002893.2', 'length_bp': 56459846}, 'aliases': ['chr9']},
    "CHR10": {'description': 'chromosome 10 (Danio rerio)', 'meaning': 'CHR:7955-chr10', 'annotations': {'refseq_accession': 'NC_007121.7', 'genbank_accession': 'CM002894.2', 'length_bp': 45420867}, 'aliases': ['chr10']},
    "CHR11": {'description': 'chromosome 11 (Danio rerio)', 'meaning': 'CHR:7955-chr11', 'annotations': {'refseq_accession': 'NC_007122.7', 'genbank_accession': 'CM002895.2', 'length_bp': 45484837}, 'aliases': ['chr11']},
    "CHR12": {'description': 'chromosome 12 (Danio rerio)', 'meaning': 'CHR:7955-chr12', 'annotations': {'refseq_accession': 'NC_007123.7', 'genbank_accession': 'CM002896.2', 'length_bp': 49182954}, 'aliases': ['chr12']},
    "CHR13": {'description': 'chromosome 13 (Danio rerio)', 'meaning': 'CHR:7955-chr13', 'annotations': {'refseq_accession': 'NC_007124.7', 'genbank_accession': 'CM002897.2', 'length_bp': 52186027}, 'aliases': ['chr13']},
    "CHR14": {'description': 'chromosome 14 (Danio rerio)', 'meaning': 'CHR:7955-chr14', 'annotations': {'refseq_accession': 'NC_007125.7', 'genbank_accession': 'CM002898.2', 'length_bp': 52660232}, 'aliases': ['chr14']},
    "CHR15": {'description': 'chromosome 15 (Danio rerio)', 'meaning': 'CHR:7955-chr15', 'annotations': {'refseq_accession': 'NC_007126.7', 'genbank_accession': 'CM002899.2', 'length_bp': 48040578}, 'aliases': ['chr15']},
    "CHR16": {'description': 'chromosome 16 (Danio rerio)', 'meaning': 'CHR:7955-chr16', 'annotations': {'refseq_accession': 'NC_007127.7', 'genbank_accession': 'CM002900.2', 'length_bp': 55266484}, 'aliases': ['chr16']},
    "CHR17": {'description': 'chromosome 17 (Danio rerio)', 'meaning': 'CHR:7955-chr17', 'annotations': {'refseq_accession': 'NC_007128.7', 'genbank_accession': 'CM002901.2', 'length_bp': 53461100}, 'aliases': ['chr17']},
    "CHR18": {'description': 'chromosome 18 (Danio rerio)', 'meaning': 'CHR:7955-chr18', 'annotations': {'refseq_accession': 'NC_007129.7', 'genbank_accession': 'CM002902.2', 'length_bp': 51023478}, 'aliases': ['chr18']},
    "CHR19": {'description': 'chromosome 19 (Danio rerio)', 'meaning': 'CHR:7955-chr19', 'annotations': {'refseq_accession': 'NC_007130.7', 'genbank_accession': 'CM002903.2', 'length_bp': 48449771}, 'aliases': ['chr19']},
    "CHR20": {'description': 'chromosome 20 (Danio rerio)', 'meaning': 'CHR:7955-chr20', 'annotations': {'refseq_accession': 'NC_007131.7', 'genbank_accession': 'CM002904.2', 'length_bp': 55201332}, 'aliases': ['chr20']},
    "CHR21": {'description': 'chromosome 21 (Danio rerio)', 'meaning': 'CHR:7955-chr21', 'annotations': {'refseq_accession': 'NC_007132.7', 'genbank_accession': 'CM002905.2', 'length_bp': 45934066}, 'aliases': ['chr21']},
    "CHR22": {'description': 'chromosome 22 (Danio rerio)', 'meaning': 'CHR:7955-chr22', 'annotations': {'refseq_accession': 'NC_007133.7', 'genbank_accession': 'CM002906.2', 'length_bp': 39133080}, 'aliases': ['chr22']},
    "CHR23": {'description': 'chromosome 23 (Danio rerio)', 'meaning': 'CHR:7955-chr23', 'annotations': {'refseq_accession': 'NC_007134.7', 'genbank_accession': 'CM002907.2', 'length_bp': 46223584}, 'aliases': ['chr23']},
    "CHR24": {'description': 'chromosome 24 (Danio rerio)', 'meaning': 'CHR:7955-chr24', 'annotations': {'refseq_accession': 'NC_007135.7', 'genbank_accession': 'CM002908.2', 'length_bp': 42172926}, 'aliases': ['chr24']},
    "CHR25": {'description': 'chromosome 25 (Danio rerio)', 'meaning': 'CHR:7955-chr25', 'annotations': {'refseq_accession': 'NC_007136.7', 'genbank_accession': 'CM002909.2', 'length_bp': 37502051}, 'aliases': ['chr25']},
    "CHRM": {'description': 'chromosome M (Danio rerio)', 'meaning': 'CHR:7955-chrM', 'annotations': {'refseq_accession': 'NC_002333.2', 'genbank_accession': 'AC024175.3', 'length_bp': 16596}, 'aliases': ['chrM', 'MT', 'chrMT']},
}

class ChickenChromosome(RichEnum):
    """
    Nuclear and mitochondrial chromosomes of Gallus gallus (chicken), as represented in the Monochrom Ontology (CHR). Sequence lengths and accessions are from the UCSC galGal6 assembly.
    """
    # Enum members
    CHR1 = "CHR1"
    CHR2 = "CHR2"
    CHR3 = "CHR3"
    CHR4 = "CHR4"
    CHR5 = "CHR5"
    CHR6 = "CHR6"
    CHR7 = "CHR7"
    CHR8 = "CHR8"
    CHR9 = "CHR9"
    CHR10 = "CHR10"
    CHR11 = "CHR11"
    CHR12 = "CHR12"
    CHR13 = "CHR13"
    CHR14 = "CHR14"
    CHR15 = "CHR15"
    CHR16 = "CHR16"
    CHR17 = "CHR17"
    CHR18 = "CHR18"
    CHR19 = "CHR19"
    CHR20 = "CHR20"
    CHR21 = "CHR21"
    CHR22 = "CHR22"
    CHR23 = "CHR23"
    CHR24 = "CHR24"
    CHR25 = "CHR25"
    CHR26 = "CHR26"
    CHR27 = "CHR27"
    CHR28 = "CHR28"
    CHR30 = "CHR30"
    CHR31 = "CHR31"
    CHR32 = "CHR32"
    CHR33 = "CHR33"
    CHRZ = "CHRZ"
    CHRW = "CHRW"
    CHRM = "CHRM"

# Set metadata after class creation
ChickenChromosome._metadata = {
    "CHR1": {'description': 'chromosome 1 (Chicken)', 'meaning': 'CHR:9031-chr1', 'annotations': {'refseq_accession': 'NC_006088.5', 'genbank_accession': 'CM000093.5', 'length_bp': 197608386}, 'aliases': ['chr1']},
    "CHR2": {'description': 'chromosome 2 (Chicken)', 'meaning': 'CHR:9031-chr2', 'annotations': {'refseq_accession': 'NC_006089.5', 'genbank_accession': 'CM000094.5', 'length_bp': 149682049}, 'aliases': ['chr2']},
    "CHR3": {'description': 'chromosome 3 (Chicken)', 'meaning': 'CHR:9031-chr3', 'annotations': {'refseq_accession': 'NC_006090.5', 'genbank_accession': 'CM000095.5', 'length_bp': 110838418}, 'aliases': ['chr3']},
    "CHR4": {'description': 'chromosome 4 (Chicken)', 'meaning': 'CHR:9031-chr4', 'annotations': {'refseq_accession': 'NC_006091.5', 'genbank_accession': 'CM000096.5', 'length_bp': 91315245}, 'aliases': ['chr4']},
    "CHR5": {'description': 'chromosome 5 (Chicken)', 'meaning': 'CHR:9031-chr5', 'annotations': {'refseq_accession': 'NC_006092.5', 'genbank_accession': 'CM000097.5', 'length_bp': 59809098}, 'aliases': ['chr5']},
    "CHR6": {'description': 'chromosome 6 (Chicken)', 'meaning': 'CHR:9031-chr6', 'annotations': {'refseq_accession': 'NC_006093.5', 'genbank_accession': 'CM000098.5', 'length_bp': 36374701}, 'aliases': ['chr6']},
    "CHR7": {'description': 'chromosome 7 (Chicken)', 'meaning': 'CHR:9031-chr7', 'annotations': {'refseq_accession': 'NC_006094.5', 'genbank_accession': 'CM000099.5', 'length_bp': 36742308}, 'aliases': ['chr7']},
    "CHR8": {'description': 'chromosome 8 (Chicken)', 'meaning': 'CHR:9031-chr8', 'annotations': {'refseq_accession': 'NC_006095.5', 'genbank_accession': 'CM000100.5', 'length_bp': 30219446}, 'aliases': ['chr8']},
    "CHR9": {'description': 'chromosome 9 (Chicken)', 'meaning': 'CHR:9031-chr9', 'annotations': {'refseq_accession': 'NC_006096.5', 'genbank_accession': 'CM000101.5', 'length_bp': 24153086}, 'aliases': ['chr9']},
    "CHR10": {'description': 'chromosome 10 (Chicken)', 'meaning': 'CHR:9031-chr10', 'annotations': {'refseq_accession': 'NC_006097.5', 'genbank_accession': 'CM000102.5', 'length_bp': 21119840}, 'aliases': ['chr10']},
    "CHR11": {'description': 'chromosome 11 (Chicken)', 'meaning': 'CHR:9031-chr11', 'annotations': {'refseq_accession': 'NC_006098.5', 'genbank_accession': 'CM000103.5', 'length_bp': 20200042}, 'aliases': ['chr11']},
    "CHR12": {'description': 'chromosome 12 (Chicken)', 'meaning': 'CHR:9031-chr12', 'annotations': {'refseq_accession': 'NC_006099.5', 'genbank_accession': 'CM000104.5', 'length_bp': 20387278}, 'aliases': ['chr12']},
    "CHR13": {'description': 'chromosome 13 (Chicken)', 'meaning': 'CHR:9031-chr13', 'annotations': {'refseq_accession': 'NC_006100.5', 'genbank_accession': 'CM000105.5', 'length_bp': 19166714}, 'aliases': ['chr13']},
    "CHR14": {'description': 'chromosome 14 (Chicken)', 'meaning': 'CHR:9031-chr14', 'annotations': {'refseq_accession': 'NC_006101.5', 'genbank_accession': 'CM000106.5', 'length_bp': 16219308}, 'aliases': ['chr14']},
    "CHR15": {'description': 'chromosome 15 (Chicken)', 'meaning': 'CHR:9031-chr15', 'annotations': {'refseq_accession': 'NC_006102.5', 'genbank_accession': 'CM000107.5', 'length_bp': 13062184}, 'aliases': ['chr15']},
    "CHR16": {'description': 'chromosome 16 (Chicken)', 'meaning': 'CHR:9031-chr16', 'annotations': {'refseq_accession': 'NC_006103.5', 'genbank_accession': 'CM000108.5', 'length_bp': 2844601}, 'aliases': ['chr16']},
    "CHR17": {'description': 'chromosome 17 (Chicken)', 'meaning': 'CHR:9031-chr17', 'annotations': {'refseq_accession': 'NC_006104.5', 'genbank_accession': 'CM000109.5', 'length_bp': 10762512}, 'aliases': ['chr17']},
    "CHR18": {'description': 'chromosome 18 (Chicken)', 'meaning': 'CHR:9031-chr18', 'annotations': {'refseq_accession': 'NC_006105.5', 'genbank_accession': 'CM000110.5', 'length_bp': 11373140}, 'aliases': ['chr18']},
    "CHR19": {'description': 'chromosome 19 (Chicken)', 'meaning': 'CHR:9031-chr19', 'annotations': {'refseq_accession': 'NC_006106.5', 'genbank_accession': 'CM000111.5', 'length_bp': 10323212}, 'aliases': ['chr19']},
    "CHR20": {'description': 'chromosome 20 (Chicken)', 'meaning': 'CHR:9031-chr20', 'annotations': {'refseq_accession': 'NC_006107.5', 'genbank_accession': 'CM000112.5', 'length_bp': 13897287}, 'aliases': ['chr20']},
    "CHR21": {'description': 'chromosome 21 (Chicken)', 'meaning': 'CHR:9031-chr21', 'annotations': {'refseq_accession': 'NC_006108.5', 'genbank_accession': 'CM000113.5', 'length_bp': 6844979}, 'aliases': ['chr21']},
    "CHR22": {'description': 'chromosome 22 (Chicken)', 'meaning': 'CHR:9031-chr22', 'annotations': {'refseq_accession': 'NC_006109.5', 'genbank_accession': 'CM000114.5', 'length_bp': 5459462}, 'aliases': ['chr22']},
    "CHR23": {'description': 'chromosome 23 (Chicken)', 'meaning': 'CHR:9031-chr23', 'annotations': {'refseq_accession': 'NC_006110.5', 'genbank_accession': 'CM000115.5', 'length_bp': 6149580}, 'aliases': ['chr23']},
    "CHR24": {'description': 'chromosome 24 (Chicken)', 'meaning': 'CHR:9031-chr24', 'annotations': {'refseq_accession': 'NC_006111.5', 'genbank_accession': 'CM000116.5', 'length_bp': 6491222}, 'aliases': ['chr24']},
    "CHR25": {'description': 'chromosome 25 (Chicken)', 'meaning': 'CHR:9031-chr25', 'annotations': {'refseq_accession': 'NC_006112.4', 'genbank_accession': 'CM000124.5', 'length_bp': 3980610}, 'aliases': ['chr25']},
    "CHR26": {'description': 'chromosome 26 (Chicken)', 'meaning': 'CHR:9031-chr26', 'annotations': {'refseq_accession': 'NC_006113.5', 'genbank_accession': 'CM000117.5', 'length_bp': 6055710}, 'aliases': ['chr26']},
    "CHR27": {'description': 'chromosome 27 (Chicken)', 'meaning': 'CHR:9031-chr27', 'annotations': {'refseq_accession': 'NC_006114.5', 'genbank_accession': 'CM000118.5', 'length_bp': 8080432}, 'aliases': ['chr27']},
    "CHR28": {'description': 'chromosome 28 (Chicken)', 'meaning': 'CHR:9031-chr28', 'annotations': {'refseq_accession': 'NC_006115.5', 'genbank_accession': 'CM000119.5', 'length_bp': 5116882}, 'aliases': ['chr28']},
    "CHR30": {'description': 'chromosome 30 (Chicken)', 'meaning': 'CHR:9031-chr30', 'annotations': {'refseq_accession': 'NC_028739.2', 'genbank_accession': 'CM003637.2', 'length_bp': 1818525}, 'aliases': ['chr30']},
    "CHR31": {'description': 'chromosome 31 (Chicken)', 'meaning': 'CHR:9031-chr31', 'annotations': {'refseq_accession': 'NC_028740.2', 'genbank_accession': 'CM003638.2', 'length_bp': 6153034}, 'aliases': ['chr31']},
    "CHR32": {'description': 'chromosome 32 (Chicken)', 'meaning': 'CHR:9031-chr32', 'annotations': {'refseq_accession': 'NC_006119.4', 'genbank_accession': 'CM000120.4', 'length_bp': 725831}, 'aliases': ['chr32']},
    "CHR33": {'description': 'chromosome 33 (Chicken)', 'meaning': 'CHR:9031-chr33', 'annotations': {'refseq_accession': 'NC_008465.4', 'genbank_accession': 'CM000123.5', 'length_bp': 7821666}, 'aliases': ['chr33']},
    "CHRZ": {'description': 'chromosome Z (Chicken)', 'meaning': 'CHR:9031-chrZ', 'annotations': {'refseq_accession': 'NC_006127.5', 'genbank_accession': 'CM000122.5', 'length_bp': 82529921}, 'aliases': ['chrZ']},
    "CHRW": {'description': 'chromosome W (Chicken)', 'meaning': 'CHR:9031-chrW', 'annotations': {'refseq_accession': 'NC_006126.5', 'genbank_accession': 'CM000121.5', 'length_bp': 6813114}, 'aliases': ['chrW']},
    "CHRM": {'description': 'chromosome M (Chicken)', 'meaning': 'CHR:9031-chrM', 'annotations': {'refseq_accession': 'NC_001323.1', 'genbank_accession': 'X52392.1', 'length_bp': 16775}, 'aliases': ['chrM', 'MT', 'chrMT']},
}

class CElegansChromosome(RichEnum):
    """
    Nuclear and mitochondrial chromosomes of Caenorhabditis elegans (C. elegans), as represented in the Monochrom Ontology (CHR). Sequence lengths and accessions are from the UCSC ce11 assembly.
    """
    # Enum members
    CHRI = "CHRI"
    CHRII = "CHRII"
    CHRIII = "CHRIII"
    CHRIV = "CHRIV"
    CHRV = "CHRV"
    CHRX = "CHRX"
    CHRM = "CHRM"

# Set metadata after class creation
CElegansChromosome._metadata = {
    "CHRI": {'description': 'chromosome I (C elegans)', 'meaning': 'CHR:6239-chrI', 'annotations': {'refseq_accession': 'NC_003279.8', 'length_bp': 15072434}, 'aliases': ['chrI']},
    "CHRII": {'description': 'chromosome II (C elegans)', 'meaning': 'CHR:6239-chrII', 'annotations': {'refseq_accession': 'NC_003280.10', 'length_bp': 15279421}, 'aliases': ['chrII']},
    "CHRIII": {'description': 'chromosome III (C elegans)', 'meaning': 'CHR:6239-chrIII', 'annotations': {'refseq_accession': 'NC_003281.10', 'length_bp': 13783801}, 'aliases': ['chrIII']},
    "CHRIV": {'description': 'chromosome IV (C elegans)', 'meaning': 'CHR:6239-chrIV', 'annotations': {'refseq_accession': 'NC_003282.8', 'length_bp': 17493829}, 'aliases': ['chrIV']},
    "CHRV": {'description': 'chromosome V (C elegans)', 'meaning': 'CHR:6239-chrV', 'annotations': {'refseq_accession': 'NC_003283.11', 'length_bp': 20924180}, 'aliases': ['chrV']},
    "CHRX": {'description': 'chromosome X (C elegans)', 'meaning': 'CHR:6239-chrX', 'annotations': {'refseq_accession': 'NC_003284.9', 'length_bp': 17718942}, 'aliases': ['chrX']},
    "CHRM": {'description': 'chromosome M (C elegans)', 'meaning': 'CHR:6239-chrM', 'annotations': {'refseq_accession': 'NC_001328.1', 'length_bp': 13794}, 'aliases': ['chrM', 'MT', 'chrMT']},
}

class MarmosetChromosome(RichEnum):
    """
    Nuclear and mitochondrial chromosomes of Callithrix jacchus (marmoset), as represented in the Monochrom Ontology (CHR). Sequence lengths and accessions are from the UCSC calJac4 assembly.
    """
    # Enum members
    CHR1 = "CHR1"
    CHR2 = "CHR2"
    CHR3 = "CHR3"
    CHR4 = "CHR4"
    CHR5 = "CHR5"
    CHR6 = "CHR6"
    CHR7 = "CHR7"
    CHR8 = "CHR8"
    CHR9 = "CHR9"
    CHR10 = "CHR10"
    CHR11 = "CHR11"
    CHR12 = "CHR12"
    CHR13 = "CHR13"
    CHR14 = "CHR14"
    CHR15 = "CHR15"
    CHR16 = "CHR16"
    CHR17 = "CHR17"
    CHR18 = "CHR18"
    CHR19 = "CHR19"
    CHR20 = "CHR20"
    CHR21 = "CHR21"
    CHR22 = "CHR22"
    CHRX = "CHRX"
    CHRY = "CHRY"
    CHRM = "CHRM"

# Set metadata after class creation
MarmosetChromosome._metadata = {
    "CHR1": {'description': 'chromosome 1 (Marmoset)', 'meaning': 'CHR:9483-chr1', 'annotations': {'refseq_accession': 'NC_048383.1', 'genbank_accession': 'CM018917.1', 'length_bp': 217961735}, 'aliases': ['chr1']},
    "CHR2": {'description': 'chromosome 2 (Marmoset)', 'meaning': 'CHR:9483-chr2', 'annotations': {'refseq_accession': 'NC_048384.1', 'genbank_accession': 'CM018918.1', 'length_bp': 204486479}, 'aliases': ['chr2']},
    "CHR3": {'description': 'chromosome 3 (Marmoset)', 'meaning': 'CHR:9483-chr3', 'annotations': {'refseq_accession': 'NC_048385.1', 'genbank_accession': 'CM018919.1', 'length_bp': 191910223}, 'aliases': ['chr3']},
    "CHR4": {'description': 'chromosome 4 (Marmoset)', 'meaning': 'CHR:9483-chr4', 'annotations': {'refseq_accession': 'NC_048386.1', 'genbank_accession': 'CM018920.1', 'length_bp': 174041770}, 'aliases': ['chr4']},
    "CHR5": {'description': 'chromosome 5 (Marmoset)', 'meaning': 'CHR:9483-chr5', 'annotations': {'refseq_accession': 'NC_048387.1', 'genbank_accession': 'CM018921.1', 'length_bp': 164351765}, 'aliases': ['chr5']},
    "CHR6": {'description': 'chromosome 6 (Marmoset)', 'meaning': 'CHR:9483-chr6', 'annotations': {'refseq_accession': 'NC_048388.1', 'genbank_accession': 'CM018922.1', 'length_bp': 161003406}, 'aliases': ['chr6']},
    "CHR7": {'description': 'chromosome 7 (Marmoset)', 'meaning': 'CHR:9483-chr7', 'annotations': {'refseq_accession': 'NC_048389.1', 'genbank_accession': 'CM018923.1', 'length_bp': 157546058}, 'aliases': ['chr7']},
    "CHR8": {'description': 'chromosome 8 (Marmoset)', 'meaning': 'CHR:9483-chr8', 'annotations': {'refseq_accession': 'NC_048390.1', 'genbank_accession': 'CM018924.1', 'length_bp': 126850804}, 'aliases': ['chr8']},
    "CHR9": {'description': 'chromosome 9 (Marmoset)', 'meaning': 'CHR:9483-chr9', 'annotations': {'refseq_accession': 'NC_048391.1', 'genbank_accession': 'CM018925.1', 'length_bp': 134044658}, 'aliases': ['chr9']},
    "CHR10": {'description': 'chromosome 10 (Marmoset)', 'meaning': 'CHR:9483-chr10', 'annotations': {'refseq_accession': 'NC_048392.1', 'genbank_accession': 'CM018926.1', 'length_bp': 137671225}, 'aliases': ['chr10']},
    "CHR11": {'description': 'chromosome 11 (Marmoset)', 'meaning': 'CHR:9483-chr11', 'annotations': {'refseq_accession': 'NC_048393.1', 'genbank_accession': 'CM018927.1', 'length_bp': 129688756}, 'aliases': ['chr11']},
    "CHR12": {'description': 'chromosome 12 (Marmoset)', 'meaning': 'CHR:9483-chr12', 'annotations': {'refseq_accession': 'NC_048394.1', 'genbank_accession': 'CM018928.1', 'length_bp': 124486764}, 'aliases': ['chr12']},
    "CHR13": {'description': 'chromosome 13 (Marmoset)', 'meaning': 'CHR:9483-chr13', 'annotations': {'refseq_accession': 'NC_048395.1', 'genbank_accession': 'CM018929.1', 'length_bp': 118934817}, 'aliases': ['chr13']},
    "CHR14": {'description': 'chromosome 14 (Marmoset)', 'meaning': 'CHR:9483-chr14', 'annotations': {'refseq_accession': 'NC_048396.1', 'genbank_accession': 'CM018930.1', 'length_bp': 112090317}, 'aliases': ['chr14']},
    "CHR15": {'description': 'chromosome 15 (Marmoset)', 'meaning': 'CHR:9483-chr15', 'annotations': {'refseq_accession': 'NC_048397.1', 'genbank_accession': 'CM018931.1', 'length_bp': 99198953}, 'aliases': ['chr15']},
    "CHR16": {'description': 'chromosome 16 (Marmoset)', 'meaning': 'CHR:9483-chr16', 'annotations': {'refseq_accession': 'NC_048398.1', 'genbank_accession': 'CM018932.1', 'length_bp': 97817134}, 'aliases': ['chr16']},
    "CHR17": {'description': 'chromosome 17 (Marmoset)', 'meaning': 'CHR:9483-chr17', 'annotations': {'refseq_accession': 'NC_048399.1', 'genbank_accession': 'CM018933.1', 'length_bp': 74942703}, 'aliases': ['chr17']},
    "CHR18": {'description': 'chromosome 18 (Marmoset)', 'meaning': 'CHR:9483-chr18', 'annotations': {'refseq_accession': 'NC_048400.1', 'genbank_accession': 'CM018934.1', 'length_bp': 47031477}, 'aliases': ['chr18']},
    "CHR19": {'description': 'chromosome 19 (Marmoset)', 'meaning': 'CHR:9483-chr19', 'annotations': {'refseq_accession': 'NC_048401.1', 'genbank_accession': 'CM018935.1', 'length_bp': 51570929}, 'aliases': ['chr19']},
    "CHR20": {'description': 'chromosome 20 (Marmoset)', 'meaning': 'CHR:9483-chr20', 'annotations': {'refseq_accession': 'NC_048402.1', 'genbank_accession': 'CM018936.1', 'length_bp': 45615054}, 'aliases': ['chr20']},
    "CHR21": {'description': 'chromosome 21 (Marmoset)', 'meaning': 'CHR:9483-chr21', 'annotations': {'refseq_accession': 'NC_048403.1', 'genbank_accession': 'CM018937.1', 'length_bp': 51259342}, 'aliases': ['chr21']},
    "CHR22": {'description': 'chromosome 22 (Marmoset)', 'meaning': 'CHR:9483-chr22', 'annotations': {'refseq_accession': 'NC_048404.1', 'genbank_accession': 'CM018938.1', 'length_bp': 51300780}, 'aliases': ['chr22']},
    "CHRX": {'description': 'chromosome X (Marmoset)', 'meaning': 'CHR:9483-chrX', 'annotations': {'refseq_accession': 'NC_048405.1', 'genbank_accession': 'CM018939.1', 'length_bp': 148168104}, 'aliases': ['chrX']},
    "CHRY": {'description': 'chromosome Y (Marmoset)', 'meaning': 'CHR:9483-chrY', 'annotations': {'refseq_accession': 'NC_048406.1', 'genbank_accession': 'CM023155.1', 'length_bp': 8228174}, 'aliases': ['chrY']},
    "CHRM": {'description': 'chromosome M (Marmoset)', 'meaning': 'CHR:9483-chrM', 'annotations': {'refseq_accession': 'NC_025586.1', 'genbank_accession': 'KM588314.1', 'length_bp': 16499}, 'aliases': ['chrM', 'MT', 'chrMT']},
}

__all__ = [
    "HumanGenomeBuild",
    "ModelOrganismGenomeBuild",
    "HumanChromosome",
    "MouseChromosome",
    "RatChromosome",
    "ZebrafishChromosome",
    "ChickenChromosome",
    "CElegansChromosome",
    "MarmosetChromosome",
]