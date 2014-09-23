import pygame
import globals

class Vehicle():
    """ The basic vehicle. """

    def __init__(self, color=globals.GREEN, pos=[10, 10]):
        self.pos = pos
        self.size = [200, 45]
        self.color = color
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
