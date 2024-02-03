import pygame
from laser import Laser

pygame.init()

class Player:
    playerimg = pygame.image.load('public/images/spaceship1.png')
    posX = 400
    posY = 480
    
    #velocity
    vx = 0
    vy = 0
    
    lasers = []
    is_shooting = False
    
    is_dead = False
    
    shoot_sfx = pygame.mixer.Sound('public/sounds/blaster-2-81267.mp3')
    def show(self, screen):
        # show player
        screen.blit(self.playerimg, (self.posX, self.posY))
        # show lasers
        for laser in self.lasers:
            laser.show(screen)
    
    def shoot(self):
        self.lasers.append(Laser(self.posX, self.posY, 0 ,-1, (255,255,0)))
        self.shoot_sfx.play()
    
    def move(self):
        # move laser
        for laser in self.lasers:
            laser.move()
            
        # move player
        self.posX += self.vx
        self.posY += self.vy
    
    def check_boundaries(self):
        if self.posX <= 0:
            self.posX = 0 
        elif self.posX >= 736:
            self.posX = 736 
            
    def rem_extra_lasers(self):
        self.lasers = [laser for laser in self.lasers if laser.is_alive()]
    
    def check_shooting(self, enemies):
        self.lasers = [laser for laser in self.lasers if laser.is_alive()]
        for laser in self.lasers:
            for enemy in enemies:
                if enemy.is_dead:
                    continue
                if laser.intersect(enemy):
                    laser.alive = False
                    enemy.is_dead = True
                    break
                
                
    def update(self , screen):
        if not self.is_dead:
            self.move()
            self.check_boundaries()
            self.rem_extra_lasers()
            
            if self.is_shooting :
                self.shoot()
            
            self.show(screen)
        
    

