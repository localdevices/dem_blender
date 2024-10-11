import click
from pathlib import Path
from dem_blender import dem_blender

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
    type=click.Path(exists=True, resolve_path=True, dir_okay=True, file_okay=False),
    help="Path to directory containing terrain models",
    # callback=validate_files_in_dir,  # TODO: write a validator that confirms that all files in folder are valid geospatial raster files
    required=True
)

@click.command()
@click.argument(
    'OUTPUT',
    type=click.Path(resolve_path=True, dir_okay=False, file_okay=True),
    required=True
)
@path_opt
def merge(
        output: Path,
        path: Path,
):
    """Single CLI command for blending terrain models."""
    print(f"Input path: {path}")
    print(f"Output path file: {output}")
    raise NotImplementedError