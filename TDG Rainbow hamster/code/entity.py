import pygame

class Entity:
    def __init__(self, xpos, ypos, image):
        self.xpos = xpos
        self.ypos = ypos
        self.image = pygame.image.load(image)
        self.velocity = pygame.Vector2(0,0) 
        self.pos = pygame.Vector2(xpos,ypos)
        self.rect = self.image.get_rect()

        