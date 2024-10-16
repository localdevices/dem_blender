import click
import glob
from pathlib import Path
from typing import Optional

from dem_blender import merge

def print_info(ctx, param, value):
    if not value:
        return {}
    click.echo(f"DEM Blender, Copyright Localdevices, OpenDroneMap.org")
    ctx.exit()

def print_license(ctx, param, value):
    if not value:
        return {}
    click.echo(f"GNU Affero General Public License v3 (AGPLv3). See https://www.gnu.org/licenses/agpl-3.0.en.html")
    ctx.exit()



path_opt = click.option(
    "-p",
    "--path",
    type=click.Path(exists=True, resolve_path=True, dir_okay=True, file_okay=False, path_type=Path),
    help="Path to directory containing terrain models",
    # callback=validate_files_in_dir,  # TODO: write a validator that confirms that all files in folder are valid geospatial raster files
    required=True
)
nodata_val_opt = click.option(
    "-n",
    "--nodata",
    type=click.INT,
    help="Missing value (default: derived from DEM layers)",
    required=False
)
overwrite_opt = click.option(
    "-o",
    "--overwrite",
    is_flag=True,
    default=False,
    help="Force overwriting result if existing"
)
@click.command()
@click.argument(
    'OUTPUT',
    type=click.Path(resolve_path=True, dir_okay=False, file_okay=True, path_type=Path),
    required=True
)
@path_opt
@nodata_val_opt
@overwrite_opt
def cli(
        output: Path,
        path: Path,
        nodata: Optional[int] = None,
        overwrite: Optional[bool] = False
):
    """Single CLI command for blending terrain models."""
    print(f"Input path: {path}")
    print(f"Output path file: {output}")
    print(f"Missing: {nodata}")
    if output.exists():
        if overwrite:
            # remove content
            output.unlink()
        else:
            raise IOError(f"Output path {output} exists. Use -o / --overwrite to force overwriting of file.")
    input_dems = list(path.glob("*.tif"))
    if len(input_dems) == 0:
        print(f"No files with extension .tif found in {path}")
    merge.euclidean_merge_dems(
        output_dem=output,
        input_dems=input_dems,
        nodata=nodata,
    )

