import pygame
from pygame.sprite import Sprite

from game_stats import GameStats

class Ship(Sprite):

    def __init__(self, ai_settings, screen):
        """Initialize the ship and at its starting position."""
        super().__init__()

        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        self.ai_settings = ai_settings

        statsa = GameStats(ai_settings)
        #Load the ship image according to levels and get its rect.
        if statsa.level > 1 and statsa.level <= 7:
            self.image = pygame.image.load('images/shipa.png')
        elif statsa.level > 7 and statsa.level < 11:
            self.image = pygame.image.load('images/shipb.png')
        else:
            self.image = pygame.image.load('images/shipc.png')

        self.image = pygame.transform.scale(self.image, (60,60))
        self.rect = self.image.get_rect()


        #Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)

        #Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        #Update the ship's center value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        
        #Update rect object from sef.center.
        self.rect.centerx = self.center

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen."""
        self.center = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
