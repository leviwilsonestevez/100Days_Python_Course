import turtle as t
import random

# Set the background color as black,
# pensize as 2 and speed of drawing
# curve as 10(relative)
t.pensize(2)
t.speed("fastest")
scene = t.Screen()
scene.colormode(255)


def random_color() -> tuple:
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def draw_spirograph(size_of_gap) -> None:
    for i in range(int(360 / size_of_gap)):
        t.color(random_color())
        t.circle(100)
        t.left(size_of_gap)
        t.hideturtle()


draw_spirograph(size_of_gap=10)
scene.exitonclick()
