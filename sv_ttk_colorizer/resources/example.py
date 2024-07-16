import tkinter as tk
from tkinter import ttk, messagebox as msg, filedialog as fd

try: import __init__ as sv_ttk
except: import sv_ttk

window = tk.Tk()
window.title("Sun Valley Demo")
window.configure(padx = 16, pady = 4)
window.minsize(width = 799, height = 456)
sv_ttk.set_theme("light")

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

def show_menu():
    if menu_bool.get(): window.configure(menu = menu)
    else: window.configure(menu = "")

ttk.Label(options, text = "Options", font = ("Segoe UI Semibold", 18)).pack(anchor = "w", pady = (0, 18))

ttk.Checkbutton(options, text = "Dark Mode", command = sv_ttk.toggle_theme, style = "Switch.TCheckbutton").pack(anchor = "w")
ttk.Checkbutton(options, text = "Show menu", variable = menu_bool, command = show_menu).pack(anchor = "w", pady = (10, 0))
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