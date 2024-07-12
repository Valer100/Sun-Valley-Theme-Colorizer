import tkinter as tk
from tkinter import ttk

try: import __init__ as sv_ttk
except: import sv_ttk

window = tk.Tk()
window.title("Sun Valley Demo")
window.configure(padx = 16, pady = 4)

checked = tk.BooleanVar(value = True)
unchecked = tk.BooleanVar(value = False)
disabled = tk.BooleanVar(value = False)
menu_bool = tk.BooleanVar(value = False)
radio = tk.StringVar(value = "1")
radio_enabled = tk.StringVar(value = "1")
option = tk.StringVar(value = "Python")
progress = tk.IntVar(value = 0)

test_menu = tk.Menu()
for i in range(5):
    test_menu.add_command(label = f"Option {str(i + 1)}")

fruits = ["Apple", "Banana", "Orange", "Strawberry", "Pear"]
vegetables = ["Tomato", "Potato", "Cabbage", "Onion", "Garlic"]
programming_langs = ["Python", "Java", "C++", "C#", "Javascript"]

menu = tk.Menu()
menu.add_cascade(label = "File", menu = test_menu)
menu.add_cascade(label = "Edit", menu = test_menu)
menu.add_cascade(label = "View", menu = test_menu)
menu.add_cascade(label = "Options", menu = test_menu)
menu.add_cascade(label = "Help", menu = test_menu)


ttk.Label(window, text = "Sun Valley Theme Demo", font = ("Segoe UI Semibold", 20)).pack(anchor = "w")


notebook = ttk.Notebook(window)
notebook.pack(pady = 16, fill = "both", expand = True)

frame = ttk.Frame(notebook, padding = 8)
frame.pack(fill = "both", expand = True)

commands = ttk.Frame(notebook, padding = 16)
commands.pack(fill = "x")

notebook.add(text = "Widgets", child = frame)
notebook.add(text = "Commands", child = commands)

frame1 = ttk.Frame(frame)
frame1.pack()

main = ttk.Frame(frame1)
main.pack(side = "left")

row1 = ttk.Frame(main)
row1.pack()


checkboxes = ttk.Labelframe(row1, text = "Checkbuttons", padding = 4)
checkboxes.pack(side = "left", fill = "y")

ttk.Checkbutton(checkboxes, text = "Checked", variable = checked, width = 15).pack(anchor = "w", padx = 4, pady = 4)
ttk.Checkbutton(checkboxes, text = "Unhecked", variable = unchecked, width = 15).pack(anchor = "w", padx = 4, pady = 4)
ttk.Checkbutton(checkboxes, text = "Disabled", variable = disabled, state = "disabled", width = 15).pack(anchor = "w", padx = 4, pady = 4)


buttons = ttk.Labelframe(row1, text = "Buttons", padding = 4)
buttons.pack(side = "left", padx = (16, 0))

ttk.Button(buttons, text = "Toolbutton", width = 27, style = "Toolbutton").pack(anchor = "w", padx = 8, pady = 4)
ttk.Button(buttons, text = "Button", width = 27).pack(anchor = "w", padx = 8, pady = 4)
ttk.Button(buttons, text = "Accent Button", width = 27, style = "Accent.TButton").pack(anchor = "w", padx = 8, pady = 4)


row2 = ttk.Frame(main)
row2.pack(pady = (16, 0))


radiobuttons = ttk.Labelframe(row2, text = "Radiobuttons", padding = 4)
radiobuttons.pack(side = "left", fill = "y")

ttk.Radiobutton(radiobuttons, text = "Selected", width = 15, variable = radio, value = "1").pack(anchor = "w", padx = 4, pady = 4)
ttk.Radiobutton(radiobuttons, text = "Unselected", width = 15, variable = radio, value = "2").pack(anchor = "w", padx = 4, pady = 4)
ttk.Radiobutton(radiobuttons, text = "Disabled", width = 15, state = "disabled").pack(anchor = "w", padx = 4, pady = 4)


input = ttk.Labelframe(row2, text = "Input", padding = 4)
input.pack(side = "left", padx = (16, 0))

entry = ttk.Entry(input)
entry.pack(padx = 8, pady = 4, fill = "x")
entry.insert(0, "Type here...")

combo = ttk.Combobox(input, values = fruits)
combo.pack(padx = 8, pady = 4, fill = "x")
combo.insert(0, "Apple")


spinbox = ttk.Spinbox(input, from_ = 0, to = 100)
spinbox.pack(padx = 8, pady = 4, fill = "x")
spinbox.insert(0, 40)


other = ttk.LabelFrame(frame1, text = "Other widgets", padding = 4)
other.pack(side = "left", padx = (16, 0))

ttk.Menubutton(other, menu = test_menu, text = "Menubutton", width = 25).pack(padx = 8, pady = 4)
ttk.OptionMenu(other, option, programming_langs[0], *programming_langs).pack(padx = 8, pady = 4, fill = "x")

readonlycombo = ttk.Combobox(other, state = "readonly", values = vegetables)
readonlycombo.pack(padx = 8, pady = 4, fill = "x")
readonlycombo.current(0)

ttk.Separator(other, orient = "horizontal").pack(padx = 4, pady = 8, fill = "x")

scale = ttk.Scale(other, orient = "horizontal", from_ = 0, to = 100, command = lambda e: progress.set(scale.get()))
scale.pack(padx = 8, pady = 4, fill = "x")

progressbar = ttk.Progressbar(other, maximum = 100, orient = "horizontal", variable = progress)
progressbar.pack(padx = 8, pady = 4, fill = "x")

ttk.Separator(other, orient = "horizontal").pack(padx = 4, pady = 8, fill = "x")

ttk.Checkbutton(other, text = "Switch", style = "Switch.TCheckbutton").pack(padx = 8, pady = 4, fill = "x")
ttk.Checkbutton(other, text = "Toggle Button", style = "Toggle.TButton").pack(padx = 8, pady = 4, fill = "x")

def show_menu():
    if menu_bool.get(): window.configure(menu = menu)
    else: window.configure(menu = "")

ttk.Label(commands, text = "Commands", font = ("Segoe UI Semibold", 18)).pack(anchor = "w", pady = (0, 18))

ttk.Checkbutton(commands, text = "Dark Mode", command = sv_ttk.toggle_theme, style = "Switch.TCheckbutton").pack(anchor = "w")
ttk.Checkbutton(commands, text = "Show menu", variable = menu_bool, command = show_menu).pack(anchor = "w", pady = (10, 0))
ttk.Button(commands, text = "Open Toplevel", command = tk.Toplevel).pack(anchor = "w", pady = (10, 0))

sv_ttk.set_theme("light")
window.mainloop()