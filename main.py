from tkinter import *

my_window = Tk()
my_window.title("Mile to Km Converter")
my_window.minsize(width=500, height=300)
my_window.config(padx=100, pady=100)

user_input = Entry()
user_input.grid(row=0, column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

equal_label = Label(text="is Equal to: ")
equal_label.grid(row=1, column=0)

make_calculate_label = Label(text="0")
make_calculate_label.grid(row=1, column=1)

km_label = Label(text="Km")
km_label.grid(row=1, column=2)


def calculate_km():
    actual_mile = int(user_input.get())
    total_km = actual_mile * 1.609344
    total_km = round(total_km, 3)
    make_calculate_label.config(text=str(total_km))
    pass


calculate_button = Button(text="Calculate", command=calculate_km)
calculate_button.grid(row=2, column=1)

my_window.mainloop()
