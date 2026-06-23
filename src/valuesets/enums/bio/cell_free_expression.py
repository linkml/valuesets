"""
Cell-Free Expression Value Sets

Value sets for cell-free protein synthesis (CFPS), also known as cell-free expression or in vitro transcription-translation (TX-TL). Covers the source extracts/systems, reaction formats, energy regeneration substrates, and common applications used in synthetic biology, structural biology, and biomanufacturing.

Generated from: bio/cell_free_expression.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class CellFreeExpressionSystemEnum(RichEnum):
    """
    Source extracts and reconstituted systems used for cell-free protein synthesis. Crude lysate systems are derived from cell extracts, while reconstituted systems (e.g. PURE) are assembled from purified components.
    """
    # Enum members
    ECOLI_EXTRACT = "ECOLI_EXTRACT"
    PURE_SYSTEM = "PURE_SYSTEM"
    WHEAT_GERM_EXTRACT = "WHEAT_GERM_EXTRACT"
    RABBIT_RETICULOCYTE_LYSATE = "RABBIT_RETICULOCYTE_LYSATE"
    INSECT_CELL_EXTRACT = "INSECT_CELL_EXTRACT"
    HELA_EXTRACT = "HELA_EXTRACT"
    CHO_EXTRACT = "CHO_EXTRACT"
    YEAST_EXTRACT = "YEAST_EXTRACT"
    LEISHMANIA_EXTRACT = "LEISHMANIA_EXTRACT"
    VIBRIO_NATRIEGENS_EXTRACT = "VIBRIO_NATRIEGENS_EXTRACT"
    TOBACCO_BY2_EXTRACT = "TOBACCO_BY2_EXTRACT"

# Set metadata after class creation
CellFreeExpressionSystemEnum._metadata = {
    "ECOLI_EXTRACT": {'description': 'Escherichia coli crude cell extract (e.g. S30, S12), the most widely used prokaryotic cell-free system for high-yield protein production', 'annotations': {'source_taxon': 'NCBITaxon:562', 'extract_type': 'crude lysate', 'domain': 'prokaryotic'}, 'aliases': ['E. coli extract', 'E. coli lysate', 'S30 extract', 'ECE']},
    "PURE_SYSTEM": {'description': 'Protein synthesis Using Recombinant Elements - a reconstituted system assembled from individually purified E. coli translation factors, ribosomes, and enzymes', 'annotations': {'extract_type': 'reconstituted', 'domain': 'prokaryotic', 'advantage': 'defined composition, low nuclease/protease activity'}, 'aliases': ['PURE', 'PURExpress', 'reconstituted system']},
    "WHEAT_GERM_EXTRACT": {'description': 'Wheat germ (Triticum aestivum) extract, a eukaryotic system favored for expression of complex and difficult eukaryotic proteins', 'annotations': {'source_taxon': 'NCBITaxon:4565', 'extract_type': 'crude lysate', 'domain': 'eukaryotic'}, 'aliases': ['WGE', 'wheat germ system']},
    "RABBIT_RETICULOCYTE_LYSATE": {'description': 'Rabbit (Oryctolagus cuniculus) reticulocyte lysate, a classic mammalian system for in vitro translation and protein labeling', 'meaning': 'BAO:0000255', 'annotations': {'source_taxon': 'NCBITaxon:9986', 'extract_type': 'crude lysate', 'domain': 'eukaryotic'}, 'aliases': ['RRL', 'reticulocyte lysate', 'rabbit reticulocyte lysate format']},
    "INSECT_CELL_EXTRACT": {'description': 'Insect cell extract, typically from Spodoptera frugiperda (Sf21), supporting eukaryotic post-translational modifications', 'annotations': {'source_taxon': 'NCBITaxon:7108', 'extract_type': 'crude lysate', 'domain': 'eukaryotic'}, 'aliases': ['ICE', 'Sf21 extract', 'insect lysate']},
    "HELA_EXTRACT": {'description': 'Human HeLa cell extract used for mammalian cell-free expression with authentic human translation machinery', 'annotations': {'source_taxon': 'NCBITaxon:9606', 'extract_type': 'crude lysate', 'domain': 'eukaryotic'}, 'aliases': ['HeLa lysate', 'human cell extract']},
    "CHO_EXTRACT": {'description': 'Chinese hamster ovary (Cricetulus griseus) cell extract supporting glycosylation and disulfide bond formation', 'annotations': {'source_taxon': 'NCBITaxon:10029', 'extract_type': 'crude lysate', 'domain': 'eukaryotic'}, 'aliases': ['CHO lysate']},
    "YEAST_EXTRACT": {'description': 'Yeast (Saccharomyces cerevisiae) cell extract for eukaryotic cell-free protein synthesis', 'annotations': {'source_taxon': 'NCBITaxon:4932', 'extract_type': 'crude lysate', 'domain': 'eukaryotic'}, 'aliases': ['S. cerevisiae extract', 'yeast lysate']},
    "LEISHMANIA_EXTRACT": {'description': 'Leishmania tarentolae cell extract, a eukaryotic system supporting high yields and post-translational modifications', 'annotations': {'source_taxon': 'NCBITaxon:5689', 'extract_type': 'crude lysate', 'domain': 'eukaryotic'}, 'aliases': ['Leishmania tarentolae extract', 'LTE']},
    "VIBRIO_NATRIEGENS_EXTRACT": {'description': 'Vibrio natriegens cell extract, an emerging fast-growing prokaryotic chassis for rapid, high-yield cell-free expression', 'annotations': {'source_taxon': 'NCBITaxon:691', 'extract_type': 'crude lysate', 'domain': 'prokaryotic'}, 'aliases': ['V. natriegens extract', 'Vmax extract']},
    "TOBACCO_BY2_EXTRACT": {'description': 'Tobacco BY-2 (Nicotiana tabacum bright yellow-2) cell lysate, a plant eukaryotic cell-free system', 'annotations': {'extract_type': 'crude lysate', 'domain': 'eukaryotic'}, 'aliases': ['BY-2 lysate', 'BYL']},
}

class CellFreeReactionFormatEnum(RichEnum):
    """
    Physical configurations of cell-free expression reactions, differing in how substrates are supplied and byproducts removed, which affects reaction duration and protein yield.
    """
    # Enum members
    BATCH = "BATCH"
    CONTINUOUS_EXCHANGE = "CONTINUOUS_EXCHANGE"
    CONTINUOUS_FLOW = "CONTINUOUS_FLOW"
    BILAYER = "BILAYER"
    LYOPHILIZED = "LYOPHILIZED"

# Set metadata after class creation
CellFreeReactionFormatEnum._metadata = {
    "BATCH": {'description': 'Single closed reaction with all components mixed at the start; simplest format but limited by substrate depletion and byproduct accumulation', 'annotations': {'duration': 'short (hours)'}, 'aliases': ['batch mode']},
    "CONTINUOUS_EXCHANGE": {'description': 'Continuous-exchange cell-free (CECF) format with a semipermeable membrane separating a reaction chamber from a feeding chamber, allowing diffusion of substrates in and byproducts out', 'annotations': {'duration': 'extended (up to ~24 h)'}, 'aliases': ['CECF', 'continuous exchange', 'dialysis mode']},
    "CONTINUOUS_FLOW": {'description': 'Continuous-flow cell-free (CFCF) format in which fresh substrates are continuously pumped through the reaction while product is collected', 'annotations': {'duration': 'extended'}, 'aliases': ['CFCF', 'continuous flow']},
    "BILAYER": {'description': 'Bilayer format where a feeding solution is layered over the reaction mixture without a membrane, prolonging reaction by passive diffusion', 'aliases': ['bilayer mode']},
    "LYOPHILIZED": {'description': 'Freeze-dried (lyophilized) cell-free reaction that is shelf-stable and activated by rehydration; basis of freeze-dried cell-free (FD-CF) diagnostics and portable biomanufacturing', 'annotations': {'advantage': 'cold-chain-free storage and distribution'}, 'aliases': ['freeze-dried', 'FD-CF', 'lyophilised']},
}

class EnergyRegenerationSubstrateEnum(RichEnum):
    """
    Secondary energy substrates added to cell-free reactions to regenerate ATP and GTP consumed during transcription and translation. Choice of substrate affects cost, reaction longevity, and inorganic phosphate accumulation.
    """
    # Enum members
    PHOSPHOCREATINE = "PHOSPHOCREATINE"
    PHOSPHOENOLPYRUVATE = "PHOSPHOENOLPYRUVATE"
    ACETYL_PHOSPHATE = "ACETYL_PHOSPHATE"
    THREE_PGA = "THREE_PGA"
    GLUCOSE = "GLUCOSE"
    GLUCOSE_6_PHOSPHATE = "GLUCOSE_6_PHOSPHATE"
    MALTOSE = "MALTOSE"
    PYRUVATE = "PYRUVATE"
    MALTODEXTRIN = "MALTODEXTRIN"

# Set metadata after class creation
EnergyRegenerationSubstrateEnum._metadata = {
    "PHOSPHOCREATINE": {'description': 'Creatine phosphate (N-phosphocreatine) regenerated with creatine kinase; a classic high-energy phosphate donor', 'meaning': 'CHEBI:17287', 'annotations': {'enzyme': 'creatine kinase'}, 'aliases': ['creatine phosphate', 'phosphocreatine', 'N-phosphocreatine']},
    "PHOSPHOENOLPYRUVATE": {'description': 'Phosphoenolpyruvate (PEP) regenerated with pyruvate kinase; a common high-energy phosphate donor', 'meaning': 'CHEBI:18021', 'annotations': {'enzyme': 'pyruvate kinase'}, 'aliases': ['PEP']},
    "ACETYL_PHOSPHATE": {'description': 'Acetyl phosphate regenerated with acetate kinase; an inexpensive energy source', 'meaning': 'CHEBI:15350', 'annotations': {'enzyme': 'acetate kinase'}, 'aliases': ['AcP', 'acetyl dihydrogen phosphate']},
    "THREE_PGA": {'description': '3-phosphoglycerate (3-PGA), a glycolytic intermediate widely used as a low-cost energy substrate in E. coli cell-free systems', 'meaning': 'CHEBI:17794', 'aliases': ['3-PGA', '3-phosphoglycerate', '3-phospho-D-glycerate', '3-phospho-D-glyceric acid']},
    "GLUCOSE": {'description': 'Glucose feeding glycolysis for ATP regeneration; a very low-cost energy source that requires phosphate buffering', 'meaning': 'CHEBI:17634', 'aliases': ['D-glucose']},
    "GLUCOSE_6_PHOSPHATE": {'description': 'Glucose 6-phosphate fed into glycolysis for energy regeneration', 'meaning': 'CHEBI:14314', 'aliases': ['G6P', 'glucose-6-phosphate', 'D-glucose 6-phosphate']},
    "MALTOSE": {'description': 'Maltose used as a low-cost energy substrate that limits inorganic phosphate accumulation', 'meaning': 'CHEBI:17306'},
    "PYRUVATE": {'description': 'Pyruvate used as an energy source, oxidized via the central metabolism of the extract', 'meaning': 'CHEBI:15361'},
    "MALTODEXTRIN": {'description': 'Maltodextrin (glucose polymer) energy substrate providing slow glucose release and minimal phosphate buildup', 'aliases': ['polymeric glucose']},
}

class CellFreeApplicationEnum(RichEnum):
    """
    Common applications and use cases for cell-free protein synthesis across research, synthetic biology, and biomanufacturing.
    """
    # Enum members
    RECOMBINANT_PROTEIN_PRODUCTION = "RECOMBINANT_PROTEIN_PRODUCTION"
    MEMBRANE_PROTEIN_EXPRESSION = "MEMBRANE_PROTEIN_EXPRESSION"
    DIFFICULT_PROTEIN_EXPRESSION = "DIFFICULT_PROTEIN_EXPRESSION"
    GENETIC_CIRCUIT_PROTOTYPING = "GENETIC_CIRCUIT_PROTOTYPING"
    METABOLIC_PATHWAY_PROTOTYPING = "METABOLIC_PATHWAY_PROTOTYPING"
    BIOSENSOR = "BIOSENSOR"
    DIAGNOSTICS = "DIAGNOSTICS"
    UNNATURAL_AMINO_ACID_INCORPORATION = "UNNATURAL_AMINO_ACID_INCORPORATION"
    PROTEIN_LABELING = "PROTEIN_LABELING"
    STRUCTURAL_BIOLOGY = "STRUCTURAL_BIOLOGY"
    HIGH_THROUGHPUT_SCREENING = "HIGH_THROUGHPUT_SCREENING"
    VACCINE_PRODUCTION = "VACCINE_PRODUCTION"
    ANTIBODY_PRODUCTION = "ANTIBODY_PRODUCTION"
    EDUCATION = "EDUCATION"

# Set metadata after class creation
CellFreeApplicationEnum._metadata = {
    "RECOMBINANT_PROTEIN_PRODUCTION": {'description': 'General production of recombinant proteins in vitro', 'aliases': ['protein production']},
    "MEMBRANE_PROTEIN_EXPRESSION": {'description': 'Expression of membrane proteins, often co-translationally inserted into liposomes, nanodiscs, or detergent micelles', 'aliases': ['membrane protein synthesis']},
    "DIFFICULT_PROTEIN_EXPRESSION": {'description': 'Expression of toxic, unstable, or otherwise difficult-to-express proteins that are problematic in living cells', 'aliases': ['toxic protein expression']},
    "GENETIC_CIRCUIT_PROTOTYPING": {'description': 'Rapid prototyping and characterization of genetic parts and circuits using in vitro transcription-translation (TX-TL)', 'aliases': ['TX-TL prototyping', 'circuit prototyping']},
    "METABOLIC_PATHWAY_PROTOTYPING": {'description': 'Building and testing enzymatic and metabolic pathways in vitro for cell-free biosynthesis', 'aliases': ['cell-free metabolic engineering', 'pathway prototyping']},
    "BIOSENSOR": {'description': 'Cell-free biosensors, including freeze-dried paper-based sensors for detecting nucleic acids, small molecules, or contaminants', 'meaning': 'NCIT:C16350', 'aliases': ['cell-free biosensor', 'Biosensors']},
    "DIAGNOSTICS": {'description': 'Point-of-care and field-deployable diagnostics, often freeze-dried cell-free reactions coupled to toehold switches or CRISPR readouts', 'aliases': ['point-of-care diagnostics']},
    "UNNATURAL_AMINO_ACID_INCORPORATION": {'description': 'Site-specific incorporation of non-canonical/unnatural amino acids via orthogonal translation components', 'aliases': ['ncAA incorporation', 'non-canonical amino acid incorporation']},
    "PROTEIN_LABELING": {'description': 'Incorporation of radioactive, fluorescent, or isotopic labels for detection and structural studies', 'aliases': ['isotopic labeling', 'radiolabeling']},
    "STRUCTURAL_BIOLOGY": {'description': 'Production of selectively or uniformly isotope-labeled proteins for NMR and other structural studies', 'aliases': ['NMR labeling']},
    "HIGH_THROUGHPUT_SCREENING": {'description': 'Parallelized small-volume expression for protein screening, directed evolution, and library characterization', 'meaning': 'NCIT:C18472', 'aliases': ['HTS']},
    "VACCINE_PRODUCTION": {'description': 'On-demand cell-free production of protein subunit and conjugate vaccine antigens', 'meaning': 'OBI:0000719', 'aliases': ['on-demand vaccine production']},
    "ANTIBODY_PRODUCTION": {'description': 'Cell-free synthesis of antibodies and antibody fragments', 'aliases': ['antibody synthesis']},
    "EDUCATION": {'description': 'Use of cell-free kits for teaching and outreach in synthetic biology', 'aliases': ['teaching']},
}

__all__ = [
    "CellFreeExpressionSystemEnum",
    "CellFreeReactionFormatEnum",
    "EnergyRegenerationSubstrateEnum",
    "CellFreeApplicationEnum",
]