import pygame


class Font:
    def __init__(self, size, bold, text, color):
        self.name = 'blackjack'
        self.size = size
        self.bold = bold
        self.t = text
        self.c = color

    def create(self, surf, x, y):
        self.font = pygame.font.SysFont(self.name, self.size, self.bold)
        self.text = self.font.render(self.t, False, self.c)
        surf.blit(self.text, (x, y))
