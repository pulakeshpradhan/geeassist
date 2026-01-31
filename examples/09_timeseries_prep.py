import ee
import geeassist as gas

gas.init(project='spatialgeography')

# Simple time series (reduction)
region = ee.Geometry.Point([77.5, 12.9]).buffer(1000)
col = ee.ImageCollection("LANDSAT/LC08/C02/T1_TOA") \
        .filterBounds(region) \
        .filterDate('2020-01-01', '2020-04-01')

def add_ndvi(img):
    return gas.indices.calculate_ndvi(img, 'B5', 'B4')

with_ndvi = col.map(add_ndvi)
print(f"Images in collection: {with_ndvi.size().getInfo()}")
