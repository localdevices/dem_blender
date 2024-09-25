# dem_blender
Blend sets of DEMs by calculating euclidean distance to null values and weighting the combination of elevation models. Based on the split-merge tool within ODM, aka a portable version of [dem-blend](https://github.com/OpenDroneMap/ODM/blob/master/contrib/dem-blend/README.md)

Requirements:
* Directory full of images to blend together
* NoData should be coded as a value of -9999

## Usage

```bash
python dem_blender.py /path/to/directory/with/dems/
```
