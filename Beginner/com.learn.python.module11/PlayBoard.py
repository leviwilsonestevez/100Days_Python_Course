import random

from Button import *
from Cards import *


class PlayBoard:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def gamePage(self, surf, b1, hitter, standing, DD, QUIT):
        global hit, set, bet, hand_cash, bet_value, stand, p_dis, b_dis, compare
        global p_hand_val, b_hand_val, BetRatio, DoubleDown
        hand_cash = 5000
        bet_value = 0
        bet = True
        deck = self.build_deck()
        surf.blit(b1, (0, 0))
        currency = Button(0, self.height // 1.5, 150, 30, "Cash: " + str(hand_cash), (255, 0, 0))
        betting = Button(0, self.height // 1.3, 150, 30, "Bet: " + str(bet_value), (0, 128, 255))
        currency.drawbutton(surf)
        betting.drawbutton(surf)
        user_cards = []
        computer_cards = []
        is_game_over = False

    def build_deck(self) -> list:
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
                deck.append(Cards(100, 100, sufix_values[j], images[i], worth))
        return deck
