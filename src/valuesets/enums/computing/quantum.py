"""
Quantum Computing Value Sets

Value sets for quantum computing concepts relevant to the DOE Quantum Algorithms and Quantum Systems challenges

Generated from: computing/quantum.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class QubitType(RichEnum):
    """
    Types of physical qubit implementations used in quantum computing hardware
    """
    # Enum members
    SUPERCONDUCTING = "SUPERCONDUCTING"
    TRAPPED_ION = "TRAPPED_ION"
    PHOTONIC = "PHOTONIC"
    TOPOLOGICAL = "TOPOLOGICAL"
    NEUTRAL_ATOM = "NEUTRAL_ATOM"
    QUANTUM_DOT = "QUANTUM_DOT"
    NITROGEN_VACANCY_CENTER = "NITROGEN_VACANCY_CENTER"
    SPIN_QUBIT = "SPIN_QUBIT"

# Set metadata after class creation
QubitType._metadata = {
    "SUPERCONDUCTING": {'description': 'Superconducting qubit using Josephson junctions cooled to millikelvin temperatures'},
    "TRAPPED_ION": {'description': 'Qubit encoded in electronic states of trapped atomic ions'},
    "PHOTONIC": {'description': 'Qubit encoded in quantum states of photons', 'meaning': 'CHEBI:30212'},
    "TOPOLOGICAL": {'description': 'Qubit based on topological states of matter resistant to local perturbations'},
    "NEUTRAL_ATOM": {'description': 'Qubit encoded in energy levels of electrically neutral atoms held in optical traps'},
    "QUANTUM_DOT": {'description': 'Qubit using semiconductor quantum dot nanostructures', 'meaning': 'NCIT:C62378'},
    "NITROGEN_VACANCY_CENTER": {'description': 'Qubit based on nitrogen-vacancy defect centers in diamond lattice'},
    "SPIN_QUBIT": {'description': 'Qubit encoded in the spin state of an electron or nucleus in a semiconductor'},
}

class QuantumAlgorithmCategoryType(RichEnum):
    """
    Categories of quantum algorithms by their primary application domain
    """
    # Enum members
    OPTIMIZATION = "OPTIMIZATION"
    SIMULATION = "SIMULATION"
    MACHINE_LEARNING = "MACHINE_LEARNING"
    CRYPTOGRAPHY = "CRYPTOGRAPHY"
    LINEAR_ALGEBRA = "LINEAR_ALGEBRA"
    SEARCH = "SEARCH"
    ERROR_CORRECTION = "ERROR_CORRECTION"
    VARIATIONAL = "VARIATIONAL"

# Set metadata after class creation
QuantumAlgorithmCategoryType._metadata = {
    "OPTIMIZATION": {'description': 'Quantum algorithms for combinatorial and continuous optimization problems'},
    "SIMULATION": {'description': 'Quantum algorithms for simulating physical and chemical systems'},
    "MACHINE_LEARNING": {'description': 'Quantum algorithms for machine learning and pattern recognition tasks'},
    "CRYPTOGRAPHY": {'description': 'Quantum algorithms for cryptographic applications including key distribution and code breaking'},
    "LINEAR_ALGEBRA": {'description': 'Quantum algorithms for linear algebra problems such as solving linear systems'},
    "SEARCH": {'description': 'Quantum search algorithms for unstructured database search'},
    "ERROR_CORRECTION": {'description': 'Quantum error correction codes and fault-tolerant computation protocols'},
    "VARIATIONAL": {'description': 'Hybrid quantum-classical variational algorithms for near-term quantum devices'},
}

__all__ = [
    "QubitType",
    "QuantumAlgorithmCategoryType",
]