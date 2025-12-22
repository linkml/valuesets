"""
Research Resource Types

Resource type classifications for research outputs, based on DataCite 4.6.

DataCite is a global registration agency for research data identifiers (DOIs)
and provides a schema for describing research outputs.

See: https://datacite-metadata-schema.readthedocs.io/


Generated from: data_catalog/resource_types.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class DataCiteResourceType(RichEnum):
    """
    General resource type classifications from DataCite 4.6.
    Used for categorizing research outputs in data repositories.
    
    """
    # Enum members
    AUDIOVISUAL = "AUDIOVISUAL"
    AWARD = "AWARD"
    BOOK = "BOOK"
    BOOK_CHAPTER = "BOOK_CHAPTER"
    COLLECTION = "COLLECTION"
    COMPUTATIONAL_NOTEBOOK = "COMPUTATIONAL_NOTEBOOK"
    CONFERENCE_PAPER = "CONFERENCE_PAPER"
    CONFERENCE_PROCEEDING = "CONFERENCE_PROCEEDING"
    DATA_PAPER = "DATA_PAPER"
    DATASET = "DATASET"
    DISSERTATION = "DISSERTATION"
    EVENT = "EVENT"
    IMAGE = "IMAGE"
    INSTRUMENT = "INSTRUMENT"
    INTERACTIVE_RESOURCE = "INTERACTIVE_RESOURCE"
    JOURNAL = "JOURNAL"
    JOURNAL_ARTICLE = "JOURNAL_ARTICLE"
    MODEL = "MODEL"
    OUTPUT_MANAGEMENT_PLAN = "OUTPUT_MANAGEMENT_PLAN"
    PEER_REVIEW = "PEER_REVIEW"
    PHYSICAL_OBJECT = "PHYSICAL_OBJECT"
    PREPRINT = "PREPRINT"
    PROJECT = "PROJECT"
    REPORT = "REPORT"
    SERVICE = "SERVICE"
    SOFTWARE = "SOFTWARE"
    SOUND = "SOUND"
    STANDARD = "STANDARD"
    STUDY_REGISTRATION = "STUDY_REGISTRATION"
    TEXT = "TEXT"
    WORKFLOW = "WORKFLOW"
    OTHER = "OTHER"

# Set metadata after class creation
DataCiteResourceType._metadata = {
    "AUDIOVISUAL": {'description': 'A series of visual representations imparting an impression of motion\nwhen shown in succession. May include sound.\n', 'meaning': 'DataCite:Audiovisual', 'annotations': {'examples': 'video, film, animation'}},
    "AWARD": {'description': 'Funding or support provided to an individual or organization\nfor research, academic work, or professional development.\n', 'meaning': 'DataCite:Award', 'annotations': {'added_version': '4.6', 'examples': 'grant award, fellowship, scholarship'}},
    "BOOK": {'description': 'A medium for recording information in the form of writing or images,\ntypically composed of many pages bound together.\n', 'meaning': 'DataCite:Book'},
    "BOOK_CHAPTER": {'description': 'One of the main divisions of a book.', 'meaning': 'DataCite:BookChapter'},
    "COLLECTION": {'description': 'An aggregation of resources, which may encompass collections of\none resource type as well as those of mixed types.\n', 'meaning': 'DataCite:Collection'},
    "COMPUTATIONAL_NOTEBOOK": {'description': 'A virtual notebook environment used for literate programming,\ncombining code, documentation, and visualizations.\n', 'meaning': 'DataCite:ComputationalNotebook', 'annotations': {'examples': 'Jupyter notebook, R Markdown, Observable'}},
    "CONFERENCE_PAPER": {'description': 'Article written with the goal of being accepted to a conference.\n', 'meaning': 'DataCite:ConferencePaper'},
    "CONFERENCE_PROCEEDING": {'description': 'Collection of academic papers published in the context of\nan academic conference.\n', 'meaning': 'DataCite:ConferenceProceeding'},
    "DATA_PAPER": {'description': 'A scholarly publication describing a dataset, intended to\nfacilitate its discovery, interpretation, and reuse.\n', 'meaning': 'DataCite:DataPaper'},
    "DATASET": {'description': 'Data encoded in a defined structure. May include tables,\ndatabases, or other structured data.\n', 'meaning': 'DataCite:Dataset'},
    "DISSERTATION": {'description': 'A written essay, treatise, or thesis, especially one written\nby a candidate for a doctoral degree.\n', 'meaning': 'DataCite:Dissertation'},
    "EVENT": {'description': 'A non-persistent, time-based occurrence. May be planned or\nunplanned.\n', 'meaning': 'DataCite:Event', 'annotations': {'examples': 'conference, workshop, exhibition'}},
    "IMAGE": {'description': 'A visual representation other than text, including photographs,\ndiagrams, illustrations, and other static visual works.\n', 'meaning': 'DataCite:Image'},
    "INSTRUMENT": {'description': 'A device, tool, or apparatus used to obtain, measure, and/or\nanalyze data.\n', 'meaning': 'DataCite:Instrument', 'annotations': {'examples': 'microscope, telescope, sensor, spectrometer'}},
    "INTERACTIVE_RESOURCE": {'description': 'A resource requiring interaction from the user to be understood,\nexecuted, or experienced.\n', 'meaning': 'DataCite:InteractiveResource', 'annotations': {'examples': 'web application, game, simulation'}},
    "JOURNAL": {'description': 'A scholarly publication consisting of articles that is published\nregularly throughout the year.\n', 'meaning': 'DataCite:Journal'},
    "JOURNAL_ARTICLE": {'description': 'A written composition on a topic of interest, which forms a\nseparate part of a journal.\n', 'meaning': 'DataCite:JournalArticle'},
    "MODEL": {'description': 'An abstract, conceptual, graphical, mathematical, or visualization\nmodel that represents empirical objects, phenomena, or processes.\n', 'meaning': 'DataCite:Model', 'annotations': {'examples': '3D model, statistical model, simulation model'}},
    "OUTPUT_MANAGEMENT_PLAN": {'description': 'A formal document that outlines how research outputs are to be\nhandled during and after a research project.\n', 'meaning': 'DataCite:OutputManagementPlan', 'aliases': ['Data Management Plan', 'DMP']},
    "PEER_REVIEW": {'description': 'Evaluation of scientific, academic, or professional work by\nothers working in the same field.\n', 'meaning': 'DataCite:PeerReview'},
    "PHYSICAL_OBJECT": {'description': 'A physical object or substance, including artifacts, specimens,\nsamples, and material objects.\n', 'meaning': 'DataCite:PhysicalObject', 'annotations': {'examples': 'fossil, artifact, tissue sample, mineral specimen'}},
    "PREPRINT": {'description': 'A version of a scholarly or scientific paper that precedes\nformal peer review and publication in a journal.\n', 'meaning': 'DataCite:Preprint'},
    "PROJECT": {'description': 'A planned endeavor or activity, frequently collaborative,\nintended to achieve a particular aim.\n', 'meaning': 'DataCite:Project', 'annotations': {'added_version': '4.6'}},
    "REPORT": {'description': 'A document that presents information in an organized format\nfor a specific audience and purpose.\n', 'meaning': 'DataCite:Report'},
    "SERVICE": {'description': 'An organized system of apparatus, appliances, staff, etc.,\nfor supplying some function required by end users.\n', 'meaning': 'DataCite:Service', 'annotations': {'examples': 'API, web service, data service'}},
    "SOFTWARE": {'description': 'A computer program other than a computational notebook,\nin either source code (text) or compiled form.\n', 'meaning': 'DataCite:Software'},
    "SOUND": {'description': 'A resource primarily intended to be heard, including music,\nspeech, and other audio recordings.\n', 'meaning': 'DataCite:Sound'},
    "STANDARD": {'description': 'Something established by authority, custom, or general consent\nas a model, example, or point of reference.\n', 'meaning': 'DataCite:Standard', 'annotations': {'examples': 'ISO standard, data format specification'}},
    "STUDY_REGISTRATION": {'description': 'A detailed, time-stamped description of a research plan,\noften openly shared in a registry or repository.\n', 'meaning': 'DataCite:StudyRegistration', 'annotations': {'examples': 'clinical trial registration, pre-registration'}},
    "TEXT": {'description': 'A resource consisting primarily of words for reading that is\nnot covered by any other textual resource type.\n', 'meaning': 'DataCite:Text'},
    "WORKFLOW": {'description': 'A structured series of steps which can be executed to produce\na final outcome, often automated.\n', 'meaning': 'DataCite:Workflow', 'annotations': {'examples': 'bioinformatics pipeline, ETL workflow, analysis script'}},
    "OTHER": {'description': 'Use when the resource type does not fit any other category.\nShould be accompanied by a free-text description.\n', 'meaning': 'DataCite:Other'},
}

__all__ = [
    "DataCiteResourceType",
]