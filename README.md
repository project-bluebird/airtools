# airtools

![example workflow](https://github.com/project-bluebird/airtools/actions/workflows/unit-tests.yml/badge.svg)
[![codecov](https://codecov.io/gh/project-bluebird/airtools/branch/main/graph/badge.svg?token=58uMq5hbNt)](https://codecov.io/gh/project-bluebird/airtools)
![License](https://img.shields.io/github/license/project-bluebird/airtools)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Installation

Clone the repository and install

```{bash}
$ git clone https://github.com/project-bluebird/airtools.git
$ cd ..
$ pip install .
```

## Developer guide

### Dependencies

To install development packages

```{bash}
$ pip install -r requirements-dev.txt
```

This includes packages [black](https://black.readthedocs.io/en/stable/) and [flake8](https://flake8.pycqa.org/en/latest/) for code formatting and checking. Both are used as part of the continuous integration checks. Once installed, they can also run locally

```{bash}
$ black .
$ flake8 .
```

#### Tests

To run unit tests

```{bash}
$ pytest [<optional-arguments>] tests
```

For example, to generate a test coverage report, run

```{bash}
$ pytest --cov=airtools tests/
```

#### Style guide

Docstrings should follow [numpydoc](https://numpydoc.readthedocs.io/en/latest/format.html) convention.
We encourage extensive documentation.

The python code itself should follow [PEP8](https://www.python.org/dev/peps/pep-0008/) convention whenever possible, with at most about 500 lines of code (not including docstrings) per script.
