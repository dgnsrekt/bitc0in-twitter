import nox
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

REQUIRES = []
for package, v in required_packages.items():
    REQUIRES.append(package + v["version"])


@nox.session(python="3.7")
def tests(session):
    "Running tests."
    for pack in REQUIRES:
        session.install(pack)
    session.install("pytest")
    session.run("pytest", "--disable-warnings")


@nox.session(python="3.7")
def lint(session):
    "Linting using black/flake8"
    session.install("flake8", "flake8-import-order", "black")
    session.run("black", "--line-length", "99", "--check", ".")
    session.run("flake8", "bitc0in_twitter")
