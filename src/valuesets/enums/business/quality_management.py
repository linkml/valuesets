"""
Quality Management Systems and Standards

Quality management frameworks, ISO standards, process improvement methodologies, and quality assurance systems. Based on international quality standards, continuous improvement methodologies, and quality management best practices.

Generated from: business/quality_management.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class QualityStandardEnum(RichEnum):
    """
    Quality management standards and frameworks
    """
    # Enum members
    ISO_9001 = "ISO_9001"
    ISO_14001 = "ISO_14001"
    ISO_45001 = "ISO_45001"
    ISO_27001 = "ISO_27001"
    TQM = "TQM"
    EFQM = "EFQM"
    MALCOLM_BALDRIGE = "MALCOLM_BALDRIGE"
    SIX_SIGMA = "SIX_SIGMA"
    LEAN_QUALITY = "LEAN_QUALITY"
    AS9100 = "AS9100"
    TS16949 = "TS16949"
    ISO_13485 = "ISO_13485"

# Set metadata after class creation
QualityStandardEnum._metadata = {
    "ISO_9001": {'description': 'International standard for quality management systems', 'annotations': {'standard': 'ISO 9001:2015', 'focus': 'quality management systems', 'approach': 'process-based approach', 'certification': 'third-party certification available', 'scope': 'applicable to all organizations'}},
    "ISO_14001": {'description': 'International standard for environmental management systems', 'annotations': {'standard': 'ISO 14001:2015', 'focus': 'environmental management', 'integration': 'integrates with quality management', 'compliance': 'environmental compliance', 'sustainability': 'environmental sustainability'}},
    "ISO_45001": {'description': 'International standard for occupational health and safety', 'annotations': {'standard': 'ISO 45001:2018', 'focus': 'occupational health and safety', 'integration': 'integrates with other management systems', 'prevention': 'injury and illness prevention', 'workplace': 'workplace safety'}},
    "ISO_27001": {'description': 'International standard for information security management', 'annotations': {'standard': 'ISO 27001:2013', 'focus': 'information security', 'risk': 'risk-based approach', 'confidentiality': 'confidentiality, integrity, availability', 'compliance': 'regulatory compliance'}},
    "TQM": {'description': 'Comprehensive quality management philosophy', 'annotations': {'philosophy': 'total quality philosophy', 'scope': 'organization-wide approach', 'customer': 'customer focus', 'improvement': 'continuous improvement', 'involvement': 'total employee involvement'}},
    "EFQM": {'description': 'European excellence model for organizational performance', 'annotations': {'model': 'excellence model', 'assessment': 'self-assessment framework', 'improvement': 'organizational improvement', 'excellence': 'business excellence', 'europe': 'European standard'}},
    "MALCOLM_BALDRIGE": {'description': 'US national quality framework and award', 'annotations': {'framework': 'performance excellence framework', 'award': 'national quality award', 'assessment': 'organizational assessment', 'excellence': 'performance excellence', 'united_states': 'US standard'}},
    "SIX_SIGMA": {'description': 'Data-driven quality improvement methodology', 'annotations': {'methodology': 'statistical quality improvement', 'data_driven': 'data and measurement focused', 'defect_reduction': 'defect and variation reduction', 'belt_system': 'belt certification system', 'tools': 'statistical tools and techniques'}},
    "LEAN_QUALITY": {'description': 'Waste elimination and value-focused quality approach', 'annotations': {'philosophy': 'lean philosophy', 'waste': 'waste elimination', 'value': 'value stream focus', 'efficiency': 'operational efficiency', 'improvement': 'continuous improvement'}},
    "AS9100": {'description': 'Quality standard for aerospace industry', 'annotations': {'industry': 'aerospace and defense', 'based_on': 'based on ISO 9001', 'requirements': 'additional aerospace requirements', 'certification': 'aerospace certification', 'safety': 'safety and reliability focus'}},
    "TS16949": {'description': 'Quality standard for automotive industry', 'annotations': {'industry': 'automotive industry', 'based_on': 'based on ISO 9001', 'requirements': 'automotive-specific requirements', 'supply_chain': 'automotive supply chain', 'defect_prevention': 'defect prevention focus'}},
    "ISO_13485": {'description': 'Quality standard for medical device industry', 'annotations': {'industry': 'medical device industry', 'regulatory': 'regulatory compliance', 'safety': 'patient safety focus', 'design_controls': 'design controls', 'risk_management': 'risk management'}},
}

class QualityMethodologyEnum(RichEnum):
    """
    Quality improvement methodologies and approaches
    """
    # Enum members
    DMAIC = "DMAIC"
    DMADV = "DMADV"
    PDCA = "PDCA"
    KAIZEN = "KAIZEN"
    LEAN_SIX_SIGMA = "LEAN_SIX_SIGMA"
    FIVE_S = "FIVE_S"
    ROOT_CAUSE_ANALYSIS = "ROOT_CAUSE_ANALYSIS"
    STATISTICAL_PROCESS_CONTROL = "STATISTICAL_PROCESS_CONTROL"
    FAILURE_MODE_ANALYSIS = "FAILURE_MODE_ANALYSIS"
    BENCHMARKING = "BENCHMARKING"

# Set metadata after class creation
QualityMethodologyEnum._metadata = {
    "DMAIC": {'description': 'Six Sigma problem-solving methodology', 'annotations': {'phases': 'Define, Measure, Analyze, Improve, Control', 'approach': 'data-driven problem solving', 'structured': 'structured improvement process', 'statistical': 'statistical analysis', 'six_sigma': 'Six Sigma methodology'}},
    "DMADV": {'description': 'Six Sigma design methodology for new processes', 'annotations': {'phases': 'Define, Measure, Analyze, Design, Verify', 'purpose': 'new process or product design', 'design': 'design for Six Sigma', 'verification': 'design verification', 'prevention': 'defect prevention'}},
    "PDCA": {'description': 'Continuous improvement cycle methodology', 'annotations': {'cycle': 'Plan, Do, Check, Act', 'continuous': 'continuous improvement', 'iterative': 'iterative process', 'deming': 'Deming cycle', 'simple': 'simple and versatile'}},
    "KAIZEN": {'description': 'Japanese philosophy of continuous improvement', 'annotations': {'philosophy': 'continuous improvement philosophy', 'incremental': 'small incremental improvements', 'employee': 'employee-driven improvement', 'culture': 'improvement culture', 'daily': 'daily improvement activities'}},
    "LEAN_SIX_SIGMA": {'description': 'Combined methodology integrating Lean and Six Sigma', 'annotations': {'combination': 'Lean and Six Sigma integration', 'waste': 'waste elimination', 'variation': 'variation reduction', 'speed': 'speed and quality', 'comprehensive': 'comprehensive improvement'}},
    "FIVE_S": {'description': 'Workplace organization and standardization methodology', 'annotations': {'components': 'Sort, Set in Order, Shine, Standardize, Sustain', 'workplace': 'workplace organization', 'visual': 'visual management', 'foundation': 'improvement foundation', 'safety': 'safety and efficiency'}},
    "ROOT_CAUSE_ANALYSIS": {'description': 'Systematic approach to identifying problem root causes', 'annotations': {'systematic': 'systematic problem analysis', 'causes': 'root cause identification', 'prevention': 'problem prevention', 'tools': 'various analytical tools', 'thorough': 'thorough investigation'}},
    "STATISTICAL_PROCESS_CONTROL": {'description': 'Statistical methods for process monitoring and control', 'annotations': {'statistical': 'statistical monitoring', 'control_charts': 'control charts', 'variation': 'variation monitoring', 'prevention': 'problem prevention', 'real_time': 'real-time monitoring'}},
    "FAILURE_MODE_ANALYSIS": {'description': 'Systematic analysis of potential failure modes', 'annotations': {'analysis': 'failure mode analysis', 'prevention': 'failure prevention', 'risk': 'risk assessment', 'systematic': 'systematic approach', 'design': 'design and process FMEA'}},
    "BENCHMARKING": {'description': 'Performance comparison with best practices', 'annotations': {'comparison': 'performance comparison', 'best_practices': 'best practice identification', 'improvement': 'improvement opportunities', 'external': 'external benchmarking', 'internal': 'internal benchmarking'}},
}

class QualityControlTechniqueEnum(RichEnum):
    """
    Quality control techniques and tools
    """
    # Enum members
    CONTROL_CHARTS = "CONTROL_CHARTS"
    PARETO_ANALYSIS = "PARETO_ANALYSIS"
    FISHBONE_DIAGRAM = "FISHBONE_DIAGRAM"
    HISTOGRAM = "HISTOGRAM"
    SCATTER_DIAGRAM = "SCATTER_DIAGRAM"
    CHECK_SHEET = "CHECK_SHEET"
    FLOW_CHART = "FLOW_CHART"
    DESIGN_OF_EXPERIMENTS = "DESIGN_OF_EXPERIMENTS"
    SAMPLING_PLANS = "SAMPLING_PLANS"
    GAUGE_R_AND_R = "GAUGE_R_AND_R"

# Set metadata after class creation
QualityControlTechniqueEnum._metadata = {
    "CONTROL_CHARTS": {'description': 'Statistical charts for monitoring process variation', 'annotations': {'statistical': 'statistical process monitoring', 'variation': 'variation tracking', 'limits': 'control limits', 'trends': 'trend identification', 'real_time': 'real-time monitoring'}},
    "PARETO_ANALYSIS": {'description': '80/20 rule analysis for problem prioritization', 'annotations': {'prioritization': 'problem prioritization', 'rule': '80/20 rule', 'focus': 'focus on vital few', 'impact': 'impact analysis', 'resources': 'resource allocation'}},
    "FISHBONE_DIAGRAM": {'description': 'Cause-and-effect analysis diagram', 'annotations': {'cause_effect': 'cause and effect analysis', 'brainstorming': 'structured brainstorming', 'categories': 'cause categories', 'visual': 'visual analysis tool', 'team': 'team analysis tool'}},
    "HISTOGRAM": {'description': 'Frequency distribution chart for data analysis', 'annotations': {'distribution': 'data distribution', 'frequency': 'frequency analysis', 'patterns': 'pattern identification', 'visual': 'visual data representation', 'analysis': 'statistical analysis'}},
    "SCATTER_DIAGRAM": {'description': 'Correlation analysis between two variables', 'annotations': {'correlation': 'correlation analysis', 'relationship': 'variable relationship', 'pattern': 'pattern identification', 'statistical': 'statistical relationship', 'visual': 'visual correlation'}},
    "CHECK_SHEET": {'description': 'Data collection and recording tool', 'annotations': {'collection': 'data collection', 'recording': 'systematic recording', 'tracking': 'problem tracking', 'simple': 'simple data tool', 'standardized': 'standardized format'}},
    "FLOW_CHART": {'description': 'Process flow visualization and analysis', 'annotations': {'process': 'process visualization', 'flow': 'workflow analysis', 'steps': 'process steps', 'improvement': 'process improvement', 'understanding': 'process understanding'}},
    "DESIGN_OF_EXPERIMENTS": {'description': 'Statistical method for process optimization', 'annotations': {'statistical': 'statistical experimentation', 'optimization': 'process optimization', 'factors': 'factor analysis', 'interaction': 'interaction effects', 'efficiency': 'experimental efficiency'}},
    "SAMPLING_PLANS": {'description': 'Systematic approach to quality sampling', 'annotations': {'sampling': 'statistical sampling', 'plans': 'sampling plans', 'acceptance': 'acceptance sampling', 'risk': 'risk control', 'efficiency': 'sampling efficiency'}},
    "GAUGE_R_AND_R": {'description': 'Measurement system analysis technique', 'annotations': {'measurement': 'measurement system analysis', 'repeatability': 'measurement repeatability', 'reproducibility': 'measurement reproducibility', 'variation': 'measurement variation', 'capability': 'measurement capability'}},
}

class QualityAssuranceLevelEnum(RichEnum):
    """
    Levels of quality assurance implementation
    """
    # Enum members
    BASIC_QA = "BASIC_QA"
    INTERMEDIATE_QA = "INTERMEDIATE_QA"
    ADVANCED_QA = "ADVANCED_QA"
    WORLD_CLASS_QA = "WORLD_CLASS_QA"
    TOTAL_QUALITY = "TOTAL_QUALITY"

# Set metadata after class creation
QualityAssuranceLevelEnum._metadata = {
    "BASIC_QA": {'description': 'Fundamental quality assurance practices', 'annotations': {'level': 'basic implementation', 'practices': 'fundamental QA practices', 'inspection': 'inspection-based approach', 'reactive': 'reactive quality approach', 'compliance': 'basic compliance'}},
    "INTERMEDIATE_QA": {'description': 'Systematic quality assurance with documented processes', 'annotations': {'level': 'intermediate implementation', 'systematic': 'systematic approach', 'documentation': 'documented processes', 'prevention': 'some prevention focus', 'training': 'quality training programs'}},
    "ADVANCED_QA": {'description': 'Comprehensive quality management system', 'annotations': {'level': 'advanced implementation', 'comprehensive': 'comprehensive QMS', 'integration': 'integrated approach', 'prevention': 'prevention-focused', 'measurement': 'quality measurement systems'}},
    "WORLD_CLASS_QA": {'description': 'Excellence-oriented quality management', 'annotations': {'level': 'world-class implementation', 'excellence': 'quality excellence', 'innovation': 'quality innovation', 'leadership': 'quality leadership', 'benchmarking': 'best practice benchmarking'}},
    "TOTAL_QUALITY": {'description': 'Organization-wide quality culture and commitment', 'annotations': {'level': 'total quality implementation', 'culture': 'quality culture', 'organization_wide': 'entire organization', 'customer': 'customer-focused', 'continuous': 'continuous improvement'}},
}

class ProcessImprovementApproachEnum(RichEnum):
    """
    Process improvement methodologies and approaches
    """
    # Enum members
    BUSINESS_PROCESS_REENGINEERING = "BUSINESS_PROCESS_REENGINEERING"
    CONTINUOUS_IMPROVEMENT = "CONTINUOUS_IMPROVEMENT"
    PROCESS_STANDARDIZATION = "PROCESS_STANDARDIZATION"
    AUTOMATION = "AUTOMATION"
    DIGITALIZATION = "DIGITALIZATION"
    OUTSOURCING = "OUTSOURCING"
    SHARED_SERVICES = "SHARED_SERVICES"
    AGILE_PROCESS_IMPROVEMENT = "AGILE_PROCESS_IMPROVEMENT"

# Set metadata after class creation
ProcessImprovementApproachEnum._metadata = {
    "BUSINESS_PROCESS_REENGINEERING": {'description': 'Radical redesign of business processes', 'annotations': {'approach': 'radical process redesign', 'dramatic': 'dramatic improvement', 'technology': 'technology-enabled', 'fundamental': 'fundamental rethinking', 'breakthrough': 'breakthrough performance'}},
    "CONTINUOUS_IMPROVEMENT": {'description': 'Ongoing incremental process improvement', 'annotations': {'approach': 'incremental improvement', 'ongoing': 'continuous effort', 'culture': 'improvement culture', 'employee': 'employee involvement', 'sustainable': 'sustainable improvement'}},
    "PROCESS_STANDARDIZATION": {'description': 'Establishing consistent process standards', 'annotations': {'standardization': 'process standardization', 'consistency': 'consistent execution', 'documentation': 'process documentation', 'training': 'standard training', 'compliance': 'standard compliance'}},
    "AUTOMATION": {'description': 'Technology-driven process automation', 'annotations': {'technology': 'automation technology', 'efficiency': 'operational efficiency', 'consistency': 'consistent execution', 'cost': 'cost reduction', 'quality': 'quality improvement'}},
    "DIGITALIZATION": {'description': 'Digital technology-enabled process transformation', 'annotations': {'digital': 'digital transformation', 'technology': 'digital technology', 'data': 'data-driven processes', 'integration': 'system integration', 'innovation': 'digital innovation'}},
    "OUTSOURCING": {'description': 'External provider process management', 'annotations': {'external': 'external process management', 'specialization': 'specialized providers', 'cost': 'cost optimization', 'focus': 'core competency focus', 'expertise': 'external expertise'}},
    "SHARED_SERVICES": {'description': 'Centralized shared process delivery', 'annotations': {'centralization': 'centralized delivery', 'sharing': 'shared across units', 'efficiency': 'scale efficiency', 'standardization': 'service standardization', 'optimization': 'cost optimization'}},
    "AGILE_PROCESS_IMPROVEMENT": {'description': 'Flexible and iterative process improvement', 'annotations': {'agile': 'agile methodology', 'iterative': 'iterative improvement', 'flexible': 'flexible approach', 'responsive': 'responsive to change', 'collaboration': 'collaborative improvement'}},
}

class QualityMaturityLevelEnum(RichEnum):
    """
    Organizational quality maturity levels
    """
    # Enum members
    AD_HOC = "AD_HOC"
    DEFINED = "DEFINED"
    MANAGED = "MANAGED"
    OPTIMIZED = "OPTIMIZED"
    WORLD_CLASS = "WORLD_CLASS"

# Set metadata after class creation
QualityMaturityLevelEnum._metadata = {
    "AD_HOC": {'description': 'Informal and unstructured quality practices', 'annotations': {'maturity': 'initial maturity level', 'structure': 'unstructured approach', 'informal': 'informal practices', 'reactive': 'reactive quality', 'inconsistent': 'inconsistent results'}},
    "DEFINED": {'description': 'Documented and standardized quality processes', 'annotations': {'maturity': 'defined maturity level', 'documentation': 'documented processes', 'standardization': 'standardized approach', 'training': 'process training', 'consistency': 'consistent execution'}},
    "MANAGED": {'description': 'Measured and controlled quality management', 'annotations': {'maturity': 'managed maturity level', 'measurement': 'quality measurement', 'control': 'process control', 'monitoring': 'performance monitoring', 'improvement': 'targeted improvement'}},
    "OPTIMIZED": {'description': 'Continuously improving quality excellence', 'annotations': {'maturity': 'optimized maturity level', 'optimization': 'continuous optimization', 'innovation': 'quality innovation', 'excellence': 'quality excellence', 'benchmarking': 'best practice adoption'}},
    "WORLD_CLASS": {'description': 'Industry-leading quality performance and innovation', 'annotations': {'maturity': 'world-class maturity level', 'leadership': 'industry leadership', 'innovation': 'quality innovation', 'excellence': 'sustained excellence', 'recognition': 'external recognition'}},
}

__all__ = [
    "QualityStandardEnum",
    "QualityMethodologyEnum",
    "QualityControlTechniqueEnum",
    "QualityAssuranceLevelEnum",
    "ProcessImprovementApproachEnum",
    "QualityMaturityLevelEnum",
]