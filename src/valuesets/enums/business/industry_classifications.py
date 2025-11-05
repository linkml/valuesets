"""
Business Industry Classifications and Economic Sectors

Industry classification systems including NAICS codes, economic sectors, and business activity categories. Based on official government classification systems and international standards for economic analysis and business categorization.

Generated from: business/industry_classifications.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class NAICSSectorEnum(RichEnum):
    """
    NAICS two-digit sector codes (North American Industry Classification System)
    """
    # Enum members
    SECTOR_11 = "SECTOR_11"
    SECTOR_21 = "SECTOR_21"
    SECTOR_22 = "SECTOR_22"
    SECTOR_23 = "SECTOR_23"
    SECTOR_31_33 = "SECTOR_31_33"
    SECTOR_42 = "SECTOR_42"
    SECTOR_44_45 = "SECTOR_44_45"
    SECTOR_48_49 = "SECTOR_48_49"
    SECTOR_51 = "SECTOR_51"
    SECTOR_52 = "SECTOR_52"
    SECTOR_53 = "SECTOR_53"
    SECTOR_54 = "SECTOR_54"
    SECTOR_55 = "SECTOR_55"
    SECTOR_56 = "SECTOR_56"
    SECTOR_61 = "SECTOR_61"
    SECTOR_62 = "SECTOR_62"
    SECTOR_71 = "SECTOR_71"
    SECTOR_72 = "SECTOR_72"
    SECTOR_81 = "SECTOR_81"
    SECTOR_92 = "SECTOR_92"

# Set metadata after class creation
NAICSSectorEnum._metadata = {
    "SECTOR_11": {'description': 'Establishments engaged in agriculture, forestry, fishing, and hunting', 'annotations': {'naics_code': '11', 'activities': 'crop production, animal production, forestry, fishing', 'economic_base': 'natural resource extraction and production'}},
    "SECTOR_21": {'description': 'Establishments engaged in extracting natural resources', 'annotations': {'naics_code': '21', 'activities': 'oil and gas extraction, mining, support activities', 'economic_base': 'natural resource extraction'}},
    "SECTOR_22": {'description': 'Establishments engaged in providing utilities', 'annotations': {'naics_code': '22', 'activities': 'electric power, natural gas, water, sewage, waste management', 'regulation': 'heavily regulated'}},
    "SECTOR_23": {'description': 'Establishments engaged in construction activities', 'annotations': {'naics_code': '23', 'activities': 'building construction, heavy construction, specialty trade contractors', 'cyclical': 'highly cyclical industry'}},
    "SECTOR_31_33": {'description': 'Establishments engaged in manufacturing goods', 'annotations': {'naics_code': '31-33', 'activities': 'food, chemicals, machinery, transportation equipment', 'value_added': 'transforms materials into finished goods'}},
    "SECTOR_42": {'description': 'Establishments engaged in wholesale distribution', 'annotations': {'naics_code': '42', 'activities': 'merchant wholesalers, agents and brokers', 'function': 'intermediary between manufacturers and retailers'}},
    "SECTOR_44_45": {'description': 'Establishments engaged in retail sales to consumers', 'annotations': {'naics_code': '44-45', 'activities': 'motor vehicle dealers, food stores, general merchandise', 'customer': 'sells to final consumers'}},
    "SECTOR_48_49": {'description': 'Establishments providing transportation and warehousing services', 'annotations': {'naics_code': '48-49', 'activities': 'air, rail, water, truck transportation, warehousing', 'infrastructure': 'transportation infrastructure dependent'}},
    "SECTOR_51": {'description': 'Establishments in information industries', 'annotations': {'naics_code': '51', 'activities': 'publishing, broadcasting, telecommunications, data processing', 'technology': 'information technology and content'}},
    "SECTOR_52": {'description': 'Establishments providing financial services', 'annotations': {'naics_code': '52', 'activities': 'banking, securities, insurance, funds and trusts', 'regulation': 'highly regulated financial sector'}},
    "SECTOR_53": {'description': 'Establishments engaged in real estate and rental activities', 'annotations': {'naics_code': '53', 'activities': 'real estate, rental and leasing services', 'asset_type': 'real and personal property'}},
    "SECTOR_54": {'description': 'Establishments providing professional services', 'annotations': {'naics_code': '54', 'activities': 'legal, accounting, engineering, consulting, research', 'knowledge_based': 'knowledge and skill intensive'}},
    "SECTOR_55": {'description': 'Establishments serving as holding companies or managing enterprises', 'annotations': {'naics_code': '55', 'activities': 'holding companies, corporate management', 'function': 'corporate ownership and management'}},
    "SECTOR_56": {'description': 'Establishments providing administrative and support services', 'annotations': {'naics_code': '56', 'activities': 'administrative services, waste management, remediation', 'support_function': 'business support services'}},
    "SECTOR_61": {'description': 'Establishments providing educational instruction', 'annotations': {'naics_code': '61', 'activities': 'schools, colleges, training programs', 'public_private': 'public and private education'}},
    "SECTOR_62": {'description': 'Establishments providing health care and social assistance', 'annotations': {'naics_code': '62', 'activities': 'hospitals, medical practices, social assistance', 'essential_services': 'essential public services'}},
    "SECTOR_71": {'description': 'Establishments in arts, entertainment, and recreation', 'annotations': {'naics_code': '71', 'activities': 'performing arts, spectator sports, museums, recreation', 'discretionary': 'discretionary consumer spending'}},
    "SECTOR_72": {'description': 'Establishments providing accommodation and food services', 'annotations': {'naics_code': '72', 'activities': 'hotels, restaurants, food services', 'consumer_services': 'consumer hospitality services'}},
    "SECTOR_81": {'description': 'Establishments providing other services', 'annotations': {'naics_code': '81', 'activities': 'repair, personal care, religious organizations', 'diverse': 'diverse service activities'}},
    "SECTOR_92": {'description': 'Government establishments', 'annotations': {'naics_code': '92', 'activities': 'executive, legislative, judicial, public safety', 'sector': 'government sector'}},
}

class EconomicSectorEnum(RichEnum):
    """
    Broad economic sector classifications
    """
    # Enum members
    PRIMARY_SECTOR = "PRIMARY_SECTOR"
    SECONDARY_SECTOR = "SECONDARY_SECTOR"
    TERTIARY_SECTOR = "TERTIARY_SECTOR"
    QUATERNARY_SECTOR = "QUATERNARY_SECTOR"
    QUINARY_SECTOR = "QUINARY_SECTOR"

# Set metadata after class creation
EconomicSectorEnum._metadata = {
    "PRIMARY_SECTOR": {'description': 'Economic activities extracting natural resources', 'annotations': {'activities': 'agriculture, mining, forestry, fishing', 'output': 'raw materials and natural resources', 'employment': 'typically lower employment share in developed economies', 'development_stage': 'dominant in early economic development'}},
    "SECONDARY_SECTOR": {'description': 'Economic activities manufacturing and processing goods', 'annotations': {'activities': 'manufacturing, construction, utilities', 'output': 'processed and manufactured goods', 'value_added': 'transforms raw materials into finished products', 'employment': 'historically significant in industrial economies'}},
    "TERTIARY_SECTOR": {'description': 'Economic activities providing services', 'annotations': {'activities': 'retail, hospitality, transportation, finance, healthcare', 'output': 'services to consumers and businesses', 'growth': 'largest and fastest growing sector in developed economies', 'employment': 'dominant employment sector'}},
    "QUATERNARY_SECTOR": {'description': 'Knowledge-based economic activities', 'annotations': {'activities': 'research, education, information technology, consulting', 'output': 'knowledge, information, and intellectual services', 'characteristics': 'high skill and education requirements', 'growth': 'rapidly growing in knowledge economies'}},
    "QUINARY_SECTOR": {'description': 'High-level decision-making and policy services', 'annotations': {'activities': 'top-level government, healthcare, education, culture', 'output': 'highest level services and decision-making', 'characteristics': 'elite services and leadership roles', 'scope': 'limited to highest level activities'}},
}

class BusinessActivityTypeEnum(RichEnum):
    """
    Types of primary business activities
    """
    # Enum members
    PRODUCTION = "PRODUCTION"
    DISTRIBUTION = "DISTRIBUTION"
    SERVICES = "SERVICES"
    TECHNOLOGY = "TECHNOLOGY"
    FINANCE = "FINANCE"
    INFORMATION = "INFORMATION"
    EDUCATION = "EDUCATION"
    HEALTHCARE = "HEALTHCARE"
    ENTERTAINMENT = "ENTERTAINMENT"
    PROFESSIONAL_SERVICES = "PROFESSIONAL_SERVICES"

# Set metadata after class creation
BusinessActivityTypeEnum._metadata = {
    "PRODUCTION": {'description': 'Creating or manufacturing physical goods', 'annotations': {'output': 'physical products and goods', 'process': 'transformation of materials', 'assets': 'physical assets and equipment intensive', 'examples': 'factories, farms, mines'}},
    "DISTRIBUTION": {'description': 'Moving goods from producers to consumers', 'annotations': {'function': 'intermediary between producers and consumers', 'value_added': 'place and time utility', 'examples': 'wholesalers, retailers, logistics companies', 'efficiency': 'improves market efficiency'}},
    "SERVICES": {'description': 'Providing intangible services to customers', 'annotations': {'output': 'intangible services', 'characteristics': 'labor intensive, customized', 'examples': 'consulting, healthcare, hospitality', 'customer_interaction': 'high customer interaction'}},
    "TECHNOLOGY": {'description': 'Developing and applying technology solutions', 'annotations': {'focus': 'technology development and application', 'innovation': 'research and development intensive', 'examples': 'software companies, biotech, engineering', 'intellectual_property': 'high intellectual property content'}},
    "FINANCE": {'description': 'Providing financial and investment services', 'annotations': {'function': 'financial intermediation and services', 'regulation': 'highly regulated', 'examples': 'banks, insurance, investment firms', 'capital': 'capital intensive'}},
    "INFORMATION": {'description': 'Creating, processing, and distributing information', 'annotations': {'output': 'information and content', 'channels': 'various distribution channels', 'examples': 'media companies, publishers, data processors', 'technology_dependent': 'technology platform dependent'}},
    "EDUCATION": {'description': 'Providing educational and training services', 'annotations': {'function': 'knowledge and skill development', 'public_private': 'public and private providers', 'examples': 'schools, universities, training companies', 'social_impact': 'high social impact'}},
    "HEALTHCARE": {'description': 'Providing health and medical services', 'annotations': {'function': 'health and medical care', 'regulation': 'highly regulated', 'examples': 'hospitals, clinics, pharmaceutical companies', 'essential': 'essential service'}},
    "ENTERTAINMENT": {'description': 'Providing entertainment and recreational services', 'annotations': {'output': 'entertainment and leisure experiences', 'discretionary': 'discretionary consumer spending', 'examples': 'media, sports, tourism, gaming', 'experience_based': 'experience and emotion based'}},
    "PROFESSIONAL_SERVICES": {'description': 'Providing specialized professional expertise', 'annotations': {'characteristics': 'high skill and knowledge requirements', 'customization': 'highly customized services', 'examples': 'law firms, consulting, accounting', 'expertise': 'specialized professional expertise'}},
}

class IndustryMaturityEnum(RichEnum):
    """
    Industry lifecycle and maturity stages
    """
    # Enum members
    EMERGING = "EMERGING"
    GROWTH = "GROWTH"
    MATURE = "MATURE"
    DECLINING = "DECLINING"
    TRANSFORMING = "TRANSFORMING"

# Set metadata after class creation
IndustryMaturityEnum._metadata = {
    "EMERGING": {'description': 'New industry in early development stage', 'annotations': {'characteristics': 'high uncertainty, rapid change', 'growth': 'high growth potential', 'technology': 'new or evolving technology', 'competition': 'few competitors, unclear standards', 'investment': 'high investment requirements'}},
    "GROWTH": {'description': 'Industry experiencing rapid expansion', 'annotations': {'characteristics': 'rapid market expansion', 'competition': 'increasing competition', 'standardization': 'emerging standards', 'investment': 'significant investment opportunities', 'profitability': 'improving profitability'}},
    "MATURE": {'description': 'Established industry with stable growth', 'annotations': {'characteristics': 'stable market conditions', 'growth': 'slower, steady growth', 'competition': 'established competitive structure', 'efficiency': 'focus on operational efficiency', 'consolidation': 'potential for consolidation'}},
    "DECLINING": {'description': 'Industry experiencing contraction', 'annotations': {'characteristics': 'decreasing demand', 'competition': 'intensifying competition for shrinking market', 'cost_focus': 'focus on cost reduction', 'consolidation': 'significant consolidation', 'exit': 'companies exiting industry'}},
    "TRANSFORMING": {'description': 'Industry undergoing fundamental change', 'annotations': {'characteristics': 'disruptive change and innovation', 'technology': 'technology-driven transformation', 'business_models': 'evolving business models', 'uncertainty': 'high uncertainty about future structure', 'opportunity': 'opportunities for innovation and disruption'}},
}

class MarketStructureEnum(RichEnum):
    """
    Competitive structure of industry markets
    """
    # Enum members
    PERFECT_COMPETITION = "PERFECT_COMPETITION"
    MONOPOLISTIC_COMPETITION = "MONOPOLISTIC_COMPETITION"
    OLIGOPOLY = "OLIGOPOLY"
    MONOPOLY = "MONOPOLY"
    DUOPOLY = "DUOPOLY"

# Set metadata after class creation
MarketStructureEnum._metadata = {
    "PERFECT_COMPETITION": {'description': 'Many small firms with identical products', 'annotations': {'competitors': 'many small competitors', 'products': 'homogeneous products', 'barriers': 'no barriers to entry', 'pricing': 'price takers', 'examples': 'agricultural commodities'}},
    "MONOPOLISTIC_COMPETITION": {'description': 'Many firms with differentiated products', 'annotations': {'competitors': 'many competitors', 'products': 'differentiated products', 'barriers': 'low barriers to entry', 'pricing': 'some pricing power', 'examples': 'restaurants, retail clothing'}},
    "OLIGOPOLY": {'description': 'Few large firms dominating the market', 'annotations': {'competitors': 'few large competitors', 'concentration': 'high market concentration', 'barriers': 'significant barriers to entry', 'interdependence': 'strategic interdependence', 'examples': 'automobiles, telecommunications'}},
    "MONOPOLY": {'description': 'Single firm controlling the market', 'annotations': {'competitors': 'single market leader', 'barriers': 'very high barriers to entry', 'pricing': 'price maker', 'regulation': 'often regulated', 'examples': 'utilities, patented products'}},
    "DUOPOLY": {'description': 'Two firms dominating the market', 'annotations': {'competitors': 'two dominant competitors', 'competition': 'head-to-head competition', 'barriers': 'high barriers to entry', 'strategy': 'strategic competition', 'examples': 'aircraft manufacturing, some software markets'}},
}

class IndustryRegulationLevelEnum(RichEnum):
    """
    Level of government regulation in different industries
    """
    # Enum members
    HIGHLY_REGULATED = "HIGHLY_REGULATED"
    MODERATELY_REGULATED = "MODERATELY_REGULATED"
    LIGHTLY_REGULATED = "LIGHTLY_REGULATED"
    SELF_REGULATED = "SELF_REGULATED"
    DEREGULATED = "DEREGULATED"

# Set metadata after class creation
IndustryRegulationLevelEnum._metadata = {
    "HIGHLY_REGULATED": {'description': 'Industries subject to extensive government oversight', 'annotations': {'oversight': 'extensive government oversight', 'compliance': 'complex compliance requirements', 'barriers': 'regulatory barriers to entry', 'examples': 'banking, healthcare, utilities, pharmaceuticals', 'reason': 'public safety, market power, or systemic risk'}},
    "MODERATELY_REGULATED": {'description': 'Industries with significant but focused regulation', 'annotations': {'oversight': 'focused regulatory oversight', 'compliance': 'specific compliance requirements', 'areas': 'targeted regulatory areas', 'examples': 'food service, transportation, insurance', 'balance': 'balance between oversight and flexibility'}},
    "LIGHTLY_REGULATED": {'description': 'Industries with minimal regulatory oversight', 'annotations': {'oversight': 'minimal regulatory oversight', 'compliance': 'basic compliance requirements', 'flexibility': 'high operational flexibility', 'examples': 'technology, consulting, retail', 'approach': 'market-based approach'}},
    "SELF_REGULATED": {'description': 'Industries primarily regulated by industry organizations', 'annotations': {'oversight': 'industry self-regulation', 'standards': 'industry-developed standards', 'compliance': 'voluntary compliance', 'examples': 'professional services, trade associations', 'effectiveness': 'varies by industry'}},
    "DEREGULATED": {'description': 'Industries formerly regulated but now market-based', 'annotations': {'history': 'formerly regulated industries', 'competition': 'market-based competition', 'transition': 'transition from regulation to competition', 'examples': 'airlines, telecommunications, energy', 'benefits': 'increased competition and efficiency'}},
}

__all__ = [
    "NAICSSectorEnum",
    "EconomicSectorEnum",
    "BusinessActivityTypeEnum",
    "IndustryMaturityEnum",
    "MarketStructureEnum",
    "IndustryRegulationLevelEnum",
]