import pygame
from pygame.locals import *

class Ball:
    def __init__(self,screen,x,y):
        self.screen = screen
        (self.screenWidth, self.screenHeight) = self.screen.get_size()
        # make ball 10 pixels wide
        self.diameter = 10
        self.x = x
        self.y = y-self.diameter/2
        # i'd like to make this mathematically better
        self.xSpeed = 0
        self.ySpeed = 0
        self.initialSpeed = 5
        
    def draw(self):
        ''' Draw ball. 
        '''
        # draw it
        pygame.draw.circle(self.screen, (100,100,100), (self.x, self.y), self.diameter)
        # update headings
        self.y += self.ySpeed
        self.x += self.xSpeed
        
    def getBottom(self):
        ''' Returns (x,y), where x and y are the coordinates of the point
            in the center-bottom of the ball.
        '''
        return (self.x, (self.y+(self.diameter)))
    
    def getTop(self):
        ''' Returns (x,y), where x and y are the coordinates of the point in the
            top-center of ball.
        '''
        return ((self.x+(self.diameter/2)), self.y)