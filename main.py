import pygame as pg
from pygame.locals import *
import sys
from sprites import *


BACKGROUND = (50,50,50)
WHITE = (255,255,255)
class Game:
    def __init__(self):
        self.game_over = True

        self.pantalla = pg.display.set_mode((720,400))
        self.pantalla.fill (BACKGROUND)
        self.pantalla.blit(self.pantalla,(0,0))

        self.hero = Hero()
        self.hero_move = 0
        
        self.sprites = pg.sprite.Group()
        self.sprites.add(self.hero)

        self.explosion = Explotions()
        
        
        self.level = Level()

        
        self.clock = pg.time.Clock()
        self.fps = 30

        self.font = pg.font.Font("./resources/fonts/font.ttf",40)
        self.marcador = self.font.render("0",True,WHITE)

        self.score = 0

        self.boom = pg.mixer.Sound("./resources/sounds/sfx-explosion-14.wav")

        
        
        
        pg.display.set_caption("Covid")

    def kill (self,group):
        lista_candidatos = pg.sprite.spritecollide(self.hero,self.level.virus,True)  
        if len(lista_candidatos)>0:
            self.explosion.rect = self.hero.rect
            self.sprites.add(self.explosion)
            self.explosion.update()
            self.boom.play()

            print("tas muerto")
        
    def on_loop (self):
        self.level.repaint_rect(self.hero.rect)
        self.hero.update()
        self.hero.rect.centery += self.hero_move

        self.level.update_virus()
        self.kill(self.sprites)
        
        self.marcador = self.font.render(str(self.score),True,WHITE)
        

    def on_render(self):
        self.level.draw(self.pantalla)
        self.sprites.draw(self.pantalla)
        
        

        self.pantalla.blit(self.marcador,(25,345))
        pg.display.flip()
    
    def handlenEvent(self):
       pass

    

    def main_loop(self):
        if pg.init() == False:
            self.game_over = False

        while (self.game_over):
            for event in pg.event.get():
                if event.type == QUIT:
                    self.quit()

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
            self.level.set_ms(ms)

                
                


       
            
            

            
            
            

            

    
    def quit (self):
        pg.quit()
        sys.exit()


if __name__ == "__main__":
    pg.init()
    game = Game()
    game.main_loop()
    game.quit()
