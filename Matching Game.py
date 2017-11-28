import pygame, sys, random
from pygame.locals import *


def Init():
    global window, circle, cross, triangle, square, pentagon, hexagon, rhombus, purple, green, pink, blue, red, yellow, difficulty, title, titleRect, font1, font2, text
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

    difficulty = 0


    Start()

    
    

    
def Start():
    global difficulty
    mousex,mousey = 0,0
    
    window.fill(blue)
    pygame.draw.rect(window, purple, (100,100, 600, 400))
    pygame.draw.rect(window, green, (125,175, 150, 300))
    pygame.draw.rect(window, yellow, (325,175, 150, 300))
    pygame.draw.rect(window, red, (525,175, 150, 300))

    diff = font2.render(text[1],True, (0,0,0))
    diffRect = diff.get_rect()
    diffRect.center = (400,125)
    
    easy = font2.render(text[2],True, (0,0,0))
    easyRect = easy.get_rect()
    easyRect.center = (200,300)
    
    med = font2.render(text[3],True, (0,0,0))
    medRect = med.get_rect()
    medRect.center = (400,300)
    
    hard = font2.render(text[4],True, (0,0,0))
    hardRect = hard.get_rect()
    hardRect.center = (600,300)
    

    window.blit(title,titleRect)
    window.blit(diff,diffRect)
    window.blit(easy,easyRect)
    window.blit(med,medRect)
    window.blit(hard,hardRect)

    pygame.display.update()
    
    while difficulty == 0:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONUP:
                mousex,mousey = event.pos
        if mousey > 175 and mousey < 475:
            if mousex > 125 and mousex < 275:
                difficulty = 3
            elif mousex > 325 and mousex < 475:
                difficulty = 5
            elif mousex > 525 and mousex < 675:
                difficulty = 7
    #print(difficulty)
    
    
class Tile(object):
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color

def MakeGrid():
    global grid
    grid = []
    minilist = []
    colorlist = [red, yellow, green, blue, purple]
    if difficulty == 3:
        shapelist = [circle, cross, triangle]
    if difficulty == 5:
        shapelist = [circle, cross, triangle, square, pentagon]
    if difficulty == 7:
        shapelist = [circle, cross, triangle, square, pentagon, hexagon, rhombus]

    for shape in shapelist:
        minilist = []
        for color in colorlist:
            newtile = Tile(shape, color)
            minilist.append(newtile)
        grid.append(minilist)

def DrawGrid():
    window.fill(pink)
    if difficulty == 3:
        offset = 250
    if difficulty == 5:
        offset = 150
    if difficulty == 7:
        offset = 50
    for x in range(0,len(grid)):
        for y in range(0,len(grid[x])):
            pygame.draw.rect(window, grid[x][y].color, (x*100+offset,y*100+100,100,100))
            window.blit(grid[x][y].shape,(x*100+offset,y*100+100))
    pygame.display.update()
            


Init()
MakeGrid()
DrawGrid()



while True:
    #window.blit(circle,(200,100))
    #window.blit(cross,(200,200))
    #window.blit(triangle,(200,300))
    #window.blit(square,(200,400))
    #window.blit(pentagon,(200,500))
    #window.blit(hexagon,(200,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONUP:
            pass
    pygame.display.update()
