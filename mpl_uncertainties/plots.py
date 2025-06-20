#!/usr/bin/env python
# coding: utf-8

# Copyright (c) andrewgsavage.
# Distributed under the terms of the Modified BSD License.

__all__ = [
    "errorbar",
    "boot_odr_band",
]
import numpy as np
import matplotlib.pyplot as plt
from uncertainties import unumpy as unp
from .helper_functions import odr_linear_regression


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

def boot_odr_band(
    x,
    y,
    ax=None,
    confidence_interval=0.95,
    x_margin=0.01,
    err_area_alpha=0.3,
    err_label_suffix=" error",
    x_divisions=100,
    n_bootstrap=1000,
    *args,
    **kwargs
):
    """
    Bootstrap ODR confidence band
    Plots the confidance band using bootstrap and odr.

    """
    x_val = unp.nominal_values(x)
    x_err = unp.std_devs(x)
    y_err = unp.std_devs(y)

    lower_percentile = (1-confidence_interval)/2
    upper_percentile = 1-lower_percentile

    # Pull out the current axes if not passed
    if ax is None:
        ax = plt.gca()

    # Pick a color if not passed
    if 'color' not in kwargs:
        kwargs['color'] = ax._get_lines._cycler_items[ax._get_lines._idx]['color']
        ax._get_lines._idx = (ax._get_lines._idx + 1) % len(ax._get_lines._cycler_items)

    # Add x range margin
    x_range = [np.min(x_val), np.max(x_val)]
    x_length = x_range[1] - x_range[0]
    x_range = [x_range[0] - x_length * x_margin, x_range[1] + x_length * x_margin]

    # Adjust the x to make more points for smoother plotting
    x_fit = np.linspace(x_range[0], x_range[1], x_divisions)
    y_fits = []

    # bootstrap
    for _ in range(n_bootstrap):
        x_sample = x + np.random.normal(0, x_err)
        y_sample = y + np.random.normal(0, y_err)
        slope, intercept = odr_linear_regression(x_sample, y_sample)
        y_fits.append(slope.n * x_fit + intercept.n)
    y_fits = np.array(y_fits)

    lower_y = np.percentile(y_fits, lower_percentile, axis=0)
    upper_y = np.percentile(y_fits, upper_percentile, axis=0)

    # Plot the fit
    slope, intercept = odr_linear_regression(x, y)
    fit_plot = ax.plot(x_fit, slope.n * x_fit + intercept.n, *args, **kwargs)

    # Plot confidence band

    if 'label' in kwargs:
        kwargs['label'] += err_label_suffix
    kwargs.setdefault('alpha', err_area_alpha)
    
    err_plot = ax.fill_between(
        x_fit,
        lower_y,
        upper_y,
        **kwargs
    )

    return [fit_plot, err_plot]