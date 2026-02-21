"""
Particle Physics Value Sets

Value sets for particle accelerators and fundamental particles relevant to the DOE Enhancing Particle Accelerators and Unifying Physics challenges

Generated from: physics/particle_physics.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class ParticleAcceleratorType(RichEnum):
    """
    Types of particle accelerator facilities used in high-energy physics research
    """
    # Enum members
    LINEAR_ACCELERATOR = "LINEAR_ACCELERATOR"
    SYNCHROTRON = "SYNCHROTRON"
    CYCLOTRON = "CYCLOTRON"
    STORAGE_RING = "STORAGE_RING"
    FREE_ELECTRON_LASER = "FREE_ELECTRON_LASER"
    COLLIDER = "COLLIDER"
    SPALLATION_SOURCE = "SPALLATION_SOURCE"
    BETATRON = "BETATRON"

# Set metadata after class creation
ParticleAcceleratorType._metadata = {
    "LINEAR_ACCELERATOR": {'description': 'Linear accelerator (linac) that accelerates particles along a straight path', 'meaning': 'NCIT:C28169'},
    "SYNCHROTRON": {'description': 'Circular accelerator with increasing magnetic field to maintain constant orbit radius', 'meaning': 'NCIT:C48205'},
    "CYCLOTRON": {'description': 'Circular accelerator using constant magnetic field and alternating electric field', 'meaning': 'NCIT:C94881'},
    "STORAGE_RING": {'description': 'Circular ring that stores particles at constant energy for extended periods'},
    "FREE_ELECTRON_LASER": {'description': 'Accelerator-based light source using relativistic electrons in a magnetic undulator'},
    "COLLIDER": {'description': 'Accelerator that directs two counter-rotating beams into head-on collisions'},
    "SPALLATION_SOURCE": {'description': 'Accelerator-driven neutron source where protons strike a heavy metal target'},
    "BETATRON": {'description': 'Circular accelerator that uses a changing magnetic field to accelerate electrons'},
}

class FundamentalParticleType(RichEnum):
    """
    Standard Model fundamental particles classified by type
    """
    # Enum members
    ELECTRON = "ELECTRON"
    MUON = "MUON"
    TAU = "TAU"
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
    GLUON = "GLUON"
    W_BOSON = "W_BOSON"
    Z_BOSON = "Z_BOSON"
    HIGGS_BOSON = "HIGGS_BOSON"

# Set metadata after class creation
FundamentalParticleType._metadata = {
    "ELECTRON": {'description': 'First-generation charged lepton with mass 0.511 MeV', 'meaning': 'CHEBI:10545'},
    "MUON": {'description': 'Second-generation charged lepton with mass 105.66 MeV', 'meaning': 'CHEBI:36356'},
    "TAU": {'description': 'Third-generation charged lepton with mass 1777 MeV', 'meaning': 'CHEBI:36355'},
    "ELECTRON_NEUTRINO": {'description': 'First-generation neutrino associated with the electron', 'meaning': 'CHEBI:30223'},
    "MUON_NEUTRINO": {'description': 'Second-generation neutrino associated with the muon', 'meaning': 'CHEBI:36353'},
    "TAU_NEUTRINO": {'description': 'Third-generation neutrino associated with the tau lepton', 'meaning': 'CHEBI:36354'},
    "UP_QUARK": {'description': 'First-generation quark with charge +2/3', 'meaning': 'CHEBI:36366'},
    "DOWN_QUARK": {'description': 'First-generation quark with charge -1/3', 'meaning': 'CHEBI:36367'},
    "CHARM_QUARK": {'description': 'Second-generation quark with charge +2/3', 'meaning': 'CHEBI:36369'},
    "STRANGE_QUARK": {'description': 'Second-generation quark with charge -1/3', 'meaning': 'CHEBI:36368'},
    "TOP_QUARK": {'description': 'Third-generation quark with charge +2/3', 'meaning': 'CHEBI:36371'},
    "BOTTOM_QUARK": {'description': 'Third-generation quark with charge -1/3', 'meaning': 'CHEBI:36370'},
    "PHOTON": {'description': 'Massless gauge boson mediating the electromagnetic force', 'meaning': 'CHEBI:30212'},
    "GLUON": {'description': 'Massless gauge boson mediating the strong force between quarks'},
    "W_BOSON": {'description': 'Massive gauge boson mediating the charged weak interaction'},
    "Z_BOSON": {'description': 'Massive gauge boson mediating the neutral weak interaction'},
    "HIGGS_BOSON": {'description': 'Scalar boson associated with the Higgs field and mass generation mechanism', 'meaning': 'CHEBI:146278'},
}

class DetectorType(RichEnum):
    """
    Types of detectors used in particle physics experiments
    """
    # Enum members
    CALORIMETER = "CALORIMETER"
    TRACKING_DETECTOR = "TRACKING_DETECTOR"
    TIME_PROJECTION_CHAMBER = "TIME_PROJECTION_CHAMBER"
    CHERENKOV_DETECTOR = "CHERENKOV_DETECTOR"
    SCINTILLATOR = "SCINTILLATOR"
    SILICON_STRIP_DETECTOR = "SILICON_STRIP_DETECTOR"
    DRIFT_CHAMBER = "DRIFT_CHAMBER"
    MUON_SPECTROMETER = "MUON_SPECTROMETER"

# Set metadata after class creation
DetectorType._metadata = {
    "CALORIMETER": {'description': 'Detector that measures the total energy of incident particles by absorbing them'},
    "TRACKING_DETECTOR": {'description': 'Detector that records the trajectories of charged particles'},
    "TIME_PROJECTION_CHAMBER": {'description': 'Gas-filled detector that provides three-dimensional particle track reconstruction'},
    "CHERENKOV_DETECTOR": {'description': 'Detector that identifies particles by measuring Cherenkov radiation emitted in a medium'},
    "SCINTILLATOR": {'description': 'Detector using scintillating material that emits light when traversed by ionizing radiation'},
    "SILICON_STRIP_DETECTOR": {'description': 'Semiconductor detector using finely segmented silicon strips for precise position measurement'},
    "DRIFT_CHAMBER": {'description': 'Gas-filled wire chamber that measures particle positions from electron drift times'},
    "MUON_SPECTROMETER": {'description': 'Large detector system designed to identify and measure the momentum of muons'},
}

__all__ = [
    "ParticleAcceleratorType",
    "FundamentalParticleType",
    "DetectorType",
]