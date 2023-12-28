# Sideways Shooter Final Version

(3 min. read)

- The game has now a "Play" button, like the Alien Invasion.
- The game speeds up at appropriate points, like the Alien Invasion.
- The player can choose difficulty levels, like in the exercise 14.4.
	- This feature is implemented in `__init__()` method of `button.py` (refactoring), `__init__()` method of `game_stats.py`, `__init__()` method of `settings.py`, and `__init__()`, `__check_events()`, `_set_difficulty()` (new), `_check_play_button()`, `_ship_hit()` (renamed to `_ship_lost()`), `_update_screen()` methods of `sideways_shooter_final_version.py`.
- The game has a scoring system, like the Alien Invasion.
	- `scoreboard.py` was refactored, to receive the score color and font properties from `settings.py`
	- Additional refactoring was needed to depict the score at the top of screen. Now, the upper edge is not at the top of the window, but at the top of the window + 180px. This value is set at the `settings.py`; whereas, `ship.py`, `alien.py`, and `sideways_shooter_final_version.py` were refactored accordingly.
- The all-time high score is stored to .json file, like in the exercise 14.5.
	- This feature is implemented in `__init__()` method of `game_stats.py`, and `__init__()`, `_check_events()` (refactoring), `_exit_game()` (new) and `_check_keydown_events()` (refactoring) methods of `sideways_shooter_final_version.py`.
- The game was refactored, like in the exercise 14.6.
	- In the `scoreboard.py`, `prep_images()` methods was implemented, and `__init__()` method was refactored accordingly.
	- In the `sideways_shooter_final_version.py`, `_check_bullet_alien_collisions()` and `_check_play_button()` methods were refactored, and `_start_new_level()` (new) and `_setup_level()` (new) methods were implemented.
- The ship can also be moved with W and S keys (this was implemented in a previous version of Sideways Shooter).
	- This feature is implemented in `_check_keydown_events()` and `_check_keyup_events()` methods of `sideways_shooter_final_version.py`.
- The game has an image as background. Both the ship and the aliens images have transparent background. All images were downloaded from [Pixabay](https://pixabay.com/).
	- This feature is implemented in `__init__()` method of `settings.py`, and `__init__()` and `_update_screen()` methods of `sideways_shooter_final_version.py`.
- The buttons have hover effect.
	- This feature is implemented in `__init__()` method of `settings.py`; `__init__()` (refactoring), `hover_effect_on()` (new), and `hover_effect_off()` (new) methods of `button.py`; and `_check_events()` (refactoring), `_set_difficulty()` (refactoring), and `_check_button_hover()` (new) methods of `sideways_shooter_final_version.py`.
- The game powers up bullets by making them piercing shots after ten alien hits, and powers down bullets to the original effect (both bullet and alien are removed on collision) after at least ten hits with the powered up bullets. The implementation is similar to those in exercise 14.7, but the bullet's power-up has a different effect. The bullet loses its piercing effect once it hits ten aliens, even if it is midair.
	- The method implementing this feature is named `_power_up_down()` and is located in `expanding_the_game.py`. Appropriate changes also took place in `game_stats.py`, `settings.py`, and `bullet.py`.
- The game has sounds, like in the exercise 14.7.
- The issue with the shooting when the game is not active was solved.
	- The method implementing this feature is `_check_keydown_events()` (refactored) in `sideways_shooter_final_version.py`
- In `sideways_shooter_final_version.py`, the method `_ship_hit()` was renamed to `_ship_lost()`, since it is used both when an alien hits the ship and when an alien reaches the left edge of the screen. In both cases, the player loses a ship (if the player has any ships) or the game (if the player has no ships left).
- The game can be paused by pressing the ESC key and resumed either i) by pressing the ESC key again; or iii) by clicking the 'Play' button. The functionality and implementation is like in the exercise 14.7, but without the spacebar key functionality.

**Note:** The directory `/poc` contains Proof-of-Concept images and a video of the game running.