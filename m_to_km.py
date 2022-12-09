from tkinter import *


def converter():
    miles = float(miles_input.get())
    km = round(miles * 1.60934, 2)
    km_ans.config(text=f"{km}")


# window:
window = Tk()
window.title("Miles to Kilometers")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

miles_input = Entry(width=7)
miles_input.insert(END, "0")
miles_input.grid(column=1, row=0)

# labels:
label = Label(text="miles")
label.grid(column=2, row=0)

is_equal = Label(text="is equal to")
is_equal.grid(column=0, row=1)

km_ans = Label(text="0")
km_ans.grid(column=1, row=1)

km = Label(text="km")
km.grid(column=2, row=1)

button = Button(text="calculate", command=converter)
button.grid(column=1, row=2)

window.mainloop()
