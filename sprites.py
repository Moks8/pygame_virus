import pygame as pg
from pygame.locals import *
import sys,random

class Hero(pg.sprite.DirtySprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("./resources/hero.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (32,32)
        self.hero_move = 0
        self.dirty = 1

class Virus(pg.sprite.DirtySprite):
    def __init__ (self):
        super().__init__(self)
        self.image = pg.image.load("./resources/virus.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (720-64,random.choice([32,250]))
        self.dirty = 1



class Tile(pg.sprite.DirtySprite):
    def __init__(self, image):
        pg.sprite.DirtySprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.dirty = 1

class Level(pg.sprite.LayeredDirty):
    def __init__(self):
        super().__init__(self)
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
                    self.tile = Tile(self._limit_sup_image)
                elif self._data[y][x] == 2:
                    self.tile = Tile(self._limit_inf_image)
                elif self._data[y][x] == 0:
                    self.tile = Tile(self._back_image)

                self.tile.rect.topleft = (x*32 ,y*32)
                self.add(self.tile)
        self.ms_to_virus = 3 *1000 #aparicion de virus cada 3 sec
        self.ms_passed = 0
    
    def set_ms(self,ms):
        self.ms_passed += ms
        if self.ms_passed > self.ms_to_virus:
            virus = Virus()
            self.sprites.add(virus)
            self.ms_passed = 0

        
            






        