pytest-prefer-nested-dup-tests - Contributing
=============================================

Contributions will be considered via standard Github Pull Requests.

Development Environment First Time Setup
----------------------------------------

1. Install ``conda`` (tested w/ `miniforge`_)

2. ``cd`` into repo directory.

3. Setup conda environment:

    $ conda env create --name pytest-prefer-nested-dup-tests --file ./conda-environment.yml -v

4. Activate conda env:

    $ conda activate pytest-prefer-nested-dup-tests

5. Install dependencies via poetry:

    $ poetry install

6. Pin poetry based dependencies:

    $ poetry show | awk '{if ($1 !~ /six|packaging|pyparsing/ ) {print "pypi::" $1}}' >"$CONDA_PREFIX"/conda-meta/pinned

Development Environment Updating
--------------------------------

1. Update conda env:

    $ conda env update --name "${MY_DIR_BASENAME}" --file ./conda-environment.yml --prune -v

2. Update additional dependencies via poetry:

    $ poetry install

3. Pin poetry based dependencies:

    $ poetry show | awk '{if ($1 !~ /six|packaging|pyparsing/ ) {print "pypi::" $1}}' >"$CONDA_PREFIX"/conda-meta/pinned


Moving Forward Dependencies' Versions
-------------------------------------

- Conda:

  - Manually update version pins in ``conda-environment.yml``

- Poetry:

  - Option 1: Manually update dependencies in ``pyproject.toml``

  - Option 2: Use ``poetry update`` command.

Testing
-------

A cross-python version test matrix can be run locally with `tox`_:

    $ tox

Current python version only tests can be run locally with `pytest`_:

    $ pytest

.. _`miniforge`: https://github.com/conda-forge/miniforge
.. _`pytest`: https://github.com/pytest-dev/pytest
.. _`tox`: https://tox.readthedocs.org/en/latest/
