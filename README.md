# DEM Blender
DEM Blender is a Command-line utility to blend sets of Digital Terrain Models (DTM)
This is done by calculating euclidean distance to null values and weighting the combination of elevation models. 
Based on the split-merge tool within ODM, aka a portable version of 
[dem-blend](https://github.com/OpenDroneMap/ODM/blob/master/contrib/dem-blend/README.md)

Requirements:

* Directory full of images to blend together

## Installation
```bash
# prepare a virtual environment for this tool, if you have an environment skip this line
# and activate your own environment in the line below.
python3 -m venv .venv/dem_blender
source .venv/dem_blender/bin/activate
# install the tool
pip install .

```

## Usage

Below are the details and examples of how to use DEM Blender CLI. To use it, always first activate
your virtual environment:
```bash
source .venv/dem_blender/bin/activate
```

### Command Syntax

```bash
dem_blender [OPTIONS] OUTPUT
```

- `OUTPUT`: Path to the output file where the blended terrain model will be saved.

### Help

```bash
dem_blender --help
```

Displays help information for the CLI.

### Options

- `-p, --path`: **(required)** Path to the directory containing terrain models.
- `-n, --nodata`: **(optional)** Missing value (default: derived from DEM layers).
- `-o, --overwrite`:  **(optional)** Force overwriting the result if it already exists.

#### Example how to blend Digital Terrain Models (DTM)

1. **Prepare your directory with terrain models**:
   Make sure you have a directory with `.tif` files (terrain models). 

2. **Run the blending command**:

   ```bash
   dem_blender -p /path/to/terrain/models -n -9999 -o /path/to/output/output.tif
   ```

   - `-p /path/to/terrain/models`: Directory containing terrain models.
   - `-n -9999`: Set `0` as the missing value. If not provided, this will default to the first terrain model's missing value
   - `-o`: Force overwrite if the output file exists.
   - `/path/to/output/output.tif`: Path to the output file where the result will be saved.

### Error Handling

If the output file already exists and the `--overwrite` flag is not set, the CLI will raise an error.

```sh
IOError: Output path /path/to/output/output.tif exists. Use -o / --overwrite to force overwriting of file.
```

Make sure to use the `-o` flag if you wish to overwrite existing files.

## License

This project is licensed under the GNU Affero General Public License v3 (AGPLv3). See [GNU AGPLv3](https://www.gnu.org/licenses/agpl-3.0.en.html) for more details.

## Contact

For more information, contact [OpenDroneMap.org](mailto:info@opendronemap.org).