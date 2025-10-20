"""
Nuclear Regulatory Frameworks Value Sets

Value sets for nuclear regulatory bodies, frameworks, and compliance standards

Generated from: energy/nuclear/nuclear_regulatory.yaml
"""

from __future__ import annotations

from typing import Dict, Any, Optional
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
    "IAEA": {'description': 'International Atomic Energy Agency', 'meaning': 'CVS:regulatory_iaea'},
    "NRC": {'description': 'US Nuclear Regulatory Commission', 'meaning': 'CVS:regulatory_nrc'},
    "ONR": {'description': 'Office for Nuclear Regulation (UK)', 'meaning': 'CVS:regulatory_onr'},
    "ASN": {'description': 'Autorité de sûreté nucléaire (France)', 'meaning': 'CVS:regulatory_asn'},
    "NISA": {'description': 'Nuclear and Industrial Safety Agency (Japan)', 'meaning': 'CVS:regulatory_nisa'},
    "CNSC": {'description': 'Canadian Nuclear Safety Commission', 'meaning': 'CVS:regulatory_cnsc'},
    "STUK": {'description': 'Radiation and Nuclear Safety Authority (Finland)', 'meaning': 'CVS:regulatory_stuk'},
    "SKI": {'description': 'Swedish Nuclear Power Inspectorate', 'meaning': 'CVS:regulatory_ski'},
    "ENSI": {'description': 'Swiss Federal Nuclear Safety Inspectorate', 'meaning': 'CVS:regulatory_ensi'},
    "ROSATOM": {'description': 'State Atomic Energy Corporation (Russia)', 'meaning': 'CVS:regulatory_rosatom'},
    "CNNC": {'description': 'China National Nuclear Corporation', 'meaning': 'CVS:regulatory_cnnc'},
    "KAERI": {'description': 'Korea Atomic Energy Research Institute', 'meaning': 'CVS:regulatory_kaeri'},
    "AERB": {'description': 'Atomic Energy Regulatory Board (India)', 'meaning': 'CVS:regulatory_aerb'},
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
    "NPT": {'description': 'Nuclear Non-Proliferation Treaty', 'meaning': 'CVS:framework_npt'},
    "COMPREHENSIVE_SAFEGUARDS": {'description': 'IAEA Comprehensive Safeguards Agreements', 'meaning': 'CVS:framework_comprehensive_safeguards'},
    "ADDITIONAL_PROTOCOL": {'description': 'IAEA Additional Protocol', 'meaning': 'CVS:framework_additional_protocol'},
    "CONVENTION_NUCLEAR_SAFETY": {'description': 'Convention on Nuclear Safety', 'meaning': 'CVS:framework_convention_nuclear_safety'},
    "JOINT_CONVENTION": {'description': 'Joint Convention on the Safety of Spent Fuel Management and Radioactive Waste', 'meaning': 'CVS:framework_joint_convention'},
    "PARIS_CONVENTION": {'description': 'Paris Convention on Third Party Liability in the Field of Nuclear Energy', 'meaning': 'CVS:framework_paris_convention'},
    "VIENNA_CONVENTION": {'description': 'Vienna Convention on Civil Liability for Nuclear Damage', 'meaning': 'CVS:framework_vienna_convention'},
    "CPPNM": {'description': 'Convention on the Physical Protection of Nuclear Material', 'meaning': 'CVS:framework_cppnm'},
    "ICSANT": {'description': 'International Convention for the Suppression of Acts of Nuclear Terrorism', 'meaning': 'CVS:framework_icsant'},
    "SAFETY_STANDARDS": {'description': 'IAEA Safety Standards Series', 'meaning': 'CVS:framework_safety_standards'},
    "SECURITY_SERIES": {'description': 'IAEA Nuclear Security Series', 'meaning': 'CVS:framework_security_series'},
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
    "PRE_APPLICATION": {'description': 'Pre-application consultation and preparation', 'meaning': 'CVS:licensing_pre_application'},
    "CONSTRUCTION_PERMIT": {'description': 'Construction permit application and review', 'meaning': 'CVS:licensing_construction_permit'},
    "OPERATING_LICENSE": {'description': 'Operating license application and review', 'meaning': 'CVS:licensing_operating_license'},
    "LICENSE_RENEWAL": {'description': 'License renewal application and review', 'meaning': 'CVS:licensing_license_renewal'},
    "POWER_UPRATE": {'description': 'Power uprate license amendment', 'meaning': 'CVS:licensing_power_uprate'},
    "DECOMMISSIONING_PLAN": {'description': 'Decommissioning plan approval', 'meaning': 'CVS:licensing_decommissioning_plan'},
    "LICENSE_TERMINATION": {'description': 'License termination and site release', 'meaning': 'CVS:licensing_license_termination'},
    "DESIGN_CERTIFICATION": {'description': 'Standard design certification', 'meaning': 'CVS:licensing_design_certification'},
    "EARLY_SITE_PERMIT": {'description': 'Early site permit for future construction', 'meaning': 'CVS:licensing_early_site_permit'},
    "COMBINED_LICENSE": {'description': 'Combined construction and operating license', 'meaning': 'CVS:licensing_combined_license'},
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
    "ISO_14001": {'description': 'Environmental Management Systems', 'meaning': 'CVS:standard_iso_14001'},
    "ISO_9001": {'description': 'Quality Management Systems', 'meaning': 'CVS:standard_iso_9001'},
    "ASME_NQA_1": {'description': 'Quality Assurance Requirements for Nuclear Facility Applications', 'meaning': 'CVS:standard_asme_nqa_1'},
    "IEEE_603": {'description': 'IEEE Standard Criteria for Safety Systems for Nuclear Power Generating Stations', 'meaning': 'CVS:standard_ieee_603'},
    "IEC_61513": {'description': 'Nuclear power plants - Instrumentation and control systems', 'meaning': 'CVS:standard_iec_61513'},
    "ANSI_N45_2": {'description': 'Quality Assurance Program Requirements for Nuclear Power Plants', 'meaning': 'CVS:standard_ansi_n45_2'},
    "NUREG_0800": {'description': 'Standard Review Plan for the Review of Safety Analysis Reports', 'meaning': 'CVS:standard_nureg_0800'},
    "IAEA_GSR": {'description': 'IAEA General Safety Requirements', 'meaning': 'CVS:standard_iaea_gsr'},
    "IAEA_NSS": {'description': 'IAEA Nuclear Security Series', 'meaning': 'CVS:standard_iaea_nss'},
    "WENRA_RL": {'description': 'Western European Nuclear Regulators Association Reference Levels', 'meaning': 'CVS:standard_wenra_rl'},
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
    "ROUTINE_INSPECTION": {'description': 'Regularly scheduled inspection activities', 'meaning': 'CVS:inspection_routine'},
    "REACTIVE_INSPECTION": {'description': 'Event-driven or follow-up inspections', 'meaning': 'CVS:inspection_reactive'},
    "TEAM_INSPECTION": {'description': 'Multi-disciplinary team inspections', 'meaning': 'CVS:inspection_team'},
    "TRIENNIAL_INSPECTION": {'description': 'Three-year cycle comprehensive inspections', 'meaning': 'CVS:inspection_triennial'},
    "CONSTRUCTION_INSPECTION": {'description': 'Construction phase inspections', 'meaning': 'CVS:inspection_construction'},
    "PRE_OPERATIONAL_TESTING": {'description': 'Pre-operational testing and commissioning inspections', 'meaning': 'CVS:inspection_pre_operational'},
    "STARTUP_TESTING": {'description': 'Initial startup and power ascension inspections', 'meaning': 'CVS:inspection_startup'},
    "PERIODIC_SAFETY_REVIEW": {'description': 'Comprehensive periodic safety reviews', 'meaning': 'CVS:inspection_periodic_safety_review'},
    "INTEGRATED_INSPECTION": {'description': 'Integrated inspection program', 'meaning': 'CVS:inspection_integrated'},
    "FORCE_ON_FORCE": {'description': 'Security force-on-force exercises', 'meaning': 'CVS:inspection_force_on_force'},
    "EMERGENCY_PREPAREDNESS": {'description': 'Emergency preparedness and response inspections', 'meaning': 'CVS:inspection_emergency_preparedness'},
    "SPECIAL_INSPECTION": {'description': 'Special inspections for significant events', 'meaning': 'CVS:inspection_special'},
    "VENDOR_INSPECTION": {'description': 'Nuclear vendor and supplier inspections', 'meaning': 'CVS:inspection_vendor'},
    "CYBER_SECURITY": {'description': 'Cybersecurity program inspections', 'meaning': 'CVS:inspection_cyber_security'},
    "DECOMMISSIONING_INSPECTION": {'description': 'Decommissioning activities inspections', 'meaning': 'CVS:inspection_decommissioning'},
}

__all__ = [
    "NuclearRegulatoryBodyEnum",
    "RegulatoryFrameworkEnum",
    "LicensingStageEnum",
    "ComplianceStandardEnum",
    "InspectionTypeEnum",
]