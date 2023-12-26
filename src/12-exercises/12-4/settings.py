class Settings:
    """A class to store all the settings."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        # Background color settings
        self.bg_color = (20, 20, 20)
        # Rocket speed
        self.rocket_speed = 2.5