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
        self.ship_limit = 3
        # Bullet settings.
        self.bullet_width = 15
        self.bullet_height = 6
        self.bullet_color = (220, 20, 90)
        self.bullet_speed = 1.0
        self.bullets_allowed = 3
        self.simple_bullet = True
        # Target settings
        self.target_width = 6
        self.target_height = 260
        self.target_color = (220, 220, 90)
        self.target_speed = 1.0
        self.target_direction = -1