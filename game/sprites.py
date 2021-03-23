import pygame as pg
import math
from settings import *


vec=pg.math.Vector2


class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.Player_Img
        game.player_img
        self.walking=False
        self.dashing=False
        #self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.vel=vec(0,0)
        self.pos=vec(x,y)*TILESIZE   
        self.rot=0            


    def keys_press (self):
        self.vel=vec(0,0)
        keys=pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.vel.x=-Player_Speed
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.vel.x=Player_Speed
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.vel.y=-Player_Speed
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.vel.y=Player_Speed
        if self.vel.x!=0 and self.vel.y!=0:
            self.vel*=0.7071


    def rotate(self):

        #mX, mY = pg.mouse.get_pos()
        #AnRad = math.atan2(self.rect.y-mY, mX-self.rect.x)
        #AnDeg = -math.degrees(AnRad)
        #self.image = pg.transform.rotate(self.unrotated_image, AnDeg)

        ###############################################################

        mouse_dir = vec(pg.mouse.get_pos()) - vec(self.camera.apply(self.player.pos).center)
        self.rot = mouse_dir.angle_to(vec(1, 0))
        
        ##############################################################
        #m_x, m_y = pg.mouse.get_pos()
        #rel_x, rel_y = m_x - self.x, m_y - self.y
        #angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
        #self.image = pg.transform.rotate(self.unrotimg, int(angle))
        #self.rect = self.image.get_rect(center=self.pos)

    
    def collide_with_walls(self, dir):
        if dir=='x':
            hits=pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vel.x>0:
                    self.pos.x=hits[0].rect.left-self.rect.width
                if self.vel.x<0:
                    self.pos.x=hits[0].rect.right
                self.vel.x=0
                self.rect.x=self.pos.x
        if dir=='y':
            hits=pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vel.y>0:
                    self.pos.y=hits[0].rect.top-self.rect.height
                if self.vel.y<0:
                    self.pos.y=hits[0].rect.bottom
                self.vel.y=0
                self.rect.y=self.pos.y

    def update(self):
        self.keys_press()
        self.pos+=self.vel*self.game.dt
        self.rect.x=self.pos.x
        self.collide_with_walls('x')
        self.rect.y=self.pos.y
        self.collide_with_walls('y')
        self.rot(self.rot + self.rot_speed + self.game.dt) %360
        self.image = pg.transform.rotate(self.game.Player_Img, self.rot)
        self.rect.center = self.pos
        #self.screen.blit(self.image, (self.rect.x, self.rect.y))

        if pg.sprite.spritecollideany(self, self.game.walls):
            self.x-= self.vx*self.game.dt
            self.y-= self.vy*self.game.dt
            self.rect.topleft=(self.x,self.y)


class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
