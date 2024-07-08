import tkinter as tk, sv_ttk, darkdetect, os, shutil, sys
from tkinter import ttk, filedialog as fd, messagebox as msg
from urllib.request import urlretrieve
from zipfile import ZipFile

def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    window = tk.Tk()
    window.title("Sun Valley Theme Colorizer")
    window.minsize(width = 1016, height = 579)
    window.configure(padx = 16, pady = 8)

    if darkdetect.isDark(): bg = "#1c1c1c"
    else: bg = "#fafafa"

    try: import util
    except: from sv_ttk_colorizer import util # type: ignore

    util.set_title_bar_color(window, darkdetect.theme().lower())

    print("Sun Valley Theme Colorizer - version 1.0.0")
    print("Work path: " + util.root_folder)

    title = ttk.Frame(window)
    title.pack(fill = "x")

    ttk.Label(title, text = "Sun Valley Theme Colorizer", font = ("Segoe UI Semibold", 20)).pack(side = "left")

    theme_switch = ttk.Checkbutton(title, text = "Dark Mode", style = "Switch.TCheckbutton", command = lambda: toggle_theme())
    if not sys.platform == "win32" or sys.platform == "darwin": theme_switch.pack(side = "right", fill = "y")

    preview_back = ttk.Frame(window)
    preview_back.pack(pady = (20, 0), padx = 16, fill = "both", expand = True)

    preview_frame = ttk.Frame(preview_back)
    preview_frame.pack(fill = "y", pady = 16, expand = True)

    preview_image = tk.Canvas(preview_frame, bg = bg, width = util.preview_bg.width(), height = util.preview.height(), bd = 0, highlightthickness = 0)
    preview_image.pack(side = "left")
    preview_image.create_image(0, 0, image = util.preview_bg, anchor = "nw")

    buttons_frame = ttk.Frame(window)
    buttons_frame.pack(side = "bottom", pady = (16, 8), fill = "x")

    ttk.Label(buttons_frame, text = "Hue:", font = ("Segoe UI Semibold", 15)).pack(side = "left")

    def update_preview(event):
        window.configure(cursor = "watch")
        window.update()
        util.update_preview(hue.get())
        util.update_accents()
        preview_image.create_image(0, 0, image = util.preview, anchor = "nw")
        preview_image.create_image(0, 0, image = util.preview_text, anchor = "nw")
        window.configure(cursor = "arrow")

    hue_img = tk.PhotoImage(file = "resources/color_range.png")

    hue_group = ttk.Frame(buttons_frame)
    hue_group.pack(padx = (16, 0), side = "left")

    hue = ttk.Scale(hue_group, length = 250, from_= 0, to = 100)
    hue.pack(pady = (0, 5))
    hue.bind("<ButtonRelease-1>", update_preview)

    hue_image = ttk.Label(hue_group, image = hue_img)
    hue_image.pack()

    def save_patch():
        save_to = fd.askdirectory(title = "Choose where to save the theme")

        if not save_to == "":
            window.configure(cursor = "watch")
            hue.configure(state = "disabled")
            theme_switch.configure(state = "disabled")
            save.forget()
            help.forget()

            status = ttk.Label(buttons_frame, text = "Downloading sv-ttk...", font = ("Segoe UI Semibold", 15))
            status.pack(side = "right")

            window.update()
            if os.path.exists(util.root_folder + "/temp"): shutil.rmtree(util.root_folder + "/temp")
            os.mkdir(util.root_folder + "/temp")
            urlretrieve(util.latest_sv_ttk, util.root_folder + "/temp/sv_ttk.zip")

            window.update()
            status["text"] = "Unzipping sv-ttk..."
            ZipFile(util.root_folder + "/temp/sv_ttk.zip").extractall(util.root_folder + "/temp/sv_ttk repo")

            window.update()
            status["text"] = "Patching files..."
            util.change_hue_and_save(util.sv_ttk_spritesheet_light, hue.get())
            util.change_hue_and_save(util.sv_ttk_spritesheet_dark, hue.get())

            light_tcl = open(util.sv_ttk_light, "r").read().replace("#005fb8", util.accent_light).replace("#2f60d8", util.accent_light).replace("#c1d8ee", util.accent_dark)
            dark_tcl = open(util.sv_ttk_dark, "r").read().replace("#57c8ff", util.accent_dark).replace("#2f60d8", util.accent_light).replace("#25536a", util.accent_light)

            open(util.sv_ttk_light, "w").write(light_tcl)
            open(util.sv_ttk_dark, "w").write(dark_tcl)

            if os.path.exists(save_to + "/sv_ttk"): 
                delete = msg.askyesno("Error", "The folder \"sv_ttk\" already exists in \"" + save_to + "\". The folder must be deleted to continue. Do you want to delete it?", icon = "error")

                if delete:
                    if os.path.exists(save_to + "/sv_ttk"): shutil.rmtree(save_to + "/sv_ttk")
                else: 
                    window.update()
                    window.configure(cursor = "arrow")
                    status.destroy()
                    save.pack(side = "right")
                    help.pack(side = "right", padx = (0, 8))
                    hue.configure(state = "enabled")
                    theme_switch.configure(state = "enabled")

                    msg.showinfo("Sun Valley Theme Colorizer", "The save has been canceled.")
                    return

            shutil.move(util.sv_ttk_download, f"{save_to}/sv_ttk")
            shutil.rmtree(util.root_folder + "/temp")

            window.update()
            window.configure(cursor = "arrow")
            status.destroy()
            save.pack(side = "right")
            help.pack(side = "right", padx = (0, 8))
            hue.configure(state = "enabled")
            theme_switch.configure(state = "enabled")

            msg.showinfo("Sun Valley Theme Colorizer", "The theme has been successfully modified and saved.")

    def help_me(): msg.showinfo("Help", "1) What's this app doing?\n\nThis app downloads sv_ttk from GitHub, changes the hue for the widgets by modifying some files and saves the modified module anywhere you want.\n\n\n2) How do I use the folder in my project?\n\nSimply put the folder in your project's root folder and you're done. It should work.")

    def toggle_theme():
        sv_ttk.toggle_theme()

        if sv_ttk.get_theme() == "dark": bg = "#1c1c1c"
        else: bg = "#fafafa"

    save = ttk.Button(buttons_frame, text = "Save", style = "Accent.TButton", width = 15, command = save_patch)
    save.pack(side = "right")

    help = ttk.Button(buttons_frame, text = "Help", width = 15, command = help_me)
    help.pack(side = "right", padx = (0, 8))

    if sys.platform == "win32" or sys.platform == "darwin": sv_ttk.set_theme(darkdetect.theme())
    else: sv_ttk.set_theme("light")
    window.mainloop()

if __name__ == "__main__": main()