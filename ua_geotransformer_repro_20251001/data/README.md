# Data Access & Integrity

The original notebook references the following input/output artifacts (non-exhaustive):

- `2010_9.tif`
- `2017_9.tif`
- `all_drivers.tif`
- `boundary.shp`
- `builtup.tif`
- `candidate_roofs.geojson`
- `crop.tif`
- `drivers/`
- `elevation.tif`
- `forest.tif`
- `grid_50m.gpkg`
- `landuse_2010.tif`
- `landuse_2017.tif`
- `landuse_2030.tif`
- `landuse_2050.tif`
- `mask.tif`
- `roads.shp`
- `simulated_landuse_2030.tif`
- `simulated_landuse_2050.tif`
- `slope.tif`
- `study_area.shp`
- `suitability.tif`
- `wetland.tif`


## Hosting & Download
- Host large rasters/vectors on Zenodo/OSF and put direct download links here.
- Provide SHA256 checksums for each file to verify integrity.

## Placement
After download, place files under:
```
data/
  raw/
  processed/
```
Update `configs/default.yaml` to point to the correct locations.
