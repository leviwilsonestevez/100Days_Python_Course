from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward() -> None:
    tim.forward(10)


def move_backwards() -> None:
    tim.backward(10)


def turn_left() -> None:
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def turn_right() -> None:
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def clear() -> None:
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")
screen.exitonclick()
