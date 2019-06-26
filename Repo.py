import pygame
import math

#VARIABLES GLOBALES
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


def Recorte(imageSprite,corteX,corteY,cantidadX,cantidadY):
	matriz=[]
	for y in range(cantidadY):
		matriz.append([])
		for x in range(cantidadX):
			cuadro=imageSprite.subsurface((x*corteX),(y*corteY),corteX,corteY)
			matriz[y].append(cuadro)
	return matriz


#Dibujar un vector
def Vector(pantalla,Color,PosInicial,PosFinal):
    pygame.draw.line(pantalla,Color,PosInicial,PosFinal)

#Dibujar un Circulo o Punto
def Circulo(pantalla,Color,Pos,Radio):
    pygame.draw.circle(pantalla,Color,Pos,Radio)

#Dibujar un plano cartesiano en el centro
def plano_cartesiano(pantalla,Color):
    pygame.draw.line(pantalla,Color,[ANCHOPANTALLA/2,0],[ANCHOPANTALLA/2,ALTOPANTALLA])
    pygame.draw.line(pantalla,Color,[0,ALTOPANTALLA/2],[ANCHOPANTALLA,ALTOPANTALLA/2])

#Dibujar un plano cartesiano enviandole el Centro
def plano_cartesiano_centro(pantalla,Color,Centro):
    pygame.draw.line(pantalla,Color,[0,Centro[1]],[ANCHOPANTALLA,Centro[1]])
    pygame.draw.line(pantalla,Color,[Centro[0],0],[Centro[0],ALTOPANTALLA])

#Funcion que convierte coordenadas de pantalla a cartesianas
def PantallaACartesiano(Coordenadas):
    x = Coordenadas[0] - int((AnchoPantalla/2))
    y = -Coordenadas[1] + int((AltoPantalla/2))
    return [x,y]

#Funcion que convierte Coordenadas de pantalla a cartesianas enviandole el Centro
def PantallaACartesianoCentro(Coordenadas,Centro):
    x = Coordenadas[0] - Centro[0]
    y = -Coordenadas[1] + Centro[1]
    return [x,y]

#Funcion que convierte coordenadas cartesianas a pantalla
def CartesianoApantalla(Coordenadas):
    x = Coordenadas[0] + int((AnchoPantalla/2))
    y = -Coordenadas[1] + int((AltoPantalla/2))
    return [x,y]

#Funcion que convierte coordenadas cartesianas a pantalla enviandole el centro
def CartesianoApantallaCentro(Coordenadas,Centro):
    x = Coordenadas[0] - Centro[0]
    y = -Coordenadas[1] + Centro[1]
    return [x,y]

#Rotacion Horaria
def Rotacion_Horaria(punto,angulo):
    '''
    punto -->coordenadas del punto que se quiere rotar
    angulo -->angulo en grados que se quiere rotar
    xp y yp --> coordenadas rotadas
    '''
    xp=int (punto[0]*math.cos(math.radians(angulo)) - punto[1]*math.sin(math.radians(angulo)))
    yp=int (punto[0]*math.sin(math.radians(angulo)) + punto[1]*math.cos(math.radians(angulo)))
    Punto=[xp,yp]
    return Punto

#Rotacion Anti Horaria
def Rotacion_AntiHoraria(punto, angulo):
    xp=int (punto[0]*math.cos(math.radians(angulo)) + punto[1]*math.sin(math.radians(angulo)))
    yp=int (-punto[0]*math.sin(math.radians(angulo)) + punto[1]*math.cos(math.radians(angulo)))
    Punto=[xp,yp]
    return Punto

#Conversion de Coordenadas Polares a Cartesiano
def Polares_a_Cartesiano(r, t):
    x=int(r*math.cos(math.radians(t)))
    y=int(r*math.sin(math.radians(t)))
    return x,y

#Conversion de Coordenadas Cartesianas a Polares
def Cartesiano_a_Polares(x, y):
    r=int(math.sqrt((x*x)+(y*y)))
    t=int(math.atan(y/x))
    return r,t

'''
events = [
    'pygame.QUIT',
    'pygame.ACTIVEEVENT',
    'pygame.KEYDOWN',
    'pygame.KEYUP',
    'pygame.MOUSEMOTION',
    'pygame.MOUSEBUTTONUP',
    'pygame.MOUSEBUTTONDOWN',
    'pygame.JOYAXISMOTION',
    'pygame.JOYBALLMOTION',
    'pygame.JOYHATMOTION',
    'pygame.JOYBUTTONUP',
    'pygame.JOYBUTTONDOWN',
    'pygame.VIDEORESIZE',
    'pygame.VIDEOEXPOSE',
    'pygame.USEREVENT'
]
'''

'''
import pygame
from Mirepositorio import *


if __name__ == '__main__':
    pygame.init()
    reloj=pygame.time.Clock()
    Pantalla=pygame.display.set_mode([AnchoPantalla,AltoPantalla])

    #Codigo

    pygame.display.flip()
    fin = False
    while not fin:
        #reloj.tick(5)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
'''
