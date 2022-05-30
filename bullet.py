import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        self.daImage = pygame.image.load("daBullet.png")
        self.rect = self.daImage.get_rect()
        self.x = self.rect.x
        self.y = self.rect.y