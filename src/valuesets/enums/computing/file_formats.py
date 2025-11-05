"""
File Formats and Protocols Value Sets

Value sets for file formats, data formats, and communication protocols commonly used in computing and data exchange.


Generated from: computing/file_formats.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class ImageFileFormatEnum(RichEnum):
    """
    Common image file formats
    """
    # Enum members
    JPEG = "JPEG"
    PNG = "PNG"
    GIF = "GIF"
    BMP = "BMP"
    TIFF = "TIFF"
    SVG = "SVG"
    WEBP = "WEBP"
    HEIC = "HEIC"
    RAW = "RAW"
    ICO = "ICO"

# Set metadata after class creation
ImageFileFormatEnum._metadata = {
    "JPEG": {'description': 'Joint Photographic Experts Group', 'meaning': 'EDAM:format_3579', 'annotations': {'extension': '.jpg, .jpeg', 'mime_type': 'image/jpeg', 'compression': 'lossy'}, 'aliases': ['JPG']},
    "PNG": {'description': 'Portable Network Graphics', 'meaning': 'EDAM:format_3603', 'annotations': {'extension': '.png', 'mime_type': 'image/png', 'compression': 'lossless'}},
    "GIF": {'description': 'Graphics Interchange Format', 'meaning': 'EDAM:format_3467', 'annotations': {'extension': '.gif', 'mime_type': 'image/gif', 'features': 'animation support'}},
    "BMP": {'description': 'Bitmap Image File', 'meaning': 'EDAM:format_3592', 'annotations': {'extension': '.bmp', 'mime_type': 'image/bmp', 'compression': 'uncompressed'}},
    "TIFF": {'description': 'Tagged Image File Format', 'meaning': 'EDAM:format_3591', 'annotations': {'extension': '.tif, .tiff', 'mime_type': 'image/tiff', 'use': 'professional photography, scanning'}},
    "SVG": {'description': 'Scalable Vector Graphics', 'meaning': 'EDAM:format_3604', 'annotations': {'extension': '.svg', 'mime_type': 'image/svg+xml', 'type': 'vector'}},
    "WEBP": {'description': 'WebP image format', 'annotations': {'extension': '.webp', 'mime_type': 'image/webp', 'compression': 'lossy and lossless'}},
    "HEIC": {'description': 'High Efficiency Image Container', 'annotations': {'extension': '.heic, .heif', 'mime_type': 'image/heic', 'use': 'Apple devices'}},
    "RAW": {'description': 'Raw image format', 'annotations': {'extension': '.raw, .cr2, .nef, .arw', 'type': 'unprocessed sensor data'}},
    "ICO": {'description': 'Icon file format', 'annotations': {'extension': '.ico', 'mime_type': 'image/x-icon', 'use': 'favicons, app icons'}},
}

class DocumentFormatEnum(RichEnum):
    """
    Document and text file formats
    """
    # Enum members
    PDF = "PDF"
    DOCX = "DOCX"
    DOC = "DOC"
    TXT = "TXT"
    RTF = "RTF"
    ODT = "ODT"
    LATEX = "LATEX"
    MARKDOWN = "MARKDOWN"
    HTML = "HTML"
    XML = "XML"
    EPUB = "EPUB"

# Set metadata after class creation
DocumentFormatEnum._metadata = {
    "PDF": {'description': 'Portable Document Format', 'meaning': 'EDAM:format_3508', 'annotations': {'extension': '.pdf', 'mime_type': 'application/pdf', 'creator': 'Adobe'}},
    "DOCX": {'description': 'Microsoft Word Open XML', 'annotations': {'extension': '.docx', 'mime_type': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document', 'application': 'Microsoft Word'}},
    "DOC": {'description': 'Microsoft Word legacy format', 'annotations': {'extension': '.doc', 'mime_type': 'application/msword', 'application': 'Microsoft Word (legacy)'}},
    "TXT": {'description': 'Plain text file', 'meaning': 'EDAM:format_1964', 'annotations': {'extension': '.txt', 'mime_type': 'text/plain', 'encoding': 'UTF-8, ASCII'}, 'aliases': ['plain text format (unformatted)']},
    "RTF": {'description': 'Rich Text Format', 'annotations': {'extension': '.rtf', 'mime_type': 'application/rtf'}},
    "ODT": {'description': 'OpenDocument Text', 'annotations': {'extension': '.odt', 'mime_type': 'application/vnd.oasis.opendocument.text', 'application': 'LibreOffice, OpenOffice'}},
    "LATEX": {'description': 'LaTeX document', 'meaning': 'EDAM:format_3817', 'annotations': {'extension': '.tex', 'mime_type': 'application/x-latex', 'use': 'scientific documents'}, 'aliases': ['latex', 'LaTeX']},
    "MARKDOWN": {'description': 'Markdown formatted text', 'annotations': {'extension': '.md, .markdown', 'mime_type': 'text/markdown'}},
    "HTML": {'description': 'HyperText Markup Language', 'meaning': 'EDAM:format_2331', 'annotations': {'extension': '.html, .htm', 'mime_type': 'text/html'}},
    "XML": {'description': 'Extensible Markup Language', 'meaning': 'EDAM:format_2332', 'annotations': {'extension': '.xml', 'mime_type': 'application/xml'}},
    "EPUB": {'description': 'Electronic Publication', 'annotations': {'extension': '.epub', 'mime_type': 'application/epub+zip', 'use': 'e-books'}},
}

class DataFormatEnum(RichEnum):
    """
    Structured data file formats
    """
    # Enum members
    JSON = "JSON"
    CSV = "CSV"
    TSV = "TSV"
    YAML = "YAML"
    TOML = "TOML"
    XLSX = "XLSX"
    XLS = "XLS"
    ODS = "ODS"
    PARQUET = "PARQUET"
    AVRO = "AVRO"
    HDF5 = "HDF5"
    NETCDF = "NETCDF"
    SQLITE = "SQLITE"

# Set metadata after class creation
DataFormatEnum._metadata = {
    "JSON": {'description': 'JavaScript Object Notation', 'meaning': 'EDAM:format_3464', 'annotations': {'extension': '.json', 'mime_type': 'application/json', 'type': 'text-based'}},
    "CSV": {'description': 'Comma-Separated Values', 'meaning': 'EDAM:format_3752', 'annotations': {'extension': '.csv', 'mime_type': 'text/csv', 'delimiter': 'comma'}},
    "TSV": {'description': 'Tab-Separated Values', 'meaning': 'EDAM:format_3475', 'annotations': {'extension': '.tsv, .tab', 'mime_type': 'text/tab-separated-values', 'delimiter': 'tab'}},
    "YAML": {'description': "YAML Ain't Markup Language", 'meaning': 'EDAM:format_3750', 'annotations': {'extension': '.yaml, .yml', 'mime_type': 'application/x-yaml'}},
    "TOML": {'description': "Tom's Obvious Minimal Language", 'annotations': {'extension': '.toml', 'mime_type': 'application/toml', 'use': 'configuration files'}},
    "XLSX": {'description': 'Microsoft Excel Open XML', 'annotations': {'extension': '.xlsx', 'mime_type': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'}},
    "XLS": {'description': 'Microsoft Excel legacy format', 'annotations': {'extension': '.xls', 'mime_type': 'application/vnd.ms-excel'}},
    "ODS": {'description': 'OpenDocument Spreadsheet', 'annotations': {'extension': '.ods', 'mime_type': 'application/vnd.oasis.opendocument.spreadsheet'}},
    "PARQUET": {'description': 'Apache Parquet columnar format', 'annotations': {'extension': '.parquet', 'mime_type': 'application/parquet', 'type': 'columnar storage'}},
    "AVRO": {'description': 'Apache Avro data serialization', 'annotations': {'extension': '.avro', 'mime_type': 'application/avro', 'features': 'schema evolution'}},
    "HDF5": {'description': 'Hierarchical Data Format version 5', 'meaning': 'EDAM:format_3590', 'annotations': {'extension': '.h5, .hdf5', 'mime_type': 'application/x-hdf', 'use': 'scientific data'}},
    "NETCDF": {'description': 'Network Common Data Form', 'meaning': 'EDAM:format_3650', 'annotations': {'extension': '.nc, .nc4', 'mime_type': 'application/x-netcdf', 'use': 'array-oriented scientific data'}},
    "SQLITE": {'description': 'SQLite database', 'annotations': {'extension': '.db, .sqlite, .sqlite3', 'mime_type': 'application/x-sqlite3', 'type': 'embedded database'}},
}

class ArchiveFormatEnum(RichEnum):
    """
    Archive and compression formats
    """
    # Enum members
    ZIP = "ZIP"
    TAR = "TAR"
    GZIP = "GZIP"
    TAR_GZ = "TAR_GZ"
    BZIP2 = "BZIP2"
    TAR_BZ2 = "TAR_BZ2"
    XZ = "XZ"
    TAR_XZ = "TAR_XZ"
    SEVEN_ZIP = "SEVEN_ZIP"
    RAR = "RAR"

# Set metadata after class creation
ArchiveFormatEnum._metadata = {
    "ZIP": {'description': 'ZIP archive', 'annotations': {'extension': '.zip', 'mime_type': 'application/zip', 'compression': 'DEFLATE'}},
    "TAR": {'description': 'Tape Archive', 'annotations': {'extension': '.tar', 'mime_type': 'application/x-tar', 'compression': 'none (archive only)'}},
    "GZIP": {'description': 'GNU zip', 'annotations': {'extension': '.gz', 'mime_type': 'application/gzip', 'compression': 'DEFLATE'}},
    "TAR_GZ": {'description': 'Gzipped tar archive', 'annotations': {'extension': '.tar.gz, .tgz', 'mime_type': 'application/x-gtar', 'compression': 'tar + gzip'}},
    "BZIP2": {'description': 'Bzip2 compression', 'annotations': {'extension': '.bz2', 'mime_type': 'application/x-bzip2', 'compression': 'Burrows-Wheeler'}},
    "TAR_BZ2": {'description': 'Bzip2 compressed tar archive', 'annotations': {'extension': '.tar.bz2, .tbz2', 'mime_type': 'application/x-bzip2'}},
    "XZ": {'description': 'XZ compression', 'annotations': {'extension': '.xz', 'mime_type': 'application/x-xz', 'compression': 'LZMA2'}},
    "TAR_XZ": {'description': 'XZ compressed tar archive', 'annotations': {'extension': '.tar.xz, .txz', 'mime_type': 'application/x-xz'}},
    "SEVEN_ZIP": {'description': '7-Zip archive', 'annotations': {'extension': '.7z', 'mime_type': 'application/x-7z-compressed', 'compression': 'LZMA'}},
    "RAR": {'description': 'RAR archive', 'annotations': {'extension': '.rar', 'mime_type': 'application/vnd.rar', 'proprietary': 'true'}},
}

class VideoFormatEnum(RichEnum):
    """
    Video file formats
    """
    # Enum members
    MP4 = "MP4"
    AVI = "AVI"
    MOV = "MOV"
    MKV = "MKV"
    WEBM = "WEBM"
    FLV = "FLV"
    WMV = "WMV"
    MPEG = "MPEG"

# Set metadata after class creation
VideoFormatEnum._metadata = {
    "MP4": {'description': 'MPEG-4 Part 14', 'annotations': {'extension': '.mp4', 'mime_type': 'video/mp4', 'codec': 'H.264, H.265'}},
    "AVI": {'description': 'Audio Video Interleave', 'annotations': {'extension': '.avi', 'mime_type': 'video/x-msvideo', 'creator': 'Microsoft'}},
    "MOV": {'description': 'QuickTime Movie', 'annotations': {'extension': '.mov', 'mime_type': 'video/quicktime', 'creator': 'Apple'}},
    "MKV": {'description': 'Matroska Video', 'annotations': {'extension': '.mkv', 'mime_type': 'video/x-matroska', 'features': 'multiple tracks'}},
    "WEBM": {'description': 'WebM video', 'annotations': {'extension': '.webm', 'mime_type': 'video/webm', 'codec': 'VP8, VP9'}},
    "FLV": {'description': 'Flash Video', 'annotations': {'extension': '.flv', 'mime_type': 'video/x-flv', 'status': 'legacy'}},
    "WMV": {'description': 'Windows Media Video', 'annotations': {'extension': '.wmv', 'mime_type': 'video/x-ms-wmv', 'creator': 'Microsoft'}},
    "MPEG": {'description': 'Moving Picture Experts Group', 'annotations': {'extension': '.mpeg, .mpg', 'mime_type': 'video/mpeg'}},
}

class AudioFormatEnum(RichEnum):
    """
    Audio file formats
    """
    # Enum members
    MP3 = "MP3"
    WAV = "WAV"
    FLAC = "FLAC"
    AAC = "AAC"
    OGG = "OGG"
    M4A = "M4A"
    WMA = "WMA"
    OPUS = "OPUS"
    AIFF = "AIFF"

# Set metadata after class creation
AudioFormatEnum._metadata = {
    "MP3": {'description': 'MPEG Audio Layer 3', 'annotations': {'extension': '.mp3', 'mime_type': 'audio/mpeg', 'compression': 'lossy'}},
    "WAV": {'description': 'Waveform Audio File Format', 'annotations': {'extension': '.wav', 'mime_type': 'audio/wav', 'compression': 'uncompressed'}},
    "FLAC": {'description': 'Free Lossless Audio Codec', 'annotations': {'extension': '.flac', 'mime_type': 'audio/flac', 'compression': 'lossless'}},
    "AAC": {'description': 'Advanced Audio Coding', 'annotations': {'extension': '.aac', 'mime_type': 'audio/aac', 'compression': 'lossy'}},
    "OGG": {'description': 'Ogg Vorbis', 'annotations': {'extension': '.ogg', 'mime_type': 'audio/ogg', 'compression': 'lossy'}},
    "M4A": {'description': 'MPEG-4 Audio', 'annotations': {'extension': '.m4a', 'mime_type': 'audio/mp4', 'compression': 'lossy or lossless'}},
    "WMA": {'description': 'Windows Media Audio', 'annotations': {'extension': '.wma', 'mime_type': 'audio/x-ms-wma', 'creator': 'Microsoft'}},
    "OPUS": {'description': 'Opus Interactive Audio Codec', 'annotations': {'extension': '.opus', 'mime_type': 'audio/opus', 'use': 'streaming, VoIP'}},
    "AIFF": {'description': 'Audio Interchange File Format', 'annotations': {'extension': '.aiff, .aif', 'mime_type': 'audio/aiff', 'creator': 'Apple'}},
}

class ProgrammingLanguageFileEnum(RichEnum):
    """
    Programming language source file extensions
    """
    # Enum members
    PYTHON = "PYTHON"
    JAVASCRIPT = "JAVASCRIPT"
    TYPESCRIPT = "TYPESCRIPT"
    JAVA = "JAVA"
    C = "C"
    CPP = "CPP"
    C_SHARP = "C_SHARP"
    GO = "GO"
    RUST = "RUST"
    RUBY = "RUBY"
    PHP = "PHP"
    SWIFT = "SWIFT"
    KOTLIN = "KOTLIN"
    R = "R"
    MATLAB = "MATLAB"
    JULIA = "JULIA"
    SHELL = "SHELL"

# Set metadata after class creation
ProgrammingLanguageFileEnum._metadata = {
    "PYTHON": {'description': 'Python source file', 'annotations': {'extension': '.py', 'mime_type': 'text/x-python'}},
    "JAVASCRIPT": {'description': 'JavaScript source file', 'annotations': {'extension': '.js', 'mime_type': 'text/javascript'}},
    "TYPESCRIPT": {'description': 'TypeScript source file', 'annotations': {'extension': '.ts', 'mime_type': 'text/typescript'}},
    "JAVA": {'description': 'Java source file', 'annotations': {'extension': '.java', 'mime_type': 'text/x-java-source'}},
    "C": {'description': 'C source file', 'annotations': {'extension': '.c', 'mime_type': 'text/x-c'}},
    "CPP": {'description': 'C++ source file', 'annotations': {'extension': '.cpp, .cc, .cxx', 'mime_type': 'text/x-c++'}},
    "C_SHARP": {'description': 'C# source file', 'annotations': {'extension': '.cs', 'mime_type': 'text/x-csharp'}},
    "GO": {'description': 'Go source file', 'annotations': {'extension': '.go', 'mime_type': 'text/x-go'}},
    "RUST": {'description': 'Rust source file', 'annotations': {'extension': '.rs', 'mime_type': 'text/x-rust'}},
    "RUBY": {'description': 'Ruby source file', 'annotations': {'extension': '.rb', 'mime_type': 'text/x-ruby'}},
    "PHP": {'description': 'PHP source file', 'annotations': {'extension': '.php', 'mime_type': 'text/x-php'}},
    "SWIFT": {'description': 'Swift source file', 'annotations': {'extension': '.swift', 'mime_type': 'text/x-swift'}},
    "KOTLIN": {'description': 'Kotlin source file', 'annotations': {'extension': '.kt', 'mime_type': 'text/x-kotlin'}},
    "R": {'description': 'R source file', 'annotations': {'extension': '.r, .R', 'mime_type': 'text/x-r'}},
    "MATLAB": {'description': 'MATLAB source file', 'annotations': {'extension': '.m', 'mime_type': 'text/x-matlab'}},
    "JULIA": {'description': 'Julia source file', 'annotations': {'extension': '.jl', 'mime_type': 'text/x-julia'}},
    "SHELL": {'description': 'Shell script', 'annotations': {'extension': '.sh, .bash', 'mime_type': 'text/x-shellscript'}},
}

class NetworkProtocolEnum(RichEnum):
    """
    Network communication protocols
    """
    # Enum members
    HTTP = "HTTP"
    HTTPS = "HTTPS"
    FTP = "FTP"
    SFTP = "SFTP"
    SSH = "SSH"
    TELNET = "TELNET"
    SMTP = "SMTP"
    POP3 = "POP3"
    IMAP = "IMAP"
    DNS = "DNS"
    DHCP = "DHCP"
    TCP = "TCP"
    UDP = "UDP"
    WEBSOCKET = "WEBSOCKET"
    MQTT = "MQTT"
    AMQP = "AMQP"
    GRPC = "GRPC"

# Set metadata after class creation
NetworkProtocolEnum._metadata = {
    "HTTP": {'description': 'Hypertext Transfer Protocol', 'annotations': {'port': '80', 'layer': 'application', 'version': '1.0, 1.1, 2, 3'}},
    "HTTPS": {'description': 'HTTP Secure', 'annotations': {'port': '443', 'layer': 'application', 'encryption': 'TLS/SSL'}},
    "FTP": {'description': 'File Transfer Protocol', 'annotations': {'port': '21', 'layer': 'application', 'use': 'file transfer'}},
    "SFTP": {'description': 'SSH File Transfer Protocol', 'annotations': {'port': '22', 'layer': 'application', 'encryption': 'SSH'}},
    "SSH": {'description': 'Secure Shell', 'annotations': {'port': '22', 'layer': 'application', 'use': 'secure remote access'}},
    "TELNET": {'description': 'Telnet protocol', 'annotations': {'port': '23', 'layer': 'application', 'security': 'unencrypted'}},
    "SMTP": {'description': 'Simple Mail Transfer Protocol', 'annotations': {'port': '25, 587', 'layer': 'application', 'use': 'email sending'}},
    "POP3": {'description': 'Post Office Protocol version 3', 'annotations': {'port': '110, 995', 'layer': 'application', 'use': 'email retrieval'}},
    "IMAP": {'description': 'Internet Message Access Protocol', 'annotations': {'port': '143, 993', 'layer': 'application', 'use': 'email access'}},
    "DNS": {'description': 'Domain Name System', 'annotations': {'port': '53', 'layer': 'application', 'use': 'name resolution'}},
    "DHCP": {'description': 'Dynamic Host Configuration Protocol', 'annotations': {'port': '67, 68', 'layer': 'application', 'use': 'IP assignment'}},
    "TCP": {'description': 'Transmission Control Protocol', 'annotations': {'layer': 'transport', 'type': 'connection-oriented'}},
    "UDP": {'description': 'User Datagram Protocol', 'annotations': {'layer': 'transport', 'type': 'connectionless'}},
    "WEBSOCKET": {'description': 'WebSocket protocol', 'annotations': {'port': '80, 443', 'layer': 'application', 'use': 'bidirectional communication'}},
    "MQTT": {'description': 'Message Queuing Telemetry Transport', 'annotations': {'port': '1883, 8883', 'layer': 'application', 'use': 'IoT messaging'}},
    "AMQP": {'description': 'Advanced Message Queuing Protocol', 'annotations': {'port': '5672', 'layer': 'application', 'use': 'message queuing'}},
    "GRPC": {'description': 'gRPC Remote Procedure Call', 'annotations': {'transport': 'HTTP/2', 'use': 'RPC framework'}},
}

__all__ = [
    "ImageFileFormatEnum",
    "DocumentFormatEnum",
    "DataFormatEnum",
    "ArchiveFormatEnum",
    "VideoFormatEnum",
    "AudioFormatEnum",
    "ProgrammingLanguageFileEnum",
    "NetworkProtocolEnum",
]