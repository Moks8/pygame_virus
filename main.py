import pygame as pg
from pygame.locals import *
import sys
from sprites import *
from config import *
from scenes import *




class Game:
    game_over = False
    score = 0
    current_scene = 0
    scene = None
    exit_game = False
    must_restart_game = False

    def __init__(self):
        pg.display.set_caption("Covid")
        self.pantalla = pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        self.hero = Hero()
        
        self.sprites = pg.sprite.Group()
        self.sprites.add(self.hero)

        #self.explosion = Explotions()
   
        self.clock = pg.time.Clock()
        self.fps = FPS

        self.font = pg.font.Font("./resources/fonts/font.ttf", 40)
        self.marcador = self.font.render("0",True,WHITE)
        self.txt_level = self.font.render("Level 0", True, WHITE)

        self.game_over_image = pg.image.load("./resources/game_over.png")

        self.boom = pg.mixer.Sound("./resources/sounds/sfx-explosion-14.wav")
        pg.mixer.music.load("./resources/sounds/resources_8-bit-Coffin-Dance-_from-Astronomia_-_1_.wav")
        pg.mixer.music.play(-1)

        self.start_game()
        
    
    def kill (self,group):
        lista_candidatos = pg.sprite.spritecollide(self.hero,self.scene.virus,True)  
        
        if len(lista_candidatos)>0:
            self.game_over= True
            '''
            self.explosion.rect = self.hero.rect
            self.sprites.add(self.explosion)
            self.explosion.update()
            pg.mixer.music.stop()
            self.boom.play()

            print("tas muerto")
            '''

    
        
    def on_loop (self):
        if self.game_over:
            pass
        else:
            self.score += self.scene.on_loop()
        if self.scene.has_hero:
            self.scene.repaint_rect(self.hero.rect)
            self.hero.move()
            self.kill(self.sprites)
        self.marcador = self.font.render(str(self.score), True, WHITE)
            
        if self.current_scene == len(self.scenes) -1:
            self.txt_level = self.font.render("THE END", True, WHITE)
        else:
            self.txt_level = self.font.render("Level "+ (str(self.current_scene)), True, WHITE)

    def on_render(self):
        if self.game_over:
            self.pantalla.blit(self.game_over_image,
                                (SCREEN_WIDTH // 2 - self.game_over_image.get_rect().width // 2,
                                 SCREEN_HEIGHT // 2 - self.game_over_image.get_rect().height / 2))
        else:
            self.scene.on_render(self.pantalla)

            if self.current_scene != 0:
                self.sprites.draw(self.pantalla)
                self.pantalla.fill(BACKGROUND,MARCADOR_RECT)
                self.pantalla.blit(self.marcador,MARCADOR_POS)
                self.pantalla.blit(self.txt_level, LEVEL_POS)

        pg.display.flip()
    
    def on_event(self,event):
        if self.game_over:
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    self.game_over = False
                    self.must_restart_game = True
        else:
            if self.scene.has_hero:
                self.hero.on_event(event)
            self.scene.on_event(event)

    def start_game(self):
        self.current_scene = 0
        self.scenes = []
        self.scenes = [Intro(),
                       Level1(),
                       Level2(),
                       Level3(),
                       Level4(),
                       Final()]
        self.scene = self.scenes[self.current_scene]
        self.score = 0

    def restart_game(self):
        # lo que sea
        self.must_restart_game = False
        self.start_game()


    def main_loop(self):
        if pg.init() == False:
            self.exit_game = True

        while not self.exit_game:
            for event in pg.event.get():
                if event.type == QUIT:
                    self.quit()

                self.on_event(event)

            

            # Wait until user press space
            if self.must_restart_game:
                self.restart_game()
                continue


            self.on_loop()
            self.on_render()
            ms = self.clock.tick(self.fps)
            self.scene.set_ms(ms)

            #Check if scene is finish

            if self.scene.finished():
                self.current_scene += 1
                if self.current_scene >= len(self.scenes):
                    self.restart_game()
                else:
                    self.scene = self.scenes[self.current_scene]
                
    def quit (self):
        pg.quit()
        sys.exit()


if __name__ == "__main__":
    pg.init()
    game = Game()
    game.main_loop()
    game.quit()
