import pygame as pg
from pygame.locals import *
import sys
from sprites import *
from config import *
from scenes import *



class Game:
    def __init__(self):
        self.game_over = True

        self.pantalla = pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

        self.current_scene = 0
        self.scenes = [Intro(),Level1(),Level2()]
        self.scene = self.scenes[self.current_scene]

        self.hero = Hero()
        self.hero_move = 0
        
        self.sprites = pg.sprite.Group()
        self.sprites.add(self.hero)

        self.explosion = Explotions()
   
        self.clock = pg.time.Clock()
        self.fps = FPS

        self.font = pg.font.Font("./resources/fonts/font.ttf", 40)
        self.marcador = self.font.render("0",True,WHITE)
        self.txt_level = self.font.render("Level 0", True, WHITE)

        self.score = 0

        self.boom = pg.mixer.Sound("./resources/sounds/sfx-explosion-14.wav")
        pg.mixer.music.load("./resources/sounds/resources_8-bit-Coffin-Dance-_from-Astronomia_-_1_.wav")
        pg.mixer.music.play(-1)
        
        
        

        pg.display.set_caption("Covid")

    def kill (self,group):
        lista_candidatos = pg.sprite.spritecollide(self.hero,self.scene.virus,True)  
        if len(lista_candidatos)>0:
            self.explosion.rect = self.hero.rect
            self.sprites.add(self.explosion)
            self.explosion.update()
            pg.mixer.music.stop()
            self.boom.play()

            print("tas muerto")
        
    def on_loop (self):
        self.score += self.scene.on_loop()
        if self.current_scene != 0:
            self.scene.repaint_rect(self.hero.rect)
            self.hero.move(self.hero_move)
            self.marcador = self.font.render(str(self.score), True, WHITE)
            self.txt_level = self.font.render("Level 0", True, WHITE)
            self.kill(self.sprites)

    def on_render(self):
        self.scene.on_render(self.pantalla)

        if self.current_scene != 0:
            self.sprites.draw(self.pantalla)
            self.pantalla.fill(BACKGROUND,MARCADOR_RECT)
            self.pantalla.blit(self.marcador,MARCADOR_POS)
            self.pantalla.blit(self.txt_level, LEVEL_POS)

        pg.display.flip()
    
    def on_event(self,event):
       self.scene.on_event(event)

    

    def main_loop(self):
        if pg.init() == False:
            self.game_over = False

        while (self.game_over):
            
            for event in pg.event.get():
                if event.type == QUIT:
                    self.quit()

                self.on_event(event)

                if self.current_scene in range (0,100):
                    if event.type == KEYDOWN:
                        if event.key == K_DOWN:
                            self.hero_move +=10
                        if event.key == K_UP:
                            self.hero_move -= 10
                if event.type == KEYUP:
                    self.hero_move = 0

        
            self.on_loop()
            self.on_render()
            ms = self.clock.tick(self.fps)
            self.scene.set_ms(ms)

            #Check if scene is finish
            if self.scene.finished():
                self.current_scene += 1
                self.scene = self.scenes[self.current_scene]


    def quit (self):
        pg.quit()
        sys.exit()


if __name__ == "__main__":
    pg.init()
    game = Game()
    game.main_loop()
    game.quit()
