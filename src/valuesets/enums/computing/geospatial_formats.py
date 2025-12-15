"""
Geospatial Data Format Value Sets

File formats commonly used for geospatial and environmental data, including raster formats, vector formats, and scientific data formats with spatial extensions.

Generated from: computing/geospatial_formats.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class GeospatialRasterFormat(RichEnum):
    """
    File formats for raster (gridded) geospatial data including satellite imagery, digital elevation models, and environmental model outputs.
    """
    # Enum members
    GEOTIFF = "GEOTIFF"
    COG = "COG"
    NETCDF = "NETCDF"
    HDF5 = "HDF5"
    HDF_EOS = "HDF_EOS"
    GRIB = "GRIB"
    JPEG2000 = "JPEG2000"
    MRF = "MRF"
    ZARR = "ZARR"
    ENVI = "ENVI"
    ERDAS_IMAGINE = "ERDAS_IMAGINE"
    ASCII_GRID = "ASCII_GRID"

# Set metadata after class creation
GeospatialRasterFormat._metadata = {
    "GEOTIFF": {'description': 'TIFF image format with embedded georeferencing information. Standard format for satellite imagery and raster GIS data.', 'annotations': {'extension': '.tif, .tiff', 'mime_type': 'image/tiff', 'georeferencing': 'embedded', 'organization': 'OGC'}},
    "COG": {'description': 'GeoTIFF optimized for cloud storage with internal tiling and overviews for efficient partial reads over HTTP.', 'annotations': {'extension': '.tif', 'mime_type': 'image/tiff', 'georeferencing': 'embedded', 'features': 'cloud-optimized, COG'}},
    "NETCDF": {'description': 'Network Common Data Form. Self-describing array-oriented scientific data format widely used for climate and environmental data.', 'meaning': 'EDAM:format_3650', 'annotations': {'extension': '.nc, .nc4', 'mime_type': 'application/x-netcdf', 'organization': 'Unidata', 'conventions': 'CF (Climate and Forecast)'}},
    "HDF5": {'description': 'Hierarchical Data Format version 5. High-performance format for large scientific datasets including satellite data.', 'meaning': 'EDAM:format_3590', 'annotations': {'extension': '.h5, .hdf5, .he5', 'mime_type': 'application/x-hdf', 'organization': 'HDF Group'}},
    "HDF_EOS": {'description': 'HDF format extended for NASA Earth Observing System data. Used for MODIS, ASTER, and other NASA satellite products.', 'annotations': {'extension': '.hdf', 'organization': 'NASA', 'variants': 'HDF-EOS2, HDF-EOS5'}},
    "GRIB": {'description': 'GRIdded Binary format. Standard WMO format for meteorological data exchange.', 'annotations': {'extension': '.grib, .grb, .grib2', 'organization': 'WMO', 'versions': 'GRIB1, GRIB2'}},
    "JPEG2000": {'description': 'Wavelet-based image compression format with georeferencing capability. Used for satellite imagery distribution.', 'annotations': {'extension': '.jp2, .j2k', 'mime_type': 'image/jp2', 'features': 'lossy/lossless compression'}},
    "MRF": {'description': 'NASA format optimized for cloud storage and fast random access to large imagery datasets.', 'annotations': {'extension': '.mrf', 'organization': 'NASA', 'features': 'cloud-optimized'}},
    "ZARR": {'description': 'Chunked, compressed, N-dimensional array format designed for cloud storage. Growing adoption for climate data.', 'annotations': {'extension': '.zarr (directory)', 'features': 'cloud-native, chunked', 'python': 'zarr library'}},
    "ENVI": {'description': 'Format used by ENVI remote sensing software. Binary raster with separate header file.', 'annotations': {'extension': '.dat, .bsq, .bil, .bip', 'header': '.hdr'}},
    "ERDAS_IMAGINE": {'description': 'Proprietary format for ERDAS IMAGINE software. Commonly used for satellite imagery processing.', 'annotations': {'extension': '.img', 'organization': 'Hexagon Geospatial'}},
    "ASCII_GRID": {'description': 'Simple text-based raster format. Header followed by space-delimited cell values.', 'annotations': {'extension': '.asc', 'format': 'text', 'organization': 'Esri'}},
}

class GeospatialVectorFormat(RichEnum):
    """
    File formats for vector (point, line, polygon) geospatial data including geographic boundaries, infrastructure, and sampling locations.
    """
    # Enum members
    SHAPEFILE = "SHAPEFILE"
    GEOJSON = "GEOJSON"
    GEOPACKAGE = "GEOPACKAGE"
    KML = "KML"
    KMZ = "KMZ"
    GML = "GML"
    TOPOJSON = "TOPOJSON"
    FLATGEOBUF = "FLATGEOBUF"
    GEOPARQUET = "GEOPARQUET"
    GEODATABASE = "GEODATABASE"
    GPKG_VECTOR = "GPKG_VECTOR"
    WKT = "WKT"
    WKB = "WKB"

# Set metadata after class creation
GeospatialVectorFormat._metadata = {
    "SHAPEFILE": {'description': 'Widely used vector format consisting of multiple files (.shp, .shx, .dbf). De facto standard despite limitations.', 'annotations': {'extension': '.shp (+ .shx, .dbf, .prj)', 'organization': 'Esri', 'limitations': '2GB size limit, 10-char field names'}},
    "GEOJSON": {'description': 'JSON-based format for encoding geographic data structures. Web-friendly and human-readable.', 'annotations': {'extension': '.geojson, .json', 'mime_type': 'application/geo+json', 'organization': 'IETF (RFC 7946)', 'crs': 'WGS84 only'}},
    "GEOPACKAGE": {'description': 'OGC standard SQLite-based format for vector and raster data. Modern replacement for Shapefile.', 'annotations': {'extension': '.gpkg', 'organization': 'OGC', 'features': 'single file, no size limit, transactions'}},
    "KML": {'description': 'Keyhole Markup Language. XML-based format for Google Earth and other applications.', 'annotations': {'extension': '.kml', 'mime_type': 'application/vnd.google-earth.kml+xml', 'organization': 'OGC (originally Google)'}},
    "KMZ": {'description': 'Compressed KML file (ZIP archive containing KML and supporting files).', 'annotations': {'extension': '.kmz', 'mime_type': 'application/vnd.google-earth.kmz', 'compression': 'ZIP'}},
    "GML": {'description': 'Geography Markup Language. OGC XML-based format for geographic features.', 'annotations': {'extension': '.gml', 'mime_type': 'application/gml+xml', 'organization': 'OGC'}},
    "TOPOJSON": {'description': 'Extension of GeoJSON that encodes topology. Smaller file sizes through shared arc representation.', 'annotations': {'extension': '.topojson, .json', 'features': 'topology encoding, smaller files'}},
    "FLATGEOBUF": {'description': 'Binary format optimized for fast streaming and random access. Cloud-native alternative to Shapefile.', 'annotations': {'extension': '.fgb', 'features': 'streaming, spatial index'}},
    "GEOPARQUET": {'description': 'Apache Parquet with geospatial extensions. Columnar format optimized for analytics on large vector datasets.', 'annotations': {'extension': '.parquet', 'features': 'columnar, cloud-optimized'}},
    "GEODATABASE": {'description': 'Esri proprietary format for storing multiple feature classes and tables in a folder structure.', 'annotations': {'extension': '.gdb (folder)', 'organization': 'Esri', 'features': 'multiple layers, domains, relationships'}},
    "GPKG_VECTOR": {'description': 'Vector data stored in GeoPackage format. Can coexist with raster data in same file.', 'annotations': {'extension': '.gpkg', 'organization': 'OGC'}},
    "WKT": {'description': 'Text markup language for representing vector geometry objects.', 'annotations': {'format': 'text', 'organization': 'OGC', 'use': 'geometry representation'}},
    "WKB": {'description': 'Binary equivalent of WKT for efficient storage and transfer.', 'annotations': {'format': 'binary', 'organization': 'OGC'}},
}

__all__ = [
    "GeospatialRasterFormat",
    "GeospatialVectorFormat",
]