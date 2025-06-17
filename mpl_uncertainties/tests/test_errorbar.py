#!/usr/bin/env python
# coding: utf-8

# Copyright (c) andrewgsavage.
# Distributed under the terms of the Modified BSD License.

from ..plots import errorbar, fit


import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat, unumpy as unp
import pytest


@pytest.mark.mpl_image_compare
def test_errorbar():
    x = np.array(
        [
            ufloat(0.5, 0.19),
            ufloat(1.3, 0.16),
            ufloat(2.1, 0.15),
            ufloat(3, 0.22),
            ufloat(4.2, 0.19),
            ufloat(4.9, 0.21),
        ]
    )
    y = np.array(
        [
            ufloat(0.5, 0.19),
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
def test_linear_fit():
    x = np.array(
        [
            ufloat(0.5, 0.19),
            ufloat(1.3, 0.16),
            ufloat(2.1, 0.15),
            ufloat(3, 0.22),
            ufloat(4.2, 0.19),
            ufloat(4.9, 0.21),
        ]
    )
    slope = ufloat(1, 0.2)
    intercept = ufloat(0, 0.2)

    fit(x, slope, intercept, label='Linear fit')
    plt.legend()
    fig = plt.gcf()
    return fig

@pytest.mark.mpl_image_compare
def test_linear_data_and_fit():
    x_val = np.array([0.5, 1.3, 2.1, 3, 4.2, 4.9])
    x_err = x_val*0.05
    y_val = np.array([0.5, 1.3, 2.1, 3, 4.2, 4.9])
    y_err = y_val*0.05 + 0.1 # 5% of the reading + 0.1

    x = unp.uarray(x_val, x_err)
    y = unp.uarray(y_val, y_err)

    slope = ufloat(1, 0.2)
    intercept = ufloat(0, 0.3)

    errorbar(x, y)
    fit(x, slope, intercept, label='Linear fit')
    plt.legend()
    fig = plt.gcf()
    return fig

@pytest.mark.mpl_image_compare
def test_exponential_fit():
    x_val = np.array([0.1, 0.5, 1.3, 2.1])
    x_err = 0.06
    y_val = np.exp(x_val)
    y_err = y_val*0.05

    x = unp.uarray(x_val, x_err)
    y = unp.uarray(y_val, y_err)

    slope = ufloat(1, 0.2)
    intercept = ufloat(0, 0.2)

    fit(x, slope, intercept, label='Exponential fit', mutate=np.exp)
    plt.legend()
    fig = plt.gcf()
    return fig