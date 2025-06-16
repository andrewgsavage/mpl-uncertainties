#!/usr/bin/env python
# coding: utf-8

# Copyright (c) andrewgsavage.
# Distributed under the terms of the Modified BSD License.

from ..plots import errorbar, fit


import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
import pytest


@pytest.mark.mpl_image_compare
def test_errorbar():
    x = np.array(
        [
            ufloat(1.3, 0.16),
            ufloat(2.1, 0.15),
            ufloat(3, 0.22),
            ufloat(4.2, 0.19),
            ufloat(4.9, 0.21),
        ]
    )
    y = np.array(
        [
            ufloat(1.3, 0.16),
            ufloat(2.1, 0.15),
            ufloat(3, 0.22),
            ufloat(4.2, 0.19),
            ufloat(4.9, 0.21),
        ]
    )

    errorbar(x, y)
    fig = plt.gcf()
    return fig

@pytest.mark.mpl_image_compare
def test_fit():
    x = np.array(
        [
            ufloat(1.3, 0.16),
            ufloat(2.1, 0.15),
            ufloat(3, 0.22),
            ufloat(4.2, 0.19),
            ufloat(4.9, 0.21),
        ]
    )
    slope = ufloat(1, 0.2)
    intercept = ufloat(0, 0.2)

    fit(x, slope, intercept)
    fig = plt.gcf()
    return fig