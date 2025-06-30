#!/usr/bin/env python
# coding: utf-8

# Copyright (c) andrewgsavage.
# Distributed under the terms of the Modified BSD License.

__all__ = [
    "odr_linear_regression",
    "calc_confidence_band",
    "pick_next_color",
]
import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat, unumpy as unp
from scipy.odr import ODR, Model, RealData
from scipy.stats import t


def odr_linear_regression(
    x, y, initial_slope=1.0, initial_intercept=0.0, return_odr_output=False
):
    """
    Use ODR for linear regression
    """
    x_val = unp.nominal_values(x)
    y_val = unp.nominal_values(y)
    x_err = unp.std_devs(x)
    y_err = unp.std_devs(y)

    if np.any(x_err == 0):
        raise ValueError(
            "One of the x uncertainties is zero, which is invalid for ODR. Please provide uncertanties or consider using a different method"
        )
    if np.any(y_err == 0):
        raise ValueError(
            "One of the y uncertainties is zero, which is invalid for ODR. Please provide uncertanties or consider using a different method"
        )

    def linear_model(B, x_val):
        return B[0] * x_val + B[1]

    fit = ODR(
        RealData(x_val, y_val, sx=x_err, sy=y_err),
        Model(linear_model),
        beta0=[initial_slope, initial_intercept],
    ).run()

    if fit.info > 3:
        fit.pprint()
        raise ValueError("Error calculating fit")

    if return_odr_output:
        return fit
    else:
        fit_slope, fit_intercept = fit.beta
        fit_slope_err, fit_intercept_err = fit.sd_beta

        return ufloat(fit_slope, fit_slope_err), ufloat(
            fit_intercept, fit_intercept_err
        )


def calc_confidence_band(x, y, confidence_interval=0.95):
    """
    Calculate the confidance band using analytical Delta Method
    """
    x_val = unp.nominal_values(x)

    fit = odr_linear_regression(x, y, return_odr_output=True)
    slope, intercept = fit.beta
    y_fit_val = slope * x_val + intercept

    dof = len(x) - len(fit.beta)
    t_val = t.ppf(1 - (1 - confidence_interval) / 2, dof)

    # Analytical Error Propagation Using the Delta Method for Linear Regression
    grad = np.vstack((x_val, np.ones_like(x_val)))  # shape (2, N)
    variances = np.einsum("ij,jk,ik->i", grad.T, fit.cov_beta, grad.T)
    pred_std_err = np.sqrt(variances)
    y_fit_err = t_val * pred_std_err

    return unp.uarray(y_fit_val, y_fit_err)


def pick_next_color(ax=None):
    # Pull out the current axes if not passed
    if ax is None:
        ax = plt.gca()

    color = ax._get_lines._cycler_items[ax._get_lines._idx]["color"]
    ax._get_lines._idx = (ax._get_lines._idx + 1) % len(ax._get_lines._cycler_items)
    return color
