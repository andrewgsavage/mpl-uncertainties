#!/usr/bin/env python
# coding: utf-8

# Copyright (c) andrewgsavage.
# Distributed under the terms of the Modified BSD License.

__all__ = [
    "errorbar",
    "fit",
]
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
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


def fit(x, slope, intercept, ax=None, mutate=lambda y: y, plot_intercept_err=None, x_margin=0.01, x0_proximity=0.2, x_divisions=100, err_area_alpha=0.3, err_label_suffix=" error", *args, **kwargs):
    """
    Plots the fit + area of the slope error + errorbar near 0 of the intercept error.

    mutate: how to mutate the fit (see doc examples for more details).
    plot_intercept_err: wether to plot the intercept error, if None then check if x=0 is in the plotting range.
    x_margin: The margin of x axis, extra % to plot before and after the x range.
    x0_proximity: percentage fron x range length, to check if near x=0, and set min x range to 0.
    x_divisions: Number of points inside x range.
    """
    x_val = unp.nominal_values(x)
    slope_val = unp.nominal_values(slope)
    intercept_val = unp.nominal_values(intercept)
    slope_err = unp.std_devs(slope)
    intercept_err = unp.std_devs(intercept)

    # Pull out the current axes if not passed
    if ax is None:
        ax = plt.gca()
        
    # Pick a color if not passed
    if 'color' not in kwargs:
        kwargs['color'] = ax._get_lines._cycler_items[ax._get_lines._idx]['color']
        ax._get_lines._idx = (ax._get_lines._idx + 1) % len(ax._get_lines._cycler_items)

    # Star/end from x=0 if close to it.
    x_range = [np.min(x_val), np.max(x_val)]
    x_length = x_range[1] - x_range[0]
    if x_range[0] > 0 and x_range[0] - x_length * x0_proximity <= 0:
        x_range[0] = 0
    elif x_range[1] < 0 and x_range[1] + x_length * x0_proximity >= 0:
        x_range[1] = 0

    # Add x range margin
    x_new_range = [x_range[0] - x_length * x_margin, x_range[1] + x_length * x_margin]

    # Adjust the x to make more points for smoother plotting
    new_x = np.linspace(x_new_range[0], x_new_range[1], x_divisions)

    # Plot the fit
    ax.plot(new_x, mutate(new_x*slope_val + intercept_val), *args, **kwargs)

    # Plot error for the intercept
    if 'label' in kwargs:
        kwargs['label'] += err_label_suffix
    if plot_intercept_err == True or (plot_intercept_err == None and x_new_range[0] <= 0 and 0 <= x_new_range[1]):
        mid_y = mutate(intercept_val)
        lower_y = mutate(intercept_val - intercept_err)
        upper_y = mutate(intercept_val + intercept_err)
        lower_err = mid_y - lower_y
        upper_err = upper_y - mid_y

        ax.errorbar(0, mid_y, yerr=[[lower_err], [upper_err]], marker='', elinewidth=2, capsize=4, capthick=2, **kwargs)

    # Plot slope error
    kwargs.setdefault('alpha', err_area_alpha)
    ax.fill_between(new_x, mutate(new_x*(slope_val + slope_err) + intercept_val), mutate(new_x*(slope_val - slope_err) + intercept_val), **kwargs)
