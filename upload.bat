@echo off
pip install setuptools, wheel, twine
rmdir /q /s dist
python setup.py sdist bdist_wheel
twine upload dist/*
