import sys
import turtle

import pandas
from turtle import Screen, Turtle

state_data = pandas.read_csv("50_states.csv")


screen = Screen()
screen.title("U.S. States Game")
map = "blank_states_img.gif"
screen.addshape("blank_states_img.gif")

tut = Turtle()
tut.shape(map)
guessed = []


def cleanup():
    all_states = state_data.state.to_list()
    for state in all_states:
        if state in guessed:
            all_states.remove(state)
    data = {"state": all_states}
    pandas.DataFrame(data=data).to_csv("learning.csv")


def start():
    tutor = Turtle(visible=False)
    tutor.penup()
    answer_state = screen.textinput(title="Guess the state", prompt="Name a state")
    transformed = answer_state[0].upper() + answer_state[1:]
    print(answer_state.title())
    if len(guessed) == len(state_data.state.index) or answer_state.title() == "Exit":
        cleanup()
        sys.exit(0)
    if " " in transformed:
        working = transformed.split(" ")
        letter = transformed.split(" ")[1][0].upper()
        transformed = f"{working[0]} {letter}{working[1][1:]}"
    if transformed in state_data.state.to_list() and transformed not in guessed:
        row = state_data[state_data.state == transformed]
        tutor.goto(row.x.item(), row.y.item())
        tutor.write(transformed, font=('Arial', 12, 'bold'))
        guessed.append(transformed)
    start()


start()


turtle.mainloop()

