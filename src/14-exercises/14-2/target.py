import pygame

class Target:
    """A class to manage the target."""

    def __init__(self, tp_game):
        """Create a target object."""
        super().__init__()
        self.screen = tp_game.screen
        self.screen_rect = tp_game.screen.get_rect()
        self.settings = tp_game.settings
        self.color = self.settings.target_color
        # Create a target rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.settings.target_width,
            self.settings.target_height)
        self.rect.x = self.settings.screen_width - 5*self.settings.target_width
        self.center_target()

    def check_edges(self):
        """Return true if target is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom or self.rect.top <= 0:
            return True

    def update(self):
        """Move the target up or down."""
        self.y += self.settings.target_speed*self.settings.target_direction
        self.rect.y = self.y

    def draw_target(self):
        """Draw the target to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)

    def center_target(self):
        """Center the target on the right side of the screen."""
        self.rect.midright = self.screen_rect.midright
        self.y = float(self.rect.y)
