import sys 

import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall class to mange game assets and behavior."""

    def __init__(self):
        """Initializa the game, and create game resources."""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")
    
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update() 
            self._update_screen()
            self.clock.tick(60)  # Making the clock tick


    def _check_events(self):
            """Respond to keypresses and mouse events."""
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Make the most recently drawn screen visible.
            pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()

    


    #ERROR CAUSE SHIP IMAGE CANT BE WRITTEN. NEED TO BE FIXED