import geeassist as gas
import ee

# 1. Initialize
gas.init(project='spatialgeography')

# 2. Check info of a simple object
n = gas.get_info(ee.Number(5))
print(f"Number from GEE: {n}")
