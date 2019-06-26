#! /usr/bin/env python
import json, pygame


ls_todos = pygame.sprite.Group()
ls_muros = pygame.sprite.Group()



def CrearNivel1(nivel):
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
                ls_todos.add(m)
                ls_muros.add(m)
            x += 32
        y += 32
        x = 0

'''
def LimpiarNivel(jugador):
    ls_muros.empty()
    ls_todos.empty()
    ls_enemigos.empty()
    ls_pildoras.empty()
    ls_estrellas.empty()
    ls_balas.empty()
    ls_explosiones.empty()
    ls_todos.add(jugador)
    jugador.rect.x = 30
    jugador.rect.y = 240
    jugador.movex = 0
    jugador.movey = 0
'''

class Muro(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass

class jugador(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        pass

    def update(self):
        col_muro = pygame.sprite.spritecollide(self, ls_muros, False)
        for muro in col_muro:
            self.vel_y = 0
