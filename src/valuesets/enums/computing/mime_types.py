"""
MIME Types Value Sets

Common MIME (Multipurpose Internet Mail Extensions) types for various file formats and content types used in web and application development.

Generated from: computing/mime_types.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class MimeType(RichEnum):
    """
    Common MIME types for various file formats
    """
    # Enum members
    APPLICATION_JSON = "APPLICATION_JSON"
    APPLICATION_XML = "APPLICATION_XML"
    APPLICATION_PDF = "APPLICATION_PDF"
    APPLICATION_ZIP = "APPLICATION_ZIP"
    APPLICATION_GZIP = "APPLICATION_GZIP"
    APPLICATION_OCTET_STREAM = "APPLICATION_OCTET_STREAM"
    APPLICATION_X_WWW_FORM_URLENCODED = "APPLICATION_X_WWW_FORM_URLENCODED"
    APPLICATION_VND_MS_EXCEL = "APPLICATION_VND_MS_EXCEL"
    APPLICATION_VND_OPENXMLFORMATS_SPREADSHEET = "APPLICATION_VND_OPENXMLFORMATS_SPREADSHEET"
    APPLICATION_VND_MS_POWERPOINT = "APPLICATION_VND_MS_POWERPOINT"
    APPLICATION_MSWORD = "APPLICATION_MSWORD"
    APPLICATION_VND_OPENXMLFORMATS_DOCUMENT = "APPLICATION_VND_OPENXMLFORMATS_DOCUMENT"
    APPLICATION_JAVASCRIPT = "APPLICATION_JAVASCRIPT"
    APPLICATION_TYPESCRIPT = "APPLICATION_TYPESCRIPT"
    APPLICATION_SQL = "APPLICATION_SQL"
    APPLICATION_GRAPHQL = "APPLICATION_GRAPHQL"
    APPLICATION_LD_JSON = "APPLICATION_LD_JSON"
    APPLICATION_N_QUADS = "APPLICATION_N_QUADS"
    APPLICATION_N_TRIPLES = "APPLICATION_N_TRIPLES"
    APPLICATION_RDF_XML = "APPLICATION_RDF_XML"
    APPLICATION_SPARQL_RESULTS_JSON = "APPLICATION_SPARQL_RESULTS_JSON"
    APPLICATION_SPARQL_RESULTS_XML = "APPLICATION_SPARQL_RESULTS_XML"
    APPLICATION_TRIG = "APPLICATION_TRIG"
    APPLICATION_WASM = "APPLICATION_WASM"
    TEXT_PLAIN = "TEXT_PLAIN"
    TEXT_HTML = "TEXT_HTML"
    TEXT_CSS = "TEXT_CSS"
    TEXT_CSV = "TEXT_CSV"
    TEXT_MARKDOWN = "TEXT_MARKDOWN"
    TEXT_YAML = "TEXT_YAML"
    TEXT_X_PYTHON = "TEXT_X_PYTHON"
    TEXT_X_JAVA = "TEXT_X_JAVA"
    TEXT_X_C = "TEXT_X_C"
    TEXT_X_CPP = "TEXT_X_CPP"
    TEXT_X_CSHARP = "TEXT_X_CSHARP"
    TEXT_X_GO = "TEXT_X_GO"
    TEXT_X_RUST = "TEXT_X_RUST"
    TEXT_X_RUBY = "TEXT_X_RUBY"
    TEXT_X_SHELLSCRIPT = "TEXT_X_SHELLSCRIPT"
    IMAGE_JPEG = "IMAGE_JPEG"
    IMAGE_PNG = "IMAGE_PNG"
    IMAGE_GIF = "IMAGE_GIF"
    IMAGE_SVG_XML = "IMAGE_SVG_XML"
    IMAGE_WEBP = "IMAGE_WEBP"
    IMAGE_BMP = "IMAGE_BMP"
    IMAGE_ICO = "IMAGE_ICO"
    IMAGE_TIFF = "IMAGE_TIFF"
    IMAGE_AVIF = "IMAGE_AVIF"
    AUDIO_MPEG = "AUDIO_MPEG"
    AUDIO_WAV = "AUDIO_WAV"
    AUDIO_OGG = "AUDIO_OGG"
    AUDIO_WEBM = "AUDIO_WEBM"
    AUDIO_AAC = "AUDIO_AAC"
    VIDEO_MP4 = "VIDEO_MP4"
    VIDEO_MPEG = "VIDEO_MPEG"
    VIDEO_WEBM = "VIDEO_WEBM"
    VIDEO_OGG = "VIDEO_OGG"
    VIDEO_QUICKTIME = "VIDEO_QUICKTIME"
    VIDEO_AVI = "VIDEO_AVI"
    FONT_WOFF = "FONT_WOFF"
    FONT_WOFF2 = "FONT_WOFF2"
    FONT_TTF = "FONT_TTF"
    FONT_OTF = "FONT_OTF"
    MULTIPART_FORM_DATA = "MULTIPART_FORM_DATA"
    MULTIPART_MIXED = "MULTIPART_MIXED"

# Set metadata after class creation
MimeType._metadata = {
    "APPLICATION_JSON": {'description': 'JSON format', 'meaning': 'iana:application/json'},
    "APPLICATION_XML": {'description': 'XML format', 'meaning': 'iana:application/xml'},
    "APPLICATION_PDF": {'description': 'Adobe Portable Document Format', 'meaning': 'iana:application/pdf'},
    "APPLICATION_ZIP": {'description': 'ZIP archive', 'meaning': 'iana:application/zip'},
    "APPLICATION_GZIP": {'description': 'GZIP compressed archive', 'meaning': 'iana:application/gzip'},
    "APPLICATION_OCTET_STREAM": {'description': 'Binary data', 'meaning': 'iana:application/octet-stream'},
    "APPLICATION_X_WWW_FORM_URLENCODED": {'description': 'Form data encoded', 'meaning': 'iana:application/x-www-form-urlencoded'},
    "APPLICATION_VND_MS_EXCEL": {'description': 'Microsoft Excel', 'meaning': 'iana:application/vnd.ms-excel'},
    "APPLICATION_VND_OPENXMLFORMATS_SPREADSHEET": {'description': 'Microsoft Excel (OpenXML)', 'meaning': 'iana:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'},
    "APPLICATION_VND_MS_POWERPOINT": {'description': 'Microsoft PowerPoint', 'meaning': 'iana:application/vnd.ms-powerpoint'},
    "APPLICATION_MSWORD": {'description': 'Microsoft Word', 'meaning': 'iana:application/msword'},
    "APPLICATION_VND_OPENXMLFORMATS_DOCUMENT": {'description': 'Microsoft Word (OpenXML)', 'meaning': 'iana:application/vnd.openxmlformats-officedocument.wordprocessingml.document'},
    "APPLICATION_JAVASCRIPT": {'description': 'JavaScript', 'meaning': 'iana:application/javascript'},
    "APPLICATION_TYPESCRIPT": {'description': 'TypeScript source code', 'meaning': 'iana:application/typescript'},
    "APPLICATION_SQL": {'description': 'SQL database format', 'meaning': 'iana:application/sql'},
    "APPLICATION_GRAPHQL": {'description': 'GraphQL query language', 'meaning': 'iana:application/graphql'},
    "APPLICATION_LD_JSON": {'description': 'JSON-LD format', 'meaning': 'iana:application/ld+json'},
    "APPLICATION_N_QUADS": {'description': 'N-Quads RDF serialization format', 'meaning': 'iana:application/n-quads'},
    "APPLICATION_N_TRIPLES": {'description': 'N-Triples RDF serialization format', 'meaning': 'iana:application/n-triples'},
    "APPLICATION_RDF_XML": {'description': 'RDF/XML serialization format', 'meaning': 'iana:application/rdf+xml'},
    "APPLICATION_SPARQL_RESULTS_JSON": {'description': 'SPARQL 1.1 Query Results JSON format', 'meaning': 'iana:application/sparql-results+json'},
    "APPLICATION_SPARQL_RESULTS_XML": {'description': 'SPARQL 1.1 Query Results XML format', 'meaning': 'iana:application/sparql-results+xml'},
    "APPLICATION_TRIG": {'description': 'TriG RDF serialization format', 'meaning': 'iana:application/trig'},
    "APPLICATION_WASM": {'description': 'WebAssembly binary format', 'meaning': 'iana:application/wasm'},
    "TEXT_PLAIN": {'description': 'Plain text', 'meaning': 'iana:text/plain'},
    "TEXT_HTML": {'description': 'HTML document', 'meaning': 'iana:text/html'},
    "TEXT_CSS": {'description': 'Cascading Style Sheets', 'meaning': 'iana:text/css'},
    "TEXT_CSV": {'description': 'Comma-separated values', 'meaning': 'iana:text/csv'},
    "TEXT_MARKDOWN": {'description': 'Markdown format', 'meaning': 'iana:text/markdown'},
    "TEXT_YAML": {'description': 'YAML format', 'meaning': 'iana:text/yaml'},
    "TEXT_X_PYTHON": {'description': 'Python source code', 'meaning': 'iana:text/x-python'},
    "TEXT_X_JAVA": {'description': 'Java source code', 'meaning': 'iana:text/x-java-source'},
    "TEXT_X_C": {'description': 'C source code', 'meaning': 'iana:text/x-c'},
    "TEXT_X_CPP": {'description': 'C++ source code', 'meaning': 'iana:text/x-c++'},
    "TEXT_X_CSHARP": {'description': 'C# source code', 'meaning': 'iana:text/x-csharp'},
    "TEXT_X_GO": {'description': 'Go source code', 'meaning': 'iana:text/x-go'},
    "TEXT_X_RUST": {'description': 'Rust source code', 'meaning': 'iana:text/x-rust'},
    "TEXT_X_RUBY": {'description': 'Ruby source code', 'meaning': 'iana:text/x-ruby'},
    "TEXT_X_SHELLSCRIPT": {'description': 'Shell script', 'meaning': 'iana:text/x-shellscript'},
    "IMAGE_JPEG": {'description': 'JPEG image', 'meaning': 'iana:image/jpeg'},
    "IMAGE_PNG": {'description': 'PNG image', 'meaning': 'iana:image/png'},
    "IMAGE_GIF": {'description': 'GIF image', 'meaning': 'iana:image/gif'},
    "IMAGE_SVG_XML": {'description': 'SVG vector image', 'meaning': 'iana:image/svg+xml'},
    "IMAGE_WEBP": {'description': 'WebP image', 'meaning': 'iana:image/webp'},
    "IMAGE_BMP": {'description': 'Bitmap image', 'meaning': 'iana:image/bmp'},
    "IMAGE_ICO": {'description': 'Icon format', 'meaning': 'iana:image/vnd.microsoft.icon'},
    "IMAGE_TIFF": {'description': 'TIFF image', 'meaning': 'iana:image/tiff'},
    "IMAGE_AVIF": {'description': 'AVIF image format', 'meaning': 'iana:image/avif'},
    "AUDIO_MPEG": {'description': 'MP3 audio', 'meaning': 'iana:audio/mpeg'},
    "AUDIO_WAV": {'description': 'WAV audio', 'meaning': 'iana:audio/wav'},
    "AUDIO_OGG": {'description': 'OGG audio', 'meaning': 'iana:audio/ogg'},
    "AUDIO_WEBM": {'description': 'WebM audio', 'meaning': 'iana:audio/webm'},
    "AUDIO_AAC": {'description': 'AAC audio', 'meaning': 'iana:audio/aac'},
    "VIDEO_MP4": {'description': 'MP4 video', 'meaning': 'iana:video/mp4'},
    "VIDEO_MPEG": {'description': 'MPEG video', 'meaning': 'iana:video/mpeg'},
    "VIDEO_WEBM": {'description': 'WebM video', 'meaning': 'iana:video/webm'},
    "VIDEO_OGG": {'description': 'OGG video', 'meaning': 'iana:video/ogg'},
    "VIDEO_QUICKTIME": {'description': 'QuickTime video', 'meaning': 'iana:video/quicktime'},
    "VIDEO_AVI": {'description': 'AVI video', 'meaning': 'iana:video/x-msvideo'},
    "FONT_WOFF": {'description': 'Web Open Font Format', 'meaning': 'iana:font/woff'},
    "FONT_WOFF2": {'description': 'Web Open Font Format 2', 'meaning': 'iana:font/woff2'},
    "FONT_TTF": {'description': 'TrueType Font', 'meaning': 'iana:font/ttf'},
    "FONT_OTF": {'description': 'OpenType Font', 'meaning': 'iana:font/otf'},
    "MULTIPART_FORM_DATA": {'description': 'Form data with file upload', 'meaning': 'iana:multipart/form-data'},
    "MULTIPART_MIXED": {'description': 'Mixed multipart message', 'meaning': 'iana:multipart/mixed'},
}

class MimeTypeCategory(RichEnum):
    """
    Categories of MIME types
    """
    # Enum members
    APPLICATION = "APPLICATION"
    TEXT = "TEXT"
    IMAGE = "IMAGE"
    AUDIO = "AUDIO"
    VIDEO = "VIDEO"
    FONT = "FONT"
    MULTIPART = "MULTIPART"
    MESSAGE = "MESSAGE"
    MODEL = "MODEL"

# Set metadata after class creation
MimeTypeCategory._metadata = {
    "APPLICATION": {'description': 'Application data'},
    "TEXT": {'description': 'Text documents'},
    "IMAGE": {'description': 'Image files'},
    "AUDIO": {'description': 'Audio files'},
    "VIDEO": {'description': 'Video files'},
    "FONT": {'description': 'Font files'},
    "MULTIPART": {'description': 'Multipart messages'},
    "MESSAGE": {'description': 'Message formats'},
    "MODEL": {'description': '3D models and similar'},
}

class TextCharset(RichEnum):
    """
    Character encodings for text content
    """
    # Enum members
    UTF_8 = "UTF_8"
    UTF_16 = "UTF_16"
    UTF_32 = "UTF_32"
    ASCII = "ASCII"
    ISO_8859_1 = "ISO_8859_1"
    ISO_8859_2 = "ISO_8859_2"
    WINDOWS_1252 = "WINDOWS_1252"
    GB2312 = "GB2312"
    SHIFT_JIS = "SHIFT_JIS"
    EUC_KR = "EUC_KR"
    BIG5 = "BIG5"

# Set metadata after class creation
TextCharset._metadata = {
    "UTF_8": {'description': 'UTF-8 Unicode encoding'},
    "UTF_16": {'description': 'UTF-16 Unicode encoding'},
    "UTF_32": {'description': 'UTF-32 Unicode encoding'},
    "ASCII": {'description': 'ASCII encoding'},
    "ISO_8859_1": {'description': 'ISO-8859-1 (Latin-1) encoding'},
    "ISO_8859_2": {'description': 'ISO-8859-2 (Latin-2) encoding'},
    "WINDOWS_1252": {'description': 'Windows-1252 encoding'},
    "GB2312": {'description': 'Simplified Chinese encoding'},
    "SHIFT_JIS": {'description': 'Japanese encoding'},
    "EUC_KR": {'description': 'Korean encoding'},
    "BIG5": {'description': 'Traditional Chinese encoding'},
}

class CompressionType(RichEnum):
    """
    Compression types used with Content-Encoding
    """
    # Enum members
    GZIP = "GZIP"
    DEFLATE = "DEFLATE"
    BR = "BR"
    COMPRESS = "COMPRESS"
    IDENTITY = "IDENTITY"

# Set metadata after class creation
CompressionType._metadata = {
    "GZIP": {'description': 'GZIP compression'},
    "DEFLATE": {'description': 'DEFLATE compression'},
    "BR": {'description': 'Brotli compression'},
    "COMPRESS": {'description': 'Unix compress'},
    "IDENTITY": {'description': 'No compression'},
}

__all__ = [
    "MimeType",
    "MimeTypeCategory",
    "TextCharset",
    "CompressionType",
]