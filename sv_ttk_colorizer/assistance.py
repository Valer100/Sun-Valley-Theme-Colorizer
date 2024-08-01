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
    style.configure("Unselected.TButton", anchor = "w")
    style.configure("Unselected.TLabel", anchor = "w", padding = (12, 6, 12, 7))
    style.configure("Help.Vertical.TScrollbar", background = util.bg)

    def uncheck_all():
        for category in categories.winfo_children():
            if isinstance(category, ttk.Button): 
                category.configure(style = "Unselected.TLabel")
                conigure_category(category)

        clear_help_info()

    def conigure_category(category):
        category.bind("<Enter>", lambda event: category.configure(style = "Unselected.TButton"))
        category.bind("<Leave>", lambda event: category.configure(style = "Unselected.TLabel"))

    def select_category(category):
        category.bind("<Enter>", lambda event: None)
        category.bind("<Leave>", lambda event: None)
        category.configure(style = "Selected.Accent.TButton")

    def show_faq(): 
        uncheck_all()
        show_help_info("How can I use this tool?", "heading")
        show_help_info("\nChoose the accent color you want using the slider and enable/disable options to your liking. When you're done, click the \"Save\" button and save the modified theme in your project's root folder. That's it.\n\n")
        show_help_info("What's this package doing?", "heading")
        show_help_info("\nAt your choice, this package downloads the theme from GitHub or copies it from site-packages, changes the hue for the widgets by modifying some files and saves the modified theme anywhere you want.\n\n")
        select_category(category_faq)

    def show_give_feedback():
        uncheck_all()
        show_help_info("Give feedback", "heading")
        show_help_info("\nIs something unexpected happening? Do you have suggestions for new features or improvements to this package? Or you simply have a question and want to get an answer to it? You can give us your feedback on our GitHub repository. Just open a new issue and start talking to us. Here's a link to it:\n\n")
        show_help_info("https://github.com/Valer100/Sun-Valley-Theme-Colorizer", "link")
        select_category(category_feedback)

    def show_color_constants():
        uncheck_all()
        show_help_info("Color constants", "heading")
        show_help_info("\nIf you enable the ")
        show_help_info("Add color constants for programmatic access", "bold")
        show_help_info(" option, a few color constants will be added to the sv_ttk module. Here are all of them:\n\n")
        show_help_info(" background ", "code_reference")
        show_help_info(" / ")
        show_help_info(" bg ", "code_reference")
        show_help_info(" - returns the background color\n\n")
        show_help_info(" foreground ", "code_reference")
        show_help_info(" / ")
        show_help_info(" fg ", "code_reference")
        show_help_info(" - returns the foreground color\n\n")
        show_help_info(" foreground_disabled ", "code_reference")
        show_help_info(" / ")
        show_help_info(" fg_dis ", "code_reference")
        show_help_info(" - returns the foreground color for disabled widgets\n\n")
        show_help_info(" selected_background ", "code_reference")
        show_help_info(" / ")
        show_help_info(" sel_bg ", "code_reference")
        show_help_info(" - returns the selected background color (for selected text)\n\n")
        show_help_info(" selected_foreground ", "code_reference")
        show_help_info(" / ")
        show_help_info(" sel_fg ", "code_reference")
        show_help_info(" - returns the selected foreground color (for selected text)\n\n")
        show_help_info(" accent ", "code_reference")
        show_help_info(" - returns the accent color\n\n")
        show_help_info("How can I use them?", "heading")
        show_help_info("\nThis basic example shows you how can you set a tk Frame's background color to the accent color (you can do more than just that):\n\n")
        show_help_info("\nframe = tkinter.Frame(root, background = sv_ttk.accent)\nframe.pack()\n\n", "code")
        select_category(category_color_constants)

    category_faq = ttk.Button(categories, text = "Getting started", width = 23, style = "Selected.Accent.TButton", command = show_faq)
    category_faq.pack()

    category_color_constants = ttk.Button(categories, text = "Color constants", width = 23, style = "Selected.Accent.TButton", command = show_color_constants)
    category_color_constants.pack(pady = (8, 0))

    category_feedback = ttk.Button(categories, text = "Give feedback", width = 23, style = "Unselected.TLabel", command = show_give_feedback)
    category_feedback.pack(pady = (8, 0))

    ttk.Separator(frame, orient = "vertical").pack(side = "left", fill = "y")

    help_frame = tk.Frame(frame)
    help_frame.pack(side = "left", fill = "both", expand = True)

    ttk.Separator(help_frame, orient = "vertical").pack(fill = "x")

    frame2 = tk.Frame(help_frame, bg = util.bg)
    frame2.pack(fill = "both", expand = True)

    help_info = tk.Text(frame2, width = 60, height = 23, wrap = "word", bg = util.bg, bd = 0, highlightthickness = 0,
                        font = ("Segoe UI", 11), padx = 16, pady = 16, state = "disabled")
    help_info.pack(side = "left", fill = "both", expand = True)
    help_info.tag_configure("normal", font = ("Segoe UI", 11))
    help_info.tag_configure("bold", font = ("Segoe UI Bold", 11))
    help_info.tag_configure("link", font = ("Segoe UI Semibold", 11), underline = True, foreground = util.accent, selectforeground = "#FFFFFF")
    help_info.tag_configure("heading", font = ("Segoe UI Semibold", 17), spacing3 = 7)
    help_info.tag_configure("code", rmargin = 16, lmargin1 = 16, font = ("Consolas", 11), background = "#000000", foreground = "#FFFFFF", selectbackground = "#00417e")
    help_info.tag_configure("code_reference", font = ("Consolas", 11), background = util.reference, foreground = "#FFFFFF", selectbackground = "#00417e")

    scrollbar = util.AutoScrollbar(frame2, command = help_info.yview, style = "Help.Vertical.TScrollbar")
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

    util.fix_mouse_focus(window)
    window.focus_set()
    window.grab_set()
    window.update()
    geometry = window.geometry().split("+")[0].split("x")
    window.minsize(width = geometry[0], height = geometry[1])