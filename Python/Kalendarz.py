from tkinter import *
import calendar

class CalendarGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Kalendarz")
        self.year = StringVar()
        self.month = StringVar()
        self.year.set("2023")
        self.month.set("1")

        self.year_label = Label(self.master, text="Rok:")
        self.year_label.grid(row=0, column=0, padx=10, pady=10)
        self.year_entry = Entry(self.master, textvariable=self.year)
        self.year_entry.grid(row=0, column=1)

        self.month_label = Label(self.master, text="Miesiąc:")
        self.month_label.grid(row=1, column=0, padx=10, pady=10)
        self.month_entry = Entry(self.master, textvariable=self.month)
        self.month_entry.grid(row=1, column=1)

        self.show_button = Button(self.master, text="Pokaż Kalendarz", command=self.show_calendar)
        self.show_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def show_calendar(self):
        year = int(self.year.get())
        month = int(self.month.get())
        cal = calendar.monthcalendar(year, month)

        top = Toplevel(self.master)
        top.title(calendar.month_name[month] + " " + str(year))

        for week in cal:
            for i, day in enumerate(week):
                if day == 0:
                    day = ""
                day_label = Label(top, text=str(day))
                day_label.grid(row=cal.index(week), column=i)

root = Tk()
app = CalendarGUI(root)
root.mainloop()
