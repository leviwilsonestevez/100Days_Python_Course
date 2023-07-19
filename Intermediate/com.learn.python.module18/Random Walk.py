import random
from turtle import Screen, Turtle
from random import choices

colors_to_draw = ["red", "green", "blue", "orange", "purple", "pink", "yellow"]

directions = [0, 90, 180, 270]
pens_sizes = [5, 10, 15]
scene = Screen()
scene.colormode(255)

tim = Turtle()


def random_color() -> tuple:
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


for i in range(200):
    tim.forward(30)
    tim.color(random_color())
    tim.setheading(random.choice(seq=directions))
    tim.pensize(random.choice(pens_sizes))


scene.exitonclick()
