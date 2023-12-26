class Settings:
    """A class to manage all the game settings."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)
        self.bg_image = 'images/bg-image.bmp'
        # Ship settings.
        self.ship_limit = 3
        # Bullet settings.
        self.bullet_width = 15
        self.bullet_height = 6
        self.bullet_color = (220, 199, 0)
        self.bullet_color_power_up = (220, 20, 90)
        self.bullets_allowed = 3
        self.bullet_threshold = 10
        self.simple_bullet = True
        # Alien settings
        self.fleet_move_speed = 14
        # How quickly tha game speeds up
        self.speedup_scale = 1.1
        # Button settings
        self.button_color = (0, 165, 90)
        self.button_color_hover = (0, 205, 50)
        self.text_color = (255, 255, 255)
        self.text_color_hover = (240, 240, 240)
        self.font_name = 'Courier New'
        self.font_size = 44
        self.button_width = 200
        self.button_height = 50
        self.difficulty_button_offset = 10
        self.initialize_dynamic_settings()
        # Scoreboard settings
        self.score_color = (40, 140, 240)
        self.score_font_family = 'Courier New'
        self.score_font_size = 44
        # How quickly the alien point values increase
        self.score_scale = 1.5
        # The upper horizontal space is reserved for scoreboard.
        self.upper_edge = 120

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        # fleet_direction of 1 represents down; -1 represents up.
        self.fleet_direction = -1
        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)