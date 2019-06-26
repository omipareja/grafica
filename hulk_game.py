#! /usr/env python
import sys, pygame
from pygame.locals import *
pygame.init()


ANCHOPANTALLA=600
ALTOPANTALLA=400
NEGRO = [0,0,0]
BLANCO = [255,255,255]
ROJO = [255,0,0]
VERDE = [0,255,0]
AZUL = [0,0,255]
AMARILLO = [255,255,0]
NARANJA = [255,127,0]
MORADO= [143,0,255]
RED = [245,173,148]
BLUE = [158,231,245]
GREEN = [180,249,165]
YELLOW = [255,241,166]





#clase jugador
class Game(pygame.sprite.Sprite):
    def __init__(self,img,pos_ini):
        pygame.sprite.Sprite.__init__(self)
        self.imgs = img
        self.image = self.imgs[0][0]
        self.imgrect=self.image.get_rect()
        self.imgrect.x=pos_ini[0]
        self.imgrect.y=pos_ini[1]
        self.velx=0
        self.vely=0

    def update(self):
        self.rect.x+=self.velx
        self.rect.y+=self.vely

#clase principal
class principal(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.pantalla=pygame.display.set_mode([ANCHOPANTALLA,ALTOPANTALLA])
        self.img= pygame.image.load('hulk_hombre.png')
        self.matriz=self.Recorte(self.img,26,40,11,10)

    def Recorte(self,img,corteX,corteY,cantidadX,cantidadY):
        m=[]
        for y in range(cantidadY):
            l=[]
            for x in range(cantidadX):
                l.append(img.subsurface((x*corteX),(y*corteY),corteX,corteY))
            m.append(l)
        return m



    def start(self):
        jugador = Game(self.matriz,[20,30])
        jugadores=pygame.sprite.Group()
        jugadores.add(jugador)
        while True:
            for event in pygame.event.get():
                if event.type == (pygame.QUIT):
                    pygame.quit()
                    sys.exit()
            #self.pantalla.blit(self.matriz[0][0],[30,30])
            #jugadores.draw(self.pantalla)
            pygame.display.flip()



if __name__ == '__main__':
    inicio=principal()
    inicio.start()
