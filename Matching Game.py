import pygame, sys, random
from pygame.locals import *


def Init():
    pygame.init()
    window = pygame.display.set_mode((800,500))
    pygame.display.set_caption('Matching Game')
    font1 = pygame.font.SysFont('broadway',32)
    window.fill((255,255,255))







Init()

while True:
    window.blit(pygame.load('square.png'),200,200)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONUP:
            pass
    pygame.display.update()
