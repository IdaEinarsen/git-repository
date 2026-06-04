import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """ Manage bullets fired from ship."""

    def __init__(self, rg_game):
        super().__init__()

        self.screen = rg_game.screen
        self.settings = rg_game.settings
        self.color = self.settings.bullet_color

        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midleft = rg_game.ship.rect.midright   # Changed this from midtop to midright to shoot from sides

        # Store as float
        self.x = float(self.rect.x)  

    def update(self):
        """ Move bullets on screen"""
        self.x += self.settings.bullet_speed
        self.rect.x = self.x

    def draw_bullet(self):
        """Draw bullet on screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
        