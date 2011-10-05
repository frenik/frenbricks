import pygame
from pygame.locals import *

class BrickUI:
    def __init__(self, screen):
        self.screen = screen
        self.score = 0
        self.lives = 3
        self.font = pygame.font.Font(None, 36)        
        self.scoreColor = (255,165,0)
        self.livesColor = (255,165,0)
    
    def draw(self):
        # score in top right        
        scoreText = self.font.render("Score: %i"%self.score, 1, self.scoreColor)
        scoreTextPos = scoreText.get_rect(topright=(self.screen.get_width()-20,20))
        # lives in top left
        livesText = self.font.render("Lives: %i"%self.lives, 1, self.livesColor)
        livesTextPos = livesText.get_rect(topleft=(20,20))
        # draw score and lives
        self.screen.blit(scoreText, scoreTextPos)
        self.screen.blit(livesText, livesTextPos)