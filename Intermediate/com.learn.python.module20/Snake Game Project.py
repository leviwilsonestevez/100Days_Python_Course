import time
from turtle import Screen

from Snake import Snake
from Food import Food
from ScoreBoard import ScoreBoard

screen = Screen()
screen.setup(width=650, height=650)
screen.bgcolor("black")
screen.tracer(0)
screen.title("My Snake Game")

snake = Snake()
food = Food()
score_board = ScoreBoard()

screen.listen()
# Case sensitive
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.14)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        score_board.increase_score()
        snake.extend()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score_board.reset()
        snake.reset()
    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 15:
            score_board.reset()
            snake.reset()

screen.exitonclick()
