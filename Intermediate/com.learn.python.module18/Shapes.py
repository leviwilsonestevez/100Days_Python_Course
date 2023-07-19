from turtle import Screen, Turtle
from random import choices


def draw_shapes(shapes: list, colors: list, length: float) -> None:
    line = Turtle()
    for shape in shapes:
        line.color(choices(colors))
        sides = shape["sides"]
        angle = shape["angle"]
        for i in range(sides):
            line.forward(length)
            line.right(angle)


# Draw polygons : number_of_sides - angle : 360 grades / number_of_sides
drawn_shapes = [{"sides": 3, "angle": 120}, {"sides": 5, "angle": 72}, {"sides": 6, "angle": 60},
                {"sides": 7, "angle": 51.42}, {"sides": 8, "angle": 45}, {"sides": 9, "angle": 40},
                {"sides": 10, "angle": 36}]
# Make a list of colors
colors_to_draw = ["red", "green", "blue", "orange", "purple", "pink", "yellow"]

draw_shapes(shapes=drawn_shapes, colors=colors_to_draw, length=100)

screen = Screen()
screen.exitonclick()
