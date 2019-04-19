from pathlib import Path
from io import open
import json

ROOT_PATH = Path(__file__).parent
PIPFILE = ROOT_PATH / "Pipfile.lock"

# Parses pipfile.lock
with open(PIPFILE, encoding="utf-8") as pipfile_lock:
    pipfile_json = json.loads(pipfile_lock.read())
    required_packages = pipfile_json["default"]
    development_packages = pipfile_json["develop"]
    python_version = pipfile_json["_meta"]["requires"]["python_version"]


# Package meta-data
NAME = ROOT_PATH.name
EMAIL = "dgnsrekt@pm.me"
AUTHOR = "dgnsrekt"
REQUIRES_PYTHON = f">={python_version}"
