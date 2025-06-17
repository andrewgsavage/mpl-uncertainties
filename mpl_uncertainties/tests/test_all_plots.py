#!/usr/bin/env python
# coding: utf-8

# Copyright (c) andrewgsavage.
# Distributed under the terms of the Modified BSD License.

from ..plots import errorbar, fill_between, plot
from ..helper_functions import odr_linear_regression, calc_confidence_band, pick_next_color

import numpy as np
import matplotlib.pyplot as plt
from uncertainties import unumpy as unp
import pytest


@pytest.mark.mpl_image_compare
def test_plot_all():
    x_val = np.array([0.5, 1.3, 2.1, 3, 4.2, 4.9])
    x_err = x_val * 0.05
    y_val = np.array([0.5, 1.3, 2.1, 3, 4.2, 4.9])
    y_err = y_val * 0.05 + 0.1  # 5% of the reading + 0.1

    x = unp.uarray(x_val, x_err)
    y = unp.uarray(y_val, y_err)

    errorbar(x, y, linestyle='None', marker='.', capsize=2, label='Linear data')

    color = pick_next_color()
    y_fit = calc_confidence_band(x, y)

    plot(x, y_fit, color=color, label='Linear fit')
    fill_between(x, y_fit, color=color, alpha=0.3, label='Linear fit confidence band')

    plt.legend()
    fig = plt.gcf()
    return fig
