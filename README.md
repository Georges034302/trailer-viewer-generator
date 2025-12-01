# 🚀 trailer-viewer-generator

This repository contains the automated **Generator** used to build and publish the Trailer Viewer website.

### 🔧 What the Generator Does
- Builds a lightweight **Ubuntu-based Docker environment**
- Installs **Python 3.10**, **pip**, and required libraries such as **PyYAML**
- Executes `trailer.py` to transform **YAML → XML**
- Executes `xsltransformer.py` to transform **XML → HTML** using XSL stylesheets
- Runs `entrypoint.sh` through a GitHub Actions workflow  
  👉 [![Trailer Viewer](https://img.shields.io/badge/Repo-trailer--viewer-blue?style=for-the-badge&logo=github)](https://github.com/Georges034302/trailer-viewer)

---

### 🔄 Automated Build & Deployment

The Generator listens for new commits in the **trailer-viewer** repository.  
Whenever YAML data is updated:

1. GitHub Actions triggers the build pipeline  
2. The Docker container runs the transformation scripts  
3. Updated XML and HTML files are produced  
4. Changes are automatically deployed back to the Trailer Viewer site

This provides a **fully automated YAML → XML → HTML publishing system** with no manual steps required.

---
