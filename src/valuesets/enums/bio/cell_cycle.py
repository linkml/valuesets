"""
Cell Cycle Value Sets

Value sets for cell cycle phases, checkpoints, and related concepts

Generated from: bio/cell_cycle.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

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
    "MEIOSIS_I": {'description': 'Meiosis I (reductional division)', 'meaning': 'GO:0007127', 'annotations': {'result': 'reduction from diploid to haploid', 'succeeded_by': 'MEIOSIS_II'}},
    "PROPHASE_I": {'description': 'Prophase I', 'meaning': 'GO:0007128', 'annotations': {'substages': 'leptotene, zygotene, pachytene, diplotene, diakinesis', 'succeeded_by': 'METAPHASE_I'}},
    "METAPHASE_I": {'description': 'Metaphase I', 'meaning': 'GO:0007132', 'annotations': {'feature': 'homologous pairs align', 'succeeded_by': 'ANAPHASE_I'}},
    "ANAPHASE_I": {'description': 'Anaphase I', 'meaning': 'GO:0007133', 'annotations': {'feature': 'homologous chromosomes separate', 'succeeded_by': 'TELOPHASE_I'}},
    "TELOPHASE_I": {'description': 'Telophase I', 'meaning': 'GO:0007134', 'annotations': {'succeeded_by': 'PROPHASE_II'}},
    "MEIOSIS_II": {'description': 'Meiosis II (equational division)', 'meaning': 'GO:0007135', 'annotations': {'similarity': 'similar to mitosis'}},
    "PROPHASE_II": {'description': 'Prophase II', 'meaning': 'GO:0007136', 'annotations': {'succeeded_by': 'METAPHASE_II'}},
    "METAPHASE_II": {'description': 'Metaphase II', 'meaning': 'GO:0007137', 'annotations': {'succeeded_by': 'ANAPHASE_II'}},
    "ANAPHASE_II": {'description': 'Anaphase II', 'meaning': 'GO:0007138', 'annotations': {'feature': 'sister chromatids separate', 'succeeded_by': 'TELOPHASE_II'}},
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
    "CELL_CYCLE_ARREST": {'description': 'Cell cycle arrest', 'meaning': 'GO:0051726', 'aliases': ['regulation of cell cycle']},
    "DNA_REPAIR": {'description': 'DNA repair', 'meaning': 'GO:0006281'},
    "APOPTOSIS_INDUCTION": {'description': 'Induction of apoptosis', 'meaning': 'GO:0043065', 'aliases': ['positive regulation of apoptotic process']},
    "SENESCENCE_INDUCTION": {'description': 'Induction of senescence', 'meaning': 'GO:0090400'},
    "CHECKPOINT_ADAPTATION": {'description': 'Checkpoint adaptation', 'annotations': {'description': 'override of checkpoint despite damage'}},
}

__all__ = [
    "CellCyclePhase",
    "MitoticPhase",
    "CellCycleCheckpoint",
    "MeioticPhase",
    "CellCycleRegulator",
    "CellProliferationState",
    "DNADamageResponse",
]