import pygame as pg
from pygame.locals import *
import sys

class Hero(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("./resources/hero.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (32,32)
        