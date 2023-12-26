from random import randint
import sys

import pygame

from settings import Settings
from raindrop import Raindrop

class SteadyRain:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Steady Rain")
        self.raindrops = pygame.sprite.Group()

        self._create_rain()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_raindrops()
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
        available_space_y = self.settings.screen_height
        number_rows = available_space_y//(2*raindrop_height)
        # Create the full rain of raindrops.
        for row_number in range(number_rows):
            for raindrop_number in range(number_raindrops_x):
                self._create_raindrop(raindrop_number, row_number)

    def _create_raindrop(self, raindrop_number, row_number):
        """Create a raindrop and place it in the row."""
        raindrop = Raindrop(self)
        raindrop_width, raindrop_height = raindrop.rect.size
        # Insert randomnes in each raindrop's position.
        # The raindrop can be left or right raindrop_width//2.
        # The raindrop can be over or below raindrop_height//2 
        # We use raindrop_width//2 and raindrop_width//2 to avoid overlapping.
        raindrop.rect.x = (raindrop_width + 2*raindrop_width*raindrop_number +
            randint(-raindrop_width//2, raindrop_width//2))
        raindrop.y = (raindrop_height + 2*raindrop_height*row_number +
            randint(-raindrop_height//2, raindrop_height//2))
        raindrop.rect.y = raindrop.y
        self.raindrops.add(raindrop)

    def _update_raindrops(self):
        """
        Drop all raindrops and delete raindrops that have disappear.
        """
        self.raindrops.update()
        # Get rid of raindrops that have disappeared.
        for raindrop in self.raindrops.copy():
            if raindrop.rect.top >= self.settings.screen_height:
                # Store the x position of the deleted raindrop
                new_raindrop_x = raindrop.rect.x
                self.raindrops.remove(raindrop)
                """Create a raindrop and place it in the row."""
                raindrop = Raindrop(self)
                # Here we don't introduce randomnes, because eventually
                # we will have overlappings.
                raindrop_width, raindrop_height = raindrop.rect.size
                raindrop.rect.x = new_raindrop_x
                raindrop.y = raindrop_height
                raindrop.rect.y = raindrop.y
                self.raindrops.add(raindrop)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.raindrops.draw(self.screen)
        pygame.display.flip()


if __name__ == "__main__":
    # Make a game instance, and run the game.
    sr = SteadyRain()
    sr.run_game()
