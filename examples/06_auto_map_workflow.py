import geeassist as gas
from geeassist.workflows import auto_process_and_map

gas.init(project='spatialgeography')

# Completely automated workflow
# 1. Finds 'Kolkata' in FAO GAUL
# 2. Computes NDVI for Jan 2022
# 3. Downloads GeoTIFF
# 4. Maps it with ggplot2 (needs R installed)

auto_process_and_map(
    location_name="Kolkata", 
    start_date="2022-01-01", 
    end_date="2022-01-31",
    output_dir="kolkata_output",
    use_ggplot=True
)
