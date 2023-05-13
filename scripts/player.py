from pygame.locals import *
import pygame
from scripts.sprite import Sprite

class Player(Sprite):
    def __init__(self, pos=(0, 0)):
        self.display = pygame.display.get_surface()

        self.image = pygame.image.load('SlideShooter/pictures/player/Idle/Slime_Medium_Red1.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_size()[0] * 3, self.image.get_size()[1] * 3))
        super().__init__(pos=(pos))
        self.rect = self.image.get_rect(center=self.position)

        self.action = 0
        self.frame = 1
        self.speed = 1
    
    def animation(self):
        self.frame += 0.05
        if self.frame > 4: self.frame = 1

        self.actions = ['Idle', 'Left', 'Right']

        self.image = pygame.image.load(f'SlideShooter/pictures/player/{self.actions[self.action]}/Slime_Medium_Red{int(self.frame)}.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_size()[0] * 3, self.image.get_size()[1] * 3))
    
    def move(self):

        self.keypress = pygame.key.get_pressed()

        if self.keypress[K_LEFT]: 
            self.position.x -= self.speed
            self.action = 1
        
        if self.keypress[K_RIGHT]: 
            self.position.x += self.speed
            self.action = 2
        
        if not self.keypress[K_LEFT] and not self.keypress[K_RIGHT]: self.action = 0
    
    def set_speed(self, speed):
        self.speed = speed
    
    def get_collide(self, body):
        return self.rect.colliderect(body)

    def barrier(self):

        if self.position.x > 510: self.position.x = -10
        if self.position.x < -10: self.position.x = 510
    
    def update(self):

        self.rect = self.image.get_rect(center=self.position)
        self.display.blit(self.image, self.rect)

    