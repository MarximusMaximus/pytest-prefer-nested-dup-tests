pytest-prefer-nested-dup-tests
==============================

by Marximus Maximus (https://www.marximus.com)

.. image:: http://img.shields.io/pypi/v/pytest-prefer-nested-dup-tests.svg
   :target: https://pypi.python.org/pypi/pytest-prefer-nested-dup-tests

.. image:: https://github.com/MarximusMaximus/pytest-prefer-nested-dup-tests/workflows/main/badge.svg
  :target: https://github.com/MarximusMaximus/pytest-prefer-nested-dup-tests/actions

A Pytest plugin to drop duplicated tests during collection, but will prefer keeping nested packages.

By default, when de-duplicating tests, all sub-packages become top level packages. This plugin keeps
the subpackage structure intact.


Installation
------------

You can install via `pip`_ from `PyPI`_::

    $ pip install pytest-prefer-nested-dup-tests


Usage
-----

The plugin is enabled by default, no other action is necessary.


Contributing
------------

Contributions are very welcome. Please see `CONTRIBUTING.rst`_.


License
-------

Distributed under the terms of the `MIT`_ license, "pytest-prefer-nested-dup-tests" is free and open source software.

License file is available at `LICENSE`_ in "plaintext" (ASCII (ASCII-7), Extended ASCII (ASCII-8), Latin-1,
Windows-1252, and UTF-8 compatible format).


Issues
------

If you encounter any problems, please `file an issue`_ along with a detailed description.


Changelog
---------

Please see `CHANGELOG.rst`_.


Like My Work & Want To Support It?
----------------------------------

- Main Website: https://www.marximus.com
- Patreon (On Going Support): https://www.patreon.com/marximus
- Ko-fi (One Time Tip): https://ko-fi.com/marximusmaximus


.. _`CHANGELOG.rst`: https://github.com/MarximusMaximus/pytest-prefer-nested-dup-tests/blob/main/CHANGELOG.rst
.. _`CONTRIBUTING.rst`: https://github.com/MarximusMaximus/pytest-prefer-nested-dup-tests/blob/main/CONTRIBUTING.rst
.. _`file an issue`: https://github.com/MarximusMaximus/pytest-prefer-nested-dup-tests/issues
.. _`LICENSE`: https://github.com/MarximusMaximus/pytest-prefer-nested-dup-tests/blob/main/LICENSE
.. _`MIT`: http://opensource.org/licenses/MIT
.. _`pip`: https://pypi.python.org/pypi/pip/
.. _`PyPI`: https://pypi.python.org/pypi
