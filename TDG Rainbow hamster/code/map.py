import pygame

class Map():
    def __init__(self):

    
        self.MAP1 = [
        [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
        [2, 0, 0, 0, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 0, 0, 0, 0, 2],
        [2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
        [2, 0, 2, 0, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 0, 0, 0, 0, 2],
        [2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2],
        [2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 2, 0, 0, 0, 2],
        [5, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2],
        [2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
        [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2],
        [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
        [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 2],
        [2, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 4, 4, 4, 0, 0, 0, 0, 0, 2],
        [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 2],
        [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
        [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
        [2, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 2],
        [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
        [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
        [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
        [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2] ]

        self.MAP2 = [
        [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
        [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
        [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
        [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
        [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
        [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
        [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
        [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
        [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
        [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
        [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
        [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
        [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
        [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
        [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
        [2, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 2],
        [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
        [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
        [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
        [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2] ]


        self.wall = pygame.image.load('TDG Rainbow hamster\\images\\Stone.png')  # load your spritesheet

        self.Rock = pygame.image.load('TDG Rainbow hamster\\images\\blocker.png') # load your spritesheet
        self.Puddle = pygame.image.load('TDG Rainbow hamster\\images\\potion thing.png') # load your spritesheet
        self.Portal = pygame.image.load('TDG Rainbow hamster\\images\\DOOR.png')
        self.currentMap = self.MAP1
    def map_collision(self, entity):

        #left collision
        if self.currentMap[int((entity.pos.y) / 40)][int((entity.pos.x - 5) / 40)] == 2 :
            entity.pos.x+=10

    
        #right collision
        if self.currentMap[int((entity.pos.y) / 40)][int((entity.pos.x +20) / 40)] == 2 :
            entity.pos.x-=10

        
        #up collision
        if self.currentMap[int((entity.pos.y-5) / 40)][int((entity.pos.x) / 40)] == 2:
            entity.pos.y+=10  

        #down collision
        if self.currentMap[int((entity.pos.y+25) / 40)][int((entity.pos.x) / 40)] == 2:
            entity.pos.y-=10  



        ###ROCK COLLISION
        #left collision
        if self.currentMap[int((entity.pos.y) / 40)][int((entity.pos.x - 5) / 40)] == 3 :
            entity.pos.x+=10

    
        #right collision
        if self.currentMap[int((entity.pos.y) / 40)][int((entity.pos.x +20) / 40)] == 3 :
            entity.pos.x-=10

        
        #up collision
        if self.currentMap[int((entity.pos.y-5) / 40)][int((entity.pos.x) / 40)] == 3:
            entity.pos.y+=10  

        #down collision
        if self.currentMap[int((entity.pos.y+25) / 40)][int((entity.pos.x) / 40)] == 3:
            entity.pos.y-=10


        
        
        #######Portal 1
        if self.currentMap[int((entity.pos.y) / 40)][int((entity.pos.x - 5) / 40)] == 5:
            self.currentMap = self.MAP2
            entity.pos.x = 730
            entity.pos.y = 690


    
        #portal 2
        if self.currentMap[int((entity.pos.y) / 40)][int((entity.pos.x +20) / 40)] == 5 :
            self.currentMap = self.MAP1
            entity.pos.x = 50
            entity.pos.y = 240


    def drawMap(self, screen):
            for i in range(20):
                for j in range(20):
                    if self.currentMap[i][j] == 2:
                        screen.blit(self.wall, (j * 40, i * 40), (0, 0, 40, 40))
                    elif self.currentMap[i][j] == 3:
                        screen.blit(self.Rock, (j * 40, i * 40), (0, 0, 40, 40))
                    elif self.currentMap[i][j] == 4:
                        screen.blit(self.Puddle, (j * 40, i * 40), (0, 0, 40, 40))
                    elif self.currentMap[i][j] == 5:
                        screen.blit(self.Portal, (j * 40, i * 40), (0, 0, 40, 40))

            

