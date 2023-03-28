import random
import pygame
from physics.engine import Engine
from physics.pointmass import PointMass
from physics.rigidlink import RigidLink
from drone.testdrone2 import create_test_drone
from drone.drone import Drone
from camera import Camera
from background import Background


class GameScene:
    def __init__(self, game):
        self.game = game
        self.engine = Engine(game.width, game.height)
        self.camera = Camera(game.width, game.height)
        self.background = Background((0, 0, 64),
                                     (64, 64, 128),
                                     (0, 64, 0),
                                     (64, 128, 64),
                                     100)
        self.drone = None
        self.backcol = (128, 0, 128)

        self.particles = []
        self.particles_to_add = []
        self.particles_to_remove = []

        # self.generate_test2()
        self.drone = Drone(self, 'saves/drone1.json')

        self.camera.attach_to_component(self.drone.get_camera_component())

    def update(self, tdelta):
        self.engine.update(tdelta)
        if self.drone != None:
            self.drone.update(tdelta)

        for p in self.particles:
            p.update(tdelta)

        self.camera.update(tdelta)

        self.particles += self.particles_to_add
        self.particles_to_add = []

        self.particles = [
            p for p in self.particles if p not in self.particles_to_remove]
        self.particles_to_remove = []

    def draw(self, sfc):
        sfc.fill(self.backcol)

        self.camera.set_surface(sfc)
        self.background.draw(self.camera)

        if self.drone != None:
            self.drone.draw(self.camera)

        for p in self.particles:
            p.draw(self.camera)

    def add_particle(self, p):
        self.particles_to_add.append(p)

    def remove_particle(self, p):
        self.particles_to_remove.append(p)

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
        self.drone = create_test_drone(self)
