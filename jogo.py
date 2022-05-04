

import pygame as pg
from pygame.locals import *
from sys import exit
from random import randint

pg.init()
largura = 1000
altura = 750
tela = pg.display.set_mode((largura, altura))
fundo = pg.image.load("fundo.jpg")
relogio = pg.time.Clock()
z = (largura/2) - 10
w = (altura/2) - 10
vidabolsonaro = 10
fonte = pg.font.SysFont('arial', 40, False, False)

class Cracha(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pg.image.load("cracha.png"))
        self.image = self.sprites[0]
        self.rect = self.image.get_rect()
        self.rect.y = randint(50, 700)
        self.rect.x = randint(50, 950)
        self.image = pg.transform.scale(self.image, (64*0.5, 64*0.5))

class Gota(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pg.image.load("gotinha-1.png.png"))
        self.sprites.append(pg.image.load("gotinha-2.png.png"))
        self.sprites.append(pg.image.load("gotinha-3.png.png"))
        self.sprites.append(pg.image.load("gotinha-4.png.png"))
        self.sprites.append(pg.image.load("gotinha-5.png.png"))
        self.sprites.append(pg.image.load("gotinha-6.png.png"))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.rect = self.image.get_rect()
        self.rect.y = w
        self.rect.x = z
        self.image = pg.transform.scale(self.image, (64 * 2, 64 * 2))

    def update(self):
        self.atual += 1
        if self.atual >= 6:
            self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pg.transform.scale(self.image, (64 * 2, 64 * 2))
        self.rect.y = w
        self.rect.x = z


class Reidograd(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pg.image.load("reidograd-1.png.png"))
        self.sprites.append(pg.image.load("reidograd-2.png.png"))
        self.sprites.append(pg.image.load("reidograd-3.png.png"))
        self.sprites.append(pg.image.load("reidograd-4.png.png"))
        self.sprites.append(pg.image.load("reidograd-5.png.png"))
        self.sprites.append(pg.image.load("reidograd-6.png.png"))
        self.sprites.append(pg.image.load("reidograd-7.png.png"))
        self.sprites.append(pg.image.load("reidograd-8.png.png"))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pg.transform.scale(self.image, (64*1.5, 64*1.5))

        self.rect = self.image.get_rect()
        self.rect.center = 500, 350

    def update(self):
        self.atual += 1
        if self.atual >= 8:
            self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pg.transform.scale(self.image, (64 * 1.5, 64 * 1.5))
        if self.rect.topright[0] <= largura+30:
            self.rect.x += 5
        else:
            self.rect.x = 0
            self.rect.y = randint(50,700)


cracha = Cracha()
rei = Reidograd()
gota = Gota()
sprites = pg.sprite.Group()
sprites.add(rei)
sprites.add(cracha)
sprites.add(gota)

while True:
    relogio.tick(30)
    mensagem = f'Pontos: {vidabolsonaro}'
    texto = fonte.render(mensagem, True, (0,0,0))
    tela.blit(fundo, (0, 0))
    sprites.draw(tela)
    sprites.update()
    tela.blit(texto, (700,100))

    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            exit()

    if pg.key.get_pressed()[K_a]:
        z = z - 10
    if pg.key.get_pressed()[K_d]:
        z = z + 10
    if pg.key.get_pressed()[K_w]:
        w = w - 10
    if pg.key.get_pressed()[K_s]:
        w = w + 10

    pg.display.flip()
