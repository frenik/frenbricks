import pygame
from pygame.locals import *

class Ball:
    def __init__(self,screen):
        self.screen = screen
        (self.screenWidth, self.screenHeight) = self.screen.get_size()
        # for now, spawn at center x, y=0, heading straight down
        self.x = self.screenWidth/2
        self.y = 0
        # make ball 10 pixels wide
        self.diameter = 10
        # i'd like to make this mathematically better
        self.xSpeed = 0
        self.ySpeed = 6
        
    def draw(self):
        # draw it
        pygame.draw.circle(self.screen, (100,100,100), (self.x, self.y), self.diameter)
        # update headings
        self.y += self.ySpeed
        
    def getBottom(self):
        ''' Returns (x,y), where x and y are the coordinates of the point
            in the center-bottom of the ball.
        '''
        return ((self.x+(self.diameter/2)), (self.y+(self.diameter)))
    
    def getTop(self):
        ''' Returns (x,y), where x and y are the coordinates of the point in the
            top-center of ball.
        '''
        return ((self.x+(self.diameter/2)), self.y)