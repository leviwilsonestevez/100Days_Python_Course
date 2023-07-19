from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position: tuple) -> None:
        super().__init__("square")
        self.color("white")
        self.shapesize(5, 1)
        self.penup()
        self.goto(position)

    def go_up(self) -> None:
        new_y = self.ycor() + 20
        same_x = self.xcor()
        self.goto((same_x, new_y))

    def go_down(self) -> None:
        new_y = self.ycor() - 20
        same_x = self.xcor()
        self.goto((same_x, new_y))
