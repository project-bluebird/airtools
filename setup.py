import os
import io

from setuptools import setup, find_packages

# Get dependencies from requirements.txt
with open(os.path.join(SETUP_DIR, "requirements.txt"), "r") as f:
    REQUIRED_PACKAGES = f.read().splitlines()

here = os.path.abspath(os.path.dirname(__file__))
try:
    with io.open(os.path.join(here, "README.md"), encoding="utf-8") as f:
        long_description = "\n" + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

# TODO: load package's version from __version__.py module
about = {}
if not VERSION:
    project_slug = NAME.lower().replace("-", "_").replace(" ", "_")
    with open(os.path.join(here, project_slug, "__version__.py")) as f:
        exec(f.read(), about)
else:
    about["__version__"] = VERSION

setup(
    name="airtools",
    version=about['__version__'],
    description="Utils for Project Bluebird",
    long_description=long_description,
    long_description_concent_type="text/markdown",
    author="Project BlueBird",
    python_requires=REQUIRES_PYTHON,
    url="https://github.com/project-bluebird/airtools",
    packages=find_packages(
        exclude=["tests", "*.tests", "*.tests.*", "tests.*"]
    ),
    install_requires=REQUIRED,
    include_package_data=True, # include items specified in MANIFEST.in
    license="MIT"
)
