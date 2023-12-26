import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ss_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ss_game.screen
        self.settings = ss_game.settings

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top right of the screen.
        self.rect.x = self.settings.screen_width - self.rect.width
        self.rect.y = self.settings.upper_edge + self.rect.height

        # Store the alien's exact vertical position.
        self.y = float(self.rect.y)

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if (self.rect.bottom >= screen_rect.bottom or
            self.rect.top <= self.settings.upper_edge):
            return True

    def update(self):
        """Move the alien up or down."""
        self.y += self.settings.alien_speed*self.settings.fleet_direction
        self.rect.y = self.y