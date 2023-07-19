from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_right() -> None:
    tim.right(90)


def move_left() -> None:
    tim.left(90)


def move_forward() -> None:
    tim.speed(1)
    tim.forward(10)


screen.listen()
screen.onkey(move_right, "d")
screen.onkey(move_left, "a")
while not screen.onkey(move_forward, "f"):
    move_forward()
screen.exitonclick()
