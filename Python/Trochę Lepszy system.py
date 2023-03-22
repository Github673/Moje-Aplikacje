import tkinter as tk
import os

class Window:
    def __init__(self, master):
        self.master = master
        master.title("AuroraOS")

        # Dodanie górnego paska z menu aplikacji
        self.menu_bar = tk.Menu(master)
        self.master.config(menu=self.menu_bar)
        self.app_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.app_menu.add_command(label="Paint", command=self.open_paint)
        self.app_menu.add_command(label="Eksplorator plików", command=self.open_explorer)
        self.menu_bar.add_cascade(label="Aplikacje", menu=self.app_menu)

        # Dodanie obsługi myszy
        master.bind("<Button-1>", self.mouse_click)

    def mouse_click(self, event):
        print(f"Kliknięto w punkt ({event.x}, {event.y})")

    def open_paint(self):
        PaintWindow(self.master)

    def open_explorer(self):
        ExplorerWindow(self.master)

class PaintWindow:
    def __init__(self, master):
        self.master = master
        master.title("Paint")

        # Dodanie obsługi myszy
        master.bind("<Button-1>", self.mouse_click)

    def mouse_click(self, event):
        print(f"Kliknięto w punkt ({event.x}, {event.y}) w Paint")

class ExplorerWindow:
    def __init__(self, master):
        self.master = master
        master.title("Eksplorator plików")

        # Dodanie obsługi myszy
        master.bind("<Button-1>", self.mouse_click)

        # Dodanie przycisku wyświetlającego zawartość bieżącego katalogu
        self.current_dir_button = tk.Button(master, text="Pokaż zawartość bieżącego katalogu", command=self.show_current_dir)
        self.current_dir_button.pack()

    def mouse_click(self, event):
        print(f"Kliknięto w punkt ({event.x}, {event.y}) w Eksploratorze plików")

    def show_current_dir(self):
        current_dir = os.getcwd()
        print(f"Zawartość katalogu {current_dir}:")
        for item in os.listdir(current_dir):
            print(item)

root = tk.Tk()
window = Window(root)
root.mainloop()
