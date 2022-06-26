from tkinter import Button, Tk, Label, Entry, IntVar, Radiobutton

windows = Tk()
windows.title("Distance Converter")
windows.minsize(width=200, height=100)


def convert(val, **kwargs):
    unit = kwargs.get("unit")
    if unit == "mile":
        return round((val * 1.609344), 4)
    if unit == "kilometer":
        return round((val / 1.609344), 4)

def button_clicked():
    miles_word = "mile"
    km_word = "kilometer"
    if radio_varint.get() == 0:
        send = miles_word
        source = km_word
    if radio_varint.get() == 1:
        send = km_word
        source = miles_word

    val = float(box_input.get())
    converted = convert(val, unit=send)
    message = f"{val} {send}s is {converted} {source}s"
    if val == 1:
        message = f"{val} {send} is {converted} {source}s"
    if converted == 1:
        message = f"{val} {send}s is {converted} {source}"
    result_label.config(text=message)

def radio_selected():
    pass

place_holder = Label()
place_holder.grid(column=0, row=0)

my_label = Label(text="Select units to convert from", font=("Arial", 20))
my_label.grid(column=1, row=0)

button = Button(text="Convert!", command=button_clicked)
button.grid(column=1, row=2)

radio_varint = IntVar()
radio_input_miles = Radiobutton(text="Miles", command=radio_selected, variable=radio_varint, value=0)
radio_input_kilometers = Radiobutton(text="Kilometers", command=radio_selected, variable=radio_varint, value=1)
radio_input_miles.grid(column=2, row=3)
radio_input_kilometers.grid(column=2, row=4)

box_input = Entry(width=10)
box_input.grid(column=1, row=5)

result_label = Label(font=("Arial", 20, "bold"))
result_label.grid(column=1, row=6)







windows.mainloop()
