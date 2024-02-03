import pygame 
import random
from laser import Laser
import time
 
class Enemy:
    enemyimg = pygame.image.load('public/images/ufo.png')
    is_dead = False
    lasers = []
    
    def __init__(self, posX, posY, vx, vy, attck_frequency):
        self.posX = posX
        self.posY = posY

        self.vx = vx
        self.vy = vy
        
        self.ATTACK_FREQ = attck_frequency
    def show(self, screen):
        #show lasers
        for laser in self.lasers:
            laser.show(screen)
        #show enemy
        screen.blit(self.enemyimg, (self.posX, self.posY))

    def move(self):
        #move leasers 
        for laser in self.lasers:
            laser.move()
        #move enemy
        self.posX += self.vx
        self.posY += self.vy
    
    def check_boundaries(self):
        if self.posX <= 0 or self.posX >= 736: 
            self.vx *= -1
        if self.posY <= 0 or self.posY >= 480:
            self.vy *= -1
    
    def rem_extra_lasers(self):
        self.lasers = [laser for laser in self.lasers if laser.is_alive()]
    
    def attack(self , frame_count):
        if frame_count % self.ATTACK_FREQ == 0:
            self.lasers.append(Laser(self.posX, self.posY, 0, 1, (255,0,0)))
    
    def check_shooting(self, players):
        if not self.is_dead:
            self.lasers = [laser for laser in self.lasers if laser.is_alive()]
            for laser in self.lasers:
                for player in players:
                    if laser.intersect(player) and not player.is_dead:
                        laser.alive = False
                        player.is_dead = True
                        break
    
    def update(self , screen, frame_count):
        if not self.is_dead:
            self.move()
            self.check_boundaries()
            self.show(screen)
            self.attack(frame_count)
            
            
        