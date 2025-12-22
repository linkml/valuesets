"""
Structural Biology Value Sets

Value sets for structural biology techniques, including cryo-EM, X-ray crystallography, SAXS/SANS, mass spectrometry, and related sample preparation and data processing methods.


Generated from: bio/structural_biology.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class SampleType(RichEnum):
    """
    Types of biological samples used in structural biology
    """
    # Enum members
    PROTEIN = "PROTEIN"
    NUCLEIC_ACID = "NUCLEIC_ACID"
    PROTEIN_COMPLEX = "PROTEIN_COMPLEX"
    MEMBRANE_PROTEIN = "MEMBRANE_PROTEIN"
    VIRUS = "VIRUS"
    ORGANELLE = "ORGANELLE"
    CELL = "CELL"
    TISSUE = "TISSUE"

# Set metadata after class creation
SampleType._metadata = {
    "PROTEIN": {'description': 'Purified protein sample', 'meaning': 'NCIT:C17021'},
    "NUCLEIC_ACID": {'description': 'Nucleic acid sample (DNA or RNA)', 'meaning': 'NCIT:C706'},
    "PROTEIN_COMPLEX": {'description': 'Protein-protein or protein-nucleic acid complex', 'meaning': 'GO:0032991'},
    "MEMBRANE_PROTEIN": {'description': 'Membrane-associated protein sample', 'meaning': 'NCIT:C16837'},
    "VIRUS": {'description': 'Viral particle or capsid', 'meaning': 'NCIT:C14283'},
    "ORGANELLE": {'description': 'Cellular organelle (mitochondria, chloroplast, etc.)', 'meaning': 'GO:0043226'},
    "CELL": {'description': 'Whole cell sample', 'meaning': 'NCIT:C12508'},
    "TISSUE": {'description': 'Tissue sample', 'meaning': 'NCIT:C12801'},
}

class StructuralBiologyTechnique(RichEnum):
    """
    Structural biology experimental techniques
    """
    # Enum members
    CRYO_EM = "CRYO_EM"
    CRYO_ET = "CRYO_ET"
    X_RAY_CRYSTALLOGRAPHY = "X_RAY_CRYSTALLOGRAPHY"
    NEUTRON_CRYSTALLOGRAPHY = "NEUTRON_CRYSTALLOGRAPHY"
    SAXS = "SAXS"
    SANS = "SANS"
    WAXS = "WAXS"
    NMR = "NMR"
    MASS_SPECTROMETRY = "MASS_SPECTROMETRY"
    NEGATIVE_STAIN_EM = "NEGATIVE_STAIN_EM"

# Set metadata after class creation
StructuralBiologyTechnique._metadata = {
    "CRYO_EM": {'description': 'Cryo-electron microscopy', 'meaning': 'CHMO:0002413', 'annotations': {'resolution_range': '2-30 Å typical', 'aliases': 'cryoEM, electron cryo-microscopy'}},
    "CRYO_ET": {'description': 'Cryo-electron tomography', 'meaning': 'MI:2338', 'annotations': {'resolution_range': '20-100 Å typical', 'aliases': 'cryoET, electron cryo-tomography'}},
    "X_RAY_CRYSTALLOGRAPHY": {'description': 'X-ray crystallography', 'meaning': 'CHMO:0000159', 'annotations': {'resolution_range': '1-4 Å typical', 'aliases': 'XRC, macromolecular crystallography'}},
    "NEUTRON_CRYSTALLOGRAPHY": {'description': 'Neutron crystallography', 'meaning': 'CHMO:0000698', 'annotations': {'advantages': 'hydrogen positions, deuteration studies'}},
    "SAXS": {'description': 'Small-angle X-ray scattering', 'meaning': 'CHMO:0000204', 'annotations': {'information': 'low-resolution structure, conformational changes'}},
    "SANS": {'description': 'Small-angle neutron scattering', 'meaning': 'CHMO:0000184', 'annotations': {'advantages': 'contrast variation with deuteration'}},
    "WAXS": {'description': 'Wide-angle X-ray scattering', 'meaning': 'CHMO:0000207'},
    "NMR": {'description': 'Nuclear magnetic resonance spectroscopy', 'meaning': 'CHMO:0000591', 'annotations': {'information': 'solution structure, dynamics'}},
    "MASS_SPECTROMETRY": {'description': 'Mass spectrometry', 'meaning': 'CHMO:0000470', 'annotations': {'applications': 'native MS, crosslinking, HDX'}},
    "NEGATIVE_STAIN_EM": {'description': 'Negative stain electron microscopy', 'meaning': 'FBbi:00000399', 'annotations': {'resolution_range': '15-30 Å typical'}},
}

class CryoEMPreparationType(RichEnum):
    """
    Types of cryo-EM sample preparation
    """
    # Enum members
    VITREOUS_ICE = "VITREOUS_ICE"
    CRYO_SECTIONING = "CRYO_SECTIONING"
    FREEZE_SUBSTITUTION = "FREEZE_SUBSTITUTION"
    HIGH_PRESSURE_FREEZING = "HIGH_PRESSURE_FREEZING"

# Set metadata after class creation
CryoEMPreparationType._metadata = {
    "VITREOUS_ICE": {'description': 'Sample embedded in vitreous ice'},
    "CRYO_SECTIONING": {'description': 'Cryo-sectioned sample'},
    "FREEZE_SUBSTITUTION": {'description': 'Freeze-substituted sample'},
    "HIGH_PRESSURE_FREEZING": {'description': 'High-pressure frozen sample'},
}

class CryoEMGridType(RichEnum):
    """
    Types of electron microscopy grids
    """
    # Enum members
    C_FLAT = "C_FLAT"
    QUANTIFOIL = "QUANTIFOIL"
    LACEY_CARBON = "LACEY_CARBON"
    ULTRATHIN_CARBON = "ULTRATHIN_CARBON"
    GOLD_GRID = "GOLD_GRID"
    GRAPHENE_OXIDE = "GRAPHENE_OXIDE"

# Set metadata after class creation
CryoEMGridType._metadata = {
    "C_FLAT": {'description': 'C-flat holey carbon grid', 'annotations': {'hole_sizes': '1.2/1.3, 2/1, 2/2 μm common', 'manufacturer': 'Protochips'}},
    "QUANTIFOIL": {'description': 'Quantifoil holey carbon grid', 'annotations': {'hole_sizes': '1.2/1.3, 2/1, 2/2 μm common', 'manufacturer': 'Quantifoil'}},
    "LACEY_CARBON": {'description': 'Lacey carbon support film', 'annotations': {'structure': 'irregular holes, thin carbon film'}},
    "ULTRATHIN_CARBON": {'description': 'Ultrathin carbon film on holey support', 'annotations': {'thickness': '3-5 nm typical'}},
    "GOLD_GRID": {'description': 'Pure gold grid', 'annotations': {'advantages': 'inert, high-resolution imaging'}},
    "GRAPHENE_OXIDE": {'description': 'Graphene oxide support', 'annotations': {'advantages': 'atomically thin, good contrast'}},
}

class VitrificationMethod(RichEnum):
    """
    Methods for sample vitrification
    """
    # Enum members
    PLUNGE_FREEZING = "PLUNGE_FREEZING"
    HIGH_PRESSURE_FREEZING = "HIGH_PRESSURE_FREEZING"
    SLAM_FREEZING = "SLAM_FREEZING"
    SPRAY_FREEZING = "SPRAY_FREEZING"

# Set metadata after class creation
VitrificationMethod._metadata = {
    "PLUNGE_FREEZING": {'description': 'Plunge freezing in liquid ethane', 'annotations': {'temperature': '-180°C ethane', 'equipment': 'Vitrobot, Leica GP'}},
    "HIGH_PRESSURE_FREEZING": {'description': 'High pressure freezing', 'annotations': {'pressure': '2100 bar typical', 'advantages': 'thick samples, no ice crystals'}},
    "SLAM_FREEZING": {'description': 'Slam freezing against metal block', 'annotations': {'cooling_rate': '10,000 K/s'}},
    "SPRAY_FREEZING": {'description': 'Spray freezing into liquid nitrogen', 'annotations': {'applications': 'large samples, tissues'}},
}

class CrystallizationMethod(RichEnum):
    """
    Methods for protein crystallization
    """
    # Enum members
    VAPOR_DIFFUSION_HANGING = "VAPOR_DIFFUSION_HANGING"
    VAPOR_DIFFUSION_SITTING = "VAPOR_DIFFUSION_SITTING"
    MICROBATCH = "MICROBATCH"
    DIALYSIS = "DIALYSIS"
    FREE_INTERFACE_DIFFUSION = "FREE_INTERFACE_DIFFUSION"
    LCP = "LCP"

# Set metadata after class creation
CrystallizationMethod._metadata = {
    "VAPOR_DIFFUSION_HANGING": {'description': 'Vapor diffusion hanging drop method', 'annotations': {'volume': '2-10 μL drops typical', 'advantages': 'visual monitoring, easy optimization'}},
    "VAPOR_DIFFUSION_SITTING": {'description': 'Vapor diffusion sitting drop method', 'annotations': {'advantages': 'automated setup, stable drops'}},
    "MICROBATCH": {'description': 'Microbatch under oil method', 'annotations': {'oil_type': 'paraffin, silicone oil', 'advantages': 'prevents evaporation'}},
    "DIALYSIS": {'description': 'Dialysis crystallization', 'annotations': {'applications': 'large volume samples, gentle conditions'}},
    "FREE_INTERFACE_DIFFUSION": {'description': 'Free interface diffusion', 'annotations': {'setup': 'capillary tubes, gel interface'}},
    "LCP": {'description': 'Lipidic cubic phase crystallization', 'annotations': {'applications': 'membrane proteins', 'lipid': 'monoolein most common'}},
}

class XRaySource(RichEnum):
    """
    Types of X-ray sources
    """
    # Enum members
    SYNCHROTRON = "SYNCHROTRON"
    ROTATING_ANODE = "ROTATING_ANODE"
    MICROFOCUS = "MICROFOCUS"
    METAL_JET = "METAL_JET"

# Set metadata after class creation
XRaySource._metadata = {
    "SYNCHROTRON": {'description': 'Synchrotron radiation source', 'meaning': 'CHMO:0001810', 'annotations': {'advantages': 'high intensity, tunable wavelength', 'brightness': '10^15-10^18 photons/s/mm²/mrad²'}},
    "ROTATING_ANODE": {'description': 'Rotating anode generator', 'annotations': {'power': '3-18 kW typical', 'target': 'copper, molybdenum common'}},
    "MICROFOCUS": {'description': 'Microfocus sealed tube', 'annotations': {'spot_size': '10-50 μm', 'applications': 'small crystals, in-house screening'}},
    "METAL_JET": {'description': 'Liquid metal jet source', 'annotations': {'advantages': 'higher power density, longer lifetime', 'metals': 'gallium, indium'}},
}

class Detector(RichEnum):
    """
    Types of detectors for structural biology
    """
    # Enum members
    DIRECT_ELECTRON = "DIRECT_ELECTRON"
    CCD = "CCD"
    CMOS = "CMOS"
    HYBRID_PIXEL = "HYBRID_PIXEL"
    PHOTOSTIMULABLE_PHOSPHOR = "PHOTOSTIMULABLE_PHOSPHOR"

# Set metadata after class creation
Detector._metadata = {
    "DIRECT_ELECTRON": {'description': 'Direct electron detector (DED)', 'annotations': {'examples': 'K2, K3, Falcon, DE-series', 'advantages': 'high DQE, fast readout'}},
    "CCD": {'description': 'Charge-coupled device camera', 'meaning': 'CHMO:0002245', 'annotations': {'applications': 'legacy EM, some crystallography'}},
    "CMOS": {'description': 'Complementary metal-oxide semiconductor detector', 'annotations': {'advantages': 'fast readout, low noise'}},
    "HYBRID_PIXEL": {'description': 'Hybrid pixel detector', 'annotations': {'examples': 'Pilatus, Eiger', 'advantages': 'photon counting, zero noise'}},
    "PHOTOSTIMULABLE_PHOSPHOR": {'description': 'Photostimulable phosphor (image plate)', 'annotations': {'applications': 'legacy crystallography'}},
}

class WorkflowType(RichEnum):
    """
    Types of computational processing workflows
    """
    # Enum members
    MOTION_CORRECTION = "MOTION_CORRECTION"
    CTF_ESTIMATION = "CTF_ESTIMATION"
    PARTICLE_PICKING = "PARTICLE_PICKING"
    CLASSIFICATION_2D = "CLASSIFICATION_2D"
    CLASSIFICATION_3D = "CLASSIFICATION_3D"
    REFINEMENT_3D = "REFINEMENT_3D"
    MODEL_BUILDING = "MODEL_BUILDING"
    MODEL_REFINEMENT = "MODEL_REFINEMENT"
    PHASING = "PHASING"
    DATA_INTEGRATION = "DATA_INTEGRATION"
    DATA_SCALING = "DATA_SCALING"
    SAXS_ANALYSIS = "SAXS_ANALYSIS"

# Set metadata after class creation
WorkflowType._metadata = {
    "MOTION_CORRECTION": {'description': 'Motion correction for cryo-EM movies', 'annotations': {'software': 'MotionCorr, Unblur, RELION'}},
    "CTF_ESTIMATION": {'description': 'Contrast transfer function estimation', 'annotations': {'software': 'CTFFIND, Gctf, RELION'}},
    "PARTICLE_PICKING": {'description': 'Particle picking from micrographs', 'annotations': {'methods': 'template matching, deep learning', 'software': 'RELION, cryoSPARC, Topaz'}},
    "CLASSIFICATION_2D": {'description': '2D classification of particles', 'annotations': {'purpose': 'sorting, cleaning particle dataset'}},
    "CLASSIFICATION_3D": {'description': '3D classification of particles', 'annotations': {'purpose': 'conformational sorting, resolution improvement'}},
    "REFINEMENT_3D": {'description': '3D refinement of particle orientations', 'annotations': {'algorithms': 'expectation maximization, gradient descent'}},
    "MODEL_BUILDING": {'description': 'Atomic model building into density', 'annotations': {'software': 'Coot, ChimeraX, Isolde'}},
    "MODEL_REFINEMENT": {'description': 'Atomic model refinement', 'annotations': {'software': 'PHENIX, REFMAC, Buster'}},
    "PHASING": {'description': 'Phase determination for crystallography', 'annotations': {'methods': 'SAD, MAD, MR, MIR'}},
    "DATA_INTEGRATION": {'description': 'Integration of diffraction data', 'annotations': {'software': 'XDS, DIALS, HKL'}},
    "DATA_SCALING": {'description': 'Scaling and merging of diffraction data', 'annotations': {'software': 'SCALA, AIMLESS, XSCALE'}},
    "SAXS_ANALYSIS": {'description': 'SAXS data analysis and modeling', 'annotations': {'software': 'PRIMUS, CRYSOL, FoXS'}},
}

class FileFormat(RichEnum):
    """
    File formats used in structural biology
    """
    # Enum members
    MRC = "MRC"
    TIFF = "TIFF"
    HDF5 = "HDF5"
    STAR = "STAR"
    PDB = "PDB"
    MMCIF = "MMCIF"
    MTZ = "MTZ"
    CBF = "CBF"
    DM3 = "DM3"
    SER = "SER"

# Set metadata after class creation
FileFormat._metadata = {
    "MRC": {'description': 'MRC format for EM density maps', 'annotations': {'extension': '.mrc, .map', 'applications': 'EM volumes, tomograms'}},
    "TIFF": {'description': 'Tagged Image File Format', 'meaning': 'EDAM:format_3591', 'annotations': {'extension': '.tif, .tiff', 'applications': 'micrographs, general imaging'}},
    "HDF5": {'description': 'Hierarchical Data Format 5', 'meaning': 'EDAM:format_3590', 'annotations': {'extension': '.h5, .hdf5', 'applications': 'large datasets, metadata storage'}},
    "STAR": {'description': 'Self-defining Text Archival and Retrieval format', 'annotations': {'extension': '.star', 'applications': 'RELION metadata, particle parameters'}},
    "PDB": {'description': 'Protein Data Bank coordinate format', 'meaning': 'EDAM:format_1476', 'annotations': {'extension': '.pdb', 'applications': 'atomic coordinates, legacy format'}},
    "MMCIF": {'description': 'Macromolecular Crystallographic Information File', 'meaning': 'EDAM:format_1477', 'annotations': {'extension': '.cif', 'applications': 'atomic coordinates, modern PDB format'}},
    "MTZ": {'description': 'MTZ reflection data format', 'annotations': {'extension': '.mtz', 'applications': 'crystallographic reflections, phases'}},
    "CBF": {'description': 'Crystallographic Binary Format', 'annotations': {'extension': '.cbf', 'applications': 'detector images, diffraction data'}},
    "DM3": {'description': 'Digital Micrograph format', 'annotations': {'extension': '.dm3, .dm4', 'applications': 'FEI/Thermo Fisher EM data'}},
    "SER": {'description': 'FEI series format', 'annotations': {'extension': '.ser', 'applications': 'FEI movie stacks'}},
}

class DataType(RichEnum):
    """
    Types of structural biology data
    """
    # Enum members
    MICROGRAPH = "MICROGRAPH"
    MOVIE = "MOVIE"
    DIFFRACTION = "DIFFRACTION"
    SCATTERING = "SCATTERING"
    PARTICLES = "PARTICLES"
    VOLUME = "VOLUME"
    TOMOGRAM = "TOMOGRAM"
    MODEL = "MODEL"
    METADATA = "METADATA"

# Set metadata after class creation
DataType._metadata = {
    "MICROGRAPH": {'description': 'Electron micrograph image', 'annotations': {'typical_size': '4k x 4k pixels'}},
    "MOVIE": {'description': 'Movie stack of frames', 'annotations': {'applications': 'motion correction, dose fractionation'}},
    "DIFFRACTION": {'description': 'X-ray diffraction pattern', 'annotations': {'information': 'structure factors, crystal lattice'}},
    "SCATTERING": {'description': 'Small-angle scattering data', 'annotations': {'information': 'I(q) vs scattering vector'}},
    "PARTICLES": {'description': 'Particle stack for single particle analysis', 'annotations': {'format': 'boxed particles, aligned'}},
    "VOLUME": {'description': '3D electron density volume', 'annotations': {'applications': 'cryo-EM maps, crystallographic maps'}},
    "TOMOGRAM": {'description': '3D tomographic reconstruction', 'annotations': {'resolution': '5-50 Å typical'}},
    "MODEL": {'description': 'Atomic coordinate model', 'annotations': {'formats': 'PDB, mmCIF'}},
    "METADATA": {'description': 'Associated metadata file', 'annotations': {'formats': 'STAR, XML, JSON'}},
}

class ProcessingStatus(RichEnum):
    """
    Status of data processing workflows
    """
    # Enum members
    RAW = "RAW"
    PREPROCESSING = "PREPROCESSING"
    PROCESSING = "PROCESSING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    QUEUED = "QUEUED"
    PAUSED = "PAUSED"
    CANCELLED = "CANCELLED"

# Set metadata after class creation
ProcessingStatus._metadata = {
    "RAW": {'description': 'Raw unprocessed data'},
    "PREPROCESSING": {'description': 'Initial preprocessing in progress'},
    "PROCESSING": {'description': 'Main processing workflow running'},
    "COMPLETED": {'description': 'Processing completed successfully'},
    "FAILED": {'description': 'Processing failed with errors'},
    "QUEUED": {'description': 'Queued for processing'},
    "PAUSED": {'description': 'Processing paused by user'},
    "CANCELLED": {'description': 'Processing cancelled by user'},
}

class CoordinationGeometry(RichEnum):
    """
    Coordination geometry of metal centers in protein structures
    """
    # Enum members
    LINEAR = "LINEAR"
    TRIGONAL_PLANAR = "TRIGONAL_PLANAR"
    TRIGONAL_PYRAMIDAL = "TRIGONAL_PYRAMIDAL"
    T_SHAPED = "T_SHAPED"
    TETRAHEDRAL = "TETRAHEDRAL"
    SQUARE_PLANAR = "SQUARE_PLANAR"
    TRIGONAL_BIPYRAMIDAL = "TRIGONAL_BIPYRAMIDAL"
    SQUARE_PYRAMIDAL = "SQUARE_PYRAMIDAL"
    PENTAGONAL_PLANAR = "PENTAGONAL_PLANAR"
    OCTAHEDRAL = "OCTAHEDRAL"
    TRIGONAL_PRISMATIC = "TRIGONAL_PRISMATIC"
    PENTAGONAL_BIPYRAMIDAL = "PENTAGONAL_BIPYRAMIDAL"
    HEXAGONAL_BIPYRAMIDAL = "HEXAGONAL_BIPYRAMIDAL"
    SQUARE_ANTIPRISMATIC = "SQUARE_ANTIPRISMATIC"
    DODECAHEDRAL = "DODECAHEDRAL"
    CUBIC = "CUBIC"
    BENT = "BENT"
    SEE_SAW = "SEE_SAW"

# Set metadata after class creation
CoordinationGeometry._metadata = {
    "LINEAR": {'description': 'Linear coordination geometry (2 ligands at 180°)', 'annotations': {'coordination_number': '2'}},
    "TRIGONAL_PLANAR": {'description': 'Trigonal planar coordination geometry (3 ligands, 120° angles)', 'annotations': {'coordination_number': '3'}},
    "TRIGONAL_PYRAMIDAL": {'description': 'Trigonal pyramidal coordination geometry', 'annotations': {'coordination_number': '3'}},
    "T_SHAPED": {'description': 'T-shaped coordination geometry', 'annotations': {'coordination_number': '3'}},
    "TETRAHEDRAL": {'description': 'Tetrahedral coordination geometry (4 ligands, 109.5° angles)', 'meaning': 'NCIT:C103215', 'annotations': {'coordination_number': '4'}},
    "SQUARE_PLANAR": {'description': 'Square planar coordination geometry (4 ligands in plane)', 'meaning': 'NCIT:C103211', 'annotations': {'coordination_number': '4'}},
    "TRIGONAL_BIPYRAMIDAL": {'description': 'Trigonal bipyramidal coordination geometry (5 ligands)', 'annotations': {'coordination_number': '5'}},
    "SQUARE_PYRAMIDAL": {'description': 'Square pyramidal coordination geometry (5 ligands)', 'annotations': {'coordination_number': '5'}},
    "PENTAGONAL_PLANAR": {'description': 'Pentagonal planar coordination geometry (5 ligands in plane)', 'annotations': {'coordination_number': '5'}},
    "OCTAHEDRAL": {'description': 'Octahedral coordination geometry (6 ligands)', 'meaning': 'NCIT:C103216', 'annotations': {'coordination_number': '6'}},
    "TRIGONAL_PRISMATIC": {'description': 'Trigonal prismatic coordination geometry (6 ligands)', 'annotations': {'coordination_number': '6'}},
    "PENTAGONAL_BIPYRAMIDAL": {'description': 'Pentagonal bipyramidal coordination geometry (7 ligands)', 'annotations': {'coordination_number': '7'}},
    "HEXAGONAL_BIPYRAMIDAL": {'description': 'Hexagonal bipyramidal coordination geometry (8 ligands)', 'annotations': {'coordination_number': '8'}},
    "SQUARE_ANTIPRISMATIC": {'description': 'Square antiprismatic coordination geometry (8 ligands)', 'annotations': {'coordination_number': '8'}},
    "DODECAHEDRAL": {'description': 'Dodecahedral coordination geometry (8 ligands)', 'annotations': {'coordination_number': '8'}},
    "CUBIC": {'description': 'Cubic coordination geometry (8 ligands)', 'annotations': {'coordination_number': '8'}},
    "BENT": {'description': 'Bent or angular coordination geometry', 'annotations': {'coordination_number': '2'}},
    "SEE_SAW": {'description': 'See-saw coordination geometry (4 ligands)', 'annotations': {'coordination_number': '4'}},
}

class MetalLigandType(RichEnum):
    """
    Types of metal-containing chemical components
    """
    # Enum members
    METAL_CATION = "METAL_CATION"
    METAL_CONTAINING_LIGAND = "METAL_CONTAINING_LIGAND"

# Set metadata after class creation
MetalLigandType._metadata = {
    "METAL_CATION": {'description': 'Metal cation (e.g., Ca2+, Mg2+, Zn2+, Fe3+)', 'annotations': {'examples': 'Ca2+, Mg2+, Zn2+, Fe2+, Fe3+, Cu2+, Mn2+'}},
    "METAL_CONTAINING_LIGAND": {'description': 'Metal-containing ligand or cofactor', 'annotations': {'examples': 'heme, chlorophyll, cobalamin, Fe-S cluster'}},
}

class ProteinModificationType(RichEnum):
    """
    Types of protein modifications
    """
    # Enum members
    METAL_COORDINATION = "METAL_COORDINATION"
    PHOSPHORYLATION = "PHOSPHORYLATION"
    GLYCOSYLATION = "GLYCOSYLATION"
    ACETYLATION = "ACETYLATION"
    METHYLATION = "METHYLATION"
    UBIQUITINATION = "UBIQUITINATION"
    SUMOYLATION = "SUMOYLATION"
    HYDROXYLATION = "HYDROXYLATION"
    LIPIDATION = "LIPIDATION"
    PROTEOLYTIC_CLEAVAGE = "PROTEOLYTIC_CLEAVAGE"
    CROSSLINKING = "CROSSLINKING"

# Set metadata after class creation
ProteinModificationType._metadata = {
    "METAL_COORDINATION": {'description': 'Metal coordination modification', 'meaning': 'MOD:00739', 'annotations': {'examples': 'zinc finger, iron-sulfur cluster binding'}},
    "PHOSPHORYLATION": {'description': 'Phosphorylation modification', 'meaning': 'MOD:00696'},
    "GLYCOSYLATION": {'description': 'Glycosylation modification', 'meaning': 'MOD:00725'},
    "ACETYLATION": {'description': 'Acetylation modification', 'meaning': 'MOD:00394'},
    "METHYLATION": {'description': 'Methylation modification', 'meaning': 'MOD:00599'},
    "UBIQUITINATION": {'description': 'Ubiquitination modification', 'meaning': 'MOD:01240'},
    "SUMOYLATION": {'description': 'SUMOylation modification', 'meaning': 'MOD:01149'},
    "HYDROXYLATION": {'description': 'Hydroxylation modification', 'meaning': 'MOD:00677'},
    "LIPIDATION": {'description': 'Lipidation modification'},
    "PROTEOLYTIC_CLEAVAGE": {'description': 'Proteolytic cleavage', 'meaning': 'GO:0006508'},
    "CROSSLINKING": {'description': 'Crosslinking modification', 'meaning': 'MOD:00033'},
}

__all__ = [
    "SampleType",
    "StructuralBiologyTechnique",
    "CryoEMPreparationType",
    "CryoEMGridType",
    "VitrificationMethod",
    "CrystallizationMethod",
    "XRaySource",
    "Detector",
    "WorkflowType",
    "FileFormat",
    "DataType",
    "ProcessingStatus",
    "CoordinationGeometry",
    "MetalLigandType",
    "ProteinModificationType",
]