import pygame as pg
from pygame.locals import *
import sys

class Hero(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("./resources/hero.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (32,32)
        self.hero_move = 0


class Tile(pg.sprite.DirtySprite):
    def __init__(self, image):
        pg.sprite.DirtySprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.dirty = 1

class Level(pg.sprite.LayeredDirty):
    def __init__(self):
        pg.sprite.LayeredDirty.__init__(self)
        self._data = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                      [0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                      [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]]
        self._back_image = pg.image.load("./resources/arteria_fondo.png")
        self._limit_sup_image = pg.image.load("./resources/arteria_borde_sup.png")
        self._limit_inf_image = pg.image.load("./resources/arteria_borde_inf.png")

        for y in range(len(self._data)):
            for x in range(len(self._data[y])):
                if self._data[y][x] == 1:
                    tile = Tile(self._limit_sup_image)
                elif self._data[y][x] == 2:
                    tile = Tile(self._limit_inf_image)
                elif self._data[y][x] == 0:
                    tile = Tile(self._back_image)

                tile.rect.topleft = (x*32 ,y*32)
                self.add(tile)

        self.ms_passed = 0

    def set_ms(self,ms):
        self.ms_passed += ms






        