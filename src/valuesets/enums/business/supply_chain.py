"""
Supply Chain Management and Procurement

Supply chain management classifications including procurement types, vendor management, logistics operations, and supply chain strategies. Based on supply chain management best practices, procurement standards, and logistics frameworks.

Generated from: business/supply_chain.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class ProcurementTypeEnum(RichEnum):
    """
    Types of procurement activities and approaches
    """
    # Enum members
    DIRECT_PROCUREMENT = "DIRECT_PROCUREMENT"
    INDIRECT_PROCUREMENT = "INDIRECT_PROCUREMENT"
    SERVICES_PROCUREMENT = "SERVICES_PROCUREMENT"
    CAPITAL_PROCUREMENT = "CAPITAL_PROCUREMENT"
    STRATEGIC_PROCUREMENT = "STRATEGIC_PROCUREMENT"
    TACTICAL_PROCUREMENT = "TACTICAL_PROCUREMENT"
    EMERGENCY_PROCUREMENT = "EMERGENCY_PROCUREMENT"
    FRAMEWORK_PROCUREMENT = "FRAMEWORK_PROCUREMENT"
    E_PROCUREMENT = "E_PROCUREMENT"
    SUSTAINABLE_PROCUREMENT = "SUSTAINABLE_PROCUREMENT"

# Set metadata after class creation
ProcurementTypeEnum._metadata = {
    "DIRECT_PROCUREMENT": {'description': 'Procurement of materials directly used in production', 'annotations': {'category': 'direct materials', 'purpose': 'production input', 'impact': 'direct impact on product', 'examples': 'raw materials, components, subassemblies', 'strategic': 'strategically important'}},
    "INDIRECT_PROCUREMENT": {'description': 'Procurement of goods and services supporting operations', 'annotations': {'category': 'indirect materials and services', 'purpose': 'operational support', 'impact': 'indirect impact on product', 'examples': 'office supplies, maintenance, professional services', 'cost_focus': 'cost optimization focus'}},
    "SERVICES_PROCUREMENT": {'description': 'Procurement of professional and business services', 'annotations': {'category': 'services', 'intangible': 'intangible deliverables', 'examples': 'consulting, IT services, maintenance', 'relationship': 'relationship-based', 'management': 'service level management'}},
    "CAPITAL_PROCUREMENT": {'description': 'Procurement of capital equipment and assets', 'annotations': {'category': 'capital expenditure', 'long_term': 'long-term assets', 'high_value': 'high value purchases', 'examples': 'machinery, equipment, facilities', 'approval': 'capital approval process'}},
    "STRATEGIC_PROCUREMENT": {'description': 'Procurement of strategically important items', 'annotations': {'importance': 'strategic importance', 'risk': 'high business risk', 'value': 'high value impact', 'partnership': 'strategic partnerships', 'long_term': 'long-term relationships'}},
    "TACTICAL_PROCUREMENT": {'description': 'Routine procurement of standard items', 'annotations': {'routine': 'routine purchases', 'standard': 'standardized items', 'efficiency': 'efficiency focused', 'transactional': 'transactional approach', 'volume': 'volume-based'}},
    "EMERGENCY_PROCUREMENT": {'description': 'Urgent procurement due to immediate needs', 'annotations': {'urgency': 'urgent requirements', 'expedited': 'expedited process', 'higher_cost': 'potentially higher costs', 'risk_mitigation': 'business continuity', 'limited_sourcing': 'limited supplier options'}},
    "FRAMEWORK_PROCUREMENT": {'description': 'Pre-negotiated procurement agreements', 'annotations': {'agreement': 'pre-negotiated terms', 'efficiency': 'procurement efficiency', 'compliance': 'standardized compliance', 'multiple_suppliers': 'multiple approved suppliers', 'call_off': 'call-off contracts'}},
    "E_PROCUREMENT": {'description': 'Technology-enabled procurement processes', 'annotations': {'technology': 'electronic platforms', 'automation': 'process automation', 'efficiency': 'operational efficiency', 'transparency': 'process transparency', 'data': 'procurement data analytics'}},
    "SUSTAINABLE_PROCUREMENT": {'description': 'Environmentally and socially responsible procurement', 'annotations': {'sustainability': 'environmental and social criteria', 'responsibility': 'corporate responsibility', 'lifecycle': 'lifecycle considerations', 'certification': 'sustainability certifications', 'stakeholder': 'stakeholder value'}},
}

class VendorCategoryEnum(RichEnum):
    """
    Vendor classification categories
    """
    # Enum members
    STRATEGIC_SUPPLIER = "STRATEGIC_SUPPLIER"
    PREFERRED_SUPPLIER = "PREFERRED_SUPPLIER"
    APPROVED_SUPPLIER = "APPROVED_SUPPLIER"
    TRANSACTIONAL_SUPPLIER = "TRANSACTIONAL_SUPPLIER"
    SINGLE_SOURCE = "SINGLE_SOURCE"
    SOLE_SOURCE = "SOLE_SOURCE"
    MINORITY_SUPPLIER = "MINORITY_SUPPLIER"
    LOCAL_SUPPLIER = "LOCAL_SUPPLIER"
    GLOBAL_SUPPLIER = "GLOBAL_SUPPLIER"
    SPOT_SUPPLIER = "SPOT_SUPPLIER"

# Set metadata after class creation
VendorCategoryEnum._metadata = {
    "STRATEGIC_SUPPLIER": {'description': 'Critical suppliers with strategic importance', 'annotations': {'importance': 'strategic business importance', 'relationship': 'partnership relationship', 'risk': 'high business risk if disrupted', 'collaboration': 'collaborative planning', 'long_term': 'long-term agreements'}},
    "PREFERRED_SUPPLIER": {'description': 'Suppliers with proven performance and preferred status', 'annotations': {'performance': 'proven performance history', 'preferred': 'preferred supplier status', 'reliability': 'reliable delivery', 'quality': 'consistent quality', 'relationship': 'ongoing relationship'}},
    "APPROVED_SUPPLIER": {'description': 'Suppliers meeting qualification requirements', 'annotations': {'qualification': 'meets qualification criteria', 'approved': 'approved for business', 'standards': 'meets quality standards', 'compliance': 'regulatory compliance', 'monitoring': 'performance monitoring'}},
    "TRANSACTIONAL_SUPPLIER": {'description': 'Suppliers for routine, low-risk purchases', 'annotations': {'routine': 'routine transactions', 'low_risk': 'low business risk', 'standard': 'standard products/services', 'efficiency': 'cost and efficiency focus', 'limited_relationship': 'limited relationship'}},
    "SINGLE_SOURCE": {'description': 'Only available supplier for specific requirement', 'annotations': {'uniqueness': 'unique product or service', 'monopoly': 'single source situation', 'dependency': 'high dependency', 'risk': 'supply risk concentration', 'relationship': 'close relationship management'}},
    "SOLE_SOURCE": {'description': 'Deliberately chosen single supplier', 'annotations': {'choice': 'deliberate single supplier choice', 'partnership': 'strategic partnership', 'specialization': 'specialized capability', 'integration': 'integrated operations', 'exclusive': 'exclusive relationship'}},
    "MINORITY_SUPPLIER": {'description': 'Suppliers meeting diversity criteria', 'annotations': {'diversity': 'supplier diversity program', 'certification': 'diversity certification', 'inclusion': 'supplier inclusion', 'social_responsibility': 'corporate social responsibility', 'development': 'supplier development'}},
    "LOCAL_SUPPLIER": {'description': 'Geographically local suppliers', 'annotations': {'geography': 'local geographic proximity', 'community': 'local community support', 'logistics': 'reduced logistics costs', 'responsiveness': 'quick response capability', 'sustainability': 'reduced carbon footprint'}},
    "GLOBAL_SUPPLIER": {'description': 'Suppliers with global capabilities', 'annotations': {'global': 'global presence and capability', 'scale': 'economies of scale', 'standardization': 'global standardization', 'complexity': 'complex management', 'risk': 'global supply chain risk'}},
    "SPOT_SUPPLIER": {'description': 'Suppliers for one-time or spot purchases', 'annotations': {'spot_market': 'spot market transactions', 'one_time': 'one-time purchases', 'price_driven': 'price-driven selection', 'no_relationship': 'no ongoing relationship', 'market_based': 'market-based pricing'}},
}

class SupplyChainStrategyEnum(RichEnum):
    """
    Supply chain strategic approaches
    """
    # Enum members
    LEAN_SUPPLY_CHAIN = "LEAN_SUPPLY_CHAIN"
    AGILE_SUPPLY_CHAIN = "AGILE_SUPPLY_CHAIN"
    RESILIENT_SUPPLY_CHAIN = "RESILIENT_SUPPLY_CHAIN"
    SUSTAINABLE_SUPPLY_CHAIN = "SUSTAINABLE_SUPPLY_CHAIN"
    GLOBAL_SUPPLY_CHAIN = "GLOBAL_SUPPLY_CHAIN"
    LOCAL_SUPPLY_CHAIN = "LOCAL_SUPPLY_CHAIN"
    DIGITAL_SUPPLY_CHAIN = "DIGITAL_SUPPLY_CHAIN"
    COLLABORATIVE_SUPPLY_CHAIN = "COLLABORATIVE_SUPPLY_CHAIN"
    COST_FOCUSED_SUPPLY_CHAIN = "COST_FOCUSED_SUPPLY_CHAIN"
    CUSTOMER_FOCUSED_SUPPLY_CHAIN = "CUSTOMER_FOCUSED_SUPPLY_CHAIN"

# Set metadata after class creation
SupplyChainStrategyEnum._metadata = {
    "LEAN_SUPPLY_CHAIN": {'description': 'Waste elimination and efficiency-focused supply chain', 'annotations': {'philosophy': 'lean philosophy', 'waste': 'waste elimination', 'efficiency': 'operational efficiency', 'flow': 'smooth material flow', 'inventory': 'minimal inventory'}},
    "AGILE_SUPPLY_CHAIN": {'description': 'Flexible and responsive supply chain', 'annotations': {'flexibility': 'high flexibility', 'responsiveness': 'rapid response capability', 'adaptation': 'quick adaptation', 'variability': 'handles demand variability', 'customer': 'customer responsiveness'}},
    "RESILIENT_SUPPLY_CHAIN": {'description': 'Risk-resistant and robust supply chain', 'annotations': {'resilience': 'supply chain resilience', 'risk_management': 'comprehensive risk management', 'redundancy': 'built-in redundancy', 'recovery': 'quick recovery capability', 'continuity': 'business continuity focus'}},
    "SUSTAINABLE_SUPPLY_CHAIN": {'description': 'Environmentally and socially responsible supply chain', 'annotations': {'sustainability': 'environmental and social sustainability', 'responsibility': 'corporate responsibility', 'lifecycle': 'lifecycle assessment', 'circular': 'circular economy principles', 'stakeholder': 'stakeholder value'}},
    "GLOBAL_SUPPLY_CHAIN": {'description': 'Internationally distributed supply chain', 'annotations': {'global': 'global geographic distribution', 'scale': 'economies of scale', 'complexity': 'increased complexity', 'risk': 'global risks', 'coordination': 'global coordination'}},
    "LOCAL_SUPPLY_CHAIN": {'description': 'Geographically concentrated supply chain', 'annotations': {'local': 'local or regional focus', 'proximity': 'geographic proximity', 'responsiveness': 'local responsiveness', 'community': 'community support', 'sustainability': 'reduced transportation'}},
    "DIGITAL_SUPPLY_CHAIN": {'description': 'Technology-enabled and data-driven supply chain', 'annotations': {'digital': 'digital transformation', 'technology': 'advanced technology', 'data': 'data-driven decisions', 'automation': 'process automation', 'visibility': 'end-to-end visibility'}},
    "COLLABORATIVE_SUPPLY_CHAIN": {'description': 'Partnership-based collaborative supply chain', 'annotations': {'collaboration': 'supply chain collaboration', 'partnership': 'strategic partnerships', 'integration': 'process integration', 'sharing': 'information sharing', 'joint_planning': 'collaborative planning'}},
    "COST_FOCUSED_SUPPLY_CHAIN": {'description': 'Cost optimization-focused supply chain', 'annotations': {'cost': 'cost optimization', 'efficiency': 'cost efficiency', 'standardization': 'process standardization', 'scale': 'economies of scale', 'procurement': 'cost-focused procurement'}},
    "CUSTOMER_FOCUSED_SUPPLY_CHAIN": {'description': 'Customer service-oriented supply chain', 'annotations': {'customer': 'customer-centric', 'service': 'customer service focus', 'customization': 'product customization', 'responsiveness': 'customer responsiveness', 'satisfaction': 'customer satisfaction'}},
}

class LogisticsOperationEnum(RichEnum):
    """
    Types of logistics operations
    """
    # Enum members
    INBOUND_LOGISTICS = "INBOUND_LOGISTICS"
    OUTBOUND_LOGISTICS = "OUTBOUND_LOGISTICS"
    REVERSE_LOGISTICS = "REVERSE_LOGISTICS"
    THIRD_PARTY_LOGISTICS = "THIRD_PARTY_LOGISTICS"
    FOURTH_PARTY_LOGISTICS = "FOURTH_PARTY_LOGISTICS"
    WAREHOUSING = "WAREHOUSING"
    TRANSPORTATION = "TRANSPORTATION"
    CROSS_DOCKING = "CROSS_DOCKING"
    DISTRIBUTION = "DISTRIBUTION"
    FREIGHT_FORWARDING = "FREIGHT_FORWARDING"

# Set metadata after class creation
LogisticsOperationEnum._metadata = {
    "INBOUND_LOGISTICS": {'description': 'Management of incoming materials and supplies', 'annotations': {'direction': 'inbound to organization', 'materials': 'raw materials and supplies', 'suppliers': 'supplier coordination', 'receiving': 'receiving operations', 'quality': 'incoming quality control'}},
    "OUTBOUND_LOGISTICS": {'description': 'Management of finished goods distribution', 'annotations': {'direction': 'outbound from organization', 'products': 'finished goods', 'customers': 'customer delivery', 'distribution': 'distribution management', 'service': 'customer service'}},
    "REVERSE_LOGISTICS": {'description': 'Management of product returns and recycling', 'annotations': {'direction': 'reverse flow', 'returns': 'product returns', 'recycling': 'recycling and disposal', 'recovery': 'value recovery', 'sustainability': 'environmental responsibility'}},
    "THIRD_PARTY_LOGISTICS": {'description': 'Outsourced logistics services', 'annotations': {'outsourcing': 'logistics outsourcing', 'service_provider': 'third-party provider', 'specialization': 'logistics specialization', 'cost': 'cost optimization', 'expertise': 'logistics expertise'}},
    "FOURTH_PARTY_LOGISTICS": {'description': 'Supply chain integration and management services', 'annotations': {'integration': 'supply chain integration', 'management': 'end-to-end management', 'coordination': 'multi-provider coordination', 'strategy': 'strategic logistics', 'technology': 'technology integration'}},
    "WAREHOUSING": {'description': 'Storage and inventory management operations', 'annotations': {'storage': 'product storage', 'inventory': 'inventory management', 'handling': 'material handling', 'distribution': 'distribution center', 'automation': 'warehouse automation'}},
    "TRANSPORTATION": {'description': 'Movement of goods between locations', 'annotations': {'movement': 'goods movement', 'modes': 'transportation modes', 'routing': 'route optimization', 'scheduling': 'delivery scheduling', 'cost': 'transportation cost'}},
    "CROSS_DOCKING": {'description': 'Direct transfer without storage', 'annotations': {'transfer': 'direct transfer', 'minimal_storage': 'minimal inventory storage', 'efficiency': 'operational efficiency', 'speed': 'fast throughput', 'consolidation': 'shipment consolidation'}},
    "DISTRIBUTION": {'description': 'Product distribution and delivery operations', 'annotations': {'distribution': 'product distribution', 'network': 'distribution network', 'delivery': 'customer delivery', 'service': 'delivery service', 'coverage': 'market coverage'}},
    "FREIGHT_FORWARDING": {'description': 'International shipping and customs management', 'annotations': {'international': 'international shipping', 'customs': 'customs clearance', 'documentation': 'shipping documentation', 'coordination': 'multi-modal coordination', 'compliance': 'regulatory compliance'}},
}

class SourcingStrategyEnum(RichEnum):
    """
    Sourcing strategy approaches
    """
    # Enum members
    SINGLE_SOURCING = "SINGLE_SOURCING"
    MULTIPLE_SOURCING = "MULTIPLE_SOURCING"
    DUAL_SOURCING = "DUAL_SOURCING"
    GLOBAL_SOURCING = "GLOBAL_SOURCING"
    DOMESTIC_SOURCING = "DOMESTIC_SOURCING"
    NEAR_SOURCING = "NEAR_SOURCING"
    VERTICAL_INTEGRATION = "VERTICAL_INTEGRATION"
    OUTSOURCING = "OUTSOURCING"
    INSOURCING = "INSOURCING"
    CONSORTIUM_SOURCING = "CONSORTIUM_SOURCING"

# Set metadata after class creation
SourcingStrategyEnum._metadata = {
    "SINGLE_SOURCING": {'description': 'Deliberate use of one supplier for strategic reasons', 'annotations': {'suppliers': 'single supplier', 'strategic': 'strategic decision', 'partnership': 'close partnership', 'risk': 'supply concentration risk', 'benefits': 'economies of scale'}},
    "MULTIPLE_SOURCING": {'description': 'Use of multiple suppliers for risk mitigation', 'annotations': {'suppliers': 'multiple suppliers', 'risk_mitigation': 'supply risk mitigation', 'competition': 'supplier competition', 'flexibility': 'sourcing flexibility', 'management': 'complex supplier management'}},
    "DUAL_SOURCING": {'description': 'Use of two suppliers for balance of risk and efficiency', 'annotations': {'suppliers': 'two suppliers', 'balance': 'risk and efficiency balance', 'backup': 'backup supply capability', 'competition': 'limited competition', 'management': 'manageable complexity'}},
    "GLOBAL_SOURCING": {'description': 'Worldwide sourcing for best value', 'annotations': {'geographic': 'global geographic scope', 'cost': 'cost optimization', 'capability': 'access to capabilities', 'complexity': 'increased complexity', 'risk': 'global supply risks'}},
    "DOMESTIC_SOURCING": {'description': 'Sourcing within domestic market', 'annotations': {'geographic': 'domestic market only', 'proximity': 'geographic proximity', 'responsiveness': 'local responsiveness', 'compliance': 'regulatory compliance', 'support': 'domestic economy support'}},
    "NEAR_SOURCING": {'description': 'Sourcing from nearby geographic regions', 'annotations': {'geographic': 'nearby regions', 'balance': 'cost and proximity balance', 'risk': 'reduced supply chain risk', 'responsiveness': 'improved responsiveness', 'cost': 'moderate cost advantage'}},
    "VERTICAL_INTEGRATION": {'description': 'Internal production instead of external sourcing', 'annotations': {'internal': 'internal production', 'control': 'direct control', 'capability': 'internal capability development', 'investment': 'significant investment', 'flexibility': 'reduced flexibility'}},
    "OUTSOURCING": {'description': 'External sourcing of non-core activities', 'annotations': {'external': 'external providers', 'focus': 'core competency focus', 'cost': 'cost optimization', 'expertise': 'access to expertise', 'dependency': 'external dependency'}},
    "INSOURCING": {'description': 'Bringing previously outsourced activities internal', 'annotations': {'internal': 'bring activities internal', 'control': 'increased control', 'capability': 'internal capability building', 'cost': 'potential cost increase', 'strategic': 'strategic importance'}},
    "CONSORTIUM_SOURCING": {'description': 'Collaborative sourcing with other organizations', 'annotations': {'collaboration': 'multi-organization collaboration', 'leverage': 'increased buying leverage', 'cost': 'cost reduction through scale', 'complexity': 'coordination complexity', 'relationships': 'multi-party relationships'}},
}

class SupplierRelationshipTypeEnum(RichEnum):
    """
    Types of supplier relationship management
    """
    # Enum members
    TRANSACTIONAL = "TRANSACTIONAL"
    PREFERRED_SUPPLIER = "PREFERRED_SUPPLIER"
    STRATEGIC_PARTNERSHIP = "STRATEGIC_PARTNERSHIP"
    ALLIANCE = "ALLIANCE"
    JOINT_VENTURE = "JOINT_VENTURE"
    VENDOR_MANAGED_INVENTORY = "VENDOR_MANAGED_INVENTORY"
    CONSIGNMENT = "CONSIGNMENT"
    COLLABORATIVE_PLANNING = "COLLABORATIVE_PLANNING"
    DEVELOPMENT_PARTNERSHIP = "DEVELOPMENT_PARTNERSHIP"
    RISK_SHARING = "RISK_SHARING"

# Set metadata after class creation
SupplierRelationshipTypeEnum._metadata = {
    "TRANSACTIONAL": {'description': 'Arms-length, price-focused supplier relationship', 'annotations': {'focus': 'price and terms focus', 'interaction': 'minimal interaction', 'duration': 'short-term orientation', 'switching': 'easy supplier switching', 'competition': 'competitive bidding'}},
    "PREFERRED_SUPPLIER": {'description': 'Ongoing relationship with proven suppliers', 'annotations': {'status': 'preferred supplier status', 'performance': 'proven performance', 'priority': 'priority consideration', 'benefits': 'preferential treatment', 'stability': 'stable relationship'}},
    "STRATEGIC_PARTNERSHIP": {'description': 'Collaborative long-term strategic relationship', 'annotations': {'collaboration': 'strategic collaboration', 'integration': 'business integration', 'planning': 'joint planning', 'development': 'joint development', 'mutual_benefit': 'mutual value creation'}},
    "ALLIANCE": {'description': 'Formal alliance with shared objectives', 'annotations': {'formal': 'formal alliance agreement', 'objectives': 'shared strategic objectives', 'resources': 'shared resources', 'risks': 'shared risks and rewards', 'governance': 'joint governance'}},
    "JOINT_VENTURE": {'description': 'Separate entity created with supplier', 'annotations': {'entity': 'separate legal entity', 'ownership': 'shared ownership', 'investment': 'joint investment', 'control': 'shared control', 'separate': 'separate business unit'}},
    "VENDOR_MANAGED_INVENTORY": {'description': 'Supplier manages customer inventory', 'annotations': {'management': 'supplier manages inventory', 'visibility': 'demand visibility', 'responsibility': 'supplier responsibility', 'efficiency': 'inventory efficiency', 'integration': 'systems integration'}},
    "CONSIGNMENT": {'description': 'Supplier owns inventory until consumption', 'annotations': {'ownership': 'supplier retains ownership', 'location': 'customer location', 'payment': 'payment on consumption', 'cash_flow': 'improved customer cash flow', 'risk': 'supplier inventory risk'}},
    "COLLABORATIVE_PLANNING": {'description': 'Joint planning and forecasting relationship', 'annotations': {'planning': 'collaborative planning', 'forecasting': 'joint forecasting', 'information': 'information sharing', 'coordination': 'demand coordination', 'efficiency': 'supply chain efficiency'}},
    "DEVELOPMENT_PARTNERSHIP": {'description': 'Investment in supplier capability development', 'annotations': {'development': 'supplier capability development', 'investment': 'customer investment', 'improvement': 'supplier improvement', 'capability': 'capability building', 'long_term': 'long-term commitment'}},
    "RISK_SHARING": {'description': 'Shared risk and reward relationship', 'annotations': {'risk': 'shared risk and reward', 'incentives': 'aligned incentives', 'performance': 'performance-based', 'outcomes': 'shared outcomes', 'collaboration': 'collaborative approach'}},
}

class InventoryManagementApproachEnum(RichEnum):
    """
    Inventory management methodologies
    """
    # Enum members
    JUST_IN_TIME = "JUST_IN_TIME"
    ECONOMIC_ORDER_QUANTITY = "ECONOMIC_ORDER_QUANTITY"
    ABC_ANALYSIS = "ABC_ANALYSIS"
    SAFETY_STOCK = "SAFETY_STOCK"
    VENDOR_MANAGED_INVENTORY = "VENDOR_MANAGED_INVENTORY"
    CONSIGNMENT_INVENTORY = "CONSIGNMENT_INVENTORY"
    KANBAN = "KANBAN"
    TWO_BIN_SYSTEM = "TWO_BIN_SYSTEM"
    CONTINUOUS_REVIEW = "CONTINUOUS_REVIEW"
    PERIODIC_REVIEW = "PERIODIC_REVIEW"

# Set metadata after class creation
InventoryManagementApproachEnum._metadata = {
    "JUST_IN_TIME": {'description': 'Minimal inventory with precise timing', 'annotations': {'timing': 'precise delivery timing', 'waste': 'inventory waste elimination', 'flow': 'continuous flow', 'supplier': 'supplier integration', 'quality': 'zero defect requirement'}},
    "ECONOMIC_ORDER_QUANTITY": {'description': 'Optimal order quantity calculation', 'annotations': {'optimization': 'cost optimization', 'calculation': 'mathematical calculation', 'trade_off': 'ordering vs holding cost trade-off', 'static': 'static demand assumption', 'classical': 'classical inventory model'}},
    "ABC_ANALYSIS": {'description': 'Inventory classification by value importance', 'annotations': {'classification': 'value-based classification', 'focus': 'priority focus on high-value items', 'management': 'differentiated management', 'efficiency': 'resource allocation efficiency', 'pareto': 'Pareto principle application'}},
    "SAFETY_STOCK": {'description': 'Buffer inventory for demand/supply uncertainty', 'annotations': {'buffer': 'inventory buffer', 'uncertainty': 'demand and supply uncertainty', 'service_level': 'service level protection', 'cost': 'additional holding cost', 'risk': 'stockout risk mitigation'}},
    "VENDOR_MANAGED_INVENTORY": {'description': 'Supplier-controlled inventory management', 'annotations': {'control': 'supplier inventory control', 'visibility': 'demand visibility', 'automation': 'automated replenishment', 'efficiency': 'inventory efficiency', 'partnership': 'supplier partnership'}},
    "CONSIGNMENT_INVENTORY": {'description': 'Supplier-owned inventory at customer location', 'annotations': {'ownership': 'supplier ownership', 'location': 'customer location', 'cash_flow': 'improved cash flow', 'availability': 'immediate availability', 'risk': 'supplier risk'}},
    "KANBAN": {'description': 'Visual pull-based inventory system', 'annotations': {'visual': 'visual control system', 'pull': 'pull-based replenishment', 'lean': 'lean methodology', 'signals': 'kanban signals', 'flow': 'smooth material flow'}},
    "TWO_BIN_SYSTEM": {'description': 'Simple reorder point system using two bins', 'annotations': {'simplicity': 'simple reorder system', 'visual': 'visual reorder point', 'bins': 'two-bin methodology', 'automatic': 'automatic reordering', 'low_cost': 'low-cost implementation'}},
    "CONTINUOUS_REVIEW": {'description': 'Continuous monitoring with fixed reorder point', 'annotations': {'monitoring': 'continuous inventory monitoring', 'reorder_point': 'fixed reorder point', 'quantity': 'fixed order quantity', 'responsiveness': 'responsive to demand', 'cost': 'higher monitoring cost'}},
    "PERIODIC_REVIEW": {'description': 'Periodic inventory review with variable order quantity', 'annotations': {'periodic': 'periodic review intervals', 'variable': 'variable order quantity', 'target': 'target inventory level', 'aggregation': 'order aggregation', 'efficiency': 'administrative efficiency'}},
}

__all__ = [
    "ProcurementTypeEnum",
    "VendorCategoryEnum",
    "SupplyChainStrategyEnum",
    "LogisticsOperationEnum",
    "SourcingStrategyEnum",
    "SupplierRelationshipTypeEnum",
    "InventoryManagementApproachEnum",
]