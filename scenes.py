import pygame as pg
from pygame.locals import *
from config import *
from sprites import *

class Scene(pg.sprite.LayeredDirty):
    virus = []
    has_finished = False

    def __init__(self):
        super().__init__()
        pass

    def draw(self, surface):
        pass
    def on_event(self,event):
        pass


    def on_render(self, pantalla):
        self.draw(pantalla)

    def on_loop(self):
        """ Must return points in this loop """
        return 0

    def set_ms(self, ms):
        pass

    def finished(self):
        return self.has_finished



class Intro(Scene):
    jugar_pos = (300, 100)
    def __init__(self):
        super().__init__()
        font = pg.font.Font("./resources/fonts/font.ttf", 40)
        self.jugar = font.render("PRESS SPACE KEY TO START", True, WHITE)

    def draw(self,surface):
        self.surface = surface
        self.surface.fill(BACKGROUND)
        self.surface.blit(self.jugar,(SCREEN_WIDTH / 2 - self.jugar.get_rect().width / 2,
                        self.jugar.get_rect().height + 30))

    def on_event(self,event):
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                self.has_finished = True




class Level(Scene):
    def __init__(self):
        super().__init__()
        self._data = None
        self._back_image = None
        self._limit_sup_image = None
        self._limit_inf_image = None

    def load_data(self, data, back_image, top_image, down_image, ms_to_virus, virus_vel, limit_virus):
        self._data = data
        self._back_image = pg.image.load(back_image)
        self._limit_sup_image = pg.image.load(top_image)
        self._limit_inf_image = pg.image.load(down_image)
        self._limit_virus = limit_virus
 
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

        self.ms_to_virus = ms_to_virus*1000 #aparición de virus cada X sec
        self.ms_passed = 0

        self.virus = pg.sprite.Group()
        self.virus.velocity = virus_vel
        self.add(self.virus)

    
    def set_ms(self,ms):
        self.ms_passed += ms
        if self.ms_passed > self.ms_to_virus:
            virus = Virus()
            self.virus.add(virus)
            self.ms_passed = 0


    def on_loop(self):
        dead_viruses = 0
        for virus in self.virus:
            self.repaint_rect(virus.rect)
            if virus.rect.x < (virus.rect.width * -1):
                dead_viruses += 1
                self.virus.remove(virus)
            else:
                virus.rect = virus.rect.move(-self.virus.velocity, 0)

        self._limit_virus -= dead_viruses
        if self._limit_virus < 0:
            self.has_finished = True


        return dead_viruses


    def draw(self, surface):
        pg.sprite.LayeredDirty.draw(self, surface)
        self.virus.draw(surface)




class Level1(Level):
    def __init__(self):
        super().__init__()
        data = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
                [0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]]

        self.load_data(data,
                       "./resources/arteria_fondo.png",
                       "./resources/arteria_borde_sup.png",
                       "./resources/arteria_borde_inf.png",
                       1,
                       10,
                       5)

                            #ms_to_virus, virus_vel, limit_virus

class Level2(Level):
    def __init__(self):
        super().__init__()
        data = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]]

        self.load_data(data,
                       "./resources/arteria_fondo.png",
                       "./resources/arteria_borde_sup.png",
                       "./resources/arteria_borde_inf.png",
                       0.5,
                       15,
                       4)

                            #ms_to_virus, virus_vel, limit_virus

