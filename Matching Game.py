import pygame, sys, random
from pygame.locals import *


def Init():
    global window, circle, cross, triangle, square, pentagon, hexagon, rhombus, purple, green, pink, blue, red, yellow, title, titleRect, font1, font2, text
    pygame.init()
    window = pygame.display.set_mode((800,600))
    pygame.display.set_caption('Matching Game')
    font1 = pygame.font.SysFont('broadway',40)
    font2 = pygame.font.SysFont('broadway',24)
    
    

    purple = (205,205,255)
    green = (205,255,205)
    pink = (255,205,205)
    blue = (125,175,255)
    red = (255,75,75)
    yellow = (255,255,125)

    text = ['Matching Game','Select Difficulty','Easy','Medium','Hard']

    title = font1.render(text[0],True, (0,0,0))
    titleRect = title.get_rect()
    titleRect.center = (400,50)

    
    
    circle = pygame.transform.scale(pygame.image.load('circle.png'),(100,100))
    cross = pygame.transform.scale(pygame.image.load('cross.png'),(100,100))
    triangle = pygame.transform.scale(pygame.image.load('triangle.png'),(100,100))
    square = pygame.transform.scale(pygame.image.load('square.png'),(100,100))
    pentagon = pygame.transform.scale(pygame.image.load('pentagon.png'),(100,100))
    hexagon = pygame.transform.scale(pygame.image.load('hexagon.png'),(100,100))
    rhombus = pygame.transform.scale(pygame.image.load('rhombus.png'),(100,100))


    Start()

    
    

    
def Start():
    window.fill(blue)
    pygame.draw.rect(window, purple, (100,100, 600, 400))
    pygame.draw.rect(window, green, (125,175, 150, 300))
    pygame.draw.rect(window, yellow, (325,175, 150, 300))
    pygame.draw.rect(window, red, (525,175, 150, 300))

    diff = font2.render(text[1],True, (0,0,0))
    diffRect = title.get_rect()
    diffRect.center = (475,150)

    window.blit(title,titleRect)
    window.blit(diff,diffRect)

    
    


class Tile(object):
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color


Init()

while True:
    window.blit(circle,(200,100))
    window.blit(cross,(200,200))
    window.blit(triangle,(200,300))
    window.blit(square,(200,400))
    window.blit(pentagon,(200,500))
    window.blit(hexagon,(200,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONUP:
            pass
    pygame.display.update()
