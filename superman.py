import random
import pygame
ancho=623
alto=563
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
        self.accion=1
        self.m=m
        self.image = m[self.accion][0]
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

        if self.accion == 7:
            self.i+=1
            if self.i >= len(self.m[self.accion]):
                self.i=0
                self.accion=1

        if self.accion == 0:
            self.i+=1
            if self.i >= len(self.m[self.accion]):
                self.i=0
                self.accion=0



        self.image = self.m[self.accion][self.i]

class Enemigo1(pygame.sprite.Sprite):
    def __init__(self,m):
        pygame.sprite.Sprite.__init__(self)
        self.accion=0
        self.m=m
        self.image = m[self.accion][0]
        self.rect=self.image.get_rect()
        self.rect.x=800
        self.rect.y=330
        self.i=0
        self.vel_x=-10
        self.vel_y=0

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y



if __name__=='__main__':
    #Definicion de variables
    pygame.init()
    pantalla=pygame.display.set_mode([ancho, alto])

    limites=[5,6,6,7,7,7,4,6,5,8,5,7]
    limites2=[4,8,6,4,7,3,6,7,5]

    E = Recortar(9,8,'hulk.png',limites2)

    m=Recortar(12,7,'super.png',limites)



    enemigos=pygame.sprite.Group()
    jugadores=pygame.sprite.Group()
    todos=pygame.sprite.Group()

    #ene=Enemigo1(E)
    j=Jugador(m)
    jugadores.add(j)

    #todos.add(ene)

        #creacion de rivales
    A=1
    for i in range(A):
        r=Enemigo1(E)
        r.rect.x=1*random.randrange(800)#Sale de atras de la pantalla
        enemigos.add(r)





    reloj=pygame.time.Clock()
    accion=0
    i=0
    fin=False
    while not fin:

        #limitador pantalla
        if j.rect.x > (ancho-j.rect.width):
            j.rect.x=ancho-j.rect.width
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

                if event.key == pygame.K_RIGHT:
                    j.vel_y = 0
                    j.vel_x = 8
                    j.accion =0
                    j.i=1
                if event.key == pygame.K_a:
                    j.accion = 2
                    j.i=0
                if event.key == pygame.K_s:
                    j.accion = 3
                    j.i=0
                if event.key == pygame.K_d:
                    j.accion = 5
                    j.i=0
                if event.key == pygame.K_f:
                    j.accion =7
                    j.i=0
            if event.type == pygame.KEYUP:
                j.vel_y=0
                j.vel_x=0

        for r in enemigos:   #Para que el cambio que haga se aplique en todo el grupo
            if r.rect.x > (ancho-r.rect.width):
                r.rect.x=ancho-r.rect.width
                r.vel_x=-1*r.vel_x
            if r.rect.x < 0:
                r.rect.x=0
                r.vel_x=-1*r.vel_x


        #colisiones
        ls_col=pygame.sprite.spritecollide(j,enemigos,False)
        if j.accion ==2 or j.accion ==3 or j.accion == 5:
            for v in ls_col:
                enemigos.remove(v)
                pygame.mixer.music.load('golpe.mp3')
                pygame.mixer.music.play()


        #Refresco de eventos
        #update
        jugadores.update()
        enemigos.update()


        pantalla.fill(Negro)
        jugadores.draw(pantalla)
        enemigos.draw(pantalla)
        pygame.display.flip()
        reloj.tick(10)
