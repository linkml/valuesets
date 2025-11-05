"""

Generated from: lab_automation/standards.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class AutomationStandardEnum(RichEnum):
    """
    Industry standards for laboratory automation systems
    """
    # Enum members
    SILA_2 = "SILA_2"
    LABOP = "LABOP"
    AUTOPROTOCOL = "AUTOPROTOCOL"
    CLSI_AUTO01 = "CLSI_AUTO01"
    CLSI_AUTO02 = "CLSI_AUTO02"
    CLSI_AUTO03 = "CLSI_AUTO03"
    CLSI_AUTO04 = "CLSI_AUTO04"
    CLSI_AUTO05 = "CLSI_AUTO05"

# Set metadata after class creation
AutomationStandardEnum._metadata = {
    "SILA_2": {'description': 'Standardization in Lab Automation version 2 - international standard for open connectivity in lab automation', 'annotations': {'organization': 'Society for Laboratory Automation and Screening', 'architecture': 'microservice-based', 'protocol': 'gRPC'}},
    "LABOP": {'description': 'Laboratory Open Protocol Language - open specification for laboratory protocols', 'annotations': {'format': 'RDF/OWL', 'organization': 'Bioprotocols Working Group'}},
    "AUTOPROTOCOL": {'description': 'JSON-based language for specifying experimental protocols', 'annotations': {'format': 'JSON'}},
    "CLSI_AUTO01": {'description': 'CLSI standard for Specimen Container/Specimen Carrier', 'annotations': {'organization': 'Clinical and Laboratory Standards Institute'}},
    "CLSI_AUTO02": {'description': 'CLSI standard for Bar Codes for Specimen Container Identification', 'annotations': {'organization': 'Clinical and Laboratory Standards Institute'}},
    "CLSI_AUTO03": {'description': 'CLSI standard for Communications with Automated Clinical Laboratory Systems', 'annotations': {'organization': 'Clinical and Laboratory Standards Institute'}},
    "CLSI_AUTO04": {'description': 'CLSI standard for Systems Operational Requirements, Characteristics, and Information Elements', 'annotations': {'organization': 'Clinical and Laboratory Standards Institute'}},
    "CLSI_AUTO05": {'description': 'CLSI standard for Electromechanical Interfaces', 'annotations': {'organization': 'Clinical and Laboratory Standards Institute'}},
}

class CommunicationProtocolEnum(RichEnum):
    """
    Communication protocols for laboratory automation integration
    """
    # Enum members
    GRPC = "GRPC"
    REST_API = "REST_API"
    SOAP = "SOAP"
    OPC_UA = "OPC_UA"
    MODBUS = "MODBUS"
    CUSTOM_API = "CUSTOM_API"
    SERIAL = "SERIAL"
    TCP_IP = "TCP_IP"
    USB = "USB"

# Set metadata after class creation
CommunicationProtocolEnum._metadata = {
    "GRPC": {'description': 'gRPC protocol used in SiLA 2', 'annotations': {'used_by': 'SiLA 2'}},
    "REST_API": {'description': 'RESTful HTTP-based API'},
    "SOAP": {'description': 'Simple Object Access Protocol'},
    "OPC_UA": {'description': 'OPC Unified Architecture for industrial automation', 'annotations': {'full_name': 'OPC Unified Architecture'}},
    "MODBUS": {'description': 'Serial communication protocol for industrial devices'},
    "CUSTOM_API": {'description': 'Vendor-specific custom API'},
    "SERIAL": {'description': 'Serial communication protocol (RS-232, RS-485)'},
    "TCP_IP": {'description': 'TCP/IP network protocol'},
    "USB": {'description': 'Universal Serial Bus communication'},
}

class LabwareStandardEnum(RichEnum):
    """
    Standardization specifications for laboratory labware
    """
    # Enum members
    ANSI_SLAS_1_2004 = "ANSI_SLAS_1_2004"
    ANSI_SLAS_2_2004 = "ANSI_SLAS_2_2004"
    ANSI_SLAS_3_2004 = "ANSI_SLAS_3_2004"
    ANSI_SLAS_4_2004 = "ANSI_SLAS_4_2004"
    ANSI_SLAS_6_2012 = "ANSI_SLAS_6_2012"
    SBS_FOOTPRINT = "SBS_FOOTPRINT"

# Set metadata after class creation
LabwareStandardEnum._metadata = {
    "ANSI_SLAS_1_2004": {'description': 'Microplates - Footprint Dimensions', 'annotations': {'reaffirmed': 2012, 'specification': 'Footprint Dimensions'}},
    "ANSI_SLAS_2_2004": {'description': 'Microplates - Height Dimensions', 'annotations': {'reaffirmed': 2012, 'specification': 'Height Dimensions'}},
    "ANSI_SLAS_3_2004": {'description': 'Microplates - Bottom Outside Flange Dimensions', 'annotations': {'reaffirmed': 2012, 'specification': 'Bottom Outside Flange Dimensions'}},
    "ANSI_SLAS_4_2004": {'description': 'Microplates - Well Positions', 'annotations': {'reaffirmed': 2012, 'specification': 'Well Positions'}},
    "ANSI_SLAS_6_2012": {'description': 'Microplates - Well Bottom Elevation', 'annotations': {'specification': 'Well Bottom Elevation'}},
    "SBS_FOOTPRINT": {'description': 'Society for Biomolecular Screening standard footprint (127.76mm x 85.5mm)', 'annotations': {'dimensions': '127.76mm x 85.5mm'}},
}

class IntegrationFeatureEnum(RichEnum):
    """
    Integration features for laboratory automation systems
    """
    # Enum members
    BARCODE_TRACKING = "BARCODE_TRACKING"
    AUTOMATED_DATA_TRANSFER = "AUTOMATED_DATA_TRANSFER"
    CLOUD_STORAGE_INTEGRATION = "CLOUD_STORAGE_INTEGRATION"
    SAMPLE_TRACKING = "SAMPLE_TRACKING"
    WORKFLOW_VALIDATION = "WORKFLOW_VALIDATION"
    ERROR_RECOVERY = "ERROR_RECOVERY"
    AUDIT_TRAIL = "AUDIT_TRAIL"
    ELECTRONIC_SIGNATURES = "ELECTRONIC_SIGNATURES"

# Set metadata after class creation
IntegrationFeatureEnum._metadata = {
    "BARCODE_TRACKING": {'description': 'Integration feature for tracking samples via barcodes'},
    "AUTOMATED_DATA_TRANSFER": {'description': 'Automatic transfer of data between systems'},
    "CLOUD_STORAGE_INTEGRATION": {'description': 'Integration with cloud-based storage systems'},
    "SAMPLE_TRACKING": {'description': 'Real-time tracking of sample location and status'},
    "WORKFLOW_VALIDATION": {'description': 'Automated validation of workflow definitions'},
    "ERROR_RECOVERY": {'description': 'Automated error detection and recovery mechanisms'},
    "AUDIT_TRAIL": {'description': 'Complete logging of all operations for compliance'},
    "ELECTRONIC_SIGNATURES": {'description': 'Support for electronic signatures for regulatory compliance'},
}

__all__ = [
    "AutomationStandardEnum",
    "CommunicationProtocolEnum",
    "LabwareStandardEnum",
    "IntegrationFeatureEnum",
]