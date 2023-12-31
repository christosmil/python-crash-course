import pygame.font

class Button:
    """A class to create all the buttons in the game."""

    def __init__(self, ai_game, msg):
        """Initialize button attributes."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        # Set the dimnsions and properties of the button.
        self.width = self.settings.button_width
        self.height = self.settings.button_height
        self.button_color = self.settings.button_bg_color
        self.text_color = self.settings.button_txt_color
        font_name = self.settings.button_font_name
        font_size = self.settings.button_font_size
        self.font = pygame.font.SysFont(font_name, font_size)
        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        # The button message needs to be prepped only once.
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color,
            self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Draw blank button and then draw message."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
