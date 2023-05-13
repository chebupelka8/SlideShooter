import pygame

class Sprite: # main class for sprite
    def __init__(self, pos=(0, 0)):
        self.position = pygame.Vector2(pos)
    
