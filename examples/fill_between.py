"""
--------------------
Fill between adapter
--------------------

You can pass 2 uncertanties arrays without needing to extract the values:
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
y1 = unp.uarray(y_val, y_err)
y2 = y1 + 1

unplt.fill_between(x, y1, y2, alpha=0.3)

unplt.plot(x, y1)
unplt.plot(x, y2)

plt.grid()
plt.xlabel("x")
plt.ylabel("y")
plt.show()

##############################################################################
# Option 2
# --------
# Alternetavely if you pass a single function then the error area will be plotted:

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

unplt.fill_between(x, y, alpha=0.3)

unplt.plot(x, y)

plt.grid()
plt.xlabel("x")
plt.ylabel("y")
plt.show()
