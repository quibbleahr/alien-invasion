import pygame

class Ship:
    """A class to manage the ship"""

    def __init__(self, ai_game):
        """Initialize ship on screen"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        # load ship image and get rect
        self.image = pygame.image.load('images/pixel_ship.bmp')
        DEFAULT_SHIP_SIZE = (100,100)
        self.image = pygame.transform.scale(self.image, DEFAULT_SHIP_SIZE)
        self.rect = self.image.get_rect()
        # start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
