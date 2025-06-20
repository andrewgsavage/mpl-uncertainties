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
from .helper_functions import odr_linear_regression, pred_std_err
from scipy.stats import t


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

def odr_delta_conf_band(
    x,
    y,
    ax=None,
    confidence_interval=0.95,
    err_area_alpha=0.3,
    err_label_suffix=" error",
    *args,
    **kwargs
):
    """
    Plots the confidence band of a model fitted with Orthogonal Distance Regression (ODR) using the analytical Delta Method.
    The band represents the uncertainty in the predicted values due to the covariance of the fitted parameters.
    """
    x_val = unp.nominal_values(x)

    # Pull out the current axes if not passed
    if ax is None:
        ax = plt.gca()

    # Pick a color if not passed
    if 'color' not in kwargs:
        kwargs['color'] = ax._get_lines._cycler_items[ax._get_lines._idx]['color']
        ax._get_lines._idx = (ax._get_lines._idx + 1) % len(ax._get_lines._cycler_items)

    # Calculate the confidance band
    fit = odr_linear_regression(x, y, return_odr_output=True)
    slope, intercept = fit.beta
    y_fit = slope * x_val + intercept

    dof = len(x) - len(fit.beta)
    t_val = t.ppf(1 - (1-confidence_interval)/2, dof)
    y_err = t_val * pred_std_err(x_val, fit.cov_beta)

    lower_band = y_fit - y_err
    upper_band = y_fit + y_err

    # Plot the fit
    fit_plot = ax.plot(x_val, y_fit, *args, **kwargs)

    # Plot confidence band

    if 'label' in kwargs:
        kwargs['label'] += err_label_suffix
    kwargs.setdefault('alpha', err_area_alpha)
    
    err_plot = ax.fill_between(
        x_val,
        lower_band,
        upper_band,
        **kwargs
    )

    return [fit_plot, err_plot]