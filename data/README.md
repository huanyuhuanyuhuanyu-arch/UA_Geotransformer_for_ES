# Data Access

The dataset accompanying this repository is openly available on Zenodo:

- **Dataset DOI**: https://doi.org/10.5281/zenodo.17251210
- You can download from the DOI page (Files list), or use the direct links below.

## Direct download links

- 2010_9.tif:  https://zenodo.org/records/17251210/files/2010_9.tif?download=1
- 2017_9.tif:  https://zenodo.org/records/17251210/files/2017_9.tif?download=1
- aspect.tif:  https://zenodo.org/records/17251210/files/aspect.tif?download=1
- distance_rail.tif:  https://zenodo.org/records/17251210/files/distance_rail.tif?download=1
- distance_road.tif:  https://zenodo.org/records/17251210/files/distance_road.tif?download=1
- distance_water.tif:  https://zenodo.org/records/17251210/files/distance_water.tif?download=1
- ecoreserve.tif:  https://zenodo.org/records/17251210/files/ecoreserve.tif?download=1
- elevation.tif:  https://zenodo.org/records/17251210/files/elevation.tif?download=1
- pop_density.tif:  https://zenodo.org/records/17251210/files/pop_density.tif?download=1
- runoff.tif:  https://zenodo.org/records/17251210/files/runoff.tif?download=1
- slope.tif:  https://zenodo.org/records/17251210/files/slope.tif?download=1
- wetland.tif:  https://zenodo.org/records/17251210/files/wetland.tif?download=1

## Suggested placement

```
data/
  raw/
    2010_9.tif
    2017_9.tif
    aspect.tif
    distance_rail.tif
    distance_road.tif
    distance_water.tif
    ecoreserve.tif
    elevation.tif
    pop_density.tif
    runoff.tif
    slope.tif
    wetland.tif
  processed/
```

If your local filenames differ, update paths in `configs/default.yaml` or override them in the notebook.

## Metadata (fill with your specifics)
- **CRS**: e.g., `EPSG:28992`
- **Resolution**: e.g., `50 m`
- **Extent**: bounding box of the study area
- **Preprocessing**: clipping, reprojection, resampling, masking, stacking, etc.
- **Intended use**: open reference for readers to understand and reuse inputs aligned with the paper.
