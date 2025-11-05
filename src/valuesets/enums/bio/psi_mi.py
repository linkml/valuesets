"""
PSI-MI (Molecular Interactions) Value Sets

Common value sets from the PSI-MI (Molecular Interactions) controlled vocabulary used for annotating protein-protein interaction experiments.

Generated from: bio/psi_mi.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class InteractionDetectionMethod(RichEnum):
    """
    Methods used to detect molecular interactions
    """
    # Enum members
    TWO_HYBRID = "TWO_HYBRID"
    COIMMUNOPRECIPITATION = "COIMMUNOPRECIPITATION"
    PULL_DOWN = "PULL_DOWN"
    TANDEM_AFFINITY_PURIFICATION = "TANDEM_AFFINITY_PURIFICATION"
    FLUORESCENCE_RESONANCE_ENERGY_TRANSFER = "FLUORESCENCE_RESONANCE_ENERGY_TRANSFER"
    SURFACE_PLASMON_RESONANCE = "SURFACE_PLASMON_RESONANCE"
    CROSS_LINKING = "CROSS_LINKING"
    X_RAY_CRYSTALLOGRAPHY = "X_RAY_CRYSTALLOGRAPHY"
    NMR = "NMR"
    ELECTRON_MICROSCOPY = "ELECTRON_MICROSCOPY"
    MASS_SPECTROMETRY = "MASS_SPECTROMETRY"
    PROXIMITY_LIGATION_ASSAY = "PROXIMITY_LIGATION_ASSAY"
    BIMOLECULAR_FLUORESCENCE_COMPLEMENTATION = "BIMOLECULAR_FLUORESCENCE_COMPLEMENTATION"
    YEAST_TWO_HYBRID = "YEAST_TWO_HYBRID"
    MAMMALIAN_TWO_HYBRID = "MAMMALIAN_TWO_HYBRID"

# Set metadata after class creation
InteractionDetectionMethod._metadata = {
    "TWO_HYBRID": {'description': 'Classical two-hybrid system using transcriptional activity', 'meaning': 'MI:0018'},
    "COIMMUNOPRECIPITATION": {'description': 'Using antibody to capture bait and its ligands', 'meaning': 'MI:0019'},
    "PULL_DOWN": {'description': 'Affinity capture using immobilized bait', 'meaning': 'MI:0096'},
    "TANDEM_AFFINITY_PURIFICATION": {'description': 'TAP tagging for protein complex purification', 'meaning': 'MI:0676'},
    "FLUORESCENCE_RESONANCE_ENERGY_TRANSFER": {'description': 'FRET for detecting proximity between molecules', 'meaning': 'MI:0055', 'aliases': ['fluorescent resonance energy transfer']},
    "SURFACE_PLASMON_RESONANCE": {'description': 'SPR for real-time binding analysis', 'meaning': 'MI:0107'},
    "CROSS_LINKING": {'description': 'Chemical cross-linking of interacting proteins', 'meaning': 'MI:0030', 'aliases': ['cross-linking study']},
    "X_RAY_CRYSTALLOGRAPHY": {'description': 'Crystal structure determination', 'meaning': 'MI:0114'},
    "NMR": {'description': 'Nuclear magnetic resonance spectroscopy', 'meaning': 'MI:0077', 'aliases': ['nuclear magnetic resonance']},
    "ELECTRON_MICROSCOPY": {'description': 'EM for structural determination', 'meaning': 'MI:0040'},
    "MASS_SPECTROMETRY": {'description': 'MS-based interaction detection', 'meaning': 'MI:0943', 'aliases': ['detection by mass spectrometry']},
    "PROXIMITY_LIGATION_ASSAY": {'description': 'PLA for detecting protein proximity', 'meaning': 'MI:0813'},
    "BIMOLECULAR_FLUORESCENCE_COMPLEMENTATION": {'description': 'BiFC split fluorescent protein assay', 'meaning': 'MI:0809'},
    "YEAST_TWO_HYBRID": {'description': 'Y2H screening in yeast', 'meaning': 'MI:0018', 'aliases': ['two hybrid']},
    "MAMMALIAN_TWO_HYBRID": {'description': 'Two-hybrid in mammalian cells', 'meaning': 'MI:2413', 'aliases': ['mammalian membrane two hybrid']},
}

class InteractionType(RichEnum):
    """
    Types of molecular interactions
    """
    # Enum members
    PHYSICAL_ASSOCIATION = "PHYSICAL_ASSOCIATION"
    DIRECT_INTERACTION = "DIRECT_INTERACTION"
    ASSOCIATION = "ASSOCIATION"
    COLOCALIZATION = "COLOCALIZATION"
    FUNCTIONAL_ASSOCIATION = "FUNCTIONAL_ASSOCIATION"
    ENZYMATIC_REACTION = "ENZYMATIC_REACTION"
    PHOSPHORYLATION_REACTION = "PHOSPHORYLATION_REACTION"
    UBIQUITINATION_REACTION = "UBIQUITINATION_REACTION"
    ACETYLATION_REACTION = "ACETYLATION_REACTION"
    METHYLATION_REACTION = "METHYLATION_REACTION"
    CLEAVAGE_REACTION = "CLEAVAGE_REACTION"
    GENETIC_INTERACTION = "GENETIC_INTERACTION"
    SELF_INTERACTION = "SELF_INTERACTION"

# Set metadata after class creation
InteractionType._metadata = {
    "PHYSICAL_ASSOCIATION": {'description': 'Molecules within the same physical complex', 'meaning': 'MI:0915'},
    "DIRECT_INTERACTION": {'description': 'Direct physical contact between molecules', 'meaning': 'MI:0407'},
    "ASSOCIATION": {'description': 'May form one or more physical complexes', 'meaning': 'MI:0914'},
    "COLOCALIZATION": {'description': 'Coincident occurrence in subcellular location', 'meaning': 'MI:0403'},
    "FUNCTIONAL_ASSOCIATION": {'description': 'Functional modulation without direct contact', 'meaning': 'MI:2286'},
    "ENZYMATIC_REACTION": {'description': 'Enzyme-substrate relationship', 'meaning': 'MI:0414'},
    "PHOSPHORYLATION_REACTION": {'description': 'Kinase-substrate phosphorylation', 'meaning': 'MI:0217'},
    "UBIQUITINATION_REACTION": {'description': 'Ubiquitin ligase-substrate relationship', 'meaning': 'MI:0220'},
    "ACETYLATION_REACTION": {'description': 'Acetyltransferase-substrate relationship', 'meaning': 'MI:0192'},
    "METHYLATION_REACTION": {'description': 'Methyltransferase-substrate relationship', 'meaning': 'MI:0213'},
    "CLEAVAGE_REACTION": {'description': 'Protease-substrate relationship', 'meaning': 'MI:0194'},
    "GENETIC_INTERACTION": {'description': 'Genetic epistatic relationship', 'meaning': 'MI:0208', 'aliases': ['genetic interaction (sensu unexpected)']},
    "SELF_INTERACTION": {'description': 'Intra-molecular interaction', 'meaning': 'MI:1126'},
}

class ExperimentalRole(RichEnum):
    """
    Role played by a participant in the experiment
    """
    # Enum members
    BAIT = "BAIT"
    PREY = "PREY"
    NEUTRAL_COMPONENT = "NEUTRAL_COMPONENT"
    ENZYME = "ENZYME"
    ENZYME_TARGET = "ENZYME_TARGET"
    SELF = "SELF"
    PUTATIVE_SELF = "PUTATIVE_SELF"
    ANCILLARY = "ANCILLARY"
    COFACTOR = "COFACTOR"
    INHIBITOR = "INHIBITOR"
    STIMULATOR = "STIMULATOR"
    COMPETITOR = "COMPETITOR"

# Set metadata after class creation
ExperimentalRole._metadata = {
    "BAIT": {'description': 'Molecule used to capture interacting partners', 'meaning': 'MI:0496'},
    "PREY": {'description': 'Molecule captured by the bait', 'meaning': 'MI:0498'},
    "NEUTRAL_COMPONENT": {'description': 'Participant with no specific role', 'meaning': 'MI:0497'},
    "ENZYME": {'description': 'Catalytically active participant', 'meaning': 'MI:0501'},
    "ENZYME_TARGET": {'description': 'Target of enzymatic activity', 'meaning': 'MI:0502'},
    "SELF": {'description': 'Self-interaction participant', 'meaning': 'MI:0503'},
    "PUTATIVE_SELF": {'description': 'Potentially self-interacting', 'meaning': 'MI:0898'},
    "ANCILLARY": {'description': 'Supporting but not directly interacting', 'meaning': 'MI:0684'},
    "COFACTOR": {'description': 'Required cofactor for interaction', 'meaning': 'MI:0682'},
    "INHIBITOR": {'description': 'Inhibitor of the interaction', 'meaning': 'MI:0586'},
    "STIMULATOR": {'description': 'Enhancer of the interaction', 'meaning': 'MI:0840'},
    "COMPETITOR": {'description': 'Competitive inhibitor', 'meaning': 'MI:0941'},
}

class BiologicalRole(RichEnum):
    """
    Physiological role of an interactor
    """
    # Enum members
    ENZYME = "ENZYME"
    ENZYME_TARGET = "ENZYME_TARGET"
    ELECTRON_DONOR = "ELECTRON_DONOR"
    ELECTRON_ACCEPTOR = "ELECTRON_ACCEPTOR"
    INHIBITOR = "INHIBITOR"
    COFACTOR = "COFACTOR"
    LIGAND = "LIGAND"
    AGONIST = "AGONIST"
    ANTAGONIST = "ANTAGONIST"
    PHOSPHATE_DONOR = "PHOSPHATE_DONOR"
    PHOSPHATE_ACCEPTOR = "PHOSPHATE_ACCEPTOR"

# Set metadata after class creation
BiologicalRole._metadata = {
    "ENZYME": {'description': 'Catalytically active molecule', 'meaning': 'MI:0501'},
    "ENZYME_TARGET": {'description': 'Substrate of enzymatic activity', 'meaning': 'MI:0502'},
    "ELECTRON_DONOR": {'description': 'Donates electrons in reaction', 'meaning': 'MI:0579'},
    "ELECTRON_ACCEPTOR": {'description': 'Accepts electrons in reaction', 'meaning': 'MI:0580'},
    "INHIBITOR": {'description': 'Inhibits activity or interaction', 'meaning': 'MI:0586'},
    "COFACTOR": {'description': 'Required for activity', 'meaning': 'MI:0682'},
    "LIGAND": {'description': 'Small molecule binding partner'},
    "AGONIST": {'description': 'Activates receptor', 'meaning': 'MI:0625'},
    "ANTAGONIST": {'description': 'Blocks receptor activation', 'meaning': 'MI:0626'},
    "PHOSPHATE_DONOR": {'description': 'Provides phosphate group', 'meaning': 'MI:0842'},
    "PHOSPHATE_ACCEPTOR": {'description': 'Receives phosphate group', 'meaning': 'MI:0843'},
}

class ParticipantIdentificationMethod(RichEnum):
    """
    Methods to identify interaction participants
    """
    # Enum members
    MASS_SPECTROMETRY = "MASS_SPECTROMETRY"
    WESTERN_BLOT = "WESTERN_BLOT"
    SEQUENCE_TAG_IDENTIFICATION = "SEQUENCE_TAG_IDENTIFICATION"
    ANTIBODY_DETECTION = "ANTIBODY_DETECTION"
    PREDETERMINED = "PREDETERMINED"
    NUCLEIC_ACID_SEQUENCING = "NUCLEIC_ACID_SEQUENCING"
    PROTEIN_SEQUENCING = "PROTEIN_SEQUENCING"

# Set metadata after class creation
ParticipantIdentificationMethod._metadata = {
    "MASS_SPECTROMETRY": {'description': 'MS-based protein identification', 'meaning': 'MI:0943', 'aliases': ['detection by mass spectrometry']},
    "WESTERN_BLOT": {'description': 'Antibody-based detection', 'meaning': 'MI:0113'},
    "SEQUENCE_TAG_IDENTIFICATION": {'description': 'Using affinity tags', 'meaning': 'MI:0102'},
    "ANTIBODY_DETECTION": {'description': 'Direct antibody recognition', 'meaning': 'MI:0678', 'aliases': ['antibody array']},
    "PREDETERMINED": {'description': 'Known from experimental design', 'meaning': 'MI:0396', 'aliases': ['predetermined participant']},
    "NUCLEIC_ACID_SEQUENCING": {'description': 'DNA/RNA sequencing', 'meaning': 'MI:0078', 'aliases': ['nucleotide sequence identification']},
    "PROTEIN_SEQUENCING": {'description': 'Direct protein sequencing'},
}

class FeatureType(RichEnum):
    """
    Molecular features affecting interactions
    """
    # Enum members
    BINDING_SITE = "BINDING_SITE"
    MUTATION = "MUTATION"
    POST_TRANSLATIONAL_MODIFICATION = "POST_TRANSLATIONAL_MODIFICATION"
    TAG = "TAG"
    CROSS_LINK = "CROSS_LINK"
    LIPIDATION_SITE = "LIPIDATION_SITE"
    PHOSPHORYLATION_SITE = "PHOSPHORYLATION_SITE"
    UBIQUITINATION_SITE = "UBIQUITINATION_SITE"
    METHYLATION_SITE = "METHYLATION_SITE"
    ACETYLATION_SITE = "ACETYLATION_SITE"
    SUMOYLATION_SITE = "SUMOYLATION_SITE"
    NECESSARY_BINDING_REGION = "NECESSARY_BINDING_REGION"
    SUFFICIENT_BINDING_REGION = "SUFFICIENT_BINDING_REGION"

# Set metadata after class creation
FeatureType._metadata = {
    "BINDING_SITE": {'description': 'Region involved in binding', 'meaning': 'MI:0117', 'aliases': ['binding-associated region']},
    "MUTATION": {'description': 'Sequence alteration', 'meaning': 'MI:0118'},
    "POST_TRANSLATIONAL_MODIFICATION": {'description': 'PTM site', 'meaning': 'MI:0121', 'aliases': ['acetylated residue']},
    "TAG": {'description': 'Affinity or epitope tag', 'meaning': 'MI:0507'},
    "CROSS_LINK": {'description': 'Cross-linking site'},
    "LIPIDATION_SITE": {'description': 'Lipid modification site'},
    "PHOSPHORYLATION_SITE": {'description': 'Phosphorylated residue', 'meaning': 'MI:0170', 'aliases': ['phosphorylated residue']},
    "UBIQUITINATION_SITE": {'description': 'Ubiquitinated residue'},
    "METHYLATION_SITE": {'description': 'Methylated residue'},
    "ACETYLATION_SITE": {'description': 'Acetylated residue'},
    "SUMOYLATION_SITE": {'description': 'SUMOylated residue'},
    "NECESSARY_BINDING_REGION": {'description': 'Required for binding', 'meaning': 'MI:0429'},
    "SUFFICIENT_BINDING_REGION": {'description': 'Sufficient for binding', 'meaning': 'MI:0442'},
}

class InteractorType(RichEnum):
    """
    Types of molecular species in interactions
    """
    # Enum members
    PROTEIN = "PROTEIN"
    PEPTIDE = "PEPTIDE"
    SMALL_MOLECULE = "SMALL_MOLECULE"
    DNA = "DNA"
    RNA = "RNA"
    PROTEIN_COMPLEX = "PROTEIN_COMPLEX"
    GENE = "GENE"
    BIOPOLYMER = "BIOPOLYMER"
    POLYSACCHARIDE = "POLYSACCHARIDE"
    LIPID = "LIPID"
    NUCLEIC_ACID = "NUCLEIC_ACID"
    SYNTHETIC_POLYMER = "SYNTHETIC_POLYMER"
    METAL_ION = "METAL_ION"

# Set metadata after class creation
InteractorType._metadata = {
    "PROTEIN": {'description': 'Polypeptide molecule', 'meaning': 'MI:0326'},
    "PEPTIDE": {'description': 'Short polypeptide', 'meaning': 'MI:0327'},
    "SMALL_MOLECULE": {'description': 'Small chemical compound', 'meaning': 'MI:0328'},
    "DNA": {'description': 'Deoxyribonucleic acid', 'meaning': 'MI:0319', 'aliases': ['deoxyribonucleic acid']},
    "RNA": {'description': 'Ribonucleic acid', 'meaning': 'MI:0320', 'aliases': ['ribonucleic acid']},
    "PROTEIN_COMPLEX": {'description': 'Multi-protein assembly', 'meaning': 'MI:0314', 'aliases': ['complex']},
    "GENE": {'description': 'Gene locus', 'meaning': 'MI:0250'},
    "BIOPOLYMER": {'description': 'Biological polymer', 'meaning': 'MI:0383'},
    "POLYSACCHARIDE": {'description': 'Carbohydrate polymer', 'meaning': 'MI:0904'},
    "LIPID": {'description': 'Lipid molecule'},
    "NUCLEIC_ACID": {'description': 'DNA or RNA', 'meaning': 'MI:0318'},
    "SYNTHETIC_POLYMER": {'description': 'Artificial polymer'},
    "METAL_ION": {'description': 'Metal ion cofactor'},
}

class ConfidenceScore(RichEnum):
    """
    Types of confidence scoring methods
    """
    # Enum members
    INTACT_MISCORE = "INTACT_MISCORE"
    AUTHOR_CONFIDENCE = "AUTHOR_CONFIDENCE"
    INTACT_CONFIDENCE = "INTACT_CONFIDENCE"
    MINT_SCORE = "MINT_SCORE"
    MATRIXDB_SCORE = "MATRIXDB_SCORE"

# Set metadata after class creation
ConfidenceScore._metadata = {
    "INTACT_MISCORE": {'description': 'IntAct molecular interaction score'},
    "AUTHOR_CONFIDENCE": {'description': 'Author-provided confidence', 'meaning': 'MI:0621'},
    "INTACT_CONFIDENCE": {'description': 'IntAct curation confidence'},
    "MINT_SCORE": {'description': 'MINT database score'},
    "MATRIXDB_SCORE": {'description': 'MatrixDB confidence score'},
}

class ExperimentalPreparation(RichEnum):
    """
    Sample preparation methods
    """
    # Enum members
    RECOMBINANT_EXPRESSION = "RECOMBINANT_EXPRESSION"
    NATIVE_SOURCE = "NATIVE_SOURCE"
    IN_VITRO_EXPRESSION = "IN_VITRO_EXPRESSION"
    OVEREXPRESSION = "OVEREXPRESSION"
    KNOCKDOWN = "KNOCKDOWN"
    KNOCKOUT = "KNOCKOUT"
    ENDOGENOUS_LEVEL = "ENDOGENOUS_LEVEL"

# Set metadata after class creation
ExperimentalPreparation._metadata = {
    "RECOMBINANT_EXPRESSION": {'description': 'Expressed in heterologous system'},
    "NATIVE_SOURCE": {'description': 'From original organism'},
    "IN_VITRO_EXPRESSION": {'description': 'Cell-free expression'},
    "OVEREXPRESSION": {'description': 'Above physiological levels', 'meaning': 'MI:0506', 'aliases': ['over expressed level']},
    "KNOCKDOWN": {'description': 'Reduced expression'},
    "KNOCKOUT": {'description': 'Gene deletion', 'meaning': 'MI:0788', 'aliases': ['knock out']},
    "ENDOGENOUS_LEVEL": {'description': 'Physiological expression'},
}

__all__ = [
    "InteractionDetectionMethod",
    "InteractionType",
    "ExperimentalRole",
    "BiologicalRole",
    "ParticipantIdentificationMethod",
    "FeatureType",
    "InteractorType",
    "ConfidenceScore",
    "ExperimentalPreparation",
]