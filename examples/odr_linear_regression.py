"""
---------------------
ODR linear regression
---------------------

This function uses ODR to include both xerr and yerr in order to calculate the linear regression:
"""

import numpy as np
import matplotlib.pyplot as plt
import mpl_uncertainties as unplt
from uncertainties import unumpy as unp

x_val = np.array([0.053, 0.551, 1.624, 1.952, 3.205])
x_err = x_val * 0.05 + 0.05  # 5% + 0.05
y_val = np.array([0.1, 0.3, 2, 2.343, 3.775])
y_err = y_val * 0.05 + 0.05  # 5% + 0.05

x = unp.uarray(x_val, x_err)
y = unp.uarray(y_val, y_err)

slope, intercept = unplt.odr_linear_regression(x, y)
y_fit = slope * x + intercept

# Plot the fit
unplt.plot(x, y_fit)

# Plot the data
unplt.errorbar(x, y, linestyle="None", marker=".", capsize=2, label="Linear data")

plt.legend()
plt.grid()
plt.xlabel("x")
plt.ylabel("y")
plt.show()

##############################################################################
# Option 2
# --------
# Alternetavely you can receive the beta/fit results of the odr calculations:

import numpy as np
import matplotlib.pyplot as plt
import mpl_uncertainties as unplt
from uncertainties import unumpy as unp
from uncertainties import ufloat

x_val = np.array([0.053, 0.551, 1.624, 1.952, 3.205])
x_err = x_val * 0.05 + 0.05  # 5% + 0.05
y_val = np.array([0.1, 0.3, 2, 2.343, 3.775])
y_err = y_val * 0.05 + 0.05  # 5% + 0.05

x = unp.uarray(x_val, x_err)
y = unp.uarray(y_val, y_err)

fit = unplt.odr_linear_regression(
    x, y, initial_slope=1.0, initial_intercept=0.0, return_odr_output=True
)

fit_slope, fit_intercept = fit.beta
fit_slope_err, fit_intercept_err = fit.sd_beta
slope = ufloat(fit_slope, fit_slope_err)
intercept = ufloat(fit_intercept, fit_intercept_err)

y_fit = slope * x + intercept

# Plot the fit
unplt.plot(x, y_fit)

# Plot the data
unplt.errorbar(x, y, linestyle="None", marker=".", capsize=2, label="Linear data")

plt.legend()
plt.grid()
plt.xlabel("x")
plt.ylabel("y")
plt.show()
