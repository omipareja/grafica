import pygame
from Repo import *
import random
'''
pasos para adicionar objtos
1 crear la Clase
2 crear el grupo
3crear el objeto e instanciar la clase
4 dibujarlo
'''




class Jugador(pygame.sprite.Sprite):
    '''
    Clase Jugador
    '''
    def __init__(self,matriz_inicial, pos_ini):
    #def __init__(self,id,p,cl=rep.BLANCO):

        pygame.sprite.Sprite.__init__(self)
        #self.id=id
        self.dir=0
        self.concol=0
        self.matriz=matriz_inicial
        self.image=self.matriz[0][0]
        self.rect=self.image.get_rect()
        self.rect.x=pos_ini[0]
        self.rect.y=pos_ini[1]
        self.velx=0
        self.vely=0


    def update(self):    #le permite al pobjeto actualizar su estado
        self.rect.x+=self.velx
        self.rect.y+=self.vely
        self.image = self.matriz[self.dir][self.concol]
        #self.concol+=1
        if self.concol>2:
            self.concol=0





if __name__ == '__main__':
    pygame.init()
    reloj=pygame.time.Clock()
    pantalla=pygame.display.set_mode([ANCHOPANTALLA,ALTOPANTALLA])
    hulk_hombre= pygame.image.load('super.png')
    m=Recorte(hulk_hombre,98,104,8,12)
    jugadores=pygame.sprite.Group()


    j1=Jugador(m,[100,150])
    jugadores.add(j1)
    #ugadores.add(j2)


    #Codigo

    reloj=pygame.time.Clock()

    pygame.display.flip()
    fin = False
    while not (fin):
        #reloj.tick(5)
        for event in pygame.event.get():
            if event.type == (pygame.QUIT):
                fin = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    j1.dir=2
                    j1.velx=5
                    j1.vely=0
                if event.key == pygame.K_LEFT:
                    j1.dir=1
                    j1.velx=-5
                    j1.vely=0
                if event.key == pygame.K_DOWN:
                    j1.concol=4
                    j1.dir=0
                    j1.vely=5
                    j1.velx=0

                if event.key == pygame.K_UP:
                    j1.concol=2
                    j1.dir=3
                    j1.vely=-5
                    j1.velx=0

                if event.key == pygame.K_SPACE:

                    j1.velx=0
                    j1.vely=0


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    j1.dir=0
                    j1.concol=2
                    j1.velx=0
                    j1.vely=0
                if event.key == pygame.K_LEFT:
                    j1.dir=2
                    j1.velx=-0
                    j1.vely=0
                if event.key == pygame.K_DOWN:
                    j1.concol=4
                    j1.dir=0
                    j1.vely=0
                    j1.velx=0

                if event.key == pygame.K_UP:
                    j1.concol=2
                    j1.dir=0
                    j1.vely=-0
                    j1.velx=0


        jugadores.update()

        #Refresco de pantalla
        pantalla.fill(NEGRO)

        jugadores.draw(pantalla)

        pygame.display.flip()
        reloj.tick(30)
