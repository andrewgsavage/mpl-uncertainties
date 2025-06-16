# mpl-uncertainties

An Uncertainties package for Matplotlib

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
