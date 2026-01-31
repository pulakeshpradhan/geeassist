# Publishing Guide

## 1. Publish to PyPI

To publish `geeassistant` to PyPI, follow these steps:

1. **Install build tools**:

    ```bash
    pip install build twine
    ```

2. **Build the package**:

    ```bash
    python -m build
    ```

    This will create `dist/geeassistant-0.1.0-py3-none-any.whl` and `dist/geeassistant-0.1.0.tar.gz`.

3. **Upload to PyPI**:

    ```bash
    twine upload dist/*
    ```

    You will be prompted for your PyPI username and password (or API token).

## 2. Publish Documentation to GitHub Pages

To publish the MkDocs site to GitHub Pages:

1. **Install documentation dependencies**:

    ```bash
    pip install mkdocs mkdocs-material mkdocstrings[python]
    ```

2. **Deploy**:

    ```bash
    mkdocs gh-deploy
    ```

    This command builds the documentation and pushes it to the `gh-pages` branch of your repository.

## 3. GitHub Repository Setup

If you haven't already, push your code to GitHub:

```bash
git remote add origin https://github.com/pulakeshpradhan/geeassistant.git
git branch -M main
git push -u origin main
```
