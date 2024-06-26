import pygame
import sys

pygame.init()

SCREEN_RES = (1500,940)

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
LIGTH_RED = (227, 66, 51)
GREEN = (0,255,0)
LIGTH_GREEN = (215,252,212)
BLUE = (0,0,255)

#Cargar Imagenes

background = pygame.image.load("Assets\BackGround.jpg")
background = pygame.transform.scale(background, (1500,940))
background_rect = background.get_rect()

background_top_10 = pygame.image.load("Assets\BackGroundTop10.jpg")
background_top_10 = pygame.transform.scale(background_top_10, (1500,940))
background_saves_rect = background_top_10.get_rect()

fondo_pantalla_opciones = pygame.image.load("Assets\ondo_pantalla_opciones.png")
fondo_pantalla_opciones = pygame.transform.scale(fondo_pantalla_opciones, (1500,940))
fondo_pantalla_opciones_rect = fondo_pantalla_opciones.get_rect()

fondo_pantalla_preguntas =pygame.image.load("Assets\ondo_pantalla_preguntas.png")
fondo_pantalla_preguntas = pygame.transform.scale(fondo_pantalla_preguntas,(1500,940))
fondo_pantalla_preguntas_rect = fondo_pantalla_preguntas.get_rect()

difuminado = pygame.image.load("Assets\save.jpg")
difuminado = pygame.transform.scale(difuminado, (1500,940))
difuminado_rect = difuminado.get_rect()