"""
tests/deeptest/test___impl.py (pytest-prefer-nested-dup-tests)
"""


from typing import (
    Any,
)

PytestFixture = Any


def test___main(testdir: PytestFixture) -> None:
    """
    test___main: simple test to confirm this subpackage of tests loads

    Args:
        testdir (PytestFixture):
    """

    testdir = testdir  # ignore unused arg in sig
    assert True
