import ee
import geeassist as gas
from geeassist.workflows import get_fao_gaul

gas.init(project='spatialgeography')

# Get geometry for Kolkata
kolkata_geom = get_fao_gaul("Kolkata", level=2)

print("Kolkata Geometry found.")
info = kolkata_geom.getInfo()
print(f"Type: {info['type']}")
