import pygame
from pygame.locals import *

class Brick:
    def __init__(self,pos,size,color,screen):
        ''' Initializes a brick with top left corner at pos=(x,y) 
            with width and size specified by size=(w,h), and of the color
            specified by a tuple (r,g,b).
        '''
        self.x = pos[0]
        self.y = pos[1]
        self.width = size[0]
        self.height = size[1]
        self.color = color
        self.screen = screen
        
    def draw(self):
        pygame.draw.rect(self.screen,self.color,(self.x,self.y,self.width,self.height))
        
class BrickBlock:
    def __init__(self, rows, cols, (x,y), screen):
        ''' Initializes a block of bricks of a specified amount of rows and 
            columns, centered on (x,y)
        '''
        # init variables
        self.brickWidth = 50
        self.brickHeight = 20
        self.rows = rows
        self.columns = cols
        self.screen = screen
        self.padding = 5
        
        # find top left x,y given amount of rows and columns, and brick dimensions
        self.x = x-self.columns*(self.brickWidth+self.padding)/2
        self.y = y-self.rows*(self.brickHeight+self.padding)/2
        
        self.brickList = []
        currX = self.x
        currY = self.y
        color = (138,43,226)
        for i in range(0,self.rows):        
            for i in range(0,self.columns):
                self.brickList.append(Brick((currX,currY),
                    (self.brickWidth,self.brickHeight), color, self.screen))
                currX += self.brickWidth+self.padding
            currX = self.x
            currY += self.brickHeight+self.padding
                    
    def draw(self):
        for b in self.brickList:
            b.draw()
            
    def testCollisions(self,x,y,radius,xSpeed,ySpeed):
        ''' Tests each block to see if there is a collision. If there is, returns
            a new (xSpeed, ySpeed).
            
            Returns (0,0) for no collisions found.
        '''
        newXSpeed = 0
        newYSpeed = 0
        # four points to test
        top = (x,y-radius)
        bottom = (x,y+radius)
        left = (x-radius,y)
        right = (x+radius,y)
        for b in self.brickList[:]:
            if top[1] <= b.y+b.height and top[1] >= b.y: 
                # top y past bottom line of brick and before top line
                if top[0] >= b.x and top[0] <= b.x+b.width:
                    # top x between left & right sides
                    # collision with bottom, bounce down
                    newYSpeed = abs(ySpeed)
                    self.brickList.remove(b)
                    return (newXSpeed,newYSpeed)
            if bottom[1] >= b.y and bottom[1] <= b.y+b.height: 
                # bottom y past top line of brick and before bottom line
                if bottom[0] >= b.x and bottom[0] <= b.x+b.width:
                    # bottom x between left & right sides
                    # collision with top
                    newYSpeed = ySpeed - ySpeed*2
                    self.brickList.remove(b)
                    return (newXSpeed,newYSpeed)
            if left[0] <= b.x+b.width and left[0] >= b.x: # left x past right line
                if left[1] >= b.y and left[1] <= b.y+b.height:
                    # y between top & bottom sides
                    # collision with right side
                    newXSpeed = abs(xSpeed)
                    self.brickList.remove(b)
                    return (newXSpeed,newYSpeed)
            if right[0] <= b.x and right[0] >= b.x+b.width: # right x past left line
                if right[1] >= b.y and right[1] <= b.y+b.height:
                    # y between top & bottom
                    # collision with left side
                    newXSpeed = xSpeed - xSpeed*2
                    self.brickList.remove(b)
                    return (newXSpeed,newYSpeed)
                
        return (0,0)
        