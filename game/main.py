import pygame as pg
import sys
import os
import math
from os import path
from pygame.locals import *
from settings import *
from sprites import * 
from tilemap import *
from camera import *
class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT,))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(250, 100)
        self.load_data()


    def load_data(self):
        game_folder = path.dirname(__file__)
        img_folder=path.join(game_folder,'sprites','Player')
        self.player_img=pg.image.load(path.join(img_folder,Player_Img)).convert_alpha()
        self.map=Map(path.join(game_folder,'map3.txt'))
        

    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self, col, row)
                if tile == 'P':
                    self.player = Player(self, col, row)
        self.camera= camera(self.map.width, self.map.height)
        

    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()


    def quit(self):
        pg.quit()
        sys.exit()


    def update(self):
        # update portion of the game loop
        self.all_sprites.update()
        self.camera.update(self.player)
        self.screen.blit(self.image, (self.rect.x, self.rect.y))
        

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))


    def draw(self):
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        #self.all_sprites.draw(self.screen)
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        pg.display.flip()


    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                   pg.quit()
                   return


    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

# create the game object
g = Game()
g.show_start_screen()
while True:
    g.new()
    g.run()
    g.show_go_screen()