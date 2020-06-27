import pygame as pg
from pygame.locals import *
import sys

BACKGROUND = (50,50,50)

class Game:
    def __init__(self):
        self.pantalla = pg.display.set_mode((720,400))
        self.pantalla.fill (BACKGROUND)
        self.pantalla.blit(self.pantalla,(0,0))
        

        


        pg.display.set_caption("Covid")

    def main_loop(self):
        game_over = False

        while not game_over:
            for event in pg.event.get():
                if event.type == QUIT:
                    game_over = True

            pg.display.flip()
    
    def quit (self):
        pg.quit()
        sys.exit()

        






if __name__ == "__main__":
    pg.init()
    game = Game()
    game.main_loop()
    game.quit()
