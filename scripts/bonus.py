import pygame
from random import randint

class Bonus:
    def __init__(self):
        self.display = pygame.display.get_surface()

        self.images = ['SlideShooter/pictures/bonus/2x_ball.png', 'SlideShooter/pictures/bonus/10x_ball.png']
        self.time = 0
        self.bonuses = []

    def add(self):
        self.bonuses.append([[randint(100, 400), -30], [0, randint(1, 2)], [randint(0, 1)]])
    
    def spawn(self):
        for self.bonus in self.bonuses:
            self.bonus[0][1] += self.bonus[1][1]

            # image
            self.image = pygame.image.load(self.images[self.bonus[2][0]]).convert_alpha()
            self.image = pygame.transform.scale(self.image, (self.image.get_size()[0] * 1.5, self.image.get_size()[1] * 1.5))
            self.rect = self.image.get_rect(center=(self.bonus[0][0], self.bonus[0][1]))
            self.display.blit(self.image, self.rect)
            
            # remove
            if self.bonus[0][1] > 500: self.delete()
    
    def update(self):
        self.time += 0.1

        if len(self.bonuses) < 1 and self.time >= randint(300, 1000): 
            self.time = 0
            self.add()
        self.spawn()
    
    def delete(self):
        self.bonuses.remove(self.bonus)
