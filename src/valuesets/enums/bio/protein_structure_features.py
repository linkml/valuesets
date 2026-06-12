"""
Protein 3D Local Structure Feature Value Sets

Value sets describing fine-grained, local three-dimensional features of protein structures: per-residue secondary structure states, super-secondary structural motifs, functional sites, and local geometric features (pockets, clefts, elbows).

These provide a curated, human-interpretable, ontology-mapped counterpart to the learned per-residue feature vocabularies produced by protein language models -- e.g. the 8-state secondary structure (SS8) track and structure-token codebook of ESM3, and the ~16,000 sparse-autoencoder feature dictionaries served per-residue by interpretability APIs (InterPLM; the Biohub/EvolutionaryScale ESMC SAE, model biohub/ESMC-6B-sae-layer60-k64-codebook16384). Where curated ontology terms exist they are mapped via ``meaning:``; geometric surface features (pocket, cleft, cavity, elbow, groove, tunnel) currently have no suitable OBO term and are flagged as gaps.


Generated from: bio/protein_structure_features.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class SecondaryStructureType(RichEnum):
    """
    Per-residue secondary structure assignment. The permissible values correspond to the canonical DSSP 8-state (SS8) classification, which is also the secondary-structure track vocabulary used by protein language models such as ESM3. The single-letter DSSP code is recorded in the ``dssp_code`` annotation.
    """
    # Enum members
    ALPHA_HELIX = "ALPHA_HELIX"
    THREE_TEN_HELIX = "THREE_TEN_HELIX"
    PI_HELIX = "PI_HELIX"
    BETA_STRAND = "BETA_STRAND"
    BETA_BRIDGE = "BETA_BRIDGE"
    TURN = "TURN"
    BEND = "BEND"
    COIL = "COIL"

# Set metadata after class creation
SecondaryStructureType._metadata = {
    "ALPHA_HELIX": {'description': 'Right-handed alpha helix (3.6 residues/turn, i to i+4 hydrogen bonding)', 'meaning': 'SO:0001117', 'annotations': {'dssp_code': 'H', 'ss8_class': 'H'}},
    "THREE_TEN_HELIX": {'description': '3-10 helix (3 residues/turn, i to i+3 hydrogen bonding)', 'meaning': 'SO:0001119', 'annotations': {'dssp_code': 'G', 'ss8_class': 'G'}},
    "PI_HELIX": {'description': 'Pi helix (4.1 residues/turn, i to i+5 hydrogen bonding)', 'meaning': 'SO:0001118', 'annotations': {'dssp_code': 'I', 'ss8_class': 'I'}},
    "BETA_STRAND": {'description': 'Extended beta strand participating in a beta sheet', 'meaning': 'SO:0001111', 'annotations': {'dssp_code': 'E', 'ss8_class': 'E'}},
    "BETA_BRIDGE": {'description': 'Residue in an isolated single-pair beta bridge', 'annotations': {'dssp_code': 'B', 'ss8_class': 'B', 'ontology_gap': 'true'}},
    "TURN": {'description': 'Hydrogen-bonded turn reversing backbone direction over <=4 residues', 'meaning': 'SO:0001128', 'annotations': {'dssp_code': 'T', 'ss8_class': 'T'}},
    "BEND": {'description': 'Region of high backbone curvature without regular hydrogen bonding', 'annotations': {'dssp_code': 'S', 'ss8_class': 'S', 'ontology_gap': 'true'}},
    "COIL": {'description': 'Irregular, unstructured backbone region (loop / random coil)', 'meaning': 'SO:0100012', 'annotations': {'dssp_code': 'C', 'ss8_class': 'C', 'aliases': 'loop, random coil, blank'}},
}

class LocalStructuralFeature(RichEnum):
    """
    Fine-grained local three-dimensional features of protein structures, spanning super-secondary structural motifs, functional sites, and local geometric surface features. This is the curated, ontology-mapped analogue of the learned per-residue feature vocabularies produced by protein language models and their sparse-autoencoder interpretations. Members marked with the ``ontology_gap`` annotation have no suitable OBO term and are candidates for new ontology terms.
    """
    # Enum members
    POLYPEPTIDE_STRUCTURAL_MOTIF = "POLYPEPTIDE_STRUCTURAL_MOTIF"
    BETA_HAIRPIN = "BETA_HAIRPIN"
    BETA_BULGE = "BETA_BULGE"
    ASX_MOTIF = "ASX_MOTIF"
    NEST = "NEST"
    COILED_COIL = "COILED_COIL"
    HELIX_CAP = "HELIX_CAP"
    CATALYTIC_RESIDUE = "CATALYTIC_RESIDUE"
    PROTEIN_BINDING_SITE = "PROTEIN_BINDING_SITE"
    DISULFIDE_BOND = "DISULFIDE_BOND"
    METAL_BINDING_SITE = "METAL_BINDING_SITE"
    POCKET = "POCKET"
    CLEFT = "CLEFT"
    CAVITY = "CAVITY"
    TUNNEL = "TUNNEL"
    GROOVE = "GROOVE"
    ELBOW = "ELBOW"
    KINK = "KINK"
    INTERFACE = "INTERFACE"

# Set metadata after class creation
LocalStructuralFeature._metadata = {
    "POLYPEPTIDE_STRUCTURAL_MOTIF": {'description': 'A recurring 3D structural element within the chain that does not form a stable globular unit (the general parent class for local motifs)', 'meaning': 'SO:0001079'},
    "BETA_HAIRPIN": {'description': 'Two adjacent antiparallel beta strands connected by a short loop or turn', 'annotations': {'ontology_gap': 'true'}},
    "BETA_BULGE": {'description': 'A local disruption of beta-sheet hydrogen bonding across three residues', 'meaning': 'SO:0001107'},
    "ASX_MOTIF": {'description': 'A five-residue motif nucleated by an Asp/Asn side chain (Asx)', 'meaning': 'SO:0001106'},
    "NEST": {'description': 'A motif of two consecutive residues forming an anion-binding concavity', 'meaning': 'SO:0001120'},
    "COILED_COIL": {'description': 'Two or more alpha helices wound together like strands of a rope', 'meaning': 'SO:0001080'},
    "HELIX_CAP": {'description': 'N-cap or C-cap residue terminating an alpha helix', 'annotations': {'ontology_gap': 'true'}},
    "CATALYTIC_RESIDUE": {'description': 'An amino acid residue directly involved in enzyme catalysis (active site)', 'meaning': 'SO:0001104'},
    "PROTEIN_BINDING_SITE": {'description': 'A site that interacts selectively and non-covalently with polypeptide molecules', 'meaning': 'SO:0000410'},
    "DISULFIDE_BOND": {'description': 'A covalent S-S bond between two cysteine residues', 'annotations': {'obo_gap': 'true'}},
    "METAL_BINDING_SITE": {'description': 'A local site coordinating one or more metal ions', 'annotations': {'obo_gap': 'true'}},
    "POCKET": {'description': 'A concave, solvent-accessible surface depression that can accommodate a ligand', 'annotations': {'ontology_gap': 'true', 'related_edam': 'EDAM:data_1542'}},
    "CLEFT": {'description': 'An elongated surface groove between structural elements or domains', 'annotations': {'ontology_gap': 'true'}},
    "CAVITY": {'description': 'An enclosed, solvent-inaccessible internal void within the structure', 'annotations': {'ontology_gap': 'true', 'related_edam': 'EDAM:data_1542'}},
    "TUNNEL": {'description': 'An elongated, often buried, passage through the structure connecting two regions', 'annotations': {'ontology_gap': 'true'}},
    "GROOVE": {'description': 'A surface channel, e.g. a nucleic-acid-binding groove', 'annotations': {'ontology_gap': 'true'}},
    "ELBOW": {'description': 'A localized bend or hinge between two structural elements or domains', 'annotations': {'ontology_gap': 'true'}},
    "KINK": {'description': 'A localized bend interrupting the regular geometry of a helix', 'annotations': {'ontology_gap': 'true'}},
    "INTERFACE": {'description': 'A surface patch mediating contact with another chain or molecule', 'annotations': {'ontology_gap': 'true'}},
}

__all__ = [
    "SecondaryStructureType",
    "LocalStructuralFeature",
]