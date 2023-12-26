class Settings:
    """A class to manage all the game settings."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings.
        self.screen_width = 1260
        self.screen_height = 820
        self.bg_color = (70, 40, 150)
        # Ship settings.
        self.ship_limit = 3
        # Bullet settings.
        self.bullet_width = 15
        self.bullet_height = 6
        self.bullet_color = (220, 20, 90)
        self.bullets_allowed = 3
        self.simple_bullet = True
        # Target settings
        self.target_width = 6
        self.target_height = 260
        self.target_color = (220, 220, 90)
        # Threshold to level up.
        self.levelup_hits = 10
        # How quickly the game speeds up.
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.target_speed = 1.0
        # target direction of -1 represents up; 1 represents down.
        self.target_direction = -1

    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.target_speed *= self.speedup_scale