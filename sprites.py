import pygame as pg
from pygame.locals import *
import sys,random
from config import *

class Hero(pg.sprite.DirtySprite):
    num_sprites = 7
    def __init__(self):
        pg.sprite.DirtySprite.__init__(self)
        self.image = pg.Surface((64,64))
        self.rect = self.image.get_rect()
        self.images = self.loadImages()
        self.imagesw = self.loadImagesW()
        self.image_act=0
        
        self.rect.topleft = (32,32)
        self.hero_move = 0
        self.dirty = 1

    def on_event(self,event):
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                self.hero_move +=10
            if event.key == K_UP:
                self.hero_move -= 10

        if event.type == KEYUP:
            self.hero_move = 0

        
    def loadImages(self):
        images = []
        for i in range (self.num_sprites):
            image = pg.image.load("./resources/hero{}.png".format(i))
            images.append(image)
        return images

    def loadImagesW(self):
        images = []
        for i in range (7):
            image = pg.image.load("./resources/winner/winner{}.png".format(i))
            images.append(image)
        return images


    def move (self):
        if (self.rect.centery + self.hero_move) >= self.rect.height and (self.rect.centery + self.hero_move) <= (VENA_HEIGHT - self.rect.height):
            self.rect.centery += self.hero_move
      
        self.image_act += 1
        if self.image_act >= self.num_sprites:
            self.image_act = 0
        self.image = self.images[self.image_act] 

    def move_final (self):
        if self.rect.centery < 190:
            self.rect.centery += 2
        elif self.rect.centery > 200:
            self.rect.centery -= 2

        if self.rect.centerx < 350:
            self.rect.centerx += 5

        self.image_act += 1
        if self.image_act >= 7:
            self.image_act = 0
        self.image = self.imagesw[self.image_act] 





class Virus(pg.sprite.DirtySprite):
    def __init__ (self):
        pg.sprite.DirtySprite.__init__(self)
        self.image = pg.image.load("./resources/virus.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (720-64,random.randint(32,250))
        self.dirty = 1


class Tile(pg.sprite.DirtySprite):
    def __init__(self, image):
        pg.sprite.DirtySprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.dirty = 1


class Lung(pg.sprite.DirtySprite):
    def __init__ (self):
        pg.sprite.DirtySprite.__init__(self)
        self.lung = pg.Surface((300,300))
        self.image = pg.image.load("./resources/lungs.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (720-64,30)
        self.dirty = 1

    def move (self,vel):
        self.rect.centerx -= vel

if __name__ == "__main__":
    game = Game()
