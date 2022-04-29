# pytest-prefer-nested-dup-tests

by Marximus Maximus (<https://www.marximus.com>)

<p align="center">
<!-- <a href=""><img alt="" src=""></a> -->
<a href="https://github.com/MarximusMaximus/pytest-prefer-nested-dup-tests/actions"><img alt="Test Status" src="https://github.com/MarximusMaximus/pytest-prefer-nested-dup-tests/workflows/main/badge.svg"></a>
<!-- TODO: coveralls.io
<a href="https://coveralls.io/github/MarximusMaximus/pytest-prefer-nested-dup-tests?branch=main"><img alt="Coverage Status" src="https://coveralls.io/repos/github/MarximusMaximus/pytest-prefer-nested-dup-tests/badge.svg?branch=main"></a> -->
<!-- TODO: readthedocs.org
<a href="https://pytest-prefer-nested-dup-tests.readthedocs.io/en/stable/?badge=stable"><img alt="Documentation Status" src="https://readthedocs.org/projects/pytest-prefer-nested-dup-tests/badge/?version=stable"></a> -->
<!-- TODO: readthedocs.org license
<a href="https://github.com/MarximusMaximus/pytest-prefer-nested-dup-tests/blob/main/LICENSE"><img alt="License: MIT" src="https://pytest-prefer-nested-dup-tests.readthedocs.io/en/stable/_static/license.svg"></a> -->
<a href="https://pypi.python.org/pypi/pytest-prefer-nested-dup-tests"><img alt="PyPI Version" src="http://img.shields.io/pypi/v/pytest-prefer-nested-dup-tests.svg"></a>
<a href="https://pepy.tech/project/pytest-prefer-nested-dup-tests"><img alt="Downloads" src="https://pepy.tech/badge/pytest-prefer-nested-dup-tests"></a>
<!-- TODO: conda-forge
<a href="https://anaconda.org/conda-forge/pytest-prefer-nested-dup-tests/"><img alt="conda-forge" src="https://img.shields.io/conda/dn/conda-forge/pytest-prefer-nested-dup-tests.svg?label=conda-forge"></a> -->
</p>

<p align="center">
<a href="https://github.com/pre-commit/pre-commit"><img alt="pre-commit" src="https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white"></a>
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
<!-- TODO: #8 isort
<a href="https://pycqa.github.io/isort/"><img alt="isort" src="https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336"></a> -->
</p>

A Pytest plugin to drop duplicated tests during collection, but will prefer keeping nested packages.

By default, when de-duplicating tests, all sub-packages become top level packages. This plugin keeps
the subpackage structure intact.

## Installation

You can install via [pip] from [PyPI]:

    $ pip install pytest-prefer-nested-dup-tests

## Usage

The plugin is enabled by default, no other action is necessary.

## Contributing

Contributions are very welcome. Please see [CONTRIBUTING.rst].

## License

Distributed under the terms of the [MIT] license, "pytest-prefer-nested-dup-tests" is free and open source software.

License file is available at[LICENSE] in "plaintext" (ASCII (ASCII-7), Extended ASCII (ASCII-8), Latin-1,
Windows-1252, and UTF-8 compatible format).

## Issues

If you encounter any problems, please [file an issue] along with a detailed description.

## Changelog

Please see [CHANGELOG.rst].

## Like My Work & Want To Support It?

- Main Website: <https://www.marximus.com>
- Patreon (On Going Support): <https://www.patreon.com/marximus>
- Ko-fi (One Time Tip): <https://ko-fi.com/marximusmaximus>

[CHANGELOG.rst]: https://github.com/MarximusMaximus/

[CONTRIBUTING.rst]: https://github.com/MarximusMaximus/pytest-prefer-nested-dup-tests/blob/main/CONTRIBUTING.rst
[file an issue]: https://github.com/MarximusMaximus/pytest-prefer-nested-dup-tests/issues
[LICENSE]: https://github.com/MarximusMaximus/pytest-prefer-nested-dup-tests/blob/main/LICENSE
[MIT]: http://opensource.org/licenses/MIT
[pip]: https://pypi.python.org/pypi/pip/
[PyPI]: https://pypi.python.org/pypi
