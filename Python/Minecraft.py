from tkinter import *
from tkinter.ttk import *

# Funkcja do poruszania postacią w górę
def move_up(event=None):
    canvas.move(player, 0, -10)

# Funkcja do poruszania postacią w dół
def move_down(event=None):
    canvas.move(player, 0, 10)

# Funkcja do poruszania postacią w lewo
def move_left(event=None):
    canvas.move(player, -10, 0)

# Funkcja do poruszania postacią w prawo
def move_right(event=None):
    canvas.move(player, 10, 0)

# Utworzenie okna aplikacji
root = Tk()
root.title("Minecraft")

# Ustawienia okna aplikacji
app_width = 600
app_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = int((screen_width/2) - (app_width/2))
y = int((screen_height/2) - (app_height/2))
root.geometry(f'{app_width}x{app_height}+{x}+{y}')
root.resizable(False, False)

# Utworzenie canvasu
canvas = Canvas(root, width=600, height=400, bg="#c6e2ff")
canvas.pack(fill=BOTH, expand=True)

# Dodanie tła
canvas.create_rectangle(0, 0, 600, 400, fill="#55aa55")

# Dodanie postaci
player = canvas.create_oval(285, 185, 315, 215, fill="#ffaa00")

# Utworzenie przycisków
up_button = Button(root, text="Up", command=move_up)
up_button.pack(side=LEFT, padx=10, pady=10)
down_button = Button(root, text="Down", command=move_down)
down_button.pack(side=LEFT, padx=10, pady=10)
left_button = Button(root, text="Left", command=move_left)
left_button.pack(side=LEFT, padx=10, pady=10)
right_button = Button(root, text="Right", command=move_right)
right_button.pack(side=LEFT, padx=10, pady=10)

# Utworzenie bindów klawiszy
root.bind("<Up>", move_up)
root.bind("<Down>", move_down)
root.bind("<Left>", move_left)
root.bind("<Right>", move_right)

# Rozpoczęcie głównej pętli programu
root.mainloop()
