#!/usr/bin/env python
# coding: utf-8

# Copyright (c) andrewgsavage.
# Distributed under the terms of the Modified BSD License.

__all__ = [
    "errorbar",
]
import numpy as np
import uncertainties as un
import matplotlib.pyplot as plt


def errorbar(ux, uy, *args, **kwargs):
    return plt.errorbar([a.n for a in ux], [a.n for a in uy], [a.s for a in ux], [a.s for a in uy], *args, **kwargs)