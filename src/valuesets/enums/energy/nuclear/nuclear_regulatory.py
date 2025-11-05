"""
Nuclear Regulatory Frameworks Value Sets

Value sets for nuclear regulatory bodies, frameworks, and compliance standards

Generated from: energy/nuclear/nuclear_regulatory.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class NuclearRegulatoryBodyEnum(RichEnum):
    """
    Nuclear regulatory authorities and international organizations
    """
    # Enum members
    IAEA = "IAEA"
    NRC = "NRC"
    ONR = "ONR"
    ASN = "ASN"
    NISA = "NISA"
    CNSC = "CNSC"
    STUK = "STUK"
    SKI = "SKI"
    ENSI = "ENSI"
    ROSATOM = "ROSATOM"
    CNNC = "CNNC"
    KAERI = "KAERI"
    AERB = "AERB"

# Set metadata after class creation
NuclearRegulatoryBodyEnum._metadata = {
    "IAEA": {'description': 'International Atomic Energy Agency'},
    "NRC": {'description': 'US Nuclear Regulatory Commission'},
    "ONR": {'description': 'Office for Nuclear Regulation (UK)'},
    "ASN": {'description': 'Autorité de sûreté nucléaire (France)'},
    "NISA": {'description': 'Nuclear and Industrial Safety Agency (Japan)'},
    "CNSC": {'description': 'Canadian Nuclear Safety Commission'},
    "STUK": {'description': 'Radiation and Nuclear Safety Authority (Finland)'},
    "SKI": {'description': 'Swedish Nuclear Power Inspectorate'},
    "ENSI": {'description': 'Swiss Federal Nuclear Safety Inspectorate'},
    "ROSATOM": {'description': 'State Atomic Energy Corporation (Russia)'},
    "CNNC": {'description': 'China National Nuclear Corporation'},
    "KAERI": {'description': 'Korea Atomic Energy Research Institute'},
    "AERB": {'description': 'Atomic Energy Regulatory Board (India)'},
}

class RegulatoryFrameworkEnum(RichEnum):
    """
    Nuclear regulatory frameworks and international conventions
    """
    # Enum members
    NPT = "NPT"
    COMPREHENSIVE_SAFEGUARDS = "COMPREHENSIVE_SAFEGUARDS"
    ADDITIONAL_PROTOCOL = "ADDITIONAL_PROTOCOL"
    CONVENTION_NUCLEAR_SAFETY = "CONVENTION_NUCLEAR_SAFETY"
    JOINT_CONVENTION = "JOINT_CONVENTION"
    PARIS_CONVENTION = "PARIS_CONVENTION"
    VIENNA_CONVENTION = "VIENNA_CONVENTION"
    CPPNM = "CPPNM"
    ICSANT = "ICSANT"
    SAFETY_STANDARDS = "SAFETY_STANDARDS"
    SECURITY_SERIES = "SECURITY_SERIES"

# Set metadata after class creation
RegulatoryFrameworkEnum._metadata = {
    "NPT": {'description': 'Nuclear Non-Proliferation Treaty'},
    "COMPREHENSIVE_SAFEGUARDS": {'description': 'IAEA Comprehensive Safeguards Agreements'},
    "ADDITIONAL_PROTOCOL": {'description': 'IAEA Additional Protocol'},
    "CONVENTION_NUCLEAR_SAFETY": {'description': 'Convention on Nuclear Safety'},
    "JOINT_CONVENTION": {'description': 'Joint Convention on the Safety of Spent Fuel Management and Radioactive Waste'},
    "PARIS_CONVENTION": {'description': 'Paris Convention on Third Party Liability in the Field of Nuclear Energy'},
    "VIENNA_CONVENTION": {'description': 'Vienna Convention on Civil Liability for Nuclear Damage'},
    "CPPNM": {'description': 'Convention on the Physical Protection of Nuclear Material'},
    "ICSANT": {'description': 'International Convention for the Suppression of Acts of Nuclear Terrorism'},
    "SAFETY_STANDARDS": {'description': 'IAEA Safety Standards Series'},
    "SECURITY_SERIES": {'description': 'IAEA Nuclear Security Series'},
}

class LicensingStageEnum(RichEnum):
    """
    Stages in nuclear facility licensing process
    """
    # Enum members
    PRE_APPLICATION = "PRE_APPLICATION"
    CONSTRUCTION_PERMIT = "CONSTRUCTION_PERMIT"
    OPERATING_LICENSE = "OPERATING_LICENSE"
    LICENSE_RENEWAL = "LICENSE_RENEWAL"
    POWER_UPRATE = "POWER_UPRATE"
    DECOMMISSIONING_PLAN = "DECOMMISSIONING_PLAN"
    LICENSE_TERMINATION = "LICENSE_TERMINATION"
    DESIGN_CERTIFICATION = "DESIGN_CERTIFICATION"
    EARLY_SITE_PERMIT = "EARLY_SITE_PERMIT"
    COMBINED_LICENSE = "COMBINED_LICENSE"

# Set metadata after class creation
LicensingStageEnum._metadata = {
    "PRE_APPLICATION": {'description': 'Pre-application consultation and preparation'},
    "CONSTRUCTION_PERMIT": {'description': 'Construction permit application and review'},
    "OPERATING_LICENSE": {'description': 'Operating license application and review'},
    "LICENSE_RENEWAL": {'description': 'License renewal application and review'},
    "POWER_UPRATE": {'description': 'Power uprate license amendment'},
    "DECOMMISSIONING_PLAN": {'description': 'Decommissioning plan approval'},
    "LICENSE_TERMINATION": {'description': 'License termination and site release'},
    "DESIGN_CERTIFICATION": {'description': 'Standard design certification'},
    "EARLY_SITE_PERMIT": {'description': 'Early site permit for future construction'},
    "COMBINED_LICENSE": {'description': 'Combined construction and operating license'},
}

class ComplianceStandardEnum(RichEnum):
    """
    Nuclear safety and security compliance standards
    """
    # Enum members
    ISO_14001 = "ISO_14001"
    ISO_9001 = "ISO_9001"
    ASME_NQA_1 = "ASME_NQA_1"
    IEEE_603 = "IEEE_603"
    IEC_61513 = "IEC_61513"
    ANSI_N45_2 = "ANSI_N45_2"
    NUREG_0800 = "NUREG_0800"
    IAEA_GSR = "IAEA_GSR"
    IAEA_NSS = "IAEA_NSS"
    WENRA_RL = "WENRA_RL"

# Set metadata after class creation
ComplianceStandardEnum._metadata = {
    "ISO_14001": {'description': 'Environmental Management Systems'},
    "ISO_9001": {'description': 'Quality Management Systems'},
    "ASME_NQA_1": {'description': 'Quality Assurance Requirements for Nuclear Facility Applications'},
    "IEEE_603": {'description': 'IEEE Standard Criteria for Safety Systems for Nuclear Power Generating Stations'},
    "IEC_61513": {'description': 'Nuclear power plants - Instrumentation and control systems'},
    "ANSI_N45_2": {'description': 'Quality Assurance Program Requirements for Nuclear Power Plants'},
    "NUREG_0800": {'description': 'Standard Review Plan for the Review of Safety Analysis Reports'},
    "IAEA_GSR": {'description': 'IAEA General Safety Requirements'},
    "IAEA_NSS": {'description': 'IAEA Nuclear Security Series'},
    "WENRA_RL": {'description': 'Western European Nuclear Regulators Association Reference Levels'},
}

class InspectionTypeEnum(RichEnum):
    """
    Types of nuclear regulatory inspections and assessments
    """
    # Enum members
    ROUTINE_INSPECTION = "ROUTINE_INSPECTION"
    REACTIVE_INSPECTION = "REACTIVE_INSPECTION"
    TEAM_INSPECTION = "TEAM_INSPECTION"
    TRIENNIAL_INSPECTION = "TRIENNIAL_INSPECTION"
    CONSTRUCTION_INSPECTION = "CONSTRUCTION_INSPECTION"
    PRE_OPERATIONAL_TESTING = "PRE_OPERATIONAL_TESTING"
    STARTUP_TESTING = "STARTUP_TESTING"
    PERIODIC_SAFETY_REVIEW = "PERIODIC_SAFETY_REVIEW"
    INTEGRATED_INSPECTION = "INTEGRATED_INSPECTION"
    FORCE_ON_FORCE = "FORCE_ON_FORCE"
    EMERGENCY_PREPAREDNESS = "EMERGENCY_PREPAREDNESS"
    SPECIAL_INSPECTION = "SPECIAL_INSPECTION"
    VENDOR_INSPECTION = "VENDOR_INSPECTION"
    CYBER_SECURITY = "CYBER_SECURITY"
    DECOMMISSIONING_INSPECTION = "DECOMMISSIONING_INSPECTION"

# Set metadata after class creation
InspectionTypeEnum._metadata = {
    "ROUTINE_INSPECTION": {'description': 'Regularly scheduled inspection activities'},
    "REACTIVE_INSPECTION": {'description': 'Event-driven or follow-up inspections'},
    "TEAM_INSPECTION": {'description': 'Multi-disciplinary team inspections'},
    "TRIENNIAL_INSPECTION": {'description': 'Three-year cycle comprehensive inspections'},
    "CONSTRUCTION_INSPECTION": {'description': 'Construction phase inspections'},
    "PRE_OPERATIONAL_TESTING": {'description': 'Pre-operational testing and commissioning inspections'},
    "STARTUP_TESTING": {'description': 'Initial startup and power ascension inspections'},
    "PERIODIC_SAFETY_REVIEW": {'description': 'Comprehensive periodic safety reviews'},
    "INTEGRATED_INSPECTION": {'description': 'Integrated inspection program'},
    "FORCE_ON_FORCE": {'description': 'Security force-on-force exercises'},
    "EMERGENCY_PREPAREDNESS": {'description': 'Emergency preparedness and response inspections'},
    "SPECIAL_INSPECTION": {'description': 'Special inspections for significant events'},
    "VENDOR_INSPECTION": {'description': 'Nuclear vendor and supplier inspections'},
    "CYBER_SECURITY": {'description': 'Cybersecurity program inspections'},
    "DECOMMISSIONING_INSPECTION": {'description': 'Decommissioning activities inspections'},
}

__all__ = [
    "NuclearRegulatoryBodyEnum",
    "RegulatoryFrameworkEnum",
    "LicensingStageEnum",
    "ComplianceStandardEnum",
    "InspectionTypeEnum",
]