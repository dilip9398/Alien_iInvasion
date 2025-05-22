import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock() # Set the Frame rote of the games. Ii will run 60 frames per second.
        self.setting = Settings()


        self.Screen = pygame.display.set_mode((self.setting.screen_width, self.setting.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        self.Screen.fill(self.setting.bg_color)
        self.ship.blitme()

        # Make the most recently draw screen visible.
        pygame.display.flip()


if __name__ == '__main__':
    #make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()