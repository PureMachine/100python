from tkinter import Button, Tk, Label, Entry

windows = Tk()
windows.title("My Game")
windows.minsize(width=500, height=300)


def button_clicked():
    my_label.config(text=box_input.get())

my_label = Label(text="I am a label", font=("Arial", 20))
my_label.grid(column=0, row=0)

button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="Click me", command=button_clicked)
new_button.grid(column=2, row=0)

box_input = Entry(width=10)
box_input.grid(column=3, row=3)main.py









windows.mainloop()
