from Button import *
from Cards import *
from Music import *
from PlayBoard import *
import pygame


class Home:
    global width, height, counter, deck, player_hand, p_hand_val, hit, set, pos
    global bet, hand_cash, bet_value, stand, b_hand_val, bot_hand, p_dis, b_dis, compare
    global BetRatio, DoubleDown

    def main(self, clock) -> None:
        width = 800
        height = 600
        standar_window = pygame.display.set_mode((width, height))
        main_background = pygame.transform.scale(pygame.image.load('images/background/Background.png'), (width, height))
        game_background = pygame.transform.scale(pygame.image.load('images/playboard/PlayingBoard.jpg'),
                                                 (width, height))
        pygame.display.set_caption("BlackJack Game")
        run = True
        main = True
        play = False
        mode = False
        bet = True
        StartButton = Button(width // 2 - 50, height // 2, 100, 60, "PLAY", (0, 255, 0))
        EasyButton = Button(width // 2 - 100, height // 10, 200, 100, "Easy (3:2)", (0, 255, 255))
        MeadButton = Button(width // 2 - 100, height // 10 + 120, 200, 100, "Medium (5:4)", (255, 128, 0))
        HardButton = Button(width // 2 - 100, height // 10 + 240, 200, 100, "Hard (6:5)", (255, 0, 0))
        HitButton = Button(width - 100, height // 2, 80, 40, "Hit", (0, 255, 0))
        StandButton = Button(width - 100, height // 2 + 50, 80, 40, "Stand", (255, 0, 0))
        DDownButton = Button(width - 100, height // 2 + 100, 80, 40, "Ddown", (0, 128, 255))
        QUIT = Button(width - 100, 0, 100, 40, "QUIT", (255, 0, 0))
        Hundred = Button(20, height - 60, 100, 40, "100", (255, 0, 255))
        Tundred = Button(130, height - 60, 100, 40, "200", (128, 255, 13))
        Thundred = Button(240, height - 60, 100, 40, "300", (255, 128, 0))
        Frundred = Button(350, height - 60, 100, 40, "400", (0, 255, 255))
        Betbuttons = (Hundred, Tundred, Thundred, Frundred)
        play_playlist()
        pygame.mixer.music.set_endevent(pygame.USEREVENT)
        while run:
            clock.tick(30)
            keys = pygame.key.get_pressed()
            if main:
                self.mainPage(surf=standar_window, button1=main_background, button2=StartButton)
            elif play:
                playboard = PlayBoard(width=width, height=height)
                playboard.gamePage(surf=standar_window, b1=game_background, hitter=HitButton,
                                   standing=StandButton, DD=DDownButton,
                                   QUIT=QUIT)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                pos = pygame.mouse.get_pos()
                pressed = pygame.MOUSEBUTTONDOWN
                if event.type == pygame.USEREVENT:
                    play_playlist()
                if main:
                    if StartButton.touching(pos) and event.type == pressed:
                        main = False
                        mode = True
                elif mode:
                    if EasyButton.touching(pos) and event.type == pressed:
                        play = True
                        mode = False
                        BetRatio = 1.5
                    elif MeadButton.touching(pos) and event.type == pressed:
                        play = True
                        mode = False
                        BetRatio = 1.25
                    elif HardButton.touching(pos) and event.type == pressed:
                        play = True
                        mode = False
                        BetRatio = 1.2
                elif bet:
                    vals = (100, 200, 300, 400)
                    for i in range(len(Betbuttons)):
                        if Betbuttons[i].touching(pos) and event.type == pressed:
                            bet_value = vals[i]
                            bet = False
                            set = True
                elif play:
                    if HitButton.touching(pos) and event.type == pressed:
                        hit = True
                    elif StandButton.touching(pos) and event.type == pressed:
                        stand = True
                    elif DDownButton.touching(pos) and event.type == pressed:
                        DoubleDown = True
                    elif QUIT.touching(pos) and event.type == pressed:
                        play = False
                        Home.reset()
                        # Home.build_deck()
                        main = True
                        bet = True
            pygame.display.update()
        pygame.quit()

    def reset(self) -> None:
        deck
        hand_cash = 5000
        counter = 51
        while len(deck) > 0:
            deck.pop(0)

    def mainPage(self, surf, button1, button2) -> None:
        surf.blit(button1, (0, 0))
        button2.drawbutton(surf)


