import pygame
from pygame.sprite import Group

from setttings import Settings
from game_stats import GameStats
from score import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf
from alien import Alien

def run_game():
    #Initialize game and create a screen object  
    pygame.init()
    # clock = pygame.time.Clock()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))


    bg = pygame.image.load('images/spacea.png')
    # bg = pygame.image.load('images/spaceb.png')
    bg= pygame.transform.scale(bg, (1250, 700))
    
    pygame.display.set_caption("The Invaison")

    #Make the Play Button
    play_button = Button(ai_settings, screen, 'Play')

    #Create the instance to score game statistics and create a scoreboard.
    stats = GameStats(ai_settings)
    scoreb = Scoreboard(ai_settings, screen, stats)

    #Make a ship, a group to store bullets in, and a group of aliens.
    ship = Ship(ai_settings, screen )
    bullets = Group()

    #Make group to store aliens and the bullets.
    aliens = Group()
    alien_bullets = Group()



    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    #Start the main loop for the game
    while True:
        gf.check_events(ai_settings, screen, stats, scoreb, play_button, ship, aliens, bullets, alien_bullets)
        
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, scoreb, ship, aliens, bullets, alien_bullets)
            gf.update_alien_bullets(alien_bullets)
            gf.update_aliens(ai_settings, stats,  scoreb, screen, ship, aliens, bullets, alien_bullets)
            gf.update_ship(ai_settings, stats, scoreb, screen, ship, aliens, bullets, alien_bullets)

        gf.update_screen(ai_settings, screen, bg, stats, scoreb, ship, aliens, bullets, play_button, alien_bullets)
        # clock.tick(100)

run_game()
  