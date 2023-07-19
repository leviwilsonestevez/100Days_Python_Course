from turtle import Turtle, Screen, mainloop, onscreenclick
import csv

FONT = ("Courier", 8, "normal")
screen = Screen()
screen.title("U.S states game")
turtle = Turtle()
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
acerted_states = 0
game_is_on = True
while game_is_on:
    answer_state = screen.textinput(title=f"Guess the state {acerted_states}/50",
                                    prompt="What's another state's name ? ")
    with open("50_states.csv", mode="r") as file:
        united_states = csv.reader(file)
        next(united_states)
        for state_data in united_states:
            if answer_state.lower() == state_data[0].lower():
                acerted_states += 1
                turtle_state = Turtle()
                turtle_state.hideturtle()
                turtle_state.penup()
                turtle_state.goto(float(state_data[1]), float(state_data[2]))
                turtle_state.write(f"{answer_state}", align="left", font=FONT)
    if acerted_states == 50:
        game_is_on = False
    if answer_state == "exit":
        game_is_on = False

# Identify the coordinate
# def get_mouse_click_coordinates(x: float, y: float) -> None:
# print(x, y)
# onscreenclick(get_mouse_click_coordinates)
