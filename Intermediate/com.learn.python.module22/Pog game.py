from turtle import Screen
from Paddle import Paddle
from Ball import Ball
import time
from ScoreBoard import ScoreBoard

screen = Screen()
width = 600
heigth = 600
screen.setup(width=width, height=heigth)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle_x = (width / 2) - 20
width *= -1
l_paddle_x = (width / 2) + 20
width *= -1

bounce_top = (heigth / 2) - 10
heigth *= -1
bounce_bottom = (heigth / 2) + 10
heigth *= -1

r_paddle = Paddle((r_paddle_x, 0))
l_paddle = Paddle((l_paddle_x, 0))
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()

screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()
    # Collision with walls
    if ball.ycor() > bounce_top or ball.ycor() < bounce_bottom:
        ball.bounce_y()
    if ball.distance(r_paddle) < 30 and ball.xcor() > 250:
        ball.bounce_x()
    if ball.distance(l_paddle) < 40 and ball.xcor() > -260:
        ball.bounce_x()
    if ball.xcor() > width:
        ball.reset_position()
        scoreboard.l_point()
        scoreboard.update_scoreboard()
    if ball.xcor() < -width:
        ball.reset_position()
        scoreboard.r_point()
        scoreboard.update_scoreboard()

screen.exitonclick()
