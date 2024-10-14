"""DEM Blender. Seamless merging of Digital Terrain Models with overlap from different sources."""

__version__ = "0.1.0"

from .cli import *
from . import dem_blender

__all__ = [
    "dem_blender",
    "cli"
]
