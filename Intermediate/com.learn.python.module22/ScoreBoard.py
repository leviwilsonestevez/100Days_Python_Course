from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.update_scoreboard()

    def update_scoreboard(self) -> None:
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 60, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 60, "normal"))

    def l_point(self) -> None:
        self.l_score += 1

    def r_point(self) -> None:
        self.r_score += 1
