from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")


def create_turtle(start):
    new = Turtle(shape="square")
    new.color("white")
    new.setx(start)
    new.shapesize(stretch_wid=1, stretch_len=1)


current_length = 3
offset = 0
for segment in range(0, current_length):
    create_turtle(offset)
    offset -= 20















screen.exitonclick()
