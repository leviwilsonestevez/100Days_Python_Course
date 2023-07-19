from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280



class Player(Turtle):
    def __init__(self) -> None:
        super().__init__("turtle")
        self.color("black")
        self.setheading(90)
        self.penup()
        self.go_to_start()

    def go_up(self) -> None:
        self.forward(MOVE_DISTANCE)

    def go_to_start(self) -> None:
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self) -> bool:
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False


