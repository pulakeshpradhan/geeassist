# Welcome to GEE Assist

**GEE Assist** simplifies your Google Earth Engine (GEE) workflows in Python. Whether you are a beginner looking to learn GEE fundamentals or an expert needing quick utility functions, this package is designed for you.

## Key Features

* **Quick Init**: Handle authentication and initialization in one go.
* **Spectral Indices**: Calculate NDVI, NDWI, EVI, and more with simple function calls.
* **Cloud Masking**: Ready-to-use cloud masking functions for Landsat and Sentinel.
* **Export Helpers**: Streamlined export functions for Images and Tables.

## Quick Start

```python
import geeassist as gas

# Initialize
gas.init()

# Check it works
print(gas.get_info(ee.Number(5)))
```

## Licensing

Distributed under the MIT License. See `LICENSE` for more information.
