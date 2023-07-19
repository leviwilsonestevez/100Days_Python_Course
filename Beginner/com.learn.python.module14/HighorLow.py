from art import logo, vs
from game_data import data
from random import randint


def check_answer(guess, competitor_a_followers, competitor_b_followers) -> bool:
    if competitor_a_followers > competitor_b_followers:
        return guess == "A" or guess == "a"
    else:
        return guess == "B" or guess == "b"


def game() -> None:
    print(logo)
    game_should_continue = True
    score = 0
    competitor_a = data[randint(0, len(data))]
    competitor_b = data[randint(0, len(data))]
    while game_should_continue:
        while competitor_a == competitor_b:
            competitor_b = data[randint(0, len(data))]
        print(f"Compare A : {competitor_a['name']} . a {competitor_a['description']} from {competitor_a['country']}")
        print(vs)
        print(f"Against B : {competitor_b['name']} .a {competitor_b['description']} from {competitor_b['country']}")
        guess = input(f"Who has more followers ? Type 'A' or 'B': ")
        result = check_answer(guess, competitor_a["follower_count"], competitor_b["follower_count"])
        if result:
            score += 1
            print(f"You're right. You score is {score}")
        else:
            print(f"You're wrong. You score is {score}")
            return


game()