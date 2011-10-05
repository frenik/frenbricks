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
        ''' Returns X multiplier if given coordinates are within top line of paddle.
            Otherwise returns False
        '''
        # is point below our y level, and between our upper left/right corners?
        if y>=self.y and x >= self.x and x <= (self.x+self.width):
            return True
        else:
            return False
                
    def getNewXSpeed(self,(x,y)):
        ''' Determines which section of the paddle (x,y) is within, and 
            returns a new x speed for the object. The first and last
            10% of the bar return -5 and 5, respectively, the second and
            second-to-last return -3 and 3, and so on. The middle 20% returns
            0, no change.
        '''
        # comments assume self.x = 1
        if x in range(self.x, self.x+10): # 1-10
            return -5
        if x in range(self.x+10, self.x+20): # 11-20
            return -3
        if x in range(self.x+20, self.x+30): # 21-30
            return -2
        if x in range(self.x+30, self.x+40): # 31-40
            return -1
        if x in range(self.x+40, self.x+60): # 41-60 (mid 20%)
            return 0
        if x in range(self.x+60, self.x+70): # 61-70
            return 1
        if x in range(self.x+70, self.x+80): # 71-80
            return 2
        if x in range(self.x+80, self.x+90): # 81-90
            return 3
        if x in range(self.x+90, self.x+101): # 91-100
            return 5