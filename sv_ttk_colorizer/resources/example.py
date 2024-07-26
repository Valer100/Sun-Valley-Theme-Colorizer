import tkinter as tk, sys
from tkinter import ttk, messagebox as msg, filedialog as fd

try: import __init__ as sv_ttk
except: import sv_ttk

window = tk.Tk()
window.title("Sun Valley Demo")
window.minsize(width = 799, height = 456)
sv_ttk.set_theme("light")

icon = tk.PhotoImage(data = "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")
window.iconphoto(True, icon)

checked = tk.BooleanVar(value = True)
unchecked = tk.BooleanVar(value = False)
disabled = tk.BooleanVar(value = False)
native_menu_bool = tk.BooleanVar(value = False)
custom_menu_bool = tk.BooleanVar(value = False)
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
menu.add_cascade(label = "Help", menu = test_menu)

# Custom menu bar
menu_bar = ttk.Frame(window)
menu_bar_frame = ttk.Frame(menu_bar, padding = (4, 0, 4, 4))
menu_bar_frame.pack(fill = "x")

if not sys.platform == "win32": menu_bar_frame.configure(padding = 4)

ttk.Separator(menu_bar, orient = "horizontal").pack(fill = "x")
ttk.Menubutton(menu_bar_frame, text = "File", menu = test_menu, style = "Toolbutton", padding = (8, 1, 8, 1)).pack(side = "left")
ttk.Menubutton(menu_bar_frame, text = "Edit", menu = test_menu, style = "Toolbutton", padding = (8, 1, 8, 1)).pack(side = "left")
ttk.Menubutton(menu_bar_frame, text = "View", menu = test_menu, style = "Toolbutton", padding = (8, 1, 8, 1)).pack(side = "left")
ttk.Menubutton(menu_bar_frame, text = "Help", menu = test_menu, style = "Toolbutton", padding = (8, 1, 8, 1)).pack(side = "left")

title = ttk.Label(window, text = "Sun Valley Theme Demo", font = ("Segoe UI Semibold", 20))
title.pack(padx = 16, pady = (8, 0), side = "top", anchor = "w")

notebook = ttk.Notebook(window)
notebook.pack(pady = 16, padx = 16, fill = "both", expand = True, side = "bottom")

frame = ttk.Frame(notebook, padding = 16)
frame.pack(fill = "both", expand = True)

options = ttk.Frame(notebook, padding = 16)
options.pack(fill = "x")

scrollbar_example = ttk.Frame(notebook, width = 751)
scrollbar_example.pack(fill = "x")

notebook.add(text = "Widgets", child = frame)
notebook.add(text = "Scrollbar", child = scrollbar_example)
notebook.add(text = "Options", child = options)

frame1 = ttk.Frame(frame)
frame1.pack()

main = ttk.Frame(frame1)
main.pack(side = "left")

row1 = ttk.Frame(main)
row1.pack()


checkboxes = ttk.Labelframe(row1, text = "Checkbuttons", padding = 4)
checkboxes.pack(side = "left", fill = "y")

ttk.Checkbutton(checkboxes, text = "Checked", variable = checked, width = 15).pack(anchor = "w", padx = 4, pady = (8, 4))
ttk.Checkbutton(checkboxes, text = "Unhecked", variable = unchecked, width = 15).pack(anchor = "w", padx = 4, pady = 4)
ttk.Checkbutton(checkboxes, text = "Disabled", variable = disabled, state = "disabled", width = 15).pack(anchor = "w", padx = 4, pady = 4)


buttons = ttk.Labelframe(row1, text = "Buttons", padding = 4)
buttons.pack(side = "left", padx = (16, 0))

ttk.Button(buttons, text = "Button", width = 27).pack(anchor = "w", padx = 8, pady = 4)
ttk.Button(buttons, text = "Accent Button", width = 27, style = "Accent.TButton").pack(anchor = "w", padx = 8, pady = 4)
ttk.Button(buttons, text = "Toolbutton", width = 27, style = "Toolbutton").pack(anchor = "w", padx = 8, pady = 4)


row2 = ttk.Frame(main)
row2.pack(pady = (16, 0))


radiobuttons = ttk.Labelframe(row2, text = "Radiobuttons", padding = 4)
radiobuttons.pack(side = "left", fill = "y")

ttk.Radiobutton(radiobuttons, text = "Selected", width = 15, variable = radio, value = "1").pack(anchor = "w", padx = 4, pady = (8, 4))
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

ttk.Checkbutton(other, text = "Switch", style = "Switch.TCheckbutton").pack(padx = 8, pady = 6, fill = "x")
ttk.Checkbutton(other, text = "Toggle Button", style = "Toggle.TButton").pack(padx = 8, pady = 4, fill = "x")


text = tk.Text(scrollbar_example, padx = 10, pady = 10, height = 5, wrap = "word", bd = 0, highlightthickness = 0, font = ("Segoe UI", 10))
text.pack(side = "left", fill = "both", expand = True)
text.insert("1.0", '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed laoreet eu libero at imperdiet. Curabitur a pretium lorem. Pellentesque sed augue ultricies, vestibulum nunc eget, gravida mauris. Vivamus venenatis arcu non fringilla laoreet. Duis vulputate id odio sit amet sodales. In velit nunc, vulputate quis sollicitudin sit amet, fermentum eget purus. Etiam sed felis ut nisi pulvinar ultricies sed id risus. Vestibulum mauris libero, consectetur quis lobortis ut, maximus ac ante. Donec molestie sit amet lorem ut porta. In odio ante, faucibus non elit eget, vehicula scelerisque mi. Proin aliquam neque nunc, quis rutrum erat ultricies euismod. Suspendisse lectus lacus, fringilla sit amet mollis quis, maximus vitae orci. Duis sodales eros nec sagittis molestie. Donec tristique pharetra ex, nec dictum est sodales vel. Proin maximus mattis sapien, id viverra nulla auctor sed.

Donec ante nulla, dignissim id bibendum eget, rutrum nec erat. Suspendisse sodales arcu quis erat consequat tincidunt. Nunc nisl massa, maximus vehicula nulla sed, interdum molestie justo. Suspendisse convallis sem ac massa auctor pulvinar. Nulla turpis ex, tempor sit amet imperdiet eu, commodo at elit. Nullam eu auctor tortor, in vehicula velit. Aenean eu mi pharetra turpis semper pellentesque. Mauris mollis eget sapien quis rhoncus. Vivamus neque mauris, porttitor scelerisque neque eu, faucibus placerat mauris. In cursus sagittis dapibus. Praesent lacinia, arcu a suscipit laoreet, quam turpis consequat ipsum, nec aliquet ipsum orci eget lacus. Quisque justo odio, scelerisque tincidunt est ac, tempor ultricies erat.

Etiam consequat, eros nec maximus vulputate, tellus urna feugiat purus, ut scelerisque enim felis nec nulla. Morbi viverra, magna quis interdum dapibus, urna lacus sollicitudin nulla, ac mattis ante dolor eu ligula. Vivamus nec laoreet lorem, ut lacinia lorem. Donec accumsan ligula felis, et tincidunt lorem pharetra in. Sed et facilisis ipsum. Vivamus et magna elementum, hendrerit felis in, dapibus purus. Nullam eleifend mattis ex, ac sagittis enim finibus nec. Praesent ut mauris lobortis, semper urna ultrices, imperdiet ligula. Pellentesque a diam rutrum mi venenatis dapibus. Curabitur eu tempus lacus. Phasellus convallis diam at fermentum sagittis.

Aliquam erat volutpat. Maecenas eros eros, ultrices sit amet luctus vitae, lobortis id augue. Donec pulvinar ante sem, sed condimentum justo condimentum et. Pellentesque congue lectus lectus, at vehicula est feugiat vel. Proin cursus mi eget ultrices rutrum. Morbi in sodales mauris. Suspendisse convallis, lacus vitae dignissim mollis, nisi ligula egestas tellus, eu consectetur ligula lorem vitae purus. Aliquam iaculis massa vel ligula porttitor fermentum. Mauris imperdiet sed mauris vel semper. Cras eu ex justo. Mauris eu sollicitudin elit, vel maximus dolor.

Sed a ex dictum, sagittis nulla ac, varius lacus. Maecenas sed commodo nunc. Ut eu convallis neque, et fringilla tellus. Nam facilisis nisl a lacus molestie rhoncus. Vestibulum eu turpis viverra, tempus tellus quis, imperdiet lectus. Aenean posuere lacus et aliquam accumsan. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec tortor diam, volutpat id consequat sit amet, vestibulum quis tellus. Vivamus pellentesque commodo rutrum. Nulla varius semper commodo. Fusce laoreet neque vitae eros consectetur, semper pellentesque quam laoreet. Proin ultrices eget turpis sit amet faucibus. Etiam sit amet laoreet erat. Proin vitae auctor erat, non hendrerit metus.

Fusce semper vitae est et ultricies. Nunc ut luctus arcu. Donec quis sapien viverra, malesuada lorem eget, pulvinar tortor. Nam tempus, elit id gravida rhoncus, ipsum diam tincidunt risus, ac scelerisque eros urna sit amet dui. Phasellus vel accumsan diam, eu auctor ipsum. Etiam nunc justo, rhoncus eu egestas consectetur, ornare a justo. Phasellus dapibus ligula vitae mauris gravida dictum. Quisque vel sem eros. Pellentesque malesuada pharetra lectus eu convallis. Nullam ullamcorper euismod nibh, sit amet placerat diam varius sit amet. Nulla at rutrum tellus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum nec risus libero.

Sed ac pellentesque lorem. Morbi at elementum odio. Maecenas commodo pulvinar orci, sed sagittis odio ornare eget. Morbi et justo nec ipsum molestie imperdiet ullamcorper sed nibh. Praesent dignissim elementum metus eu convallis. Nam non tortor bibendum, feugiat augue interdum, faucibus mi. Nulla ipsum ex, elementum vitae odio quis, ullamcorper consectetur diam. Nam erat felis, sagittis quis feugiat nec, molestie vitae neque. Vivamus ullamcorper placerat augue sit amet euismod. In et pretium arcu, sit amet vestibulum risus. Nullam id tempus mauris, sollicitudin varius tortor. Donec ultricies, risus quis pellentesque volutpat, tellus velit tristique neque, id condimentum leo tellus eget risus. Fusce laoreet, arcu id lobortis porta, nunc orci tincidunt elit, non bibendum enim libero eu tortor. Vivamus nec ligula gravida, iaculis ante ut, varius tortor.

Sed sit amet lectus quis elit faucibus rutrum. Aenean arcu diam, laoreet et elit eget, malesuada euismod nulla. Aenean quam eros, dapibus ut suscipit a, posuere vel justo. Nunc sed metus diam. Aliquam efficitur varius pellentesque. Praesent viverra odio eu nisi tincidunt tempor. Aliquam erat volutpat. Vestibulum sapien lorem, molestie id erat eget, accumsan ultrices magna. Vivamus convallis ex augue, sit amet finibus ante cursus convallis. Duis ornare nisi in lacinia venenatis. Duis id semper mi.

In a odio gravida, mollis purus ut, dignissim nisl. Donec in tellus convallis felis sodales tincidunt non a mauris. Aliquam ac lorem nisl. Pellentesque vehicula neque quis sapien facilisis semper. Proin vel blandit velit. Integer elementum nisi lorem, quis gravida sapien placerat et. Morbi vitae diam enim. Pellentesque eget malesuada lorem. Nullam quis leo sit amet leo egestas luctus. Suspendisse ut posuere metus. Nunc interdum mattis elit vitae pellentesque. Cras placerat convallis posuere. Suspendisse elementum diam eget arcu commodo feugiat. Etiam porttitor ante sed mi vulputate, vitae sodales felis sagittis. Nam egestas augue neque, a dictum libero fringilla at. Nam auctor lorem lacus, quis sagittis risus vulputate at.

Praesent odio sapien, auctor efficitur suscipit sed, dictum et elit. Vivamus quis diam eu lectus laoreet pulvinar. Nunc malesuada posuere augue. Suspendisse potenti. Nam blandit mi eget suscipit egestas. Nulla arcu felis, faucibus vel justo ac, iaculis finibus lacus. Curabitur ut justo et arcu gravida condimentum. Nam malesuada orci turpis. Proin eu massa at dolor rhoncus vehicula. In quis lorem orci. Mauris laoreet diam varius est porttitor, sit amet facilisis purus rhoncus. Pellentesque rhoncus egestas lorem, nec mattis sem faucibus vel. Nam vitae dolor tincidunt, congue nibh ac, iaculis lorem. Vivamus quam mauris, molestie nec dui sit amet, egestas ultrices leo. Quisque congue justo id nulla semper pretium. Sed molestie eget ex sed malesuada.''')
text.configure(state = "disabled")

scrollbar = ttk.Scrollbar(scrollbar_example, orient = "vertical", command = text.yview)
scrollbar.pack(side = "left", fill = "y", pady = 8)

text.configure(yscrollcommand = scrollbar.set)

def show_native_menu():
    if native_menu_bool.get(): window.configure(menu = menu)
    else: window.configure(menu = "")

def show_custom_menu():
    if custom_menu_bool.get(): 
        menu_bar.pack(side = "top", fill = "x")
        title.forget()
        
        if sv_ttk.get_theme() == "dark": window.configure(bg = "#1f1f1f")
        else: window.configure(bg = "#ffffff")
    else: 
        menu_bar.forget()
        title.pack(padx = 16, pady = (8, 0), side = "top", anchor = "w")

        if sv_ttk.get_theme() == "dark": window.configure(bg = "#1c1c1c")
        else: window.configure(bg = "#fafafa")

def toggle_theme(): sv_ttk.toggle_theme(); show_custom_menu()

ttk.Label(options, text = "Options", font = ("Segoe UI Semibold", 18)).pack(anchor = "w", pady = (0, 18))

ttk.Checkbutton(options, text = "Dark Mode", command = toggle_theme, style = "Switch.TCheckbutton").pack(anchor = "w")
ttk.Checkbutton(options, text = "Show native menu", variable = native_menu_bool, command = show_native_menu).pack(anchor = "w", pady = (10, 0))
ttk.Checkbutton(options, text = "Show custom menu", variable = custom_menu_bool, command = show_custom_menu).pack(anchor = "w", pady = (10, 0))
ttk.Button(options, text = "Open Toplevel", command = tk.Toplevel).pack(anchor = "w", pady = (10, 0))
ttk.Button(options, text = "Show message box", command = lambda: msg.showinfo("Test message box", "This is a test message box.")).pack(anchor = "w", pady = (10, 0))
ttk.Button(options, text = "Show file dialog", command = lambda: fd.askdirectory()).pack(anchor = "w", pady = (10, 0))
ttk.Button(options, text = "Send <<ThemeChanged>> event", command = lambda: window.event_generate("<<ThemeChanged>>")).pack(anchor = "w", pady = (10, 0))

window.update()

geometry = window.geometry().split("+")[0].split("x")
window.minsize(width = geometry[0], height = geometry[1])

frame1.forget()
frame1.place(relx = .5, rely = .5, anchor = "center")

window.mainloop()