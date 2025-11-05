"""
Academic and Research Value Sets

Value sets for academic publishing, research, and scholarly communication

Generated from: academic/research.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class PublicationType(RichEnum):
    """
    Types of academic and research publications
    """
    # Enum members
    JOURNAL_ARTICLE = "JOURNAL_ARTICLE"
    REVIEW_ARTICLE = "REVIEW_ARTICLE"
    RESEARCH_ARTICLE = "RESEARCH_ARTICLE"
    SHORT_COMMUNICATION = "SHORT_COMMUNICATION"
    EDITORIAL = "EDITORIAL"
    LETTER = "LETTER"
    COMMENTARY = "COMMENTARY"
    PERSPECTIVE = "PERSPECTIVE"
    CASE_REPORT = "CASE_REPORT"
    TECHNICAL_NOTE = "TECHNICAL_NOTE"
    BOOK = "BOOK"
    BOOK_CHAPTER = "BOOK_CHAPTER"
    EDITED_BOOK = "EDITED_BOOK"
    REFERENCE_BOOK = "REFERENCE_BOOK"
    TEXTBOOK = "TEXTBOOK"
    CONFERENCE_PAPER = "CONFERENCE_PAPER"
    CONFERENCE_ABSTRACT = "CONFERENCE_ABSTRACT"
    CONFERENCE_POSTER = "CONFERENCE_POSTER"
    CONFERENCE_PROCEEDINGS = "CONFERENCE_PROCEEDINGS"
    PHD_THESIS = "PHD_THESIS"
    MASTERS_THESIS = "MASTERS_THESIS"
    BACHELORS_THESIS = "BACHELORS_THESIS"
    TECHNICAL_REPORT = "TECHNICAL_REPORT"
    WORKING_PAPER = "WORKING_PAPER"
    WHITE_PAPER = "WHITE_PAPER"
    POLICY_BRIEF = "POLICY_BRIEF"
    DATASET = "DATASET"
    SOFTWARE = "SOFTWARE"
    DATA_PAPER = "DATA_PAPER"
    SOFTWARE_PAPER = "SOFTWARE_PAPER"
    PROTOCOL = "PROTOCOL"
    PREPRINT = "PREPRINT"
    POSTPRINT = "POSTPRINT"
    PUBLISHED_VERSION = "PUBLISHED_VERSION"
    PATENT = "PATENT"
    STANDARD = "STANDARD"
    BLOG_POST = "BLOG_POST"
    PRESENTATION = "PRESENTATION"
    LECTURE = "LECTURE"
    ANNOTATION = "ANNOTATION"

# Set metadata after class creation
PublicationType._metadata = {
    "JOURNAL_ARTICLE": {'description': 'Peer-reviewed journal article', 'meaning': 'FABIO:JournalArticle'},
    "REVIEW_ARTICLE": {'description': 'Review article synthesizing existing research', 'meaning': 'FABIO:ReviewArticle'},
    "RESEARCH_ARTICLE": {'description': 'Original research article', 'meaning': 'FABIO:ResearchPaper'},
    "SHORT_COMMUNICATION": {'description': 'Brief communication or short report', 'meaning': 'FABIO:BriefCommunication'},
    "EDITORIAL": {'description': 'Editorial or opinion piece', 'meaning': 'FABIO:Editorial'},
    "LETTER": {'description': 'Letter to the editor', 'meaning': 'FABIO:Letter'},
    "COMMENTARY": {'description': 'Commentary on existing work', 'meaning': 'FABIO:Comment'},
    "PERSPECTIVE": {'description': 'Perspective or viewpoint article', 'meaning': 'FABIO:Comment'},
    "CASE_REPORT": {'description': 'Clinical or scientific case report', 'meaning': 'FABIO:CaseReport'},
    "TECHNICAL_NOTE": {'description': 'Technical or methodological note', 'meaning': 'FABIO:BriefCommunication'},
    "BOOK": {'description': 'Complete book or monograph', 'meaning': 'FABIO:Book'},
    "BOOK_CHAPTER": {'description': 'Chapter in an edited book', 'meaning': 'FABIO:BookChapter'},
    "EDITED_BOOK": {'description': 'Edited collection or anthology', 'meaning': 'FABIO:EditedBook'},
    "REFERENCE_BOOK": {'description': 'Reference work or encyclopedia', 'meaning': 'FABIO:ReferenceBook'},
    "TEXTBOOK": {'description': 'Educational textbook', 'meaning': 'FABIO:Textbook'},
    "CONFERENCE_PAPER": {'description': 'Full conference paper', 'meaning': 'FABIO:ConferencePaper'},
    "CONFERENCE_ABSTRACT": {'description': 'Conference abstract', 'meaning': 'FABIO:ConferenceAbstract'},
    "CONFERENCE_POSTER": {'description': 'Conference poster', 'meaning': 'FABIO:ConferencePoster'},
    "CONFERENCE_PROCEEDINGS": {'description': 'Complete conference proceedings', 'meaning': 'FABIO:ConferenceProceedings'},
    "PHD_THESIS": {'description': 'Doctoral dissertation', 'meaning': 'FABIO:DoctoralThesis'},
    "MASTERS_THESIS": {'description': "Master's thesis", 'meaning': 'FABIO:MastersThesis'},
    "BACHELORS_THESIS": {'description': "Bachelor's or undergraduate thesis", 'meaning': 'FABIO:BachelorsThesis'},
    "TECHNICAL_REPORT": {'description': 'Technical or research report', 'meaning': 'FABIO:TechnicalReport'},
    "WORKING_PAPER": {'description': 'Working paper or discussion paper', 'meaning': 'FABIO:WorkingPaper'},
    "WHITE_PAPER": {'description': 'White paper or position paper', 'meaning': 'FABIO:WhitePaper'},
    "POLICY_BRIEF": {'description': 'Policy brief or recommendation', 'meaning': 'FABIO:PolicyBrief'},
    "DATASET": {'description': 'Research dataset', 'meaning': 'DCMITYPE:Dataset'},
    "SOFTWARE": {'description': 'Research software or code', 'meaning': 'DCMITYPE:Software'},
    "DATA_PAPER": {'description': 'Data descriptor or data paper', 'meaning': 'FABIO:DataPaper'},
    "SOFTWARE_PAPER": {'description': 'Software or tools paper', 'meaning': 'FABIO:ResearchPaper'},
    "PROTOCOL": {'description': 'Research protocol or methodology', 'meaning': 'FABIO:Protocol'},
    "PREPRINT": {'description': 'Preprint or unrefereed manuscript', 'meaning': 'FABIO:Preprint'},
    "POSTPRINT": {'description': 'Accepted manuscript after peer review', 'meaning': 'FABIO:Preprint'},
    "PUBLISHED_VERSION": {'description': 'Final published version', 'meaning': 'IAO:0000311'},
    "PATENT": {'description': 'Patent or patent application', 'meaning': 'FABIO:Patent'},
    "STANDARD": {'description': 'Technical standard or specification', 'meaning': 'FABIO:Standard'},
    "BLOG_POST": {'description': 'Academic blog post', 'meaning': 'FABIO:BlogPost'},
    "PRESENTATION": {'description': 'Presentation slides or talk', 'meaning': 'FABIO:Presentation'},
    "LECTURE": {'description': 'Lecture or educational material', 'meaning': 'FABIO:Presentation'},
    "ANNOTATION": {'description': 'Annotation or scholarly note', 'meaning': 'FABIO:Annotation'},
}

class PeerReviewStatus(RichEnum):
    """
    Status of peer review process
    """
    # Enum members
    NOT_PEER_REVIEWED = "NOT_PEER_REVIEWED"
    SUBMITTED = "SUBMITTED"
    UNDER_REVIEW = "UNDER_REVIEW"
    REVIEW_COMPLETE = "REVIEW_COMPLETE"
    MAJOR_REVISION = "MAJOR_REVISION"
    MINOR_REVISION = "MINOR_REVISION"
    ACCEPTED = "ACCEPTED"
    ACCEPTED_WITH_REVISIONS = "ACCEPTED_WITH_REVISIONS"
    REJECTED = "REJECTED"
    WITHDRAWN = "WITHDRAWN"
    PUBLISHED = "PUBLISHED"

# Set metadata after class creation
PeerReviewStatus._metadata = {
    "NOT_PEER_REVIEWED": {'description': 'Not peer reviewed'},
    "SUBMITTED": {'description': 'Submitted for review'},
    "UNDER_REVIEW": {'description': 'Currently under peer review', 'meaning': 'SIO:000035'},
    "REVIEW_COMPLETE": {'description': 'Peer review complete', 'meaning': 'SIO:000034'},
    "MAJOR_REVISION": {'description': 'Major revisions requested'},
    "MINOR_REVISION": {'description': 'Minor revisions requested'},
    "ACCEPTED": {'description': 'Accepted for publication'},
    "ACCEPTED_WITH_REVISIONS": {'description': 'Conditionally accepted pending revisions'},
    "REJECTED": {'description': 'Rejected after review'},
    "WITHDRAWN": {'description': 'Withdrawn by authors'},
    "PUBLISHED": {'description': 'Published after review', 'meaning': 'IAO:0000311'},
}

class AcademicDegree(RichEnum):
    """
    Academic degrees and qualifications
    """
    # Enum members
    BA = "BA"
    BS = "BS"
    BSC = "BSC"
    BENG = "BENG"
    BFA = "BFA"
    LLB = "LLB"
    MBBS = "MBBS"
    MA = "MA"
    MS = "MS"
    MSC = "MSC"
    MBA = "MBA"
    MFA = "MFA"
    MPH = "MPH"
    MENG = "MENG"
    MED = "MED"
    LLM = "LLM"
    MPHIL = "MPHIL"
    PHD = "PHD"
    MD = "MD"
    JD = "JD"
    EDD = "EDD"
    PSYD = "PSYD"
    DBA = "DBA"
    DPHIL = "DPHIL"
    SCD = "SCD"
    POSTDOC = "POSTDOC"

# Set metadata after class creation
AcademicDegree._metadata = {
    "BA": {'meaning': 'NCIT:C71345', 'annotations': {'level': 'undergraduate'}},
    "BS": {'description': 'Bachelor of Science', 'meaning': 'NCIT:C71351', 'annotations': {'level': 'undergraduate'}, 'aliases': ['Bachelor of Science']},
    "BSC": {'description': 'Bachelor of Science (British)', 'meaning': 'NCIT:C71351', 'annotations': {'level': 'undergraduate'}, 'aliases': ['Bachelor of Science']},
    "BENG": {'description': 'Bachelor of Engineering', 'meaning': 'NCIT:C71347', 'annotations': {'level': 'undergraduate'}, 'aliases': ['Bachelor of Engineering']},
    "BFA": {'description': 'Bachelor of Fine Arts', 'meaning': 'NCIT:C71349', 'annotations': {'level': 'undergraduate'}, 'aliases': ['Bachelor of Fine Arts']},
    "LLB": {'description': 'Bachelor of Laws', 'meaning': 'NCIT:C71352', 'annotations': {'level': 'undergraduate'}, 'aliases': ['Bachelor of Science in Law']},
    "MBBS": {'description': 'Bachelor of Medicine, Bachelor of Surgery', 'meaning': 'NCIT:C39383', 'annotations': {'level': 'undergraduate'}, 'aliases': ['Doctor of Medicine']},
    "MA": {'description': 'Master of Arts', 'meaning': 'NCIT:C71364', 'annotations': {'level': 'graduate'}, 'aliases': ['Master of Arts']},
    "MS": {'description': 'Master of Science', 'meaning': 'NCIT:C39452', 'annotations': {'level': 'graduate'}, 'aliases': ['Master of Science']},
    "MSC": {'description': 'Master of Science (British)', 'meaning': 'NCIT:C39452', 'annotations': {'level': 'graduate'}, 'aliases': ['Master of Science']},
    "MBA": {'description': 'Master of Business Administration', 'meaning': 'NCIT:C39449', 'annotations': {'level': 'graduate'}, 'aliases': ['Master of Business Administration']},
    "MFA": {'description': 'Master of Fine Arts', 'annotations': {'level': 'graduate'}},
    "MPH": {'description': 'Master of Public Health', 'meaning': 'NCIT:C39451', 'annotations': {'level': 'graduate'}, 'aliases': ['Master of Public Health']},
    "MENG": {'description': 'Master of Engineering', 'meaning': 'NCIT:C71368', 'annotations': {'level': 'graduate'}, 'aliases': ['Master of Engineering']},
    "MED": {'description': 'Master of Education', 'meaning': 'NCIT:C71369', 'annotations': {'level': 'graduate'}, 'aliases': ['Master of Education']},
    "LLM": {'description': 'Master of Laws', 'meaning': 'NCIT:C71363', 'annotations': {'level': 'graduate'}, 'aliases': ['Master of Law']},
    "MPHIL": {'description': 'Master of Philosophy', 'annotations': {'level': 'graduate'}},
    "PHD": {'description': 'Doctor of Philosophy', 'meaning': 'NCIT:C39387', 'annotations': {'level': 'doctoral'}, 'aliases': ['Doctor of Philosophy']},
    "MD": {'description': 'Doctor of Medicine', 'meaning': 'NCIT:C39383', 'annotations': {'level': 'doctoral'}, 'aliases': ['Doctor of Medicine']},
    "JD": {'description': 'Juris Doctor', 'meaning': 'NCIT:C71361', 'annotations': {'level': 'doctoral'}, 'aliases': ['Doctor of Law']},
    "EDD": {'description': 'Doctor of Education', 'meaning': 'NCIT:C71359', 'annotations': {'level': 'doctoral'}, 'aliases': ['Doctor of Education']},
    "PSYD": {'description': 'Doctor of Psychology', 'annotations': {'level': 'doctoral'}},
    "DBA": {'description': 'Doctor of Business Administration', 'annotations': {'level': 'doctoral'}},
    "DPHIL": {'description': 'Doctor of Philosophy (Oxford/Sussex)', 'meaning': 'NCIT:C39387', 'annotations': {'level': 'doctoral'}, 'aliases': ['Doctor of Philosophy']},
    "SCD": {'description': 'Doctor of Science', 'meaning': 'NCIT:C71379', 'annotations': {'level': 'doctoral'}, 'aliases': ['Doctor of Science']},
    "POSTDOC": {'description': 'Postdoctoral researcher', 'annotations': {'level': 'postdoctoral'}},
}

class LicenseType(RichEnum):
    """
    Common software and content licenses
    """
    # Enum members
    MIT = "MIT"
    APACHE_2_0 = "APACHE_2_0"
    BSD_3_CLAUSE = "BSD_3_CLAUSE"
    BSD_2_CLAUSE = "BSD_2_CLAUSE"
    ISC = "ISC"
    GPL_3_0 = "GPL_3_0"
    GPL_2_0 = "GPL_2_0"
    LGPL_3_0 = "LGPL_3_0"
    LGPL_2_1 = "LGPL_2_1"
    AGPL_3_0 = "AGPL_3_0"
    MPL_2_0 = "MPL_2_0"
    CC_BY_4_0 = "CC_BY_4_0"
    CC_BY_SA_4_0 = "CC_BY_SA_4_0"
    CC_BY_NC_4_0 = "CC_BY_NC_4_0"
    CC_BY_NC_SA_4_0 = "CC_BY_NC_SA_4_0"
    CC_BY_ND_4_0 = "CC_BY_ND_4_0"
    CC0_1_0 = "CC0_1_0"
    UNLICENSE = "UNLICENSE"
    PROPRIETARY = "PROPRIETARY"
    CUSTOM = "CUSTOM"

# Set metadata after class creation
LicenseType._metadata = {
    "MIT": {'description': 'MIT License', 'meaning': 'SPDX:MIT'},
    "APACHE_2_0": {'description': 'Apache License 2.0', 'meaning': 'SPDX:Apache-2.0'},
    "BSD_3_CLAUSE": {'description': 'BSD 3-Clause License', 'meaning': 'SPDX:BSD-3-Clause'},
    "BSD_2_CLAUSE": {'description': 'BSD 2-Clause License', 'meaning': 'SPDX:BSD-2-Clause'},
    "ISC": {'description': 'ISC License', 'meaning': 'SPDX:ISC'},
    "GPL_3_0": {'description': 'GNU General Public License v3.0', 'meaning': 'SPDX:GPL-3.0'},
    "GPL_2_0": {'description': 'GNU General Public License v2.0', 'meaning': 'SPDX:GPL-2.0'},
    "LGPL_3_0": {'description': 'GNU Lesser General Public License v3.0', 'meaning': 'SPDX:LGPL-3.0'},
    "LGPL_2_1": {'description': 'GNU Lesser General Public License v2.1', 'meaning': 'SPDX:LGPL-2.1'},
    "AGPL_3_0": {'description': 'GNU Affero General Public License v3.0', 'meaning': 'SPDX:AGPL-3.0'},
    "MPL_2_0": {'description': 'Mozilla Public License 2.0', 'meaning': 'SPDX:MPL-2.0'},
    "CC_BY_4_0": {'description': 'Creative Commons Attribution 4.0', 'meaning': 'SPDX:CC-BY-4.0'},
    "CC_BY_SA_4_0": {'description': 'Creative Commons Attribution-ShareAlike 4.0', 'meaning': 'SPDX:CC-BY-SA-4.0'},
    "CC_BY_NC_4_0": {'description': 'Creative Commons Attribution-NonCommercial 4.0', 'meaning': 'SPDX:CC-BY-NC-4.0'},
    "CC_BY_NC_SA_4_0": {'description': 'Creative Commons Attribution-NonCommercial-ShareAlike 4.0', 'meaning': 'SPDX:CC-BY-NC-SA-4.0'},
    "CC_BY_ND_4_0": {'description': 'Creative Commons Attribution-NoDerivatives 4.0', 'meaning': 'SPDX:CC-BY-ND-4.0'},
    "CC0_1_0": {'description': 'Creative Commons Zero v1.0 Universal', 'meaning': 'SPDX:CC0-1.0'},
    "UNLICENSE": {'description': 'The Unlicense', 'meaning': 'SPDX:Unlicense'},
    "PROPRIETARY": {'description': 'Proprietary/All rights reserved'},
    "CUSTOM": {'description': 'Custom license terms'},
}

class ResearchField(RichEnum):
    """
    Major research fields and disciplines
    """
    # Enum members
    PHYSICS = "PHYSICS"
    CHEMISTRY = "CHEMISTRY"
    BIOLOGY = "BIOLOGY"
    MATHEMATICS = "MATHEMATICS"
    EARTH_SCIENCES = "EARTH_SCIENCES"
    ASTRONOMY = "ASTRONOMY"
    MEDICINE = "MEDICINE"
    NEUROSCIENCE = "NEUROSCIENCE"
    GENETICS = "GENETICS"
    ECOLOGY = "ECOLOGY"
    MICROBIOLOGY = "MICROBIOLOGY"
    BIOCHEMISTRY = "BIOCHEMISTRY"
    COMPUTER_SCIENCE = "COMPUTER_SCIENCE"
    ENGINEERING = "ENGINEERING"
    MATERIALS_SCIENCE = "MATERIALS_SCIENCE"
    ARTIFICIAL_INTELLIGENCE = "ARTIFICIAL_INTELLIGENCE"
    ROBOTICS = "ROBOTICS"
    PSYCHOLOGY = "PSYCHOLOGY"
    SOCIOLOGY = "SOCIOLOGY"
    ECONOMICS = "ECONOMICS"
    POLITICAL_SCIENCE = "POLITICAL_SCIENCE"
    ANTHROPOLOGY = "ANTHROPOLOGY"
    EDUCATION = "EDUCATION"
    HISTORY = "HISTORY"
    PHILOSOPHY = "PHILOSOPHY"
    LITERATURE = "LITERATURE"
    LINGUISTICS = "LINGUISTICS"
    ART = "ART"
    MUSIC = "MUSIC"
    BIOINFORMATICS = "BIOINFORMATICS"
    COMPUTATIONAL_BIOLOGY = "COMPUTATIONAL_BIOLOGY"
    DATA_SCIENCE = "DATA_SCIENCE"
    COGNITIVE_SCIENCE = "COGNITIVE_SCIENCE"
    ENVIRONMENTAL_SCIENCE = "ENVIRONMENTAL_SCIENCE"
    PUBLIC_HEALTH = "PUBLIC_HEALTH"

# Set metadata after class creation
ResearchField._metadata = {
    "PHYSICS": {'description': 'Physics', 'meaning': 'NCIT:C16989'},
    "CHEMISTRY": {'description': 'Chemistry', 'meaning': 'NCIT:C16414'},
    "BIOLOGY": {'description': 'Biology', 'meaning': 'NCIT:C16345'},
    "MATHEMATICS": {'description': 'Mathematics', 'meaning': 'NCIT:C16825'},
    "EARTH_SCIENCES": {'description': 'Earth sciences and geology'},
    "ASTRONOMY": {'description': 'Astronomy and astrophysics'},
    "MEDICINE": {'description': 'Medicine and health sciences', 'meaning': 'NCIT:C16833'},
    "NEUROSCIENCE": {'description': 'Neuroscience', 'meaning': 'NCIT:C15817'},
    "GENETICS": {'description': 'Genetics and genomics', 'meaning': 'NCIT:C16624'},
    "ECOLOGY": {'description': 'Ecology and environmental science', 'meaning': 'NCIT:C16526'},
    "MICROBIOLOGY": {'meaning': 'NCIT:C16851'},
    "BIOCHEMISTRY": {'meaning': 'NCIT:C16337'},
    "COMPUTER_SCIENCE": {'description': 'Computer science'},
    "ENGINEERING": {'description': 'Engineering'},
    "MATERIALS_SCIENCE": {'description': 'Materials science'},
    "ARTIFICIAL_INTELLIGENCE": {'description': 'Artificial intelligence and machine learning'},
    "ROBOTICS": {'description': 'Robotics'},
    "PSYCHOLOGY": {'description': 'Psychology'},
    "SOCIOLOGY": {'description': 'Sociology'},
    "ECONOMICS": {'description': 'Economics'},
    "POLITICAL_SCIENCE": {'description': 'Political science'},
    "ANTHROPOLOGY": {'description': 'Anthropology'},
    "EDUCATION": {'description': 'Education'},
    "HISTORY": {'description': 'History'},
    "PHILOSOPHY": {'description': 'Philosophy'},
    "LITERATURE": {'description': 'Literature'},
    "LINGUISTICS": {'description': 'Linguistics'},
    "ART": {'description': 'Art and art history'},
    "MUSIC": {'description': 'Music and musicology'},
    "BIOINFORMATICS": {'description': 'Bioinformatics'},
    "COMPUTATIONAL_BIOLOGY": {'description': 'Computational biology'},
    "DATA_SCIENCE": {'description': 'Data science'},
    "COGNITIVE_SCIENCE": {'description': 'Cognitive science'},
    "ENVIRONMENTAL_SCIENCE": {'description': 'Environmental science'},
    "PUBLIC_HEALTH": {'description': 'Public health'},
}

class FundingType(RichEnum):
    """
    Types of research funding
    """
    # Enum members
    GRANT = "GRANT"
    CONTRACT = "CONTRACT"
    FELLOWSHIP = "FELLOWSHIP"
    AWARD = "AWARD"
    GIFT = "GIFT"
    INTERNAL = "INTERNAL"
    INDUSTRY = "INDUSTRY"
    GOVERNMENT = "GOVERNMENT"
    FOUNDATION = "FOUNDATION"
    CROWDFUNDING = "CROWDFUNDING"

# Set metadata after class creation
FundingType._metadata = {
    "GRANT": {'description': 'Research grant'},
    "CONTRACT": {'description': 'Research contract'},
    "FELLOWSHIP": {'description': 'Fellowship or scholarship', 'meaning': 'NCIT:C20003'},
    "AWARD": {'description': 'Prize or award'},
    "GIFT": {'description': 'Gift or donation'},
    "INTERNAL": {'description': 'Internal/institutional funding'},
    "INDUSTRY": {'description': 'Industry sponsorship'},
    "GOVERNMENT": {'description': 'Government funding'},
    "FOUNDATION": {'description': 'Foundation or charity funding'},
    "CROWDFUNDING": {'description': 'Crowdfunded research'},
}

class ManuscriptSection(RichEnum):
    """
    Sections of a scientific manuscript or publication
    """
    # Enum members
    TITLE = "TITLE"
    AUTHORS = "AUTHORS"
    ABSTRACT = "ABSTRACT"
    KEYWORDS = "KEYWORDS"
    INTRODUCTION = "INTRODUCTION"
    LITERATURE_REVIEW = "LITERATURE_REVIEW"
    METHODS = "METHODS"
    RESULTS = "RESULTS"
    DISCUSSION = "DISCUSSION"
    CONCLUSIONS = "CONCLUSIONS"
    RESULTS_AND_DISCUSSION = "RESULTS_AND_DISCUSSION"
    ACKNOWLEDGMENTS = "ACKNOWLEDGMENTS"
    REFERENCES = "REFERENCES"
    APPENDICES = "APPENDICES"
    SUPPLEMENTARY_MATERIAL = "SUPPLEMENTARY_MATERIAL"
    DATA_AVAILABILITY = "DATA_AVAILABILITY"
    CODE_AVAILABILITY = "CODE_AVAILABILITY"
    AUTHOR_CONTRIBUTIONS = "AUTHOR_CONTRIBUTIONS"
    CONFLICT_OF_INTEREST = "CONFLICT_OF_INTEREST"
    FUNDING = "FUNDING"
    ETHICS_STATEMENT = "ETHICS_STATEMENT"
    SYSTEMATIC_REVIEW_METHODS = "SYSTEMATIC_REVIEW_METHODS"
    META_ANALYSIS = "META_ANALYSIS"
    STUDY_PROTOCOL = "STUDY_PROTOCOL"
    CONSORT_FLOW_DIAGRAM = "CONSORT_FLOW_DIAGRAM"
    HIGHLIGHTS = "HIGHLIGHTS"
    GRAPHICAL_ABSTRACT = "GRAPHICAL_ABSTRACT"
    LAY_SUMMARY = "LAY_SUMMARY"
    BOX = "BOX"
    CASE_PRESENTATION = "CASE_PRESENTATION"
    LIMITATIONS = "LIMITATIONS"
    FUTURE_DIRECTIONS = "FUTURE_DIRECTIONS"
    GLOSSARY = "GLOSSARY"
    ABBREVIATIONS = "ABBREVIATIONS"
    OTHER_MAIN_TEXT = "OTHER_MAIN_TEXT"
    OTHER_SUPPLEMENTARY = "OTHER_SUPPLEMENTARY"

# Set metadata after class creation
ManuscriptSection._metadata = {
    "TITLE": {'meaning': 'IAO:0000305', 'annotations': {'order': 1}},
    "AUTHORS": {'description': 'Authors and affiliations', 'meaning': 'IAO:0000321', 'annotations': {'order': 2}},
    "ABSTRACT": {'description': 'Abstract', 'meaning': 'IAO:0000315', 'annotations': {'order': 3, 'typical_length': '150-300 words'}},
    "KEYWORDS": {'meaning': 'IAO:0000630', 'annotations': {'order': 4}},
    "INTRODUCTION": {'description': 'Introduction/Background', 'meaning': 'IAO:0000316', 'annotations': {'order': 5}, 'aliases': ['Background']},
    "LITERATURE_REVIEW": {'description': 'Literature review', 'meaning': 'IAO:0000639', 'annotations': {'order': 6, 'optional': True}},
    "METHODS": {'description': 'Methods/Materials and Methods', 'meaning': 'IAO:0000317', 'annotations': {'order': 7}, 'aliases': ['Materials and Methods', 'Methodology', 'Experimental']},
    "RESULTS": {'meaning': 'IAO:0000318', 'annotations': {'order': 8}, 'aliases': ['Findings']},
    "DISCUSSION": {'meaning': 'IAO:0000319', 'annotations': {'order': 9}},
    "CONCLUSIONS": {'description': 'Conclusions', 'meaning': 'IAO:0000615', 'annotations': {'order': 10}, 'aliases': ['Conclusion']},
    "RESULTS_AND_DISCUSSION": {'description': 'Combined Results and Discussion', 'annotations': {'order': 8, 'note': 'alternative to separate sections'}},
    "ACKNOWLEDGMENTS": {'description': 'Acknowledgments', 'meaning': 'IAO:0000324', 'annotations': {'order': 11}, 'aliases': ['Acknowledgements']},
    "REFERENCES": {'description': 'References/Bibliography', 'meaning': 'IAO:0000320', 'annotations': {'order': 12}, 'aliases': ['Bibliography', 'Literature Cited', 'Works Cited']},
    "APPENDICES": {'description': 'Appendices', 'meaning': 'IAO:0000326', 'annotations': {'order': 13}, 'aliases': ['Appendix']},
    "SUPPLEMENTARY_MATERIAL": {'description': 'Supplementary material', 'meaning': 'IAO:0000326', 'annotations': {'order': 14, 'location': 'often online-only'}, 'aliases': ['Supporting Information', 'Supplemental Data']},
    "DATA_AVAILABILITY": {'description': 'Data availability statement', 'meaning': 'IAO:0000611', 'annotations': {'order': 11.1, 'required_by': 'many journals'}},
    "CODE_AVAILABILITY": {'description': 'Code availability statement', 'meaning': 'IAO:0000611', 'annotations': {'order': 11.2}},
    "AUTHOR_CONTRIBUTIONS": {'description': 'Author contributions', 'meaning': 'IAO:0000323', 'annotations': {'order': 11.3}, 'aliases': ['CRediT statement']},
    "CONFLICT_OF_INTEREST": {'description': 'Conflict of interest statement', 'meaning': 'IAO:0000616', 'annotations': {'order': 11.4}, 'aliases': ['Competing Interests', 'Declaration of Interests']},
    "FUNDING": {'description': 'Funding information', 'meaning': 'IAO:0000623', 'annotations': {'order': 11.5}, 'aliases': ['Financial Support', 'Grant Information']},
    "ETHICS_STATEMENT": {'description': 'Ethics approval statement', 'meaning': 'IAO:0000620', 'annotations': {'order': 11.6}},
    "SYSTEMATIC_REVIEW_METHODS": {'description': 'Systematic review methodology (PRISMA)', 'annotations': {'specific_to': 'systematic reviews'}},
    "META_ANALYSIS": {'description': 'Meta-analysis section', 'annotations': {'specific_to': 'meta-analyses'}},
    "STUDY_PROTOCOL": {'description': 'Study protocol', 'annotations': {'specific_to': 'clinical trials'}},
    "CONSORT_FLOW_DIAGRAM": {'description': 'CONSORT flow diagram', 'annotations': {'specific_to': 'randomized trials'}},
    "HIGHLIGHTS": {'description': 'Highlights/Key points', 'annotations': {'order': 3.5, 'typical_length': '3-5 bullet points'}},
    "GRAPHICAL_ABSTRACT": {'description': 'Graphical abstract', 'meaning': 'IAO:0000707', 'annotations': {'order': 3.6, 'format': 'visual'}},
    "LAY_SUMMARY": {'description': 'Lay summary/Plain language summary', 'meaning': 'IAO:0000609', 'annotations': {'order': 3.7, 'audience': 'general public'}},
    "BOX": {'description': 'Box/Sidebar with supplementary information', 'annotations': {'placement': 'variable'}},
    "CASE_PRESENTATION": {'description': 'Case presentation (for case reports)', 'meaning': 'IAO:0000613', 'annotations': {'specific_to': 'case reports'}},
    "LIMITATIONS": {'description': 'Limitations section', 'meaning': 'IAO:0000631', 'annotations': {'often_part_of': 'Discussion'}},
    "FUTURE_DIRECTIONS": {'description': 'Future directions/Future work', 'meaning': 'IAO:0000625', 'annotations': {'often_part_of': 'Discussion or Conclusions'}},
    "GLOSSARY": {'description': 'Glossary of terms', 'annotations': {'placement': 'front or back matter'}},
    "ABBREVIATIONS": {'description': 'List of abbreviations', 'meaning': 'IAO:0000606', 'annotations': {'placement': 'front matter'}},
    "OTHER_MAIN_TEXT": {'description': 'Other main text section', 'annotations': {'catch_all': True}},
    "OTHER_SUPPLEMENTARY": {'description': 'Other supplementary section', 'annotations': {'catch_all': True}},
}

class ResearchRole(RichEnum):
    """
    Roles in research and authorship
    """
    # Enum members
    CONCEPTUALIZATION = "CONCEPTUALIZATION"
    DATA_CURATION = "DATA_CURATION"
    FORMAL_ANALYSIS = "FORMAL_ANALYSIS"
    FUNDING_ACQUISITION = "FUNDING_ACQUISITION"
    INVESTIGATION = "INVESTIGATION"
    METHODOLOGY = "METHODOLOGY"
    PROJECT_ADMINISTRATION = "PROJECT_ADMINISTRATION"
    RESOURCES = "RESOURCES"
    SOFTWARE = "SOFTWARE"
    SUPERVISION = "SUPERVISION"
    VALIDATION = "VALIDATION"
    VISUALIZATION = "VISUALIZATION"
    WRITING_ORIGINAL = "WRITING_ORIGINAL"
    WRITING_REVIEW = "WRITING_REVIEW"
    FIRST_AUTHOR = "FIRST_AUTHOR"
    CORRESPONDING_AUTHOR = "CORRESPONDING_AUTHOR"
    SENIOR_AUTHOR = "SENIOR_AUTHOR"
    CO_AUTHOR = "CO_AUTHOR"
    PRINCIPAL_INVESTIGATOR = "PRINCIPAL_INVESTIGATOR"
    CO_INVESTIGATOR = "CO_INVESTIGATOR"
    COLLABORATOR = "COLLABORATOR"

# Set metadata after class creation
ResearchRole._metadata = {
    "CONCEPTUALIZATION": {'description': 'Ideas; formulation of research goals', 'meaning': 'CRediT:conceptualization'},
    "DATA_CURATION": {'description': 'Data management and annotation', 'meaning': 'CRediT:data-curation'},
    "FORMAL_ANALYSIS": {'description': 'Statistical and mathematical analysis', 'meaning': 'CRediT:formal-analysis'},
    "FUNDING_ACQUISITION": {'description': 'Acquisition of financial support', 'meaning': 'CRediT:funding-acquisition'},
    "INVESTIGATION": {'description': 'Conducting research and data collection', 'meaning': 'CRediT:investigation'},
    "METHODOLOGY": {'description': 'Development of methodology', 'meaning': 'CRediT:methodology'},
    "PROJECT_ADMINISTRATION": {'description': 'Project management and coordination', 'meaning': 'CRediT:project-administration'},
    "RESOURCES": {'description': 'Provision of materials and tools', 'meaning': 'CRediT:resources'},
    "SOFTWARE": {'description': 'Programming and software development', 'meaning': 'CRediT:software'},
    "SUPERVISION": {'description': 'Oversight and mentorship', 'meaning': 'CRediT:supervision'},
    "VALIDATION": {'description': 'Verification of results', 'meaning': 'CRediT:validation'},
    "VISUALIZATION": {'description': 'Data presentation and visualization', 'meaning': 'CRediT:visualization'},
    "WRITING_ORIGINAL": {'description': 'Writing - original draft', 'meaning': 'CRediT:writing-original-draft'},
    "WRITING_REVIEW": {'description': 'Writing - review and editing', 'meaning': 'CRediT:writing-review-editing'},
    "FIRST_AUTHOR": {'description': 'First/lead author', 'meaning': 'MS:1002034'},
    "CORRESPONDING_AUTHOR": {'meaning': 'NCIT:C164481'},
    "SENIOR_AUTHOR": {'description': 'Senior/last author', 'annotations': {'note': 'Often the PI or lab head'}},
    "CO_AUTHOR": {'description': 'Co-author', 'meaning': 'NCIT:C42781'},
    "PRINCIPAL_INVESTIGATOR": {'description': 'Principal investigator (PI)', 'meaning': 'NCIT:C19924'},
    "CO_INVESTIGATOR": {'meaning': 'NCIT:C51812'},
    "COLLABORATOR": {'meaning': 'NCIT:C84336'},
}

class OpenAccessType(RichEnum):
    """
    Types of open access publishing
    """
    # Enum members
    GOLD = "GOLD"
    GREEN = "GREEN"
    HYBRID = "HYBRID"
    DIAMOND = "DIAMOND"
    BRONZE = "BRONZE"
    CLOSED = "CLOSED"
    EMBARGO = "EMBARGO"

# Set metadata after class creation
OpenAccessType._metadata = {
    "GOLD": {'description': 'Gold open access (published OA)'},
    "GREEN": {'description': 'Green open access (self-archived)'},
    "HYBRID": {'description': 'Hybrid journal with OA option'},
    "DIAMOND": {'description': 'Diamond/platinum OA (no fees)'},
    "BRONZE": {'description': 'Free to read but no license'},
    "CLOSED": {'description': 'Closed access/subscription only'},
    "EMBARGO": {'description': 'Under embargo period'},
}

class CitationStyle(RichEnum):
    """
    Common citation and reference styles
    """
    # Enum members
    APA = "APA"
    MLA = "MLA"
    CHICAGO = "CHICAGO"
    HARVARD = "HARVARD"
    VANCOUVER = "VANCOUVER"
    IEEE = "IEEE"
    ACS = "ACS"
    AMA = "AMA"
    NATURE = "NATURE"
    SCIENCE = "SCIENCE"
    CELL = "CELL"

# Set metadata after class creation
CitationStyle._metadata = {
    "APA": {'description': 'American Psychological Association'},
    "MLA": {'description': 'Modern Language Association'},
    "CHICAGO": {'description': 'Chicago Manual of Style'},
    "HARVARD": {'description': 'Harvard referencing'},
    "VANCOUVER": {'description': 'Vancouver style (biomedical)'},
    "IEEE": {'description': 'Institute of Electrical and Electronics Engineers'},
    "ACS": {'description': 'American Chemical Society'},
    "AMA": {'description': 'American Medical Association'},
    "NATURE": {'description': 'Nature style'},
    "SCIENCE": {'description': 'Science style'},
    "CELL": {'description': 'Cell Press style'},
}

__all__ = [
    "PublicationType",
    "PeerReviewStatus",
    "AcademicDegree",
    "LicenseType",
    "ResearchField",
    "FundingType",
    "ManuscriptSection",
    "ResearchRole",
    "OpenAccessType",
    "CitationStyle",
]