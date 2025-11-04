"""
tiff_gdal_tools
================
Basic GDAL utility to show information about a GeoTIFF file.
"""

from osgeo import gdal


def tiff_info(tiff_path):
    """Show basic information of a GeoTIFF file."""
    ds = gdal.Open(tiff_path)
    if not ds:
        print("Cannot open file.")
        return
    print("Driver:", ds.GetDriver().ShortName)
    print("Size:", ds.RasterXSize, "x", ds.RasterYSize, "x", ds.RasterCount)
    print("Projection:", ds.GetProjection())
    print("GeoTransform:", ds.GetGeoTransform())


