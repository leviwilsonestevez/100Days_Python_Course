from Font import *
import pygame


class Cards:
    def __init__(self, x, y, val, suit, worth):
        self.x = x
        self.y = y
        self.v = val
        self.n = worth
        self.f2 = pygame.transform.scale(pygame.image.load(suit), (15, 15))

    def face_up(self, win):
        white = (255, 255, 255)
        pygame.draw.rect(win, white, (self.x, self.y, 40, 80))
        pygame.draw.rect(win, (255, 0, 0), (self.x, self.y, 40, 80), 3)
        self.f1.create(win, self.x + 5, self.y)
        win.blit(self.f2, (self.x + 5, self.y + 20))

    def face_down(self, win):
        pygame.draw.rect(win, (255, 0, 0), (self.x, self.y, 40, 80))
        pygame.draw.rect(win, (255, 255, 255), (self.x, self.y, 40, 80), 3)
