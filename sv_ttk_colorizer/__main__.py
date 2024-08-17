import tkinter as tk, sv_ttk, darkdetect, os, shutil, sys, subprocess, importlib.metadata, appdirs
from tkinter import ttk, filedialog as fd, messagebox as msg
from tkscrollframe import ScrollFrame
from urllib.request import urlretrieve
from zipfile import ZipFile

def main():
    global hue_value, hue_thumb, hue_thumb_pressed, is_editing_allowed, preview_theme, switcher_bg
    hue_value = 0
    is_editing_allowed = True
    preview_theme = "light"

    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    window = tk.Tk()
    window.title("Sun Valley Theme Colorizer")

    icon_48x48 = tk.PhotoImage(file = "resources/icon/48x48.png")
    icon_32x32 = tk.PhotoImage(file = "resources/icon/32x32.png")
    icon_16x16 = tk.PhotoImage(file = "resources/icon/16x16.png")
    
    if sys.platform == "win32": window.iconphoto(True, icon_48x48, icon_32x32, icon_16x16)

    dark_mode = tk.BooleanVar(value = False)

    if not sys.platform == "win32" or sys.platform == "darwin": 
        if os.path.exists(appdirs.user_data_dir("sv_ttk_colorizer") + "/dark_mode"): 
            if open(appdirs.user_data_dir("sv_ttk_colorizer") + "/dark_mode").read() == "1": dark_mode.set(True)

    window.minsize(width = 900, height = 600)
    
    dm_titlebars = tk.BooleanVar(value = False)
    menu_revert_colors = tk.BooleanVar(value = False)
    accent_funcs = tk.BooleanVar(value = False)
    fix_lag = tk.BooleanVar(value = False)
    include_examplepy = tk.BooleanVar(value = True)
    include_config = tk.BooleanVar(value = True)
    working_mode = tk.StringVar(value = "online")

    try: import util, assistance
    except Exception as e: from sv_ttk_colorizer import util, assistance # type: ignore

    util.set_title_bar_color(window, darkdetect.theme().lower())

    print("Sun Valley Theme Colorizer v1.3.2")
    print("Work path: " + util.root_folder)

    title = ttk.Frame(window)
    title.pack(fill = "x", pady = (8, 0))

    ttk.Label(title, text = "Sun Valley Theme Colorizer", font = ("Segoe UI Semibold", 20)).pack(side = "left", padx = 16)

    theme_switch = ttk.Checkbutton(title, text = "Dark Mode", style = "Switch.TCheckbutton", command = lambda: toggle_theme(), variable = dark_mode)
    if not sys.platform == "win32" or sys.platform == "darwin": theme_switch.pack(side = "right", fill = "y", padx = (0, 16))

    frame = tk.Frame(window, bg = util.bg)
    frame.pack(pady = (16, 0), fill = "both", expand = True)

    if sys.platform == "win32" or sys.platform == "darwin": sv_ttk.set_theme(darkdetect.theme())
    else: sv_ttk.set_theme("light")

    window.configure(cursor = "watch")
    window.update()

    image = tk.PhotoImage(file = util.root_folder + f"/resources/image.png")

    window.configure(cursor = "")

    preview = tk.Canvas(frame, bg = util.bg, highlightthickness = 0)
    preview.pack(fill = "both", expand = True, side = "left")

    ttk.Separator(preview, orient = "horizontal").pack(fill = "x")

    theme_switcher_preview = ttk.Frame(preview, padding = 4)
    theme_switcher_preview.pack(pady = (19, 16))
    theme_switcher_preview.columnconfigure(index = 0, weight = 1, minsize = 134)
    theme_switcher_preview.columnconfigure(index = 1, weight = 1, minsize = 134)

    light = ttk.Button(theme_switcher_preview, text = "Light", style = "Accent.TButton", command = lambda: update_preview_theme("light"))
    light.grid(row = 0, column = 0, sticky = "nesw", padx = (0, 6))

    dark = ttk.Button(theme_switcher_preview, text = "Dark", command = lambda: update_preview_theme("dark"))
    dark.grid(row = 0, column = 1, sticky = "nesw", padx = (6, 0))

    options_frame = ttk.Frame(frame, padding = (24, 8, 0, 24))
    options_frame.pack(side = "right", anchor = "n", fill = "y")

    ttk.Separator(frame, orient = "vertical").pack(side = "right", fill = "y")

    def update_preview_theme(theme):
        global preview_theme
        preview_theme = theme

        if theme == "dark": light["style"] = "TButton"; dark["style"] = "Accent.TButton"
        else: light["style"] = "Accent.TButton"; dark["style"] = "TButton"

        util.update_preview_assets(theme)
        preview.delete("window")
        preview.delete("accent")
        preview.delete("text")
        preview.create_image(preview.winfo_width() // 2, preview.winfo_height() // 2 + 28, image = util.preview_bg, anchor = "center", tag = "window")
        preview.create_image(preview.winfo_width() // 2, preview.winfo_height() // 2 + 28, image = util.preview, anchor = "center", tag = "accent")
        preview.create_image(preview.winfo_width() // 2, preview.winfo_height() // 2 + 28, image = util.preview_text, anchor = "center", tag = "text")

    def update_preview(event):
        if is_editing_allowed:
            try:
                thumb_coords = hue_slider.coords("thumb")
                hue_slider.delete("thumb")
                hue_slider.create_image(thumb_coords[0], thumb_coords[1], image = hue_thumb, anchor = "center", tag = "thumb")
            except:
                thumb_coords = hue_slider.coords("thumb_hover")
                hue_slider.delete("thumb_hover")
                hue_slider.create_image(thumb_coords[0], thumb_coords[1], image = hue_thumb, anchor = "center", tag = "thumb_hover")

            window.configure(cursor = "watch")
            hue_slider.configure(cursor = "watch")
            window.update()
            util.update_preview(hue_value)
            util.update_accents()
            update_preview_theme(preview_theme)
            window.configure(cursor = "")
            hue_slider.configure(cursor = "")

    def gen_export_file(): 
        return f'''// This is a Sun Valley Theme Colorizer configuration file.
// Do not edit this by hand or unexpected things will happen.

{str(hue_value)}
{str(int(dm_titlebars.get()))}
{str(int(accent_funcs.get()))}
{str(int(fix_lag.get()))}
{str(int(include_examplepy.get()))}
{str(int(include_config.get()))}
{str(int(menu_revert_colors.get()))}'''

    def export_settings():
        file_path = fd.asksaveasfile(filetypes = [("Sun Valley Theme Colorizer configuration file", ".svttkc")], title = "Export settings", initialdir = util.desktop, initialfile = "config.svttkc")

        if not file_path == None:
            open(file_path.name, "w").write(gen_export_file())
            msg.showinfo("Sun Valley Theme Colorizer", "The settings have been exported.")

    def import_settings():
        global hue_value
        file_path = fd.askopenfile(filetypes = [("Sun Valley Theme Colorizer configuration file", ".svttkc")], initialdir = util.desktop, initialfile = "config.svttkc")

        if not file_path == None:
            settings = open(file_path.name).read().split("\n")

            try:
                hue_value = (float(settings[3]))
                hue_slider.delete("thumb")

                update_hue_slider()
                update_preview(None)

                dm_titlebars.set(int(settings[4]))
                accent_funcs.set(int(settings[5]))
                fix_lag.set(int(settings[6]))
                include_examplepy.set(int(settings[7]))
                include_config.set(int(settings[8]))
                menu_revert_colors.set(int(settings[9]))

                msg.showinfo("Sun Valley Theme Colorizer", "The settings were imported.")
            except Exception as e: msg.showerror("Sun Valley Theme Colorizer", "Invalid configuration file or the configuration file was made using an older version of Sun Valley Theme Colorizer."); print(e)

    scrolled_frame_parent = tk.Frame(options_frame)
    scrolled_frame_parent.pack(fill = "y", expand = True)

    scrolled_frame = ScrollFrame(scrolled_frame_parent)
    scrolled_frame.pack(fill = "both", expand = True, pady = (0, 24), anchor = "w")
    scrolled_frame.canvas.configure(width = 280)

    def fix_scrolling(event):
        if sys.platform.startswith("darwin"): scrolled_frame.canvas.yview_scroll(-1 * event.delta, "units") #macOS
        elif event.num == 4: scrolled_frame.canvas.yview_scroll(-1, "units") # Linux (scroll up)
        elif event.num == 5: scrolled_frame.canvas.yview_scroll(1, "units") # Linux (scroll down)
        else: scrolled_frame.canvas.yview_scroll(-1 * (event.delta // 120), "units") # Windows

    scrolled_frame.canvas.bind_all("<MouseWheel>", fix_scrolling)
    scrolled_frame.canvas.bind_all("<Button-4>", fix_scrolling)
    scrolled_frame.canvas.bind_all("<Button-5>", fix_scrolling)

    options = scrolled_frame.viewPort
    
    import_export = ttk.Frame(options)
    import_export.pack(anchor = "w", pady = (0, 16), padx = (0, 24), fill = "x")
    import_export.columnconfigure(index = 0, weight = 1)
    import_export.columnconfigure(index = 1, weight = 1)

    import_ = ttk.Button(import_export, text = "Import", command = import_settings)
    import_.grid(row = 0, column = 0, sticky = "nesw", padx = (0, 4))

    export = ttk.Button(import_export, text = "Export", style = "Accent.TButton", command = export_settings)
    export.grid(row = 0, column = 1, sticky = "nesw", padx = (4, 0))

    ttk.Separator(options, orient = "vertical").pack(fill = "x", pady = (0, 16))

    ttk.Label(options, text = "Working mode").pack(anchor = "w")
    util.add_radiobutton(options, "Download sv_ttk from GitHub (recommended)", working_mode, "online")
    util.add_radiobutton(options, "Use sv_ttk from site-packages", working_mode, "offline")

    ttk.Separator(options, orient = "vertical").pack(fill = "x", pady = (16, 0))

    ttk.Label(options, text = "Accent color").pack(anchor = "w", pady = (16, 8))

    hue_img = tk.PhotoImage(file = "resources/hue_scale/track.png")
    hue_thumb = tk.PhotoImage(file = f"resources/hue_scale/thumb_{sv_ttk.get_theme()}.png")
    hue_thumb_pressed = tk.PhotoImage(file = f"resources/hue_scale/thumb_pressed_{sv_ttk.get_theme()}.png")

    def on_progress_change(event):
        global hue_value, hue_thumb, hue_thumb_pressed, is_editing_allowed
        hue_slider.focus_set()

        if is_editing_allowed:
            if event.x >= 10 and event.x <= 240:
                hue_slider.delete("thumb")
                hue_slider.create_image(event.x, hue_thumb.height() // 2, image = hue_thumb_pressed, anchor = "center", tag = "thumb")

                hue_value = event.x / 2.4
            elif event.x <= 10:
                hue_slider.delete("thumb")
                hue_slider.create_image(10, hue_thumb.height() // 2, image = hue_thumb_pressed, anchor = "center", tag = "thumb")

                hue_value = 0
            elif event.x >= 240:
                hue_slider.delete("thumb")
                hue_slider.create_image(240, hue_thumb.height() // 2, image = hue_thumb_pressed, anchor = "center", tag = "thumb")

                hue_value = 100

    hue_slider = tk.Canvas(options, highlightthickness = 0, width = hue_img.width(), height = hue_thumb.height())
    hue_slider.pack(anchor = "w")
    hue_slider.create_image(0, 8, image = hue_img, anchor = "nw")
    hue_slider.create_image(10, hue_thumb.height() // 2, image = hue_thumb, anchor = "center", tag = "thumb")
    hue_slider.bind("<Button-1>", on_progress_change)
    hue_slider.bind("<B1-Motion>", on_progress_change)
    hue_slider.bind("<ButtonRelease-1>", update_preview)

    ttk.Separator(options, orient = "vertical").pack(fill = "x", pady = (16, 0))

    util.add_switch(options, "Dark Mode title bars on Windows", dm_titlebars)

    warning1 = ttk.Label(options, text = "This setting requires an additional dependency for your project: pywinstyles.", foreground = util.warning, wraplength = 270)
    warning1.pack(pady = (8, 0), anchor = "w")

    ttk.Separator(options, orient = "vertical").pack(fill = "x", pady = (16, 0))

    util.add_switch(options, "Don't change menu colors on Windows and macOS", menu_revert_colors)
    ttk.Separator(options, orient = "vertical").pack(fill = "x", pady = (16, 0))

    util.add_switch(options, "Add color constants for programmatic access", accent_funcs)

    warning2 = ttk.Label(options, text = "You can learn more about this option in Help > Color constants.", foreground = util.warning, wraplength = 250)
    warning2.pack(pady = (8, 0), anchor = "w")

    ttk.Separator(options, orient = "vertical").pack(fill = "x", pady = (16, 0))

    util.add_switch(options, "Fix Toolbutton lag in complex layouts", fix_lag)
    ttk.Separator(options, orient = "vertical").pack(fill = "x", pady = (16, 0))
    util.add_switch(options, "Include a preview file to test the theme (\"example.py\")", include_examplepy)
    ttk.Separator(options, orient = "vertical").pack(fill = "x", pady = (16, 0))
    util.add_switch(options, "Include a configuration file with these settings (\"config.svttkc\")", include_config)
    ttk.Separator(options, orient = "vertical").pack(fill = "x", pady = (16, 0))

    def allow_editing():
        global status, is_editing_allowed, hue_thumb
        is_editing_allowed = True

        hue_thumb = tk.PhotoImage(file = f"resources/hue_scale/thumb_{sv_ttk.get_theme()}.png")
        update_hue_slider()

        window.update()
        window.configure(cursor = "")
        status.destroy()
        save.pack(side = "bottom", fill = "x", padx = (0, 24))
        help_btn.pack(side = "bottom", pady = (0, 8), fill = "x", padx = (0, 24))
        util.enable_all_widgets(options)
        theme_switch.configure(state = "enabled")

    def save_patch():
        global status, is_editing_allowed, hue_thumb
        save_to = fd.askdirectory(title = "Choose a folder to save the modified theme", initialdir = util.desktop)

        if not save_to == "":
            is_editing_allowed = False
            hue_thumb = tk.PhotoImage(file = f"resources/hue_scale/thumb_disabled_{sv_ttk.get_theme()}.png")
            update_hue_slider()

            window.configure(cursor = "watch")
            util.disable_all_widgets(options)
            theme_switch.configure(state = "disabled")
            save.forget()
            help_btn.forget()

            if os.path.exists(util.root_folder + "/temp"): shutil.rmtree(util.root_folder + "/temp")
            os.mkdir(util.root_folder + "/temp")


            if working_mode.get() == "online":
                status = ttk.Label(options_frame, text = "Downloading sv_ttk...", font = ("Segoe UI Semibold", 15))
                status.pack(side = "bottom", padx = (0, 24))

                window.update()

                try: urlretrieve(util.latest_sv_ttk, util.root_folder + "/temp/sv_ttk.zip")
                except:
                    allow_editing()
                    msg.showerror("Failed to download sv_ttk", "Check your internet connection and try again. If your internet connection is down or unstable, try choosing \"Use sv_ttk from site-packages\" under \"Working mode\".")
                    return

                status["text"] = "Unzipping sv-ttk..."
                window.update()
                ZipFile(util.root_folder + "/temp/sv_ttk.zip").extractall(util.root_folder + "/temp/sv_ttk repo")
                urlretrieve(util.sv_ttk_license, util.sv_ttk_download + "/LICENSE")
            elif working_mode.get() == "offline":
                status = ttk.Label(options_frame, text = "Copying sv_ttk...", font = ("Segoe UI Semibold", 15))
                status.pack(side = "bottom", padx = (0, 24))

                window.update()
                os.makedirs(util.root_folder + "/temp/sv_ttk repo/Sun-Valley-ttk-theme-main")
                shutil.copytree(sv_ttk.__path__[0], util.root_folder + "/temp/sv_ttk repo/Sun-Valley-ttk-theme-main/sv_ttk")
                shutil.copyfile(f"{sv_ttk.__path__[0]}-{importlib.metadata.metadata('sv_ttk')['Version']}.dist-info/{importlib.metadata.metadata('sv_ttk')['License-File']}", util.sv_ttk_download + "/LICENSE")

                if os.path.exists(util.sv_ttk_download + "/__pycache__"): shutil.rmtree(util.sv_ttk_download + "/__pycache__")

            shutil.copyfile(util.root_folder + "/resources/LICENSE_MODIFICATIONS", util.sv_ttk_download + "/LICENSE_MODIFICATIONS")

            window.update()
            status["text"] = "Patching files..."
            
            util.change_hue_and_save(util.sv_ttk_spritesheet_light, hue_value)
            util.change_hue_and_save(util.sv_ttk_spritesheet_dark, hue_value)

            if include_examplepy.get(): shutil.copyfile(util.root_folder + "/resources/example.py", util.sv_ttk_download + "/example.py")

            light_tcl = open(util.sv_ttk_light, "r").read().replace("#005fb8", util.accent_light).replace("#2f60d8", util.accent_light).replace("#c1d8ee", "#dadada")
            dark_tcl = open(util.sv_ttk_dark, "r").read().replace("#57c8ff", util.accent_dark).replace("#2f60d8", util.accent_light).replace("#25536a", "#252525")

            open(util.sv_ttk_light, "w").write(light_tcl)
            open(util.sv_ttk_dark, "w").write(dark_tcl)

            if dm_titlebars.get():
                __init__file = open(util.sv_ttk_download + "/__init__.py", "r").read().replace(util.dm_titlebars_find1, util.dm_titlebars_replace1).replace(util.dm_titlebars_find2, util.dm_titlebars_replace2)
                open(util.sv_ttk_download + "/__init__.py", "w").write(__init__file)

            if accent_funcs.get():
                __init__file = open(util.sv_ttk_download + "/__init__.py", "r").read().replace(util.color_constants_patch_find, util.color_constants_patch_replace)
                open(util.sv_ttk_download + "/__init__.py", "w").write(__init__file)

            if fix_lag.get():
                sprites_light = open(util.sv_ttk_light_sprites, "r").read().replace(util.toolbutton_fix_find, util.toolbutton_fix_replace)
                sprites_dark = open(util.sv_ttk_dark_sprites, "r").read().replace(util.toolbutton_fix_find, util.toolbutton_fix_replace)

                open(util.sv_ttk_light_sprites, "w").write(sprites_light)
                open(util.sv_ttk_dark_sprites, "w").write(sprites_dark)

            if menu_revert_colors.get():
                __init__file = open(util.sv_ttk_download + "/__init__.py", "r").read().replace(util.menu_revert_colors_find, util.menu_revert_colors_replace)
                open(util.sv_ttk_download + "/__init__.py", "w").write(__init__file)

            if include_config.get(): open(util.sv_ttk_download + "/config.svttkc", "w").write(gen_export_file())

            window.update()
            status["text"] = "Almost there..."

            if os.path.exists(save_to + "/sv_ttk"): 
                delete = msg.askyesno("Error", "The folder \"sv_ttk\" already exists in \"" + save_to + "\". The folder must be deleted to continue. Do you want to delete it?", icon = "error")

                if delete:
                    if os.path.exists(save_to + "/sv_ttk"): shutil.rmtree(save_to + "/sv_ttk")
                else: 
                    allow_editing()

                    msg.showinfo("Sun Valley Theme Colorizer", "The save has been canceled.")
                    return

            shutil.move(util.sv_ttk_download, f"{save_to}/sv_ttk")
            shutil.rmtree(util.root_folder + "/temp")

            allow_editing()

            if include_examplepy.get():
                show_preview = msg.askyesno("Sun Valley Theme Colorizer", "The theme has been successfully modified and saved. Do you want to see it in action?", icon = "info")
                if show_preview: subprocess.Popen(f"\"{sys.executable}\" \"{save_to}/sv_ttk/example.py\"", shell = True)
            else:
                msg.showinfo("Sun Valley Theme Colorizer", "The theme has been successfully modified and saved.")

    def toggle_theme():
        global hue_value, hue_thumb, hue_thumb_pressed, switcher_bg

        sv_ttk.toggle_theme()
        util.update_colors(sv_ttk.get_theme())
        warning1["foreground"] = util.warning
        warning2["foreground"] = util.warning
        frame["background"] = util.bg
        preview["background"] = util.bg
        
        switcher_bg = tk.PhotoImage(file = f"resources/theme_switcher/bg_{sv_ttk.get_theme()}.png")
        hue_thumb = tk.PhotoImage(file = f"resources/hue_scale/thumb_{sv_ttk.get_theme()}.png")
        hue_thumb_pressed = tk.PhotoImage(file = f"resources/hue_scale/thumb_pressed_{sv_ttk.get_theme()}.png")
        update_hue_slider()

        preview.delete("switcher_bg")
        preview.create_image(preview.winfo_width() // 2, 12, image = switcher_bg, anchor = "n", tag = "switcher_bg")

        if sv_ttk.get_theme() == "dark": open(util.root_folder + "/dark_mode", "w").write("1")
        else: open(util.root_folder + "/dark_mode", "w").write("0")

    def update_hue_slider(event = None):
        global hue_value, hue_thumb
        hue_thumb = tk.PhotoImage(file = f"resources/hue_scale/thumb_{sv_ttk.get_theme()}.png")
        
        hue_slider.delete("thumb")
        hue_slider.delete("thumb_hover")

        if hue_value == 0: hue_slider.create_image(10, hue_thumb.height() // 2, image = hue_thumb, anchor = "center", tag = "thumb")
        elif hue_value == 100: hue_slider.create_image(240, hue_thumb.height() // 2, image = hue_thumb, anchor = "center", tag = "thumb")
        else: hue_slider.create_image(hue_value * 2.4, hue_thumb.height() // 2, image = hue_thumb, anchor = "center", tag = "thumb")

    def update_hue_slider_hover(event = None):
        global hue_value, hue_thumb
        hue_thumb = tk.PhotoImage(file = f"resources/hue_scale/thumb_hover_{sv_ttk.get_theme()}.png")

        hue_slider.delete("thumb")
        hue_slider.delete("thumb_hover")

        if hue_value == 0: hue_slider.create_image(10, hue_thumb.height() // 2, image = hue_thumb, anchor = "center", tag = "thumb_hover")
        elif hue_value == 100: hue_slider.create_image(240, hue_thumb.height() // 2, image = hue_thumb, anchor = "center", tag = "thumb_hover")
        else: hue_slider.create_image(hue_value * 2.4, hue_thumb.height() // 2, image = hue_thumb, anchor = "center", tag = "thumb_hover")

    hue_slider.tag_bind("thumb", "<Enter>", update_hue_slider_hover)
    hue_slider.tag_bind("thumb_hover", "<Leave>", update_hue_slider)

    save = ttk.Button(options_frame, text = "Save", style = "Accent.TButton", command = save_patch)
    save.pack(side = "bottom", fill = "x", padx = (0, 24))

    help_btn = ttk.Button(options_frame, text = "Help", command = assistance.show)
    help_btn.pack(side = "bottom", pady = (0, 8), fill = "x", padx = (0, 24))

    switcher_bg = tk.PhotoImage(file = f"resources/theme_switcher/bg_{sv_ttk.get_theme()}.png")

    preview.update()
    preview.create_image(preview.winfo_width() // 2, preview.winfo_height() // 2, image = image, anchor = "center")
    preview.create_image(preview.winfo_width() // 2, 12, image = switcher_bg, anchor = "n", tag = "switcher_bg")
    preview.create_image(preview.winfo_width() // 2, preview.winfo_height() // 2 + 28, image = util.preview_bg, anchor = "center", tag = "window")

    def toggle_preview_theme(event):
        if dark["style"] == "Accent.TButton": update_preview_theme("light")
        else: update_preview_theme("dark")

    preview.bind("<ButtonRelease-1>", toggle_preview_theme)

    def on_resize(event):
        preview.update()
        preview.delete("all")
        preview.create_image(preview.winfo_width() // 2, preview.winfo_height() // 2, image = image, anchor = "center")
        preview.create_image(preview.winfo_width() // 2, 12, image = switcher_bg, anchor = "n", tag = "switcher_bg")
        preview.create_image(preview.winfo_width() // 2, preview.winfo_height() // 2 + 28, image = util.preview_bg, anchor = "center", tag = "window")
        preview.create_image(preview.winfo_width() // 2, preview.winfo_height() // 2 + 28, image = util.preview, anchor = "center", tag = "accent")
        preview.create_image(preview.winfo_width() // 2, preview.winfo_height() // 2 + 28, image = util.preview_text, anchor = "center", tag = "text")

    if not (sys.platform == "win32" or sys.platform == "darwin") and dark_mode.get(): toggle_theme()

    util.fix_mouse_focus(window)
    preview.bind("<Configure>", on_resize)
    window.mainloop()

if __name__ == "__main__": main()