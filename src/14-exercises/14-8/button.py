import pygame.font

class Button:
    """A class to create all the buttons in the game."""

    def __init__(self, ss_game, msg, x_offset='', y_offset=''):
        """Initialize button attributes."""
        self.screen = ss_game.screen
        self.screen_rect = ss_game.screen.get_rect()
        self.settings = ss_game.settings
        self.msg = msg
        # Set the dimnsions and properties of the button.
        width = self.settings.button_width
        height = self.settings.button_height
        self.button_color = self.settings.button_color
        self.text_color = self.settings.text_color
        font_name = self.settings.font_name
        font_size = self.settings.font_size
        self.font = pygame.font.SysFont(font_name, font_size)
        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, width, height)
        self.rect.center = self.screen_rect.center
        if x_offset:
            self.rect.x += x_offset
        if y_offset:
            self.rect.y += y_offset
        # The button message needs to be prepped only once.
        self._prep_msg(self.msg)

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

    def hover_effect_on(self):
        """Turns the hover effect on."""
        self.button_color = self.settings.button_color_hover
        self.text_color = self.settings.text_color_hover
        self._prep_msg(self.msg)

    def hover_effect_off(self):
        """Turns the hover effect on."""
        self.button_color = self.settings.button_color
        self.text_color = self.settings.text_color
        self._prep_msg(self.msg)