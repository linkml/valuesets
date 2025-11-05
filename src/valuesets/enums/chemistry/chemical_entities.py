"""
Chemical Entities Value Sets

Value sets for chemical entities including subatomic particles, chemical elements, bond types, and chemical classifications. Based on the ChemROF ontological framework.


Generated from: chemistry/chemical_entities.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class SubatomicParticleEnum(RichEnum):
    """
    Fundamental and composite subatomic particles
    """
    # Enum members
    ELECTRON = "ELECTRON"
    POSITRON = "POSITRON"
    MUON = "MUON"
    TAU_LEPTON = "TAU_LEPTON"
    ELECTRON_NEUTRINO = "ELECTRON_NEUTRINO"
    MUON_NEUTRINO = "MUON_NEUTRINO"
    TAU_NEUTRINO = "TAU_NEUTRINO"
    UP_QUARK = "UP_QUARK"
    DOWN_QUARK = "DOWN_QUARK"
    CHARM_QUARK = "CHARM_QUARK"
    STRANGE_QUARK = "STRANGE_QUARK"
    TOP_QUARK = "TOP_QUARK"
    BOTTOM_QUARK = "BOTTOM_QUARK"
    PHOTON = "PHOTON"
    W_BOSON = "W_BOSON"
    Z_BOSON = "Z_BOSON"
    GLUON = "GLUON"
    HIGGS_BOSON = "HIGGS_BOSON"
    PROTON = "PROTON"
    NEUTRON = "NEUTRON"
    ALPHA_PARTICLE = "ALPHA_PARTICLE"
    DEUTERON = "DEUTERON"
    TRITON = "TRITON"

# Set metadata after class creation
SubatomicParticleEnum._metadata = {
    "ELECTRON": {'description': 'Elementary particle with -1 charge, spin 1/2', 'meaning': 'CHEBI:10545', 'annotations': {'mass': '0.51099895 MeV/c²', 'charge': '-1', 'spin': '1/2', 'type': 'lepton'}},
    "POSITRON": {'description': 'Antiparticle of electron with +1 charge', 'meaning': 'CHEBI:30225', 'annotations': {'mass': '0.51099895 MeV/c²', 'charge': '+1', 'spin': '1/2', 'type': 'lepton'}},
    "MUON": {'description': 'Heavy lepton with -1 charge', 'meaning': 'CHEBI:36356', 'annotations': {'mass': '105.658 MeV/c²', 'charge': '-1', 'spin': '1/2', 'type': 'lepton'}},
    "TAU_LEPTON": {'description': 'Heaviest lepton with -1 charge', 'meaning': 'CHEBI:36355', 'annotations': {'mass': '1777.05 MeV/c²', 'charge': '-1', 'spin': '1/2', 'type': 'lepton'}},
    "ELECTRON_NEUTRINO": {'description': 'Electron neutrino, nearly massless', 'meaning': 'CHEBI:30223', 'annotations': {'mass': '<2.2 eV/c²', 'charge': '0', 'spin': '1/2', 'type': 'lepton'}},
    "MUON_NEUTRINO": {'description': 'Muon neutrino', 'meaning': 'CHEBI:36353', 'annotations': {'mass': '<0.17 MeV/c²', 'charge': '0', 'spin': '1/2', 'type': 'lepton'}},
    "TAU_NEUTRINO": {'description': 'Tau neutrino', 'meaning': 'CHEBI:36354', 'annotations': {'mass': '<15.5 MeV/c²', 'charge': '0', 'spin': '1/2', 'type': 'lepton'}},
    "UP_QUARK": {'description': 'First generation quark with +2/3 charge', 'meaning': 'CHEBI:36366', 'annotations': {'mass': '2.16 MeV/c²', 'charge': '+2/3', 'spin': '1/2', 'type': 'quark', 'generation': '1'}},
    "DOWN_QUARK": {'description': 'First generation quark with -1/3 charge', 'meaning': 'CHEBI:36367', 'annotations': {'mass': '4.67 MeV/c²', 'charge': '-1/3', 'spin': '1/2', 'type': 'quark', 'generation': '1'}},
    "CHARM_QUARK": {'description': 'Second generation quark with +2/3 charge', 'meaning': 'CHEBI:36369', 'annotations': {'mass': '1.27 GeV/c²', 'charge': '+2/3', 'spin': '1/2', 'type': 'quark', 'generation': '2'}},
    "STRANGE_QUARK": {'description': 'Second generation quark with -1/3 charge', 'meaning': 'CHEBI:36368', 'annotations': {'mass': '93.4 MeV/c²', 'charge': '-1/3', 'spin': '1/2', 'type': 'quark', 'generation': '2'}},
    "TOP_QUARK": {'description': 'Third generation quark with +2/3 charge', 'meaning': 'CHEBI:36371', 'annotations': {'mass': '172.76 GeV/c²', 'charge': '+2/3', 'spin': '1/2', 'type': 'quark', 'generation': '3'}},
    "BOTTOM_QUARK": {'description': 'Third generation quark with -1/3 charge', 'meaning': 'CHEBI:36370', 'annotations': {'mass': '4.18 GeV/c²', 'charge': '-1/3', 'spin': '1/2', 'type': 'quark', 'generation': '3'}},
    "PHOTON": {'description': 'Force carrier for electromagnetic interaction', 'meaning': 'CHEBI:30212', 'annotations': {'mass': '0', 'charge': '0', 'spin': '1', 'type': 'gauge boson'}},
    "W_BOSON": {'description': 'Force carrier for weak interaction', 'meaning': 'CHEBI:36343', 'annotations': {'mass': '80.379 GeV/c²', 'charge': '±1', 'spin': '1', 'type': 'gauge boson'}},
    "Z_BOSON": {'description': 'Force carrier for weak interaction', 'meaning': 'CHEBI:36344', 'annotations': {'mass': '91.1876 GeV/c²', 'charge': '0', 'spin': '1', 'type': 'gauge boson'}},
    "GLUON": {'description': 'Force carrier for strong interaction', 'annotations': {'mass': '0', 'charge': '0', 'spin': '1', 'type': 'gauge boson', 'color_charge': 'yes'}},
    "HIGGS_BOSON": {'description': 'Scalar boson responsible for mass', 'meaning': 'CHEBI:146278', 'annotations': {'mass': '125.25 GeV/c²', 'charge': '0', 'spin': '0', 'type': 'scalar boson'}},
    "PROTON": {'description': 'Positively charged nucleon', 'meaning': 'CHEBI:24636', 'annotations': {'mass': '938.272 MeV/c²', 'charge': '+1', 'spin': '1/2', 'type': 'baryon', 'composition': 'uud'}},
    "NEUTRON": {'description': 'Neutral nucleon', 'meaning': 'CHEBI:30222', 'annotations': {'mass': '939.565 MeV/c²', 'charge': '0', 'spin': '1/2', 'type': 'baryon', 'composition': 'udd'}},
    "ALPHA_PARTICLE": {'description': 'Helium-4 nucleus', 'meaning': 'CHEBI:30216', 'annotations': {'mass': '3727.379 MeV/c²', 'charge': '+2', 'composition': '2 protons, 2 neutrons'}},
    "DEUTERON": {'description': 'Hydrogen-2 nucleus', 'meaning': 'CHEBI:29233', 'annotations': {'mass': '1875.613 MeV/c²', 'charge': '+1', 'composition': '1 proton, 1 neutron'}},
    "TRITON": {'description': 'Hydrogen-3 nucleus', 'meaning': 'CHEBI:29234', 'annotations': {'mass': '2808.921 MeV/c²', 'charge': '+1', 'composition': '1 proton, 2 neutrons'}},
}

class BondTypeEnum(RichEnum):
    """
    Types of chemical bonds
    """
    # Enum members
    SINGLE = "SINGLE"
    DOUBLE = "DOUBLE"
    TRIPLE = "TRIPLE"
    QUADRUPLE = "QUADRUPLE"
    AROMATIC = "AROMATIC"
    IONIC = "IONIC"
    HYDROGEN = "HYDROGEN"
    METALLIC = "METALLIC"
    VAN_DER_WAALS = "VAN_DER_WAALS"
    COORDINATE = "COORDINATE"
    PI = "PI"
    SIGMA = "SIGMA"

# Set metadata after class creation
BondTypeEnum._metadata = {
    "SINGLE": {'description': 'Single covalent bond', 'meaning': 'gc:Single', 'annotations': {'bond_order': '1', 'electrons_shared': '2'}},
    "DOUBLE": {'description': 'Double covalent bond', 'meaning': 'gc:Double', 'annotations': {'bond_order': '2', 'electrons_shared': '4'}},
    "TRIPLE": {'description': 'Triple covalent bond', 'meaning': 'gc:Triple', 'annotations': {'bond_order': '3', 'electrons_shared': '6'}},
    "QUADRUPLE": {'description': 'Quadruple bond (rare, in transition metals)', 'meaning': 'gc:Quadruple', 'annotations': {'bond_order': '4', 'electrons_shared': '8'}},
    "AROMATIC": {'description': 'Aromatic bond', 'meaning': 'gc:AromaticBond', 'annotations': {'bond_order': '1.5', 'delocalized': 'true'}},
    "IONIC": {'description': 'Ionic bond', 'meaning': 'CHEBI:50860', 'annotations': {'type': 'electrostatic'}},
    "HYDROGEN": {'description': 'Hydrogen bond', 'annotations': {'type': 'weak interaction', 'energy': '5-30 kJ/mol'}},
    "METALLIC": {'description': 'Metallic bond', 'annotations': {'type': 'delocalized electrons'}},
    "VAN_DER_WAALS": {'description': 'Van der Waals interaction', 'annotations': {'type': 'weak interaction', 'energy': '0.4-4 kJ/mol'}},
    "COORDINATE": {'description': 'Coordinate/dative covalent bond', 'meaning': 'CHEBI:33240', 'annotations': {'electrons_from': 'one atom'}},
    "PI": {'description': 'Pi bond', 'annotations': {'orbital_overlap': 'side-to-side'}},
    "SIGMA": {'description': 'Sigma bond', 'annotations': {'orbital_overlap': 'head-to-head'}},
}

class PeriodicTableBlockEnum(RichEnum):
    """
    Blocks of the periodic table
    """
    # Enum members
    S_BLOCK = "S_BLOCK"
    P_BLOCK = "P_BLOCK"
    D_BLOCK = "D_BLOCK"
    F_BLOCK = "F_BLOCK"

# Set metadata after class creation
PeriodicTableBlockEnum._metadata = {
    "S_BLOCK": {'description': 's-block elements (groups 1 and 2)', 'meaning': 'CHEBI:33674', 'annotations': {'valence_orbital': 's', 'groups': '1,2'}},
    "P_BLOCK": {'description': 'p-block elements (groups 13-18)', 'meaning': 'CHEBI:33675', 'annotations': {'valence_orbital': 'p', 'groups': '13,14,15,16,17,18'}},
    "D_BLOCK": {'description': 'd-block elements (transition metals)', 'meaning': 'CHEBI:33561', 'annotations': {'valence_orbital': 'd', 'groups': '3-12'}},
    "F_BLOCK": {'description': 'f-block elements (lanthanides and actinides)', 'meaning': 'CHEBI:33562', 'annotations': {'valence_orbital': 'f', 'series': 'lanthanides, actinides'}},
}

class ElementFamilyEnum(RichEnum):
    """
    Chemical element families/groups
    """
    # Enum members
    ALKALI_METALS = "ALKALI_METALS"
    ALKALINE_EARTH_METALS = "ALKALINE_EARTH_METALS"
    TRANSITION_METALS = "TRANSITION_METALS"
    LANTHANIDES = "LANTHANIDES"
    ACTINIDES = "ACTINIDES"
    CHALCOGENS = "CHALCOGENS"
    HALOGENS = "HALOGENS"
    NOBLE_GASES = "NOBLE_GASES"
    METALLOIDS = "METALLOIDS"
    POST_TRANSITION_METALS = "POST_TRANSITION_METALS"
    NONMETALS = "NONMETALS"

# Set metadata after class creation
ElementFamilyEnum._metadata = {
    "ALKALI_METALS": {'description': 'Group 1 elements (except hydrogen)', 'meaning': 'CHEBI:22314', 'annotations': {'group': '1', 'elements': 'Li, Na, K, Rb, Cs, Fr'}},
    "ALKALINE_EARTH_METALS": {'description': 'Group 2 elements', 'meaning': 'CHEBI:22315', 'annotations': {'group': '2', 'elements': 'Be, Mg, Ca, Sr, Ba, Ra'}},
    "TRANSITION_METALS": {'description': 'd-block elements', 'meaning': 'CHEBI:27081', 'annotations': {'groups': '3-12'}},
    "LANTHANIDES": {'description': 'Lanthanide series', 'meaning': 'CHEBI:33768', 'annotations': {'atomic_numbers': '57-71'}},
    "ACTINIDES": {'description': 'Actinide series', 'meaning': 'CHEBI:33769', 'annotations': {'atomic_numbers': '89-103'}},
    "CHALCOGENS": {'description': 'Group 16 elements', 'meaning': 'CHEBI:33303', 'annotations': {'group': '16', 'elements': 'O, S, Se, Te, Po'}},
    "HALOGENS": {'description': 'Group 17 elements', 'meaning': 'CHEBI:47902', 'annotations': {'group': '17', 'elements': 'F, Cl, Br, I, At'}},
    "NOBLE_GASES": {'description': 'Group 18 elements', 'meaning': 'CHEBI:33310', 'annotations': {'group': '18', 'elements': 'He, Ne, Ar, Kr, Xe, Rn'}},
    "METALLOIDS": {'description': 'Elements with intermediate properties', 'meaning': 'CHEBI:33559', 'annotations': {'elements': 'B, Si, Ge, As, Sb, Te, Po'}},
    "POST_TRANSITION_METALS": {'description': 'Metals after the transition series', 'annotations': {'elements': 'Al, Ga, In, Tl, Sn, Pb, Bi'}},
    "NONMETALS": {'description': 'Non-metallic elements', 'meaning': 'CHEBI:25585', 'annotations': {'elements': 'H, C, N, O, F, P, S, Cl, Se, Br, I'}},
}

class ElementMetallicClassificationEnum(RichEnum):
    """
    Metallic character classification
    """
    # Enum members
    METALLIC = "METALLIC"
    NON_METALLIC = "NON_METALLIC"
    SEMI_METALLIC = "SEMI_METALLIC"

# Set metadata after class creation
ElementMetallicClassificationEnum._metadata = {
    "METALLIC": {'description': 'Metallic elements', 'meaning': 'damlpt:Metallic', 'annotations': {'properties': 'conductive, malleable, ductile'}},
    "NON_METALLIC": {'description': 'Non-metallic elements', 'meaning': 'damlpt:Non-Metallic', 'annotations': {'properties': 'poor conductors, brittle'}},
    "SEMI_METALLIC": {'description': 'Semi-metallic/metalloid elements', 'meaning': 'damlpt:Semi-Metallic', 'annotations': {'properties': 'intermediate properties'}},
}

class HardOrSoftEnum(RichEnum):
    """
    HSAB (Hard Soft Acid Base) classification
    """
    # Enum members
    HARD = "HARD"
    SOFT = "SOFT"
    BORDERLINE = "BORDERLINE"

# Set metadata after class creation
HardOrSoftEnum._metadata = {
    "HARD": {'description': 'Hard acids/bases (small, high charge density)', 'annotations': {'examples': 'H+, Li+, Mg2+, Al3+, F-, OH-', 'polarizability': 'low'}},
    "SOFT": {'description': 'Soft acids/bases (large, low charge density)', 'annotations': {'examples': 'Cu+, Ag+, Au+, I-, S2-', 'polarizability': 'high'}},
    "BORDERLINE": {'description': 'Borderline acids/bases', 'annotations': {'examples': 'Fe2+, Co2+, Ni2+, Cu2+, Zn2+', 'polarizability': 'intermediate'}},
}

class BronstedAcidBaseRoleEnum(RichEnum):
    """
    Brønsted-Lowry acid-base roles
    """
    # Enum members
    ACID = "ACID"
    BASE = "BASE"
    AMPHOTERIC = "AMPHOTERIC"

# Set metadata after class creation
BronstedAcidBaseRoleEnum._metadata = {
    "ACID": {'description': 'Proton donor', 'meaning': 'CHEBI:39141', 'annotations': {'definition': 'species that donates H+'}},
    "BASE": {'description': 'Proton acceptor', 'meaning': 'CHEBI:39142', 'annotations': {'definition': 'species that accepts H+'}},
    "AMPHOTERIC": {'description': 'Can act as both acid and base', 'annotations': {'definition': 'species that can donate or accept H+', 'examples': 'H2O, HSO4-, H2PO4-'}},
}

class LewisAcidBaseRoleEnum(RichEnum):
    """
    Lewis acid-base roles
    """
    # Enum members
    LEWIS_ACID = "LEWIS_ACID"
    LEWIS_BASE = "LEWIS_BASE"

# Set metadata after class creation
LewisAcidBaseRoleEnum._metadata = {
    "LEWIS_ACID": {'description': 'Electron pair acceptor', 'annotations': {'definition': 'species that accepts electron pair', 'examples': 'BF3, AlCl3, H+'}},
    "LEWIS_BASE": {'description': 'Electron pair donor', 'annotations': {'definition': 'species that donates electron pair', 'examples': 'NH3, OH-, H2O'}},
}

class OxidationStateEnum(RichEnum):
    """
    Common oxidation states
    """
    # Enum members
    MINUS_4 = "MINUS_4"
    MINUS_3 = "MINUS_3"
    MINUS_2 = "MINUS_2"
    MINUS_1 = "MINUS_1"
    ZERO = "ZERO"
    PLUS_1 = "PLUS_1"
    PLUS_2 = "PLUS_2"
    PLUS_3 = "PLUS_3"
    PLUS_4 = "PLUS_4"
    PLUS_5 = "PLUS_5"
    PLUS_6 = "PLUS_6"
    PLUS_7 = "PLUS_7"
    PLUS_8 = "PLUS_8"

# Set metadata after class creation
OxidationStateEnum._metadata = {
    "MINUS_4": {'description': 'Oxidation state -4', 'annotations': {'value': '-4', 'example': 'C in CH4'}},
    "MINUS_3": {'description': 'Oxidation state -3', 'annotations': {'value': '-3', 'example': 'N in NH3'}},
    "MINUS_2": {'description': 'Oxidation state -2', 'annotations': {'value': '-2', 'example': 'O in H2O'}},
    "MINUS_1": {'description': 'Oxidation state -1', 'annotations': {'value': '-1', 'example': 'Cl in NaCl'}},
    "ZERO": {'description': 'Oxidation state 0', 'annotations': {'value': '0', 'example': 'elemental forms'}},
    "PLUS_1": {'description': 'Oxidation state +1', 'annotations': {'value': '+1', 'example': 'Na in NaCl'}},
    "PLUS_2": {'description': 'Oxidation state +2', 'annotations': {'value': '+2', 'example': 'Ca in CaCl2'}},
    "PLUS_3": {'description': 'Oxidation state +3', 'annotations': {'value': '+3', 'example': 'Al in Al2O3'}},
    "PLUS_4": {'description': 'Oxidation state +4', 'annotations': {'value': '+4', 'example': 'C in CO2'}},
    "PLUS_5": {'description': 'Oxidation state +5', 'annotations': {'value': '+5', 'example': 'P in PO4³⁻'}},
    "PLUS_6": {'description': 'Oxidation state +6', 'annotations': {'value': '+6', 'example': 'S in SO4²⁻'}},
    "PLUS_7": {'description': 'Oxidation state +7', 'annotations': {'value': '+7', 'example': 'Mn in MnO4⁻'}},
    "PLUS_8": {'description': 'Oxidation state +8', 'annotations': {'value': '+8', 'example': 'Os in OsO4'}},
}

class ChiralityEnum(RichEnum):
    """
    Chirality/stereochemistry descriptors
    """
    # Enum members
    R = "R"
    S = "S"
    D = "D"
    L = "L"
    RACEMIC = "RACEMIC"
    MESO = "MESO"
    E = "E"
    Z = "Z"

# Set metadata after class creation
ChiralityEnum._metadata = {
    "R": {'description': 'Rectus (right) configuration', 'annotations': {'cahn_ingold_prelog': 'true'}},
    "S": {'description': 'Sinister (left) configuration', 'annotations': {'cahn_ingold_prelog': 'true'}},
    "D": {'description': 'Dextrorotatory', 'annotations': {'fischer_projection': 'true', 'optical_rotation': 'positive'}},
    "L": {'description': 'Levorotatory', 'annotations': {'fischer_projection': 'true', 'optical_rotation': 'negative'}},
    "RACEMIC": {'description': 'Racemic mixture (50:50 of enantiomers)', 'annotations': {'optical_rotation': 'zero'}},
    "MESO": {'description': 'Meso compound (achiral despite stereocenters)', 'annotations': {'internal_symmetry': 'true'}},
    "E": {'description': 'Entgegen (opposite) configuration', 'annotations': {'geometric_isomer': 'true'}},
    "Z": {'description': 'Zusammen (together) configuration', 'annotations': {'geometric_isomer': 'true'}},
}

class NanostructureMorphologyEnum(RichEnum):
    """
    Types of nanostructure morphologies
    """
    # Enum members
    NANOTUBE = "NANOTUBE"
    NANOPARTICLE = "NANOPARTICLE"
    NANOROD = "NANOROD"
    QUANTUM_DOT = "QUANTUM_DOT"
    NANOWIRE = "NANOWIRE"
    NANOSHEET = "NANOSHEET"
    NANOFIBER = "NANOFIBER"

# Set metadata after class creation
NanostructureMorphologyEnum._metadata = {
    "NANOTUBE": {'description': 'Cylindrical nanostructure', 'meaning': 'CHEBI:50796', 'annotations': {'dimensions': '1D', 'examples': 'carbon nanotubes'}},
    "NANOPARTICLE": {'description': 'Particle with nanoscale dimensions', 'meaning': 'CHEBI:50803', 'annotations': {'dimensions': '0D', 'size_range': '1-100 nm'}},
    "NANOROD": {'description': 'Rod-shaped nanostructure', 'meaning': 'CHEBI:50805', 'annotations': {'dimensions': '1D', 'aspect_ratio': '3-20'}},
    "QUANTUM_DOT": {'description': 'Semiconductor nanocrystal', 'meaning': 'CHEBI:50853', 'annotations': {'dimensions': '0D', 'property': 'quantum confinement'}},
    "NANOWIRE": {'description': 'Wire with nanoscale diameter', 'annotations': {'dimensions': '1D', 'diameter': '<100 nm'}},
    "NANOSHEET": {'description': 'Two-dimensional nanostructure', 'annotations': {'dimensions': '2D', 'thickness': '<100 nm'}},
    "NANOFIBER": {'description': 'Fiber with nanoscale diameter', 'annotations': {'dimensions': '1D', 'diameter': '<1000 nm'}},
}

__all__ = [
    "SubatomicParticleEnum",
    "BondTypeEnum",
    "PeriodicTableBlockEnum",
    "ElementFamilyEnum",
    "ElementMetallicClassificationEnum",
    "HardOrSoftEnum",
    "BronstedAcidBaseRoleEnum",
    "LewisAcidBaseRoleEnum",
    "OxidationStateEnum",
    "ChiralityEnum",
    "NanostructureMorphologyEnum",
]