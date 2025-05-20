import pygame
from entity import Entity

class Player(Entity):
    def __init__(self,xpos, ypos, image_path):
        super().__init__(xpos, ypos, image_path)

        #animation variables
        self.frameWidth = 60
        self.frameHeight = 60
        self.RowNum = 0  # for left animation, this will need to change for other animations
        self.frameNum = 0
        self.ticker = 0 
        self.image.set_colorkey((255,0,255))

    def draw(self, screen):
        screen.blit(self.image, (self.pos.x, self.pos.y), (self.frameWidth * self.frameNum, self.RowNum * self.frameHeight, self.frameWidth, self.frameHeight))

    def move(self, speed = 10):
        keys = pygame.key.get_pressed()
        self.velocity.x = speed if keys[pygame.K_RIGHT] or keys[pygame.K_d] else -speed if keys[pygame.K_LEFT] or keys[pygame.K_a] else 0
        self.velocity.y = speed if keys[pygame.K_DOWN] or keys[pygame.K_s] else -speed if keys[pygame.K_UP] or keys[pygame.K_w] else 0

        self.pos += self.velocity


    def animate(self):
        self.ticker+=1
        if self.velocity.x != 0: #only animate when moving
            if self.ticker % 10 == 0:  # only change frames every 10 ticks (make number smaller for faster running animation)
                self.frameNum += 1
        if self.frameNum > 7:
            self.frameNum = 0


         
