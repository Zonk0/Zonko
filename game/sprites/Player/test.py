import pygame as pg
import os
from os import path
pg.init()
pg.display.set_mode ((500, 500))

x=250
y=250
v=10
move_l=False
move_r=False
animation=0


idle=pg.image.load(os.path.join('sprites','Player','down','d1.png'))

walk_L=[pg.image.load(os.path.join('sprites','Player','left','l1.png')),
        pg.image.load(os.path.join('sprites','Player','left','l2.png')),
        pg.image.load(os.path.join('sprites','Player','left','l3.png')),
        pg.image.load(os.path.join('sprites','Player','left','l4.png')),
        pg.image.load(os.path.join('sprites','Player','left','l5.png')),
        pg.image.load(os.path.join('sprites','Player','left','l6.png')),
        pg.image.load(os.path.join('sprites','Player','left','l7.png')),
        pg.image.load(os.path.join('sprites','Player','left','l8.png')),
        pg.image.load(os.path.join('sprites','Player','left','l9.png'))]


walk_R=[pg.image.load(os.path.join('sprites','Player','right','r1.png')),
        pg.image.load(os.path.join('sprites','Player','right','r2.png')),
        pg.image.load(os.path.join('sprites','Player','right','r3.png')),
        pg.image.load(os.path.join('sprites','Player','right','r4.png')),
        pg.image.load(os.path.join('sprites','Player','right','r5.png')),
        pg.image.load(os.path.join('sprites','Player','right','r6.png')),
        pg.image.load(os.path.join('sprites','Player','right','r7.png')),
        pg.image.load(os.path.join('sprites','Player','right','r8.png')),
        pg.image.load(os.path.join('sprites','Player','right','r9.png'))]

def draw_game():
    global animation
    if animation>=9:
        animation=0
    if move_l:
        win.blit(walk_L[animation],(x,y))
        animation+=1
    elif move_r:
        win.blit(walk_R[animation],(x,y))
        animation+=1
    else:
        win.blit(idle,(x,y))

run=True
while run:
    for event in pg.event_get():

        ui=pg.key.get_pressed()
    if ui [pg.K_LEFT]:
        x-=v
        move_l=True
        move_r=False
    if ui [pg.K_RIGHT]:
        x=v
        move_l=False
        move_r=True
    else:
        move_l=False
        move_r=False
        animation=0



pg.time_delay(30)
pg.display.update()