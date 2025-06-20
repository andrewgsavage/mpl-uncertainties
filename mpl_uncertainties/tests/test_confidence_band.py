#!/usr/bin/env python
# coding: utf-8

# Copyright (c) andrewgsavage.
# Distributed under the terms of the Modified BSD License.

from ..plots import errorbar, boot_odr_band


import numpy as np
import matplotlib.pyplot as plt
from uncertainties import unumpy as unp
import pytest


@pytest.mark.mpl_image_compare
def test_linear_data_and_fit():
    x_val = np.array([0.5, 1.3, 2.1, 3, 4.2, 4.9])
    x_err = x_val * 0.05
    y_val = np.array([0.5, 1.3, 2.1, 3, 4.2, 4.9])
    y_err = y_val * 0.05 + 0.1  # 5% of the reading + 0.1

    x = unp.uarray(x_val, x_err)
    y = unp.uarray(y_val, y_err)

    boot_odr_band(x, y, label='Linear fit')
    errorbar(x, y, linestyle='none', capsize=2)
    plt.legend()
    fig = plt.gcf()
    return fig
