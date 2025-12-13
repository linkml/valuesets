"""
Mass Spectrometry Value Sets

Value sets for mass spectrometry and analytical chemistry, derived from MS and MSIO ontologies.

Generated from: analytical_chemistry/mass_spectrometry.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class RelativeTimeEnum(RichEnum):
    """
    Temporal relationships between events or time points
    """
    # Enum members
    BEFORE = "BEFORE"
    AFTER = "AFTER"
    AT_SAME_TIME_AS = "AT_SAME_TIME_AS"

# Set metadata after class creation
RelativeTimeEnum._metadata = {
    "BEFORE": {'description': 'Occurs before the reference time point'},
    "AFTER": {'description': 'Occurs after the reference time point'},
    "AT_SAME_TIME_AS": {'description': 'Occurs at the same time as the reference time point'},
}

class PresenceEnum(RichEnum):
    """
    Classification of whether an entity is present, absent, or at detection limits
    """
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

class MassSpectrometerFileFormat(RichEnum):
    """
    Standard file formats used in mass spectrometry
    """
    # Enum members
    MZML = "MZML"
    MZXML = "MZXML"
    MGF = "MGF"
    THERMO_RAW = "THERMO_RAW"
    WATERS_RAW = "WATERS_RAW"
    WIFF = "WIFF"
    MZDATA = "MZDATA"
    PKL = "PKL"
    DTA = "DTA"
    MS2 = "MS2"
    BRUKER_BAF = "BRUKER_BAF"
    BRUKER_TDF = "BRUKER_TDF"
    BRUKER_TSF = "BRUKER_TSF"
    MZ5 = "MZ5"
    MZMLB = "MZMLB"
    UIMF = "UIMF"

# Set metadata after class creation
MassSpectrometerFileFormat._metadata = {
    "MZML": {'description': 'mzML format - PSI standard for mass spectrometry data', 'meaning': 'MS:1000584'},
    "MZXML": {'description': 'ISB mzXML format', 'meaning': 'MS:1000566'},
    "MGF": {'description': 'Mascot Generic Format', 'meaning': 'MS:1001062'},
    "THERMO_RAW": {'description': 'Thermo RAW format', 'meaning': 'MS:1000563'},
    "WATERS_RAW": {'description': 'Waters raw format', 'meaning': 'MS:1000526'},
    "WIFF": {'description': 'ABI WIFF format', 'meaning': 'MS:1000562'},
    "MZDATA": {'description': 'PSI mzData format', 'meaning': 'MS:1000564'},
    "PKL": {'description': 'Micromass PKL format', 'meaning': 'MS:1000565'},
    "DTA": {'description': 'DTA format', 'meaning': 'MS:1000613'},
    "MS2": {'description': 'MS2 format', 'meaning': 'MS:1001466'},
    "BRUKER_BAF": {'description': 'Bruker BAF format', 'meaning': 'MS:1000815'},
    "BRUKER_TDF": {'description': 'Bruker TDF format', 'meaning': 'MS:1002817'},
    "BRUKER_TSF": {'description': 'Bruker TSF format', 'meaning': 'MS:1003282'},
    "MZ5": {'description': 'mz5 format', 'meaning': 'MS:1001881'},
    "MZMLB": {'description': 'mzMLb format', 'meaning': 'MS:1002838'},
    "UIMF": {'description': 'UIMF format', 'meaning': 'MS:1002531'},
}

class MassSpectrometerVendor(RichEnum):
    """
    Major mass spectrometer manufacturers
    """
    # Enum members
    THERMO_FISHER_SCIENTIFIC = "THERMO_FISHER_SCIENTIFIC"
    WATERS = "WATERS"
    BRUKER_DALTONICS = "BRUKER_DALTONICS"
    SCIEX = "SCIEX"
    AGILENT = "AGILENT"
    SHIMADZU = "SHIMADZU"
    LECO = "LECO"

# Set metadata after class creation
MassSpectrometerVendor._metadata = {
    "THERMO_FISHER_SCIENTIFIC": {'description': 'Thermo Fisher Scientific', 'meaning': 'MS:1000483'},
    "WATERS": {'description': 'Waters Corporation', 'meaning': 'MS:1000126'},
    "BRUKER_DALTONICS": {'description': 'Bruker Daltonics', 'meaning': 'MS:1000122'},
    "SCIEX": {'description': 'SCIEX (formerly Applied Biosystems)', 'meaning': 'MS:1000121'},
    "AGILENT": {'description': 'Agilent Technologies', 'meaning': 'MS:1000490'},
    "SHIMADZU": {'description': 'Shimadzu Corporation', 'meaning': 'MS:1000124'},
    "LECO": {'description': 'LECO Corporation', 'meaning': 'MS:1001800'},
}

class ChromatographyType(RichEnum):
    """
    Types of chromatographic separation methods
    """
    # Enum members
    GAS_CHROMATOGRAPHY = "GAS_CHROMATOGRAPHY"
    HIGH_PERFORMANCE_LIQUID_CHROMATOGRAPHY = "HIGH_PERFORMANCE_LIQUID_CHROMATOGRAPHY"
    LIQUID_CHROMATOGRAPHY_MASS_SPECTROMETRY = "LIQUID_CHROMATOGRAPHY_MASS_SPECTROMETRY"
    GAS_CHROMATOGRAPHY_MASS_SPECTROMETRY = "GAS_CHROMATOGRAPHY_MASS_SPECTROMETRY"
    TANDEM_MASS_SPECTROMETRY = "TANDEM_MASS_SPECTROMETRY"
    ISOTOPE_RATIO_MASS_SPECTROMETRY = "ISOTOPE_RATIO_MASS_SPECTROMETRY"

# Set metadata after class creation
ChromatographyType._metadata = {
    "GAS_CHROMATOGRAPHY": {'description': 'Gas chromatography', 'meaning': 'MSIO:0000147'},
    "HIGH_PERFORMANCE_LIQUID_CHROMATOGRAPHY": {'description': 'High performance liquid chromatography', 'meaning': 'MSIO:0000148'},
    "LIQUID_CHROMATOGRAPHY_MASS_SPECTROMETRY": {'description': 'Liquid chromatography-mass spectrometry', 'meaning': 'CHMO:0000524'},
    "GAS_CHROMATOGRAPHY_MASS_SPECTROMETRY": {'description': 'Gas chromatography-mass spectrometry', 'meaning': 'CHMO:0000497'},
    "TANDEM_MASS_SPECTROMETRY": {'description': 'Tandem mass spectrometry', 'meaning': 'CHMO:0000575'},
    "ISOTOPE_RATIO_MASS_SPECTROMETRY": {'description': 'Isotope ratio mass spectrometry', 'meaning': 'CHMO:0000506'},
}

class DerivatizationMethod(RichEnum):
    """
    Chemical derivatization methods for sample preparation
    """
    # Enum members
    SILYLATION = "SILYLATION"
    METHYLATION = "METHYLATION"
    ACETYLATION = "ACETYLATION"
    TRIFLUOROACETYLATION = "TRIFLUOROACETYLATION"
    ALKYLATION = "ALKYLATION"
    OXIMATION = "OXIMATION"

# Set metadata after class creation
DerivatizationMethod._metadata = {
    "SILYLATION": {'description': 'Addition of silyl groups for improved volatility', 'meaning': 'MSIO:0000117'},
    "METHYLATION": {'description': 'Addition of methyl groups', 'meaning': 'MSIO:0000115'},
    "ACETYLATION": {'description': 'Addition of acetyl groups', 'meaning': 'MSIO:0000112'},
    "TRIFLUOROACETYLATION": {'description': 'Addition of trifluoroacetyl groups', 'meaning': 'MSIO:0000113'},
    "ALKYLATION": {'description': 'Addition of alkyl groups', 'meaning': 'MSIO:0000114'},
    "OXIMATION": {'description': 'Addition of oxime groups', 'meaning': 'MSIO:0000116'},
}

class MetabolomicsAssayType(RichEnum):
    """
    Types of metabolomics assays and profiling approaches
    """
    # Enum members
    TARGETED_METABOLITE_PROFILING = "TARGETED_METABOLITE_PROFILING"
    UNTARGETED_METABOLITE_PROFILING = "UNTARGETED_METABOLITE_PROFILING"
    METABOLITE_QUANTITATION_HPLC = "METABOLITE_QUANTITATION_HPLC"

# Set metadata after class creation
MetabolomicsAssayType._metadata = {
    "TARGETED_METABOLITE_PROFILING": {'description': 'Assay targeting specific known metabolites', 'meaning': 'MSIO:0000100'},
    "UNTARGETED_METABOLITE_PROFILING": {'description': 'Assay profiling all detectable metabolites', 'meaning': 'MSIO:0000101'},
    "METABOLITE_QUANTITATION_HPLC": {'description': 'Metabolite quantitation using HPLC', 'meaning': 'MSIO:0000099'},
}

class AnalyticalControlType(RichEnum):
    """
    Types of control samples used in analytical chemistry
    """
    # Enum members
    INTERNAL_STANDARD = "INTERNAL_STANDARD"
    EXTERNAL_STANDARD = "EXTERNAL_STANDARD"
    POSITIVE_CONTROL = "POSITIVE_CONTROL"
    NEGATIVE_CONTROL = "NEGATIVE_CONTROL"
    LONG_TERM_REFERENCE = "LONG_TERM_REFERENCE"
    BLANK = "BLANK"
    QUALITY_CONTROL = "QUALITY_CONTROL"

# Set metadata after class creation
AnalyticalControlType._metadata = {
    "INTERNAL_STANDARD": {'description': 'Known amount of standard added to analytical sample', 'meaning': 'MSIO:0000005'},
    "EXTERNAL_STANDARD": {'description': 'Reference standard used as external reference point', 'meaning': 'MSIO:0000004'},
    "POSITIVE_CONTROL": {'description': 'Control providing known positive signal', 'meaning': 'MSIO:0000008'},
    "NEGATIVE_CONTROL": {'description': 'Control providing baseline/no signal reference', 'meaning': 'MSIO:0000007'},
    "LONG_TERM_REFERENCE": {'description': 'Stable reference for cross-batch comparisons', 'meaning': 'MSIO:0000006'},
    "BLANK": {'description': 'Sample containing only solvent/matrix without analyte'},
    "QUALITY_CONTROL": {'description': 'Sample with known composition for system performance monitoring'},
}

__all__ = [
    "RelativeTimeEnum",
    "PresenceEnum",
    "MassSpectrometerFileFormat",
    "MassSpectrometerVendor",
    "ChromatographyType",
    "DerivatizationMethod",
    "MetabolomicsAssayType",
    "AnalyticalControlType",
]