from math import sqrt
import pygame

pygame.init()

class Laser:
    #dimesions , positon, velcity
    dx = 5
    dy = 25
    
    px = 0
    py = 0
    
    vx = 0
    vy = 0
    
    color = (0, 0, 0)
    alive = True
    
    explosion_sfx = pygame.mixer.Sound('public/sounds/explosion.wav')
    def __init__(self , posx, posy, velx, vely, color):
        self.px = posx + 28
        self.py = posy
        self.vx = velx
        self.vy = vely
        self.color = color
        
    
    def move(self):
        self.px += self.vx
        self.py += self.vy
        
    def show(self, screen):
        if self.alive :
            pygame.draw.rect(screen, self.color, pygame.Rect(self.px, self.py, self.dx, self.dy))
        
    def is_alive(self):
        if self.py < 0: #exited the screen
            self.alive = False
            return False
        else:
            return True
        
    def intersect(self, enemy):
        # TODO: adding some explosion animation here
        
        # if cartesian distance between enemy and laser is less than 20 than intersect is tru
        if sqrt((self.px - enemy.posX)**2 + (self.py - enemy.posY)**2) < 30  :
            self.explosion_sfx.play()
            return True
        else:
            return False