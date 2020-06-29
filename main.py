import pygame as pg
from pygame.locals import *
import sys
from sprites import *


BACKGROUND = (50,50,50)

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
        

        self.level = Level()

        

        
        self.clock = pg.time.Clock()
        self.fps = 30

       

        
        
        
        pg.display.set_caption("Covid")

    def on_loop (self):
        self.level.repaint_rect(self.hero.rect)
        self.hero.update()
        self.hero.rect.centery += self.hero_move

        self.level.update_virus()

        if pg.sprite.spritecollideany(self.hero, self.level.virus):
            print("tas muerto")
    def on_render(self):
        self.level.draw(self.pantalla)
        self.sprites.draw(self.pantalla)
        
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
