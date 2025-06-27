"""
----------
Linear Fit
----------
We will use ODR for this example (because we have both x_err and y_err)
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
# Confidence Band
# ---------------
# The calc_confidence_band function uses ODR with analytical Delta Method.

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

y_fit = unplt.calc_confidence_band(x, y)

color = unplt.pick_next_color()

# Plot the fit
unplt.plot(x, y_fit, color=color, label="Linear fit")

# Plot 95% confidence band
unplt.fill_between(x, y_fit, color=color, alpha=0.3, label="Linear fit confidence band")

# Plot the data
unplt.errorbar(x, y, linestyle="None", marker=".", capsize=2, label="Linear data")

plt.legend()
plt.grid()
plt.xlabel("x")
plt.ylabel("y")
plt.show()
