@echo off
rmdir /q /s dist
python setup.py sdist bdist_wheel
twine upload dist/*