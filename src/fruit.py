import pygame
from random import randint


class Fruit:
    def __init__(self, screen):
        """ a simple idea of a fruit """
        self.position = (randint(0, 39) * 20, randint(0, 24) * 20)
        self.color = (255, 0, 0)

        self.screen = screen
        self.surface = pygame.Surface((15, 15))
        self.surface.fill(self.color)

    def update(self):
        """ Updates the coordinates of the fruit """
        self.position = (randint(0, 39) * 20, randint(0, 24) * 20)

    def render(self):
        """ Draws the fruit turn on the screen """
        self.screen.blit(self.surface, self.position)
