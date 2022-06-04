import random
import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        self.daImage = pygame.image.load("enemy.png")
        self.rect = self.daImage.get_rect()
        self.x = self.rect.x
        self.y = self.rect.y
        self.types = ["normal", "colossal", "minimoys"]
        self.daType = self.types[random.randint(0, len(self.types) - 1)]
        self.health = 1
        self.spawn = ['left', 'right', 'down', 'up']
        self.daSpawn = self.spawn[random.randint(0,3)]