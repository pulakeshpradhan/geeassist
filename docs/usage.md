# User Guide

## Initialization

Before using GEE functionalities, you must initialize the library. `geeassist` handles the standard `ee.Initialize()` call and can trigger authentication if needed.

```python
import geeassist as gas

# Simple init
gas.init()

# Init with a specific project
gas.init(project='my-gee-project')
```

## Calculating Indices

One of the most common tasks in remote sensing is calculating spectral indices.

### NDVI

Normalized Difference Vegetation Index (NDVI) is used to quantify vegetation greenness.

```python
import ee
import geeassist as gas

# Load a Landsat 8 image
image = ee.Image('LANDSAT/LC08/C01/T1_TOA/LC08_044034_20140318')

# Calculate NDVI (B5 is NIR, B4 is Red for Landsat 8)
ndvi_image = gas.indices.calculate_ndvi(image, nir_band='B5', red_band='B4')

# The resulting image has a new band named 'NDVI'
print(ndvi_image.bandNames().getInfo())
```

### NDWI

Normalized Difference Water Index (NDWI) is useful for water body mapping.

```python
# Calculate NDWI (B3 is Green, B5 is NIR for Landsat 8)
ndwi_image = gas.indices.calculate_ndwi(image, green_band='B3', nir_band='B5')
```

## Cloud Masking

`geeassist` provides helpers to mask clouds.

```python
# Function to mask clouds for Landsat 8
masked_image = gas.utils.mask_clouds_landsat8(image)
```

## Exporting Data

Exporting images to Google Drive is simplified.

```python
# Define a region of interest
geometry = ee.Geometry.Rectangle([77, 12, 78, 13])

# Export
gas.utils.export_image_to_drive(
    image=ndvi_image.select('NDVI'),
    description='ndvi_export_example',
    folder='GEE_Exports',
    region=geometry,
    scale=30
)
```
