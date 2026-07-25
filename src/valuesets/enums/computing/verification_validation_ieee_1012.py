"""
IEEE 1012 Verification and Validation Processes

Value sets for system, software, and hardware verification and validation activities defined by IEEE 1012.

Generated from: computing/verification_validation_ieee_1012.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class VerificationValidationProcessIEEE1012(RichEnum):
    """
    Verification and validation processes applied across the system, software, and hardware life cycle.
    """
    # Enum members
    CONCEPT_AND_REQUIREMENTS_V_AND_V = "CONCEPT_AND_REQUIREMENTS_V_AND_V"
    ARCHITECTURE_AND_DESIGN_V_AND_V = "ARCHITECTURE_AND_DESIGN_V_AND_V"
    IMPLEMENTATION_V_AND_V = "IMPLEMENTATION_V_AND_V"
    INTEGRATION_V_AND_V = "INTEGRATION_V_AND_V"
    QUALIFICATION_TESTING = "QUALIFICATION_TESTING"
    INSTALLATION_AND_CHECKOUT = "INSTALLATION_AND_CHECKOUT"
    OPERATION_V_AND_V = "OPERATION_V_AND_V"
    MAINTENANCE_V_AND_V = "MAINTENANCE_V_AND_V"
    DISPOSAL_V_AND_V = "DISPOSAL_V_AND_V"

# Set metadata after class creation
VerificationValidationProcessIEEE1012._metadata = {
}

__all__ = [
    "VerificationValidationProcessIEEE1012",
]