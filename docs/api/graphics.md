# Graphics Module

The `graphics` module provides high-level wrappers around R's powerful plotting libraries (`ggplot2`, `tmap`) to create publication-quality maps directly from Python.

!!! warning "Requirement"
    This module requires **R** to be installed on your system.
    It also requires the `rpy2` Python package, which is installed automatically with `geeassistant`.
    The R packages `ggplot2`, `tmap`, `ggspatial`, `sf`, and `dplyr` must be installed in your R environment.

## Usage

```python
import geeassist as gas
import geopandas as gpd

# 1. Check if R environment is ready
ready, msg = gas.graphics.check_r_environment()
if not ready:
    print(msg)
    # gas.graphics.install_r_packages() # Run this once if needed

# 2. Prepare Data (e.g., from a Shapefile or GEE export)
gdf = gpd.read_file('path/to/my_data.shp')

# 3. Create a static map with ggplot2
gas.graphics.ggplot_map(
    data=gdf,
    title="Vegetation Index Map",
    output_file="ndvi_map.png"
)

# 4. Create a thematic map with tmap
gas.graphics.tmap_map(
    data=gdf,
    title="Reference Map",
    output_file="ref_map.png"
)
```

## API Reference

::: geeassist.graphics
    handler: python
    options:
      members:
        - check_r_environment
        - install_r_packages
        - ggplot_map
        - tmap_map
