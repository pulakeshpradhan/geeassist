# Workflows Module

The `workflows` module provides high-level automated pipelines to perform common tasks with a single function call.

## Automated Mapping

The `auto_process_and_map` function allows you to go from a city name to a publication-quality map in one step.

```python
from geeassist.workflows import auto_process_and_map

# Automatically:
# 1. Finds 'Kolkata' boundary
# 2. Calculates NDVI
# 3. Downloads the GeoTIFF
# 4. Plots it with ggplot2
auto_process_and_map(
    location_name="Kolkata",
    start_date="2022-01-01",
    end_date="2022-01-31",
    output_dir="outputs"
)
```

## API Reference

::: geeassist.workflows
    handler: python
    options:
      members:
        - get_fao_gaul
        - download_ndvi_image
        - auto_process_and_map
