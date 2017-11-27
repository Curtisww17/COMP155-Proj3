import pygame, sys, random
from pygame.locals import *






while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONUP:
    pygame.display.update()
