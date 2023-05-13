import pygame
from math import cos, sin, atan2
from random import choice

class Bullet:
    def __init__(self, pos=(0, 0)):
        self.position = pygame.Vector2(pos)


class Bullets(Bullet):
    def __init__(self, pos=(0, 0)):
        self.display = pygame.display.get_surface()

        self.speed = 5
        self.bullets = []
        self.time = 0
        self.queue = 10

        super().__init__(pos=pos)
    
    def rotate(self, pos):
        self.mx, self.my = pygame.mouse.get_pos()
        self.x, self.y = pos

        self.rel_angle = atan2(self.y - self.my, self.x - self.mx)
        self.velx = cos(self.rel_angle) * self.speed
        self.vely = sin(self.rel_angle) * self.speed

    def flugbahn(self):

        self.angle = atan2(self.x - self.mx, self.y - self.my)
        pygame.draw.aaline(self.display, 'red', (self.x, self.y), ((self.x + sin(self.angle) * -50), (self.y + cos(self.angle) * -50)))
    
    def update_pos(self, pos):
        self.position = pygame.Vector2(pos)

    def add(self):
        colors = ['orange', 'yellow', 'light blue', 'violet', 'purple', 'light gray', 'red', 'green']
        self.bullets.append([[self.position.x, self.position.y], [self.velx, self.vely], [choice(colors)]])
    
    def spawn(self):
        for self.bullet in self.bullets:
            self.bullet[0][0] -= self.bullet[1][0]
            self.bullet[0][1] -= self.bullet[1][1]

            self.circle = pygame.draw.circle(self.display, 'light blue', (self.bullet[0][0], self.bullet[0][1]), 5)

            if self.bullet[0][1] < 0: self.delete()

    def update(self):
        self.time += 0.1

        self.mousepos = pygame.mouse.get_pos()
        self.mousepress = pygame.mouse.get_pressed()

        if self.mousepress[0] and self.time >= self.queue:
            self.add()
            self.time = 0
        
        self.spawn()
    
    def set_queue(self, queue):

        self.queue = queue
    
    def delete(self):
        self.bullets.remove(self.bullet)
