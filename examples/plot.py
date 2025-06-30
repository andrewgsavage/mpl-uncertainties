"""
------------
Plot adapter
------------

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

# Plot the fit
unplt.plot(x, y)

plt.grid()
plt.xlabel("x")
plt.ylabel("y")
plt.show()
