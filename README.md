# trailer-viewer-generator
This Generator repo
* Installs and runs ubuntu on Docker
* Installs Python3.10 python3-pip and PyYAML
* Runs trailer.py to transform YAML to XML
* Runs xsltransformer.py to transform the generated XML to HTML using XSL technology and Python
* Runs entrypoint.sh to initiate and push to 👉 [![Trailer Viewer](https://img.shields.io/badge/Repo-trailer--viewer-blue?style=for-the-badge&logo=github)](https://github.com/Georges034302/trailer-viewer)

``The Generator detects new commits in trailer-viewer repo and automatically deploy the changes using GitHub actions``
