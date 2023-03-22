import tkinter as tk

class Paint:
    def __init__(self, master):
        self.master = master
        master.title("Paint")
        self.color = "black"
        self.brush_size = 10

        self.canvas = tk.Canvas(master, width=500, height=500, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<Button-3>", self.erase)

        color_label = tk.Label(master, text="Choose color:")
        color_label.pack(side=tk.LEFT, padx=10)

        self.color_menu = tk.OptionMenu(master, tk.StringVar(), "black", "red", "blue", "green", "yellow")
        self.color_menu.config(width=8)
        self.color_menu.pack(side=tk.LEFT)

        size_label = tk.Label(master, text="Brush size:")
        size_label.pack(side=tk.LEFT, padx=10)

        self.size_slider = tk.Scale(master, from_=1, to=50, orient=tk.HORIZONTAL)
        self.size_slider.set(self.brush_size)
        self.size_slider.pack(side=tk.LEFT)

        clear_button = tk.Button(master, text="Clear canvas", command=self.clear)
        clear_button.pack(side=tk.RIGHT, padx=10)

    def draw(self, event):
        x, y = event.x, event.y
        r = self.brush_size
        self.canvas.create_oval(x-r, y-r, x+r, y+r, fill=self.color, outline="")

    def erase(self, event):
        x, y = event.x, event.y
        r = self.brush_size
        self.canvas.create_oval(x-r, y-r, x+r, y+r, fill="white", outline="white")

    def clear(self):
        self.canvas.delete("all")

root = tk.Tk()
paint = Paint(root)
root.mainloop()

