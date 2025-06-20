#!/usr/bin/env python
# coding: utf-8

# Copyright (c) andrewgsavage.
# Distributed under the terms of the Modified BSD License.

__all__ = [
    "odr_linear_regression",
]
import numpy as np
from uncertainties import ufloat, unumpy as unp
from scipy.odr import ODR, Model, RealData

def odr_linear_regression(x, y, initial_slope=1.0, initial_intercept=0.0):
    """
    use ODR for linear regression
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
    fit_slope, fit_intercept = fit.beta
    fit_slope_err, fit_intercept_err = fit.sd_beta

    if fit.info > 3:
        fit.pprint()
        raise ValueError("Error calculating fit")

    fit_slope, fit_intercept = fit.beta
    fit_slope_err, fit_intercept_err = fit.sd_beta

    return ufloat(fit_slope, fit_slope_err), ufloat(fit_intercept, fit_intercept_err)
