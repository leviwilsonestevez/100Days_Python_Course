from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")


class ScoreBoard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        highest_score = open("highest_score.txt", mode="r")
        self.high_score = int(highest_score.read())
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self) -> None:
        self.clear()
        self.write(f"Score : {self.score} | High Score :{self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self) -> None:
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        with open("highest_score.txt", mode="w") as highest_score:
            highest_score.write(str(self.high_score))
        self.update_scoreboard()

    def increase_score(self) -> None:
        self.score += 1
        self.update_scoreboard()
