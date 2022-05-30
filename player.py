import pygame
pygame.init()

class Player(pygame.sprite.Sprite): 
    def __init__(self):
        self.daImage = pygame.image.load('daCube.png')
        self.rect = self.daImage.get_rect()
        self.x = self.rect.x
        self.y = self.rect.y
