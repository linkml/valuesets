"""

Generated from: lab_automation/protocols.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class WorkflowOrchestrationTypeEnum(RichEnum):
    """
    Types of workflow orchestration in laboratory automation systems
    """
    # Enum members
    STATIC_ORCHESTRATION = "STATIC_ORCHESTRATION"
    DYNAMIC_ORCHESTRATION = "DYNAMIC_ORCHESTRATION"
    HYBRID_ORCHESTRATION = "HYBRID_ORCHESTRATION"
    EVENT_DRIVEN = "EVENT_DRIVEN"
    PARALLEL_PROCESSING = "PARALLEL_PROCESSING"

# Set metadata after class creation
WorkflowOrchestrationTypeEnum._metadata = {
    "STATIC_ORCHESTRATION": {'description': 'Pre-planned orchestration based on known constraints and fixed workflow'},
    "DYNAMIC_ORCHESTRATION": {'description': 'Real-time orchestration that adapts to changing conditions and events'},
    "HYBRID_ORCHESTRATION": {'description': 'Combination of static planning with dynamic replanning capabilities'},
    "EVENT_DRIVEN": {'description': 'Orchestration triggered by specific events in the system'},
    "PARALLEL_PROCESSING": {'description': 'Orchestration that enables concurrent execution of independent tasks'},
}

class SchedulerTypeEnum(RichEnum):
    """
    Types of scheduling algorithms for laboratory automation
    """
    # Enum members
    STATIC_SCHEDULER = "STATIC_SCHEDULER"
    DYNAMIC_SCHEDULER = "DYNAMIC_SCHEDULER"
    PRIORITY_BASED = "PRIORITY_BASED"
    FIFO = "FIFO"
    RESOURCE_AWARE = "RESOURCE_AWARE"
    DEADLINE_DRIVEN = "DEADLINE_DRIVEN"

# Set metadata after class creation
SchedulerTypeEnum._metadata = {
    "STATIC_SCHEDULER": {'description': 'Makes decisions based on known constraints requiring upfront planning'},
    "DYNAMIC_SCHEDULER": {'description': 'Adapts scheduling decisions in real-time based on system state'},
    "PRIORITY_BASED": {'description': 'Schedules tasks based on assigned priority levels'},
    "FIFO": {'description': 'First-in-first-out scheduling'},
    "RESOURCE_AWARE": {'description': 'Schedules tasks considering available resources and constraints'},
    "DEADLINE_DRIVEN": {'description': 'Schedules tasks to meet specified deadlines'},
}

class ProtocolStateEnum(RichEnum):
    """
    Execution states of laboratory protocols
    """
    # Enum members
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    PAUSED = "PAUSED"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    ABORTED = "ABORTED"
    VALIDATING = "VALIDATING"
    WAITING_FOR_RESOURCE = "WAITING_FOR_RESOURCE"

# Set metadata after class creation
ProtocolStateEnum._metadata = {
    "PENDING": {'description': 'Protocol is queued but not yet started'},
    "RUNNING": {'description': 'Protocol is currently executing'},
    "PAUSED": {'description': 'Protocol execution has been temporarily suspended'},
    "COMPLETED": {'description': 'Protocol has finished successfully'},
    "FAILED": {'description': 'Protocol execution has failed'},
    "ABORTED": {'description': 'Protocol execution was manually aborted'},
    "VALIDATING": {'description': 'Protocol is being validated before execution'},
    "WAITING_FOR_RESOURCE": {'description': 'Protocol is waiting for required resources to become available'},
}

class ExecutionModeEnum(RichEnum):
    """
    Modes of protocol execution
    """
    # Enum members
    AUTOMATED = "AUTOMATED"
    MANUAL = "MANUAL"
    SEMI_AUTOMATED = "SEMI_AUTOMATED"
    SUPERVISED = "SUPERVISED"
    SIMULATION = "SIMULATION"
    DRY_RUN = "DRY_RUN"

# Set metadata after class creation
ExecutionModeEnum._metadata = {
    "AUTOMATED": {'description': 'Fully automated execution without human intervention'},
    "MANUAL": {'description': 'Manual execution by human operator'},
    "SEMI_AUTOMATED": {'description': 'Combination of automated and manual steps'},
    "SUPERVISED": {'description': 'Automated execution with human supervision'},
    "SIMULATION": {'description': 'Simulated execution for testing and validation'},
    "DRY_RUN": {'description': 'Test execution without actual operations'},
}

class WorkflowErrorHandlingEnum(RichEnum):
    """
    Error handling strategies in laboratory automation workflows
    """
    # Enum members
    ABORT_ON_ERROR = "ABORT_ON_ERROR"
    RETRY = "RETRY"
    SKIP_AND_CONTINUE = "SKIP_AND_CONTINUE"
    NOTIFY_AND_PAUSE = "NOTIFY_AND_PAUSE"
    ROLLBACK = "ROLLBACK"
    FAILOVER = "FAILOVER"

# Set metadata after class creation
WorkflowErrorHandlingEnum._metadata = {
    "ABORT_ON_ERROR": {'description': 'Terminate workflow immediately upon encountering an error'},
    "RETRY": {'description': 'Attempt to retry the failed operation'},
    "SKIP_AND_CONTINUE": {'description': 'Skip the failed operation and continue with the workflow'},
    "NOTIFY_AND_PAUSE": {'description': 'Notify operator and pause workflow for intervention'},
    "ROLLBACK": {'description': 'Revert to previous stable state'},
    "FAILOVER": {'description': 'Switch to backup resource or alternative execution path'},
}

class IntegrationSystemEnum(RichEnum):
    """
    Types of systems integrated with laboratory automation platforms
    """
    # Enum members
    LIMS = "LIMS"
    ELN = "ELN"
    MES = "MES"
    SCADA = "SCADA"
    CLOUD_STORAGE = "CLOUD_STORAGE"
    DATABASE = "DATABASE"

# Set metadata after class creation
IntegrationSystemEnum._metadata = {
    "LIMS": {'description': 'Laboratory Information Management System', 'annotations': {'full_name': 'Laboratory Information Management System'}},
    "ELN": {'description': 'Electronic Laboratory Notebook', 'annotations': {'full_name': 'Electronic Laboratory Notebook'}},
    "MES": {'description': 'Manufacturing Execution System', 'annotations': {'full_name': 'Manufacturing Execution System'}},
    "SCADA": {'description': 'Supervisory Control and Data Acquisition', 'annotations': {'full_name': 'Supervisory Control and Data Acquisition'}},
    "CLOUD_STORAGE": {'description': 'Cloud-based data storage systems'},
    "DATABASE": {'description': 'Laboratory database systems'},
}

__all__ = [
    "WorkflowOrchestrationTypeEnum",
    "SchedulerTypeEnum",
    "ProtocolStateEnum",
    "ExecutionModeEnum",
    "WorkflowErrorHandlingEnum",
    "IntegrationSystemEnum",
]