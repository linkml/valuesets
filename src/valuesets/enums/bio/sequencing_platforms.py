"""
Sequencing Platform Value Sets

Value sets for DNA/RNA sequencing platforms, technologies, and methodologies

Generated from: bio/sequencing_platforms.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class SequencingPlatform(RichEnum):
    """
    Major DNA/RNA sequencing platforms and instruments used in genomics research
    """
    # Enum members
    ILLUMINA_HISEQ_2000 = "ILLUMINA_HISEQ_2000"
    ILLUMINA_HISEQ_2500 = "ILLUMINA_HISEQ_2500"
    ILLUMINA_HISEQ_3000 = "ILLUMINA_HISEQ_3000"
    ILLUMINA_HISEQ_4000 = "ILLUMINA_HISEQ_4000"
    ILLUMINA_HISEQ_X = "ILLUMINA_HISEQ_X"
    ILLUMINA_NOVASEQ_6000 = "ILLUMINA_NOVASEQ_6000"
    ILLUMINA_NEXTSEQ_500 = "ILLUMINA_NEXTSEQ_500"
    ILLUMINA_NEXTSEQ_550 = "ILLUMINA_NEXTSEQ_550"
    ILLUMINA_NEXTSEQ_1000 = "ILLUMINA_NEXTSEQ_1000"
    ILLUMINA_NEXTSEQ_2000 = "ILLUMINA_NEXTSEQ_2000"
    ILLUMINA_MISEQ = "ILLUMINA_MISEQ"
    ILLUMINA_ISEQ_100 = "ILLUMINA_ISEQ_100"
    PACBIO_RS = "PACBIO_RS"
    PACBIO_RS_II = "PACBIO_RS_II"
    PACBIO_SEQUEL = "PACBIO_SEQUEL"
    PACBIO_SEQUEL_II = "PACBIO_SEQUEL_II"
    PACBIO_REVIO = "PACBIO_REVIO"
    NANOPORE_MINION = "NANOPORE_MINION"
    NANOPORE_GRIDION = "NANOPORE_GRIDION"
    NANOPORE_PROMETHION = "NANOPORE_PROMETHION"
    NANOPORE_FLONGLE = "NANOPORE_FLONGLE"
    ELEMENT_AVITI = "ELEMENT_AVITI"
    MGI_DNBSEQ_T7 = "MGI_DNBSEQ_T7"
    MGI_DNBSEQ_G400 = "MGI_DNBSEQ_G400"
    MGI_DNBSEQ_G50 = "MGI_DNBSEQ_G50"
    SANGER_SEQUENCING = "SANGER_SEQUENCING"
    ROCHE_454_GS = "ROCHE_454_GS"
    LIFE_TECHNOLOGIES_ION_TORRENT = "LIFE_TECHNOLOGIES_ION_TORRENT"
    ABI_SOLID = "ABI_SOLID"

# Set metadata after class creation
SequencingPlatform._metadata = {
    "ILLUMINA_HISEQ_2000": {'description': 'Illumina HiSeq 2000', 'meaning': 'OBI:0002001', 'annotations': {'manufacturer': 'Illumina', 'read_type': 'short', 'chemistry': 'sequencing by synthesis'}},
    "ILLUMINA_HISEQ_2500": {'description': 'Illumina HiSeq 2500', 'meaning': 'OBI:0002002', 'annotations': {'manufacturer': 'Illumina', 'read_type': 'short', 'chemistry': 'sequencing by synthesis'}},
    "ILLUMINA_HISEQ_3000": {'description': 'Illumina HiSeq 3000', 'meaning': 'OBI:0002048', 'annotations': {'manufacturer': 'Illumina', 'read_type': 'short', 'chemistry': 'sequencing by synthesis'}},
    "ILLUMINA_HISEQ_4000": {'description': 'Illumina HiSeq 4000', 'meaning': 'OBI:0002049', 'annotations': {'manufacturer': 'Illumina', 'read_type': 'short', 'chemistry': 'sequencing by synthesis'}},
    "ILLUMINA_HISEQ_X": {'description': 'Illumina HiSeq X', 'meaning': 'OBI:0002129', 'annotations': {'manufacturer': 'Illumina', 'read_type': 'short', 'chemistry': 'sequencing by synthesis'}, 'aliases': ['Illumina HiSeq X Ten']},
    "ILLUMINA_NOVASEQ_6000": {'description': 'Illumina NovaSeq 6000', 'meaning': 'OBI:0002630', 'annotations': {'manufacturer': 'Illumina', 'read_type': 'short', 'chemistry': 'sequencing by synthesis'}},
    "ILLUMINA_NEXTSEQ_500": {'description': 'Illumina NextSeq 500', 'meaning': 'OBI:0002021', 'annotations': {'manufacturer': 'Illumina', 'read_type': 'short', 'chemistry': 'sequencing by synthesis'}},
    "ILLUMINA_NEXTSEQ_550": {'description': 'Illumina NextSeq 550', 'meaning': 'OBI:0003387', 'annotations': {'manufacturer': 'Illumina', 'read_type': 'short', 'chemistry': 'sequencing by synthesis'}},
    "ILLUMINA_NEXTSEQ_1000": {'description': 'Illumina NextSeq 1000', 'annotations': {'manufacturer': 'Illumina', 'read_type': 'short', 'chemistry': 'sequencing by synthesis'}},
    "ILLUMINA_NEXTSEQ_2000": {'description': 'Illumina NextSeq 2000', 'annotations': {'manufacturer': 'Illumina', 'read_type': 'short', 'chemistry': 'sequencing by synthesis'}},
    "ILLUMINA_MISEQ": {'description': 'Illumina MiSeq', 'meaning': 'OBI:0002003', 'annotations': {'manufacturer': 'Illumina', 'read_type': 'short', 'chemistry': 'sequencing by synthesis'}},
    "ILLUMINA_ISEQ_100": {'description': 'Illumina iSeq 100', 'annotations': {'manufacturer': 'Illumina', 'read_type': 'short', 'chemistry': 'sequencing by synthesis'}},
    "PACBIO_RS": {'description': 'PacBio RS', 'annotations': {'manufacturer': 'Pacific Biosciences', 'read_type': 'long', 'chemistry': 'single molecule real time'}},
    "PACBIO_RS_II": {'description': 'PacBio RS II', 'meaning': 'OBI:0002012', 'annotations': {'manufacturer': 'Pacific Biosciences', 'read_type': 'long', 'chemistry': 'single molecule real time'}},
    "PACBIO_SEQUEL": {'description': 'PacBio Sequel', 'meaning': 'OBI:0002632', 'annotations': {'manufacturer': 'Pacific Biosciences', 'read_type': 'long', 'chemistry': 'single molecule real time'}},
    "PACBIO_SEQUEL_II": {'description': 'PacBio Sequel II', 'meaning': 'OBI:0002633', 'annotations': {'manufacturer': 'Pacific Biosciences', 'read_type': 'long', 'chemistry': 'single molecule real time'}},
    "PACBIO_REVIO": {'description': 'PacBio Revio', 'annotations': {'manufacturer': 'Pacific Biosciences', 'read_type': 'long', 'chemistry': 'single molecule real time'}},
    "NANOPORE_MINION": {'description': 'Oxford Nanopore MinION', 'meaning': 'OBI:0002750', 'annotations': {'manufacturer': 'Oxford Nanopore Technologies', 'read_type': 'long', 'chemistry': 'nanopore sequencing'}, 'aliases': ['Oxford Nanopore MinION']},
    "NANOPORE_GRIDION": {'description': 'Oxford Nanopore GridION', 'meaning': 'OBI:0002751', 'annotations': {'manufacturer': 'Oxford Nanopore Technologies', 'read_type': 'long', 'chemistry': 'nanopore sequencing'}, 'aliases': ['Oxford Nanopore GridION Mk1']},
    "NANOPORE_PROMETHION": {'description': 'Oxford Nanopore PromethION', 'meaning': 'OBI:0002752', 'annotations': {'manufacturer': 'Oxford Nanopore Technologies', 'read_type': 'long', 'chemistry': 'nanopore sequencing'}, 'aliases': ['Oxford Nanopore PromethION']},
    "NANOPORE_FLONGLE": {'description': 'Oxford Nanopore Flongle', 'annotations': {'manufacturer': 'Oxford Nanopore Technologies', 'read_type': 'long', 'chemistry': 'nanopore sequencing'}},
    "ELEMENT_AVITI": {'description': 'Element Biosciences AVITI', 'annotations': {'manufacturer': 'Element Biosciences', 'read_type': 'short', 'chemistry': 'sequencing by avidity'}},
    "MGI_DNBSEQ_T7": {'description': 'MGI DNBSEQ-T7', 'annotations': {'manufacturer': 'MGI/BGI', 'read_type': 'short', 'chemistry': 'DNA nanoball sequencing'}},
    "MGI_DNBSEQ_G400": {'description': 'MGI DNBSEQ-G400', 'annotations': {'manufacturer': 'MGI/BGI', 'read_type': 'short', 'chemistry': 'DNA nanoball sequencing'}},
    "MGI_DNBSEQ_G50": {'description': 'MGI DNBSEQ-G50', 'annotations': {'manufacturer': 'MGI/BGI', 'read_type': 'short', 'chemistry': 'DNA nanoball sequencing'}},
    "SANGER_SEQUENCING": {'description': 'Sanger chain termination sequencing', 'meaning': 'OBI:0000695', 'annotations': {'manufacturer': 'Various', 'read_type': 'short', 'chemistry': 'chain termination'}, 'aliases': ['chain termination sequencing assay']},
    "ROCHE_454_GS": {'description': 'Roche 454 Genome Sequencer', 'meaning': 'OBI:0000702', 'annotations': {'manufacturer': 'Roche/454', 'read_type': 'short', 'chemistry': 'pyrosequencing', 'status': 'discontinued'}, 'aliases': ['454 Genome Sequencer FLX']},
    "LIFE_TECHNOLOGIES_ION_TORRENT": {'description': 'Life Technologies Ion Torrent', 'annotations': {'manufacturer': 'Life Technologies/Thermo Fisher', 'read_type': 'short', 'chemistry': 'semiconductor sequencing'}},
    "ABI_SOLID": {'description': 'ABI SOLiD', 'annotations': {'manufacturer': 'Life Technologies/Applied Biosystems', 'read_type': 'short', 'chemistry': 'sequencing by ligation', 'status': 'discontinued'}},
}

class SequencingChemistry(RichEnum):
    """
    Fundamental chemical methods used for DNA/RNA sequencing
    """
    # Enum members
    SEQUENCING_BY_SYNTHESIS = "SEQUENCING_BY_SYNTHESIS"
    SINGLE_MOLECULE_REAL_TIME = "SINGLE_MOLECULE_REAL_TIME"
    NANOPORE_SEQUENCING = "NANOPORE_SEQUENCING"
    PYROSEQUENCING = "PYROSEQUENCING"
    SEQUENCING_BY_LIGATION = "SEQUENCING_BY_LIGATION"
    CHAIN_TERMINATION = "CHAIN_TERMINATION"
    SEMICONDUCTOR_SEQUENCING = "SEMICONDUCTOR_SEQUENCING"
    DNA_NANOBALL_SEQUENCING = "DNA_NANOBALL_SEQUENCING"
    SEQUENCING_BY_AVIDITY = "SEQUENCING_BY_AVIDITY"

# Set metadata after class creation
SequencingChemistry._metadata = {
    "SEQUENCING_BY_SYNTHESIS": {'description': 'Sequencing by synthesis (Illumina)', 'meaning': 'OBI:0000734', 'aliases': ['DNA sequencing by synthesis assay']},
    "SINGLE_MOLECULE_REAL_TIME": {'description': 'Single molecule real-time sequencing (PacBio)'},
    "NANOPORE_SEQUENCING": {'description': 'Nanopore sequencing (Oxford Nanopore)'},
    "PYROSEQUENCING": {'description': 'Pyrosequencing (454)'},
    "SEQUENCING_BY_LIGATION": {'description': 'Sequencing by ligation (SOLiD)', 'meaning': 'OBI:0000723', 'aliases': ['DNA sequencing by ligation assay']},
    "CHAIN_TERMINATION": {'description': 'Chain termination method (Sanger)', 'meaning': 'OBI:0000695', 'aliases': ['chain termination sequencing assay']},
    "SEMICONDUCTOR_SEQUENCING": {'description': 'Semiconductor/Ion semiconductor sequencing'},
    "DNA_NANOBALL_SEQUENCING": {'description': 'DNA nanoball sequencing (MGI/BGI)'},
    "SEQUENCING_BY_AVIDITY": {'description': 'Sequencing by avidity (Element Biosciences)'},
}

class LibraryPreparation(RichEnum):
    """
    Methods for preparing sequencing libraries from nucleic acid samples
    """
    # Enum members
    GENOMIC_DNA = "GENOMIC_DNA"
    WHOLE_GENOME_AMPLIFICATION = "WHOLE_GENOME_AMPLIFICATION"
    PCR_AMPLICON = "PCR_AMPLICON"
    RNA_SEQ = "RNA_SEQ"
    SMALL_RNA_SEQ = "SMALL_RNA_SEQ"
    SINGLE_CELL_RNA_SEQ = "SINGLE_CELL_RNA_SEQ"
    ATAC_SEQ = "ATAC_SEQ"
    CHIP_SEQ = "CHIP_SEQ"
    BISULFITE_SEQ = "BISULFITE_SEQ"
    HI_C = "HI_C"
    CUT_AND_RUN = "CUT_AND_RUN"
    CUT_AND_TAG = "CUT_AND_TAG"
    CAPTURE_SEQUENCING = "CAPTURE_SEQUENCING"
    EXOME_SEQUENCING = "EXOME_SEQUENCING"
    METAGENOMICS = "METAGENOMICS"
    AMPLICON_SEQUENCING = "AMPLICON_SEQUENCING"
    DIRECT_RNA = "DIRECT_RNA"
    CDNA_SEQUENCING = "CDNA_SEQUENCING"
    RIBOSOME_PROFILING = "RIBOSOME_PROFILING"

# Set metadata after class creation
LibraryPreparation._metadata = {
    "GENOMIC_DNA": {'description': 'Genomic DNA library preparation'},
    "WHOLE_GENOME_AMPLIFICATION": {'description': 'Whole genome amplification (WGA)'},
    "PCR_AMPLICON": {'description': 'PCR amplicon sequencing'},
    "RNA_SEQ": {'description': 'RNA sequencing library prep'},
    "SMALL_RNA_SEQ": {'description': 'Small RNA sequencing'},
    "SINGLE_CELL_RNA_SEQ": {'description': 'Single-cell RNA sequencing'},
    "ATAC_SEQ": {'description': 'ATAC-seq (chromatin accessibility)'},
    "CHIP_SEQ": {'description': 'ChIP-seq (chromatin immunoprecipitation)'},
    "BISULFITE_SEQ": {'description': 'Bisulfite sequencing (methylation)'},
    "HI_C": {'description': 'Hi-C (chromosome conformation capture)'},
    "CUT_AND_RUN": {'description': 'CUT&RUN (chromatin profiling)'},
    "CUT_AND_TAG": {'description': 'CUT&Tag (chromatin profiling)'},
    "CAPTURE_SEQUENCING": {'description': 'Target capture/enrichment sequencing'},
    "EXOME_SEQUENCING": {'description': 'Whole exome sequencing'},
    "METAGENOMICS": {'description': 'Metagenomic sequencing'},
    "AMPLICON_SEQUENCING": {'description': '16S/ITS amplicon sequencing'},
    "DIRECT_RNA": {'description': 'Direct RNA sequencing (nanopore)'},
    "CDNA_SEQUENCING": {'description': 'cDNA sequencing'},
    "RIBOSOME_PROFILING": {'description': 'Ribosome profiling (Ribo-seq)'},
}

class SequencingApplication(RichEnum):
    """
    Primary applications or assays using DNA/RNA sequencing
    """
    # Enum members
    WHOLE_GENOME_SEQUENCING = "WHOLE_GENOME_SEQUENCING"
    WHOLE_EXOME_SEQUENCING = "WHOLE_EXOME_SEQUENCING"
    TRANSCRIPTOME_SEQUENCING = "TRANSCRIPTOME_SEQUENCING"
    TARGETED_SEQUENCING = "TARGETED_SEQUENCING"
    EPIGENOMICS = "EPIGENOMICS"
    METAGENOMICS = "METAGENOMICS"
    SINGLE_CELL_GENOMICS = "SINGLE_CELL_GENOMICS"
    SINGLE_CELL_TRANSCRIPTOMICS = "SINGLE_CELL_TRANSCRIPTOMICS"
    CHROMATIN_IMMUNOPRECIPITATION = "CHROMATIN_IMMUNOPRECIPITATION"
    CHROMATIN_ACCESSIBILITY = "CHROMATIN_ACCESSIBILITY"
    DNA_METHYLATION = "DNA_METHYLATION"
    CHROMOSOME_CONFORMATION = "CHROMOSOME_CONFORMATION"
    VARIANT_CALLING = "VARIANT_CALLING"
    PHARMACOGENOMICS = "PHARMACOGENOMICS"
    CLINICAL_DIAGNOSTICS = "CLINICAL_DIAGNOSTICS"
    POPULATION_GENOMICS = "POPULATION_GENOMICS"

# Set metadata after class creation
SequencingApplication._metadata = {
    "WHOLE_GENOME_SEQUENCING": {'description': 'Whole genome sequencing (WGS)', 'meaning': 'EDAM:topic_3673'},
    "WHOLE_EXOME_SEQUENCING": {'description': 'Whole exome sequencing (WES)', 'meaning': 'EDAM:topic_3676', 'aliases': ['Exome sequencing']},
    "TRANSCRIPTOME_SEQUENCING": {'description': 'RNA sequencing (RNA-seq)', 'meaning': 'EDAM:topic_3170', 'aliases': ['RNA-Seq']},
    "TARGETED_SEQUENCING": {'description': 'Targeted gene panel sequencing'},
    "EPIGENOMICS": {'description': 'Epigenomic profiling'},
    "METAGENOMICS": {'description': 'Metagenomic sequencing', 'meaning': 'EDAM:topic_3837', 'aliases': ['Metagenomic sequencing']},
    "SINGLE_CELL_GENOMICS": {'description': 'Single-cell genomics'},
    "SINGLE_CELL_TRANSCRIPTOMICS": {'description': 'Single-cell transcriptomics', 'meaning': 'EDAM:topic_4028', 'aliases': ['Single-cell sequencing']},
    "CHROMATIN_IMMUNOPRECIPITATION": {'description': 'ChIP-seq', 'meaning': 'EDAM:topic_3656', 'aliases': ['Immunoprecipitation experiment']},
    "CHROMATIN_ACCESSIBILITY": {'description': 'ATAC-seq/FAIRE-seq'},
    "DNA_METHYLATION": {'description': 'Bisulfite/methylation sequencing'},
    "CHROMOSOME_CONFORMATION": {'description': 'Hi-C/3C-seq'},
    "VARIANT_CALLING": {'description': 'Genetic variant discovery'},
    "PHARMACOGENOMICS": {'description': 'Pharmacogenomic sequencing'},
    "CLINICAL_DIAGNOSTICS": {'description': 'Clinical diagnostic sequencing'},
    "POPULATION_GENOMICS": {'description': 'Population-scale genomics'},
}

class ReadType(RichEnum):
    """
    Configuration of sequencing reads generated by different platforms
    """
    # Enum members
    SINGLE_END = "SINGLE_END"
    PAIRED_END = "PAIRED_END"
    MATE_PAIR = "MATE_PAIR"
    LONG_READ = "LONG_READ"
    ULTRA_LONG_READ = "ULTRA_LONG_READ"
    CONTINUOUS_LONG_READ = "CONTINUOUS_LONG_READ"

# Set metadata after class creation
ReadType._metadata = {
    "SINGLE_END": {'description': 'Single-end reads'},
    "PAIRED_END": {'description': 'Paired-end reads'},
    "MATE_PAIR": {'description': 'Mate-pair reads (large insert)'},
    "LONG_READ": {'description': 'Long reads (>1kb typical)'},
    "ULTRA_LONG_READ": {'description': 'Ultra-long reads (>10kb)'},
    "CONTINUOUS_LONG_READ": {'description': 'Continuous long reads (nanopore)'},
}

class SequenceFileFormat(RichEnum):
    """
    Standard file formats used for storing sequence data
    """
    # Enum members
    FASTA = "FASTA"
    FASTQ = "FASTQ"
    SAM = "SAM"
    BAM = "BAM"
    CRAM = "CRAM"
    VCF = "VCF"
    BCF = "BCF"
    GFF3 = "GFF3"
    GTF = "GTF"
    BED = "BED"
    BIGWIG = "BIGWIG"
    BIGBED = "BIGBED"
    HDF5 = "HDF5"
    SFF = "SFF"
    FAST5 = "FAST5"
    POD5 = "POD5"

# Set metadata after class creation
SequenceFileFormat._metadata = {
    "FASTA": {'description': 'FASTA sequence format', 'meaning': 'EDAM:format_1929', 'annotations': {'extensions': '.fa, .fasta, .fna, .ffn, .faa, .frn', 'content': 'sequences only'}},
    "FASTQ": {'description': 'FASTQ sequence with quality format', 'meaning': 'EDAM:format_1930', 'annotations': {'extensions': '.fq, .fastq', 'content': 'sequences and quality scores'}},
    "SAM": {'description': 'Sequence Alignment Map format', 'meaning': 'EDAM:format_2573', 'annotations': {'extensions': '.sam', 'content': 'aligned sequences (text)'}},
    "BAM": {'description': 'Binary Alignment Map format', 'meaning': 'EDAM:format_2572', 'annotations': {'extensions': '.bam', 'content': 'aligned sequences (binary)'}},
    "CRAM": {'description': 'Compressed Reference-oriented Alignment Map', 'annotations': {'extensions': '.cram', 'content': 'compressed aligned sequences'}},
    "VCF": {'description': 'Variant Call Format', 'meaning': 'EDAM:format_3016', 'annotations': {'extensions': '.vcf', 'content': 'genetic variants'}},
    "BCF": {'description': 'Binary Variant Call Format', 'meaning': 'EDAM:format_3020', 'annotations': {'extensions': '.bcf', 'content': 'genetic variants (binary)'}},
    "GFF3": {'description': 'Generic Feature Format version 3', 'annotations': {'extensions': '.gff, .gff3', 'content': 'genomic annotations'}},
    "GTF": {'description': 'Gene Transfer Format', 'annotations': {'extensions': '.gtf', 'content': 'gene annotations'}},
    "BED": {'description': 'Browser Extensible Data format', 'annotations': {'extensions': '.bed', 'content': 'genomic intervals'}},
    "BIGWIG": {'description': 'BigWig format for continuous data', 'annotations': {'extensions': '.bw, .bigwig', 'content': 'continuous genomic data'}},
    "BIGBED": {'description': 'BigBed format for interval data', 'annotations': {'extensions': '.bb, .bigbed', 'content': 'genomic intervals (indexed)'}},
    "HDF5": {'description': 'Hierarchical Data Format 5', 'annotations': {'extensions': '.h5, .hdf5', 'content': 'multi-dimensional arrays'}},
    "SFF": {'description': 'Standard Flowgram Format (454)', 'meaning': 'EDAM:format_3284', 'annotations': {'extensions': '.sff', 'content': '454 sequencing data', 'status': 'legacy'}},
    "FAST5": {'description': 'Fast5 format (Oxford Nanopore)', 'annotations': {'extensions': '.fast5', 'content': 'nanopore raw signal data'}},
    "POD5": {'description': 'POD5 format (Oxford Nanopore, newer)', 'annotations': {'extensions': '.pod5', 'content': 'nanopore raw signal data (compressed)'}},
}

class DataProcessingLevel(RichEnum):
    """
    Levels of processing applied to raw sequencing data
    """
    # Enum members
    RAW = "RAW"
    QUALITY_FILTERED = "QUALITY_FILTERED"
    TRIMMED = "TRIMMED"
    ALIGNED = "ALIGNED"
    DEDUPLICATED = "DEDUPLICATED"
    RECALIBRATED = "RECALIBRATED"
    VARIANT_CALLED = "VARIANT_CALLED"
    NORMALIZED = "NORMALIZED"
    ASSEMBLED = "ASSEMBLED"
    ANNOTATED = "ANNOTATED"

# Set metadata after class creation
DataProcessingLevel._metadata = {
    "RAW": {'description': 'Raw unprocessed sequencing reads'},
    "QUALITY_FILTERED": {'description': 'Quality filtered reads'},
    "TRIMMED": {'description': 'Adapter/quality trimmed reads'},
    "ALIGNED": {'description': 'Aligned to reference genome'},
    "DEDUPLICATED": {'description': 'PCR duplicates removed'},
    "RECALIBRATED": {'description': 'Base quality score recalibrated'},
    "VARIANT_CALLED": {'description': 'Variants called from alignments'},
    "NORMALIZED": {'description': 'Expression normalized (RNA-seq)'},
    "ASSEMBLED": {'description': 'De novo assembled sequences'},
    "ANNOTATED": {'description': 'Functionally annotated sequences'},
}

__all__ = [
    "SequencingPlatform",
    "SequencingChemistry",
    "LibraryPreparation",
    "SequencingApplication",
    "ReadType",
    "SequenceFileFormat",
    "DataProcessingLevel",
]