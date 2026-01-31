# Installation

## Prerequisites

- Python 3.7 or higher
- A Google Earth Engine account
- **Optional (for advanced plotting):**
  - R installation (v4.0+)
  - R packages: `ggplot2`, `tmap`, `ggspatial`, `sf`, `dplyr`

## Install via pip

You can install `geeassist` directly from PyPI (once published):

```bash
pip install geeassist
```

## Install from Source

To install the latest development version from GitHub:

```bash
git clone https://github.com/pulakeshpradhan/geeassist.git
cd geeassist
pip install .
```

## Verify Installation

To verify that the package is installed correctly, open a Python shell and run:

```python
import geeassist
print(geeassist.__version__)
```
