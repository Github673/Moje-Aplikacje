import tkinter as tk

# funkcja, która wykonuje działanie kalkulatora
def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operator = operator_var.get()
        
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            result = num1 / num2
            
        result_label.config(text="Wynik: " + str(result))
    except ValueError:
        result_label.config(text="Wprowadź poprawne wartości!")
    except ZeroDivisionError:
        result_label.config(text="Nie można dzielić przez zero!")

# utworzenie okna
window = tk.Tk()
window.title("Kalkulator")

# utworzenie pól wprowadzania liczb
entry1 = tk.Entry(window, width=10)
entry1.grid(row=0, column=0, padx=5, pady=5)

entry2 = tk.Entry(window, width=10)
entry2.grid(row=0, column=1, padx=5, pady=5)

# utworzenie pola wyboru operatora
operator_var = tk.StringVar(value="+")
operator_choices = ["+", "-", "*", "/"]
operator_dropdown = tk.OptionMenu(window, operator_var, *operator_choices)
operator_dropdown.grid(row=0, column=2, padx=5, pady=5)

# utworzenie przycisku "Oblicz"
calculate_button = tk.Button(window, text="Oblicz", command=calculate)
calculate_button.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

# utworzenie etykiety z wynikiem
result_label = tk.Label(window, text="Wynik:")
result_label.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

# uruchomienie pętli głównej
window.mainloop()
