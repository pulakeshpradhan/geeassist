import ee
import geeassist as gas

gas.init(project='spatialgeography')

l8 = ee.ImageCollection("LANDSAT/LC09/C02/T1_L2") \
       .filterDate('2022-01-01', '2022-02-01') \
       .first()

masked = gas.utils.mask_clouds_landsat8(l8)
print("Cloud mask applied.")
