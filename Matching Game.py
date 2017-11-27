import pygame, sys, random
from pygame.locals import *


def Init():
    pygame.init()
    window = pygame.display.set_mode((800,500))
    pygame.display.set_caption('Matching Game')
    font1 pygame.font.SysFont('broadway',32)






Init()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONUP:
    pygame.display.update()
