<p align="center">
  <img width=700 src="https://github.com/Valer100/Sun-Valley-Theme-Colorizer/blob/main/screenshots/screenshot_hero_dark.png"/>
</p>

# Sun Valley Theme Colorizer

This Python module allows you to change the accent color of [@rdbende](https://github.com/rdbende)'s Sun Valley ttk theme without the need to manually download the theme from GitHub, change the hue of the spritesheet files and change some colors in the tcl files. This module does all of this for you.

## How to install
Run this command in your terminal:
```
pip install sv_ttk_colorizer
```

To launch the module, run this command in your terminal:
```
python -m sv_ttk_colorizer
```

## Requirements
Python 3.8 or newer (like the theme)

## What's this module doing?
Well, like I said before, it downloads the latest version of the theme from GitHub, then it changes the hue of the spritesheet images, changes a few colors in ```light.tcl``` and ```dark.tcl``` and then it gives you the modified theme inside a folder named ```sv_ttk``` that you will have to move into your project's root folder. You don't have to do any changes in your code.

## License (of the module)
[MIT](https://github.com/Valer100/Sun-Valley-Theme-Colorizer/blob/main/LICENSE)
