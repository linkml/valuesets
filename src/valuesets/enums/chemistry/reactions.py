"""
Chemical Reactions Value Sets

Value sets for chemical reactions, reaction types, mechanisms, and kinetics.


Generated from: chemistry/reactions.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

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

__all__ = [
    "ReactionTypeEnum",
    "ReactionMechanismEnum",
    "CatalystTypeEnum",
    "ReactionConditionEnum",
    "ReactionRateOrderEnum",
    "EnzymeClassEnum",
    "SolventClassEnum",
    "ThermodynamicParameterEnum",
]