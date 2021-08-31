from setuptools import setup, find_packages

NAME = "airtools"
REQUIRES_PYTHON = ">=3.6.0"
VERSION = None
LONG_DESCRIPTION = open("./README.md", "r").read()

# Get dependencies from requirements.txt
# Source dependencies from requirements.txt file.
try:
    with open("requirements.txt", "r") as f:
        lines = f.readlines()
        REQUIRED_PACKAGES = [line.strip() for line in lines]
except FileNotFoundError:
    REQUIRED_PACKAGES = []

# load package's version from __version__.py module
# version information
MAJOR = 0
MINOR = 1
MICRO = 0
version = "{}.{}.{}".format(MAJOR, MINOR, MICRO)

setup(
    name=NAME,
    version=version,
    description="Utils for Project Bluebird",
    long_description=LONG_DESCRIPTION,
    long_description_concent_type="text/markdown",
    author="Project BlueBird",
    python_requires=REQUIRES_PYTHON,
    url="https://github.com/project-bluebird/airtools",
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    install_requires=REQUIRED_PACKAGES,
    include_package_data=True,  # include items specified in MANIFEST.in
    license="MIT",
)
