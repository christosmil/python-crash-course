# Expansions

(2 min. read)

- The game can start both by clicking the "Play" button and by pressing the spacebar key.
	- The method implementing this feature is named `_activate_game()` and is located in `expanding_the_game.py`. Most of the necessary functionality was already in the `_check_play_button()` method, so I refactored the code accordingly.
	- This expansion, also, solves the following issue: previously, when you pressed the spacebar key during the start screen (visible "Play" button), the ship used to fire a bullet that stood at the top of the ship's rectangle.
- The game powers up bullets by increasing their width after ten alien hits, and powers down bullets to the original width after at least ten hits with the powered up bullets. The wider bullets can be used to player's advantage, e.g., the player may have hit nine aliens with the previous powered up bullets and with the last powered up bullet the player may manage to hit two aliens.
	- The method implementing this feature is named `_power_up_down()` and is located in `expanding_the_game.py`. Appropriate changes also took place in `game_stats.py` and `settings.py`.
- The game has sounds. The sounds are implemented with the guides found in the [book's online resources](https://ehmatthes.github.io/pcc_2e/beyond_pcc/ai_player/#adding-sound). On top of the guides' functionalities, I have added the following sound-related functionalities:
	- Different sounds for original and powered up bullets.
	- Sound for the 'Play' screen (in loop).
	- Sound for the main game (in loop).
	- Sound for moving to the next level.
	- Sound for losing a ship either by an alien hitting the ship, or by an alien reaching the ground. 
- The game can be paused by pressing the ESC key and resumed either i) by pressing the ESC key again; ii) by pressing the spacebar key; or iii) by clicking the 'Play' button.
	- Two extra methods were implemented for this feature, `_pause_game()` and `_resume_game()`, both located in `expanding_the_game.py`. An additional flag was used, the variable `game_paused` located in `game_stats.py`. Conditionals were refactored in `run_game()`, `_check_play_button()`, `_check_keydown_events()`, and `_update_screen()`.