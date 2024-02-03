from math import sqrt
import pygame
import time
from player import Player
from enemy import Enemy
import random

# Initialize the game
pygame.init()

# Creating a game (creating the background of the game window)(800 = width, 600 = height)
screen = pygame.display.set_mode((800, 600))

# Titles and Icons
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('public/images/spaceship.png')
pygame.display.set_icon(icon)

#background
background = pygame.image.load('public/images/OIP.jpg')

# Player
player = Player()

#enemy for testing purposes
#enemy
# enemy = Enemy()                   
    
#change total number of enemies
enemy_cnts = 5
enemies = []
def enemies_init():
    for _ in range(enemy_cnts):
        enemies.append(Enemy(random.randint(0, 700), random.randint(0, 300), random.random()/2, 0, random.randint(200,1000))) # enemy(posx, posy, vx, vy, attack_frequency)

running = True
frame_count = 0

enemies_init()
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0,0))
    frame_count += 1
    
    #checking key events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # If keystroke is pressed, check whether it is right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.vx = -0.3
            if event.key == pygame.K_RIGHT:
                player.vx = 0.3    
            if event.key == pygame.K_SPACE:
                # player.is_shooting = True  #uncomment this for cintuous shoots
                player.shoot()        #uncomment this for buttony shoots  
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.vx = 0
            if event.key == pygame.K_SPACE:
                player.is_shooting = False

    
    player.update(screen)
    player.check_shooting(enemies)
    
    for enemy in enemies:
        enemy.update(screen, frame_count)
        enemy.check_shooting([player])
    
    #removing dead enemies
    enemies = [enemy for enemy in enemies if not enemy.is_dead]
    
    if player.is_dead:
        print("GAME OVER\nPlayer is dead!!\nSCORE: ",(frame_count * (enemy_cnts - len(enemies)))) ## score is number of frames survived * the enemies killed
        exit()
        
    if len(enemies) == 0:
        print("You Won!! \nSCORE: ",(frame_count * (enemy_cnts - len(enemies)))) ## score is number of frames survived * the enemies killed
        exit()
    
    pygame.display.update()


print(enemies)