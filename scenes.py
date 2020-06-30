import pygame as pg
from pygame.locals import *
from config import *
from sprites import *

class Scene(pg.sprite.LayeredDirty):
    def __init__(self):
        super().__init__()
        pass

    def draw(self, surface):
        pass


class Intro(Scene):
    jugar_pos = (300, 100)
    def __init__(self):
        super().__init__()
        font = pg.font.Font("./resources/fonts/font.ttf", 40)
        self.jugar = font.render("PRESS SPACE KEY TO START", True, WHITE)

    def draw(self, surface):
        surface.fill(BACKGROUND)
        self.pantalla.blit(self.jugar, jugar_pos)


class Level1(Scene):
    def __init__(self):
        super().__init__()
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

        self.ms_to_virus = 3 *1000 
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
        dead_viruses = 0
        for virus in self.virus:
            self.repaint_rect(virus.rect)
            if virus.rect.x < (virus.rect.width * -1):
                dead_viruses += 1
                self.virus.remove(virus)
            else:
                virus.rect = virus.rect.move(-self.virus.velocity, 0)

        return dead_viruses


    def draw(self, surface):
        pg.sprite.LayeredDirty.draw(self, surface)
        self.virus.draw(surface)
