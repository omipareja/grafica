import random
import pygame
ancho=800
alto=600
Verde=[0,255,0]
Negro=[0,0,0]
Rojo=[250,0,0]
Blanco=[255,255,255]
Azul=[0,0,255]

def Recortar (nf, nc, archivo, limites):
    imagen = pygame.image.load(archivo)
    info = imagen.get_rect()
    an_img = info[2]
    al_img = info[3]
    an_corte=int(an_img/nc)
    al_corte=int(al_img/nf)
    m=[]
    for y in range(nf):
        fila=[]
        for x in range(limites[y]):
            cuadro=imagen.subsurface(x*an_corte,y*al_corte, an_corte, al_corte)
            fila.append(cuadro)
        m.append(fila)

    return m


class Jugador(pygame.sprite.Sprite):
    def __init__(self,m):
        pygame.sprite.Sprite.__init__(self)
        self.accion=0
        self.fila=0
        self.m=m
        self.image = m[self.accion][self.fila]
        self.rect=self.image.get_rect()
        self.rect.x=4
        self.rect.y=330
        self.i=0
        self.vel_x=0
        self.vel_y=0

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        if self.accion == 2:
            self.i+=1
            if self.i >= len(self.m[self.accion]):
                self.i=0
                self.accion=1

        if self.accion == 3:
            self.i+=1
            if self.i >= len(self.m[self.accion]):
                self.i=0
                self.accion=1


        if self.accion == 5:
            self.i+=1
            if self.i >= len(self.m[self.accion]):
                self.i=0
                self.accion=1

            if self.accion == 0:
                self.i+=1
                if self.i >= len(self.m[self.accion]):
                    self.i=0
                    self.accion=1



        self.image = self.m[self.accion][self.i]




if __name__=='__main__':
    #Definicion de variables
    pygame.init()
    pantalla=pygame.display.set_mode([ancho, alto])
    limites=[7,6,6,7,7,7,4,6,5,8,5,7]
    m=Recortar(12,8,'super.png',limites)
    pos_aux=0
    x=0
    y=5

    jugadores=pygame.sprite.Group()
    todos=pygame.sprite.Group()


    j=Jugador(m)
    jugadores.add(j)
    todos.add(j)



    reloj=pygame.time.Clock()
    accion=0
    i=0
    fin=False
    fondo= pygame.image.load('fondo.png')
    while not fin:


        #limitador pantalla
        if j.rect.x > (ancho-j.rect.width):
            j.rect.x=ancho-j.rect.width
            j.vel_x=0

        if j.rect.x <= (0):
            j.rect.x=0
            j.vel_x=0

        if j.rect.y > (alto-j.rect.height):
            j.rect.y=alto-j.rect.height
            j.vel_y=0
        if j.rect.y == 0:
            j.rect.y=0
            j.vel_y=0
        if j.rect.x == 0:
            j.rect.x=0
            j.vel_x=0


        #Gestion de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    j.vel_y = 0
                    j.vel_x = -8
                    j.accion = 0
                    j.i=0
                if event.key == pygame.K_RIGHT:
                    j.vel_y = 0
                    j.vel_x = 8
                    j.accion =0
                    j.i=0
                if event.key == pygame.K_a:
                    j.accion = 2
                    j.i=0
                if event.key == pygame.K_s:
                    j.accion = 3
                    j.i=0
                if event.key == pygame.K_d:
                    j.accion = 5
                    j.i=0
                    j.vel_y = 0
                    j.vel_x = 8


                if event.key == pygame.K_f:
                    j.accion = 9
                    j.fila = 0
            if event.type == pygame.KEYUP:
                j.vel_y=0
                j.vel_x=0




        #Refresco de eventos
        pantalla.fill(Negro)
        pantalla.blit(fondo,(0,0))
        todos.update()
        todos.draw(pantalla)
        pygame.display.flip()
        reloj.tick(10)
