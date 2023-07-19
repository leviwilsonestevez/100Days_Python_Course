from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self) -> None:
        x_food = random.randint(-260, 260)
        y_food = random.randint(-260, 270)
        self.goto(x_food, y_food)
