import tkinter as tk
from tkinter import scrolledtext

# funkcja, która zapisuje zawartość pola tekstowego do pliku
def save_file():
    file_name = file_name_entry.get()
    text = text_area.get("1.0", "end")
    with open(file_name, "w") as file:
        file.write(text)

# utworzenie okna
window = tk.Tk()
window.title("Program do pisania")

# utworzenie etykiety "Nazwa pliku:"
file_name_label = tk.Label(window, text="Nazwa pliku:")
file_name_label.grid(row=0, column=0, padx=5, pady=5)

# utworzenie pola wprowadzania nazwy pliku
file_name_entry = tk.Entry(window, width=30)
file_name_entry.grid(row=0, column=1, padx=5, pady=5)

# utworzenie przycisku "Zapisz"
save_button = tk.Button(window, text="Zapisz", command=save_file)
save_button.grid(row=0, column=2, padx=5, pady=5)

# utworzenie pola tekstowego
text_area = scrolledtext.ScrolledText(window, width=80, height=20)
text_area.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

# uruchomienie pętli głównej
window.mainloop()
