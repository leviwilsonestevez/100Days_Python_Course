from Home import *
import pygame

pygame.init()
clock = pygame.time.Clock()
home = Home()
Home.main(home, clock=clock)
