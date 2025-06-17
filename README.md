# mpl-uncertainties

An Uncertainties package for Matplotlib

## Examples
Simple linear fit example:
```python
import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat, unumpy as unp
import mpl_uncertainties as unplt

x_val = np.array([0.5, 1.3, 2.1, 3, 4.2, 4.9])
x_err = x_val*0.05 # 5% of the reading
y_val = np.array([0.5, 1.3, 2.1, 3, 4.2, 4.9])
y_err = y_val*0.05 # 5% of the reading

x = unp.uarray(x_val, x_err)
y = unp.uarray(y_val, y_err)

slope, intercept = odr_linear_regression(x, y)

unplt.errorbar(x, y, label="Linear data")
unplt.fit(x, slope, intercept, label='Linear fit')

plt.legend()
plt.grid()
plt.show()
```
Result:
TODO upload the real result image when the library will be available
![image of a linear graph (examples/linear_fit.png)](examples/linear_fit.png)

The linear regression thats used:
```python
def odr_linear_regression(x, y, initial_slope=1., initial_intercept=0.):
    """
    use ODR for linear regression
    """
    if np.any(err(x) == 0):
        raise ValueError("One of the x uncertainties is zero, which is invalid for ODR. Please provide uncertanties or consider using a different method")
    if np.any(err(y) == 0):
        raise ValueError("One of the y uncertainties is zero, which is invalid for ODR. Please provide uncertanties or consider using a different method")
        
    def linear_model(B, x_val):
        return B[0] * x_val + B[1]

    x_val = val(x)
    x_err = err(x)
    y_val = val(y)
    y_err = err(y)
    
    fit = ODR(RealData(x_val, y_val, sx=x_err, sy=y_err), Model(linear_model), beta0=[initial_slope, initial_intercept]).run()
    fit_slope, fit_intercept = fit.beta
    fit_slope_err, fit_intercept_err = fit.sd_beta

    if fit.info > 3:
        fit.pprint()
        raise ValueError("Error calculating fit")

    fit_slope, fit_intercept = fit.beta
    fit_slope_err, fit_intercept_err = fit.sd_beta

    return ufloat(fit_slope, fit_slope_err), ufloat(fit_intercept, fit_intercept_err)
```

For for examples documentation please visit:
https://mpl-uncertainties.readthedocs.io/en/latest/examples/

## Installation

You can install using `pip`:

```bash
pip install mpl_uncertainties
```

## Development Installation

```bash
pip install -e ".[dev]"
```

## Install development version with git/pixi

```bash
git clone https://github.com/andrewgsavage/mpl-uncertainties.git
cd mpl-uncertainties

pixi install

# run tests
pixi run test

# generate baseline images for tests
pixi run test_mpl_generate

# build docs
pixi run build-doc
```
