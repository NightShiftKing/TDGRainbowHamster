import pygame
import math
from map import Map
from player import Player
pygame.init()
pygame.display.set_caption("sprite sheet")  # sets the window title
screen = pygame.display.set_mode((800,800))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #set up clock
gameover = False #variable to run our game loop

# CONSTANTS
LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3
SPACE = 4
keys = [False, False, False, False, False] #this list holds whether each key has been pressed
mapNum = 1

#maps

map = Map.MAP1.value

twomap = Map.MAP2.value


wall = pygame.image.load('stone.png')  # load your spritesheet

Rock = pygame.image.load('blocker.png') # load your spritesheet
Puddle = pygame.image.load('potion thing.png') # load your spritesheet
Portal = pygame.image.load('DOOR.png')


# player variables
xpos = 400  # xpos of player
ypos = 400  # ypos of player

PunkHamster = Player(xpos,ypos,'The Punk.png')

ticker = 0
direction = DOWN

while not gameover:
    clock.tick(60)  # FPS

    for event in pygame.event.get():  # quit game if x is pressed in top corner
        if event.type == pygame.QUIT:
            gameover = True

        #keyboard input---------------------------
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                keys[LEFT] = True
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT] = True
            elif event.key == pygame.K_UP:
                keys[UP] = True
            elif event.key == pygame.K_DOWN:
                keys[DOWN] = True


        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                keys[LEFT] = False
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT] = False
            elif event.key == pygame.K_UP:
                keys[UP] = False
            elif event.key == pygame.K_DOWN:
                keys[DOWN] = False




    #Left/right MOVEMENT-------------------------------------
    PunkHamster.move() 

    #map collision---------------------






    # Animation update
    ticker+=1
    if vx != 0: #only animate when moving
        if ticker % 10 == 0:  # only change frames every 10 ticks (make number smaller for faster running animation)
            frameNum += 1
    if frameNum > 1:
        frameNum = 0

    # Render section--------------------------------------------------------
    screen.fill((0, 0, 0))  # wipe screen so it doesn't smear
    # draw map
    if mapNum == 1:
        for i in range(20):
            for j in range(20):
                if map[i][j] == 2:
                    screen.blit(wall, (j * 40, i * 40), (0, 0, 40, 40))
                elif map[i][j] == 3:
                    screen.blit(Rock, (j * 40, i * 40), (0, 0, 40, 40))
                elif map[i][j] == 4:
                    screen.blit(Puddle, (j * 40, i * 40), (0, 0, 40, 40))
                elif map[i][j] == 5:
                    screen.blit(Portal, (j * 40, i * 40), (0, 0, 40, 40))

    if mapNum == 2:
        for i in range(20):
            for j in range(20):
                if twomap[i][j] == 2:
                    screen.blit(wall, (j * 40, i * 40), (0, 0, 40, 40))
                elif twomap[i][j] == 3:
                    screen.blit(Rock, (j * 40, i * 40), (0, 0, 40, 40))
                elif twomap[i][j] == 4:
                    screen.blit(Puddle, (j * 40, i * 40), (0, 0, 40, 40))
                elif twomap[i][j] == 5:
                    screen.blit(Portal, (j * 40, i * 40), (0, 0, 40, 40))

    # draw player
    PunkHamster.draw(screen)
    pygame.display.flip()  # this actually puts the pixel on the screen

# end game loop
pygame.quit()