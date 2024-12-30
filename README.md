<div align="center">
  <img width=700 src="https://github.com/Valer100/Sun-Valley-Theme-Colorizer/blob/main/screenshots/image_hero_dark.png?raw=true"/>
</div>

# Sun Valley Theme Colorizer

[![PyPI](https://img.shields.io/pypi/v/sv_ttk_colorizer)](https://pypi.org/project/sv_ttk_colorizer/)
[![Downloads](https://img.shields.io/pepy/dt/sv_ttk_colorizer)](https://pypi.org/project/sv_ttk_colorizer/)
[![Stars](https://img.shields.io/github/stars/Valer100/Sun-Valley-Theme-Colorizer?style=flat&color=yellow)]()
[![Contributors](https://img.shields.io/github/contributors/Valer100/Sun-Valley-Theme-Colorizer)](https://github.com/Valer100/Sun-Valley-Theme-Colorizer/graphs/contributors)
[![Last commit](https://img.shields.io/github/last-commit/Valer100/Sun-Valley-Theme-Colorizer)](https://github.com/Valer100/Sun-Valley-Theme-Colorizer/commits/main)
[![Commits since latest release](https://img.shields.io/github/commits-since/Valer100/Sun-Valley-Theme-Colorizer/latest)](https://github.com/Valer100/Sun-Valley-Theme-Colorizer/commits/main)
[![License](https://img.shields.io/github/license/Valer100/Sun-Valley-Theme-Colorizer)](https://github.com/Valer100/Sun-Valley-Theme-Colorizer/blob/main/LICENSE)

This Python module allows you to change the accent color of [@rdbende](https://github.com/rdbende)'s [Sun Valley ttk theme](https://github.com/rdbende/Sun-Valley-ttk-theme) and to apply other tweaks and improvements without the need to manually download the theme from GitHub, change the hue of the spritesheet files and change some colors in the tcl files. This module does everything for you.

## 📦 How to install
Run this command in your terminal:
```
pip install sv_ttk_colorizer
```

To launch the module, run this command in your terminal:
```
sv_ttk_colorizer
```

... or even shorter:
```
sv_ttk_c
```

If all the commands above didn't work, try this one (it looks like your Python installation's ```Scripts``` folder is not on your PATH):
```
python -m sv_ttk_colorizer
```

## 📋 Requirements
- 🐍 Python 3.8 or newer (like the theme)

## 🤔 What's this module doing?
At your choice, this package downloads the theme from GitHub or copies it from site-packages, then it changes the hue of the spritesheet images, changes some colors in ```light.tcl``` and ```dark.tcl``` and then it gives you the modified theme in a folder named ```sv_ttk``` that you have to move to the root folder of your project. You don't need to make any changes to your code.

## 📸 Screenshots
<details>
  <summary>Windows</summary>
  <br>
  <img src="https://raw.githubusercontent.com/Valer100/Sun-Valley-Theme-Colorizer/main/screenshots/screenshot_dark_win.png"/>
  <br><br>
  <img src="https://raw.githubusercontent.com/Valer100/Sun-Valley-Theme-Colorizer/main/screenshots/screenshot_light_win.png"/>
</details>
<details>
  <summary>Linux</summary>
  <br>
  <img src="https://raw.githubusercontent.com/Valer100/Sun-Valley-Theme-Colorizer/main/screenshots/screenshot_dark_linux.png"/>
  <br><br>
  <img src="https://raw.githubusercontent.com/Valer100/Sun-Valley-Theme-Colorizer/main/screenshots/screenshot_light_linux.png"/>
</details>

## 📜 License (of this package)
[MIT](https://github.com/Valer100/Sun-Valley-Theme-Colorizer/blob/main/LICENSE)
