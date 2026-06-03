# 12.2 Game Characters   (Using blue sky program as foundation and settings in main file)

import sys

import pygame
from guy import Guy


class BlueSky:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initializa the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Blue Sky")

        self.guy = Guy(self)

        #Set background color
        self.bg_color = (0, 0, 255)

    def run_game(self):
        """Starting the main loop for the game"""
        while True:
             # Watch for keyboard and mouse events.
             for event in pygame.event.get():
                 if event.type == pygame.QUIT:
                     sys.exit()

             # Redraw the screen during each pass through the loop.
             self.screen.fill(self.bg_color)
             self.guy.blitme()
            
             # Make the most recently drawn screen visible
             pygame.display.flip()
             self.clock.tick(60)
        
if __name__ == '__main__':
    # Make a game instance, and run the game.
    bs = BlueSky()
    bs.run_game()
