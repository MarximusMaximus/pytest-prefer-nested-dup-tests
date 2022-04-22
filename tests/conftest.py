"""
tests/conftest.py (pytest-prefer-nested-dup-tests)
"""

from typing import (
    Sequence,
    Union,
)

pytest_plugins: Union[str, Sequence[str]] = ["pytester"]
