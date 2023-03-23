import pygame
from physics.engine import Engine
from physics.pointmass import PointMass
from physics.rigidlink import RigidLink


class GameScene:
    def __init__(self, game):
        self.game = game
        self.engine = Engine(game.width, game.height)
        self.backcol = (0, 0, 64)
        self.forecol = (0, 255, 128)

        # This is for testing
        self.generate_test()

    def generate_test(self):
        p = PointMass(self.engine, 64, 64)
        self.engine.add_pointmass(p)

    def update(self, tdelta):
        self.engine.update(tdelta)

    def draw(self, sfc):
        sfc.fill(self.backcol)
        for p in self.engine.points:
            pygame.draw.circle(sfc, self.forecol, (p.x, p.y), 16)
