import pygame

pygame.mixer.init()

bullet_sound_original = pygame.mixer.Sound('sounds/bullet1.wav')
bullet_sound_power_up = pygame.mixer.Sound('sounds/bullet2.wav')
explosion_sound = pygame.mixer.Sound('sounds/explosion.wav')

start_screen_sound = pygame.mixer.Sound('sounds/mars.wav')
main_game_sound = pygame.mixer.Sound('sounds/dst-railjet-longseamlessloop.mp3')
level_up_sound = pygame.mixer.Sound('sounds/level-up.mp3')
ship_lost = pygame.mixer.Sound('sounds/ship-lost.flac')