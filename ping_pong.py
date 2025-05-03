from time import *
import pygame as pg
from random import *
pg.init()

pg.mixer.init()

class BaseSprite(pg.sprite.Sprite):
    def __init__(self, filename, x, y, w, h, speed_x=0, speed_y=0):
        super().__init__()
        self.rect = pg.Rect(x, y, w, h)
        self.rect.x = x
        self.rect.y = y
        self.image = pg.transform.scale(pg.image.load(filename), (w, h))
        self.speed_x = speed_x
        self.speed_y = speed_y

    def draw(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

class Player(BaseSprite):
    def update(self):
        if self.rect.x>200:    
            keys = pg.key.get_pressed()     
            if keys[pg.K_UP] and self.rect.y >= 5:
                self.rect.y -= self.speed_y 

            if keys[pg.K_DOWN] and self.rect.y <= win_size[1] - self.rect.height:            
                self.rect.y += self.speed_y
        elif self.rect.x<200:
            keys = pg.key.get_pressed()     
            if keys[pg.K_w] and self.rect.y >= 5:
                self.rect.y -= self.speed_y 

            if keys[pg.K_s] and self.rect.y <= win_size[1] - self.rect.height:            
                self.rect.y += self.speed_y

class Ball(BaseSprite):
    def moving(self):
        self.rect.x += self.speed_x
        if self.rect.y >= 550:
            self.rect.y += self.speed_y*-1
            self.rect.x -= self.speed_x
        elif self.rect.y <= 0:
            self.rect.y -= self.speed_y*-1
            self.rect.x += self.speed_x

win_size = (800, 600)
x, y = 0, 1

mw = pg.display.set_mode(win_size)
# mw = pg.display.set_mode(win_size, pg.FULLSCREEN)
pg.display.set_caption("Ping Pong")
clock = pg.time.Clock()

fon = pg.transform.scale(
                            pg.image.load("pingpong_fon.jpg"), win_size
                            )
#fon_go = pg.transform.scale(
#                            pg.image.load(""), win_size
#                            )
#fon_win = pg.transform.scale(pg.image.load("win.png"), win_size)

player_1 = Player('raketka.png', 5, 5, 100, 100, 0, 5)
player_2 = Player('raketka.png', 695, 495, 100, 100, 0, 5)
ball = Ball('ball.png', 375, 275, 50, 50, 6, 6)

play = True
win = False
game = True
ticks = 1
formula = 0

while play:
    for e in pg.event.get():
        if e.type == pg.QUIT or \
                    (e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE):
                play  = False

    if game:
        mw.blit(fon, (0, 0))
        player_1.update()
        player_1.draw()
        player_2.update()
        player_2.draw()
        ball.moving()
        if pg.sprite.spritecollide(ball, player_1, False):
                ball.rect.x += ball.speed_x*-1
                ball.rect.y -= ball.speed_y
        if pg.sprite.spritecollide(ball, player_2, False):
                ball.rect.x -= ball.speed_x*-1
                ball.rect.y -= ball.speed_y
        ball.update()
        ball.draw()

    else:
        mw.blit(fon_go, (0, 0))


    pg.display.update()
    clock.tick(60)
    ticks += 1
