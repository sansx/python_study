
import pygame
from settings import Settings
from ship import Ship
# from alien import Alien
from pygame.sprite import Group
import game_functions as gf
from game_stats import GameStats
from button import Button

def run_game():
    pygame.init()
    ai_settings = Settings()
    stats = GameStats(ai_settings)
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(ai_settings , screen)
    bullets = Group()
    aliens = Group()
    play_button = Button(ai_settings, screen, "Play")
    gf.create_fleet(ai_settings, screen, ship, aliens)
    
    while True:
        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)
        # gf.update_screen(ai_settings,screen,ship,bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens( ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, stats, screen, ship, aliens, bullets, play_button)

run_game()