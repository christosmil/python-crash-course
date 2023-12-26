class GameStats:
    """Track statistics for Sideways Shooter."""

    def __init__(self, ss_game, high_score):
        """Initialize statistics."""
        self.settings = ss_game.settings
        self.reset_stats()
        # Start Alien Invasion in an inactive state.
        self.play_button_pressed = False
        self.game_active = False
        self.game_paused = False
        # High score should never been reset.
        self.high_score = high_score

    def reset_stats(self):
        """Initialize attributes that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
        self.alien_hits = 0
        self.settings.simple_bullet = True