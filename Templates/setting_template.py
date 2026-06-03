class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initializa the game's settings."""
        
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 100) 



        
# When using a settings file you have to change so u dont have bg_color and the other settings in main file.

# Using this example you have to :
# - Import Settings file 
# - Add self.settings = Settings() in game resources.
# - change = pygame.display.set_mode to ((self.settings.screen_width, self.settings.screen_height))
# - change screen.fill = (self.settings.bg_color)


