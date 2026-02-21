"""
Autonomous Laboratory Value Sets

Value sets for AI-driven autonomous laboratories, self-driving lab components, and experimental design methods relevant to the DOE Autonomous Labs challenge

Generated from: lab_automation/autonomous_labs.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class AutonomousLabComponentType(RichEnum):
    """
    Types of hardware and software components that comprise an AI-driven autonomous laboratory system
    """
    # Enum members
    ROBOTIC_SAMPLE_HANDLER = "ROBOTIC_SAMPLE_HANDLER"
    AUTOMATED_SYNTHESIZER = "AUTOMATED_SYNTHESIZER"
    HIGH_THROUGHPUT_SCREENING_PLATFORM = "HIGH_THROUGHPUT_SCREENING_PLATFORM"
    AUTOMATED_CHARACTERIZATION_INSTRUMENT = "AUTOMATED_CHARACTERIZATION_INSTRUMENT"
    AI_EXPERIMENT_PLANNER = "AI_EXPERIMENT_PLANNER"
    DATA_MANAGEMENT_SYSTEM = "DATA_MANAGEMENT_SYSTEM"
    SAFETY_MONITORING_SYSTEM = "SAFETY_MONITORING_SYSTEM"
    SAMPLE_STORAGE_SYSTEM = "SAMPLE_STORAGE_SYSTEM"

# Set metadata after class creation
AutonomousLabComponentType._metadata = {
    "ROBOTIC_SAMPLE_HANDLER": {'description': 'Robotic system for automated sample manipulation, transfer, and preparation', 'annotations': {'function': 'sample handling and transfer'}},
    "AUTOMATED_SYNTHESIZER": {'description': 'Automated system for chemical or biological synthesis operations', 'annotations': {'function': 'automated synthesis'}},
    "HIGH_THROUGHPUT_SCREENING_PLATFORM": {'description': 'Integrated platform for rapid screening of large numbers of samples or conditions', 'meaning': 'BAO:0010074'},
    "AUTOMATED_CHARACTERIZATION_INSTRUMENT": {'description': 'Instrument for automated measurement and characterization of samples', 'annotations': {'examples': 'automated XRD, SEM, spectroscopy'}},
    "AI_EXPERIMENT_PLANNER": {'description': 'AI-based software system that designs and plans experiments based on prior data and objectives', 'annotations': {'function': 'experiment planning and design'}},
    "DATA_MANAGEMENT_SYSTEM": {'description': 'System for automated collection, storage, and management of experimental data', 'annotations': {'function': 'data management and integration'}},
    "SAFETY_MONITORING_SYSTEM": {'description': 'System for real-time monitoring of laboratory safety conditions and automated hazard response', 'annotations': {'function': 'safety monitoring and emergency response'}},
    "SAMPLE_STORAGE_SYSTEM": {'description': 'Automated storage and retrieval system for laboratory samples', 'annotations': {'function': 'sample storage and inventory management'}},
}

class ExperimentalDesignMethodType(RichEnum):
    """
    Computational and statistical methods used for experimental design in autonomous laboratory workflows
    """
    # Enum members
    BAYESIAN_OPTIMIZATION = "BAYESIAN_OPTIMIZATION"
    ACTIVE_LEARNING = "ACTIVE_LEARNING"
    REINFORCEMENT_LEARNING = "REINFORCEMENT_LEARNING"
    EVOLUTIONARY_ALGORITHM = "EVOLUTIONARY_ALGORITHM"
    RANDOM_SEARCH = "RANDOM_SEARCH"
    GRID_SEARCH = "GRID_SEARCH"
    LATIN_HYPERCUBE_SAMPLING = "LATIN_HYPERCUBE_SAMPLING"
    DESIGN_OF_EXPERIMENTS = "DESIGN_OF_EXPERIMENTS"
    MULTI_OBJECTIVE_OPTIMIZATION = "MULTI_OBJECTIVE_OPTIMIZATION"

# Set metadata after class creation
ExperimentalDesignMethodType._metadata = {
    "BAYESIAN_OPTIMIZATION": {'description': 'Probabilistic model-based optimization using Bayesian inference to guide experimental selection', 'annotations': {'approach': 'surrogate model with acquisition function'}},
    "ACTIVE_LEARNING": {'description': 'Machine learning approach that iteratively selects the most informative experiments to perform', 'annotations': {'approach': 'query-based learning from unlabeled data'}},
    "REINFORCEMENT_LEARNING": {'description': 'Machine learning approach where an agent learns optimal experimental strategies through trial and reward', 'annotations': {'approach': 'reward-based sequential decision making'}},
    "EVOLUTIONARY_ALGORITHM": {'description': 'Optimization method inspired by biological evolution using mutation, crossover, and selection', 'annotations': {'approach': 'population-based metaheuristic'}},
    "RANDOM_SEARCH": {'description': 'Experimental design using random sampling of the parameter space', 'annotations': {'approach': 'random sampling'}},
    "GRID_SEARCH": {'description': 'Systematic exploration of parameter space using a regular grid of experimental conditions', 'annotations': {'approach': 'exhaustive grid evaluation'}},
    "LATIN_HYPERCUBE_SAMPLING": {'description': 'Statistical sampling method that ensures even coverage of each parameter dimension', 'annotations': {'approach': 'stratified random sampling'}},
    "DESIGN_OF_EXPERIMENTS": {'description': 'Classical statistical methods for planning experiments including factorial and response surface designs', 'annotations': {'approaches': 'full factorial, fractional factorial, Box-Behnken, central composite'}},
    "MULTI_OBJECTIVE_OPTIMIZATION": {'description': 'Optimization approach that simultaneously considers multiple competing objectives', 'annotations': {'approach': 'Pareto-optimal solution search'}},
}

class LabAutomationWorkflowType(RichEnum):
    """
    Types of automated workflows implemented in autonomous laboratory systems
    """
    # Enum members
    CLOSED_LOOP_OPTIMIZATION = "CLOSED_LOOP_OPTIMIZATION"
    HIGH_THROUGHPUT_SCREENING = "HIGH_THROUGHPUT_SCREENING"
    AUTOMATED_SYNTHESIS = "AUTOMATED_SYNTHESIS"
    AUTONOMOUS_CHARACTERIZATION = "AUTONOMOUS_CHARACTERIZATION"
    SELF_DRIVING_EXPERIMENTATION = "SELF_DRIVING_EXPERIMENTATION"
    ROBOTIC_SAMPLE_PREPARATION = "ROBOTIC_SAMPLE_PREPARATION"

# Set metadata after class creation
LabAutomationWorkflowType._metadata = {
    "CLOSED_LOOP_OPTIMIZATION": {'description': 'Workflow where experimental results are automatically fed back to guide subsequent experiments', 'annotations': {'characteristic': 'feedback-driven iterative optimization'}},
    "HIGH_THROUGHPUT_SCREENING": {'description': 'Workflow for rapid parallel evaluation of many samples or conditions', 'meaning': 'NCIT:C18472', 'annotations': {'characteristic': 'massively parallel evaluation'}},
    "AUTOMATED_SYNTHESIS": {'description': 'Workflow for automated execution of chemical or biological synthesis procedures', 'annotations': {'characteristic': 'automated reaction execution'}},
    "AUTONOMOUS_CHARACTERIZATION": {'description': 'Workflow for automated sample characterization using multiple analytical techniques', 'annotations': {'characteristic': 'multi-modal automated measurement'}},
    "SELF_DRIVING_EXPERIMENTATION": {'description': 'Fully autonomous workflow combining AI-driven planning, execution, and analysis without human intervention', 'annotations': {'characteristic': 'end-to-end autonomous operation'}},
    "ROBOTIC_SAMPLE_PREPARATION": {'description': 'Workflow for automated preparation of samples for analysis or further processing', 'annotations': {'characteristic': 'automated sample handling and preparation'}},
}

__all__ = [
    "AutonomousLabComponentType",
    "ExperimentalDesignMethodType",
    "LabAutomationWorkflowType",
]