import sys

import pygame

from settings import Settings

class Keys():
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize game, and create the game resources."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Keys")

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print(event.key)

    def _update_screen(self):
        """Update images to the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        pygame.display.flip()

if __name__ == "__main__":
    """Make a game instance and run the game."""
    key = Keys()
    key.run_game()