import pygame
from pygame.locals import *

# my imports
import paddle
import ball

# Constants
SCREEN_MODE = (1280,1024) # screen size (w,h)
SCREEN_FLAGS = (pygame.FULLSCREEN)
SCREEN_CAPTION = 'Bricks'

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
    b = ball.Ball(screen)
    
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == QUIT:
                done = True   
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                done = True
        # blit background surface to wipe
        screen.blit(bg, (0,0))
        # check for collision of bottom of ball/paddle
        if p.isCollided(b.getBottom()):
            b.ySpeed -= b.ySpeed*2
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
            # create new ball for now
            b = ball.Ball(screen)
        # do all other drawing
        p.draw()
        b.draw()
        # flip it
        pygame.display.flip()
        # limit to 60 fps
        clock.tick(60)

if __name__ == '__main__':
    main()