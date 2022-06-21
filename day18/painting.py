import random
from turtle import Turtle, Screen

import colorgram


def rip_colors(source):
    colors = colorgram.extract(source, 10)
    color_formed = []
    for color in colors:
        color_formed.append((color.rgb.r, color.rgb.g, color.rgb.b))
    return color_formed


def place_dot(tut, colors):
    tut.pensize(20)
    tut.dot(20, random.choice(colors))


def next_step(tut, step_size):
    tut.forward(50)


def next_row(tut, step_size):
    tut.setpos(10, tut.ycor() + step_size)


def main():
    tut = Turtle()
    tut.shape("turtle")
    tut.color("AliceBlue")
    tut.penup()
    tut_screen = Screen()
    tut_screen.bgcolor("white")
    tut_screen.colormode(255)
    step_size = 50
    palette = rip_colors("source.jpg")
    tut.setpos(-(tut_screen.canvwidth / 2), -(tut_screen.canvheight / 2))
    steps = int(round(tut_screen.canvwidth / step_size))
    rows = int(round(tut_screen.canvheight / step_size))
    for row in range(0, rows):
        for step in range(0, steps):
            place_dot(tut, palette)
            next_step(tut, step_size)
        next_row(tut, step_size)


if __name__ == "__main__":
    main()


