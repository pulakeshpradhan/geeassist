import ee
import geeassist as gas

gas.init(project='spatialgeography')

l8 = ee.ImageCollection("LANDSAT/LC08/C02/T1_TOA") \
       .filterBounds(ee.Geometry.Point(77.5, 12.9)) \
       .filterDate('2014-01-01', '2014-04-01') \
       .first()

ndvi = gas.indices.calculate_ndvi(l8, 'B5', 'B4', rename='VI')
evi = gas.indices.calculate_evi(l8, 'B5', 'B4', 'B2', rename='VI')

print("Diff calculated.")
