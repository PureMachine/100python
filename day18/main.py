from turtle import Turtle, Screen
import random


def random_color():
    return random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)


def get_angle(sides):
    return 360 / sides


def random_turn(angles):
    return random.choice(angles)


def draw_shape(tut, sides):
    distance = 100
    tut.pencolor(random_color())
    for _i in range(sides):
        tut.forward(distance)
        tut.right(get_angle(sides))


def draw_random(tut):
    distance = 50
    angles = range(90, 360, 90)
    tut.pensize(15)
    while True:
        tut.pencolor(random_color())
        tut.forward(distance)
        tut.right(random_turn(angles))


def draw_spirograph(tut):
    radius = 150
    tut.speed(10)
    tut.pensize(10)
    for _ in range(0, 100):
        tut.pencolor(random_color())
        tut.circle(radius)
        tut.setheading(tut.heading() + 5)


def main():
    tut = Turtle()
    tut.shape("turtle")
    tut.color("AliceBlue")
    tut_screen = Screen()
    tut_screen.bgcolor("white")
    tut_screen.colormode(255)
    shapes = [3, 4, 5, 6, 7, 8, 9, 10]
    # for shape in shapes:
    #     draw_shape(tut, shape)
    # draw_random(tut)
    draw_spirograph(tut)
    tut_screen.exitonclick()


if __name__ == "__main__":
    main()


