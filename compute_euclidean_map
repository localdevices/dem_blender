import os
import sys
import rasterio
import numpy
import math
import time
import shutil
import glob
import re
from joblib import delayed, Parallel
from opendm.system import run
from opendm import point_cloud
from opendm import io
from opendm import system
from opendm.concurrency import get_max_memory, parallel_map, get_total_memory
from datetime import datetime
from opendm.vendor.gdal_fillnodata import main as gdal_fillnodata
from opendm import log

from .ground_rectification.rectify import run_rectification
from . import pdal

def compute_euclidean_map(geotiff_path, output_path, overwrite=False):
    if not os.path.exists(geotiff_path):
        log.ODM_WARNING("Cannot compute euclidean map (file does not exist: %s)" % geotiff_path)
        return

    nodata = -9999
    with rasterio.open(geotiff_path) as f:
        nodata = f.nodatavals[0]

    if not os.path.isfile(output_path) or overwrite:
        if os.path.isfile(output_path):
            os.remove(output_path)

        log.ODM_INFO("Computing euclidean distance: %s" % output_path)

        if gdal_proximity is not None:
            try:
                gdal_proximity(['gdal_proximity.py', 
                                geotiff_path, output_path, '-values', str(nodata),
                                '-co', 'TILED=YES',
                                '-co', 'BIGTIFF=IF_SAFER',
                                '-co', 'COMPRESS=DEFLATE',
                            ])
            except Exception as e:
                log.ODM_WARNING("Cannot compute euclidean distance: %s" % str(e))

            if os.path.exists(output_path):
                return output_path
            else:
                log.ODM_WARNING("Cannot compute euclidean distance file: %s" % output_path)
        else:
            log.ODM_WARNING("Cannot compute euclidean map, gdal_proximity is missing")
            
    else:
        log.ODM_INFO("Found a euclidean distance map: %s" % output_path)
        return output_path
