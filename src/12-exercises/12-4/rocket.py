import pygame

class Rocket:
    """Represent the rocket."""

    def __init__(self, r_game):
        """Initialize rocket's attributes."""
        # Initialize screen.
        self.screen = r_game.screen
        self.screen_rect = r_game.screen.get_rect()
        # Initialize settings.
        self.settings = r_game.settings
        # Load the rocket image and get its rect.
        self.image = pygame.image.load('./images/rocket.bmp')
        self.rect = self.image.get_rect()
        # Start each new rocket at the center of the screen.
        self.rect.center = self.screen_rect.center
        # Store a decimal value for the rocket's position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        # Movement flags.
        self.moving_right = False
        self.moving_left = False
        self.moving_top = False
        self.moving_bottom = False

    def blitme(self):
        """Draw the rocket at its current position."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Update the rocket's position base on the movement flags."""
        # Update the ship's x and y values.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.rocket_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.rocket_speed
        if self.moving_top and self.rect.top > 0:
            self.y -= self.settings.rocket_speed
        if self.moving_bottom and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.rocket_speed
        # Update the rect object.
        self.rect.x = self.x
        self.rect.y = self.y