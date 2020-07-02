import pygame as pg
from pygame.locals import *
from config import *
from sprites import *


class Scene(pg.sprite.LayeredDirty):
    virus = []
    has_finished = False
    has_hero = False 
    

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
    show_story= False
    jugar_pos = (300, 100)
    def __init__(self):
        super().__init__()
        font = pg.font.Font("./resources/fonts/font.ttf", 40)
        subfont = pg.font.Font("./resources/fonts/font.ttf", 20)
        self.jugar = font.render("PRESS SPACE KEY TO START", True, WHITE)
        self.knowhow= subfont.render("If you want to know how to play press a",True,WHITE)
        # Story
        self.story = subfont.render("Help the red blood cell to reach the lung",True, WHITE)
        self.story2 = subfont.render("and give it some oxygen to fight the virus." , True, WHITE) 
        self.story3 = subfont.render("Be careful on the way,there are virus that can", True, WHITE)
        self.story4 = subfont.render("infect your oxygen, try to avoid them!", True, WHITE)
        self.space = subfont.render("Press SPACE to start", True, WHITE)
        
        self.textRect = self.story.get_rect()
        self.textRect2 = self.story2.get_rect()
        self.textRect3 = self.story3.get_rect()
        self.textRect4 = self.story4.get_rect()
        self.textRect5 = self.space.get_rect()
        
        self.textRect.center = (SCREEN_WIDTH//2,50)
        self.textRect2.center = (SCREEN_WIDTH//2,75)
        self.textRect3.center = (SCREEN_WIDTH//2,100)
        self.textRect4.center = (SCREEN_WIDTH//2,125)
        self.textRect5.center = (SCREEN_WIDTH//2,350)

        self.cell = pg.image.load("./resources/hero0.png")
        self.cellrect = self.cell.get_rect()
        self.cellrect.center = (180,250)

        self.keyboard = pg.image.load("./resources/keyboard.png")
        self.keyboardrect = self.keyboard.get_rect()
        self.keyboardrect.center = (540,250)
        

    def draw(self,surface):
        self.surface = surface
        if self.show_story == True:
            self.surface.fill(BACKGROUND)
            self.surface.blit(self.story,self.textRect)
            self.surface.blit(self.story2,self.textRect2)
            self.surface.blit(self.story3,self.textRect3)
            self.surface.blit(self.story4,self.textRect4)
            self.surface.blit(self.cell,self.cellrect)
            self.surface.blit(self.keyboard,self.keyboardrect)
            self.surface.blit(self.space,self.textRect5)
        else:
            self.surface = surface
            self.surface.fill(BACKGROUND)
            self.surface.blit(self.jugar,(SCREEN_WIDTH / 2 - self.jugar.get_rect().width / 2,
                            self.jugar.get_rect().height + 30))
            self.surface.blit(self.knowhow,(SCREEN_WIDTH / 2 - self.knowhow.get_rect().width / 2,
                            self.knowhow.get_rect().height + 100))
        

    def on_event(self,event):
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                self.has_finished = True

            if event.key == K_a:
                self.show_story = True

            





class Level(Scene):
    def __init__(self):
        super().__init__()
        self.has_hero = True
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
        if self._limit_virus > 0:
            self.virus.velocity = virus_vel
            self.add(self.virus)

    
    def set_ms(self,ms):
        self.ms_passed += ms
        if self._limit_virus > 0 :
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
                       12,
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

class Level3(Level):
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
                       "./resources/vena_fondo.png",
                       "./resources/vena_borde_sup.png",
                       "./resources/vena_borde_inf.png",
                       1,
                       15,
                       5)


class Level4(Level):
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
                       "./resources/vena_fondo.png",
                       "./resources/vena_borde_sup.png",
                       "./resources/vena_borde_inf.png",
                       0.5,
                       15,
                       4)

class Final(Level):
    def __init__(self):
        super().__init__()
        self.lung = Lung()
        self.lungsprite = pg.sprite.Group()
        self.lungsprite.add(self.lung)
        

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
                       "./resources/vena_fondo.png",
                       "./resources/vena_borde_sup.png",
                       "./resources/vena_borde_inf.png",
                       0,
                       0,
                       0)

    def draw(self, surface):
        pg.sprite.LayeredDirty.draw(self, surface)
        self.lungsprite.draw(surface)

        

    def on_loop(self):
        self.repaint_rect(self.lung.rect)
    

        if self.lung.rect.x > SCREEN_WIDTH//2 - self.lung.rect.width // 2:
            self.lung.move(3)
    
        return 0
                       
                
            
   
            
