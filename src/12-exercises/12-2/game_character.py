import pygame

class GameCharacter:
    """A class to manage the game character."""

    def __init__(self, gc_game):
        """Initialize the character and set its starting position."""
        self.screen = gc_game.screen
        self.screen_rect = gc_game.screen.get_rect()
        # Load the character image and set its rect.
        self.image = pygame.image.load('./images/spiderman_baby.bmp')
        self.rect = self.image.get_rect()
        # Start each new character at the center of the screen.
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Draw the character at its current location."""
        self.screen.blit(self.image, self.rect)