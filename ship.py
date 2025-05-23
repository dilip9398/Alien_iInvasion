import pygame

class Ship:
    """A class to manage ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position"""
        self.screen = ai_game.Screen
        self.screen_rect = ai_game.Screen.get_rect()

        #Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        #Movement flag ; start with a ship that's not moving.
        self.moving_right = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_right:
            self.rect += 1


    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image,self.rect)

