import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk

# Tworzenie głównego okna aplikacji
root = tk.Tk()
root.title("Paint App")

# Tworzenie obszaru rysowania
canvas_width = 600
canvas_height = 400
canvas_color = 'white'
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg=canvas_color)
canvas.pack(side=tk.LEFT, padx=10, pady=10)

# Tworzenie paletki kolorów
color_palette = ['#000000', '#808080', '#FFFFFF', '#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#00FFFF', '#FF00FF']
color_frame = ttk.Frame(root)
color_frame.pack(side=tk.LEFT, padx=10, pady=10)
for color in color_palette:
    ttk.Button(color_frame, width=3, background=color, command=lambda c=color: canvas.config(
        {'bg': c})).pack(side=tk.TOP, padx=2, pady=2)

# Tworzenie przycisków
button_frame = ttk.Frame(root)
button_frame.pack(side=tk.TOP, padx=10, pady=10)
ttk.Button(button_frame, text='Clear', command=lambda: canvas.delete('all')).pack(side=tk.LEFT, padx=5, pady=5)
ttk.Button(button_frame, text='Save', command=lambda: save_image()).pack(side=tk.LEFT, padx=5, pady=5)
ttk.Button(button_frame, text='Load', command=lambda: load_image()).pack(side=tk.LEFT, padx=5, pady=5)

# Funkcje dla przycisków Save i Load
def save_image():
    filename = filedialog.asksaveasfilename(defaultextension='.png')
    if filename:
        canvas.postscript(file=filename + '.eps')
        img = Image.open(filename + '.eps')
        img.save(filename)

def load_image():
    filename = filedialog.askopenfilename()
    if filename:
        img = Image.open(filename)
        img_tk = ImageTk.PhotoImage(img)
        canvas.create_image(canvas_width / 2, canvas_height / 2, image=img_tk)
        canvas.image = img_tk

# Uruchamianie aplikacji
root.mainloop()
