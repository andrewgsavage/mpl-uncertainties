#!/usr/bin/env python
# coding: utf-8

# Copyright (c) andrewgsavage.
# Distributed under the terms of the Modified BSD License.

# Must import __version__ first to avoid errors importing this file during the build process.
# See https://github.com/pypa/setuptools/issues/1724#issuecomment-627241822
from ._version import __version__  # noqa: F401

from .plots import errorbar  # noqa: F401
