import pygame


class GameScene:
    def __init__(self, game):
        self.game = game

    def update(self, tdelta):
        pass

    def draw(self, sfc):
        # Test
        sfc.fill((0, 0, 64))
        pygame.draw.rect(sfc, (0, 255, 128), (100, 100, 64, 64), 4)
