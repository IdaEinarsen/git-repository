import sys

import pygame


# this is how it can look in the beginning whitout using a settings file.
# this will create a window in the set color 0, 0, 255 (blue) whit the name Blue Sky

class BlueSky:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initializa the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Blue Sky")

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
            
             # Make the most recently drawn screen visible
             pygame.display.flip()
             self.clock.tick(60) #framerate 
        
if __name__ == '__main__':
    # Make a game instance, and run the game.
    bs = BlueSky()
    bs.run_game()