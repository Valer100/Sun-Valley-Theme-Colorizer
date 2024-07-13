import tkinter as tk, sv_ttk
from tkinter import ttk

try: import util
except Exception as e: from sv_ttk_colorizer import util # type: ignore

def show():
    window = tk.Toplevel()
    window.grab_set()
    window.title("Help")
    util.set_title_bar_color(window, sv_ttk.get_theme())

    ttk.Label(window, text = "Help", font = ("Segoe UI Semibold", 20)).pack(padx = 16, pady = (8, 0), anchor = "w")

    frame = ttk.Frame(window)
    frame.pack(fill = "both", expand = True)

    categories = ttk.Frame(frame, padding = 16)
    categories.pack(side = "left", anchor = "n")

    def uncheck_all():
        for category in categories.winfo_children():
            if isinstance(category, ttk.Button): category.configure(style = "Toolbutton")

        clear_help_info()

    def show_faq(): 
        uncheck_all()
        show_help_info("What's this package doing?", "heading")
        show_help_info("\nThis package downloads sv_ttk from GitHub, changes the hue for the widgets by modifying some files and saves the modified module anywhere you want.\n\n")
        show_help_info("How do I use the folder in my project?", "heading")
        show_help_info("\nSimply put the folder in your project's root folder and you're done. It should work.\n\n")
        show_help_info("Do I need an Internet connection to use this package?", "heading")
        show_help_info("\nUnfortunately, yes. This app downloads the theme from its GitHub repository, to make sure it is up to date.")
        category_faq["style"] = "Accent.TButton"

    def show_menu_colors(): 
        uncheck_all()
        show_help_info("Why do menus have a white border when using this theme with the dark mode variant?", "heading")
        show_help_info("\nThis theme also changes the background color of the menus. But on Windows, if the background color of the menus is changed, there will be a white border. The only way to fix this is to revert the colors of the menu back to default. Here's how you can do this:")
        show_help_info("\n\nyourmenu.configure(bg=\"SystemMenu\", fg=\"SystemMenuText\")", "code")
        show_help_info("\n\nReplace yourmenu with the reference to your menu. Make sure to only run this code on Windows, because on Linux the menus colors look just fine. You can do that using the sys module. The final code would look like this:")
        show_help_info("\n\nimport sys\n\n# Making sure the code runs only on Windows\nif sys.platform == \"win32\":\n    yourmenu.configure(bg=\"SystemMenu\", fg=\"SystemMenuText\")", "code")
        category_menu_colors["style"] = "Accent.TButton"

    category_faq = ttk.Button(categories, text = "Frequently asked questions", width = 30, style = "Accent.TButton", command = show_faq)
    category_faq.pack()
    
    category_menu_colors = ttk.Button(categories, text = "Menu white borders on Windows", width = 30, style = "Toolbutton", command = show_menu_colors)
    category_menu_colors.pack(pady = (8, 0))

    ttk.Separator(frame, orient = "vertical").pack(side = "left", fill = "y")

    help_frame = tk.Frame(frame)
    help_frame.pack(side = "left", fill = "both", expand = True)

    ttk.Separator(help_frame, orient = "vertical").pack(fill = "x")

    help_info = tk.Text(help_frame, width = 70, height = 25, wrap = "word", bg = util.bg, bd = 0, highlightthickness = 0,
                        font = ("Segoe UI", 11), padx = 16, pady = 16, state = "disabled")
    help_info.pack(fill = "both", expand = True)
    help_info.tag_configure("normal", font = ("Segoe UI", 11))
    help_info.tag_configure("heading", font = ("Segoe UI Semibold", 17), spacing3 = 10)
    help_info.tag_configure("code", font = ("Consolas", 11))

    def show_help_info(help, tag = "normal"):
        help_info.configure(state = "normal")
        help_info.insert("end", help, tag)
        help_info.configure(state = "disabled")

    def clear_help_info():
        help_info.configure(state = "normal")
        help_info.delete("1.0", "end")
        help_info.configure(state = "disabled")

    show_faq()

    window.focus_set()
    window.mainloop()