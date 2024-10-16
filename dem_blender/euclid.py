import os
import rasterio

from dem_blender import log

try:
    # GDAL >= 3.3
    from osgeo_utils.gdal_proximity import main as gdal_proximity
except ModuleNotFoundError:
    # GDAL <= 3.2
    try:
        from osgeo.utils.gdal_proximity import main as gdal_proximity
    except:
        pass

def compute_euclidean_map(geotiff_path, output_path, overwrite=False, nodata=None):
    if not os.path.exists(geotiff_path):
        log.ODM_WARNING("Cannot compute euclidean map (file does not exist: %s)" % geotiff_path)
        return
    with rasterio.open(geotiff_path) as f:
        nodata = f.nodatavals[0]

    if not os.path.isfile(output_path) or overwrite:
        if os.path.isfile(output_path):
            os.remove(output_path)

        log.ODM_INFO("Computing euclidean distance: %s" % output_path)

        #if gdal_proximity is not None:
        try:
            gdal_proximity(['gdal_proximity.py', 
                            str(geotiff_path), str(output_path), '-values', str(nodata),
                            '-co', 'TILED=YES',
                            '-co', 'BIGTIFF=IF_SAFER',
                            '-co', 'COMPRESS=DEFLATE',
                        ])
        except Exception as e:
            log.ODM_WARNING("What?! Cannot compute euclidean distance: %s" % str(e))

        if os.path.exists(output_path):
            return output_path
        else:
            log.ODM_WARNING("Who?! Cannot compute euclidean distance file: %s" % output_path)
            
    else:
        log.ODM_INFO("Found a euclidean distance map: %s" % output_path)
        return output_path
