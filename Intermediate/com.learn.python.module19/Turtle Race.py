import random
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
width = 500
height = 400
screen.setup(width, height)
user_bet = screen.textinput(title="Make your bet", prompt="Wich turtle will win in the race? Choose a color : ")
colors_to_draw = ["red", "green", "blue", "orange", "purple", "pink", "yellow"]
turtles = []
init = int(width / 2) - width
y_positions = [-70, -40, -10, 20, 50, 80]
for i in range(0, 6):
    tim = Turtle("turtle")
    tim.color(colors_to_draw[i])
    tim.penup()
    tim.goto(init, y_positions[i])
    tim.pendown()
    turtles.append(tim)

if user_bet in colors_to_draw:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 250:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("You win")
            else:
                print(f"The winning turtle is the {winning_color} turtle")
        forward_turtle = random.randint(0, 10)
        turtle.penup()
        turtle.forward(forward_turtle)
        turtle.pendown()

screen.exitonclick()
