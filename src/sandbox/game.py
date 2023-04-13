# Hide pygame support prompt
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'

# Imports
from gamescene import GameScene
import pygame


class Game:
    def __init__(self, width, height):
        # Fields
        self.width = width
        self.height = height
        self.FPS = 60
        self.spt = 1. / self.FPS
        self.mspt = int(1000. * self.spt)

        # Initialize and setup pygame
        pygame.init()
        self.win = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Drone Sandbox 2D')

        # Gameplay scene
        self.scene = GameScene(self)

    # Run main game loop
    def run(self):
        # Whether game is running
        running = True

        # Main loop
        while running:
            pygame.time.delay(self.mspt)

            # Update and draw game objects
            if running:
                self.update()
                self.draw()

            # Process events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

    # Update call
    def update(self):
        self.scene.update(self.mspt)

    # Draw call
    def draw(self):
        self.scene.draw(self.win)
        pygame.display.update([self.win.get_rect()])
