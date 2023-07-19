# start a turtle document:
import turtle as t
from turtle import Screen


def draw_dashed_line(elements: int, length: float) -> None:
    dash_line = t.Turtle()
    for i in range(elements):
        dash_line.forward(length)
        dash_line.penup()
        dash_line.forward(length)
        dash_line.pendown()


draw_dashed_line(elements=15, length=10.00)
scene = Screen()
scene.exitonclick()
