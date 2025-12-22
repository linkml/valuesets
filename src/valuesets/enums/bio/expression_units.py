"""
Gene Expression Unit Value Sets

Value sets for gene expression quantification units used in RNA-seq and other transcriptomic analyses. Includes normalization methods and count types.

Generated from: bio/expression_units.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class ExpressionUnitEnum(RichEnum):
    """
    Quantification units for gene expression data from RNA-seq and microarray experiments. Includes raw counts and various normalization methods.
    """
    # Enum members
    RAW_COUNTS = "RAW_COUNTS"
    NORMALIZED_COUNTS = "NORMALIZED_COUNTS"
    COUNTS = "COUNTS"
    TPM = "TPM"
    FPKM = "FPKM"
    RPKM = "RPKM"
    CPM = "CPM"
    RPKM_UQ = "RPKM_UQ"
    VST = "VST"
    RLOG = "RLOG"
    LOG2_RATIO = "LOG2_RATIO"
    Z_SCORE = "Z_SCORE"

# Set metadata after class creation
ExpressionUnitEnum._metadata = {
    "RAW_COUNTS": {'description': 'Raw read counts of transcripts without normalization', 'annotations': {'normalization': 'none', 'use': 'within-sample comparisons only'}, 'aliases': ['Raw Counts', 'raw counts']},
    "NORMALIZED_COUNTS": {'description': 'Counts normalized by a method such as DESeq2 or edgeR', 'annotations': {'normalization': 'library size', 'use': 'differential expression'}, 'aliases': ['Normalized Counts']},
    "COUNTS": {'description': 'General read counts category', 'aliases': ['Counts']},
    "TPM": {'description': 'Transcripts per million - normalized for gene length and sequencing depth', 'meaning': 'NCIT:C181327', 'annotations': {'normalization': 'length and depth', 'use': 'within and between sample comparisons', 'formula': '(reads/gene_length_kb) / sum(reads/gene_length_kb) * 1e6'}, 'aliases': ['Transcript per million']},
    "FPKM": {'description': 'Fragments per kilobase of transcript per million reads mapped', 'meaning': 'STATO:0000172', 'annotations': {'normalization': 'length and depth', 'use': 'within-sample comparisons', 'library_type': 'paired-end'}, 'aliases': ['Fragments per kilobase of transcript per million reads mapped']},
    "RPKM": {'description': 'Reads per kilobase of transcript per million reads mapped', 'meaning': 'STATO:0000206', 'annotations': {'normalization': 'length and depth', 'use': 'within-sample comparisons', 'library_type': 'single-end'}, 'aliases': ['Reads per kilobase of transcript per million reads mapped']},
    "CPM": {'description': 'Counts per million reads', 'annotations': {'normalization': 'depth only'}, 'aliases': ['Counts per million']},
    "RPKM_UQ": {'description': 'RPKM with upper quartile normalization', 'annotations': {'normalization': 'length, depth, and upper quartile'}},
    "VST": {'description': 'Variance stabilizing transformation values', 'annotations': {'method': 'DESeq2', 'use': 'visualization, clustering'}},
    "RLOG": {'description': 'Regularized log transformation values', 'annotations': {'method': 'DESeq2', 'use': 'visualization, clustering'}, 'aliases': ['rlog']},
    "LOG2_RATIO": {'description': 'Log2 fold change ratio', 'annotations': {'use': 'differential expression'}},
    "Z_SCORE": {'description': 'Z-score normalized expression', 'annotations': {'use': 'cross-gene comparisons'}},
}

class ConcentrationUnitEnum(RichEnum):
    """
    Units for measuring concentration in biological experiments
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
    PARTICLES_PER_ML = "PARTICLES_PER_ML"
    PERCENT_W_V = "PERCENT_W_V"
    PERCENT_V_V = "PERCENT_V_V"

# Set metadata after class creation
ConcentrationUnitEnum._metadata = {
    "MOLAR": {'description': 'Molar concentration (mol/L)', 'meaning': 'UO:0000062', 'aliases': ['M']},
    "MILLIMOLAR": {'description': 'Millimolar concentration (mmol/L)', 'meaning': 'UO:0000063', 'aliases': ['mM']},
    "MICROMOLAR": {'description': 'Micromolar concentration (umol/L)', 'meaning': 'UO:0000064', 'aliases': ['uM']},
    "NANOMOLAR": {'description': 'Nanomolar concentration (nmol/L)', 'meaning': 'UO:0000065', 'aliases': ['nM']},
    "PICOMOLAR": {'description': 'Picomolar concentration (pmol/L)', 'meaning': 'UO:0000066', 'aliases': ['pM']},
    "MG_PER_ML": {'description': 'Milligrams per milliliter', 'meaning': 'UO:0000176', 'aliases': ['mg/mL']},
    "UG_PER_ML": {'description': 'Micrograms per milliliter', 'meaning': 'UO:0000274', 'aliases': ['ug/mL']},
    "NG_PER_ML": {'description': 'Nanograms per milliliter', 'aliases': ['ng/mL']},
    "PARTICLES_PER_ML": {'description': 'Particles per milliliter', 'aliases': ['particles/mL']},
    "PERCENT_W_V": {'description': 'Percent weight per volume', 'meaning': 'UO:0000164', 'aliases': ['% w/v']},
    "PERCENT_V_V": {'description': 'Percent volume per volume', 'meaning': 'UO:0000165', 'aliases': ['% v/v']},
}

class TimeUnitEnum(RichEnum):
    """
    Units for measuring time in biological experiments
    """
    # Enum members
    SECONDS = "SECONDS"
    MINUTES = "MINUTES"
    HOURS = "HOURS"
    DAYS = "DAYS"
    WEEKS = "WEEKS"
    MONTHS = "MONTHS"
    YEARS = "YEARS"

# Set metadata after class creation
TimeUnitEnum._metadata = {
    "SECONDS": {'description': 'Time in seconds', 'meaning': 'UO:0000010', 'aliases': ['s', 'sec']},
    "MINUTES": {'description': 'Time in minutes', 'meaning': 'UO:0000031', 'aliases': ['min']},
    "HOURS": {'description': 'Time in hours', 'meaning': 'UO:0000032', 'aliases': ['h', 'hr']},
    "DAYS": {'description': 'Time in days', 'meaning': 'UO:0000033', 'aliases': ['d']},
    "WEEKS": {'description': 'Time in weeks', 'meaning': 'UO:0000034', 'aliases': ['wk']},
    "MONTHS": {'description': 'Time in months', 'meaning': 'UO:0000035', 'aliases': ['mo']},
    "YEARS": {'description': 'Time in years', 'meaning': 'UO:0000036', 'aliases': ['yr']},
}

__all__ = [
    "ExpressionUnitEnum",
    "ConcentrationUnitEnum",
    "TimeUnitEnum",
]