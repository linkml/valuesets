"""
AI Risk Taxonomy Dimensions

Cross-cutting dimensions for describing, comparing, and mapping AI risk taxonomies -- what Berman et al. (2026) call Sociotechnical Outcome Taxonomies (SOT).
Most published AI risk taxonomies enumerate *categories of harm* but leave implicit the dimensions along which those categories are organised: what kind of thing a category names (a hazard? a risk? a realised harm?), whether it has been observed or is anticipated, who is affected and at what level, which actor's decision brings it about, and where in the AI lifecycle that decision sits. Berman et al. identify the last of these as a central failure of current SOT: they "typically enumerate harms without linking them to decision points or actors implicated in their occurrence, leaving accountability difficult to assign."
This module supplies those dimensions as reusable value sets so that any specific taxonomy -- the ones encoded in the sibling modules of this directory, or others -- can be annotated along them rather than restating them. It is deliberately taxonomy-neutral: it names no risk categories of its own.
SCOPE AND BOUNDARY CONDITIONS (per the extensibility recommendations of Berman et al. section on SOT design): these value sets describe the *structure* of risk classification, not the risks themselves, and not risk magnitude, likelihood, or acceptability. Severity and priority scales live in data_science/priority_severity. Risk treatment and control selection, assurance and conformity-assessment regimes, and jurisdiction-specific regulatory risk tiers (e.g. the EU AI Act's unacceptable/high/limited/minimal tiers) are all adjacent and NOT covered here; they are legitimate extension points.

Generated from: ai_governance/risk_taxonomy_dimensions.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class SociotechnicalOutcomeTypeEnum(RichEnum):
    """
    The kind of entity a taxonomy entry names. Berman et al. (2026) argue that SOT interoperability requires "clear distinctions between risks, impacts, and harms" as an organising primitive, because two taxonomies that use compatible conventions can be aligned even where their categorical content differs. Many published taxonomies mix these types within a single flat list; recording the type makes the mixture visible rather than silently flattening it.
    """
    # Enum members
    HAZARD = "HAZARD"
    RISK = "RISK"
    IMPACT = "IMPACT"
    HARM = "HARM"
    BENEFIT = "BENEFIT"

# Set metadata after class creation
SociotechnicalOutcomeTypeEnum._metadata = {
    "HAZARD": {'description': 'A source or condition with the potential to cause harm, independent of whether harm occurs. A property of the system or its context.'},
    "RISK": {'description': 'The possibility of harm arising, typically understood as combining a hazard with some likelihood and severity of the harm it may produce.'},
    "IMPACT": {'description': 'A change in the world attributable to the AI system, which may be negative, positive, or mixed. Broader than harm.'},
    "HARM": {'description': 'A realised setback to the interests or wellbeing of a person, group, or other entity. Distinguished from RISK by having actually occurred.'},
    "BENEFIT": {'description': 'A realised positive outcome. Included because several taxonomies pair harms with benefits, and dropping the pairing distorts their structure.'},
}

class RiskEvidenceStatusEnum(RichEnum):
    """
    The evidentiary standing of a risk category. Berman et al. (2026) list the distinction "between observed and anticipated effects" among the structural conventions needed for SOT to be comparable. Weidinger et al. (2022) apply exactly this distinction internally, labelling risks "observed" where already evidenced in language models and "anticipated" where not yet observed but considered sufficiently likely to merit attention.
    """
    # Enum members
    OBSERVED = "OBSERVED"
    ANTICIPATED = "ANTICIPATED"
    SPECULATIVE = "SPECULATIVE"
    CONTESTED = "CONTESTED"

# Set metadata after class creation
RiskEvidenceStatusEnum._metadata = {
    "OBSERVED": {'description': 'The risk has been empirically evidenced in deployed or studied systems.'},
    "ANTICIPATED": {'description': 'The risk has not yet been observed but is considered sufficiently likely to merit attention.'},
    "SPECULATIVE": {'description': 'The risk is conjectured, with no evidentiary base and no established consensus that it is likely.'},
    "CONTESTED": {'description': 'Whether the risk is real, or whether the evidence supports it, is actively disputed among relevant experts or affected communities.'},
}

class HarmBearerLevelEnum(RichEnum):
    """
    The level of social organisation at which a harm is borne. Berman et al. (2026) name the distinction "between types of harm and levels at which they occur" as a structural convention required for SOT interoperability; collapsing the two is a common source of incommensurability between taxonomies.
    """
    # Enum members
    INDIVIDUAL = "INDIVIDUAL"
    GROUP = "GROUP"
    COMMUNITY = "COMMUNITY"
    ORGANIZATION = "ORGANIZATION"
    SOCIETY = "SOCIETY"
    GLOBAL = "GLOBAL"
    NON_HUMAN_ANIMAL = "NON_HUMAN_ANIMAL"
    ENVIRONMENT = "ENVIRONMENT"
    AI_SYSTEM = "AI_SYSTEM"

# Set metadata after class creation
HarmBearerLevelEnum._metadata = {
    "INDIVIDUAL": {'description': 'Borne by a specific person, whether or not they are a user of the system'},
    "GROUP": {'description': 'Borne by people sharing a characteristic (e.g. a demographic group), including via unequal treatment or performance across groups'},
    "COMMUNITY": {'description': 'Borne by a located or self-identifying community'},
    "ORGANIZATION": {'description': 'Borne by a firm, institution, or other organised body'},
    "SOCIETY": {'description': 'Borne by a society or polity as a whole, e.g. through effects on institutions, shared information, or democratic processes'},
    "GLOBAL": {'description': 'Borne across societies, at planetary or transnational scale'},
    "NON_HUMAN_ANIMAL": {'description': 'Borne by non-human animals'},
    "ENVIRONMENT": {'description': 'Borne by ecosystems or the physical environment'},
    "AI_SYSTEM": {'description': 'Borne by the AI system itself, under framings that treat AI welfare as a coherent category. Included because at least one major taxonomy (the MIT AI Risk Repository, subdomain 7.5) contains such a category; including it here does not endorse the framing.'},
}

class SociotechnicalHarmTypeEnum(RichEnum):
    """
    Modality of harm from algorithmic systems, following the five major themes of Shelby et al. (2023), derived from a scoping review of 172 computing research papers. This is the "harm modality" dimension: it classifies the *kind* of injury done, orthogonally to the domain in which it occurs, so that domain taxonomies organised by application area can be cross-cut by it.
    """
    # Enum members
    REPRESENTATIONAL = "REPRESENTATIONAL"
    ALLOCATIVE = "ALLOCATIVE"
    QUALITY_OF_SERVICE = "QUALITY_OF_SERVICE"
    INTERPERSONAL = "INTERPERSONAL"
    SOCIAL_SYSTEM = "SOCIAL_SYSTEM"

# Set metadata after class creation
SociotechnicalHarmTypeEnum._metadata = {
    "REPRESENTATIONAL": {'description': 'Harms that demean, stereotype, erase, or otherwise misrepresent social groups, independent of any resource allocation.'},
    "ALLOCATIVE": {'description': 'Harms arising from the withholding or unequal distribution of opportunities, resources, or information.'},
    "QUALITY_OF_SERVICE": {'description': 'Harms arising where a system performs less well for some people than others, imposing extra effort, reduced benefit, or outright failure.'},
    "INTERPERSONAL": {'description': 'Harms to relations between people, including loss of agency, privacy violation, and technology-facilitated harassment or coercion.'},
    "SOCIAL_SYSTEM": {'description': 'Harms to societal structures and shared conditions, including information ecosystems, labour, culture, and the environment.', 'aliases': ['societal harm']},
}

class AIActorRoleEnum(RichEnum):
    """
    Roles held by actors implicated in the occurrence or mitigation of an AI risk. Berman et al. (2026) find that SOT "typically enumerate harms without linking them to decision points or actors implicated in their occurrence, leaving accountability difficult to assign"; this value set exists so a taxonomy entry can name the actor rather than leaving it unstated.
    An actor may hold several roles at once, and roles may be held by individuals, teams, or organisations.
    """
    # Enum members
    DATA_SUBJECT = "DATA_SUBJECT"
    DATA_WORKER = "DATA_WORKER"
    DATASET_CURATOR = "DATASET_CURATOR"
    MODEL_DEVELOPER = "MODEL_DEVELOPER"
    MODEL_PROVIDER = "MODEL_PROVIDER"
    APPLICATION_DEVELOPER = "APPLICATION_DEVELOPER"
    DEPLOYER = "DEPLOYER"
    PROCUREMENT_DECISION_MAKER = "PROCUREMENT_DECISION_MAKER"
    END_USER = "END_USER"
    AFFECTED_NON_USER = "AFFECTED_NON_USER"
    PLATFORM_OPERATOR = "PLATFORM_OPERATOR"
    COMPUTE_PROVIDER = "COMPUTE_PROVIDER"
    EVALUATOR = "EVALUATOR"
    AUDITOR = "AUDITOR"
    REGULATOR = "REGULATOR"
    STANDARDS_BODY = "STANDARDS_BODY"
    CIVIL_SOCIETY_ORGANIZATION = "CIVIL_SOCIETY_ORGANIZATION"
    RESEARCHER = "RESEARCHER"
    MALICIOUS_ACTOR = "MALICIOUS_ACTOR"

# Set metadata after class creation
AIActorRoleEnum._metadata = {
    "DATA_SUBJECT": {'description': 'A person whose data is present in, or inferable from, training data'},
    "DATA_WORKER": {'description': 'A person performing data collection, annotation, or content moderation labour, including under outsourced arrangements'},
    "DATASET_CURATOR": {'description': 'An actor selecting, filtering, or documenting training data'},
    "MODEL_DEVELOPER": {'description': 'An actor training or fine-tuning the model'},
    "MODEL_PROVIDER": {'description': 'An actor releasing or serving a model to others, and setting the terms of that release'},
    "APPLICATION_DEVELOPER": {'description': 'An actor building a product or service on top of a model'},
    "DEPLOYER": {'description': 'An actor putting a system into use in a particular context, who may differ from the party that built it'},
    "PROCUREMENT_DECISION_MAKER": {'description': 'An actor deciding whether and on what terms to acquire a system'},
    "END_USER": {'description': 'A person interacting directly with the deployed system'},
    "AFFECTED_NON_USER": {'description': 'A person affected by the system without interacting with it, and typically without having consented to it'},
    "PLATFORM_OPERATOR": {'description': 'An actor operating distribution or hosting infrastructure'},
    "COMPUTE_PROVIDER": {'description': 'An actor supplying training or inference compute'},
    "EVALUATOR": {'description': 'An actor conducting evaluations, red-teaming, or benchmarking'},
    "AUDITOR": {'description': 'An actor conducting external or internal audit of the system'},
    "REGULATOR": {'description': 'A public body setting or enforcing binding rules'},
    "STANDARDS_BODY": {'description': 'An actor developing voluntary standards or conformity regimes'},
    "CIVIL_SOCIETY_ORGANIZATION": {'description': 'An advocacy, community, or public-interest organisation representing affected parties'},
    "RESEARCHER": {'description': 'An actor studying the system or its effects, including SOT developers'},
    "MALICIOUS_ACTOR": {'description': 'An actor deliberately using the system to cause harm or gain illegitimate advantage'},
}

class AILifecycleStageEnum(RichEnum):
    """
    Stages of the AI system lifecycle, used to locate where in the development and deployment pipeline a risk arises or can be addressed. Coarse-grained and deliberately generic, so that it can be aligned with the lifecycle models used by specific governance regimes rather than committing to one.
    Note that the boundary between stages is a matter of convention: several taxonomies collapse the whole of pre-release work into a single "development" stage, and the MIT AI Risk Repository's Timing category reduces it further to pre-deployment versus post-deployment.
    """
    # Enum members
    PROBLEM_FORMULATION = "PROBLEM_FORMULATION"
    DATA_COLLECTION = "DATA_COLLECTION"
    DATA_PREPARATION = "DATA_PREPARATION"
    MODEL_TRAINING = "MODEL_TRAINING"
    MODEL_ADAPTATION = "MODEL_ADAPTATION"
    EVALUATION = "EVALUATION"
    RELEASE_DECISION = "RELEASE_DECISION"
    DEPLOYMENT = "DEPLOYMENT"
    OPERATION_AND_MONITORING = "OPERATION_AND_MONITORING"
    INCIDENT_RESPONSE = "INCIDENT_RESPONSE"
    REDRESS = "REDRESS"
    DECOMMISSIONING = "DECOMMISSIONING"

# Set metadata after class creation
AILifecycleStageEnum._metadata = {
    "PROBLEM_FORMULATION": {'description': 'Deciding what problem the system addresses, for whom, and whether to build it at all'},
    "DATA_COLLECTION": {'description': 'Sourcing, scraping, purchasing, or otherwise acquiring data'},
    "DATA_PREPARATION": {'description': 'Cleaning, filtering, annotating, and documenting data'},
    "MODEL_TRAINING": {'description': 'Pre-training or otherwise fitting model parameters'},
    "MODEL_ADAPTATION": {'description': 'Fine-tuning, instruction-tuning, preference optimisation, or other post-training alignment work'},
    "EVALUATION": {'description': 'Benchmarking, red-teaming, and other pre-release assessment'},
    "RELEASE_DECISION": {'description': 'Deciding whether, to whom, and under what access conditions to release the model or system'},
    "DEPLOYMENT": {'description': 'Integrating the system into a product, service, or workflow'},
    "OPERATION_AND_MONITORING": {'description': 'Running the system in production and observing its behaviour and effects'},
    "INCIDENT_RESPONSE": {'description': 'Detecting, investigating, and responding to realised harms'},
    "REDRESS": {'description': 'Providing remedy to affected parties. Listed separately from incident response because the two are frequently owned by different actors and the second is often absent.'},
    "DECOMMISSIONING": {'description': 'Withdrawing, deprecating, or shutting down the system'},
}

class AIGovernanceDecisionPointEnum(RichEnum):
    """
    Concrete decisions at which an AI risk may be introduced, amplified, or mitigated, and to which accountability for it can therefore be attached.
    This is the dimension Berman et al. (2026) identify as most conspicuously missing from existing SOT. Where AILifecycleStageEnum answers "when", this answers "at which choice, by whom" -- the granularity at which a taxonomy entry becomes actionable for a product team rather than merely descriptive. Each decision point typically pairs with one or more AIActorRoleEnum values.
    """
    # Enum members
    BUILD_OR_NOT_DECISION = "BUILD_OR_NOT_DECISION"
    SCOPE_DEFINITION_DECISION = "SCOPE_DEFINITION_DECISION"
    DATA_SOURCING_DECISION = "DATA_SOURCING_DECISION"
    DATA_EXCLUSION_DECISION = "DATA_EXCLUSION_DECISION"
    ANNOTATION_GUIDELINE_DECISION = "ANNOTATION_GUIDELINE_DECISION"
    DATA_WORKER_CONDITIONS_DECISION = "DATA_WORKER_CONDITIONS_DECISION"
    OBJECTIVE_DECISION = "OBJECTIVE_DECISION"
    SAFETY_MITIGATION_DECISION = "SAFETY_MITIGATION_DECISION"
    EVALUATION_DESIGN_DECISION = "EVALUATION_DESIGN_DECISION"
    RELEASE_MODALITY_DECISION = "RELEASE_MODALITY_DECISION"
    ACCESS_CONTROL_DECISION = "ACCESS_CONTROL_DECISION"
    USE_POLICY_DECISION = "USE_POLICY_DECISION"
    DISCLOSURE_DECISION = "DISCLOSURE_DECISION"
    MONITORING_DECISION = "MONITORING_DECISION"
    INCIDENT_ESCALATION_DECISION = "INCIDENT_ESCALATION_DECISION"
    REDRESS_DECISION = "REDRESS_DECISION"
    DEPRECATION_DECISION = "DEPRECATION_DECISION"
    PROCUREMENT_DECISION = "PROCUREMENT_DECISION"

# Set metadata after class creation
AIGovernanceDecisionPointEnum._metadata = {
    "BUILD_OR_NOT_DECISION": {'description': 'Whether to develop the system at all'},
    "SCOPE_DEFINITION_DECISION": {'description': 'What the system is and is not intended to do, and for whom'},
    "DATA_SOURCING_DECISION": {'description': 'Which data sources to draw on, and on what legal and ethical basis'},
    "DATA_EXCLUSION_DECISION": {'description': 'What to filter out of training data, which necessarily also determines what is filtered in'},
    "ANNOTATION_GUIDELINE_DECISION": {'description': 'How labelling categories are defined and what annotators are instructed to treat as harmful, acceptable, or out of scope'},
    "DATA_WORKER_CONDITIONS_DECISION": {'description': 'Pay, exposure limits, and support for data and moderation workers'},
    "OBJECTIVE_DECISION": {'description': 'What the system is optimised for, including proxy metric selection'},
    "SAFETY_MITIGATION_DECISION": {'description': 'Which mitigations to apply, and which residual risks to accept'},
    "EVALUATION_DESIGN_DECISION": {'description': 'What is measured before release, and therefore what is capable of being detected'},
    "RELEASE_MODALITY_DECISION": {'description': 'Open weights, API access, staged release, or no release, and the reversibility implied by that choice'},
    "ACCESS_CONTROL_DECISION": {'description': 'Who may use the system and under what verification or restriction'},
    "USE_POLICY_DECISION": {'description': 'What uses are permitted, prohibited, and how that is enforced'},
    "DISCLOSURE_DECISION": {'description': 'What is documented and disclosed to users, deployers, regulators, and the public, including known limitations'},
    "MONITORING_DECISION": {'description': 'What is observed post-deployment, and what is left unobserved'},
    "INCIDENT_ESCALATION_DECISION": {'description': 'What triggers escalation, and to whom'},
    "REDRESS_DECISION": {'description': 'Whether and how affected parties can seek remedy'},
    "DEPRECATION_DECISION": {'description': 'Whether and when to withdraw the system'},
    "PROCUREMENT_DECISION": {'description': 'Whether a third party acquires and deploys the system'},
}

class TaxonomyMappingStatusEnum(RichEnum):
    """
    The relationship between a category in one taxonomy and a category in another. Berman et al. (2026) recommend that SOT development "produce explicit mappings to adjacent SOT (e.g., noting a category maps to X in another scheme or stating it has no direct equivalent)", supported by stable semantic identifiers and by the Simple Standard for Sharing Ontological Mappings (SSSOM; Matentzoglu et al. 2022).
    The values below are aligned with SKOS mapping predicates as used by SSSOM, with two additions -- NO_DIRECT_EQUIVALENT and OUT_OF_SCOPE -- that record *negative* mapping results. Recording those is the point: an absent mapping is ambiguous between "not equivalent" and "not yet examined", and only the explicit negative distinguishes them.
    """
    # Enum members
    EXACT_MATCH = "EXACT_MATCH"
    CLOSE_MATCH = "CLOSE_MATCH"
    BROAD_MATCH = "BROAD_MATCH"
    NARROW_MATCH = "NARROW_MATCH"
    RELATED_MATCH = "RELATED_MATCH"
    NO_DIRECT_EQUIVALENT = "NO_DIRECT_EQUIVALENT"
    OUT_OF_SCOPE = "OUT_OF_SCOPE"
    NOT_YET_ASSESSED = "NOT_YET_ASSESSED"

# Set metadata after class creation
TaxonomyMappingStatusEnum._metadata = {
    "EXACT_MATCH": {'description': 'The two categories are interchangeable across the taxonomies', 'aliases': ['skos:exactMatch']},
    "CLOSE_MATCH": {'description': 'The two categories are similar enough to be used interchangeably in some applications but not all', 'aliases': ['skos:closeMatch']},
    "BROAD_MATCH": {'description': "The other taxonomy's category is broader than this one", 'aliases': ['skos:broadMatch']},
    "NARROW_MATCH": {'description': "The other taxonomy's category is narrower than this one", 'aliases': ['skos:narrowMatch']},
    "RELATED_MATCH": {'description': 'The categories are associated but neither equivalent nor hierarchically related; typically they overlap partially', 'aliases': ['skos:relatedMatch']},
    "NO_DIRECT_EQUIVALENT": {'description': 'The mapping was examined and no corresponding category exists in the other taxonomy. A positive assertion of absence, not a missing mapping.'},
    "OUT_OF_SCOPE": {'description': 'The category falls outside the declared scope of the other taxonomy, so its absence there is by design rather than an omission'},
    "NOT_YET_ASSESSED": {'description': 'No mapping has been attempted. Distinguished from NO_DIRECT_EQUIVALENT so that unexamined pairs are not mistaken for examined negatives.'},
}

__all__ = [
    "SociotechnicalOutcomeTypeEnum",
    "RiskEvidenceStatusEnum",
    "HarmBearerLevelEnum",
    "SociotechnicalHarmTypeEnum",
    "AIActorRoleEnum",
    "AILifecycleStageEnum",
    "AIGovernanceDecisionPointEnum",
    "TaxonomyMappingStatusEnum",
]