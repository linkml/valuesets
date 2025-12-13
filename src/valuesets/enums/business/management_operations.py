"""
Business Management and Operations

Business management methodologies, operational frameworks, strategic planning approaches, and performance management systems. Based on management theory, business strategy frameworks, and operational excellence practices.

Generated from: business/management_operations.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class ManagementMethodologyEnum(RichEnum):
    """
    Management approaches and methodologies
    """
    # Enum members
    TRADITIONAL_MANAGEMENT = "TRADITIONAL_MANAGEMENT"
    AGILE_MANAGEMENT = "AGILE_MANAGEMENT"
    LEAN_MANAGEMENT = "LEAN_MANAGEMENT"
    PARTICIPATIVE_MANAGEMENT = "PARTICIPATIVE_MANAGEMENT"
    MATRIX_MANAGEMENT = "MATRIX_MANAGEMENT"
    PROJECT_MANAGEMENT = "PROJECT_MANAGEMENT"
    RESULTS_ORIENTED_MANAGEMENT = "RESULTS_ORIENTED_MANAGEMENT"
    SERVANT_LEADERSHIP = "SERVANT_LEADERSHIP"
    TRANSFORMATIONAL_MANAGEMENT = "TRANSFORMATIONAL_MANAGEMENT"
    DEMOCRATIC_MANAGEMENT = "DEMOCRATIC_MANAGEMENT"

# Set metadata after class creation
ManagementMethodologyEnum._metadata = {
    "TRADITIONAL_MANAGEMENT": {'description': 'Hierarchical command-and-control management approach', 'annotations': {'structure': 'hierarchical structure', 'authority': 'centralized authority', 'communication': 'top-down communication', 'control': 'direct supervision and control'}},
    "AGILE_MANAGEMENT": {'description': 'Flexible, iterative management approach', 'annotations': {'flexibility': 'adaptive and flexible', 'iteration': 'iterative approach', 'collaboration': 'cross-functional collaboration', 'customer_focus': 'customer-centric'}},
    "LEAN_MANAGEMENT": {'description': 'Waste elimination and value optimization approach', 'annotations': {'focus': 'waste elimination', 'value': 'value stream optimization', 'continuous_improvement': 'kaizen and continuous improvement', 'efficiency': 'operational efficiency'}},
    "PARTICIPATIVE_MANAGEMENT": {'description': 'Employee involvement in decision-making', 'annotations': {'involvement': 'employee participation', 'decision_making': 'shared decision-making', 'empowerment': 'employee empowerment', 'engagement': 'increased employee engagement'}},
    "MATRIX_MANAGEMENT": {'description': 'Dual reporting relationships and shared authority', 'annotations': {'structure': 'matrix reporting structure', 'authority': 'shared authority', 'flexibility': 'organizational flexibility', 'complexity': 'increased complexity'}},
    "PROJECT_MANAGEMENT": {'description': 'Structured approach to managing projects', 'annotations': {'methodology': 'project management methodology', 'lifecycle': 'project lifecycle management', 'deliverables': 'deliverable-focused', 'temporary': 'temporary organizational structure'}},
    "RESULTS_ORIENTED_MANAGEMENT": {'description': 'Focus on outcomes and performance results', 'annotations': {'focus': 'results and outcomes', 'measurement': 'performance measurement', 'accountability': 'accountability for results', 'goals': 'goal-oriented approach'}},
    "SERVANT_LEADERSHIP": {'description': 'Leader serves and supports team members', 'annotations': {'philosophy': 'service-oriented leadership', 'support': 'leader supports team', 'development': 'people development focus', 'empowerment': 'team empowerment'}},
    "TRANSFORMATIONAL_MANAGEMENT": {'description': 'Change-oriented and inspirational management', 'annotations': {'change': 'transformation and change focus', 'inspiration': 'inspirational leadership', 'vision': 'vision-driven', 'development': 'follower development'}},
    "DEMOCRATIC_MANAGEMENT": {'description': 'Collaborative and consensus-building approach', 'annotations': {'participation': 'democratic participation', 'consensus': 'consensus-building', 'equality': 'equal voice in decisions', 'transparency': 'transparent processes'}},
}

class StrategicFrameworkEnum(RichEnum):
    """
    Strategic planning and analysis frameworks
    """
    # Enum members
    SWOT_ANALYSIS = "SWOT_ANALYSIS"
    PORTERS_FIVE_FORCES = "PORTERS_FIVE_FORCES"
    BALANCED_SCORECARD = "BALANCED_SCORECARD"
    BLUE_OCEAN_STRATEGY = "BLUE_OCEAN_STRATEGY"
    ANSOFF_MATRIX = "ANSOFF_MATRIX"
    BCG_MATRIX = "BCG_MATRIX"
    VALUE_CHAIN_ANALYSIS = "VALUE_CHAIN_ANALYSIS"
    SCENARIO_PLANNING = "SCENARIO_PLANNING"
    STRATEGIC_CANVAS = "STRATEGIC_CANVAS"
    CORE_COMPETENCY_ANALYSIS = "CORE_COMPETENCY_ANALYSIS"

# Set metadata after class creation
StrategicFrameworkEnum._metadata = {
    "SWOT_ANALYSIS": {'description': 'Strengths, Weaknesses, Opportunities, Threats analysis', 'annotations': {'components': 'strengths, weaknesses, opportunities, threats', 'purpose': 'strategic positioning analysis', 'simplicity': 'simple and widely used', 'application': 'strategic planning and decision-making'}},
    "PORTERS_FIVE_FORCES": {'description': 'Industry competitiveness analysis framework', 'annotations': {'forces': 'competitive rivalry, supplier power, buyer power, substitutes, barriers', 'purpose': 'industry attractiveness analysis', 'competition': 'competitive strategy framework', 'application': 'industry analysis and strategy formulation'}},
    "BALANCED_SCORECARD": {'description': 'Performance measurement from multiple perspectives', 'annotations': {'perspectives': 'financial, customer, internal process, learning', 'purpose': 'strategic performance measurement', 'balance': 'balanced view of performance', 'alignment': 'strategy alignment tool'}},
    "BLUE_OCEAN_STRATEGY": {'description': 'Creating uncontested market space strategy', 'annotations': {'concept': 'value innovation and market creation', 'competition': 'competition avoidance', 'differentiation': 'differentiation and low cost', 'innovation': 'strategic innovation'}},
    "ANSOFF_MATRIX": {'description': 'Product and market growth strategy framework', 'annotations': {'dimensions': 'products and markets', 'strategies': 'market penetration, development, diversification', 'growth': 'growth strategy framework', 'risk': 'risk assessment of growth options'}},
    "BCG_MATRIX": {'description': 'Portfolio analysis of business units', 'annotations': {'dimensions': 'market growth and market share', 'categories': 'stars, cash cows, question marks, dogs', 'portfolio': 'business portfolio analysis', 'resource_allocation': 'resource allocation decisions'}},
    "VALUE_CHAIN_ANALYSIS": {'description': 'Analysis of value-creating activities', 'annotations': {'activities': 'primary and support activities', 'value': 'value creation analysis', 'advantage': 'competitive advantage source identification', 'optimization': 'value chain optimization'}},
    "SCENARIO_PLANNING": {'description': 'Multiple future scenario development and planning', 'annotations': {'scenarios': 'multiple future scenarios', 'uncertainty': 'uncertainty management', 'planning': 'strategic contingency planning', 'flexibility': 'strategic flexibility'}},
    "STRATEGIC_CANVAS": {'description': 'Visual representation of competitive factors', 'annotations': {'visualization': 'visual strategy representation', 'factors': 'competitive factors analysis', 'comparison': 'competitor comparison', 'innovation': 'value innovation identification'}},
    "CORE_COMPETENCY_ANALYSIS": {'description': 'Identification and development of core competencies', 'annotations': {'competencies': 'unique organizational capabilities', 'advantage': 'sustainable competitive advantage', 'focus': 'competency-based strategy', 'development': 'capability development'}},
}

class OperationalModelEnum(RichEnum):
    """
    Business operational models and approaches
    """
    # Enum members
    CENTRALIZED_OPERATIONS = "CENTRALIZED_OPERATIONS"
    DECENTRALIZED_OPERATIONS = "DECENTRALIZED_OPERATIONS"
    HYBRID_OPERATIONS = "HYBRID_OPERATIONS"
    OUTSOURCED_OPERATIONS = "OUTSOURCED_OPERATIONS"
    SHARED_SERVICES = "SHARED_SERVICES"
    NETWORK_OPERATIONS = "NETWORK_OPERATIONS"
    PLATFORM_OPERATIONS = "PLATFORM_OPERATIONS"
    AGILE_OPERATIONS = "AGILE_OPERATIONS"
    LEAN_OPERATIONS = "LEAN_OPERATIONS"
    DIGITAL_OPERATIONS = "DIGITAL_OPERATIONS"

# Set metadata after class creation
OperationalModelEnum._metadata = {
    "CENTRALIZED_OPERATIONS": {'description': 'Centralized operational control and decision-making', 'annotations': {'control': 'centralized control', 'efficiency': 'operational efficiency', 'standardization': 'standardized processes', 'coordination': 'central coordination'}},
    "DECENTRALIZED_OPERATIONS": {'description': 'Distributed operational control and autonomy', 'annotations': {'autonomy': 'local autonomy', 'responsiveness': 'market responsiveness', 'flexibility': 'operational flexibility', 'empowerment': 'local empowerment'}},
    "HYBRID_OPERATIONS": {'description': 'Combination of centralized and decentralized elements', 'annotations': {'combination': 'mixed centralized and decentralized', 'balance': 'balance between control and flexibility', 'optimization': 'situational optimization', 'complexity': 'increased complexity'}},
    "OUTSOURCED_OPERATIONS": {'description': 'External service provider operational model', 'annotations': {'provider': 'external service providers', 'focus': 'core competency focus', 'cost': 'cost optimization', 'expertise': 'specialized expertise'}},
    "SHARED_SERVICES": {'description': 'Centralized services shared across business units', 'annotations': {'sharing': 'shared service delivery', 'efficiency': 'scale efficiency', 'standardization': 'service standardization', 'cost_effectiveness': 'cost-effective service delivery'}},
    "NETWORK_OPERATIONS": {'description': 'Collaborative network of partners and suppliers', 'annotations': {'network': 'partner and supplier network', 'collaboration': 'collaborative operations', 'flexibility': 'network flexibility', 'coordination': 'network coordination'}},
    "PLATFORM_OPERATIONS": {'description': 'Platform-based business operational model', 'annotations': {'platform': 'platform-based operations', 'ecosystem': 'business ecosystem', 'scalability': 'scalable operations', 'network_effects': 'network effects'}},
    "AGILE_OPERATIONS": {'description': 'Flexible and responsive operational approach', 'annotations': {'agility': 'operational agility', 'responsiveness': 'market responsiveness', 'adaptation': 'rapid adaptation', 'iteration': 'iterative improvement'}},
    "LEAN_OPERATIONS": {'description': 'Waste elimination and value-focused operations', 'annotations': {'waste': 'waste elimination', 'value': 'value stream focus', 'efficiency': 'operational efficiency', 'continuous_improvement': 'continuous improvement'}},
    "DIGITAL_OPERATIONS": {'description': 'Technology-enabled and digital-first operations', 'annotations': {'technology': 'digital technology enabled', 'automation': 'process automation', 'data_driven': 'data-driven operations', 'scalability': 'digital scalability'}},
}

class PerformanceMeasurementEnum(RichEnum):
    """
    Performance measurement systems and approaches
    """
    # Enum members
    KEY_PERFORMANCE_INDICATORS = "KEY_PERFORMANCE_INDICATORS"
    OBJECTIVES_KEY_RESULTS = "OBJECTIVES_KEY_RESULTS"
    BALANCED_SCORECARD_MEASUREMENT = "BALANCED_SCORECARD_MEASUREMENT"
    RETURN_ON_INVESTMENT = "RETURN_ON_INVESTMENT"
    ECONOMIC_VALUE_ADDED = "ECONOMIC_VALUE_ADDED"
    CUSTOMER_SATISFACTION_METRICS = "CUSTOMER_SATISFACTION_METRICS"
    EMPLOYEE_ENGAGEMENT_METRICS = "EMPLOYEE_ENGAGEMENT_METRICS"
    OPERATIONAL_EFFICIENCY_METRICS = "OPERATIONAL_EFFICIENCY_METRICS"
    INNOVATION_METRICS = "INNOVATION_METRICS"
    SUSTAINABILITY_METRICS = "SUSTAINABILITY_METRICS"

# Set metadata after class creation
PerformanceMeasurementEnum._metadata = {
    "KEY_PERFORMANCE_INDICATORS": {'description': 'Specific metrics measuring critical performance areas', 'annotations': {'specificity': 'specific performance metrics', 'critical': 'critical success factors', 'measurement': 'quantitative measurement', 'tracking': 'performance tracking'}},
    "OBJECTIVES_KEY_RESULTS": {'description': 'Goal-setting framework with measurable outcomes', 'annotations': {'objectives': 'qualitative objectives', 'results': 'quantitative key results', 'alignment': 'organizational alignment', 'transparency': 'transparent goal setting'}},
    "BALANCED_SCORECARD_MEASUREMENT": {'description': 'Multi-perspective performance measurement system', 'annotations': {'perspectives': 'multiple performance perspectives', 'balance': 'balanced performance view', 'strategy': 'strategy-linked measurement', 'cause_effect': 'cause-and-effect relationships'}},
    "RETURN_ON_INVESTMENT": {'description': 'Financial return measurement relative to investment', 'annotations': {'financial': 'financial performance measure', 'investment': 'investment-based measurement', 'efficiency': 'capital efficiency', 'comparison': 'investment comparison'}},
    "ECONOMIC_VALUE_ADDED": {'description': 'Value creation measurement after cost of capital', 'annotations': {'value': 'economic value creation', 'capital_cost': 'cost of capital consideration', 'shareholder': 'shareholder value focus', 'performance': 'true economic performance'}},
    "CUSTOMER_SATISFACTION_METRICS": {'description': 'Customer experience and satisfaction measurement', 'annotations': {'customer': 'customer-focused measurement', 'satisfaction': 'satisfaction and loyalty', 'experience': 'customer experience', 'retention': 'customer retention'}},
    "EMPLOYEE_ENGAGEMENT_METRICS": {'description': 'Employee satisfaction and engagement measurement', 'annotations': {'engagement': 'employee engagement', 'satisfaction': 'employee satisfaction', 'retention': 'employee retention', 'productivity': 'employee productivity'}},
    "OPERATIONAL_EFFICIENCY_METRICS": {'description': 'Operational performance and efficiency measurement', 'annotations': {'efficiency': 'operational efficiency', 'productivity': 'process productivity', 'quality': 'quality metrics', 'cost': 'cost efficiency'}},
    "INNOVATION_METRICS": {'description': 'Innovation performance and capability measurement', 'annotations': {'innovation': 'innovation performance', 'development': 'new product development', 'improvement': 'process improvement', 'creativity': 'organizational creativity'}},
    "SUSTAINABILITY_METRICS": {'description': 'Environmental and social sustainability measurement', 'annotations': {'sustainability': 'sustainability performance', 'environmental': 'environmental impact', 'social': 'social responsibility', 'governance': 'governance effectiveness'}},
}

class DecisionMakingStyleEnum(RichEnum):
    """
    Decision-making approaches and styles
    """
    # Enum members
    AUTOCRATIC = "AUTOCRATIC"
    DEMOCRATIC = "DEMOCRATIC"
    CONSULTATIVE = "CONSULTATIVE"
    CONSENSUS = "CONSENSUS"
    DELEGATED = "DELEGATED"
    DATA_DRIVEN = "DATA_DRIVEN"
    INTUITIVE = "INTUITIVE"
    COMMITTEE = "COMMITTEE"
    COLLABORATIVE = "COLLABORATIVE"
    CRISIS = "CRISIS"

# Set metadata after class creation
DecisionMakingStyleEnum._metadata = {
    "AUTOCRATIC": {'description': 'Single decision-maker with full authority', 'annotations': {'authority': 'centralized decision authority', 'speed': 'fast decision making', 'control': 'complete control', 'input': 'limited input from others'}},
    "DEMOCRATIC": {'description': 'Group participation in decision-making process', 'annotations': {'participation': 'group participation', 'consensus': 'consensus building', 'input': 'diverse input and perspectives', 'ownership': 'shared ownership of decisions'}},
    "CONSULTATIVE": {'description': 'Leader consults others before deciding', 'annotations': {'consultation': 'stakeholder consultation', 'input': 'seeks input and advice', 'authority': 'leader retains decision authority', 'informed': 'informed decision making'}},
    "CONSENSUS": {'description': 'Agreement reached through group discussion', 'annotations': {'agreement': 'group agreement required', 'discussion': 'extensive group discussion', 'unanimous': 'unanimous or near-unanimous agreement', 'time': 'time-intensive process'}},
    "DELEGATED": {'description': 'Decision authority delegated to others', 'annotations': {'delegation': 'decision authority delegation', 'empowerment': 'employee empowerment', 'autonomy': 'decision autonomy', 'accountability': 'delegated accountability'}},
    "DATA_DRIVEN": {'description': 'Decisions based on data analysis and evidence', 'annotations': {'data': 'data and analytics based', 'evidence': 'evidence-based decisions', 'objectivity': 'objective decision making', 'analysis': 'analytical approach'}},
    "INTUITIVE": {'description': 'Decisions based on experience and gut feeling', 'annotations': {'intuition': 'intuition and experience based', 'speed': 'rapid decision making', 'experience': 'leverages experience', 'creativity': 'creative and innovative'}},
    "COMMITTEE": {'description': 'Formal group decision-making structure', 'annotations': {'structure': 'formal committee structure', 'representation': 'stakeholder representation', 'process': 'structured decision process', 'accountability': 'shared accountability'}},
    "COLLABORATIVE": {'description': 'Joint decision-making with shared responsibility', 'annotations': {'collaboration': 'collaborative approach', 'shared': 'shared responsibility', 'teamwork': 'team-based decisions', 'synergy': 'collective wisdom'}},
    "CRISIS": {'description': 'Rapid decision-making under crisis conditions', 'annotations': {'urgency': 'urgent decision making', 'limited_info': 'limited information available', 'speed': 'rapid response required', 'risk': 'high-risk decision making'}},
}

class LeadershipStyleEnum(RichEnum):
    """
    Leadership approaches and styles
    """
    # Enum members
    TRANSFORMATIONAL = "TRANSFORMATIONAL"
    TRANSACTIONAL = "TRANSACTIONAL"
    SERVANT = "SERVANT"
    AUTHENTIC = "AUTHENTIC"
    CHARISMATIC = "CHARISMATIC"
    SITUATIONAL = "SITUATIONAL"
    DEMOCRATIC = "DEMOCRATIC"
    AUTOCRATIC = "AUTOCRATIC"
    LAISSEZ_FAIRE = "LAISSEZ_FAIRE"
    COACHING = "COACHING"

# Set metadata after class creation
LeadershipStyleEnum._metadata = {
    "TRANSFORMATIONAL": {'description': 'Inspirational leadership that motivates change', 'annotations': {'inspiration': 'inspirational motivation', 'vision': 'visionary leadership', 'development': 'follower development', 'change': 'change-oriented'}},
    "TRANSACTIONAL": {'description': 'Exchange-based leadership with rewards and consequences', 'annotations': {'exchange': 'reward and consequence based', 'structure': 'structured approach', 'performance': 'performance-based', 'management': 'management by exception'}},
    "SERVANT": {'description': 'Leader serves followers and facilitates their growth', 'annotations': {'service': 'service to followers', 'empowerment': 'follower empowerment', 'development': 'personal development focus', 'humility': 'humble leadership approach'}},
    "AUTHENTIC": {'description': 'Genuine and self-aware leadership approach', 'annotations': {'authenticity': 'genuine and authentic', 'self_awareness': 'high self-awareness', 'values': 'values-based leadership', 'integrity': 'personal integrity'}},
    "CHARISMATIC": {'description': 'Inspiring leadership through personal charisma', 'annotations': {'charisma': 'personal charisma', 'inspiration': 'inspirational influence', 'emotion': 'emotional appeal', 'following': 'devoted following'}},
    "SITUATIONAL": {'description': 'Adaptive leadership based on situation requirements', 'annotations': {'adaptation': 'situational adaptation', 'flexibility': 'flexible approach', 'assessment': 'situation assessment', 'style_variation': 'varying leadership styles'}},
    "DEMOCRATIC": {'description': 'Participative leadership with shared decision-making', 'annotations': {'participation': 'follower participation', 'shared': 'shared decision making', 'empowerment': 'team empowerment', 'collaboration': 'collaborative approach'}},
    "AUTOCRATIC": {'description': 'Directive leadership with centralized control', 'annotations': {'control': 'centralized control', 'directive': 'directive approach', 'authority': 'strong authority', 'efficiency': 'decision efficiency'}},
    "LAISSEZ_FAIRE": {'description': 'Hands-off leadership with minimal interference', 'annotations': {'autonomy': 'high follower autonomy', 'minimal': 'minimal leadership intervention', 'freedom': 'freedom to operate', 'self_direction': 'self-directed teams'}},
    "COACHING": {'description': 'Development-focused leadership approach', 'annotations': {'development': 'skill and capability development', 'guidance': 'mentoring and guidance', 'growth': 'personal and professional growth', 'support': 'supportive leadership'}},
}

class BusinessProcessTypeEnum(RichEnum):
    """
    Types of business processes
    """
    # Enum members
    CORE_PROCESS = "CORE_PROCESS"
    SUPPORT_PROCESS = "SUPPORT_PROCESS"
    MANAGEMENT_PROCESS = "MANAGEMENT_PROCESS"
    OPERATIONAL_PROCESS = "OPERATIONAL_PROCESS"
    STRATEGIC_PROCESS = "STRATEGIC_PROCESS"
    INNOVATION_PROCESS = "INNOVATION_PROCESS"
    CUSTOMER_PROCESS = "CUSTOMER_PROCESS"
    FINANCIAL_PROCESS = "FINANCIAL_PROCESS"

# Set metadata after class creation
BusinessProcessTypeEnum._metadata = {
    "CORE_PROCESS": {'description': 'Primary processes that create customer value', 'annotations': {'value': 'direct customer value creation', 'primary': 'primary business activities', 'competitive': 'competitive advantage source', 'strategic': 'strategic importance'}},
    "SUPPORT_PROCESS": {'description': 'Processes that enable core business activities', 'annotations': {'support': 'supports core processes', 'enabling': 'enabling activities', 'infrastructure': 'business infrastructure', 'indirect': 'indirect value contribution'}},
    "MANAGEMENT_PROCESS": {'description': 'Processes for planning, controlling, and improving', 'annotations': {'management': 'management and governance', 'planning': 'planning and control', 'improvement': 'process improvement', 'oversight': 'organizational oversight'}},
    "OPERATIONAL_PROCESS": {'description': 'Day-to-day operational activities', 'annotations': {'operations': 'daily operations', 'routine': 'routine activities', 'execution': 'operational execution', 'efficiency': 'operational efficiency'}},
    "STRATEGIC_PROCESS": {'description': 'Long-term planning and strategic activities', 'annotations': {'strategy': 'strategic planning', 'long_term': 'long-term focus', 'direction': 'organizational direction', 'competitive': 'competitive positioning'}},
    "INNOVATION_PROCESS": {'description': 'Processes for developing new products or services', 'annotations': {'innovation': 'innovation and development', 'creativity': 'creative processes', 'new_development': 'new product/service development', 'competitive': 'competitive innovation'}},
    "CUSTOMER_PROCESS": {'description': 'Processes focused on customer interaction and service', 'annotations': {'customer': 'customer-facing processes', 'service': 'customer service', 'relationship': 'customer relationship', 'satisfaction': 'customer satisfaction'}},
    "FINANCIAL_PROCESS": {'description': 'Processes related to financial management', 'annotations': {'financial': 'financial management', 'accounting': 'accounting and reporting', 'control': 'financial control', 'compliance': 'financial compliance'}},
}

__all__ = [
    "ManagementMethodologyEnum",
    "StrategicFrameworkEnum",
    "OperationalModelEnum",
    "PerformanceMeasurementEnum",
    "DecisionMakingStyleEnum",
    "LeadershipStyleEnum",
    "BusinessProcessTypeEnum",
]