#!/usr/bin/env python
# coding: utf-8

# Copyright (c) andrewgsavage.
# Distributed under the terms of the Modified BSD License.

__all__ = [
    "errorbar",
]
import matplotlib.pyplot as plt
import numpy as np
from uncertainties import unumpy as unp, UFloat

def errorbar(x, y, ax=None, **kwargs):
    """
    Plots errorbar from x,y
    """
    if not isinstance(x, np.ndarray) or not np.all([isinstance(x_i, UFloat) for x_i in x]):
        raise TypeError("x must be numpy arrays (np.ndarray) of uncertainties floats (UFloat)")
    if not isinstance(y, np.ndarray) or not np.all([isinstance(y_i, UFloat) for y_i in y]):
        raise TypeError("y must be numpy arrays (np.ndarray) of uncertainties floats (UFloat)")

    # Pull out the current axes if not passed (only after this function began running)
    if ax is None:
        ax = plt.gca()

    # Plot the errorbar
    kwargs.setdefault('marker', '.')
    kwargs.setdefault('linestyle', '')
    kwargs.setdefault('capsize', 2)
    ax.errorbar(unp.nominal_values(x), unp.nominal_values(y), xerr=unp.std_devs(x), yerr=unp.std_devs(y), **kwargs)