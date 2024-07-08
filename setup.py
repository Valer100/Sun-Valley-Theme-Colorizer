from setuptools import setup, find_packages

description = open("README.md", "r").read()

setup(
    name = "sv_ttk_colorizer",
    version = "0.0.6",
    packages = find_packages(),
    install_requires = [
        "darkdetect",
        "Pillow",
        "requests",
        "pywinstyles",
        "sv_ttk",
        "appdirs"
    ],
    entry_points = {
        "console_scripts": [
            "sv_ttk_colorizer = sv_ttk_colorizer:main",
            "sv_ttk_c = sv_ttk_colorizer:main"
        ],
    },
    long_description = description,
    long_description_content_type = "text/markdown"
)