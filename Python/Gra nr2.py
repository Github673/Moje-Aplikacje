import tkinter as tk
import random

class Game:
    def __init__(self, master):
        self.master = master
        self.points = 0
        self.time_left = 60
        
        self.points_label = tk.Label(self.master, text=f"Punkty: {self.points}")
        self.points_label.pack()
        
        self.time_label = tk.Label(self.master, text=f"Czas: {self.time_left}")
        self.time_label.pack()
        
        self.button = tk.Button(self.master, text="Kliknij mnie!", command=self.add_point)
        self.button.pack()
        
        self.timer()
    
    def add_point(self):
        self.points += 1
        self.points_label.config(text=f"Punkty: {self.points}")
        
    def timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.time_label.config(text=f"Czas: {self.time_left}")
            self.master.after(1000, self.timer)
        else:
            self.button.config(state=tk.DISABLED)
            self.points_label.config(text=f"Koniec gry! Zdobyłeś {self.points} punktów.")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Gra punktowa")
    game = Game(root)
    root.mainloop()
