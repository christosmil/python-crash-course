import pygame
from pygame.sprite import Sprite

class Raindrop(Sprite):
    """A class to represent a single raindrop."""

    def __init__(self, steady_rain):
        """Initialize the raindrop and set its starting position."""
        super().__init__()
        self.screen = steady_rain.screen
        self.settings = steady_rain.settings

        # Load the raindrop image and set its rect attribute.
        self.image = pygame.image.load('./images/raindrop.bmp')
        self.rect = self.image.get_rect()

        # Start each new raindrop near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the raindrop's exact vertical position.
        self.y = float(self.rect.y)

    def update(self):
        """Drop the raindrop."""
        self.y += self.settings.raindrop_speed
        self.rect.y = self.y