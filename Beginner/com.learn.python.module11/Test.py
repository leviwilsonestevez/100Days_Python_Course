from Cards import *


def build_deck() -> None:
    global deck
    deck = []
    images = []
    extension = ".jpg"
    while len(deck) > 0:
        deck.pop(0)
    # key : type_card   value : worth
    sufix_values = (
        {"a": 1}, {'2': 2}, {'3': 3}, {'4': 4}, {'5': 5}, {'6': 6}, {'7': 7}, {'8': 8}, {'9': 9},
        {'10': 10}, {'j': 10}, {'q': 10}, {'k': 10})
    card_types_directories = (
        'images/clover/clover_', 'images/diamond/diamond_', 'images/heart/heart_', 'images/spade/spade_')
    for i in range(len(card_types_directories)):
        for j in range(len(sufix_values)):
            card_type = card_types_directories[i]
            sufix = sufix_values[j]
            worth = 0
            for key in sufix:
                image = card_type + key + extension
                worth = sufix[key]
            images.append(image)
            deck.append(Cards(20, 20, sufix_values[j], images[i], worth))
    print(deck)


build_deck()

