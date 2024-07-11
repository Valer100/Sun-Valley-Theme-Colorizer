import tkinter as tk, sv_ttk, darkdetect, os, shutil, sys
from tkinter import ttk, filedialog as fd, messagebox as msg
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
    tkmenus_fix = tk.BooleanVar(value = False)

    try: import util
    except Exception as e: from sv_ttk_colorizer import util; print(str(e)) # type: ignore

    util.set_title_bar_color(window, darkdetect.theme().lower())

    print("Sun Valley Theme Colorizer - version 1.1.0")
    print("Work path: " + util.root_folder)

    title = ttk.Frame(window)
    title.pack(fill = "x", pady = (8, 0))

    ttk.Label(title, text = "Sun Valley Theme Colorizer", font = ("Segoe UI Semibold", 20)).pack(side = "left", padx = 16)

    theme_switch = ttk.Checkbutton(title, text = "Dark Mode", style = "Switch.TCheckbutton", command = lambda: toggle_theme())
    if not sys.platform == "win32" or sys.platform == "darwin": theme_switch.pack(side = "right", fill = "y", padx = 16)

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

    options_frame = ttk.Frame(frame, padding = (24, 8, 24, 24))
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

    hue_img = tk.PhotoImage(file = "resources/color_range.png")

    ttk.Label(options_frame, text = "Accent color").pack(anchor = "w", pady = (0, 8))

    hue_group = ttk.Frame(options_frame)
    hue_group.pack()

    hue = ttk.Scale(hue_group, length = 250, from_= 0, to = 100)
    hue.pack(pady = (0, 5))
    hue.bind("<ButtonRelease>", update_preview)
    hue.bind("<KeyRelease>", update_preview)

    hue_image = ttk.Label(hue_group, image = hue_img)
    hue_image.pack()

    dark_mode_titlebars = ttk.Checkbutton(options_frame, text = "Dark mode title bars on Windows", style = "Switch.TCheckbutton", variable = dm_titlebars)
    dark_mode_titlebars.pack(pady = (32, 0))

    warning1 = ttk.Label(options_frame, text = "This setting requires an additional dependency for your project: pywinstyles.", foreground = util.warning, wraplength = 270)
    warning1.pack(pady = (8, 0))

    menus_fix = ttk.Checkbutton(options_frame, text = "Don't change menu colors on\nWindows and macOS", style = "Switch.TCheckbutton", variable = tkmenus_fix)
    menus_fix.pack(pady = (16, 0), fill = "x")

    def save_patch():
        save_to = fd.askdirectory(title = "Choose where to save the theme", initialdir = util.desktop)

        if not save_to == "":
            window.configure(cursor = "watch")
            hue.configure(state = "disabled")
            dark_mode_titlebars.configure(state = "disabled")
            menus_fix.configure(state = "disabled")
            theme_switch.configure(state = "disabled")
            save.forget()
            help.forget()

            status = ttk.Label(options_frame, text = "Downloading sv-ttk...", font = ("Segoe UI Semibold", 15))
            status.pack(side = "bottom")

            window.update()
            if os.path.exists(util.root_folder + "/temp"): shutil.rmtree(util.root_folder + "/temp")
            os.mkdir(util.root_folder + "/temp")
            urlretrieve(util.latest_sv_ttk, util.root_folder + "/temp/sv_ttk.zip")

            window.update()
            status["text"] = "Unzipping sv-ttk..."
            ZipFile(util.root_folder + "/temp/sv_ttk.zip").extractall(util.root_folder + "/temp/sv_ttk repo")
            urlretrieve(util.sv_ttk_license, util.sv_ttk_download + "/LICENSE")

            window.update()
            status["text"] = "Patching files..."
            util.change_hue_and_save(util.sv_ttk_spritesheet_light, hue.get())
            util.change_hue_and_save(util.sv_ttk_spritesheet_dark, hue.get())

            light_tcl = open(util.sv_ttk_light, "r").read().replace("#005fb8", util.accent_light).replace("#2f60d8", util.accent_light).replace("#c1d8ee", util.accent_dark)
            dark_tcl = open(util.sv_ttk_dark, "r").read().replace("#57c8ff", util.accent_dark).replace("#2f60d8", util.accent_light).replace("#25536a", util.accent_light)

            open(util.sv_ttk_light, "w").write(light_tcl)
            open(util.sv_ttk_dark, "w").write(dark_tcl)

            if dm_titlebars.get():
                os.remove(util.sv_ttk_download + "/__init__.py")
                urlretrieve(util.dm_titlebars_patch, util.sv_ttk_download + "/__init__.py")

            if tkmenus_fix.get():
                sv_tcl = open(util.sv_ttk_sv, "r").read().replace(util.menus_patch_find, util.menus_patch_replace)
                open(util.sv_ttk_sv, "w").write(sv_tcl)

            if os.path.exists(save_to + "/sv_ttk"): 
                delete = msg.askyesno("Error", "The folder \"sv_ttk\" already exists in \"" + save_to + "\". The folder must be deleted to continue. Do you want to delete it?", icon = "error")

                if delete:
                    if os.path.exists(save_to + "/sv_ttk"): shutil.rmtree(save_to + "/sv_ttk")
                else: 
                    window.update()
                    window.configure(cursor = "arrow")
                    status.destroy()
                    save.pack(side = "bottom", fill = "x")
                    help.pack(side = "bottom", pady = (0, 8), fill = "x")
                    hue.configure(state = "enabled")
                    dark_mode_titlebars.configure(state = "enabled")
                    menus_fix.configure(state = "enabled")
                    theme_switch.configure(state = "enabled")

                    msg.showinfo("Sun Valley Theme Colorizer", "The save has been canceled.")
                    return

            shutil.move(util.sv_ttk_download, f"{save_to}/sv_ttk")
            shutil.rmtree(util.root_folder + "/temp")

            window.update()
            window.configure(cursor = "arrow")
            status.destroy()
            save.pack(side = "bottom", fill = "x")
            help.pack(side = "bottom", pady = (0, 8), fill = "x")
            hue.configure(state = "enabled")
            dark_mode_titlebars.configure(state = "enabled")
            menus_fix.configure(state = "enabled")
            theme_switch.configure(state = "enabled")

            msg.showinfo("Sun Valley Theme Colorizer", "The theme has been successfully modified and saved.")

    def help_me(): msg.showinfo("Help", "1) What's this app doing?\n\nThis app downloads sv_ttk from GitHub, changes the hue for the widgets by modifying some files and saves the modified module anywhere you want.\n\n\n2) How do I use the folder in my project?\n\nSimply put the folder in your project's root folder and you're done. It should work.")

    def toggle_theme():
        sv_ttk.toggle_theme()
        util.update_colors(sv_ttk.get_theme())
        warning1["foreground"] = util.warning
        frame["background"] = util.bg
        frame2["background"] = util.bg
        preview_frame["background"] = util.bg
        preview_image["background"] = util.bg

    save = ttk.Button(options_frame, text = "Save", style = "Accent.TButton", command = save_patch)
    save.pack(side = "bottom", fill = "x")

    help = ttk.Button(options_frame, text = "Help", command = help_me)
    help.pack(side = "bottom", pady = (0, 8), fill = "x")

    if sys.platform == "win32" or sys.platform == "darwin": sv_ttk.set_theme(darkdetect.theme())
    else: sv_ttk.set_theme("light")

    window.mainloop()

if __name__ == "__main__": main()