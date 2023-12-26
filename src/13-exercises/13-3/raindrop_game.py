import sys

import pygame

from settings import Settings
from raindrop import Raindrop

class RaindropGame:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Raindrop Game")
        self.raindrops = pygame.sprite.Group()
        self._create_rain()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.raindrops.update()
            self._delete_raindrops()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_q:
            sys.exit()

    def _create_rain(self):
        """Create the rain consisted of raindrops."""
        # Create a raindrop and find the number of raindrops in a row.
        # Spacing between each raindrop is equal to one raindrop width.
        raindrop = Raindrop(self)
        raindrop_width, raindrop_height = raindrop.rect.size
        available_space_x = self.settings.screen_width - 2*raindrop_width
        number_raindrops_x = available_space_x//(2*raindrop_width)
        # Determine the number of rows of raindrops that fit on the screen.
        available_space_y = self.settings.screen_height - 2*raindrop_height
        number_rows = available_space_y//(2*raindrop_height)
        # Create the full rain of raindrops.
        for row_number in range(number_rows):
            for raindrop_number in range(number_raindrops_x):
                self._create_raindrop(raindrop_number, row_number)

    def _create_raindrop(self, raindrop_number, row_number):
        """Create a raindrop and place it in the row."""
        raindrop = Raindrop(self)
        raindrop_width, raindrop_height = raindrop.rect.size
        raindrop.rect.x = raindrop_width + 2*raindrop_width*raindrop_number
        raindrop.y = raindrop_height + 2*raindrop_height*row_number
        raindrop.rect.y = raindrop.y
        self.raindrops.add(raindrop)

    def _delete_raindrops(self):
        # Get rid of the raindrop if it has disappeared.
        for raindrop in self.raindrops.copy():
            if raindrop.rect.top >= self.settings.screen_height:
                self.raindrops.remove(raindrop)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.raindrops.draw(self.screen)
        pygame.display.flip()


if __name__ == "__main__":
    # Make a game instance, and run the game.
    rg = RaindropGame()
    rg.run_game()
