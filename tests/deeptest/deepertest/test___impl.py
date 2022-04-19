from typing import (
    Any,
)

PytestFixture = Any


def test___main(testdir: PytestFixture) -> None:
    testdir = testdir  # ignore unused arg in sig
    assert True
