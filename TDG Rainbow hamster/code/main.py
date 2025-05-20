import pygame
import math
from map import Map
from player import Player
pygame.init()
pygame.display.set_caption("sprite sheet")  # sets the window title
screen = pygame.display.set_mode((800,800))  # creates game screen

clock = pygame.time.Clock() #set up clock
gameover = False #variable to run our game loop

#maps
map = Map()

# player variables
xpos = 400  # xpos of player
ypos = 400  # ypos of player
PunkHamster = Player(xpos,ypos,'TDG Rainbow hamster\\images\\The PUNK.png')


#game loop
while not gameover:
    ticks = clock.get_time()
    clock.tick(60)  # FPS
    gameEvents = pygame.event.get()

    for event in gameEvents:  # quit game if x is pressed in top corner
        if event.type == pygame.QUIT:
            gameover = True

    #keyboard input---------------------------
    PunkHamster.move() 
    #map collision---------------------
    map.map_collision(PunkHamster)
    # Animation update
    PunkHamster.animate()
    # Render section--------------------------------------------------------
    screen.fill((0, 0, 0))  # wipe screen so it doesn't smear
    PunkHamster.draw(screen)
    # draw map
    map.drawMap(screen)
    # draw player
    pygame.display.flip()  # this actually puts the pixel on the screen

# end game loop
pygame.quit()