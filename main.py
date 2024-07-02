import pygame
import sys, datetime
from clases import *
from consts import *
from funciones import *

pygame.init()

screen = pygame.display.set_mode((SCREEN_RES))

reproducir_musica_ambiente()

main_menu(screen)