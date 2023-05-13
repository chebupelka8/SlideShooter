import pygame
from random import randint, random, choice

class Fon:
    def __init__(self):
        self.display = pygame.display.get_surface()

        self.particles = []
    
    def add(self):
        colors = [(80, 80, 80), (85, 85, 85), (90, 90, 90), (95, 95, 95)]
        self.particles.append([[randint(0, 500), randint(0, 500)], [random() * (1 + 1) - 1, random() * (1 + 1) - 1], [choice(colors)], [randint(3, 10)], [randint(0, 1)]])
    
    def spawn(self):
        for self.particle in self.particles:
            self.particle[0][0] -= self.particle[1][0]
            self.particle[0][1] -= self.particle[1][1]

            pygame.draw.rect(self.display, self.particle[2][0], (self.particle[0][0], self.particle[0][1], self.particle[3][0], self.particle[3][0]), self.particle[4][0])

            if self.particle[0][0] >= 500 or self.particle[0][0] <= 0 or self.particle[0][1] >= 500 or self.particle[0][1] <= 0: self.delete()
    
    def update(self):
        if len(self.particles) < 100:
            self.add()
        self.spawn()

    def delete(self):
        self.particles.remove(self.particle)