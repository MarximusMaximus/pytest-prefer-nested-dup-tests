#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding="utf-8").read()


setup(
    name="pytest-prefer-nested-dup-tests",
    author="Marximus Maximus",
    author_email="marximus@marximus.com",
    maintainer="Marximus Maximus",
    maintainer_email="marximus@marximus.com",
    license="MIT",
    url="https://github.com/MarximusMaximus/pytest-prefer-nested-dup-tests",
    description="A Pytest plugin to drop duplicated tests during collection, but prefer nested versions",
    long_description=read("README.rst"),
    py_modules=["pytest_prefer_nested_dup_tests"],
    setup_requires="setuptools_scm",
    use_scm_version=True,
    install_requires=["pytest>=2.7"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Framework :: Pytest",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Testing",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: Implementation :: CPython",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
    entry_points={"pytest11": ["prefer-nested-dup-tests = pytest_prefer_nested_dup_tests",],},
)
