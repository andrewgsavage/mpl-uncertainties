#!/usr/bin/env python
# coding: utf-8

# Copyright (c) andrewgsavage.
# Distributed under the terms of the Modified BSD License.

__all__ = [
    "errorbar",
    "fill_between",
    "plot",
]
import matplotlib.pyplot as plt
from uncertainties import unumpy as unp


def errorbar(x, y, ax=None, *args, **kwargs):
    """
    Adapter function for plt.errorbar
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


def fill_between(x, y1, y2=None, ax=None, *args, **kwargs):
    """
    Adapter function for plt.fill_between
    If y2 is not passed then will plot the erea of y1 error
    """
    x_val = unp.nominal_values(x)
    if y2 is None:
        y_val = unp.nominal_values(y1)
        y_err = unp.std_devs(y1)
        lower_band = y_val - y_err
        upper_band = y_val + y_err
    else:
        lower_band = unp.nominal_values(y1)
        upper_band = unp.nominal_values(y2)

    # Pull out the current axes if not passed
    if ax is None:
        ax = plt.gca()

    # Plot confidence band
    return ax.fill_between(x_val, lower_band, upper_band, *args, **kwargs)


def plot(x, y, ax=None, *args, **kwargs):
    """
    Adapter function for plt.plot
    """
    x_val = unp.nominal_values(x)
    y_val = unp.nominal_values(y)

    # Pull out the current axes if not passed
    if ax is None:
        ax = plt.gca()

    # Plot the fit
    return ax.plot(x_val, y_val, *args, **kwargs)
