import pygame
from pygame.locals import *

class Ball:
    def __init__(self,screen):
        self.screen = screen
        (self.screenWidth, self.screenHeight) = self.screen.get_size()
        # for now, spawn at center x, y=0, heading straight down
        self.x = self.screenWidth/2
        self.y = 0
        # i'd like to make this mathematically better
        self.xSpeed = 0
        self.ySpeed = 2
        
    def draw(self):
        # draw it
        pygame.draw.circle(self.screen, (100,100,100), (self.x, self.y), 10)
        # update headings
        self.y += self.ySpeed