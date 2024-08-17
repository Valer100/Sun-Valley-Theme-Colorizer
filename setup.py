from setuptools import setup, find_packages

description = open("README.md", "r", encoding = "utf8").read()

setup(
    name = "sv_ttk_colorizer",
    version = "1.3.2",
    python_requires = ">=3.8",
    license = "MIT",
    author = "Valer100",
    description = "A module for changing the accent color of @rdbende's Sun Valley ttk theme.",
    url = "https://github.com/Valer100/Sun-Valley-Theme-Colorizer",
    project_urls = {
        "Source": "https://github.com/Valer100/Sun-Valley-Theme-Colorizer",
        "Issues": "https://github.com/Valer100/Sun-Valley-Theme-Colorizer/issues",
    },
    packages = find_packages(),
    install_requires = [
        "darkdetect",
        "Pillow",
        "requests",
        "pywinstyles",
        "sv_ttk",
        "appdirs",
        "tkscrollframe"
    ],
    package_data={
        "sv_ttk_colorizer": ["resources/*", "resources/dark/*", "resources/hue_scale/*", "resources/icon/*", "resources/light/*", "resources/theme_switcher/*"]
    },
    entry_points = {
        "console_scripts": [
            "sv_ttk_colorizer = sv_ttk_colorizer:main",
            "sv_ttk_c = sv_ttk_colorizer:main"
        ],
    },
    long_description = description,
    long_description_content_type = "text/markdown",
    classifiers = [
        "Intended Audience :: Developers",
        "Topic :: Software Development :: User Interfaces",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords = [
        "sv-ttk",
        "sv-ttk-colorizer",
        "sv-ttk-c",
        "sv_ttk_colorizer",
        "sv_ttk_c",
        "theme",
        "tk",
        "ttk",
        "tkinter",
        "modern",
        "fluent",
        "dark-theme",
        "sun-valley",
        "windows-11",
        "winui",
    ],
)
