import tkinter as tk, sv_ttk
from tkinter import ttk

try: import util
except Exception as e: from sv_ttk_colorizer import util # type: ignore

def show():
    window = tk.Toplevel()
    window.title("Help")
    util.set_title_bar_color(window, sv_ttk.get_theme())

    ttk.Label(window, text = "Help", font = ("Segoe UI Semibold", 20)).pack(padx = 16, pady = (8, 0), anchor = "w")

    frame = ttk.Frame(window)
    frame.pack(fill = "both", expand = True)

    categories = ttk.Frame(frame, padding = 16)
    categories.pack(side = "left", anchor = "n")

    style = ttk.Style()
    style.configure("Selected.Accent.TButton", anchor = "w")
    style.configure("Unselected.Toolbutton", anchor = "w")

    def uncheck_all():
        for category in categories.winfo_children():
            if isinstance(category, ttk.Button): category.configure(style = "Unselected.Toolbutton")

        clear_help_info()

    def show_faq(): 
        uncheck_all()
        show_help_info("What's this package doing?", "heading")
        show_help_info("\nThis package downloads sv_ttk from GitHub, changes the hue for the widgets by modifying some files and saves the modified module anywhere you want.\n\n")
        show_help_info("How do I use the folder in my project?", "heading")
        show_help_info("\nSimply put the folder in your project's root folder and you're done. It should work.\n\n")
        show_help_info("Why is the package stuck at \"Downloading sv_ttk...\" stage?", "heading")
        show_help_info("\nThat may happen because you're not connected to the Internet or your Internet connection signal strength is weak. Try waiting a few minutes. If nothing happens, check your Internet connection and try again.")
        category_faq["style"] = "Selected.Accent.TButton"

    def show_menu_colors(): 
        uncheck_all()
        show_help_info("Why do menus have a white border when using this theme with the dark mode variant?", "heading")
        show_help_info("\nThis theme also changes the background color of the menus. But on Windows, if the background color of the menus is changed, there will be a white border. The only way to fix this is to revert the colors of the menu back to default. Here's how you can do this:\n\n")
        show_help_info("yourmenu.configure(bg=\"SystemMenu\", fg=\"SystemMenuText\")", "code")
        show_help_info("\n\nReplace yourmenu with the reference to your menu. Make sure to only run this code on Windows, because on Linux the menus colors look just fine. You can do that using the sys module. The final code would look like this:\n\n")
        show_help_info("import sys\n\n# Making sure the code runs only on Windows\nif sys.platform == \"win32\":\n    yourmenu.configure(bg=\"SystemMenu\", fg=\"SystemMenuText\")", "code")
        category_menu_colors["style"] = "Selected.Accent.TButton"

    def show_give_feedback():
        uncheck_all()
        show_help_info("Give feedback", "heading")
        show_help_info("\nIs something unexpected happening? Do you have suggestions for new features or improvements to this packages? Or you simply want to ask a question and get an answer about this package? You can give us feedback on our GitHub repository. Just open a new Issue and give us your feedback. Here's a link to the GitHub repository:\n\n")
        show_help_info("https://github.com/Valer100/Sun-Valley-Theme-Colorizer", "link")
        category_feedback["style"] = "Selected.Accent.TButton"

    category_faq = ttk.Button(categories, text = "Frequently asked questions", width = 25, style = "Selected.Accent.TButton", command = show_faq)
    category_faq.pack()
    
    category_menu_colors = ttk.Button(categories, text = "Menu white borders", width = 25, style = "Unselected.Toolbutton", command = show_menu_colors)
    category_menu_colors.pack(pady = (8, 0))

    category_feedback = ttk.Button(categories, text = "Give feedback", width = 25, style = "Unselected.Toolbutton", command = show_give_feedback)
    category_feedback.pack(pady = (8, 0))

    ttk.Separator(frame, orient = "vertical").pack(side = "left", fill = "y")

    help_frame = tk.Frame(frame)
    help_frame.pack(side = "left", fill = "both", expand = True)

    ttk.Separator(help_frame, orient = "vertical").pack(fill = "x")

    frame2 = tk.Frame(help_frame, bg = util.bg)
    frame2.pack(fill = "both", expand = True)

    help_info = tk.Text(frame2, width = 70, height = 25, wrap = "word", bg = util.bg, bd = 0, highlightthickness = 0,
                        font = ("Segoe UI", 11), padx = 16, pady = 16, state = "disabled")
    help_info.pack(side = "left", fill = "both", expand = True)
    help_info.tag_configure("normal", font = ("Segoe UI", 11))
    help_info.tag_configure("link", font = ("Segoe UI Semibold", 11), underline = True, foreground = util.accent, selectforeground = "#FFFFFF")
    help_info.tag_configure("heading", font = ("Segoe UI Semibold", 17), spacing3 = 7)
    help_info.tag_configure("code", font = ("Consolas", 11))

    style = ttk.Style()
    style.configure("TScrollbar", background = util.bg)

    scrollbar = ttk.Scrollbar(frame2, orient = "vertical", command = help_info.yview)
    scrollbar.pack(side = "left", fill = "y", pady = 4)

    help_info.configure(yscrollcommand = scrollbar.set)

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
    window.grab_set()
    window.update()
    geometry = window.geometry().split("+")[0].split("x")
    window.minsize(width = geometry[0], height = geometry[1])