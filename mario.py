#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Módulos
import sys, pygame
from pygame.locals import *

# Constantes
WIDTH = 640
HEIGHT = 480
#Clases
#-------------------------------------------------------------
class Mario(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("imagenes/yoshi.png", True)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT / 2
        self.speed = [0.4, -0.4]
    def actualizar(self, time):
        keys = pygame.key.get_pressed()
        if keys[K_DOWN]:
               self.rect.y += 6
        if self.rect.y>=480:
               self.rect.y -= 6
        if keys[K_UP]:
               self.rect.y -= 6
        if self.rect.y <=0:
               self.rect.y += 6
        if keys[K_RIGHT]:
               self.rect.x += 6
        if self.rect.x>=640:
               self.rect.x -= 6
        if keys[K_LEFT]:
            self.rect.x -= 6
        if self.rect.x<=0:
            self.rect.x += 6
     
class Enemigo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("imagenes/enemigo.png", True)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT / 2
        self.speed = [0.3, -0.3]
 
    def actualizar(self, time):
        self.rect.centerx += self.speed[0] * time
        self.rect.centery += self.speed[1] * time
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.speed[0] = -self.speed[0]
            self.rect.centerx += self.speed[0] * time
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.speed[1] = -self.speed[1]
            self.rect.centery += self.speed[1] * time

class Casper(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("imagenes/casper1.png", True)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT / 2
        self.speed = [0.5, -0.5]

    def actualizar(self, time):
        self.rect.centerx += self.speed[0] * time
        self.rect.centery += self.speed[1] * time
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.speed[0] = -self.speed[0]
            self.rect.centerx += self.speed[0] * time
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.speed[1] = -self.speed[1]
            self.rect.centery += self.speed[1] * time

#Funciones
#--------------------------------------------------------------
def load_image(filename, transparent=False):
        try: image = pygame.image.load(filename)
        except pygame.error, message:
                raise SystemExit, message
        image = image.convert()
        if transparent:
                color = image.get_at((0,0))
                image.set_colorkey(color, RLEACCEL)
        return image

#---------------------------------------------------------------
def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Juego Carlos Gil")
    background_image = load_image('imagenes/mario3.jpg')
    seta = load_image("imagenes/seta1.png", True)
    mario = Mario()
    enemigo = Enemigo()
    casper = Casper()
    clock = pygame.time.Clock()
    while True:
	time = clock.tick(60)
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)


	oldx = enemigo.rect.left
	oldy = enemigo.rect.left
        mario.actualizar(time)
	enemigo.actualizar(time)
	casper.actualizar(time)
	#imagen.actualizar(time)
	screen.blit(background_image, (0, 0))
	screen.blit(seta, (585,330))
        screen.blit(mario.image, mario.rect)
	screen.blit(enemigo.image, enemigo.rect)
	screen.blit(casper.image, casper.rect)
	pygame.display.flip()
    return 0

if __name__ == '__main__':
    pygame.init()
    main()

