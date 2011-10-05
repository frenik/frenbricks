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
        for b in self.brickList[:]:
            inX = False
            inY = False
            # test for side collisions
            if xSpeed > 0: # ball traveling right
                if x+radius > b.x and x+radius < b.x+b.width:
                    # ball within x boundaries
                    inX = True
                    newXSpeed = xSpeed - xSpeed*2
            elif xSpeed < 0: # ball traveling left
                if x-radius > b.x and x-radius < b.x+b.width:
                    inX = True
                    newXSpeed = abs(xSpeed)
            else: # ball traveling along Y axis
                if x > b.x and x < b.x+b.width:
                    inX = True                
            if ySpeed > 0: # ball traveling down
                if y+radius > b.y and y+radius < b.y+b.height:
                    inY = True
                    newYSpeed = ySpeed - ySpeed*2
            elif ySpeed < 0:
                if y-radius > b.y and y-radius < b.y+b.height:
                    inY = True
                    newYSpeed = abs(ySpeed)
            else: # ball traveling along X axis (shouldn't happen)
                if y > b.y and y < b.y+b.height:
                    inY = True
            if inX and inY:
                self.brickList.remove(b)
                return (newXSpeed,newYSpeed)
            else:
                # false alarm, reset
                newXSpeed = 0
                newYSpeed = 0
                
        return (newXSpeed,newYSpeed)
        