from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.font import Font

# Funkcja do otwierania pliku
def open_file():
    filepath = askopenfilename(defaultextension=".wws", filetypes=[("WWS Files", "*.wws"), ("KLP Files", "*.klp"), ("All Files", "*.*")])
    if not filepath:
        return
    text.delete(1.0, END)
    with open(filepath, "r") as file:
        text.insert(INSERT, file.read())

# Funkcja do zapisywania pliku
def save_file():
    filepath = asksaveasfilename(defaultextension=".wws", filetypes=[("WWS Files", "*.wws"), ("KLP Files", "*.klp"), ("All Files", "*.*")])
    if not filepath:
        return
    with open(filepath, "w") as file:
        file.write(text.get(1.0, END))

# Funkcja do zmiany czcionki
def change_font():
    global current_font
    font_name = font_var.get()
    font_size = size_var.get()
    current_font = Font(family=font_name, size=font_size)
    text.config(font=current_font)

# Utworzenie okna głównego aplikacji
root = Tk()
root.title("Text Editor")

# Utworzenie menu
menu_bar = Menu(root)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)
font_menu = Menu(menu_bar, tearoff=0)
font_var = StringVar(value="Helvetica")
font_menu.add_radiobutton(label="Helvetica", variable=font_var, command=change_font)
font_menu.add_radiobutton(label="Times New Roman", variable=font_var, command=change_font)
font_menu.add_radiobutton(label="Courier New", variable=font_var, command=change_font)
menu_bar.add_cascade(label="Font", menu=font_menu)
size_menu = Menu(font_menu, tearoff=0)
size_var = IntVar(value=12)
size_menu.add_radiobutton(label="12", variable=size_var, command=change_font)
size_menu.add_radiobutton(label="14", variable=size_var, command=change_font)
size_menu.add_radiobutton(label="16", variable=size_var, command=change_font)
menu_bar.add_cascade(label="Size", menu=size_menu)
root.config(menu=menu_bar)

# Utworzenie pola tekstowego
text = Text(root, font=("Helvetica", 12))
text.pack(expand=YES, fill=BOTH)

# Uruchomienie pętli głównej aplikacji
root.mainloop()
