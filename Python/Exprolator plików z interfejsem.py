import os
import tkinter as tk
from tkinter import filedialog, messagebox

root = tk.Tk()
root.title("Eksplorator plików")

# funkcja wywoływana po kliknięciu przycisku "Przeglądaj"
def browse_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        listbox.delete(0, tk.END)
        for item in os.listdir(folder_path):
            listbox.insert(tk.END, item)

# funkcja wywoływana po kliknięciu przycisku "Otwórz"
def open_file():
    selected = listbox.curselection()
    if selected:
        file_path = os.path.join(folder_path, listbox.get(selected))
        if os.path.isfile(file_path):
            os.startfile(file_path)
        else:
            messagebox.showerror("Błąd", "To nie jest plik")
    else:
        messagebox.showwarning("Ostrzeżenie", "Nie wybrano żadnego pliku")

# funkcja wywoływana po kliknięciu przycisku "Uruchom"
def run_program():
    selected = listbox.curselection()
    if selected:
        file_path = os.path.join(folder_path, listbox.get(selected))
        if os.path.isfile(file_path) and file_path.endswith(".exe"):
            os.startfile(file_path)
        else:
            messagebox.showerror("Błąd", "To nie jest program lub nie ma rozszerzenia .exe")
    else:
        messagebox.showwarning("Ostrzeżenie", "Nie wybrano żadnego pliku")

# przyciski
button_frame = tk.Frame(root)
button_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

browse_button = tk.Button(button_frame, text="Przeglądaj", command=browse_folder)
browse_button.pack(side=tk.LEFT, padx=5)

open_button = tk.Button(button_frame, text="Otwórz", command=open_file)
open_button.pack(side=tk.LEFT, padx=5)

run_button = tk.Button(button_frame, text="Uruchom", command=run_program)
run_button.pack(side=tk.LEFT, padx=5)

# lista plików
listbox_frame = tk.Frame(root)
listbox_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)

scrollbar = tk.Scrollbar(listbox_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(listbox_frame, yscrollcommand=scrollbar.set)
listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar.config(command=listbox.yview)

# wywołanie pętli zdarzeń
folder_path = ""
root.mainloop()
