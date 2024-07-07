import tkinter as tk, colorsys, shutil, sys, appdirs, os
from PIL import Image

latest_sv_ttk = "https://github.com/rdbende/Sun-Valley-ttk-theme/archive/refs/heads/main.zip"
root_folder = appdirs.user_data_dir("sv_ttk_colorizer")

if not os.path.exists(root_folder): os.makedirs(root_folder)
if os.path.exists(root_folder + "/resources"): shutil.rmtree(root_folder + "/resources")

shutil.copytree("resources", root_folder + "/resources")

preview_bg = tk.PhotoImage(file = root_folder + "/resources/preview.png")
preview_text = tk.PhotoImage(file = root_folder + "/resources/preview_accent_text.png")
preview = tk.PhotoImage(file = root_folder + "/resources/preview_accent.png")

accent_light = "#005fb8"
accent_dark = "#57c8ff"

sv_ttk_download = root_folder + "/temp/sv_ttk repo/Sun-Valley-ttk-theme-main/sv_ttk/"
sv_ttk_spritesheet_light = sv_ttk_download + "/theme/spritesheet_light.png"
sv_ttk_spritesheet_dark = sv_ttk_download + "/theme/spritesheet_dark.png"
sv_ttk_light = sv_ttk_download + "/theme/light.tcl"
sv_ttk_dark = sv_ttk_download + "/theme/dark.tcl"

def change_hue_and_save(path, hue):
    img = Image.open(path)
    img.convert("RGBA")
    img = img.copy()
    data = img.getdata()
    hue /= 100

    new_img_data = []
    for item in data:
        r, g, b, a = item
        if a == 0:
            new_img_data.append((r, g, b, a))
            continue
        h, s, v = colorsys.rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)
        h = (h + hue) % 1.0
        r, g, b = colorsys.hsv_to_rgb(h, s, v)
        r, g, b = int(r * 255.0), int(g * 255.0), int(b * 255.0)
        new_img_data.append((r, g, b, a))

    img.putdata(new_img_data)
    img.save(path)
    img.close()

def update_accents():
    global accent_light, accent_dark
    img = Image.open(root_folder + "/resources/preview_accent_modified.png")

    accent_light_rgb = img.getpixel((50, 75))
    accent_dark_rgb = img.getpixel((537, 75))

    accent_light = "#{:02x}{:02x}{:02x}".format(accent_light_rgb[0], accent_light_rgb[1], accent_light_rgb[2])
    accent_dark = "#{:02x}{:02x}{:02x}".format(accent_dark_rgb[0], accent_dark_rgb[1], accent_dark_rgb[2])

def update_preview(hue):
    global preview

    shutil.copyfile(root_folder + "/resources/preview_accent.png", root_folder + "/resources/preview_accent_modified.png")
    change_hue_and_save(root_folder + "/resources/preview_accent_modified.png", hue)

    preview = tk.PhotoImage(file = root_folder + "/resources/preview_accent_modified.png")

def set_title_bar_color(root, theme):
    if get_windows_version() == 10:
        import pywinstyles

        if theme == "dark": pywinstyles.apply_style(root, "dark")
        else: pywinstyles.apply_style(root, "normal")

        root.wm_attributes("-alpha", 0.99)
        root.wm_attributes("-alpha", 1)
    elif get_windows_version() == 11:
        import pywinstyles
            
        if theme == "dark": pywinstyles.change_header_color(root, "#1c1c1c")
        elif theme == "light": pywinstyles.change_header_color(root, "#fafafa")

def get_windows_version() -> int:
    if sys.platform == "win32":
        version = sys.getwindowsversion()

        if version.major == 10 and version.build >= 22000:
            return 11
        elif version.major == 10:
            return 10
        else:
            return version.major
    else:
        return 0