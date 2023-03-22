import os
from tkinter import *

class AuroraOS:

    def __init__(self, master):
        self.master = master
        master.title("AuroraOS")

        # GUI elementy
        self.label = Label(master, text="Witaj w AuroraOS!")
        self.label.pack()

        self.dir_button = Button(master, text="DIR", command=self.show_dir)
        self.dir_button.pack()

        self.cd_button = Button(master, text="CD", command=self.change_dir)
        self.cd_button.pack()

        self.type_button = Button(master, text="TYPE", command=self.show_file)
        self.type_button.pack()

        self.copy_button = Button(master, text="COPY", command=self.copy_file)
        self.copy_button.pack()

        self.del_button = Button(master, text="DEL", command=self.delete_file)
        self.del_button.pack()

        # konsola
        self.console_label = Label(master, text="Konsola:")
        self.console_label.pack()

        self.console = Text(master, height=10)
        self.console.pack()

        # pole tekstowe do wpisywania poleceń
        self.command_label = Label(master, text="Wpisz polecenie:")
        self.command_label.pack()

        self.command_entry = Entry(master)
        self.command_entry.pack()

        self.command_button = Button(master, text="Wykonaj", command=self.execute_command)
        self.command_button.pack()

    def show_dir(self):
        files = os.listdir(os.getcwd())
        self.console.insert(END, "\n".join(files) + "\n")

    def change_dir(self):
        path = self.command_entry.get()
        try:
            os.chdir(path)
            self.console.insert(END, f"Zmieniono bieżący katalog na {path}\n")
        except FileNotFoundError:
            self.console.insert(END, f"Nie znaleziono katalogu {path}\n")
        except NotADirectoryError:
            self.console.insert(END, f"{path} nie jest katalogiem\n")

    def show_file(self):
        path = self.command_entry.get()
        try:
            with open(path, "r") as file:
                content = file.read()
                self.console.insert(END, f"\n{content}\n")
        except FileNotFoundError:
            self.console.insert(END, f"Nie znaleziono pliku {path}\n")

    def copy_file(self):
        paths = self.command_entry.get().split()
        try:
            with open(paths[0], "rb") as source:
                with open(paths[1], "wb") as destination:
                    destination.write(source.read())
            self.console.insert(END, f"Skopiowano {paths[0]} do {paths[1]}\n")
        except FileNotFoundError:
            self.console.insert(END, f"Nie znaleziono pliku {paths[0]}\n")

    def delete_file(self):
        path = self.command_entry.get()
        try:
            os.remove(path)
            self.console.insert(END, f"Usunięto plik {path}\n")
        except FileNotFoundError:
            self.console.insert(END, f"Nie znaleziono pliku {path}\n")

    def execute_command(self):
        command = self.command_entry.get()
        if command == "EXIT":
            self.master.quit()
        else:
            self.console.insert(END, f"{command}\n")
            self.command_entry.delete(0, END)

root = Tk()
my_gui = AuroraOS(root)
root.mainloop()

