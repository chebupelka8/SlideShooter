import pygame
from pygame.locals import *
from scripts.settings import *
from scripts.monsters import Enemy
from scripts.bullets import Bullets
from scripts.player import Player
from scripts.particles import Particles
from scripts.text import SetText
from scripts.cursor import Cursor
from scripts.bonus import Bonus
from scripts.fon import Fon
from scripts.menu import MenuButton
from scripts.record import *
from time import time
import sys 

pygame.init()

pygame.mixer.music.load('SlideShooter\music\8597bb02c2b2555.mp3')
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)

class Game:
    def __init__(self):
        self.display = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_icon(pygame.image.load('SlideShooter\pictures\monster\enemy.png'))
        self.scene = 0
    
    def update(self):
        pygame.display.update()
        self.clock.tick(FPS)
        self.display.fill('#FFBF9B')
        self.display.fill((70, 70, 70))
        pygame.display.set_caption(f'SlideShooter       |         FPS:{int(self.clock.get_fps())}')
    
    def events(self):
        for self.event in pygame.event.get():
            if self.event.type == QUIT: 
                self.run = False
            
            if self.event.type == KEYDOWN:
                if self.event.key == K_ESCAPE and self.scene == 1: self.scene = 2
    
    def new_classes(self):
        # menu
        self.btn_start = MenuButton(pos=(250, 200), size=(190, 35), text='START', text_size=22, text_color='white')
        self.btn_profile = MenuButton(pos=(250, 250), size=(190, 35), text='PROFILE', text_size=22, text_color='white')
        self.btn_info = MenuButton(pos=(250, 300), size=(190, 35), text='Information', text_color='white', text_size=22)
        self.btn_quit = MenuButton(pos=(250, 350), size=(190, 35), text='QUIT', text_size=22, text_color='white')

        # exit menu
        self.btn_resume = MenuButton(pos=(250, 100), size=(190, 35), text='RESUME', text_size=22, text_color='white')
        self.btn_exit = MenuButton(pos=(250, 150), size=(190, 35), text='EXIT', text_color='white', text_size=22)

        # information 
        self.btn_back = MenuButton(pos=(35, 10), size=(70, 25), text='Back', text_color='white', text_size=12)

        # game
        self.player = Player(pos=(250, 480))
        self.bullet = Bullets(pos=self.player.rect.center)
        self.enemy = Enemy(pos=(250, -30))

        self.particles = Particles()
        self.cursor = Cursor(filename='SlideShooter\pictures\cursor\cursor.png', edit=1)
        
        self.bonus = Bonus()
        self.bonus_particle = Particles()
        self.fon = Fon()
    
    def new(self):
        # game
        self.bullet_rect = pygame.Rect(0, 0, 10, 10)
        self.enemy_rect = pygame.Rect(0, 0, 27, 39)

        self.lose_score = 0
        self.score = 0

        self.start_time = time()
        self.bonus_time = None
    
    def menu(self): # menu
        self.fon.update()
        
        SetText(text='SlideShooter', color='white', pos=(250, 100), size=52, font='comic sans ms', jump=True)

        self.btn_start.update()
        self.btn_start.update_press(color_standart=(0, 250, 0), color_collide=(0, 120, 0), color_press=(0, 80, 0))
        if self.btn_start.get_pressed(): self.scene = 1

        self.btn_profile.update()
        self.btn_profile.update_press(color_standart=(194, 178, 128), color_collide=(139, 128, 0), color_press=(139, 128, 0))
        if self.btn_profile.get_pressed(): self.scene = 4

        self.btn_info.update()
        self.btn_info.update_press(color_standart=(0, 100, 250), color_collide=(0, 50, 120), color_press=(0, 50, 80))
        if self.btn_info.get_pressed(): self.scene = 3

        self.btn_quit.update()
        self.btn_quit.update_press(color_standart=(250, 0, 0), color_collide=(120, 0, 0), color_press=(80, 0, 0))
        if self.btn_quit.get_pressed(): sys.exit()

        pygame.mouse.set_visible(True)
    
    def profile(self):
        self.fon.update()

        SetText(text='Profile', color='white', pos=(250, 30), size=52, font='comic sans ms', jump=True)

        self.btn_back.update()
        self.btn_back.update_press(color_standart=(100, 100, 100), color_collide=(60, 60, 60), color_press=(30, 30, 30))
        if self.btn_back.get_pressed(): self.scene = 0

        SetText(text='K/D ' + str(round(get_max_score('SlideShooter\scripts\score.txt') / get_max_score('SlideShooter\scripts\lose_scores.txt'), 2)), pos=(250, 250), font='comic sans ms', color='light blue', size=34)
        SetText(text='Record score: ' + str(get_max_score('SlideShooter\scripts\score.txt')), pos=(250, 360), color='light green', font='comic sans ms', size=16)
        SetText(text='Lose score: ' + str(get_max_score('SlideShooter\scripts\lose_scores.txt')), pos=(250, 380), color='light green', font='comic sans ms', size=16)

    
    def exit_menu(self):
        self.fon.update()

        SetText(text='Pause', color='white', pos=(250, 30), size=52, font='comic sans ms', jump=True)

        self.btn_resume.update()
        self.btn_resume.update_press(color_standart=(0, 100, 250), color_collide=(0, 50, 120), color_press=(0, 50, 80))
        if self.btn_resume.get_pressed(): self.scene = 1

        self.btn_exit.update()
        self.btn_exit.update_press(color_standart=(250, 0, 0), color_collide=(120, 0, 0), color_press=(80, 0, 0))
        if self.btn_exit.get_pressed(): self.scene = 0

        pygame.mouse.set_visible(True)
    
    def information(self):
        self.fon.update()

        SetText(text='Information', pos=(250, 50), color='white', size=52, font='comic sans ms', jump=True)
        
        self.btn_back.update()
        self.btn_back.update_press(color_standart=(100, 100, 100), color_collide=(60, 60, 60), color_press=(30, 30, 30))
        if self.btn_back.get_pressed(): self.scene = 0

        SetText(text='Version - v.0.3', pos=(120, 260), color='white', size=16, font='comic sans ms')
        
        SetText(text="What's new?", pos=(115, 310), color='white', size=16, font='comic sans ms')
        SetText(text='-Menu', pos=(100, 330), color='white', size=16, font='comic sans ms')
        SetText(text='-Pause', pos=(100, 350), color='white', size=16, font='comic sans ms')
        SetText(text='-Profile', pos=(105, 370), color='white', size=16, font='comic sans ms')
        SetText(text='-Record Score', pos=(130, 390), color='white', size=16, font='comic sans ms')
        SetText(text='-Fix bugs', pos=(110, 410), color='white', size=16, font='comic sans ms')

        SetText(text='Developer: Stepa Zamyatin', pos=(120, 460), color='white', size=16, font='comic sans ms')
        SetText(text='Textures: itch.io', pos=(80, 480), color='white', size=16, font='comic sans ms')


        pygame.mouse.set_visible(True)


    def game(self): # main game 
        self.new_time = time()

        self.fon.update()

        # record 
        if self.score > get_max_score(filename='SlideShooter\scripts\score.txt'): write_score(self.score, filename='SlideShooter\scripts\score.txt')
        if self.lose_score > get_max_score(filename='SlideShooter\scripts\lose_scores.txt'): write_score(self.lose_score, filename='SlideShooter\scripts\lose_scores.txt')
        
        # bullet
        self.bullet.update()
        self.bullet.rotate(self.player.rect.center)
        self.bullet.flugbahn()
        self.bullet.update_pos(self.player.rect.center)

        # player
        self.player.move()
        self.player.update()
        self.player.barrier()
        self.player.animation()   

        # collisions;
        # enemy
        for enemy in self.enemy.enemies:
            enemy[0][0] -= enemy[1][0]
            enemy[0][1] -= enemy[1][1]

            self.enemy.update(pos=(enemy[0][0], enemy[0][1]))

            if enemy[0][1] > 500 or enemy[0][0] < 0 or enemy[0][0] > 500:
                self.enemy.enemies.remove(enemy)
                self.lose_score += 1
            
            if enemy[0][1] < -30: self.enemy.enemies.remove(enemy)

            # bullet
            for bullet in self.bullet.bullets:
                    self.bullet_rect.center = (bullet[0][0], bullet[0][1])

                    if self.bullet_rect.colliderect(self.enemy):
                        self.enemy.enemies.remove(enemy)
                        self.score += 1

                        for i in range(10):
                            self.particles.add(pos=(enemy[0][0], enemy[0][1]), shade='monster')
            self.particles.spawn()
        
        # spawn enemy
        if len(self.enemy.enemies) < 2: self.enemy.add()


        # bonus
        self.bonus.update()
        if len(self.bonus.bonuses) > 0:
            if self.player.get_collide(self.bonus.rect): 
                self.bonus.delete()
                self.bonus_time = time()

                if self.bonus.bonus[2][0] == 1: 
                    self.bullet.set_queue(queue=1)

                    # particles bonus
                    for i in range(10):
                        self.bonus_particle.add(pos=(self.bonus.bonus[0][0], self.bonus.bonus[0][1]), shade='bonus_blue')
                
                if self.bonus.bonus[2][0] == 0: 
                    self.player.set_speed(speed=4)

                    # particles bonus
                    for i in range(10):
                        self.bonus_particle.add(pos=(self.bonus.bonus[0][0], self.bonus.bonus[0][1]), shade='bonus_green')         
            
        self.bonus_particle.spawn()

        # update queue & speed
        if self.bonus_time != None: 
            if self.new_time - self.bonus_time > 5: 
                self.player.set_speed(speed=1)
                self.bullet.set_queue(queue=10)
                

        # texts
        SetText(text=f'Scores: {self.score}', pos=(45, 10), font='comic sans ms', size=16, color='green')
        SetText(text=f'Lose scores: {self.lose_score}', pos=(65, 30), font='comic sans ms', size=16, color='red')

        SetText(text=f'Time: {round(self.new_time - self.start_time, 1)}', pos=(455, 10), font='comic sans ms', size=16, color='light blue')

        self.cursor.update() # cursor

    def main(self):
        self.new_classes()
        self.new()

        self.run = True
        while self.run:
            
            if self.scene == 0: self.menu()
            if self.scene == 1: self.game()
            if self.scene == 2: self.exit_menu()
            if self.scene == 3: self.information()
            if self.scene == 4: self.profile()

            self.update()
            self.events()
        
        pygame.quit()

if __name__ == '__main__': game = Game().main()