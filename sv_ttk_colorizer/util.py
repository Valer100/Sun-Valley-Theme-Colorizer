import tkinter as tk, colorsys, shutil, sys, appdirs, os, darkdetect
from tkinter import ttk
from PIL import Image

is_accent_modified = False
latest_sv_ttk = "https://github.com/rdbende/Sun-Valley-ttk-theme/archive/refs/heads/main.zip"
sv_ttk_license = "https://raw.githubusercontent.com/rdbende/Sun-Valley-ttk-theme/main/LICENSE"
dm_titlebars_patch = "https://raw.githubusercontent.com/Valer100/Sun-Valley-ttk-theme/windows-titlebar-tweaks/sv_ttk/__init__.py"
root_folder = appdirs.user_data_dir("sv_ttk_colorizer")

if not os.path.exists(root_folder): os.makedirs(root_folder)
if os.path.exists(root_folder + "/resources"): shutil.rmtree(root_folder + "/resources")

shutil.copytree("resources", root_folder + "/resources")

def update_preview_assets(theme):
    global preview_bg, preview_text, preview, preview_theme, is_accent_changed

    preview_theme = theme
    preview_bg = tk.PhotoImage(file = root_folder + f"/resources/{theme}/preview.png")
    preview_text = tk.PhotoImage(file = root_folder + f"/resources/{theme}/preview_accent_text.png")

    if is_accent_modified: preview = tk.PhotoImage(file = root_folder + f"/resources/{theme}/preview_accent_modified.png")
    else: preview = tk.PhotoImage(file = root_folder + f"/resources/{theme}/preview_accent.png")

update_preview_assets("light")

accent_light = "#005fb8"
accent_dark = "#57c8ff"


color_constants_patch_find = '''def set_theme(theme: str, root: tkinter.Tk | None = None) -> None:'''

color_constants_patch_replace = f'''def set_theme(theme: str, root: tkinter.Tk | None = None) -> None:
    global background, bg, foreground, fg, foreground_disabled, fg_dis, selection_foreground, sel_fg, selection_background, sel_bg, accent 

    if theme.lower() == "dark":
        background, bg = "#1c1c1c", "#1c1c1c"
        foreground, fg = "#fafafa", "#fafafa"
        foreground_disabled, fg_dis = "#595959", "#595959"
        selection_foreground, sel_fg = "#ffffff", "#ffffff"
        selection_background, sel_bg = "{accent_light}", "{accent_light}"
        accent = "{accent_dark}", "{accent_dark}"
    elif theme.lower() == "light":
        background, bg = "#fafafa", "#fafafa"
        foreground, fg = "#1c1c1c", "#1c1c1c"
        foreground_disabled, fg_dis = "#a0a0a0", "#a0a0a0"
        selection_foreground, sel_fg = "#ffffff", "#ffffff"
        selection_background, sel_bg = "{accent_light}", "{accent_light}"
        accent = "{accent_light}", "{accent_light}"
'''

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

dm_titlebars_find1 = '''TCL_THEME_FILE_PATH = Path(__file__).with_name("sv.tcl").absolute()'''

dm_titlebars_replace1 = '''TCL_THEME_FILE_PATH = Path(__file__).with_name("sv.tcl").absolute()


# A hacky way to change a Toplevel's title bar color after it's created
class ThemedToplevel(tkinter.Toplevel):
    def __init__(self, master=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        try: set_theme(get_theme())
        except: pass

tkinter.Toplevel = ThemedToplevel'''

dm_titlebars_find2 = '''style.theme_use(f"sun-valley-{theme}")'''

dm_titlebars_replace2 = '''# Set title bar color on Windows
    def set_title_bar_color(root):
        import sys

        if sys.platform == "win32":
            import pywinstyles
            version = sys.getwindowsversion()

            if version.major == 10 and version.build >= 22000:
                if theme == "dark": pywinstyles.change_header_color(root, "#1c1c1c")
                elif theme == "light": pywinstyles.change_header_color(root, "#fafafa")
            elif version.major == 10:
                if theme == "dark": pywinstyles.apply_style(root, "dark")
                else: pywinstyles.apply_style(root, "normal")

                # A hacky way to update the title bar's color on Windows 10 (it doesn't update instantly like on Windows 11)
                root.wm_attributes("-alpha", 0.99)
                root.wm_attributes("-alpha", 1)

    def set_title_bar_color_toplevels():
        for widget in style.master.winfo_children():
            if isinstance(widget, tkinter.Toplevel): set_title_bar_color(widget)

    set_title_bar_color(style.master)
    set_title_bar_color_toplevels()

    style.theme_use(f"sun-valley-{theme}")'''


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
    global accent_light, accent_dark, color_constants_patch_replace

    img_light = Image.open(root_folder + "/resources/light/preview_accent_modified.png")
    accent_light_rgb = img_light.getpixel((310, 373))

    img_dark = Image.open(root_folder + "/resources/dark/preview_accent_modified.png")
    accent_dark_rgb = img_dark.getpixel((310, 373))

    accent_light = "#{:02x}{:02x}{:02x}".format(accent_light_rgb[0], accent_light_rgb[1], accent_light_rgb[2])
    accent_dark = "#{:02x}{:02x}{:02x}".format(accent_dark_rgb[0], accent_dark_rgb[1], accent_dark_rgb[2])

    color_constants_patch_replace = f'''def set_theme(theme: str, root: tkinter.Tk | None = None) -> None:
    global background, bg, foreground, fg, foreground_disabled, fg_dis, selection_foreground, sel_fg, selection_background, sel_bg, accent 

    if theme.lower() == "dark":
        background, bg = "#1c1c1c", "#1c1c1c"
        foreground, fg = "#fafafa", "#fafafa"
        foreground_disabled, fg_dis = "#595959", "#595959"
        selection_foreground, sel_fg = "#ffffff", "#ffffff"
        selection_background, sel_bg = "{accent_light}", "{accent_light}"
        accent = "{accent_dark}"
    elif theme.lower() == "light":
        background, bg = "#fafafa", "#fafafa"
        foreground, fg = "#1c1c1c", "#1c1c1c"
        foreground_disabled, fg_dis = "#a0a0a0", "#a0a0a0"
        selection_foreground, sel_fg = "#ffffff", "#ffffff"
        selection_background, sel_bg = "{accent_light}", "{accent_light}"
        accent = "{accent_light}"
'''

def update_preview(hue):
    global preview, is_accent_modified, preview_theme

    shutil.copyfile(root_folder + "/resources/light/preview_accent.png", root_folder + "/resources/light/preview_accent_modified.png")
    shutil.copyfile(root_folder + "/resources/dark/preview_accent.png", root_folder + "/resources/dark/preview_accent_modified.png")
    change_hue_and_save(root_folder + "/resources/light/preview_accent_modified.png", hue)
    change_hue_and_save(root_folder + "/resources/dark/preview_accent_modified.png", hue)

    is_accent_modified = True
    update_preview_assets(preview_theme)

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

    # if not get_windows_version() == 0: root.iconbitmap("resources/icon.ico")
    # else: root.iconphoto(True, icon)

def get_windows_version() -> int:
    if sys.platform == "win32":
        version = sys.getwindowsversion()

        if version.major == 10 and version.build >= 22000: return 11
        elif version.major == 10: return 10
        else: return version.major
    else: return 0

def disable_all_widgets(root):
    for widget in root.winfo_children():
        if isinstance(widget, (tk.Frame, ttk.Frame, ttk.Separator)): disable_all_widgets(widget)
        else:
            if not isinstance(widget, (ttk.Label, tk.Canvas)): widget["state"] = "disabled"

def enable_all_widgets(root):
    for widget in root.winfo_children():
        if isinstance(widget, (tk.Frame, ttk.Frame, ttk.Separator, tk.Canvas)): enable_all_widgets(widget)
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
        checkbox.focus_set()

    label = ttk.Label(layout, text = text, wraplength = 200, anchor = "w")
    label.pack(side = "left")
    label.bind("<Enter>", on_enter)
    label.bind("<Leave>", on_leave)
    label.bind("<ButtonRelease-1>", on_click)

def add_radiobutton(parent, text, variable, value):
    layout = ttk.Frame(parent)
    layout.pack(fill = "x", pady = (8, 0))

    radiobutton = ttk.Radiobutton(layout, variable = variable, value = value)
    radiobutton.pack(side = "left")

    def on_enter(event):
        if not str(radiobutton["state"]).__contains__("disabled"): radiobutton.configure(state = "active")

    def on_leave(event):
        if not str(radiobutton["state"]).__contains__("disabled"): radiobutton.configure(state = "!active")

    def on_click(event):
        if not str(radiobutton["state"]).__contains__("disabled"): variable.set(value)
        radiobutton.focus_set()

    label = ttk.Label(layout, text = text, wraplength = 200, anchor = "w")
    label.pack(side = "left")
    label.bind("<Enter>", on_enter)
    label.bind("<Leave>", on_leave)
    label.bind("<ButtonRelease-1>", on_click)

def fix_mouse_focus(parent):
    for widget in parent.winfo_children():
        if isinstance(widget, (tk.Frame, ttk.Frame, tk.Canvas)): fix_mouse_focus(widget)
        elif not isinstance(widget, (ttk.Entry, ttk.Combobox, ttk.Spinbox, tk.Text)): 
            widget.bind("<ButtonRelease-1>", lambda event: parent.focus_set(), add = "+")
            widget.bind("<B1-Leave>", lambda event: parent.focus_set(), add = "+")