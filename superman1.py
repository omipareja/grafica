import random,pygame,sys

ancho=626
alto=365
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

class VidasD(pygame.sprite.Sprite):
    al=10
    def __init__(self,an = 100):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([an, self.al])
        self.image.fill(Rojo)
        self.rect=self.image.get_rect()
        self.var_x=0
        self.dir=0
        self.rest = 0


    def update(self):
        pass

'''class  lacers(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.accion=0
        #self.m=m
        #self.image = m[self.accion][0]
        self.rect=self.image.get_rect()
        self.rect.x=-100
        self.rect.y=100
        self.i=0
        self.vel_y=0
        self.vel_x=0


    def update(self):
        pass'''


class Jugador(pygame.sprite.Sprite):
    def __init__(self,m):
        pygame.sprite.Sprite.__init__(self)
        self.accion=5
        self.m=m
        self.image = m[self.accion][0]
        self.rect=self.image.get_rect()
        self.rect.x=4
        self.rect.y=330
        self.i=4
        self.vel_x=0
        self.vel_y=0
        self.vidas=3

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        if self.accion == 2:
            self.i+=1
            if self.i >= len(self.m[self.accion]):
                self.i=0
                self.accion=0

        if self.accion == 7:
            self.i+=1
            if self.i >= len(self.m[self.accion]):
                self.i=0
                self.accion=6

        if self.accion == 8:
            self.i+=1
            if self.i >= len(self.m[self.accion]):
                self.i=0
                self.accion=6



        if self.accion ==1:
            self.i+=1
            if self.i >= len(self.m[self.accion]):
                self.i=0
                self.accion=0


        if self.accion == 0:
            self.i+=1
            if self.i >= len(self.m[self.accion]):
                self.i=0
                self.accion=0


        if self.accion == 6:
            self.i+=1
            if self.i >= len(self.m[self.accion]):
                self.i=0
                self.accion=6

        if self.accion == 4:
            self.i+=1
            if self.i >= len(self.m[self.accion]):
                self.i=0
                self.accion=0

        if self.accion == 3:
            self.i+=1
            if self.i >= len(self.m[self.accion]):
                self.i=0
                self.accion=0

        if self.accion == 9:
            self.i+=1
            if self.i >= len(self.m[self.accion]):
                self.i=0
                self.accion=6



        self.image = self.m[self.accion][self.i]

class ventanas(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.alto=400
        self.ancho=400
        self.vent=pygame.display.set_mode([self.ancho,self.alto])


    def ventana_gameover(self):
        fin=False
        while not fin:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    fin=True
                    sys.exit()

            pygame.display.flip()





class Enemigo1(pygame.sprite.Sprite):
    def __init__(self,m):
        pygame.sprite.Sprite.__init__(self)
        self.accion=0
        self.m=m
        self.image = m[self.accion][0]
        self.rect=self.image.get_rect()
        self.rect.x=800
        self.rect.y=180
        self.i=0
        self.vel_x=-10
        self.vel_y=0
        self.cont=0

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        self.accion=1
        self.image = self.m[self.accion][self.cont]
        self.cont+=1
        if self.cont >6:
            self.cont=0

class bomba(pygame.sprite.Sprite):
    def __init__(self,m):
        pygame.sprite.Sprite.__init__(self)
        self.accion=2
        self.m=m
        self.image = m[self.accion][0]
        self.rect=self.image.get_rect()
        self.rect.x=random.randrange(623)
        self.rect.y=0
        self.i=0
        self.vel_y=8


    def update(self):
        self.rect.y += self.vel_y
        if self.rect.y >= (alto - self.rect.height):
            self.rect.y=alto - self.rect.height
            self.vel_y=self.vel_y

class Vida(pygame.sprite.Sprite):
    def __init__(self,m):
        pygame.sprite.Sprite.__init__(self)
        self.accion=0
        self.m=m
        self.image = m[self.accion][0]
        self.rect=self.image.get_rect()
        self.rect.x=random.randrange(623)
        self.rect.y=0
        self.i=0
        self.vel_y=4
        self.cont= 50


    def update(self):
        self.rect.y += self.vel_y
        if self.rect.y >= (alto - self.rect.height):
            self.rect.y=alto - self.rect.height
            self.vel_y=self.vel_y



if __name__=='__main__':
    #Definicion de variables
    pygame.init()
    pantalla=pygame.display.set_mode([ancho, alto])
    fondo=pygame.image.load('ciudad.jpg')





    b=0
    a=0

    '''lacer=lacers()
    l=pygame.sprite.Group()
    l.add(lacer)'''
    ######enemigos###################
    limitesEnemigo=[7,7]
    E =Recortar(2,7,'robot.png',limitesEnemigo)
    ##########################################
    limites=[5,6,6,7,7,7,4,6,5,7,5,7]
    m=Recortar(12,7,'super.png',limites)

    limitemodificador=[1,1,1]
    bom=Recortar(3,1,'modificadores.png',limitemodificador)

    jp=VidasD()
    VidasS=pygame.sprite.Group()
    VidasS.add(jp)

    enemigos=pygame.sprite.Group()
    jugadores=pygame.sprite.Group()
    bombas=pygame.sprite.Group()
    modificadores = pygame.sprite.Group()

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


    vv=j.vidas
    fuente = pygame.font.Font(None,50)
    texto = fuente.render('Ronda 1',False,Negro)
    reloj=pygame.time.Clock()
    accion=0
    i=0
    w = 100
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
                    j.vel_y = 5
                    j.vel_x = -12
                    j.i=0
                    j.accion=6
                    b=1
                    a=0

                if event.key == pygame.K_RIGHT:
                    j.vel_y = 5
                    j.vel_x = 12
                    j.accion=0
                    j.i=0
                    a=1
                    b=0

                if event.key == pygame.K_a:
                    if a==1:
                        j.accion = 2
                        j.i=0
                        #a=0


                    if b==1:
                        j.accion = 8
                        j.i=0
                        #b=0



                if event.key == pygame.K_s:
                    if a==1:
                        j.accion = 1
                        j.i=0
                        #a=0


                    if b==1:
                        j.accion = 7
                        j.i=0
                        #b=0


                if event.key == pygame.K_UP:
                    j.vel_x =0
                    j.vel_y= -15

                if event.key == pygame.K_DOWN:
                    j.vel_x =0
                    j.vel_y =15

                if event.key == pygame.K_SPACE:
                    if b == 1:
                        j.accion=  3
                        j.i=0

                    if a == 1:
                        j.accion =  9
                        j.i=0

            if event.type == pygame.KEYUP:
                j.vel_y=5
                j.vel_x=0
                #j.accion=0
                #j.i=0

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

        #bombas
        si_explo= random.randrange(600)
        if si_explo >590:
            b=bomba(bom)
            bombas.add(b)

        #modificador vida
        si_vid =random.randrange(1000)
        if si_vid < 5:
            v= Vida(bom)
            modificadores.add(v)



        #para la colion con las bom
        for j in jugadores:
            ls_bo=pygame.sprite.spritecollide(j,bombas,True)
            for b in ls_bo:
                j.vidas-=1
                j.accion = 4
                j.i = 1
                w = w-33
                if w >= 0:
                    for h in VidasS:
                        VidasS.remove(h)
                    jp = VidasD(w)
                    VidasS.add(jp)
                if j.vidas ==0:
                    for h in VidasS:
                        VidasS.remove(h)
                    jugadores.remove(j)
                    pygame.quit()
                    v=ventanas()
                    v.ventana_gameover()

        #colision con el enemigo
        for j in jugadores:
            ls_ene=pygame.sprite.spritecollide(j,enemigos,True)
            for r in ls_ene:
                j.vidas -= 1
                j.accion = 4
                j.i = 1
                w = w-33
                for h in VidasS:
                    VidasS.remove(h)
                jp = VidasD(w)
                VidasS.add(jp)
                if j.vidas ==0:
                    for h in VidasS:
                        VidasS.remove(h)
                    jugadores.remove(j)
                    pygame.quit()
                    v=ventanas()
                    v.ventana_gameover()

        #remover bombas cuando tocan el suelo
        for b in bombas:
            if b.rect.y == (alto - b.rect.height):
                bombas.remove(b)

        #recoleta las VIDAS
        for j in jugadores:
            ls_vida=pygame.sprite.spritecollide(j,modificadores,True)
            for v in ls_vida:
                j.vidas += 1
                w = w+33
                if w <= 100:
                    for h in VidasS:
                        VidasS.remove(h)
                    jp = VidasD(w)
                    VidasS.add(jp)
                jugadores.remove(v)






        #Refresco de eventos
        #update
        jugadores.update()
        enemigos.update()
        bombas.update()
        modificadores.update()
        VidasS.update()

        pantalla.blit(fondo,[1,1])
        jugadores.draw(pantalla)
        enemigos.draw(pantalla)
        bombas.draw(pantalla)
        VidasS.draw(pantalla)
        modificadores.draw(pantalla)
        pantalla.blit(texto,[250,10])
        pygame.display.flip()
        reloj.tick(10)
