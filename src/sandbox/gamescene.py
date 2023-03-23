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
        # Point1
        p1 = PointMass(self.engine, 100, 100, 20, 0)
        p1.grradius = 16
        p1.mass = 3
        self.engine.add_pointmass(p1)

        # Point2
        p2 = PointMass(self.engine, 100, 200, 0, 0)
        p2.grradius = 16
        p2.mass = 2
        self.engine.add_pointmass(p2)

        # Rigid link
        l = RigidLink(self.engine, p1, p2)
        self.engine.add_rigidlink(l)

    def update(self, tdelta):
        self.engine.update(tdelta)

    def draw(self, sfc):
        sfc.fill(self.backcol)

        for p in self.engine.points:
            pygame.draw.circle(sfc, self.forecol, (p.x, p.y), p.grradius)

        for l in self.engine.links:
            pygame.draw.line(sfc, self.forecol,
                             (l.p1.x, l.p1.y), (l.p2.x, l.p2.y))
