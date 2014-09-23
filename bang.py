import pygame
import globals

class Bang():

    def __init__(self, color=globals.RED, pos=[0, 0]):
        self.pos = pos
        #self.cordinate = [
        self.size = [globals.WIDTH, globals.HEIGHT]
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
