"""
---------------
Confidence Band
---------------

A function confidence band plot with uncertainties.

We will use ODR for this example (because we have both x_err and y_err)
"""

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


##############################################################################
# Linear Fit
# ----------
# Plotting linear fit of the data:

import numpy as np
import matplotlib.pyplot as plt
import mpl_uncertainties as unplt
from uncertainties import ufloat, unumpy as unp

x_val = np.array([0.053, 0.551, 1.624, 1.952, 3.205])
x_err = x_val * 0.05 + 0.05  # 5% + 0.05
y_val = np.array([0.1, 0.3, 2, 2.343, 3.775])
y_err = y_val * 0.05 + 0.05  # 5% + 0.05

x = unp.uarray(x_val, x_err)
y = unp.uarray(y_val, y_err)

slope, intercept = odr_linear_regression(x, y)

# Plotting
unplt.errorbar(x, y, label='Linear data', marker='.', linestyle='', capsize=2)
unplt.confidence_band(x, slope, intercept, label='Linear fit')

plt.legend()
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.show()

##############################################################################
# None Linear Fit
# ---------------
# Assuming the data goes exponantially to x.
# We will first do ln(y) to get linear ratio between x and y, because its the best method of keeping proper error esimation.
# After finding linear correlation (slope and intercept) between x and ln(y) we will plot the fit using the `mutate` variable:

x_val = np.array([0.053, 0.127, 0.227, 0.345, 0.551, 0.923, 0.993, 1.624, 1.952, 3.205])
x_err = 0.06
y_val = np.array(
    [1.616, 0.954, 1.351, 2.447, 1.778, 2.562, 2.918, 5.134, 8.979, 21.649]
)
y_err = y_val * 0.05

x = unp.uarray(x_val, x_err)
y = unp.uarray(y_val, y_err)
ln_y = unp.log(y)

slope, intercept = odr_linear_regression(x, ln_y)

# Plotting
unplt.errorbar(x, y, label='Linear data', linestyle='', capsize=2)
unplt.confidence_band(x, slope, intercept, label='Linear fit', mutate=np.exp)

plt.legend()
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.show()

##############################################################################
# confidence_band() Parameters
# ----------------------------
# x:
#     the x of the graph, it can be numpy array or array of uncertainties values.
# slope:
#     ``ufloat`` or ``float`` slope of the linear regression.
# intercept:
#     ``ufloat`` or ``float`` intercept of the linear regression.
# ax=None:
#     the axes where to plot the graph. if not specified then ``plt`` is used.
# mutate=lambda y: y:
#     function to mutate the fit.
# plot_intercept_err=None:
#     wether to plot the intercept error, if None then check if x=0 is in the plotting range.
# x_margin=0.01:
#     The margin of x axis, extra % to plot before and after the x range.
# x0_proximity=0.2:
#     percentage fron x range length, to check if near x=0, and set min x range to 0.
# x_divisions=100:
#     Number of points inside x range.
# err_area_alpha=0.3:
#     color alpha (transparancy) of the error area.
# err_label_suffix=" error":
#     suffix for the error area label (error label = label + err_label_suffix).
