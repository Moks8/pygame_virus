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
        self.image_act=0
        
        self.rect.topleft = (32,32)
        self.hero_move = 0
        self.dirty = 1

        
    def loadImages(self):
        images = []
        for i in range (self.num_sprites):
            image = pg.image.load("./resources/hero{}.png".format(i))
            images.append(image)
        return images



    def move (self,pos):
        if (self.rect.centery + pos) >= self.rect.height and (self.rect.centery + pos) <= (VENA_HEIGHT - self.rect.height):
            self.rect.centery += pos
        
        self.image_act += 1
        if self.image_act >= self.num_sprites:
            self.image_act = 0
        self.image = self.images[self.image_act] 





class Virus(pg.sprite.DirtySprite):
    def __init__ (self):
        pg.sprite.DirtySprite.__init__(self)
        self.image = pg.image.load("./resources/virus.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (720-64,random.randint(32,250))
        self.dirty = 1

class Explotions (pg.sprite.Sprite):
    num_sprites = 9
    def __init__ (self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((64,64))
        self.rect = self.image.get_rect()
        self.images = self.loadImages()
        self.image_act=0

        
    def loadImages(self):
        images = []
        for i in range (self.num_sprites):
            image = pg.image.load("./resources/explosions/regularExplosion0{}.png".format(i)).convert()
            image.set_colorkey(WHITE) #RLEACCEL
            images.append(image)
        return images


    def update(self):
        self.image_act += 1
        if self.image_act >= self.num_sprites:
            self.image_act = 0
        
        self.image = self.images[self.image_act]

    def kill (self,group):
        lista_candidatos = pg.sprite.spritecollide(self.hero,self.level.virus,True)  
        if len(lista_candidatos)>0:
            self.explosion.rect = self.hero.rect
            self.sprites.add(self.explosion)
            self.explosion.update()
            self.boom.play()

            print("tas muerto") 



class Tile(pg.sprite.DirtySprite):
    def __init__(self, image):
        pg.sprite.DirtySprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.dirty = 1


if __name__ == "__main__":
    game = Game()
