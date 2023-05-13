import pygame
from random import choice, randint, random

class Particles:
    def __init__(self):
        self.display = pygame.display.get_surface()
        
        self.particles = []
    
    def add(self, pos=(0, 0), shade='gray'):
        
        self.x, self.y = pos
        self.shades = {
            'gray': [(80, 80, 80), (100, 100, 100), (130, 130, 130), (160, 160, 160), (180, 180, 180)],
            'monster': ['green', 'red', 'green'],
            'bonus_blue': ['blue', 'light blue'],
            'bonus_green': ['green', 'light green']
        }

        self.particles.append([[self.x, self.y], [random() * (1 + 1) - 1, random() * (1 + 1) - 1], [randint(3, 14)], [choice(self.shades[shade])]])
    
    def spawn(self):
        for self.particle in self.particles:
            self.particle[0][0] -= self.particle[1][0]
            self.particle[0][1] -= self.particle[1][1]
            self.particle[2][0] -= 0.05

            pygame.draw.rect(self.display, self.particle[3][0], (self.particle[0][0], self.particle[0][1], self.particle[2][0], self.particle[2][0]))
            #pygame.draw.circle(self.display, self.particle[3][0], (self.particle[0][0], self.particle[0][1]), self.particle[2][0])

            if self.particle[2][0] < 0: self.delete()
    
    def update(self):
        self.mousepress = pygame.mouse.get_pressed()
        self.mousepos = pygame.mouse.get_pos()

        if self.mousepress[0]: self.add(pos=self.mousepos)
        self.spawn()
    
    def delete(self):
        self.particles.remove(self.particle)