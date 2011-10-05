import pygame
from pygame.locals import *

class Paddle:
    def __init__(self,screen):
        self.screen = screen
        self.width = 100
        self.height = 10
        (self.screenWidth, self.screenHeight) = self.screen.get_size()
        # position 40 pixels from bottom
        self.y = self.screenHeight-40
        # initial pos in middle of screen, minus half width for centering
        self.x = (self.screenWidth/2)-(self.width/2)
       
    def draw(self):
        (mouseX,mouseY) = pygame.mouse.get_pos()
        self.x = mouseX-(self.width/2)
        pygame.draw.rect(self.screen, (255,255,255), (self.x,self.y,100,10))
        
    def isCollided(self,(x,y)):
        ''' Returns True if given coordinates are within top line of paddle.
            Otherwise returns False
        '''
        # is point below our y level, and between our upper left/right corners?
        if y>=self.y and x >= self.x and x <= (self.x+self.width):
                return True
        
        return False
                
            