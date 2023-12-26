import sys

import pygame

from rocket import Rocket
from settings import Settings

class RocketGame:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize game, and create the game resources."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Rocket')
        self.rocket = Rocket(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.rocket.update()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                self._check_key_events(event)

    def _check_key_events(self, event):
        """Respond to key events."""
        keypress = False
        if event.type == pygame.KEYDOWN:
            keypress = True
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = keypress
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = keypress
        elif event.key == pygame.K_UP:
            self.rocket.moving_top = keypress
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_bottom = keypress
        if event.key == pygame.K_q:
            sys.exit()

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.rocket.blitme()
        pygame.display.flip()


if __name__ == "__main__":
    """Make a game instance and run the game."""
    rg = RocketGame()
    rg.run_game()