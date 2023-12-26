import json
import sys
from time import sleep

import pygame

from alien import Alien
from bullet import Bullet
from button import Button
from game_stats import GameStats
from scoreboard import Scoreboard
from settings import Settings
from ship import Ship
import sound_effects as se

class SidewaysShooter:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        self.bg_image = pygame.image.load(self.settings.bg_image)
        pygame.display.set_caption('Sideways Shooter')
        # Create an instance to store game statistics,
        #   and create a scoreboard.
        # Highscore file
        self.high_score_file = 'highscore.json'
        try:
            with open(self.high_score_file, 'r') as f:
                high_score = json.load(f)
        except FileNotFoundError:
            high_score = 0
        self.stats = GameStats(self, high_score)
        self.sb = Scoreboard(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        # Make the play and difficulty buttons.
        self.play_button = Button(self, 'Play')
        x = -(self.settings.button_width +
            self.settings.difficulty_button_offset)
        y = -(self.settings.button_height +
            self.settings.difficulty_button_offset)
        self.easy_button = Button(self, 'Easy', x_offset=x, y_offset=y)
        self.fair_button = Button(self, 'Fair', x_offset=0, y_offset=y)
        x = -x
        self.hard_button = Button(self, 'Hard', x_offset=x, y_offset=y)

    def run_game(self):
        """Start the main loop for the game."""
        # Turn on the starting screen sound.
        se.start_screen_sound.play(-1)
        while True:
            self._check_events()
            if self.stats.game_active and not self.stats.game_paused:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        self._check_button_hover(self.play_button)
        difficulty_buttons = (self.easy_button, self.fair_button,
            self.hard_button)
        for button in difficulty_buttons:
                self._check_button_hover(button)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._exit_game()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
                self._set_difficulty(mouse_pos, difficulty_buttons)

    def _check_button_hover(self, button):
        """Checks if there is a mouseover for a button."""
        mouse_pos = pygame.mouse.get_pos()
        if button.rect.collidepoint(mouse_pos):
            button.hover_effect_on()
        else:
            button.hover_effect_off()

    def _exit_game(self):
        """Saves the highscore, and exits the game."""
        with open(self.high_score_file, 'w') as f:
            json.dump(self.stats.high_score, f)
        sys.exit()

    def _set_difficulty(self, mouse_pos, difficulty_buttons):
        """Sets the starting difficulty of the game."""
        for difficulty, button in enumerate(difficulty_buttons):
            button_clicked = button.rect.collidepoint(mouse_pos)
            if (button_clicked and not self.stats.game_active and 
                self.stats.play_button_pressed):
                # Set the selected difficulty.
                self.settings.ship_speed += difficulty
                self.settings.bullet_speed += difficulty
                self.settings.alien_speed += difficulty
                # Activate game
                self.stats.game_active = True
                # Hide the mouse cursor.
                pygame.mouse.set_visible(False)
                # Turn off the starting screen sound.
                se.start_screen_sound.stop()
                # Turn on the main game sound.
                se.main_game_sound.play(-1)
                # If difficulty selected, no need to check others.
                break

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked:
            if self.stats.game_paused:
                self._resume_game()
            elif not self.stats.game_active:
                # Reset the game settings.
                self.settings.initialize_dynamic_settings()
                # Reset the game statistics.
                self.stats.reset_stats()
                self.stats.play_button_pressed = True
                self.sb.prep_images()
                # Clear the reminders on the screen and setup the level
                self._setup_level()

    def _pause_game(self):
        """Pauses the game."""
        self.stats.game_paused = True
        # Appear the mouse cursor.
        pygame.mouse.set_visible(True)

    def _resume_game(self):
        """Resumes a paused game."""
        self.stats.game_paused = False
        # Hide the mouse cursor.
        pygame.mouse.set_visible(False)

    def _setup_level(self, new_level=False):
        """Setup the ship and the fleet for the level."""
        # Get rid of any remaining aliens and bullets.
        self.aliens.empty()
        self.bullets.empty()
        # Create a new fleet.
        self._create_fleet()
        # Center the ship, if necessary.
        if not new_level:
            self.ship.center_ship()

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_UP or event.key == pygame.K_w:
            self.ship.moving_top = True
        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
            self.ship.moving_bottom = True
        elif event.key == pygame.K_SPACE and self.stats.game_active:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            self._exit_game()
        elif event.key == pygame.K_ESCAPE:
            # If game paused resume it, else pause it.
            if self.stats.game_active:
                if self.stats.game_paused:
                    self._resume_game()
                else:
                    self._pause_game()

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
            if self.settings.simple_bullet:
                se.bullet_sound_original.play()
            else:
                se.bullet_sound_power_up.play()

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()
        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.screen.get_rect().right:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions."""
        # Remove any bullets and aliens that have collided.
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens,
            self.settings.simple_bullet, True)
        if collisions:
            for aliens in collisions.values():
                aliens_hit = len(aliens)
                self._power_up_down(aliens_hit) 
                self.stats.score += self.settings.alien_points * aliens_hit
            self.sb.prep_score()
            self.sb.check_high_score()
            se.explosion_sound.play()
        if not self.aliens:
            self._start_new_level()
            se.level_up_sound.play()

    def _power_up_down(self, aliens_hit):
        self.stats.alien_hits += aliens_hit
        if self.stats.alien_hits >= self.settings.bullet_threshold:
            self.stats.alien_hits = 0
            if self.settings.simple_bullet:
                self.settings.simple_bullet = False
            else:
                self.settings.simple_bullet = True

    def _start_new_level(self):
        """Starts a new level, after player has cleared all aliens."""
        # Destroy existing bullets and create new fleet.
        self._setup_level(new_level=True)
        self.settings.increase_speed()
        # Increase level.
        self.stats.level += 1
        self.sb.prep_level()

    def _update_aliens(self):
        """
        Check if the fleet is at an edge,
          then update the position of all aliens on the fleet.
        """
        self._check_fleet_edges()
        self.aliens.update()
        # Look for aliens-ship collisions.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_lost()
        # Look for aliens hitting the left of the screen.
        self._check_aliens_left_side()

    def _check_aliens_left_side(self):
        """Check if any aliens have reached the left of the screen."""
        for alien in self.aliens.sprites():
            if alien.rect.left <= 0:
                # Treat this the same as if the ship got hit.
                self._ship_lost()
                break

    def _ship_lost(self):
        """Respond to the ship being hit by an alien."""
        se.ship_lost.play()
        if self.stats.ships_left > 0:
            # Decrement ships left, and update the scoreboard.
            self.stats.ships_left -= 1
            self.sb.prep_ships()
            # Clear the reminders on the screen and setup the level
            self._setup_level()
            # Pause.
            sleep(0.5)
        else:
            self.stats.play_button_pressed = False
            self.stats.game_active = False
            pygame.mouse.set_visible(True)
            # Turn off the main game sound.
            se.main_game_sound.stop()
            # Turn on the starting screen sound.
            se.start_screen_sound.play(-1)

    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Create an alien and find the number of aliens in a row.
        # Spacing between each alien is equal to one alien width.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        ship_width = self.ship.rect.width
        available_space_x = (self.settings.screen_width - (3*alien_width)
            - ship_width)
        number_aliens_x = available_space_x//(2*alien_width)
        # Determine the number of rows of aliens that fit on the screen.
        available_space_y = (self.settings.screen_height - 2*alien_height
            - self.settings.upper_edge)
        number_rows = available_space_y//(4*alien_height)
        # Create the full fleet of aliens.
        for alien_number in range(number_aliens_x):
            for row_number in range(number_rows):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """Create an alien and place it in the row."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.rect.x = (self.settings.screen_width
            - 2*alien_width*(alien_number+1))
        # [Careful] We update alien.y not alien.rect.y.
        alien.y = (self.settings.upper_edge + alien_height
            + 4*alien_height*row_number)
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Move the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.x -= self.settings.fleet_move_speed
        self.settings.fleet_direction *= -1

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.screen.blit(self.bg_image, (0, 0))
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        # Draw the score information.
        self.sb.show_score()
        # Draw the play button if it wasn't pressed or the game is paused.
        if not self.stats.play_button_pressed or self.stats.game_paused:
            self.play_button.draw_button()
        # Draw the difficulty buttons if the game is inactive.
        if not self.stats.game_active and self.stats.play_button_pressed:
            self.easy_button.draw_button()
            self.fair_button.draw_button()
            self.hard_button.draw_button()
        pygame.display.flip()


if __name__ == "__main__":
    # Make a game instance, and run the game.
    ss = SidewaysShooter()
    ss.run_game()