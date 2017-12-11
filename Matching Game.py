import pygame, sys, random
from pygame.locals import *


def Init():
    global window, win, counter1, xcoord, ycoord, gridx, gridy, circle, cross, triangle, square, pentagon, hexagon, rhombus, purple, green, pink, blue, red, yellow, difficulty, title, titleRect, font1, font2, text
    pygame.init()
    window = pygame.display.set_mode((800,600))
    pygame.display.set_caption('Matching Game')
    font1 = pygame.font.SysFont('broadway',40)
    font2 = pygame.font.SysFont('broadway',24)
    movecounter = 0
    counter1 = 0
    xcoord,ycoord = -1,-1
    gridx, gridy = -1,-1
    win = False


    purple = (205,205,255)
    green = (205,255,205)
    pink = (255,205,205)
    blue = (125,175,255)
    red = (255,75,75)
    yellow = (255,255,125)

    text = ['Matching Game','Select Difficulty','Easy','Medium','Hard', 'You Win! Play Again?', 'You Lose. Try Again?']

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

class Tile(object):
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color

def MakeGrid():
    global grid, moves
    shuffleList = []
    colorlist = [red, yellow, green, blue, purple]
    if difficulty == 3:
        shapelist = [circle, cross, triangle]
    if difficulty == 5:
        shapelist = [circle, cross, triangle, square, pentagon]
    if difficulty == 7:
        shapelist = [circle, cross, triangle, square, pentagon, hexagon, rhombus]

    moves = difficulty*5
    for shape in shapelist:
        for color in colorlist:
            newtile = Tile(shape, color)
            shuffleList.append(newtile)
    random.shuffle(shuffleList)

    grid = list(splitter(shuffleList, 5))


def DrawGrid():
    global offset, moves1, movesRect
    window.fill(pink)
    window.blit(title,titleRect)
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

    moves1 = font2.render(str(moves),True, (0,0,0))
    movesRect = moves1.get_rect()
    movesRect.center = (100,50)
    window.blit(moves1, movesRect)

def splitter(l, n):
    # For item i in a range that is a length of l,
    for i in range(0, len(l), n):
        # Creates an index range for l of n items:
        yield l[i:i+n]

def winChecker():
    global win
    counter2 = 0
    for smalllist in grid:
        if all(smalllist[0].shape == item.shape for item in smalllist):
            for item in grid[0]:
                if all(item.color == grid[integer][grid[0].index(item)].color for integer in range(1,difficulty)):
                    counter2 += 1
    if counter2 == 5*difficulty:
        win = True

def reset():
    global win, difficulty
    win = False
    difficulty = 0

def winScreen():
    global difficulty
    mousex,mousey = 0,0

    window.fill(blue)
    pygame.draw.rect(window, purple, (100,100, 600, 400))
    pygame.draw.rect(window, green, (125,175, 150, 300))
    pygame.draw.rect(window, yellow, (325,175, 150, 300))
    pygame.draw.rect(window, red, (525,175, 150, 300))

    diff = font2.render(text[5],True, (0,0,0))
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
    reset()

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

    MakeGrid()
    DrawGrid()



Init()
MakeGrid()
DrawGrid()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONUP:
            mousex,mousey = event.pos
            if mousex > offset and mousex < offset + (difficulty*100):
                if mousey > 100 and mousey < 600:
                    xcoord = (mousex - offset) // 100
                    ycoord = (mousey - 100) // 100
                    if xcoord != gridx or ycoord != gridy:
                        counter1 += 1

    if counter1 == 2:
        tile = grid[xcoord][ycoord]
        grid[xcoord][ycoord] = grid[gridx][gridy]
        grid[gridx][gridy] = tile
        DrawGrid()
        winChecker()
        xcoord,ycoord,gridx,gridy = -1,-1,-1,-1
        counter1 = 0
        moves -= 1
        pygame.draw.rect(window, pink, (75,0,100,100))
        moves1 = font2.render(str(moves),True, (0,0,0))
        movesRect = moves1.get_rect()
        movesRect.center = (100,50)
        window.blit(moves1, movesRect)
        if win == True:
            winScreen()

    if counter1 == 1:
        gridx,gridy = xcoord,ycoord

    pygame.display.update()
