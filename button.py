import pygame
from settings import *

class Button:
    def __init__(self, x, y, width, height, text = None, function = None ,params = None):
        self.image = pygame.Surface((width, height))
        self.pos = (x, y)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos
        self.text = text
        self.color = COLOR_BLUE
        self.colorHighlighted = COLOR_GRAY
        self.function = function
        self.params = params
        self.highlighted = False

    def update(self, mousePos):
        # if the mouse is hovering over the button
        if (self.rect.collidepoint(mousePos)):
            self.highlighted = True
        else:
            self.highlighted = False
    
    def draw(self, window):
        self.image.fill(self.colorHighlighted if self.highlighted else self.color)
        window.blit(self.image, self.pos)

