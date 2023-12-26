import sys
from time import sleep

import pygame

from bullet import Bullet
from button import Button
from game_stats import GameStats
from settings import Settings
from ship import Ship
from target import Target

class TargetPractice:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Target Practice')
        self.stats = GameStats(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.target = Target(self)
        # Make the play button.
        self.start_button = Button(self, 'Start')

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._check_target_edges()
                self._update_bullets()
                self.target.update()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_start_button(mouse_pos)

    def _check_start_button(self, mouse_pos):
        """Start a new game when the player clicks Start."""
        button_clicked = self.start_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # Reset the game statistics.
            self.stats.reset_stats()
            self.stats.game_active = True
            # Get rid of any remaining bullets.
            self.bullets.empty()
            # Center the ship and the target.
            self.ship.center_ship()
            self.target.center_target()
            # Hide the mouse cursor.
            pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_UP or event.key == pygame.K_w:
            self.ship.moving_top = True
        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
            self.ship.moving_bottom = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_UP or event.key == pygame.K_w:
            self.ship.moving_top = False
        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
            self.ship.moving_bottom = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()
        # Look for target misses.
        for bullet in self.bullets:
            collision = pygame.sprite.spritecollideany(self.target,
                self.bullets)
            bullet_lost = bullet.rect.left >= self.screen.get_rect().right
            if collision:
                self.bullets.remove(bullet)
                self.stats.hits += 1
                if self.stats.hits >= self.settings.levelup_hits:
                    self.stats.hits = 0
                    self.settings.increase_speed()
            elif not collision and bullet_lost:
                self._target_miss()
                # Get rid of bullets that missed and have disappeared.
                self.bullets.remove(bullet)

    def _target_miss(self):
        """Respond to a bullet missing a target."""
        if self.stats.ships_left > 0:
            # Decrement ships left.
            self.stats.ships_left -= 1
            # Pause.
            sleep(0.1)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _check_target_edges(self):
        """Respond appropriately if the target has reached an edge."""
        if self.target.check_edges():
            self.settings.target_direction *= -1

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.target.draw_target()
        # Draw the Start button, if the game is inactive.
        if not self.stats.game_active:
            # Reset the game settings.
            self.settings.initialize_dynamic_settings()
            self.start_button.draw_button()
        pygame.display.flip()


if __name__ == "__main__":
    # Make a game instance, and run the game.
    tp = TargetPractice()
    tp.run_game()