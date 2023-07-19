from Font import *
import pygame


class Button:
    def __init__(self, x, y, w, h, txt, color):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.t = Font(30, True, txt, (0, 0, 0))
        self.c = color
        self.c1 = color

    def drawbutton(self, win):
        pygame.draw.rect(win, self.c, (self.x, self.y, self.w, self.h))
        pygame.draw.rect(win, (0, 0, 0), (self.x, self.y, self.w, self.h), 3)
        font = self.t
        font.create(win, self.x + 5, self.y + 5)

    def touching(self, pos):
        if self.x < pos[0] < self.x + self.w:
            if self.y < pos[1] < self.y + self.h:
                self.c = (255, 255, 255)
                return True
            else:
                self.c = self.c1
                return False
        else:
            self.c = self.c1
            return False
