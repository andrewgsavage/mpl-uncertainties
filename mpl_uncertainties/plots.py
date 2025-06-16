#!/usr/bin/env python
# coding: utf-8

# Copyright (c) andrewgsavage.
# Distributed under the terms of the Modified BSD License.

__all__ = [
    "errorbar",
]
import matplotlib.pyplot as plt
from uncertainties import unumpy as unp

def errorbar(x, y, ax=None, *args, **kwargs):
    """
    Plots errorbar from x,y
    """
    x_val = unp.nominal_values(x)
    y_val = unp.nominal_values(y)
    x_err = unp.std_devs(x)
    y_err = unp.std_devs(y)

    # Pull out the current axes if not passed
    if ax is None:
        ax = plt.gca()

    # Plot the errorbar
    return ax.errorbar(x_val, y_val, xerr=x_err, yerr=y_err, *args, **kwargs)