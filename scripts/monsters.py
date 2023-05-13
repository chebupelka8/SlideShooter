import pygame
from scripts.sprite import Sprite
from random import random, randint


class Enemy(Sprite):
    def __init__(self, pos=(0, 0)):
        self.display = pygame.display.get_surface()

        self.image = pygame.image.load('SlideShooter/pictures/monster/enemy.png')
        self.image = pygame.transform.scale(self.image, (self.image.get_size()[0] * 3, self.image.get_size()[1] * 3))
        self.enemies = []
        
        super().__init__(pos=pos)
    
    def add(self):
        self.enemies.append([[randint(100, 400), self.position.y], [random() * (1 + 1) - 1, random() * (1 + 1) - 1]])
            
    def update(self, pos=(0, 0)):
        self.rect = self.image.get_rect(center=pos)
        self.display.blit(self.image, self.rect)


