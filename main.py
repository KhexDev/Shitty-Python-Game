import imp
import math
import json
import random
import sys
from tracemalloc import start
import pygame
from bullet import Bullet
from enemy import Enemy
from CoolUtils import CoolUtils
from player import Player

pygame.init()

print("fuck you boiiiiiiiiiiiiiiii");

WIDTH = 1280
HEIGHT = 720
SPEED = 20
FPS = 120

player_width = 50
player_height = 50

pygame.display.set_caption("SHITTY GAME")
daScreen = pygame.display.set_mode((WIDTH, HEIGHT))

bg = pygame.image.load("bg.jpg")

daPlayer = Player()
daPlayer.daImage = pygame.transform.scale(daPlayer.daImage, (player_width, player_height))

left = False
right = False
down = False
up = False

bullets = []
enemys = []

enemyType = ["normal", "colossal", "minimoys"]

score = 0

running = True


fire = False
canShoot = True

daFont = pygame.font.SysFont(None, 100)

daJson = '{}'

def draw_text(text, font, color, surface, x, y):
    #print("drawing text")
    daText = font.render(text, 1, color)
    daRect = daText.get_rect()
    daRect.topleft = (x, y)
    surface.blit(daText, daRect)

def addEnemy():
    daType = enemyType[random.randint(0,2)]
    print("adding random enemy")
    enemy = Enemy()
    enemy.daType = daType

    if (enemy.daSpawn == "right"):
        enemy.x = WIDTH
        enemy.y = random.randint(0, HEIGHT)
    elif (enemy.daSpawn == "left"):
        enemy.x = -enemy.daImage.get_width()
        enemy.y = random.randint(0, HEIGHT)
    elif (enemy.daSpawn == "up"):
        enemy.y = -enemy.daImage.get_height()
        enemy.x = random.randint(0, WIDTH)
    elif (enemy.daSpawn == "down"):
        enemy.y = HEIGHT
        enemy.x = random.randint(0, WIDTH)

    
    if (enemy.daType == "colossal"):
        enemy.daImage = pygame.transform.scale(enemy.daImage, (80,80))
    elif (enemy.daType == "minimoys"):
        enemy.daImage = pygame.transform.scale(enemy.daImage, (30,30))
    else:        
        enemy.daImage = pygame.transform.scale(enemy.daImage, (50,50))

    print(enemy.x, enemy.y)    
    print(enemy.daSpawn);    
    enemys.append(enemy)

def addingBullet():
    print("adding some bullets")
    bullet = Bullet()
    bullet.daImage = pygame.transform.scale(bullet.daImage, (30, 15))
    bullet.x = daPlayer.x + (player_width / 2)
    bullet.y = daPlayer.y + (player_height / 2)
    bullets.append(bullet)

startTick = pygame.time.get_ticks()
seconds = 0

clock = pygame.time.Clock()

def shittyTimer(seconds, doCode):
    curSeconds = 0
    startTick = pygame.time.get_ticks()
    while curSeconds < seconds:
        curSeconds += (pygame.time.get_ticks() - startTick)/1000
    else:
        doCode()

    


while running:

    elapsed = clock.tick(FPS) / 60


    #event shit
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            running = False
            print("goodbye")
            sys.exit()
        
        if (event.type == pygame.KEYDOWN):

            if (event.key == pygame.K_SPACE and canShoot):
                addingBullet()


            if (event.key == pygame.K_LEFT):
                left = True
            elif (event.key == pygame.K_RIGHT):
                right = True
            if (event.key == pygame.K_DOWN):
                down = True
            elif (event.key == pygame.K_UP):
                up = True

        if (event.type == pygame.KEYUP):

            if (event.key == pygame.K_LEFT):
                left = False
            elif (event.key == pygame.K_RIGHT):
                right = False
            if (event.key == pygame.K_DOWN):
                down = False
            elif (event.key == pygame.K_UP):
                up = False
          
    # print(keys)

    #logic update shit

    # shitty timer
    #probably going to make that a function
    seconds =+ (pygame.time.get_ticks() - startTick)/1000
    if (seconds > 1):
        seconds = 0
        startTick = pygame.time.get_ticks()
        addEnemy()

    #shittyTimer(10 ,addEnemy)



    if (right or left or down or up):
        # print(elapsed)
        if (right and daPlayer.x + SPEED + player_width < WIDTH):
            daPlayer.x += SPEED * elapsed
        if (left and daPlayer.x - SPEED > 0):
            daPlayer.x -= SPEED * elapsed
        if (down and daPlayer.y + SPEED + player_height < HEIGHT):
            daPlayer.y += SPEED * elapsed
        if (up and daPlayer.y - SPEED > -50):
            daPlayer.y -= SPEED * elapsed

    
    #update that shit
    daScreen.blit(bg, (0,0))
    draw_text(str(score), daFont, (255, 255, 255), daScreen, 0, 0)
    daScreen.blit(daPlayer.daImage, (daPlayer.x, daPlayer.y))

    if (len(enemys) > 0):
        for enemy in enemys:
            enemySPEED = 0
            
            if (enemy.daType == "colossal"):
                enemySPEED = 10 * elapsed
            elif (enemy.daType == "minimoys"):
                enemySPEED = 25 * elapsed
            else:                
                enemySPEED = 15 * elapsed
            
            if (enemy.daSpawn == "right"):
                enemy.x -= enemySPEED
            elif (enemy.daSpawn == "left"):
                enemy.x += enemySPEED
            elif (enemy.daSpawn == "down"):
                enemy.y -= enemySPEED
            elif(enemy.daSpawn == "up"):
                enemy.y += enemySPEED

            daScreen.blit(enemy.daImage, (enemy.x, enemy.y))
            
            # wtf is that
            if (enemy.x < -200 and enemy.daSpawn == "right" or enemy.x > WIDTH and enemy.daSpawn == "left" or enemy.y > HEIGHT and enemy.daSpawn == "up" or enemy.y < -200 and enemy.daSpawn == "down"):
                enemys.remove(enemy)


    if (len(bullets) > 0):
        for daBullet in bullets:
            daBullet.x += 100 * elapsed
            daScreen.blit(daBullet.daImage, (daBullet.x, daBullet.y))
            if (daBullet.x > WIDTH):
                bullets.remove(daBullet)

    #check if player hit enemy
    if (len(enemys)):
        for enemy in enemys:
            if (enemy.daType == "colossal"):
                if (CoolUtils.overlaping(daPlayer, enemy)):
                    enemy.remove(enemy)
                    running = False
            else:
                if (CoolUtils.overlaping(enemy, daPlayer)):
                    enemys.remove(enemy)
                    running = False

    #check if bullet hit enemy
    if (len((bullets, enemys)) > 0):
        for daBullet in bullets:
            for enemy in enemys:
                if (CoolUtils.overlaping(daBullet, enemy)):
                    print("overlaped")
                    bullets.remove(daBullet)
                    enemys.remove(enemy)
                    if (enemy.daType == "colossal"):
                        score += 50
                    elif (enemy.daType == "minimoys"):
                        score += 100
                    else:
                        score += 10

    clock.tick(FPS)
    pygame.display.flip()