import pygame
import globals

class Road():

    def __init__(self, pos=[0, globals.HEIGHT-100]):
        self.pos = pos
        self.size = [800, 100]
        self.color = globals.BROWN
        self.window = pygame.display.get_surface()

    def display(self):
        pygame.draw.rect(
            self.window,
            self.color,
            (
                self.pos[0],
                self.pos[1],
                self.size[0],
                self.size[1]/2
            )
        )
        pygame.draw.rect(
            self.window,
            self.color,
            (
                self.pos[0],
                self.pos[1]+50,
                self.size[0],
                self.size[1]/2
            )
        )
        pygame.draw.rect(
        self.window,
        globals.BLACK,
        (
            self.pos[0],
            self.pos[1]+45,
            self.size[0],
            10
        )
    )
