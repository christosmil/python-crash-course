class Settings:
    """A class to manage all the game settings."""

    def __init__(self):
        """Initialize the game settings."""
        # Screen settings.
        self.screen_width = 1260
        self.screen_height = 820
        self.bg_color = (70, 40, 150)
        # Ship settings.
        self.ship_speed = 1.5
        # Bullet settings.
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (220, 20, 90)
        self.bullet_speed = 3.0
        self.bullets_allowed = 3