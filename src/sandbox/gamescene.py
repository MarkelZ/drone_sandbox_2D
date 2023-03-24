import pygame
from physics.engine import Engine
from physics.pointmass import PointMass
from physics.rigidlink import RigidLink
from drone.testdrone import create_test_drone


class GameScene:
    def __init__(self, game):
        self.game = game
        self.engine = Engine(game.width, game.height)
        self.drone = None
        self.backcol = (0, 0, 64)

        # This is for testing
        self.generate_test2()

    def update(self, tdelta):
        self.engine.update(tdelta)
        if self.drone != None:
            self.drone.update(tdelta)

    def draw(self, sfc):
        sfc.fill(self.backcol)
        if self.drone != None:
            self.drone.draw(sfc)

    def generate_test1(self):
        # Point1
        p1 = PointMass(self.engine, 100, 100, 20, 0)
        p1.grradius = 16
        p1.mass = 3

        # Point2
        p2 = PointMass(self.engine, 100, 200, 0, 0)
        p2.grradius = 16
        p2.mass = 2

        # Rigid link
        l = RigidLink(self.engine, p1, p2)

    def generate_test2(self):
        self.drone = create_test_drone(self.engine)
