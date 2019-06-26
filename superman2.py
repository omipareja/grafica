import random,pygame,sys

ls_muros = pygame.sprite.Group()

ancho=640
alto=384
Verde=[0,255,0]
Negro=[0,0,0]
Rojo=[250,0,0]
Blanco=[255,255,255]
Azul=[0,0,255]


def CrearNivel1():
    x = 0
    y = 0
    img = pygame.image.load("Suelo.png")
    suelo = []
    mat = []
    t=0
    with open('Suelo.json') as file:
        Datos = json.load(file)

        for mapa in Datos['layers']:
            suelo = mapa['data']

        for f in range(12):
            l = []
            for c in range(60):
                l.append(suelo[t])
                t+=1
            mat.append(l)

    for f in 12:
        for c in 60:
            if  mat[f][c] != 0:
                m = Muro(x,y, img)
                #ls_todos.add(m)
                ls_muros.add(m)
            x += 32
        y += 32
        x = 0




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
    def __init__(self,an =100):
        pygame.sprite.Sprite.__init__(self)
        if an > 0:
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
        self.rect.x=313
        self.rect.y=330
        self.i=4
        self.vel_x=0
        self.vel_y=0
        self.vidas=300000000000
        self.golpe=pygame.mixer.Sound('golpe.mp3')
        self.cont=0
        self.disparo = 1
        self.score= 0


    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        self.cont=self.cont

        if self.cont ==30:
            self.cont=0
            self.vel_x=0


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

        col_muro = pygame.sprite.spritecollide(self, ls_muros, False)
        for muro in col_muro:
            self.vel_y = 0

            print  col_muro


class Muro(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass

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
        self.rect.y=170
        self.i=0
        self.vel_x=-20
        self.vel_y=0
        self.cont=0

    def update(self):
        self.rect.x += self.vel_x
        #self.rect.y += self.vel_y
        if self.accion == 0:
            self.i+=1
            if self.i >= len(self.m[self.accion]):
                self.i=0
                self.accion=0
        if self.accion == 1:
            self.i+=1
            if self.i >= len(self.m[self.accion]):
                self.i=0
                self.accion=1
#enemigo cielo
class Enemigo2(pygame.sprite.Sprite):
    def __init__(self,m):
        pygame.sprite.Sprite.__init__(self)
        self.accion=0
        self.m=m
        self.image = m[0][0]
        self.rect=self.image.get_rect()
        self.rect.x=800
        self.rect.y=640
        self.i=0
        self.vel_x=-30
        self.vel_y=0
        self.cont=0

    def update(self):
        self.rect.x += self.vel_x



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
        self.bomba=pygame.mixer.Sound('explosion.wav')


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
        self.vel_x=0
        self.vida=pygame.mixer.Sound('vida.wav')



    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        if self.rect.y >= (alto - self.rect.height):
            self.rect.y=alto - self.rect.height
            self.vel_y=0

class Disparo(pygame.sprite.Sprite):
    def __init__(self,m):
        pygame.sprite.Sprite.__init__(self)
        self.accion=0
        self.m=m
        self.image = m[1][0]
        self.rect=self.image.get_rect()
        self.rect.x=random.randrange(623)
        self.rect.y=0
        self.i=0
        self.vel_y=4
        self.vel_x=0






    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        if self.rect.y >= (alto - self.rect.height):
            self.rect.y=alto - self.rect.height
            self.vel_y=0



class laser(pygame.sprite.Sprite):
    """docstring for ."""
    def __init__(self, m):
        pygame.sprite.Sprite.__init__(self)
        self.matriz=m
        self.image=self.matriz[0][0]
        self.rect=self.image.get_rect()
        self.i=0
        self.vel_x=20
        self.laser= pygame.mixer.Sound('laser.wav')



    def update(self):
        self.rect.x += self.vel_x




if __name__=='__main__':
    #Definicion de variables
    pygame.init()
    pantalla=pygame.display.set_mode([ancho, alto])
    fondo=pygame.image.load('ciudad.jpg')
    CrearNivel1


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

    limitelaser=[1,1]
    las=Recortar(1,1,'laser.png',limitelaser)

   ###################limite enemigo 2##################
    limiteenemigo2 =[1]
    ene2=Recortar(1,2,'androide.png',limiteenemigo2)

    jp=VidasD()
    VidasS=pygame.sprite.Group()
    VidasS.add(jp)


    laserD=pygame.sprite.Group()
    enemigos=pygame.sprite.Group()
    jugadores=pygame.sprite.Group()
    bombas=pygame.sprite.Group()
    modificadores = pygame.sprite.Group()
    modificadordis= pygame.sprite.Group()
    enemigos2=pygame.sprite.Group()

    #ene=Enemigo1(E)
    j=Jugador(m)
    jugadores.add(j)

    #todos.add(ene)

        #creacion de rivales
    A=1
    for i in range(A):


        r=Enemigo1(E)
        r.accion=1
        r.i=0
        r20=Enemigo1(E)
        #r.rect.x=1*random.randint(600,800)#Sale de atras de la pantalla
        r20.rect.x=0

        r20.accion=1
        r20.i=0
        r.rect.x=620
        enemigos.add(r,r20)


    z=10
    for i in range(z):
        r2=Enemigo2(ene2)
        r2.rect.x=1*random.randrange(700)#Sale de atras de la pantalla
        r2.rect.y=random.randrange(150)
        enemigos2.add(r2)


    vv=j.vidas
    fuente = pygame.font.Font(None,50)
    texto = fuente.render('Ronda 1',False,Negro)

    reloj=pygame.time.Clock()
    accion=0
    i=0
    w = 100
    fin=False
    pygame.mixer.music.load('sword.mp3')
    pygame.mixer.music.play()
    while not fin:
        #musica fondo

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
                    print "Izquierda: ", b

                if event.key == pygame.K_RIGHT:
                    j.vel_y = 5
                    j.vel_x = 12
                    j.accion=0
                    j.i=0
                    a=1

                    print "Derecha: ", a

                if event.key == pygame.K_a:
                    print b, " ", a
                    if a==1:
                        j.accion = 2
                        j.i=0
                        #a=0
                    if b==1:
                        print "if b == 1"
                        j.accion = 8
                        j.i=0
                        #b=0



                if event.key == pygame.K_s:

                    if a==1:
                        j.accion = 1
                        j.i=0
                        #a=0


                    if b==1:
                        print ("dfsdfsfsfsfsdf")
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
                    if j.disparo>1:
                        if b == 1:

                            j.accion=  9
                            j.i=0
                            j.disparo-=1

                        if a == 1:


                            j.accion =  3
                            j.i=0
                            j.disparo-=1

            if event.type == pygame.KEYUP:
                j.vel_y=5
                j.vel_x=0
                j.accion=0
                j.i=0


#control
        #control enemigostierra
        for r in enemigos:   #Para que el cambio que haga se aplique en todo el grupo
            if r.rect.x > (ancho-r.rect.width):
                r.rect.x=ancho-r.rect.width
                r.vel_x=-1*r.vel_x
            if r.rect.x < 0:
                r.rect.x=0
                r.vel_x=-1*r.vel_x

        #control enemigo cielo
        for r2 in enemigos2:   #Para que el cambio que haga se aplique en todo el grupo
            if r2.rect.x > (ancho-r2.rect.width):
                r2.rect.x=ancho-r2.rect.width
                r2.vel_x=-1*r2.vel_x
            if r2.rect.x < 0:
                r2.rect.x=0
                r2.vel_x=-1*r2.vel_x

        #colisiones enemigo tierra
        for j in jugadores:
            ls_col=pygame.sprite.spritecollide(j,enemigos,False)
            if j.accion ==2 or j.accion == 5:
                for v in ls_col:
                    enemigos.remove(v)
                    j.golpe.play()
                    j.score+=10
                #pygame.mixer.music.load('golpe.mp3')
                #pygame.mixer.music.play()

        #laser Disparo
        if j.accion ==9:
            l=laser(las)
            laserD.add(l)
            l.laser.play()
            l.rect.x=j.rect.x+5
            l.rect.y=j.rect.y-25
            l.vel_x=l.vel_x*-1

        if j.accion ==3:
            l=laser(las)
            laserD.add(l)
            l.laser.play()
            l.rect.x=j.rect.x+5
            l.rect.y=j.rect.y-25

        for l in laserD:
            laser_col=pygame.sprite.spritecollide(l,enemigos,False)
            for r in laser_col:
                enemigos.remove(r)
                j.score +=10

        for l in laserD:
            laser_col2=pygame.sprite.spritecollide(l,enemigos2,True)
            for r2 in laser_col2:
                enemigos2.remove(r2)
                j.score +=10

        # col ecemigo cielo
        for j in jugadores:
            ls_col2=pygame.sprite.spritecollide(j,enemigos2,False)
            if j.accion ==2 or j.accion == 5:
                j.golpe.play()
                for v in ls_col2:
                    enemigos2.remove(v)
                    j.score+=10


        '''
        #colison con el laserD
        ls_las=pygame.sprite.spritecollide(l,enemigos,False)
        for l in ls_las:
            enemigos.remove(v)
        '''


        #bombas
        si_explo= random.randrange(600)
        if si_explo <40:
            b=bomba(bom)
            bombas.add(b)

        #modificador vida
        si_vid =random.randrange(1000)
        if si_vid < 5:
            v= Vida(bom)
            modificadores.add(v)


        si_disparo =random.randrange(1000)
        if si_disparo < 2:
            dis= Disparo(bom)
            modificadordis.add(dis)
        '''
        for j in jugadores:
            ls_vel=pygame.sprite.spritecollide(j,modificadores,True)
            for vel in ls_vel:
                j.cont=1
                if j.cont != 30:
                    j.vel_x=20
        '''



        #para la colion con las bom
        for j in jugadores:
            ls_bo=pygame.sprite.spritecollide(j,bombas,True)
            for b in ls_bo:
                j.vidas-=1
                j.accion = 4
                j.i = 1
                b.bomba.play()
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
            ls_ene=pygame.sprite.spritecollide(j,enemigos,False)
            for r in ls_ene:
                j.vidas -= 1
                j.accion = 4
                j.i = 1
                w = w-33
                for h in VidasS:
                    VidasS.remove(h)
                if w > 0:
                    jp = VidasD(w)
                    VidasS.add(jp)
                if j.vidas ==0:
                    for h in VidasS:
                        VidasS.remove(h)
                    jugadores.remove(j)
                    pygame.quit()
                    v=ventanas()
                    v.ventana_gameover()


        for j in jugadores:
            ls_ene2=pygame.sprite.spritecollide(j,enemigos2,False)
            for r2 in ls_ene2:
                j.vidas -= 1
                j.accion = 4
                j.i = 1
                w = w-33
                for h in VidasS:
                    VidasS.remove(h)
                if w > 0:
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
                v.vida.play()
                w = w+33
                if w <= 100:
                    for h in VidasS:
                        VidasS.remove(h)
                        jp = VidasD(w)
                    VidasS.add(jp)
                jugadores.remove(v)




        for j in jugadores:
            ls_dis= pygame.sprite.spritecollide(j,modificadordis,True)
            for dis in ls_dis:
                j.disparo+=1



        #Refresco de eventos
        #update

        modificadordis.update()
        enemigos2.update()
        laserD.update()
        jugadores.update()
        enemigos.update()
        bombas.update()
        modificadores.update()
        VidasS.update()
        ls_muros.update()

        pantalla.blit(fondo,[1,1])



        laserD.draw(pantalla)
        modificadordis.draw(pantalla)
        jugadores.draw(pantalla)
        enemigos.draw(pantalla)
        bombas.draw(pantalla)
        VidasS.draw(pantalla)
        enemigos2.draw(pantalla)
        modificadores.draw(pantalla)
        ls_muros.draw(pantalla)
        pantalla.blit(texto,[250,10])
        puntaje= fuente.render(str(j.score),False,Negro)
        pantalla.blit(puntaje,[600,10])
        pygame.display.flip()
        reloj.tick(10)
