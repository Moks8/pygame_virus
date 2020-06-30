import pygame as pg
from pygame.locals import *
import sys,random
WHITE = (255,255,255)

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

    def update(self):
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

        self.virus = pg.sprite.Group()
        self.virus.velocity = 10
        self.add(self.virus)

    
    def set_ms(self,ms):
        self.ms_passed += ms
        if self.ms_passed > self.ms_to_virus:
            virus = Virus()
            self.virus.add(virus)
            self.ms_passed = 0

    def update_virus(self):
        for virus in self.virus:
            self.repaint_rect(virus.rect)
            if virus.rect.x < (virus.rect.width * -1):
                self.virus.remove(virus)
            else:
                virus.rect = virus.rect.move(-self.virus.velocity, 0)


    def draw(self, surface):
        pg.sprite.LayeredDirty.draw(self, surface)
        self.virus.draw(surface)

if __name__ == "__main__":
    game = Game()

        
            






        