from pathlib import Path
from io import open
import json

from setuptools import find_packages, setup

ROOT_PATH = Path(__file__).parent
PROJECT_PATH = ROOT_PATH / "bitc0in_twitter"
VERSION_PATH = PROJECT_PATH / "__version__.py"
PIPFILE = ROOT_PATH / "Pipfile.lock"
README_FILE = ROOT_PATH / "README.md"

# Parses pipfile.lock
with open(PIPFILE, encoding="utf-8") as pipfile_lock:
    pipfile_json = json.loads(pipfile_lock.read())
    required_packages = pipfile_json["default"]
    development_packages = pipfile_json["develop"]
    python_version = pipfile_json["_meta"]["requires"]["python_version"]

REQUIRES = []
for package, v in required_packages.items():
    REQUIRES.append(package + v["version"])

EXTRAS_REQUIRES = []
for package, v in development_packages.items():
    EXTRAS_REQUIRES.append(package + v["version"])

with open(README_FILE, encoding="utf-8") as readme_file:
    LONG_DESCRIPTION = "\n" + readme_file.read()

# Package meta-data
NAME = "bitc0in-twitter"
DESCRIPTION = "blah"
URL = "https://github.com/dgnsrekt/bitc0in-twitter"
EMAIL = "dgnsrekt@pm.me"
AUTHOR = "dgnsrekt"
REQUIRES_PYTHON = f">={python_version}"

# Parses version
about = {}
with open(VERSION_PATH) as version_file:
    exec(version_file.read(), about)

setup(
    name=NAME,
    version=about["__version__"],
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(),
    # If your package is a single module, use this instead of 'packages':
    # py_modules=['mypackage'],
    entry_points={"console_scripts": ["bitcoin-twitter=bitc0in_twitter.cli:bitc0in_twitter"]},
    install_requires=REQUIRES,
    extras_require={"dev": EXTRAS_REQUIRES},
    include_package_data=True,
    license="MIT",
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        f"Programming Language :: Python :: {REQUIRES_PYTHON[0]}",
        f"Programming Language :: Python :: {REQUIRES_PYTHON}",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
)
