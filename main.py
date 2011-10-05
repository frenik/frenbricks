import pygame
from pygame.locals import *

# my imports
import paddle
import ball
import brickui
import bricks

# Constants
SCREEN_MODE = (1280,1024) # screen size (w,h)
SCREEN_FLAGS = (pygame.FULLSCREEN)
SCREEN_CAPTION = 'Bricks'
GS_LAUNCH = 0   # waiting to launch ball
GS_BOUNCE = 1   # ball bouncing

def main():   
    pygame.init()
    # set screen mode
    screen = pygame.display.set_mode(SCREEN_MODE, SCREEN_FLAGS)
    # set window title
    pygame.display.set_caption(SCREEN_CAPTION)
    # hide mouse (we'll draw our own later)
    pygame.mouse.set_visible(0)
    # set up background surface
    bg = pygame.Surface(screen.get_size())
    bg = bg.convert()
    bg.fill((0,0,0)) # black    
    screen.blit(bg, (0,0))
    pygame.display.flip()
    clock = pygame.time.Clock()
    p = paddle.Paddle(screen)
    gameState = GS_LAUNCH
    b = ball.Ball(screen,p.x+p.width/2,p.y)
    scoreboard = brickui.BrickUI(screen)
    brickBlock = bricks.BrickBlock(5,10,
        (screen.get_width()/2,screen.get_height()/2),screen)
    
    # FOR DEBUG TEXT
    debugFont = pygame.font.Font(None, 36)
    
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == QUIT:
                done = True   
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                done = True
                
        # blit background surface to wipe
        screen.blit(bg, (0,0))
        # do different things depending on gamestate
        if gameState == GS_LAUNCH:
            p.draw()
            # update ball's x to middle of paddle
            b.x = p.x + p.width/2
            # update ball's y to sit on top of paddle
            b.y = p.y - b.diameter
            # draw it
            b.draw()
            if pygame.mouse.get_pressed()[0]:
                gameState = GS_BOUNCE
                # launch upwards
                b.ySpeed -= b.initialSpeed       
            # draw walls
            pygame.draw.rect(screen, (255,255,255), 
                (0,0,screen.get_size()[0],screen.get_size()[1]+10),10)
            # draw bricks
            brickBlock.draw()
            # draw UI
            scoreboard.draw()
        elif gameState == GS_BOUNCE:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    #reset, TEMPORARY
                    if event.key == K_r: 
                        gameState = GS_LAUNCH
                        b = ball.Ball(screen, p.x+p.width/2,p.y)
            # check for collision of bottom of ball/paddle
            if p.isCollided(b.getBottom()):
                b.ySpeed -= b.ySpeed*2
                b.ySpeed -= 1 # speed up by 1
                newXSpeed = p.getNewXSpeed(b.getBottom()) 
                if newXSpeed != 0: b.xSpeed = newXSpeed
            # check for collision with top wall
            if b.y <= 0:
                # vertical speed should be negative, so we'll just abs() it.
                b.ySpeed = abs(b.ySpeed)
            # check for ball hitting left wall
            if b.x <= 0:
                b.xSpeed = abs(b.xSpeed)
            # check for ball hitting right wall
            if b.x+b.diameter >= screen.get_size()[0]:
                b.xSpeed -= b.xSpeed*2
            # check for ball exiting screen through bottom
            if b.y >= screen.get_size()[1]:
                # reinit ball
                b = ball.Ball(screen,p.x+p.width/2,p.y)
                # go back to launch
                gameState = GS_LAUNCH
            # check for ball colliding with any bricks
            newVector = brickBlock.testCollisions(b.x,b.y,b.diameter/2,
                b.xSpeed,b.ySpeed)
            if newVector[0] != 0: # bounced left or right
                b.xSpeed = newVector[0]
            if newVector[1] != 0: # bounced up or down
                b.ySpeed = newVector[1]
            # do all other drawing
            p.draw() # paddle
            b.draw() # ball
            # draw walls
            pygame.draw.rect(screen, (255,255,255), 
                (0,0,screen.get_size()[0],screen.get_size()[1]+10),10)
            # draw bricks            
            brickBlock.draw()
            # draw UI
            scoreboard.draw()
            # ANY DEBUG TEXT
            '''
            debugText = "BALL X, Y = %i, %i"%(b.x,b.y)
            text = debugFont.render(debugText,1,(255,255,255))
            screen.blit(text, (20,20,text.get_width(),text.get_height()))
            debugText = "PADDLE EDGE = %i"%(p.x+100)
            text = debugFont.render(debugText,1,(255,255,255))
            screen.blit(text, (20,50,text.get_width(),text.get_height()))
            '''
            
        # flip it
        pygame.display.flip()
        # limit to 60 fps
        clock.tick(60)

if __name__ == '__main__':
    main()