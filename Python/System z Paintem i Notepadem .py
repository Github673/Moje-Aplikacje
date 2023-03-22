import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import os

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Tworzenie menu
        menubar = tk.Menu(self.master)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open Notepad", command=self.open_notepad)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.master.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        self.master.config(menu=menubar)

        # Tworzenie ramki z obrazem
        self.image_frame = tk.Frame(self.master, height=300, width=300)
        self.image_frame.pack(side="left")

        # Wczytywanie obrazka
        img = Image.new("RGB", (300, 300), "white")
        photo = ImageTk.PhotoImage(img)
        self.image_label = tk.Label(self.image_frame, image=photo)
        self.image_label.image = photo
        self.image_label.pack()

        # Tworzenie przycisku do otwierania Painta
        self.paint_button = tk.Button(self.master, text="Open Paint", command=self.open_paint)
        self.paint_button.pack(side="left")

    def open_paint(self):
        os.system("mspaint.exe")

    def open_notepad(self):
        # Otwieranie pliku tekstowego
        filename = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if filename:
            # Otwieranie pliku w notatniku
            os.system("notepad.exe " + filename)


root = tk.Tk()
app = Application(master=root)
app.mainloop()
