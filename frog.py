import pygame
import globals

class Frog():
    """ The Basic frog object for out game. """

    def __init__(self, color=globals.GREEN, pos=[10, 10]):
        self.pos = pos
        self.size = [25, 25]
        self.color = color
        self.direction = "UP"
        self.collision = 0
        self.window = pygame.display.get_surface()

    def display(self):
        pygame.draw.rect(
            self.window,
            self.color,
            (
                self.pos[0],
                self.pos[1],
                self.size[0],
                self.size[1]
            )
        )
