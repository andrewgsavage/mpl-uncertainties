"""
------------
Errorbar
------------

A short Errorbar showcasing how to use the library. The docstrings will be
converted to RST by sphinx-gallery.
"""

import numpy as np
import matplotlib.pyplot as plt
import mpl_uncertainties as unplt
from uncertainties import ufloat


x = np.array(
    [
        ufloat(1.3, 0.16),
        ufloat(2.1, 0.15),
        ufloat(3, 0.22),
        ufloat(4.2, 0.19),
        ufloat(4.9, 0.21),
    ]
)
y = np.array(
    [
        ufloat(1.3, 0.16),
        ufloat(2.1, 0.15),
        ufloat(3, 0.22),
        ufloat(4.2, 0.19),
        ufloat(4.9, 0.21),
    ]
)

unplt.errorbar(x, y)
plt.show()
