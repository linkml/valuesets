"""
Human Resources Management and Workforce Classifications

Employment types, HR functions, compensation structures, performance management, and workforce development classifications. Based on labor standards, HR best practices, and organizational development frameworks.

Generated from: business/human_resources.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class EmploymentTypeEnum(RichEnum):
    """
    Types of employment arrangements and contracts
    """
    # Enum members
    FULL_TIME = "FULL_TIME"
    PART_TIME = "PART_TIME"
    CONTRACT = "CONTRACT"
    TEMPORARY = "TEMPORARY"
    FREELANCE = "FREELANCE"
    INTERN = "INTERN"
    SEASONAL = "SEASONAL"
    CONSULTANT = "CONSULTANT"
    VOLUNTEER = "VOLUNTEER"

# Set metadata after class creation
EmploymentTypeEnum._metadata = {
    "FULL_TIME": {'description': 'Regular full-time employment status', 'annotations': {'hours': 'typically 40 hours per week', 'benefits': 'full benefits package', 'classification': 'exempt or non-exempt', 'stability': 'permanent position', 'commitment': 'full organizational commitment'}},
    "PART_TIME": {'description': 'Regular part-time employment status', 'annotations': {'hours': 'less than full-time hours', 'benefits': 'limited or prorated benefits', 'flexibility': 'flexible scheduling', 'classification': 'typically non-exempt', 'commitment': 'ongoing but reduced hours'}},
    "CONTRACT": {'description': 'Fixed-term contractual employment', 'annotations': {'duration': 'defined contract period', 'relationship': 'contractual relationship', 'benefits': 'limited benefits', 'termination': 'defined end date', 'purpose': 'specific project or duration'}},
    "TEMPORARY": {'description': 'Short-term temporary employment', 'annotations': {'duration': 'short-term assignment', 'agency': 'often through staffing agency', 'benefits': 'minimal benefits', 'purpose': 'seasonal or project work', 'flexibility': 'high flexibility'}},
    "FREELANCE": {'description': 'Independent contractor or freelance work', 'annotations': {'relationship': 'independent contractor', 'benefits': 'no traditional benefits', 'control': 'high work autonomy', 'taxes': 'responsible for own taxes', 'projects': 'project-based work'}},
    "INTERN": {'description': 'Student or entry-level internship program', 'annotations': {'purpose': 'learning and experience', 'duration': 'limited duration', 'compensation': 'may be paid or unpaid', 'education': 'educational component', 'supervision': 'mentorship and guidance'}},
    "SEASONAL": {'description': 'Employment tied to seasonal business needs', 'annotations': {'pattern': 'recurring seasonal pattern', 'duration': 'specific seasons', 'industry': 'retail, agriculture, tourism', 'return': 'potential for seasonal return', 'benefits': 'limited benefits'}},
    "CONSULTANT": {'description': 'Professional consulting services', 'annotations': {'expertise': 'specialized expertise', 'relationship': 'advisory relationship', 'independence': 'independent professional', 'project': 'project or retainer basis', 'value': 'strategic value-add'}},
    "VOLUNTEER": {'description': 'Unpaid volunteer service', 'annotations': {'compensation': 'unpaid service', 'motivation': 'altruistic motivation', 'commitment': 'voluntary commitment', 'purpose': 'mission-driven work', 'recognition': 'non-monetary recognition'}},
}

class JobLevelEnum(RichEnum):
    """
    Organizational job levels and career progression
    """
    # Enum members
    ENTRY_LEVEL = "ENTRY_LEVEL"
    JUNIOR = "JUNIOR"
    MID_LEVEL = "MID_LEVEL"
    SENIOR = "SENIOR"
    LEAD = "LEAD"
    MANAGER = "MANAGER"
    DIRECTOR = "DIRECTOR"
    VP = "VP"
    C_LEVEL = "C_LEVEL"

# Set metadata after class creation
JobLevelEnum._metadata = {
    "ENTRY_LEVEL": {'description': 'Beginning career level positions', 'annotations': {'experience': '0-2 years experience', 'responsibilities': 'basic operational tasks', 'supervision': 'high supervision required', 'development': 'learning and development focus', 'career_stage': 'career beginning'}},
    "JUNIOR": {'description': 'Junior professional level', 'annotations': {'experience': '2-4 years experience', 'responsibilities': 'routine professional tasks', 'independence': 'some independence', 'mentorship': 'receiving mentorship', 'skill_building': 'skill development phase'}},
    "MID_LEVEL": {'description': 'Experienced professional level', 'annotations': {'experience': '4-8 years experience', 'responsibilities': 'complex project work', 'independence': 'high independence', 'mentorship': 'providing and receiving mentorship', 'expertise': 'developing expertise'}},
    "SENIOR": {'description': 'Senior professional level', 'annotations': {'experience': '8+ years experience', 'responsibilities': 'strategic project leadership', 'expertise': 'subject matter expertise', 'mentorship': 'mentoring others', 'influence': 'organizational influence'}},
    "LEAD": {'description': 'Team leadership role', 'annotations': {'responsibility': 'team leadership', 'people_management': 'direct reports', 'coordination': 'team coordination', 'accountability': 'team results', 'development': 'team development'}},
    "MANAGER": {'description': 'Management level position', 'annotations': {'scope': 'departmental management', 'people_management': 'multiple direct reports', 'budget': 'budget responsibility', 'strategy': 'tactical strategy', 'operations': 'operational management'}},
    "DIRECTOR": {'description': 'Director level executive', 'annotations': {'scope': 'multi-departmental oversight', 'strategy': 'strategic planning', 'leadership': 'organizational leadership', 'stakeholders': 'senior stakeholder management', 'results': 'business results accountability'}},
    "VP": {'description': 'Vice President executive level', 'annotations': {'scope': 'business unit or functional area', 'strategy': 'strategic leadership', 'board': 'board interaction', 'organization': 'organizational impact', 'succession': 'succession planning'}},
    "C_LEVEL": {'description': 'Chief executive level', 'annotations': {'scope': 'enterprise-wide responsibility', 'governance': 'corporate governance', 'vision': 'organizational vision', 'stakeholders': 'external stakeholder management', 'fiduciary': 'fiduciary responsibility'}},
}

class HRFunctionEnum(RichEnum):
    """
    Human resources functional areas and specializations
    """
    # Enum members
    TALENT_ACQUISITION = "TALENT_ACQUISITION"
    EMPLOYEE_RELATIONS = "EMPLOYEE_RELATIONS"
    COMPENSATION_BENEFITS = "COMPENSATION_BENEFITS"
    PERFORMANCE_MANAGEMENT = "PERFORMANCE_MANAGEMENT"
    LEARNING_DEVELOPMENT = "LEARNING_DEVELOPMENT"
    HR_ANALYTICS = "HR_ANALYTICS"
    ORGANIZATIONAL_DEVELOPMENT = "ORGANIZATIONAL_DEVELOPMENT"
    HR_COMPLIANCE = "HR_COMPLIANCE"
    HRIS_TECHNOLOGY = "HRIS_TECHNOLOGY"

# Set metadata after class creation
HRFunctionEnum._metadata = {
    "TALENT_ACQUISITION": {'description': 'Recruitment and hiring functions', 'annotations': {'activities': 'sourcing, screening, interviewing, hiring', 'focus': 'attracting and selecting talent', 'metrics': 'time to hire, quality of hire', 'strategy': 'workforce planning', 'technology': 'ATS and recruitment tools'}},
    "EMPLOYEE_RELATIONS": {'description': 'Managing employee relationships and workplace issues', 'annotations': {'activities': 'conflict resolution, grievance handling', 'focus': 'positive employee relations', 'communication': 'employee communication', 'culture': 'workplace culture', 'mediation': 'dispute resolution'}},
    "COMPENSATION_BENEFITS": {'description': 'Managing compensation and benefits programs', 'annotations': {'activities': 'salary administration, benefits design', 'analysis': 'market analysis and benchmarking', 'compliance': 'regulatory compliance', 'cost': 'cost management', 'competitiveness': 'market competitiveness'}},
    "PERFORMANCE_MANAGEMENT": {'description': 'Employee performance evaluation and improvement', 'annotations': {'activities': 'performance reviews, goal setting', 'development': 'performance improvement', 'measurement': 'performance metrics', 'feedback': 'continuous feedback', 'coaching': 'performance coaching'}},
    "LEARNING_DEVELOPMENT": {'description': 'Employee training and development programs', 'annotations': {'activities': 'training design, skill development', 'career': 'career development', 'leadership': 'leadership development', 'compliance': 'compliance training', 'technology': 'learning management systems'}},
    "HR_ANALYTICS": {'description': 'HR data analysis and workforce metrics', 'annotations': {'activities': 'data analysis, metrics reporting', 'insights': 'workforce insights', 'predictive': 'predictive analytics', 'dashboard': 'HR dashboards', 'decision_support': 'data-driven decisions'}},
    "ORGANIZATIONAL_DEVELOPMENT": {'description': 'Organizational design and change management', 'annotations': {'activities': 'change management, culture transformation', 'design': 'organizational design', 'effectiveness': 'organizational effectiveness', 'culture': 'culture development', 'transformation': 'business transformation'}},
    "HR_COMPLIANCE": {'description': 'Employment law compliance and risk management', 'annotations': {'activities': 'policy development, compliance monitoring', 'legal': 'employment law compliance', 'risk': 'HR risk management', 'auditing': 'compliance auditing', 'documentation': 'record keeping'}},
    "HRIS_TECHNOLOGY": {'description': 'HR information systems and technology', 'annotations': {'activities': 'system administration, data management', 'systems': 'HRIS implementation', 'automation': 'process automation', 'integration': 'system integration', 'security': 'data security'}},
}

class CompensationTypeEnum(RichEnum):
    """
    Types of employee compensation structures
    """
    # Enum members
    BASE_SALARY = "BASE_SALARY"
    HOURLY_WAGE = "HOURLY_WAGE"
    COMMISSION = "COMMISSION"
    BONUS = "BONUS"
    STOCK_OPTIONS = "STOCK_OPTIONS"
    PROFIT_SHARING = "PROFIT_SHARING"
    PIECE_RATE = "PIECE_RATE"
    STIPEND = "STIPEND"

# Set metadata after class creation
CompensationTypeEnum._metadata = {
    "BASE_SALARY": {'description': 'Fixed annual salary compensation', 'annotations': {'structure': 'fixed annual amount', 'payment': 'regular pay periods', 'exemption': 'often exempt from overtime', 'predictability': 'predictable income', 'market': 'market benchmarked'}},
    "HOURLY_WAGE": {'description': 'Compensation paid per hour worked', 'annotations': {'structure': 'rate per hour', 'overtime': 'overtime eligible', 'tracking': 'time tracking required', 'variability': 'variable based on hours', 'classification': 'non-exempt employees'}},
    "COMMISSION": {'description': 'Performance-based sales commission', 'annotations': {'structure': 'percentage of sales', 'performance': 'performance-based', 'variability': 'highly variable', 'motivation': 'sales motivation', 'risk': 'income risk'}},
    "BONUS": {'description': 'Additional compensation for performance', 'annotations': {'timing': 'annual or periodic', 'criteria': 'performance criteria', 'discretionary': 'may be discretionary', 'recognition': 'performance recognition', 'retention': 'retention tool'}},
    "STOCK_OPTIONS": {'description': 'Equity compensation through stock options', 'annotations': {'equity': 'equity participation', 'vesting': 'vesting schedule', 'retention': 'long-term retention', 'upside': 'company growth upside', 'risk': 'market risk'}},
    "PROFIT_SHARING": {'description': 'Sharing of company profits with employees', 'annotations': {'structure': 'percentage of profits', 'performance': 'company performance based', 'culture': 'ownership culture', 'variability': 'variable based on profits', 'alignment': 'interest alignment'}},
    "PIECE_RATE": {'description': 'Compensation based on units produced', 'annotations': {'structure': 'rate per unit produced', 'productivity': 'productivity-based', 'manufacturing': 'common in manufacturing', 'measurement': 'output measurement', 'efficiency': 'efficiency incentive'}},
    "STIPEND": {'description': 'Fixed regular allowance or payment', 'annotations': {'purpose': 'specific purpose payment', 'amount': 'modest fixed amount', 'regularity': 'regular payment', 'supplemental': 'supplemental income', 'categories': 'interns, volunteers, board members'}},
}

class PerformanceRatingEnum(RichEnum):
    """
    Employee performance evaluation ratings
    """
    # Enum members
    EXCEEDS_EXPECTATIONS = "EXCEEDS_EXPECTATIONS"
    MEETS_EXPECTATIONS = "MEETS_EXPECTATIONS"
    PARTIALLY_MEETS = "PARTIALLY_MEETS"
    DOES_NOT_MEET = "DOES_NOT_MEET"
    OUTSTANDING = "OUTSTANDING"

# Set metadata after class creation
PerformanceRatingEnum._metadata = {
    "EXCEEDS_EXPECTATIONS": {'description': 'Performance significantly above expected standards', 'annotations': {'level': 'top performance tier', 'impact': 'significant business impact', 'recognition': 'high recognition', 'development': 'stretch assignments', 'percentage': 'typically 10-20% of population'}},
    "MEETS_EXPECTATIONS": {'description': 'Performance meets all expected standards', 'annotations': {'level': 'satisfactory performance', 'standards': 'meets all job requirements', 'competency': 'demonstrates required competencies', 'consistency': 'consistent performance', 'percentage': 'typically 60-70% of population'}},
    "PARTIALLY_MEETS": {'description': 'Performance meets some but not all standards', 'annotations': {'level': 'below standard performance', 'improvement': 'improvement needed', 'support': 'additional support required', 'development': 'focused development plan', 'percentage': 'typically 10-15% of population'}},
    "DOES_NOT_MEET": {'description': 'Performance below acceptable standards', 'annotations': {'level': 'unsatisfactory performance', 'action': 'performance improvement plan', 'timeline': 'improvement timeline', 'consequences': 'potential consequences', 'percentage': 'typically 5-10% of population'}},
    "OUTSTANDING": {'description': 'Exceptional performance far exceeding standards', 'annotations': {'level': 'exceptional performance', 'impact': 'transformational impact', 'leadership': 'demonstrates leadership', 'innovation': 'innovation and excellence', 'rarity': 'rare rating'}},
}

class RecruitmentSourceEnum(RichEnum):
    """
    Sources for candidate recruitment and sourcing
    """
    # Enum members
    INTERNAL_REFERRAL = "INTERNAL_REFERRAL"
    JOB_BOARDS = "JOB_BOARDS"
    COMPANY_WEBSITE = "COMPANY_WEBSITE"
    SOCIAL_MEDIA = "SOCIAL_MEDIA"
    RECRUITMENT_AGENCIES = "RECRUITMENT_AGENCIES"
    CAMPUS_RECRUITING = "CAMPUS_RECRUITING"
    PROFESSIONAL_NETWORKS = "PROFESSIONAL_NETWORKS"
    HEADHUNTERS = "HEADHUNTERS"

# Set metadata after class creation
RecruitmentSourceEnum._metadata = {
    "INTERNAL_REFERRAL": {'description': 'Candidates referred by current employees', 'annotations': {'source': 'employee networks', 'quality': 'typically high quality', 'cost': 'low cost per hire', 'cultural_fit': 'good cultural fit', 'retention': 'higher retention rates'}},
    "JOB_BOARDS": {'description': 'Candidates from online job posting sites', 'annotations': {'reach': 'broad candidate reach', 'cost': 'moderate cost', 'volume': 'high application volume', 'screening': 'requires screening', 'examples': 'Indeed, LinkedIn, Monster'}},
    "COMPANY_WEBSITE": {'description': 'Candidates applying through company website', 'annotations': {'interest': 'high company interest', 'brand': 'employer brand driven', 'quality': 'targeted candidates', 'direct': 'direct application', 'cost': 'low incremental cost'}},
    "SOCIAL_MEDIA": {'description': 'Candidates sourced through social media platforms', 'annotations': {'platforms': 'LinkedIn, Facebook, Twitter', 'active': 'active sourcing', 'networking': 'professional networking', 'targeting': 'targeted approach', 'engagement': 'relationship building'}},
    "RECRUITMENT_AGENCIES": {'description': 'Candidates sourced through recruitment firms', 'annotations': {'expertise': 'specialized expertise', 'cost': 'higher cost', 'speed': 'faster time to hire', 'screening': 'pre-screened candidates', 'specialization': 'industry specialization'}},
    "CAMPUS_RECRUITING": {'description': 'Recruitment from educational institutions', 'annotations': {'target': 'students and new graduates', 'programs': 'internship and graduate programs', 'relationships': 'university relationships', 'pipeline': 'talent pipeline', 'early_career': 'early career focus'}},
    "PROFESSIONAL_NETWORKS": {'description': 'Recruitment through professional associations', 'annotations': {'industry': 'industry-specific networks', 'expertise': 'specialized expertise', 'relationships': 'professional relationships', 'credibility': 'professional credibility', 'targeted': 'targeted recruitment'}},
    "HEADHUNTERS": {'description': 'Executive-level recruitment specialists', 'annotations': {'level': 'senior and executive roles', 'expertise': 'specialized search expertise', 'network': 'extensive professional networks', 'confidential': 'confidential searches', 'cost': 'premium cost'}},
}

class TrainingTypeEnum(RichEnum):
    """
    Types of employee training and development programs
    """
    # Enum members
    ONBOARDING = "ONBOARDING"
    TECHNICAL_SKILLS = "TECHNICAL_SKILLS"
    LEADERSHIP_DEVELOPMENT = "LEADERSHIP_DEVELOPMENT"
    COMPLIANCE_TRAINING = "COMPLIANCE_TRAINING"
    SOFT_SKILLS = "SOFT_SKILLS"
    SAFETY_TRAINING = "SAFETY_TRAINING"
    DIVERSITY_INCLUSION = "DIVERSITY_INCLUSION"
    CROSS_TRAINING = "CROSS_TRAINING"

# Set metadata after class creation
TrainingTypeEnum._metadata = {
    "ONBOARDING": {'description': 'Orientation and integration training for new hires', 'annotations': {'timing': 'first days/weeks of employment', 'purpose': 'integration and orientation', 'content': 'company culture, policies, role basics', 'delivery': 'structured program', 'outcome': 'successful integration'}},
    "TECHNICAL_SKILLS": {'description': 'Job-specific technical competency development', 'annotations': {'focus': 'technical competencies', 'relevance': 'job-specific skills', 'methods': 'hands-on training', 'certification': 'may include certification', 'updating': 'continuous skill updates'}},
    "LEADERSHIP_DEVELOPMENT": {'description': 'Management and leadership capability building', 'annotations': {'target': 'managers and high-potential employees', 'skills': 'leadership and management skills', 'development': 'long-term development', 'mentorship': 'coaching and mentorship', 'succession': 'succession planning'}},
    "COMPLIANCE_TRAINING": {'description': 'Required training for regulatory compliance', 'annotations': {'requirement': 'mandatory training', 'regulation': 'regulatory compliance', 'documentation': 'completion tracking', 'frequency': 'periodic updates', 'risk': 'risk mitigation'}},
    "SOFT_SKILLS": {'description': 'Communication and interpersonal skills training', 'annotations': {'skills': 'communication, teamwork, problem-solving', 'application': 'broadly applicable', 'development': 'personal development', 'effectiveness': 'workplace effectiveness', 'collaboration': 'collaboration skills'}},
    "SAFETY_TRAINING": {'description': 'Workplace safety and health training', 'annotations': {'focus': 'safety procedures and practices', 'compliance': 'OSHA compliance', 'prevention': 'accident prevention', 'emergency': 'emergency procedures', 'culture': 'safety culture'}},
    "DIVERSITY_INCLUSION": {'description': 'Training on diversity, equity, and inclusion', 'annotations': {'awareness': 'cultural awareness', 'bias': 'unconscious bias training', 'inclusion': 'inclusive practices', 'culture': 'inclusive culture', 'behavior': 'behavior change'}},
    "CROSS_TRAINING": {'description': 'Training in multiple roles or departments', 'annotations': {'flexibility': 'workforce flexibility', 'coverage': 'backup coverage', 'development': 'career development', 'understanding': 'broader understanding', 'collaboration': 'improved collaboration'}},
}

class EmployeeStatusEnum(RichEnum):
    """
    Current employment status classifications
    """
    # Enum members
    ACTIVE = "ACTIVE"
    ON_LEAVE = "ON_LEAVE"
    PROBATIONARY = "PROBATIONARY"
    SUSPENDED = "SUSPENDED"
    TERMINATED = "TERMINATED"
    RETIRED = "RETIRED"

# Set metadata after class creation
EmployeeStatusEnum._metadata = {
    "ACTIVE": {'description': 'Currently employed and working', 'annotations': {'status': 'actively working', 'benefits': 'receiving full benefits', 'responsibilities': 'fulfilling job responsibilities', 'engagement': 'expected engagement', 'performance': 'subject to performance management'}},
    "ON_LEAVE": {'description': 'Temporarily away from work on approved leave', 'annotations': {'temporary': 'temporary absence', 'approval': 'approved leave', 'return': 'expected return date', 'benefits': 'may retain benefits', 'types': 'medical, family, personal leave'}},
    "PROBATIONARY": {'description': 'New employee in probationary period', 'annotations': {'duration': 'defined probationary period', 'evaluation': 'ongoing evaluation', 'benefits': 'limited or delayed benefits', 'termination': 'easier termination', 'assessment': 'performance assessment'}},
    "SUSPENDED": {'description': 'Temporarily suspended from work', 'annotations': {'disciplinary': 'disciplinary action', 'investigation': 'pending investigation', 'pay': 'with or without pay', 'temporary': 'temporary status', 'review': 'pending review'}},
    "TERMINATED": {'description': 'Employment has been terminated', 'annotations': {'end': 'employment ended', 'voluntary': 'voluntary or involuntary', 'benefits': 'benefits cessation', 'final': 'final status', 'documentation': 'termination documentation'}},
    "RETIRED": {'description': 'Retired from employment', 'annotations': {'voluntary': 'voluntary departure', 'age': 'retirement age', 'benefits': 'retirement benefits', 'service': 'completed service', 'transition': 'career transition'}},
}

class WorkArrangementEnum(RichEnum):
    """
    Work location and arrangement types
    """
    # Enum members
    ON_SITE = "ON_SITE"
    REMOTE = "REMOTE"
    HYBRID = "HYBRID"
    FIELD_WORK = "FIELD_WORK"
    TELECOMMUTE = "TELECOMMUTE"

# Set metadata after class creation
WorkArrangementEnum._metadata = {
    "ON_SITE": {'description': 'Work performed at company facilities', 'annotations': {'location': 'company premises', 'collaboration': 'in-person collaboration', 'supervision': 'direct supervision', 'equipment': 'company-provided equipment', 'culture': 'office culture participation'}},
    "REMOTE": {'description': 'Work performed away from company facilities', 'annotations': {'location': 'home or remote location', 'technology': 'technology-enabled work', 'flexibility': 'location flexibility', 'independence': 'high independence', 'communication': 'virtual communication'}},
    "HYBRID": {'description': 'Combination of on-site and remote work', 'annotations': {'flexibility': 'location flexibility', 'balance': 'office and remote balance', 'collaboration': 'mixed collaboration modes', 'scheduling': 'flexible scheduling', 'adaptation': 'adaptive work style'}},
    "FIELD_WORK": {'description': 'Work performed at client or field locations', 'annotations': {'location': 'customer or field locations', 'travel': 'travel requirements', 'independence': 'field independence', 'client': 'client interaction', 'mobility': 'mobile work style'}},
    "TELECOMMUTE": {'description': 'Regular remote work arrangement', 'annotations': {'arrangement': 'formal remote arrangement', 'technology': 'telecommunication technology', 'productivity': 'productivity focus', 'work_life': 'work-life integration', 'communication': 'virtual team communication'}},
}

class BenefitsCategoryEnum(RichEnum):
    """
    Categories of employee benefits and compensation
    """
    # Enum members
    HEALTH_INSURANCE = "HEALTH_INSURANCE"
    RETIREMENT_BENEFITS = "RETIREMENT_BENEFITS"
    PAID_TIME_OFF = "PAID_TIME_OFF"
    LIFE_INSURANCE = "LIFE_INSURANCE"
    FLEXIBLE_BENEFITS = "FLEXIBLE_BENEFITS"
    WELLNESS_PROGRAMS = "WELLNESS_PROGRAMS"
    PROFESSIONAL_DEVELOPMENT = "PROFESSIONAL_DEVELOPMENT"
    WORK_LIFE_BALANCE = "WORK_LIFE_BALANCE"

# Set metadata after class creation
BenefitsCategoryEnum._metadata = {
    "HEALTH_INSURANCE": {'description': 'Medical, dental, and vision insurance coverage', 'annotations': {'coverage': 'medical coverage', 'family': 'family coverage options', 'cost_sharing': 'employer contribution', 'networks': 'provider networks', 'essential': 'essential benefit'}},
    "RETIREMENT_BENEFITS": {'description': 'Retirement savings and pension plans', 'annotations': {'savings': '401(k) or retirement savings', 'matching': 'employer matching', 'vesting': 'vesting schedules', 'planning': 'retirement planning', 'long_term': 'long-term benefit'}},
    "PAID_TIME_OFF": {'description': 'Vacation, sick leave, and personal time', 'annotations': {'vacation': 'vacation time', 'sick': 'sick leave', 'personal': 'personal days', 'accrual': 'accrual systems', 'work_life': 'work-life balance'}},
    "LIFE_INSURANCE": {'description': 'Life and disability insurance coverage', 'annotations': {'protection': 'financial protection', 'beneficiaries': 'beneficiary designation', 'disability': 'disability coverage', 'group': 'group coverage', 'peace_of_mind': 'financial security'}},
    "FLEXIBLE_BENEFITS": {'description': 'Flexible spending and benefit choice options', 'annotations': {'choice': 'benefit choice', 'spending': 'flexible spending accounts', 'customization': 'personalized benefits', 'tax_advantage': 'tax advantages', 'lifestyle': 'lifestyle accommodation'}},
    "WELLNESS_PROGRAMS": {'description': 'Employee health and wellness initiatives', 'annotations': {'health': 'health promotion', 'fitness': 'fitness programs', 'mental_health': 'mental health support', 'prevention': 'preventive care', 'culture': 'wellness culture'}},
    "PROFESSIONAL_DEVELOPMENT": {'description': 'Training, education, and career development benefits', 'annotations': {'education': 'continuing education', 'training': 'professional training', 'career': 'career development', 'skill': 'skill enhancement', 'growth': 'professional growth'}},
    "WORK_LIFE_BALANCE": {'description': 'Benefits supporting work-life integration', 'annotations': {'flexibility': 'work flexibility', 'family': 'family support', 'childcare': 'childcare assistance', 'elder_care': 'elder care support', 'balance': 'life balance'}},
}

__all__ = [
    "EmploymentTypeEnum",
    "JobLevelEnum",
    "HRFunctionEnum",
    "CompensationTypeEnum",
    "PerformanceRatingEnum",
    "RecruitmentSourceEnum",
    "TrainingTypeEnum",
    "EmployeeStatusEnum",
    "WorkArrangementEnum",
    "BenefitsCategoryEnum",
]