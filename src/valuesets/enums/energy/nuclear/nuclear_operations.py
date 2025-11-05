"""
Nuclear Operations and Reactor States

Classifications for nuclear reactor operational states, maintenance activities, licensing stages, and operational procedures. Based on nuclear industry standards and regulatory frameworks.

Generated from: energy/nuclear/nuclear_operations.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class ReactorOperatingStateEnum(RichEnum):
    """
    Operational states of nuclear reactors
    """
    # Enum members
    STARTUP = "STARTUP"
    CRITICAL = "CRITICAL"
    POWER_ESCALATION = "POWER_ESCALATION"
    FULL_POWER_OPERATION = "FULL_POWER_OPERATION"
    LOAD_FOLLOWING = "LOAD_FOLLOWING"
    REDUCED_POWER = "REDUCED_POWER"
    HOT_STANDBY = "HOT_STANDBY"
    COLD_SHUTDOWN = "COLD_SHUTDOWN"
    REFUELING = "REFUELING"
    REACTOR_TRIP = "REACTOR_TRIP"
    SCRAM = "SCRAM"
    EMERGENCY_SHUTDOWN = "EMERGENCY_SHUTDOWN"

# Set metadata after class creation
ReactorOperatingStateEnum._metadata = {
    "STARTUP": {'description': 'Reactor transitioning from shutdown to power operation', 'annotations': {'neutron_level': 'increasing', 'control_rod_position': 'withdrawing', 'power_level': 'rising from zero', 'duration': 'hours to days', 'operator_attention': 'high'}},
    "CRITICAL": {'description': 'Reactor achieving self-sustaining chain reaction', 'annotations': {'neutron_multiplication': 'k-effective = 1.0', 'power_level': 'minimal but self-sustaining', 'control_rod_position': 'critical position', 'milestone': 'first criticality achievement'}},
    "POWER_ESCALATION": {'description': 'Reactor increasing power toward full power operation', 'annotations': {'power_level': 'increasing incrementally', 'testing': 'ongoing at each power level', 'duration': 'days to weeks', 'procedures': 'systematic power increases'}},
    "FULL_POWER_OPERATION": {'description': 'Reactor operating at rated thermal power', 'annotations': {'power_level': '100% rated power', 'operation_mode': 'commercial electricity generation', 'duration': 'typically 12-24 months', 'fuel_burnup': 'accumulating'}},
    "LOAD_FOLLOWING": {'description': 'Reactor adjusting power to match electrical demand', 'annotations': {'power_level': 'variable based on demand', 'control_mode': 'automatic load following', 'flexibility': 'grid demand responsive', 'frequency': 'daily power variations'}},
    "REDUCED_POWER": {'description': 'Reactor operating below rated power', 'annotations': {'power_level': '<100% rated power', 'reasons': 'maintenance, grid demand, testing', 'control_rod_position': 'partially inserted'}},
    "HOT_STANDBY": {'description': 'Reactor subcritical but at operating temperature', 'annotations': {'criticality': 'subcritical', 'temperature': 'operating temperature maintained', 'pressure': 'operating pressure maintained', 'ready_time': 'rapid return to power possible'}},
    "COLD_SHUTDOWN": {'description': 'Reactor subcritical and cooled below operating temperature', 'annotations': {'criticality': 'subcritical with margin', 'temperature': '<200°F (93°C) typically', 'refueling': 'possible in this state', 'maintenance': 'major maintenance possible'}},
    "REFUELING": {'description': 'Reactor shut down for fuel replacement', 'annotations': {'reactor_head': 'removed', 'fuel_handling': 'active fuel movement', 'criticality_control': 'strict procedures', 'duration': 'typically 30-60 days'}},
    "REACTOR_TRIP": {'description': 'Rapid automatic shutdown due to safety system actuation', 'annotations': {'shutdown_speed': 'seconds', 'cause': 'safety system activation', 'control_rods': 'fully inserted rapidly', 'investigation': 'cause determination required'}},
    "SCRAM": {'description': 'Emergency rapid shutdown of reactor', 'annotations': {'shutdown_type': 'emergency shutdown', 'control_rod_insertion': 'fastest possible', 'operator_action': 'manual or automatic', 'follow_up': 'immediate safety assessment'}},
    "EMERGENCY_SHUTDOWN": {'description': 'Shutdown due to emergency conditions', 'annotations': {'urgency': 'immediate shutdown required', 'safety_systems': 'may be activated', 'investigation': 'extensive post-event analysis', 'recovery': 'detailed restart procedures'}},
}

class MaintenanceTypeEnum(RichEnum):
    """
    Types of nuclear facility maintenance activities
    """
    # Enum members
    PREVENTIVE_MAINTENANCE = "PREVENTIVE_MAINTENANCE"
    CORRECTIVE_MAINTENANCE = "CORRECTIVE_MAINTENANCE"
    PREDICTIVE_MAINTENANCE = "PREDICTIVE_MAINTENANCE"
    CONDITION_BASED_MAINTENANCE = "CONDITION_BASED_MAINTENANCE"
    REFUELING_OUTAGE_MAINTENANCE = "REFUELING_OUTAGE_MAINTENANCE"
    FORCED_OUTAGE_MAINTENANCE = "FORCED_OUTAGE_MAINTENANCE"
    IN_SERVICE_INSPECTION = "IN_SERVICE_INSPECTION"
    MODIFICATION_WORK = "MODIFICATION_WORK"

# Set metadata after class creation
MaintenanceTypeEnum._metadata = {
    "PREVENTIVE_MAINTENANCE": {'description': 'Scheduled maintenance to prevent equipment failure', 'annotations': {'schedule': 'predetermined intervals', 'purpose': 'prevent failures', 'planning': 'extensive advance planning', 'outage_type': 'planned outage'}},
    "CORRECTIVE_MAINTENANCE": {'description': 'Maintenance to repair failed or degraded equipment', 'annotations': {'trigger': 'equipment failure or degradation', 'urgency': 'varies by safety significance', 'planning': 'may be immediate', 'schedule': 'unplanned'}},
    "PREDICTIVE_MAINTENANCE": {'description': 'Maintenance based on condition monitoring', 'annotations': {'basis': 'condition monitoring data', 'timing': 'based on predicted failure', 'efficiency': 'optimized maintenance timing', 'technology': 'condition monitoring systems'}},
    "CONDITION_BASED_MAINTENANCE": {'description': 'Maintenance triggered by equipment condition assessment', 'annotations': {'assessment': 'continuous condition monitoring', 'trigger': 'condition degradation', 'optimization': 'resource optimization', 'safety': 'maintains safety margins'}},
    "REFUELING_OUTAGE_MAINTENANCE": {'description': 'Major maintenance during scheduled refueling', 'annotations': {'frequency': 'every 12-24 months', 'scope': 'major equipment inspection and repair', 'duration': '30-60 days typical', 'access': 'full plant access available'}},
    "FORCED_OUTAGE_MAINTENANCE": {'description': 'Unplanned maintenance due to equipment failure', 'annotations': {'cause': 'unexpected equipment failure', 'urgency': 'immediate attention required', 'duration': 'variable', 'safety_significance': 'may affect safety systems'}},
    "IN_SERVICE_INSPECTION": {'description': 'Required inspection of safety-related components', 'annotations': {'regulatory_requirement': 'mandated by regulations', 'frequency': 'specified intervals (typically 10 years)', 'scope': 'pressure vessels, piping, supports', 'techniques': 'non-destructive testing'}},
    "MODIFICATION_WORK": {'description': 'Changes to plant design or configuration', 'annotations': {'purpose': 'plant improvement or regulatory compliance', 'approval': 'requires design change approval', 'testing': 'extensive post-modification testing', 'documentation': 'comprehensive documentation updates'}},
}

class LicensingStageEnum(RichEnum):
    """
    Nuclear facility licensing stages
    """
    # Enum members
    SITE_PERMIT = "SITE_PERMIT"
    DESIGN_CERTIFICATION = "DESIGN_CERTIFICATION"
    CONSTRUCTION_PERMIT = "CONSTRUCTION_PERMIT"
    OPERATING_LICENSE = "OPERATING_LICENSE"
    LICENSE_RENEWAL = "LICENSE_RENEWAL"
    COMBINED_LICENSE = "COMBINED_LICENSE"
    DECOMMISSIONING_PLAN = "DECOMMISSIONING_PLAN"
    LICENSE_TERMINATION = "LICENSE_TERMINATION"

# Set metadata after class creation
LicensingStageEnum._metadata = {
    "SITE_PERMIT": {'description': 'Early site permit for nuclear facility', 'annotations': {'scope': 'site suitability evaluation', 'duration': '10-20 years typically', 'flexibility': 'technology-neutral', 'advantage': 'reduced licensing risk'}},
    "DESIGN_CERTIFICATION": {'description': 'Certification of standardized reactor design', 'annotations': {'scope': 'reactor design approval', 'duration': '15-20 years typically', 'advantage': 'reduced construction licensing time', 'standardization': 'enables multiple deployments'}},
    "CONSTRUCTION_PERMIT": {'description': 'Authorization to begin nuclear facility construction', 'annotations': {'authorization': 'construction activities', 'requirements': 'detailed design and safety analysis', 'oversight': 'construction inspection program', 'milestone': 'major licensing milestone'}},
    "OPERATING_LICENSE": {'description': 'Authorization for commercial reactor operation', 'annotations': {'authorization': 'power operation and fuel loading', 'duration': 'initially 40 years', 'renewal': 'possible for additional 20 years', 'testing': 'extensive pre-operational testing'}},
    "LICENSE_RENEWAL": {'description': 'Extension of operating license beyond initial term', 'annotations': {'extension': 'additional 20 years typical', 'review': 'aging management program review', 'basis': 'demonstrated safe operation', 'economics': 'enables continued operation'}},
    "COMBINED_LICENSE": {'description': 'Combined construction and operating license', 'annotations': {'scope': 'construction and operation authorization', 'advantage': 'single licensing process', 'requirements': 'complete design and safety analysis', 'efficiency': 'streamlined licensing approach'}},
    "DECOMMISSIONING_PLAN": {'description': 'Approval of facility decommissioning plan', 'annotations': {'scope': 'facility dismantlement plan', 'funding': 'decommissioning funding assurance', 'schedule': 'decommissioning timeline', 'end_state': 'final site condition'}},
    "LICENSE_TERMINATION": {'description': 'Final termination of nuclear facility license', 'annotations': {'completion': 'decommissioning completion', 'survey': 'final radiological survey', 'release': 'site release for unrestricted use', 'finality': 'end of regulatory oversight'}},
}

class FuelCycleOperationEnum(RichEnum):
    """
    Nuclear fuel cycle operational activities
    """
    # Enum members
    URANIUM_EXPLORATION = "URANIUM_EXPLORATION"
    URANIUM_EXTRACTION = "URANIUM_EXTRACTION"
    URANIUM_MILLING = "URANIUM_MILLING"
    URANIUM_CONVERSION = "URANIUM_CONVERSION"
    URANIUM_ENRICHMENT = "URANIUM_ENRICHMENT"
    FUEL_FABRICATION = "FUEL_FABRICATION"
    REACTOR_FUEL_LOADING = "REACTOR_FUEL_LOADING"
    REACTOR_OPERATION = "REACTOR_OPERATION"
    SPENT_FUEL_DISCHARGE = "SPENT_FUEL_DISCHARGE"
    SPENT_FUEL_STORAGE = "SPENT_FUEL_STORAGE"
    SPENT_FUEL_REPROCESSING = "SPENT_FUEL_REPROCESSING"
    WASTE_CONDITIONING = "WASTE_CONDITIONING"
    WASTE_DISPOSAL = "WASTE_DISPOSAL"

# Set metadata after class creation
FuelCycleOperationEnum._metadata = {
    "URANIUM_EXPLORATION": {'description': 'Search and evaluation of uranium deposits', 'annotations': {'activities': 'geological surveys, drilling, sampling', 'purpose': 'locate economically viable deposits', 'methods': 'airborne surveys, ground exploration'}},
    "URANIUM_EXTRACTION": {'description': 'Mining and extraction of uranium ore', 'annotations': {'methods': 'open pit, underground, in-situ leaching', 'output': 'uranium ore', 'processing': 'crushing and grinding'}},
    "URANIUM_MILLING": {'description': 'Processing of uranium ore to produce yellowcake', 'annotations': {'input': 'uranium ore', 'output': 'uranium concentrate (U3O8)', 'process': 'acid or alkaline leaching'}},
    "URANIUM_CONVERSION": {'description': 'Conversion of yellowcake to uranium hexafluoride', 'annotations': {'input': 'uranium concentrate (U3O8)', 'output': 'uranium hexafluoride (UF6)', 'purpose': 'prepare for enrichment'}},
    "URANIUM_ENRICHMENT": {'description': 'Increase U-235 concentration in uranium', 'annotations': {'input': 'natural uranium (0.711% U-235)', 'output': 'enriched uranium (3-5% typical)', 'waste': 'depleted uranium tails', 'methods': 'gas centrifuge, gaseous diffusion'}},
    "FUEL_FABRICATION": {'description': 'Manufacturing of nuclear fuel assemblies', 'annotations': {'input': 'enriched uranium', 'output': 'fuel assemblies', 'process': 'pellet production, rod assembly'}},
    "REACTOR_FUEL_LOADING": {'description': 'Installation of fresh fuel in reactor', 'annotations': {'frequency': 'every 12-24 months', 'procedure': 'careful criticality control', 'configuration': 'specific loading pattern'}},
    "REACTOR_OPERATION": {'description': 'Power generation and fuel burnup', 'annotations': {'duration': '12-24 months typical cycle', 'burnup': 'fuel depletion over time', 'output': 'electricity and fission products'}},
    "SPENT_FUEL_DISCHARGE": {'description': 'Removal of used fuel from reactor', 'annotations': {'timing': 'end of fuel cycle', 'handling': 'underwater fuel handling', 'destination': 'spent fuel pool storage'}},
    "SPENT_FUEL_STORAGE": {'description': 'Interim storage of discharged fuel', 'annotations': {'cooling': 'decay heat removal', 'duration': '5-100+ years', 'methods': 'pools, dry casks'}},
    "SPENT_FUEL_REPROCESSING": {'description': 'Chemical separation of spent fuel components', 'annotations': {'separation': 'uranium, plutonium, waste', 'recovery': 'recovers usable materials', 'waste': 'high-level waste production'}},
    "WASTE_CONDITIONING": {'description': 'Preparation of waste for storage or disposal', 'annotations': {'treatment': 'solidification, encapsulation', 'purpose': 'stable waste form', 'standards': 'waste acceptance criteria'}},
    "WASTE_DISPOSAL": {'description': 'Permanent disposal of nuclear waste', 'annotations': {'method': 'geological repository', 'isolation': 'long-term containment', 'safety': 'protect public and environment'}},
}

class ReactorControlModeEnum(RichEnum):
    """
    Reactor control and safety system operational modes
    """
    # Enum members
    MANUAL_CONTROL = "MANUAL_CONTROL"
    AUTOMATIC_CONTROL = "AUTOMATIC_CONTROL"
    REACTOR_PROTECTION_SYSTEM = "REACTOR_PROTECTION_SYSTEM"
    ENGINEERED_SAFEGUARDS = "ENGINEERED_SAFEGUARDS"
    EMERGENCY_OPERATING_PROCEDURES = "EMERGENCY_OPERATING_PROCEDURES"
    SEVERE_ACCIDENT_MANAGEMENT = "SEVERE_ACCIDENT_MANAGEMENT"

# Set metadata after class creation
ReactorControlModeEnum._metadata = {
    "MANUAL_CONTROL": {'description': 'Direct operator control of reactor systems', 'annotations': {'operator_role': 'direct manual operation', 'automation': 'minimal automation', 'response_time': 'depends on operator', 'application': 'startup, shutdown, testing'}},
    "AUTOMATIC_CONTROL": {'description': 'Automated reactor control systems', 'annotations': {'automation': 'high level automation', 'operator_role': 'supervisory', 'response_time': 'rapid automatic response', 'application': 'normal power operation'}},
    "REACTOR_PROTECTION_SYSTEM": {'description': 'Safety system monitoring for trip conditions', 'annotations': {'function': 'automatic reactor trip on unsafe conditions', 'redundancy': 'multiple independent channels', 'response_time': 'milliseconds to seconds', 'priority': 'overrides operator actions'}},
    "ENGINEERED_SAFEGUARDS": {'description': 'Safety systems for accident mitigation', 'annotations': {'function': 'mitigate consequences of accidents', 'activation': 'automatic on accident conditions', 'systems': 'emergency core cooling, containment', 'redundancy': 'multiple trains'}},
    "EMERGENCY_OPERATING_PROCEDURES": {'description': 'Operator actions for emergency conditions', 'annotations': {'guidance': 'symptom-based procedures', 'training': 'extensive operator training', 'decision_making': 'structured approach', 'coordination': 'with emergency response'}},
    "SEVERE_ACCIDENT_MANAGEMENT": {'description': 'Procedures for beyond design basis accidents', 'annotations': {'scope': 'core damage mitigation', 'guidance': 'severe accident management guidelines', 'equipment': 'portable emergency equipment', 'coordination': 'multi-unit considerations'}},
}

class OperationalProcedureEnum(RichEnum):
    """
    Standard nuclear facility operational procedures
    """
    # Enum members
    STARTUP_PROCEDURE = "STARTUP_PROCEDURE"
    SHUTDOWN_PROCEDURE = "SHUTDOWN_PROCEDURE"
    REFUELING_PROCEDURE = "REFUELING_PROCEDURE"
    SURVEILLANCE_TESTING = "SURVEILLANCE_TESTING"
    MAINTENANCE_PROCEDURE = "MAINTENANCE_PROCEDURE"
    EMERGENCY_RESPONSE = "EMERGENCY_RESPONSE"
    RADIOLOGICAL_PROTECTION = "RADIOLOGICAL_PROTECTION"
    SECURITY_PROCEDURE = "SECURITY_PROCEDURE"

# Set metadata after class creation
OperationalProcedureEnum._metadata = {
    "STARTUP_PROCEDURE": {'description': 'Systematic procedure for bringing reactor to power', 'annotations': {'phases': 'multiple phases with hold points', 'testing': 'system testing at each phase', 'authorization': 'management authorization required', 'duration': 'hours to days'}},
    "SHUTDOWN_PROCEDURE": {'description': 'Systematic procedure for shutting down reactor', 'annotations': {'control_rod_insertion': 'gradual or rapid', 'cooling': 'controlled cooldown', 'systems': 'systematic system shutdown', 'verification': 'shutdown margin verification'}},
    "REFUELING_PROCEDURE": {'description': 'Procedure for fuel handling and replacement', 'annotations': {'criticality_control': 'strict criticality prevention', 'handling': 'underwater fuel handling', 'documentation': 'detailed records', 'verification': 'independent verification'}},
    "SURVEILLANCE_TESTING": {'description': 'Regular testing of safety systems', 'annotations': {'frequency': 'specified by technical specifications', 'scope': 'functionality verification', 'documentation': 'test result documentation', 'corrective_action': 'if performance degraded'}},
    "MAINTENANCE_PROCEDURE": {'description': 'Systematic approach to equipment maintenance', 'annotations': {'work_control': 'work order control process', 'safety_tagging': 'equipment isolation', 'testing': 'post-maintenance testing', 'documentation': 'maintenance records'}},
    "EMERGENCY_RESPONSE": {'description': 'Response to emergency conditions', 'annotations': {'classification': 'event classification', 'notification': 'offsite notification', 'mitigation': 'protective action implementation', 'coordination': 'with offsite authorities'}},
    "RADIOLOGICAL_PROTECTION": {'description': 'Procedures for radiation protection', 'annotations': {'monitoring': 'radiation monitoring', 'contamination_control': 'contamination prevention', 'dose_control': 'personnel dose limits', 'emergency': 'radiological emergency response'}},
    "SECURITY_PROCEDURE": {'description': 'Physical security and access control procedures', 'annotations': {'access_control': 'personnel access authorization', 'detection': 'intrusion detection systems', 'response': 'security force response', 'coordination': 'with law enforcement'}},
}

__all__ = [
    "ReactorOperatingStateEnum",
    "MaintenanceTypeEnum",
    "LicensingStageEnum",
    "FuelCycleOperationEnum",
    "ReactorControlModeEnum",
    "OperationalProcedureEnum",
]