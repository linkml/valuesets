"""
Carcinogenicity Classification Value Sets

Standard carcinogenicity classifications from IARC (International Agency for Research on Cancer), EPA IRIS (Integrated Risk Information System), and NTP (National Toxicology Program).

Generated from: environmental_health/carcinogenicity.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class IARCCarcinogenicityGroup(RichEnum):
    """
    International Agency for Research on Cancer (IARC) classification groups for carcinogenic hazard to humans. IARC evaluates the strength of evidence that an agent can cause cancer in humans.
    """
    # Enum members
    GROUP_1 = "GROUP_1"
    GROUP_2A = "GROUP_2A"
    GROUP_2B = "GROUP_2B"
    GROUP_3 = "GROUP_3"

# Set metadata after class creation
IARCCarcinogenicityGroup._metadata = {
    "GROUP_1": {'description': 'Sufficient evidence of carcinogenicity in humans. The agent is carcinogenic to humans.', 'annotations': {'evidence_level': 'sufficient in humans', 'examples': 'asbestos, benzene, tobacco smoking, ionizing radiation'}},
    "GROUP_2A": {'description': 'Limited evidence of carcinogenicity in humans and sufficient evidence in experimental animals. The agent is probably carcinogenic to humans.', 'annotations': {'evidence_level': 'limited in humans, sufficient in animals', 'examples': 'red meat, night shift work, glyphosate'}},
    "GROUP_2B": {'description': 'Limited evidence of carcinogenicity in humans and less than sufficient evidence in experimental animals. The agent is possibly carcinogenic to humans.', 'annotations': {'evidence_level': 'limited in humans or animals', 'examples': 'coffee, pickled vegetables, gasoline engine exhaust'}},
    "GROUP_3": {'description': 'Inadequate evidence of carcinogenicity in humans and inadequate or limited evidence in experimental animals. The agent is not classifiable as to its carcinogenicity to humans.', 'annotations': {'evidence_level': 'inadequate', 'examples': 'caffeine, cholesterol, saccharin'}},
}

class EPAIRISCarcinogenicityGroup(RichEnum):
    """
    U.S. Environmental Protection Agency Integrated Risk Information System (IRIS) weight-of-evidence descriptors for carcinogenicity. These classifications characterize the extent to which available data support the hypothesis that an agent causes cancer in humans.
    """
    # Enum members
    CARCINOGENIC_TO_HUMANS = "CARCINOGENIC_TO_HUMANS"
    LIKELY_CARCINOGENIC = "LIKELY_CARCINOGENIC"
    SUGGESTIVE_EVIDENCE = "SUGGESTIVE_EVIDENCE"
    INADEQUATE_INFORMATION = "INADEQUATE_INFORMATION"
    NOT_LIKELY_CARCINOGENIC = "NOT_LIKELY_CARCINOGENIC"
    GROUP_A = "GROUP_A"
    GROUP_B1 = "GROUP_B1"
    GROUP_B2 = "GROUP_B2"
    GROUP_C = "GROUP_C"
    GROUP_D = "GROUP_D"
    GROUP_E = "GROUP_E"

# Set metadata after class creation
EPAIRISCarcinogenicityGroup._metadata = {
    "CARCINOGENIC_TO_HUMANS": {'description': 'Strong evidence of human carcinogenicity. This descriptor is appropriate when there is convincing epidemiologic evidence of a causal association between human exposure and cancer.', 'annotations': {'legacy_group': 'A', 'evidence': 'convincing epidemiologic evidence'}},
    "LIKELY_CARCINOGENIC": {'description': 'Evidence is adequate to demonstrate carcinogenic potential to humans but does not reach the weight of evidence for Carcinogenic to Humans.', 'annotations': {'legacy_group': 'B1/B2', 'evidence': 'adequate evidence'}},
    "SUGGESTIVE_EVIDENCE": {'description': 'Evidence is suggestive of carcinogenicity but not sufficient to assess human carcinogenic potential.', 'annotations': {'legacy_group': 'C', 'evidence': 'suggestive but not sufficient'}},
    "INADEQUATE_INFORMATION": {'description': 'Available data are inadequate for an assessment of human carcinogenic potential.', 'annotations': {'legacy_group': 'D', 'evidence': 'inadequate data'}},
    "NOT_LIKELY_CARCINOGENIC": {'description': 'Available data are considered robust for deciding that there is no basis for human hazard concern.', 'annotations': {'legacy_group': 'E', 'evidence': 'robust evidence of no hazard'}},
    "GROUP_A": {'description': 'Legacy EPA classification. Sufficient evidence from epidemiologic studies to support a causal association between exposure and cancer.', 'annotations': {'status': 'legacy', 'superseded_by': 'CARCINOGENIC_TO_HUMANS'}},
    "GROUP_B1": {'description': 'Legacy EPA classification. Limited evidence of carcinogenicity from epidemiologic studies.', 'annotations': {'status': 'legacy', 'superseded_by': 'LIKELY_CARCINOGENIC'}},
    "GROUP_B2": {'description': 'Legacy EPA classification. Sufficient evidence from animal studies and inadequate evidence from epidemiologic studies.', 'annotations': {'status': 'legacy', 'superseded_by': 'LIKELY_CARCINOGENIC'}},
    "GROUP_C": {'description': 'Legacy EPA classification. Limited evidence of carcinogenicity in animals in the absence of human data.', 'annotations': {'status': 'legacy', 'superseded_by': 'SUGGESTIVE_EVIDENCE'}},
    "GROUP_D": {'description': 'Legacy EPA classification. Inadequate human and animal evidence of carcinogenicity or no data available.', 'annotations': {'status': 'legacy', 'superseded_by': 'INADEQUATE_INFORMATION'}},
    "GROUP_E": {'description': 'Legacy EPA classification. No evidence of carcinogenicity in at least two adequate animal tests or in adequate epidemiologic and animal studies.', 'annotations': {'status': 'legacy', 'superseded_by': 'NOT_LIKELY_CARCINOGENIC'}},
}

class NTPCarcinogenicityGroup(RichEnum):
    """
    U.S. National Toxicology Program (NTP) Report on Carcinogens classifications. The NTP identifies and discusses agents, substances, mixtures, or exposure circumstances that may pose a carcinogenic hazard to human health.
    """
    # Enum members
    KNOWN_CARCINOGEN = "KNOWN_CARCINOGEN"
    RAHC = "RAHC"

# Set metadata after class creation
NTPCarcinogenicityGroup._metadata = {
    "KNOWN_CARCINOGEN": {'description': 'There is sufficient evidence of carcinogenicity from studies in humans, which indicates a causal relationship between exposure to the agent and human cancer.', 'annotations': {'abbreviation': 'K', 'evidence': 'sufficient human evidence', 'examples': 'arsenic, asbestos, benzene, vinyl chloride'}},
    "RAHC": {'description': 'There is limited evidence of carcinogenicity from studies in humans, which indicates that causal interpretation is credible but alternative explanations cannot be ruled out, OR there is sufficient evidence of carcinogenicity from studies in experimental animals.', 'annotations': {'abbreviation': 'RAHC', 'evidence': 'limited human or sufficient animal evidence', 'examples': 'lead compounds, styrene, trichloroethylene'}},
}

__all__ = [
    "IARCCarcinogenicityGroup",
    "EPAIRISCarcinogenicityGroup",
    "NTPCarcinogenicityGroup",
]