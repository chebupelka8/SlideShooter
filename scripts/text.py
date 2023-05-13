import pygame
import math
import time

def SetText(text=' ', pos=(0, 0), size=12, font='arial', color='white', jump=False):
    display = pygame.display.get_surface() # main display
    
    font = pygame.font.SysFont(font, size).render(text, True, color)

    if not jump: rect = font.get_rect(center=pos)
    if jump: rect = font.get_rect(center=(pos[0], pos[1] + (math.sin(time.time() * 8) * 10)))
    
    display.blit(font, rect)