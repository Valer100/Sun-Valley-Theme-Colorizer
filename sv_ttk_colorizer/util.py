import tkinter as tk, colorsys, shutil, sys, appdirs, os, darkdetect
from tkinter import ttk
from PIL import Image

latest_sv_ttk = "https://github.com/rdbende/Sun-Valley-ttk-theme/archive/refs/heads/main.zip"
sv_ttk_license = "https://raw.githubusercontent.com/rdbende/Sun-Valley-ttk-theme/main/LICENSE"
dm_titlebars_patch = "https://raw.githubusercontent.com/Valer100/Sun-Valley-ttk-theme/windows-titlebar-tweaks/sv_ttk/__init__.py"
root_folder = appdirs.user_data_dir("sv_ttk_colorizer")

if not os.path.exists(root_folder): os.makedirs(root_folder)
if os.path.exists(root_folder + "/resources"): shutil.rmtree(root_folder + "/resources")

shutil.copytree("resources", root_folder + "/resources")

preview_bg = tk.PhotoImage(file = root_folder + "/resources/preview.png")
preview_text = tk.PhotoImage(file = root_folder + "/resources/preview_accent_text.png")
preview = tk.PhotoImage(file = root_folder + "/resources/preview_accent.png")

accent_light = "#005fb8"
accent_dark = "#57c8ff"

get_accents_patch_find = '''use_dark_theme = partial(set_theme, "dark")
use_light_theme = partial(set_theme, "light")'''

get_accents_patch_replace = f'''def get_accent_color() -> str:
    if get_theme() == "dark": return "{accent_dark}"
    return "{accent_light}"
    
def get_selection_accent_color() -> str: return "{accent_light}"


use_dark_theme = partial(set_theme, "dark")
use_light_theme = partial(set_theme, "light")'''

toolbutton_fix_find = '''empty 152 64 10 10 \\'''
toolbutton_fix_replace = '''empty 152 209 20 20 \\'''

menu_revert_colors_find = '''TCL_THEME_FILE_PATH = Path(__file__).with_name("sv.tcl").absolute()'''

menu_revert_colors_replace = '''TCL_THEME_FILE_PATH = Path(__file__).with_name("sv.tcl").absolute()

class MenuFix(tkinter.Menu):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)

        def fix_menu_colors(event = None):
            import sys
            
            if sys.platform == "win32" or sys.platform == "darwin":
                if (str(self["bg"]).lower() == "#fafafa" and str(self["fg"]).lower() == "#1c1c1c") or (str(self["bg"]).lower() == "#1c1c1c" and str(self["fg"]).lower() == "#fafafa"): 
                    self.configure(bg="SystemMenu", fg="SystemMenuText")
        
        fix_menu_colors()
        self.after(100, fix_menu_colors)
        self.bind("<<ThemeChanged>>", fix_menu_colors)

tkinter.Menu = MenuFix'''

def update_colors(theme):
    global bg, warning, bg_wallpaper, accent, reference

    if theme == "dark": 
        bg = "#202020"
        warning = "#FFFF00"
        accent = "#57c8ff"
        reference = "#121212"
    else: 
        bg = "#ffffff"
        warning = "#FF0000"
        accent = "#005fb8"
        reference = "#383838"

update_colors(darkdetect.theme().lower())

sv_ttk_download = root_folder + "/temp/sv_ttk repo/Sun-Valley-ttk-theme-main/sv_ttk/"
sv_ttk_spritesheet_light = sv_ttk_download + "/theme/spritesheet_light.png"
sv_ttk_spritesheet_dark = sv_ttk_download + "/theme/spritesheet_dark.png"
sv_ttk_light = sv_ttk_download + "/theme/light.tcl"
sv_ttk_dark = sv_ttk_download + "/theme/dark.tcl"
sv_ttk_light_sprites = sv_ttk_download + "/theme/sprites_light.tcl"
sv_ttk_dark_sprites = sv_ttk_download + "/theme/sprites_dark.tcl"
sv_ttk_sv = sv_ttk_download + "/sv.tcl"

desktop = os.path.expanduser("~") + "/Desktop"

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
    global accent_light, accent_dark, get_accents_patch_replace
    img = Image.open(root_folder + "/resources/preview_accent_modified.png")

    accent_light_rgb = img.getpixel((50, 75))
    accent_dark_rgb = img.getpixel((537, 75))

    accent_light = "#{:02x}{:02x}{:02x}".format(accent_light_rgb[0], accent_light_rgb[1], accent_light_rgb[2])
    accent_dark = "#{:02x}{:02x}{:02x}".format(accent_dark_rgb[0], accent_dark_rgb[1], accent_dark_rgb[2])

    get_accents_patch_replace = f'''def get_accent_color() -> str:
    if get_theme() == "dark": return "{accent_dark}"
    return "{accent_light}"
    
def get_selection_accent_color() -> str: return "{accent_light}"


use_dark_theme = partial(set_theme, "dark")
use_light_theme = partial(set_theme, "light")'''

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

    if not get_windows_version() == 0: root.iconbitmap("resources/icon.ico")

def get_windows_version() -> int:
    if sys.platform == "win32":
        version = sys.getwindowsversion()

        if version.major == 10 and version.build >= 22000: return 11
        elif version.major == 10: return 10
        else: return version.major
    else: return 0

def disable_all_widgets(root):
    for widget in root.winfo_children():
        if isinstance(widget, (tk.Frame, ttk.Frame)): disable_all_widgets(widget)
        else:
            if not isinstance(widget, ttk.Label): widget["state"] = "disabled"

def enable_all_widgets(root):
    for widget in root.winfo_children():
        if isinstance(widget, (tk.Frame, ttk.Frame)): enable_all_widgets(widget)
        else: widget["state"] = "enabled"

class AutoScrollbar(ttk.Scrollbar):
    def set(self, lo, hi):
        if float(lo) <= 0.0 and float(hi) >= 1.0: self.pack_forget()
        else:
            if self.cget("orient") == "horizontal": self.pack(fill = "x")
            else: self.pack(fill = "y", expand = True)
            
        ttk.Scrollbar.set(self, lo, hi)

def add_switch(parent, text, variable):
    layout = ttk.Frame(parent)
    layout.pack(fill = "x", pady = (16, 0))

    checkbox = ttk.Checkbutton(layout, variable = variable, style = "Switch.TCheckbutton")
    checkbox.pack(side = "left")

    def on_enter(event):
        if not str(checkbox["state"]).__contains__("disabled"): checkbox.configure(state = "active")

    def on_leave(event):
        if not str(checkbox["state"]).__contains__("disabled"): checkbox.configure(state = "!active")

    def on_click(event):
        if not str(checkbox["state"]).__contains__("disabled"): variable.set(not variable.get())

    label = ttk.Label(layout, text = text, wraplength = 200, anchor = "w")
    label.pack(side = "left")
    label.bind("<Enter>", on_enter)
    label.bind("<Leave>", on_leave)
    label.bind("<ButtonRelease-1>", on_click)