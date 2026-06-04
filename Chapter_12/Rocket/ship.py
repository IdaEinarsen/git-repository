import pygame  #import pygame module

class Ship:
    """Class to manage the ship"""
    
    def __init__(self, rg_game):
        """Initialize the rocketship and set starting position."""
        self.screen = rg_game.screen
        self.settings = rg_game.settings
        self.screen_rect = rg_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/onlyrocket.bmp').convert()

        # Make white transparent
        self.image.set_colorkey((255, 255, 255))

        # Scale image
        self.image = pygame.transform.scale(self.image, (150, 150))

        self.rect = self.image.get_rect()

        # Start each new ship at the center of screen
        self.rect.center = self.screen_rect.center

        # Store a float for the ship's exact horizontal position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flag; start with a ship that's not moving
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if  self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed 
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed 

        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
