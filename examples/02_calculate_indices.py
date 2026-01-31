import ee
import geeassist as gas

gas.init(project='spatialgeography')

# Load a Landsat 8 image (Collection 2)
# Using a filtered collection to ensure we get a valid image without hardcoding fragile IDs
image = ee.ImageCollection("LANDSAT/LC08/C02/T1_TOA") \
          .filterBounds(ee.Geometry.Point(77.5, 12.9)) \
          .filterDate('2022-01-01', '2022-04-01') \
          .first()

# Calculate indices
img_ndvi = gas.indices.calculate_ndvi(image, 'B5', 'B4')
img_ndwi = gas.indices.calculate_ndwi(image, 'B3', 'B5')

print(f"Bands after calc: {img_ndvi.bandNames().getInfo()}")
