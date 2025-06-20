from os import path

from setuptools import setup

# extract version
path = path.realpath("mpl_uncertainties/_version.py")
version_ns = {}
with open(path, encoding="utf8") as f:
    exec(f.read(), {}, version_ns)
version = version_ns["__version__"]

setup_args = dict(
    version=version,
)

if __name__ == "__main__":
    setup(**setup_args)
