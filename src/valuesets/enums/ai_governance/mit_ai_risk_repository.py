"""
MIT AI Risk Repository Taxonomies

Faithful encoding of the two classification systems of the MIT AI Risk Repository: Slattery et al., "A systematic evidence review and common frame of reference for the risks from artificial intelligence" (https://arxiv.org/abs/2408.12622), published in Patterns (2026).
The Repository is a meta-review: 1,725 risks were extracted from 74 existing taxonomies and frameworks and organised under two complementary schemes.
- The CAUSAL TAXONOMY classifies risks by their antecedents, along three
  categories -- Entity, Intent, and Timing. Each risk is classified under
  exactly one level within each category. 1,480 of 1,725 risks (86%) contained
  sufficient information to be coded against it. Encoded here as three separate
  enums, since the three categories are orthogonal and a risk carries one value
  from each.

- The DOMAIN TAXONOMY classifies risks by their effects, across 7 domains and
  24 subdomains. 1,506 of 1,725 risks (87%) were coded against it. Encoded here
  as a single hierarchical enum, with domains as top-level values and
  subdomains linked by is_a.

Subdomain descriptions are taken from Table 2 of the source. Domain and subdomain numbering is preserved verbatim in annotations, since that numbering (e.g. "7.3") is how the Repository is cited in practice and is the stable handle for mapping to it.
IMPORTANT STRUCTURAL DIFFERENCE between the two schemes, stated by the source: Causal Taxonomy levels are mutually exclusive within each category, whereas Domain Taxonomy domains are NOT mutually exclusive -- some risks span multiple domains. Consumers that assume single-assignment will misrepresent the domain taxonomy.
The source also reports that frameworks it reviewed addressed on average only 8 of the 24 subdomains, with coverage ranging from 1 to 20. Any single taxonomy's silence about a subdomain is therefore weak evidence about the subdomain and strong evidence about the taxonomy's scope.

Generated from: ai_governance/mit_ai_risk_repository.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class MITAIRiskCausalEntityEnum(RichEnum):
    """
    Entity category of the Causal Taxonomy: whether the risk is caused by decisions or actions made by humans, by AI systems, or arises from human-AI interaction (or is ambiguously specified). Across the coded database, risks were nearly equally attributed to AI systems (42%) and human decisions (38%).
    """
    # Enum members
    HUMAN = "HUMAN"
    AI = "AI"
    OTHER = "OTHER"

# Set metadata after class creation
MITAIRiskCausalEntityEnum._metadata = {
    "HUMAN": {'description': 'The risk is caused by a decision or action made by humans'},
    "AI": {'description': 'The risk is caused by a decision or action made by an AI system'},
    "OTHER": {'description': 'The risk arises from human-AI interaction rather than either agent alone, or the causing entity is ambiguous or unspecified'},
}

class MITAIRiskCausalIntentEnum(RichEnum):
    """
    Intent category of the Causal Taxonomy: whether the risk occurs as an expected outcome (intentional) or unexpected outcome (unintentional) of pursuing a goal, or is presented without clear specification of intentionality. Across the coded database, intentional and unintentional causes were similarly distributed (35% each).
    """
    # Enum members
    INTENTIONAL = "INTENTIONAL"
    UNINTENTIONAL = "UNINTENTIONAL"
    OTHER = "OTHER"

# Set metadata after class creation
MITAIRiskCausalIntentEnum._metadata = {
    "INTENTIONAL": {'description': 'The risk occurs due to an expected outcome from pursuing a goal'},
    "UNINTENTIONAL": {'description': 'The risk occurs due to an unexpected outcome from pursuing a goal'},
    "OTHER": {'description': 'The risk is presented as occurring without clearly specifying the intentionality'},
}

class MITAIRiskCausalTimingEnum(RichEnum):
    """
    Timing category of the Causal Taxonomy: whether the risk occurs before deployment, after the AI model has been trained and deployed, or spans both phases (or is unspecified). Across the coded database, frameworks tended to focus on post-deployment risks (62%), with fewer addressing pre-deployment risks (13%).
    """
    # Enum members
    PRE_DEPLOYMENT = "PRE_DEPLOYMENT"
    POST_DEPLOYMENT = "POST_DEPLOYMENT"
    OTHER = "OTHER"

# Set metadata after class creation
MITAIRiskCausalTimingEnum._metadata = {
    "PRE_DEPLOYMENT": {'description': 'The risk occurs before the AI is deployed'},
    "POST_DEPLOYMENT": {'description': 'The risk occurs after the AI model has been trained and deployed'},
    "OTHER": {'description': 'The risk occurs across both pre- and post-deployment phases, or is presented without a clearly specified time of occurrence'},
}

class MITAIRiskDomainEnum(RichEnum):
    """
    Seven domains and 24 subdomains classifying AI risks by the types of hazards and harms they describe. Domains are top-level values; subdomains are linked to their domain by is_a and annotated with the source's numbering.
    Domains are NOT mutually exclusive: the source states that some risks span multiple domains.
    """
    # Enum members
    DISCRIMINATION_AND_TOXICITY = "DISCRIMINATION_AND_TOXICITY"
    UNFAIR_DISCRIMINATION_AND_MISREPRESENTATION = "UNFAIR_DISCRIMINATION_AND_MISREPRESENTATION"
    EXPOSURE_TO_TOXIC_CONTENT = "EXPOSURE_TO_TOXIC_CONTENT"
    UNEQUAL_PERFORMANCE_ACROSS_GROUPS = "UNEQUAL_PERFORMANCE_ACROSS_GROUPS"
    PRIVACY_AND_SECURITY = "PRIVACY_AND_SECURITY"
    COMPROMISE_OF_PRIVACY = "COMPROMISE_OF_PRIVACY"
    AI_SYSTEM_SECURITY_VULNERABILITIES_AND_ATTACKS = "AI_SYSTEM_SECURITY_VULNERABILITIES_AND_ATTACKS"
    MISINFORMATION = "MISINFORMATION"
    FALSE_OR_MISLEADING_INFORMATION = "FALSE_OR_MISLEADING_INFORMATION"
    POLLUTION_OF_INFORMATION_ECOSYSTEM_AND_LOSS_OF_CONSENSUS_REALITY = "POLLUTION_OF_INFORMATION_ECOSYSTEM_AND_LOSS_OF_CONSENSUS_REALITY"
    MALICIOUS_ACTORS_AND_MISUSE = "MALICIOUS_ACTORS_AND_MISUSE"
    DISINFORMATION_SURVEILLANCE_AND_INFLUENCE_AT_SCALE = "DISINFORMATION_SURVEILLANCE_AND_INFLUENCE_AT_SCALE"
    CYBERATTACKS_WEAPON_DEVELOPMENT_OR_USE_AND_MASS_HARM = "CYBERATTACKS_WEAPON_DEVELOPMENT_OR_USE_AND_MASS_HARM"
    FRAUD_SCAMS_AND_TARGETED_MANIPULATION = "FRAUD_SCAMS_AND_TARGETED_MANIPULATION"
    HUMAN_COMPUTER_INTERACTION = "HUMAN_COMPUTER_INTERACTION"
    OVERRELIANCE_AND_UNSAFE_USE = "OVERRELIANCE_AND_UNSAFE_USE"
    LOSS_OF_HUMAN_AGENCY_AND_AUTONOMY = "LOSS_OF_HUMAN_AGENCY_AND_AUTONOMY"
    SOCIOECONOMIC_AND_ENVIRONMENTAL_HARM = "SOCIOECONOMIC_AND_ENVIRONMENTAL_HARM"
    POWER_CENTRALIZATION_AND_UNFAIR_DISTRIBUTION_OF_BENEFITS = "POWER_CENTRALIZATION_AND_UNFAIR_DISTRIBUTION_OF_BENEFITS"
    INCREASED_INEQUALITY_AND_DECLINE_IN_EMPLOYMENT_QUALITY = "INCREASED_INEQUALITY_AND_DECLINE_IN_EMPLOYMENT_QUALITY"
    ECONOMIC_AND_CULTURAL_DEVALUATION_OF_HUMAN_EFFORT = "ECONOMIC_AND_CULTURAL_DEVALUATION_OF_HUMAN_EFFORT"
    COMPETITIVE_DYNAMICS = "COMPETITIVE_DYNAMICS"
    GOVERNANCE_FAILURE = "GOVERNANCE_FAILURE"
    ENVIRONMENTAL_HARM = "ENVIRONMENTAL_HARM"
    AI_SYSTEM_SAFETY_FAILURES_AND_LIMITATIONS = "AI_SYSTEM_SAFETY_FAILURES_AND_LIMITATIONS"
    AI_PURSUING_ITS_OWN_GOALS_IN_CONFLICT_WITH_HUMAN_GOALS_OR_VALUES = "AI_PURSUING_ITS_OWN_GOALS_IN_CONFLICT_WITH_HUMAN_GOALS_OR_VALUES"
    AI_POSSESSING_DANGEROUS_CAPABILITIES = "AI_POSSESSING_DANGEROUS_CAPABILITIES"
    LACK_OF_CAPABILITY_OR_ROBUSTNESS = "LACK_OF_CAPABILITY_OR_ROBUSTNESS"
    LACK_OF_TRANSPARENCY_OR_INTERPRETABILITY = "LACK_OF_TRANSPARENCY_OR_INTERPRETABILITY"
    AI_WELFARE_AND_RIGHTS = "AI_WELFARE_AND_RIGHTS"
    MULTI_AGENT_RISKS = "MULTI_AGENT_RISKS"

# Set metadata after class creation
MITAIRiskDomainEnum._metadata = {
    "DISCRIMINATION_AND_TOXICITY": {'description': 'Unfair discrimination, exposure to toxic content, and unequal performance across groups.', 'annotations': {'node_type': 'domain', 'domain_code': '1'}},
    "UNFAIR_DISCRIMINATION_AND_MISREPRESENTATION": {'description': 'Unequal treatment of individuals or groups by AI, often based on race, gender, or other sensitive characteristics, resulting in unfair outcomes and unfair representation of those groups.', 'annotations': {'node_type': 'subdomain', 'domain_code': '1.1'}},
    "EXPOSURE_TO_TOXIC_CONTENT": {'description': 'AI that exposes users to harmful, abusive, unsafe or inappropriate content. May involve providing advice or encouraging action. Examples of toxic content include hate speech, violence, extremism, illegal acts, or child sexual abuse material, as well as content that violates community norms such as profanity, inflammatory political speech, or pornography.', 'annotations': {'node_type': 'subdomain', 'domain_code': '1.2'}},
    "UNEQUAL_PERFORMANCE_ACROSS_GROUPS": {'description': 'Accuracy and effectiveness of AI decisions and actions is dependent on group membership, where decisions in AI system design and biased training data lead to unequal outcomes, reduced benefits, increased effort, and alienation of users.', 'annotations': {'node_type': 'subdomain', 'domain_code': '1.3'}},
    "PRIVACY_AND_SECURITY": {'description': 'Privacy compromise and AI system security vulnerabilities.', 'annotations': {'node_type': 'domain', 'domain_code': '2'}},
    "COMPROMISE_OF_PRIVACY": {'description': 'AI systems that memorize and leak sensitive personal data or infer private information about individuals without their consent. Unexpected or unauthorized sharing of data and information can compromise user expectation of privacy, assist identity theft, or cause loss of confidential intellectual property.', 'annotations': {'node_type': 'subdomain', 'domain_code': '2.1'}, 'aliases': ['Compromise of privacy by leaking or correctly inferring sensitive information']},
    "AI_SYSTEM_SECURITY_VULNERABILITIES_AND_ATTACKS": {'description': 'Vulnerabilities that can be exploited in AI systems, software development toolchains, and hardware, resulting in unauthorized access, data and privacy breaches, or system manipulation causing unsafe outputs or behavior.', 'annotations': {'node_type': 'subdomain', 'domain_code': '2.2'}},
    "MISINFORMATION": {'description': 'False information and pollution of the information ecosystem.', 'annotations': {'node_type': 'domain', 'domain_code': '3'}},
    "FALSE_OR_MISLEADING_INFORMATION": {'description': 'AI systems that inadvertently generate or spread incorrect or deceptive information, which can lead to inaccurate beliefs in users and undermine their autonomy. Humans that make decisions based on false beliefs can experience physical, emotional, or material harms.', 'annotations': {'node_type': 'subdomain', 'domain_code': '3.1'}},
    "POLLUTION_OF_INFORMATION_ECOSYSTEM_AND_LOSS_OF_CONSENSUS_REALITY": {'description': 'Highly personalized AI-generated misinformation that creates "filter bubbles" where individuals only see what matches their existing beliefs, undermining shared reality and weakening social cohesion and political processes.', 'annotations': {'node_type': 'subdomain', 'domain_code': '3.2'}},
    "MALICIOUS_ACTORS_AND_MISUSE": {'description': 'Disinformation at scale, cyberattacks and weapons, and fraud and manipulation.', 'annotations': {'node_type': 'domain', 'domain_code': '4'}},
    "DISINFORMATION_SURVEILLANCE_AND_INFLUENCE_AT_SCALE": {'description': 'Using AI systems to conduct large-scale disinformation campaigns, malicious surveillance, or targeted and sophisticated automated censorship and propaganda, with the aim of manipulating political processes, public opinion, and behavior.', 'annotations': {'node_type': 'subdomain', 'domain_code': '4.1'}},
    "CYBERATTACKS_WEAPON_DEVELOPMENT_OR_USE_AND_MASS_HARM": {'description': 'Using AI systems to develop cyber weapons (e.g., by coding cheaper, more effective malware), develop new or enhance existing weapons (e.g., Lethal Autonomous Weapons or chemical, biological, radiological, nuclear, and high-yield explosives), or use weapons to cause mass harm.', 'annotations': {'node_type': 'subdomain', 'domain_code': '4.2'}},
    "FRAUD_SCAMS_AND_TARGETED_MANIPULATION": {'description': 'Using AI systems to gain a personal advantage over others such as through cheating, fraud, scams, blackmail, or targeted manipulation of beliefs or behavior. Examples include AI-facilitated plagiarism for research or education, impersonating a trusted or fake individual for illegitimate financial benefit, or creating humiliating or sexual imagery.', 'annotations': {'node_type': 'subdomain', 'domain_code': '4.3'}},
    "HUMAN_COMPUTER_INTERACTION": {'description': 'Overreliance and loss of human agency.', 'annotations': {'node_type': 'domain', 'domain_code': '5'}},
    "OVERRELIANCE_AND_UNSAFE_USE": {'description': 'Anthropomorphizing, trusting, or relying on AI systems by users, leading to emotional or material dependence and to inappropriate relationships with or expectations of AI systems. Trust can be exploited by malicious actors (e.g., to harvest information or enable manipulation), or result in harm from inappropriate use of AI in critical situations (e.g., medical emergency). Over reliance on AI systems can compromise autonomy and weaken social ties.', 'annotations': {'node_type': 'subdomain', 'domain_code': '5.1'}},
    "LOSS_OF_HUMAN_AGENCY_AND_AUTONOMY": {'description': 'Delegating by humans of key decisions to AI systems, or AI systems that make decisions that diminish human control and autonomy, potentially leading to humans feeling disempowered, losing the ability to shape a fulfilling life trajectory, or becoming cognitively enfeebled.', 'annotations': {'node_type': 'subdomain', 'domain_code': '5.2'}},
    "SOCIOECONOMIC_AND_ENVIRONMENTAL_HARM": {'description': 'Power centralisation, inequality, devaluation of human effort, competitive dynamics, governance failure, and environmental harm.', 'annotations': {'node_type': 'domain', 'domain_code': '6'}},
    "POWER_CENTRALIZATION_AND_UNFAIR_DISTRIBUTION_OF_BENEFITS": {'description': 'AI-driven concentration of power and resources within certain entities or groups, especially those with access to or ownership of powerful AI systems, leading to inequitable distribution of benefits and increased societal inequality.', 'annotations': {'node_type': 'subdomain', 'domain_code': '6.1'}},
    "INCREASED_INEQUALITY_AND_DECLINE_IN_EMPLOYMENT_QUALITY": {'description': 'Social and economic inequalities caused by widespread use of AI, such as by automating jobs, reducing the quality of employment, or producing exploitative dependencies between workers and their employers.', 'annotations': {'node_type': 'subdomain', 'domain_code': '6.2'}},
    "ECONOMIC_AND_CULTURAL_DEVALUATION_OF_HUMAN_EFFORT": {'description': 'AI systems capable of creating economic or cultural value, including through reproduction of human innovation or creativity (e.g., art, music, writing, coding, invention), destabilizing economic and social systems that rely on human effort. The ubiquity of AI-generated content may lead to reduced appreciation for human skills, disruption of creative and knowledge-based industries, and homogenization of cultural experiences.', 'annotations': {'node_type': 'subdomain', 'domain_code': '6.3'}},
    "COMPETITIVE_DYNAMICS": {'description': 'Competition by AI developers or state-like actors in an AI "race" by rapidly developing, deploying, and applying AI systems to maximize strategic or economic advantage, increasing the risk they release unsafe and error-prone systems.', 'annotations': {'node_type': 'subdomain', 'domain_code': '6.4'}},
    "GOVERNANCE_FAILURE": {'description': 'Inadequate regulatory frameworks and oversight mechanisms that fail to keep pace with AI development, leading to ineffective governance and the inability to manage AI risks appropriately.', 'annotations': {'node_type': 'subdomain', 'domain_code': '6.5'}},
    "ENVIRONMENTAL_HARM": {'description': 'The development and operation of AI systems that cause environmental harm, such as through energy consumption of data centers or the materials and carbon footprints associated with AI hardware.', 'annotations': {'node_type': 'subdomain', 'domain_code': '6.6'}},
    "AI_SYSTEM_SAFETY_FAILURES_AND_LIMITATIONS": {'description': 'Misalignment, dangerous capabilities, lack of robustness, lack of transparency, AI welfare, and multi-agent risks.', 'annotations': {'node_type': 'domain', 'domain_code': '7'}},
    "AI_PURSUING_ITS_OWN_GOALS_IN_CONFLICT_WITH_HUMAN_GOALS_OR_VALUES": {'description': 'AI systems that act in conflict with ethical standards or human goals or values, especially the goals of designers or users. These misaligned behaviors may be introduced by humans during design and development, such as through reward hacking and goal misgeneralisation, and may result in AI using dangerous capabilities such as manipulation, deception, or situational awareness to seek power, self-proliferate, or achieve other goals.', 'annotations': {'node_type': 'subdomain', 'domain_code': '7.1'}},
    "AI_POSSESSING_DANGEROUS_CAPABILITIES": {'description': 'AI systems that develop, access, or are provided with capabilities that increase their potential to cause mass harm through deception, weapons development and acquisition, persuasion and manipulation, political strategy, cyber-offense, AI development, situational awareness, and self-proliferation. These capabilities may cause mass harm due to malicious human actors, misaligned AI systems, or failure in the AI system.', 'annotations': {'node_type': 'subdomain', 'domain_code': '7.2'}},
    "LACK_OF_CAPABILITY_OR_ROBUSTNESS": {'description': 'AI systems that fail to perform reliably or effectively under varying conditions, exposing them to errors and failures that can have significant consequences, especially in critical applications or areas that require moral reasoning.', 'annotations': {'node_type': 'subdomain', 'domain_code': '7.3'}},
    "LACK_OF_TRANSPARENCY_OR_INTERPRETABILITY": {'description': 'Challenges in understanding or explaining the decision-making processes of AI systems, which can lead to mistrust, difficulty in enforcing compliance standards or holding relevant actors accountable for harms, and the inability to identify and correct errors.', 'annotations': {'node_type': 'subdomain', 'domain_code': '7.4'}},
    "AI_WELFARE_AND_RIGHTS": {'description': 'Ethical considerations regarding the treatment of potentially sentient AI entities, including discussions around their potential rights and welfare, particularly as AI systems become more advanced and autonomous.', 'annotations': {'node_type': 'subdomain', 'domain_code': '7.5'}},
    "MULTI_AGENT_RISKS": {'description': 'Risks from multi-agent interactions due to incentives (which can lead to conflict or collusion) and/or the structure of multi-agent systems, which can create cascading failures, selection pressures, new security vulnerabilities, and a lack of shared information and trust.', 'annotations': {'node_type': 'subdomain', 'domain_code': '7.6'}},
}

__all__ = [
    "MITAIRiskCausalEntityEnum",
    "MITAIRiskCausalIntentEnum",
    "MITAIRiskCausalTimingEnum",
    "MITAIRiskDomainEnum",
]