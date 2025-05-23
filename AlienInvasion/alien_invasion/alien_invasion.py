import pygame
from . import game_functions as gf

from .settings import Settings
from .ship import Ship
from .game_stats import GameStats
from .button import Button
from .scoreboard import ScoreBoard

from pygame.sprite import Group

def run_game():
    pygame.init()
    pygame.display.set_caption("Invasão Alienígena")

    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

    play_button = Button(ai_settings, screen, "Jogar")

    ship = Ship(ai_settings, screen)
    stats = GameStats(ai_settings)
    sb = ScoreBoard(ai_settings, screen, stats)

    bullets = Group()
    aliens = Group()

    gf.create_fleet(ai_settings, screen, ship, aliens)

    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)