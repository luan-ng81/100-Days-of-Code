#Use import * only if import 1 module in a script
from tkinter import *

def calculate():
    miles = entry.get()
    km = float(miles) * 1.609
    result.config(text=f"{km}")

PADY = 0

window = Tk()
window.title("Mile to Km Converter")
# window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

entry = Entry(width=7)
entry.grid(row=0, column=1, padx=PADY, pady=PADY)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2, padx=PADY, pady=PADY)

is_equal_to = Label(text="is equal to")
is_equal_to.grid(row=1, column=0, padx=PADY, pady=PADY)

result = Label(text="0")
result.grid(row=1, column=1, padx=PADY, pady=PADY)

km_label = Label(text="Km")
km_label.grid(row=1, column=2, padx=PADY, pady=PADY)

button = Button(text="Calculate", command=calculate)
button.grid(row=2, column=1, padx=PADY, pady=PADY)



window.mainloop()