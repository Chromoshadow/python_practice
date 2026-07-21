# FT_package

A simple package demonstrating packaging with setuptools.

## From project root :
python -m build

## Usage :
pip install --force-reinstall dist/ft_package-0.0.1.tar.gz
pip uninstall -y ft_package
pip install --force-reinstall dist/ft_package-0.0.1-py3-none-any.whl
pip show -v ft_package
