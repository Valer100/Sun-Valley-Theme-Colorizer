import tkinter as tk, sv_ttk, darkdetect, os, shutil, sys, subprocess
from tkinter import ttk, filedialog as fd, messagebox as msg
from tkscrollframe import ScrollFrame
from urllib.request import urlretrieve
from zipfile import ZipFile

def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    window = tk.Tk()
    window.title("Sun Valley Theme Colorizer")

    if sys.platform == "win32" or sys.platform == "darwin": window.state("zoomed")
    else: window.wm_attributes("-zoomed", True)

    window.minsize(width = 1307, height = 579)
    window.configure()

    dm_titlebars = tk.BooleanVar(value = False)
    menu_revert_colors = tk.BooleanVar(value = False)
    accent_funcs = tk.BooleanVar(value = False)
    fix_lag = tk.BooleanVar(value = False)
    include_examplepy = tk.BooleanVar(value = True)
    include_config = tk.BooleanVar(value = True)

    try: import util, assistance
    except Exception as e: from sv_ttk_colorizer import util, assistance # type: ignore

    util.set_title_bar_color(window, darkdetect.theme().lower())

    print("Sun Valley Theme Colorizer - version 1.2.0")
    print("Work path: " + util.root_folder)

    title = ttk.Frame(window)
    title.pack(fill = "x", pady = (8, 0))

    ttk.Label(title, text = "Sun Valley Theme Colorizer", font = ("Segoe UI Semibold", 20)).pack(side = "left", padx = 16)

    theme_switch = ttk.Checkbutton(title, text = "Dark Mode", style = "Switch.TCheckbutton", command = lambda: toggle_theme())
    if not sys.platform == "win32" or sys.platform == "darwin": theme_switch.pack(side = "right", fill = "y", padx = (0, 16))

    frame = tk.Frame(window, bg = util.bg)
    frame.pack(pady = (16, 0), fill = "both", expand = True)

    frame2 = tk.Frame(frame, bg = util.bg)
    frame2.pack(fill = "both", expand = True, side = "left")

    ttk.Separator(frame2, orient = "horizontal").pack(fill = "x")

    preview_frame = tk.Frame(frame2, bg = util.bg)
    preview_frame.pack(fill = "y", padx = 16, pady = 16, expand = True, side = "left")

    preview_image = tk.Canvas(preview_frame, bg = util.bg, width = util.preview_bg.width(), height = util.preview.height(), bd = 0, highlightthickness = 0)
    preview_image.pack(side = "left")
    preview_image.create_image(0, 0, image = util.preview_bg, anchor = "nw")

    options_frame = ttk.Frame(frame, padding = (24, 8, 0, 24))
    options_frame.pack(side = "right", anchor = "n", fill = "y")

    ttk.Separator(frame, orient = "vertical").pack(side = "right", fill = "y")

    def update_preview(event):
        if hue.focus_get():
            window.configure(cursor = "watch")
            window.update()
            util.update_preview(hue.get())
            util.update_accents()
            preview_image.create_image(0, 0, image = util.preview, anchor = "nw")
            preview_image.create_image(0, 0, image = util.preview_text, anchor = "nw")
            window.configure(cursor = "arrow")

    def gen_export_file(): 
        return f'''// This is a Sun Valley Theme Colorizer configuration file.
// Do not edit it by hand or unexpected things will happen.

{str(hue.get())}
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
        file_path = fd.askopenfile(filetypes = [("Sun Valley Theme Colorizer configuration file", ".svttkc")], initialdir = util.desktop, initialfile = "config.svttkc")

        if not file_path == None:
            settings = open(file_path.name).read().split("\n")

            try:
                hue.set(float(settings[3]))
                update_preview(None)

                dm_titlebars.set(int(settings[4]))
                accent_funcs.set(int(settings[5]))
                fix_lag.set(int(settings[6]))
                include_examplepy.set(int(settings[7]))
                include_config.set(int(settings[8]))
                menu_revert_colors.set(int(settings[9]))

                msg.showinfo("Sun Valley Theme Colorizer", "The settings were imported.")
            except Exception as e: msg.showerror("Sun Valley Theme Colorizer", "Invalid configuration file or the configuration file was made using an older version of Sun Valley Theme Colorizer."); print(e)

    hue_img = tk.PhotoImage(file = "resources/color_range.png")

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

    ttk.Label(options, text = "Accent color").pack(anchor = "w", pady = (0, 8))

    hue_group = ttk.Frame(options)
    hue_group.pack(anchor = "w", pady = (0, 8))

    hue = ttk.Scale(hue_group, length = 250, from_= 0, to = 100)
    hue.pack(pady = (0, 5))
    hue.bind("<ButtonRelease>", update_preview)
    hue.bind("<KeyRelease>", update_preview)

    hue_image = ttk.Label(hue_group, image = hue_img)
    hue_image.pack()

    util.add_switch(options, "Dark Mode title bars on Windows", dm_titlebars)

    warning1 = ttk.Label(options, text = "This setting requires an additional dependency for your project: pywinstyles.", foreground = util.warning, wraplength = 270)
    warning1.pack(pady = (8, 0), anchor = "w")

    util.add_switch(options, "Don't change menu colors on Windows and macOS", menu_revert_colors)
    util.add_switch(options, "Add functions to get the accent colors", accent_funcs)

    warning2 = ttk.Label(options, text = "This option will add 2 new functions to the sv_ttk module: get_accent_color() and get_selection_accent_color()", foreground = util.warning, wraplength = 250)
    warning2.pack(pady = (8, 0), anchor = "w")

    util.add_switch(options, "Fix Toolbutton lag in complex layouts", fix_lag)
    util.add_switch(options, "Include a preview file to test the theme (\"example.py\")", include_examplepy)
    util.add_switch(options, "Include a configuration file with these settings (\"config.svttkc\")", include_config)

    def save_patch():
        save_to = fd.askdirectory(title = "Choose a folder to save the modified theme", initialdir = util.desktop)

        if not save_to == "":
            window.configure(cursor = "watch")
            util.disable_all_widgets(options)
            theme_switch.configure(state = "disabled")
            save.forget()
            help_btn.forget()

            status = ttk.Label(options_frame, text = "Downloading sv-ttk...", font = ("Segoe UI Semibold", 15))
            status.pack(side = "bottom", padx = (0, 24))

            window.update()
            if os.path.exists(util.root_folder + "/temp"): shutil.rmtree(util.root_folder + "/temp")
            os.mkdir(util.root_folder + "/temp")
            urlretrieve(util.latest_sv_ttk, util.root_folder + "/temp/sv_ttk.zip")

            window.update()
            status["text"] = "Unzipping sv-ttk..."
            ZipFile(util.root_folder + "/temp/sv_ttk.zip").extractall(util.root_folder + "/temp/sv_ttk repo")
            urlretrieve(util.sv_ttk_license, util.sv_ttk_download + "/LICENSE")
            shutil.copyfile(util.root_folder + "/resources/LICENSE_MODIFICATIONS", util.sv_ttk_download + "/LICENSE_MODIFICATIONS")

            window.update()
            status["text"] = "Patching files..."
            util.change_hue_and_save(util.sv_ttk_spritesheet_light, hue.get())
            util.change_hue_and_save(util.sv_ttk_spritesheet_dark, hue.get())

            if include_examplepy.get(): shutil.copyfile(util.root_folder + "/resources/example.py", util.sv_ttk_download + "/example.py")

            light_tcl = open(util.sv_ttk_light, "r").read().replace("#005fb8", util.accent_light).replace("#2f60d8", util.accent_light).replace("#c1d8ee", util.accent_dark)
            dark_tcl = open(util.sv_ttk_dark, "r").read().replace("#57c8ff", util.accent_dark).replace("#2f60d8", util.accent_light).replace("#25536a", util.accent_light)

            open(util.sv_ttk_light, "w").write(light_tcl)
            open(util.sv_ttk_dark, "w").write(dark_tcl)

            if dm_titlebars.get():
                os.remove(util.sv_ttk_download + "/__init__.py")
                urlretrieve(util.dm_titlebars_patch, util.sv_ttk_download + "/__init__.py")

            if accent_funcs.get():
                __init__file = open(util.sv_ttk_download + "/__init__.py", "r").read().replace(util.get_accents_patch_find, util.get_accents_patch_replace)
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

            if os.path.exists(save_to + "/sv_ttk"): 
                delete = msg.askyesno("Error", "The folder \"sv_ttk\" already exists in \"" + save_to + "\". The folder must be deleted to continue. Do you want to delete it?", icon = "error")

                if delete:
                    if os.path.exists(save_to + "/sv_ttk"): shutil.rmtree(save_to + "/sv_ttk")
                else: 
                    window.update()
                    window.configure(cursor = "arrow")
                    status.destroy()
                    save.pack(side = "bottom", fill = "x", padx = (0, 24))
                    help_btn.pack(side = "bottom", pady = (0, 8), fill = "x", padx = (0, 24))
                    util.enable_all_widgets(options)
                    theme_switch.configure(state = "enabled")

                    msg.showinfo("Sun Valley Theme Colorizer", "The save has been canceled.")
                    return

            shutil.move(util.sv_ttk_download, f"{save_to}/sv_ttk")
            shutil.rmtree(util.root_folder + "/temp")

            window.update()
            window.configure(cursor = "arrow")
            status.destroy()
            save.pack(side = "bottom", fill = "x", padx = (0, 24))
            help_btn.pack(side = "bottom", pady = (0, 8), fill = "x", padx = (0, 24))
            util.enable_all_widgets(options)
            theme_switch.configure(state = "enabled")

            if include_examplepy.get():
                show_preview = msg.askyesno("Sun Valley Theme Colorizer", "The theme has been successfully modified and saved. Do you want to see it in action?", icon = "info")
                if show_preview: subprocess.Popen(f"\"{sys.executable}\" \"{save_to}/sv_ttk/example.py\"", shell = True)
            else:
                msg.showinfo("Sun Valley Theme Colorizer", "The theme has been successfully modified and saved.")

    def toggle_theme():
        sv_ttk.toggle_theme()
        util.update_colors(sv_ttk.get_theme())
        warning1["foreground"] = util.warning
        warning2["foreground"] = util.warning
        frame["background"] = util.bg
        frame2["background"] = util.bg
        preview_frame["background"] = util.bg
        preview_image["background"] = util.bg

    save = ttk.Button(options_frame, text = "Save", style = "Accent.TButton", command = save_patch)
    save.pack(side = "bottom", fill = "x", padx = (0, 24))

    help_btn = ttk.Button(options_frame, text = "Help", command = assistance.show)
    help_btn.pack(side = "bottom", pady = (0, 8), fill = "x", padx = (0, 24))

    if sys.platform == "win32" or sys.platform == "darwin": sv_ttk.set_theme(darkdetect.theme())
    else: sv_ttk.set_theme("light")

    window.mainloop()

if __name__ == "__main__": main()