<div align="center">
  <img width=700 src="https://github.com/Valer100/Sun-Valley-Theme-Colorizer/blob/main/screenshots/image_hero_dark.png?raw=true"/>
</div>

# Sun Valley Theme Colorizer

This Python module allows you to change the accent color of [@rdbende](https://github.com/rdbende)'s [Sun Valley ttk theme](https://github.com/rdbende/Sun-Valley-ttk-theme) without the need to manually download the theme from GitHub, change the hue of the spritesheet files and change some colors in the tcl files. This module does everything for you.

## How to install
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

## Requirements
Python 3.8 or newer (like the theme)

## What's this module doing?
Well, like I said before, it downloads the latest version of the theme from GitHub, then it changes the hue of the spritesheet images, changes some colors in ```light.tcl``` and ```dark.tcl``` and then it gives you the modified theme in a folder named ```sv_ttk``` that you have to move to the root folder of your project. You don't need to make any changes to your code.

## Screenshots
<details>
  <summary>Show</summary>
  <br>
  <img src="https://raw.githubusercontent.com/Valer100/Sun-Valley-Theme-Colorizer/main/screenshots/screenshot_dark.png"/>
  <br><br>
  <img src="https://raw.githubusercontent.com/Valer100/Sun-Valley-Theme-Colorizer/main/screenshots/screenshot_light.png"/>
</details>

## License (of the module)
[MIT](https://github.com/Valer100/Sun-Valley-Theme-Colorizer/blob/main/LICENSE)
