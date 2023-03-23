import pygame
from gamescene import GameScene


class Game:
    def __init__(self, width, height):
        # Fields
        self.WIDTH = width
        self.HEIGHT = height
        self.FPS = 60
        self.mspt = int(1000. / self.FPS)

        # Initialize and setup pygame
        pygame.init()
        self.win = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption('Neon ninja')

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
        pygame.display.flip()
