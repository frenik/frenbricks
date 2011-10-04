import pygame
from pygame.locals import *

# my imports
import paddle
import ball

# Constants
SCREEN_MODE = (640,480) # screen size (w,h)
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
        # TODO: check for collisions
        
        # do all other drawing
        p.draw()
        b.draw()
        # flip it
        pygame.display.flip()
        # limit to 60 fps
        clock.tick(60)

if __name__ == '__main__':
    main()