from turtle import Turtle, Screen
import turtle as t

screen = Screen()
screen.title("Welcome to the turtle zoo!")
def draw_square(length: float) -> None:
    timmy_the_turtle = Turtle()
    timmy_the_turtle.shape("turtle")
    timmy_the_turtle.color("red")
    for i in range(4):
        timmy_the_turtle.forward(length)
        timmy_the_turtle.right(90)


draw_square(length=100.00)


screen.exitonclick()
