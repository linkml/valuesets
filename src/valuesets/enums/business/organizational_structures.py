"""
Business Organizational Structures and Legal Entities

Classifications of business organizational structures including legal entity types, corporate hierarchies, management levels, and organizational frameworks. Based on business law standards, corporate governance frameworks, and organizational behavior research.

Generated from: business/organizational_structures.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class LegalEntityTypeEnum(RichEnum):
    """
    Legal entity types for business organizations
    """
    # Enum members
    SOLE_PROPRIETORSHIP = "SOLE_PROPRIETORSHIP"
    GENERAL_PARTNERSHIP = "GENERAL_PARTNERSHIP"
    LIMITED_PARTNERSHIP = "LIMITED_PARTNERSHIP"
    LIMITED_LIABILITY_PARTNERSHIP = "LIMITED_LIABILITY_PARTNERSHIP"
    LIMITED_LIABILITY_COMPANY = "LIMITED_LIABILITY_COMPANY"
    SINGLE_MEMBER_LLC = "SINGLE_MEMBER_LLC"
    MULTI_MEMBER_LLC = "MULTI_MEMBER_LLC"
    C_CORPORATION = "C_CORPORATION"
    S_CORPORATION = "S_CORPORATION"
    B_CORPORATION = "B_CORPORATION"
    PUBLIC_CORPORATION = "PUBLIC_CORPORATION"
    PRIVATE_CORPORATION = "PRIVATE_CORPORATION"
    NONPROFIT_CORPORATION = "NONPROFIT_CORPORATION"
    COOPERATIVE = "COOPERATIVE"
    JOINT_VENTURE = "JOINT_VENTURE"
    HOLDING_COMPANY = "HOLDING_COMPANY"
    SUBSIDIARY = "SUBSIDIARY"
    FRANCHISE = "FRANCHISE"
    GOVERNMENT_ENTITY = "GOVERNMENT_ENTITY"

# Set metadata after class creation
LegalEntityTypeEnum._metadata = {
    "SOLE_PROPRIETORSHIP": {'description': 'Business owned and operated by single individual', 'annotations': {'legal_separation': 'no separation from owner', 'liability': 'unlimited personal liability', 'taxation': 'pass-through to personal returns', 'complexity': 'simplest structure', 'registration': 'minimal requirements'}},
    "GENERAL_PARTNERSHIP": {'description': 'Business owned by two or more partners sharing responsibilities', 'annotations': {'ownership': 'shared among general partners', 'liability': 'unlimited personal liability for all partners', 'taxation': 'pass-through to partners', 'management': 'shared management responsibilities'}},
    "LIMITED_PARTNERSHIP": {'description': 'Partnership with general and limited partners', 'annotations': {'partner_types': 'general partners and limited partners', 'liability': 'general partners have unlimited liability', 'limited_liability': 'limited partners have liability protection', 'management': 'general partners manage operations'}},
    "LIMITED_LIABILITY_PARTNERSHIP": {'description': 'Partnership providing liability protection to all partners', 'annotations': {'liability': 'limited liability for all partners', 'professional_use': 'often used by professional services', 'taxation': 'pass-through taxation', 'management': 'flexible management structure'}},
    "LIMITED_LIABILITY_COMPANY": {'description': 'Hybrid entity combining corporation and partnership features', 'annotations': {'liability': 'limited liability protection', 'taxation': 'flexible tax election options', 'management': 'flexible management structure', 'formality': 'fewer formal requirements than corporations'}},
    "SINGLE_MEMBER_LLC": {'description': 'LLC with only one owner/member', 'annotations': {'ownership': 'single member', 'liability': 'limited liability protection', 'taxation': 'disregarded entity for tax purposes', 'simplicity': 'simpler than multi-member LLC'}},
    "MULTI_MEMBER_LLC": {'description': 'LLC with multiple owners/members', 'annotations': {'ownership': 'multiple members', 'liability': 'limited liability protection', 'taxation': 'partnership taxation by default', 'operating_agreement': 'recommended operating agreement'}},
    "C_CORPORATION": {'description': 'Traditional corporation with double taxation', 'annotations': {'legal_status': 'separate legal entity', 'liability': 'limited liability for shareholders', 'taxation': 'double taxation (corporate and dividend)', 'governance': 'formal board and officer structure', 'stock': 'can issue multiple classes of stock'}},
    "S_CORPORATION": {'description': 'Corporation electing pass-through taxation', 'annotations': {'taxation': 'pass-through to shareholders', 'shareholders': 'limited to 100 shareholders', 'stock_types': 'single class of stock only', 'eligibility': 'restrictions on shareholder types'}},
    "B_CORPORATION": {'description': 'Corporation with social and environmental mission', 'annotations': {'purpose': 'profit and public benefit', 'accountability': 'stakeholder governance requirements', 'transparency': 'annual benefit reporting', 'certification': 'optional third-party certification'}},
    "PUBLIC_CORPORATION": {'description': 'Corporation with publicly traded shares', 'annotations': {'shares': 'publicly traded on stock exchanges', 'regulation': 'SEC reporting requirements', 'governance': 'extensive governance requirements', 'liquidity': 'high share liquidity'}},
    "PRIVATE_CORPORATION": {'description': 'Corporation with privately held shares', 'annotations': {'shares': 'privately held shares', 'shareholders': 'limited number of shareholders', 'regulation': 'fewer regulatory requirements', 'liquidity': 'limited share liquidity'}},
    "NONPROFIT_CORPORATION": {'description': 'Corporation organized for charitable or public purposes', 'annotations': {'purpose': 'charitable, educational, or public benefit', 'taxation': 'tax-exempt status possible', 'profit_distribution': 'no profit distribution to members', 'governance': 'board of directors governance'}},
    "COOPERATIVE": {'description': 'Member-owned and democratically controlled organization', 'annotations': {'ownership': 'member ownership', 'control': 'democratic member control', 'benefits': 'benefits proportional to participation', 'purpose': 'mutual benefit of members'}},
    "JOINT_VENTURE": {'description': 'Temporary partnership for specific project or purpose', 'annotations': {'duration': 'temporary or project-specific', 'purpose': 'specific business objective', 'ownership': 'shared ownership of venture', 'liability': 'depends on structure chosen'}},
    "HOLDING_COMPANY": {'description': 'Company that owns controlling interests in other companies', 'annotations': {'purpose': 'own and control subsidiary companies', 'operations': 'minimal direct operations', 'structure': 'parent-subsidiary relationships', 'control': 'controls subsidiaries through ownership'}},
    "SUBSIDIARY": {'description': 'Company controlled by another company (parent)', 'annotations': {'control': 'controlled by parent company', 'ownership': 'majority owned by parent', 'operations': 'may operate independently', 'liability': 'separate legal entity'}},
    "FRANCHISE": {'description': "Business operating under franchisor's brand and system", 'annotations': {'relationship': 'franchisor-franchisee relationship', 'brand': 'operates under established brand', 'system': "follows franchisor's business system", 'fees': 'pays franchise fees and royalties'}},
    "GOVERNMENT_ENTITY": {'description': 'Entity owned and operated by government', 'annotations': {'ownership': 'government ownership', 'purpose': 'public service or policy implementation', 'regulation': 'government regulations and oversight', 'funding': 'government funding sources'}},
}

class OrganizationalStructureEnum(RichEnum):
    """
    Types of organizational hierarchy and reporting structures
    """
    # Enum members
    HIERARCHICAL = "HIERARCHICAL"
    FLAT = "FLAT"
    MATRIX = "MATRIX"
    FUNCTIONAL = "FUNCTIONAL"
    DIVISIONAL = "DIVISIONAL"
    NETWORK = "NETWORK"
    TEAM_BASED = "TEAM_BASED"
    VIRTUAL = "VIRTUAL"
    HYBRID = "HYBRID"

# Set metadata after class creation
OrganizationalStructureEnum._metadata = {
    "HIERARCHICAL": {'description': 'Traditional pyramid structure with clear chain of command', 'annotations': {'authority_flow': 'top-down authority', 'communication': 'vertical communication channels', 'levels': 'multiple management levels', 'control': 'centralized control', 'decision_making': 'centralized decision making'}},
    "FLAT": {'description': 'Minimal hierarchical levels with broader spans of control', 'annotations': {'levels': 'few hierarchical levels', 'span_of_control': 'broad spans of control', 'communication': 'direct communication', 'decision_making': 'decentralized decision making', 'flexibility': 'high flexibility'}},
    "MATRIX": {'description': 'Dual reporting relationships combining functional and project lines', 'annotations': {'reporting': 'dual reporting relationships', 'authority': 'shared authority between managers', 'flexibility': 'high project flexibility', 'complexity': 'increased complexity', 'communication': 'multidirectional communication'}},
    "FUNCTIONAL": {'description': 'Organization by business functions or departments', 'annotations': {'grouping': 'by business function', 'specialization': 'functional specialization', 'efficiency': 'operational efficiency', 'coordination': 'vertical coordination', 'expertise': 'concentrated expertise'}},
    "DIVISIONAL": {'description': 'Organization by product lines, markets, or geography', 'annotations': {'grouping': 'by products, markets, or geography', 'autonomy': 'divisional autonomy', 'focus': 'market or product focus', 'coordination': 'horizontal coordination', 'responsibility': 'profit center responsibility'}},
    "NETWORK": {'description': 'Flexible structure with interconnected relationships', 'annotations': {'relationships': 'network of relationships', 'flexibility': 'high flexibility', 'boundaries': 'blurred organizational boundaries', 'collaboration': 'extensive collaboration', 'adaptability': 'high adaptability'}},
    "TEAM_BASED": {'description': 'Organization around self-managing teams', 'annotations': {'unit': 'teams as basic organizational unit', 'management': 'self-managing teams', 'collaboration': 'high collaboration', 'decision_making': 'team-based decision making', 'flexibility': 'operational flexibility'}},
    "VIRTUAL": {'description': 'Geographically dispersed organization connected by technology', 'annotations': {'location': 'geographically dispersed', 'technology': 'technology-enabled communication', 'flexibility': 'location flexibility', 'coordination': 'virtual coordination', 'boundaries': 'minimal physical boundaries'}},
    "HYBRID": {'description': 'Combination of multiple organizational structures', 'annotations': {'combination': 'multiple structure types', 'flexibility': 'structural flexibility', 'adaptation': 'adaptable to different needs', 'complexity': 'increased structural complexity', 'customization': 'customized to organization needs'}},
}

class ManagementLevelEnum(RichEnum):
    """
    Hierarchical levels within organizational management structure
    """
    # Enum members
    BOARD_OF_DIRECTORS = "BOARD_OF_DIRECTORS"
    C_SUITE = "C_SUITE"
    SENIOR_EXECUTIVE = "SENIOR_EXECUTIVE"
    VICE_PRESIDENT = "VICE_PRESIDENT"
    DIRECTOR = "DIRECTOR"
    MANAGER = "MANAGER"
    SUPERVISOR = "SUPERVISOR"
    TEAM_LEAD = "TEAM_LEAD"
    SENIOR_INDIVIDUAL_CONTRIBUTOR = "SENIOR_INDIVIDUAL_CONTRIBUTOR"
    INDIVIDUAL_CONTRIBUTOR = "INDIVIDUAL_CONTRIBUTOR"
    ENTRY_LEVEL = "ENTRY_LEVEL"

# Set metadata after class creation
ManagementLevelEnum._metadata = {
    "BOARD_OF_DIRECTORS": {'description': 'Governing body elected by shareholders', 'annotations': {'authority': 'highest governance authority', 'responsibility': 'fiduciary responsibility to shareholders', 'oversight': 'strategic oversight and control', 'composition': 'independent and inside directors'}},
    "C_SUITE": {'description': 'Top executive leadership team', 'annotations': {'level': 'top executive level', 'scope': 'organization-wide responsibility', 'titles': 'CEO, CFO, COO, CTO, etc.', 'accountability': 'accountable to board of directors'}},
    "SENIOR_EXECUTIVE": {'description': 'Senior leadership below C-suite level', 'annotations': {'level': 'senior leadership', 'scope': 'major business unit or function', 'titles': 'EVP, SVP, General Manager', 'reporting': 'reports to C-suite'}},
    "VICE_PRESIDENT": {'description': 'Senior management responsible for major divisions', 'annotations': {'level': 'senior management', 'scope': 'division or major function', 'authority': 'significant decision-making authority', 'titles': 'VP, Assistant VP'}},
    "DIRECTOR": {'description': 'Management responsible for departments or major programs', 'annotations': {'level': 'middle management', 'scope': 'department or program', 'responsibility': 'departmental leadership', 'oversight': 'manages multiple managers'}},
    "MANAGER": {'description': 'Supervisory role managing teams or operations', 'annotations': {'level': 'middle management', 'scope': 'team or operational unit', 'responsibility': 'day-to-day operations', 'supervision': 'manages individual contributors'}},
    "SUPERVISOR": {'description': 'First-line management overseeing frontline employees', 'annotations': {'level': 'first-line management', 'scope': 'small team or shift', 'responsibility': 'direct supervision', 'interface': 'employee-management interface'}},
    "TEAM_LEAD": {'description': 'Lead role within team without formal management authority', 'annotations': {'level': 'senior individual contributor', 'authority': 'informal authority', 'responsibility': 'team coordination', 'expertise': 'technical or project leadership'}},
    "SENIOR_INDIVIDUAL_CONTRIBUTOR": {'description': 'Experienced professional without management responsibilities', 'annotations': {'level': 'senior professional', 'expertise': 'specialized expertise', 'mentoring': 'may mentor junior staff', 'projects': 'leads complex projects'}},
    "INDIVIDUAL_CONTRIBUTOR": {'description': 'Professional or specialist role', 'annotations': {'level': 'professional', 'responsibility': 'individual work output', 'specialization': 'functional specialization', 'career_path': 'professional career track'}},
    "ENTRY_LEVEL": {'description': 'Beginning professional or support roles', 'annotations': {'experience': 'minimal professional experience', 'development': 'learning and development focus', 'supervision': 'close supervision', 'growth_potential': 'career growth opportunities'}},
}

class CorporateGovernanceRoleEnum(RichEnum):
    """
    Roles within corporate governance structure
    """
    # Enum members
    CHAIRMAN_OF_BOARD = "CHAIRMAN_OF_BOARD"
    LEAD_INDEPENDENT_DIRECTOR = "LEAD_INDEPENDENT_DIRECTOR"
    INDEPENDENT_DIRECTOR = "INDEPENDENT_DIRECTOR"
    INSIDE_DIRECTOR = "INSIDE_DIRECTOR"
    AUDIT_COMMITTEE_CHAIR = "AUDIT_COMMITTEE_CHAIR"
    COMPENSATION_COMMITTEE_CHAIR = "COMPENSATION_COMMITTEE_CHAIR"
    NOMINATING_COMMITTEE_CHAIR = "NOMINATING_COMMITTEE_CHAIR"
    CHIEF_EXECUTIVE_OFFICER = "CHIEF_EXECUTIVE_OFFICER"
    CHIEF_FINANCIAL_OFFICER = "CHIEF_FINANCIAL_OFFICER"
    CHIEF_OPERATING_OFFICER = "CHIEF_OPERATING_OFFICER"
    CORPORATE_SECRETARY = "CORPORATE_SECRETARY"

# Set metadata after class creation
CorporateGovernanceRoleEnum._metadata = {
    "CHAIRMAN_OF_BOARD": {'description': 'Leader of board of directors', 'annotations': {'leadership': 'board leadership', 'meetings': 'chairs board meetings', 'interface': 'shareholder interface', 'governance': 'governance oversight'}},
    "LEAD_INDEPENDENT_DIRECTOR": {'description': 'Senior independent director when chairman is not independent', 'annotations': {'independence': 'independent from management', 'leadership': 'leads independent directors', 'oversight': 'additional oversight role', 'communication': 'shareholder communication'}},
    "INDEPENDENT_DIRECTOR": {'description': 'Board member independent from company management', 'annotations': {'independence': 'independent from management', 'objectivity': 'objective oversight', 'committees': 'serves on key committees', 'governance': 'independent governance perspective'}},
    "INSIDE_DIRECTOR": {'description': 'Board member who is also company employee or has material relationship', 'annotations': {'relationship': 'material relationship with company', 'expertise': 'insider knowledge', 'perspective': 'management perspective', 'potential_conflicts': 'potential conflicts of interest'}},
    "AUDIT_COMMITTEE_CHAIR": {'description': "Chair of board's audit committee", 'annotations': {'committee': 'audit committee leadership', 'oversight': 'financial oversight', 'independence': 'must be independent', 'expertise': 'financial expertise required'}},
    "COMPENSATION_COMMITTEE_CHAIR": {'description': "Chair of board's compensation committee", 'annotations': {'committee': 'compensation committee leadership', 'responsibility': 'executive compensation oversight', 'independence': 'must be independent', 'alignment': 'shareholder interest alignment'}},
    "NOMINATING_COMMITTEE_CHAIR": {'description': "Chair of board's nominating and governance committee", 'annotations': {'committee': 'nominating committee leadership', 'responsibility': 'board composition and governance', 'succession': 'leadership succession planning', 'governance': 'governance best practices'}},
    "CHIEF_EXECUTIVE_OFFICER": {'description': 'Highest-ranking executive officer', 'annotations': {'authority': 'highest executive authority', 'strategy': 'strategic leadership', 'accountability': 'accountable to board', 'representation': 'company representation'}},
    "CHIEF_FINANCIAL_OFFICER": {'description': 'Senior executive responsible for financial management', 'annotations': {'responsibility': 'financial management', 'reporting': 'financial reporting oversight', 'compliance': 'financial compliance', 'strategy': 'financial strategy'}},
    "CHIEF_OPERATING_OFFICER": {'description': 'Senior executive responsible for operations', 'annotations': {'responsibility': 'operational management', 'execution': 'strategy execution', 'efficiency': 'operational efficiency', 'coordination': 'cross-functional coordination'}},
    "CORPORATE_SECRETARY": {'description': 'Officer responsible for corporate records and governance compliance', 'annotations': {'records': 'corporate records maintenance', 'compliance': 'governance compliance', 'meetings': 'board meeting coordination', 'legal': 'legal compliance oversight'}},
}

class BusinessOwnershipTypeEnum(RichEnum):
    """
    Types of business ownership structures
    """
    # Enum members
    PRIVATE_OWNERSHIP = "PRIVATE_OWNERSHIP"
    PUBLIC_OWNERSHIP = "PUBLIC_OWNERSHIP"
    FAMILY_OWNERSHIP = "FAMILY_OWNERSHIP"
    EMPLOYEE_OWNERSHIP = "EMPLOYEE_OWNERSHIP"
    INSTITUTIONAL_OWNERSHIP = "INSTITUTIONAL_OWNERSHIP"
    GOVERNMENT_OWNERSHIP = "GOVERNMENT_OWNERSHIP"
    FOREIGN_OWNERSHIP = "FOREIGN_OWNERSHIP"
    JOINT_OWNERSHIP = "JOINT_OWNERSHIP"

# Set metadata after class creation
BusinessOwnershipTypeEnum._metadata = {
    "PRIVATE_OWNERSHIP": {'description': 'Business owned by private individuals or entities', 'annotations': {'ownership': 'private individuals or entities', 'control': 'private control', 'capital': 'private capital sources', 'disclosure': 'limited disclosure requirements'}},
    "PUBLIC_OWNERSHIP": {'description': 'Business with publicly traded ownership shares', 'annotations': {'ownership': 'public shareholders', 'trading': 'publicly traded shares', 'regulation': 'extensive regulatory requirements', 'disclosure': 'public disclosure requirements'}},
    "FAMILY_OWNERSHIP": {'description': 'Business owned and controlled by family members', 'annotations': {'ownership': 'family members', 'succession': 'family succession planning', 'values': 'family values integration', 'long_term': 'long-term orientation'}},
    "EMPLOYEE_OWNERSHIP": {'description': 'Business owned by employees through stock or cooperative structure', 'annotations': {'ownership': 'employee owners', 'participation': 'employee participation', 'alignment': 'ownership-management alignment', 'structure': 'ESOP or cooperative structure'}},
    "INSTITUTIONAL_OWNERSHIP": {'description': 'Business owned by institutional investors', 'annotations': {'ownership': 'institutional investors', 'professional': 'professional management', 'capital': 'institutional capital', 'governance': 'institutional governance'}},
    "GOVERNMENT_OWNERSHIP": {'description': 'Business owned by government entities', 'annotations': {'ownership': 'government entities', 'purpose': 'public policy objectives', 'regulation': 'government oversight', 'funding': 'public funding'}},
    "FOREIGN_OWNERSHIP": {'description': 'Business owned by foreign individuals or entities', 'annotations': {'ownership': 'foreign entities', 'regulation': 'foreign investment regulations', 'capital': 'foreign capital', 'compliance': 'international compliance'}},
    "JOINT_OWNERSHIP": {'description': 'Business owned jointly by multiple parties', 'annotations': {'ownership': 'multiple ownership parties', 'agreements': 'joint ownership agreements', 'governance': 'shared governance', 'coordination': 'ownership coordination'}},
}

class BusinessSizeClassificationEnum(RichEnum):
    """
    Size classifications for business entities
    """
    # Enum members
    MICRO_BUSINESS = "MICRO_BUSINESS"
    SMALL_BUSINESS = "SMALL_BUSINESS"
    MEDIUM_BUSINESS = "MEDIUM_BUSINESS"
    LARGE_BUSINESS = "LARGE_BUSINESS"
    MULTINATIONAL_CORPORATION = "MULTINATIONAL_CORPORATION"
    FORTUNE_500 = "FORTUNE_500"

# Set metadata after class creation
BusinessSizeClassificationEnum._metadata = {
    "MICRO_BUSINESS": {'description': 'Very small business with minimal employees and revenue', 'annotations': {'employees': 'typically 1-9 employees', 'revenue': 'very low revenue', 'characteristics': 'home-based or small office', 'support': 'minimal administrative support'}},
    "SMALL_BUSINESS": {'description': 'Small business as defined by SBA standards', 'annotations': {'employees': 'varies by industry (typically <500)', 'revenue': 'varies by industry', 'sba_definition': 'meets SBA size standards', 'characteristics': 'independently owned and operated'}},
    "MEDIUM_BUSINESS": {'description': 'Mid-sized business between small and large classifications', 'annotations': {'employees': 'typically 500-1500 employees', 'revenue': 'moderate revenue levels', 'characteristics': 'regional or specialized market presence', 'structure': 'more formal organizational structure'}},
    "LARGE_BUSINESS": {'description': 'Major corporation with significant operations', 'annotations': {'employees': '>1500 employees', 'revenue': 'high revenue levels', 'market_presence': 'national or international presence', 'structure': 'complex organizational structure'}},
    "MULTINATIONAL_CORPORATION": {'description': 'Large corporation operating in multiple countries', 'annotations': {'geographic_scope': 'multiple countries', 'complexity': 'high operational complexity', 'structure': 'global organizational structure', 'coordination': 'international coordination'}},
    "FORTUNE_500": {'description': 'Among the 500 largest US corporations by revenue', 'annotations': {'ranking': 'Fortune 500 list', 'revenue': 'highest revenue levels', 'market_position': 'market leadership positions', 'recognition': 'prestigious business recognition'}},
}

class BusinessLifecycleStageEnum(RichEnum):
    """
    Stages in business development lifecycle
    """
    # Enum members
    CONCEPT_STAGE = "CONCEPT_STAGE"
    STARTUP_STAGE = "STARTUP_STAGE"
    GROWTH_STAGE = "GROWTH_STAGE"
    EXPANSION_STAGE = "EXPANSION_STAGE"
    MATURITY_STAGE = "MATURITY_STAGE"
    DECLINE_STAGE = "DECLINE_STAGE"
    TURNAROUND_STAGE = "TURNAROUND_STAGE"
    EXIT_STAGE = "EXIT_STAGE"

# Set metadata after class creation
BusinessLifecycleStageEnum._metadata = {
    "CONCEPT_STAGE": {'description': 'Initial business idea development and validation', 'annotations': {'focus': 'idea development and validation', 'activities': 'market research, business planning', 'funding': 'personal or angel funding', 'risk': 'highest risk level'}},
    "STARTUP_STAGE": {'description': 'Business launch and early operations', 'annotations': {'focus': 'product development and market entry', 'activities': 'building initial customer base', 'funding': 'seed funding, early investments', 'growth': 'rapid learning and adaptation'}},
    "GROWTH_STAGE": {'description': 'Rapid expansion and scaling operations', 'annotations': {'focus': 'scaling operations and market expansion', 'activities': 'increasing market share', 'funding': 'venture capital, growth financing', 'challenges': 'scaling challenges'}},
    "EXPANSION_STAGE": {'description': 'Market expansion and diversification', 'annotations': {'focus': 'market expansion and diversification', 'activities': 'new markets, products, or services', 'funding': 'growth capital, strategic investments', 'sophistication': 'increased operational sophistication'}},
    "MATURITY_STAGE": {'description': 'Stable operations with established market position', 'annotations': {'focus': 'operational efficiency and market defense', 'activities': 'defending market position', 'funding': 'self-funding, debt financing', 'stability': 'stable cash flows'}},
    "DECLINE_STAGE": {'description': 'Decreasing market relevance or performance', 'annotations': {'focus': 'cost reduction and restructuring', 'activities': 'turnaround efforts or exit planning', 'challenges': 'declining revenues or relevance', 'options': 'restructuring, sale, or closure'}},
    "TURNAROUND_STAGE": {'description': 'Recovery efforts from decline or crisis', 'annotations': {'focus': 'crisis management and recovery', 'activities': 'restructuring and repositioning', 'leadership': 'turnaround management', 'urgency': 'urgent transformation needs'}},
    "EXIT_STAGE": {'description': 'Business sale, merger, or closure', 'annotations': {'focus': 'exit strategy execution', 'activities': 'sale, merger, or liquidation', 'valuation': 'business valuation', 'transition': 'ownership transition'}},
}

__all__ = [
    "LegalEntityTypeEnum",
    "OrganizationalStructureEnum",
    "ManagementLevelEnum",
    "CorporateGovernanceRoleEnum",
    "BusinessOwnershipTypeEnum",
    "BusinessSizeClassificationEnum",
    "BusinessLifecycleStageEnum",
]