import pygame
import math
import random
from physics.pointmass import PointMass


class Particle:
    def __init__(self, gamescene, x, y, vx, vy, duration, radius, col1, col2):
        self.gs = gamescene
        self.p = PointMass(self.gs.engine, x, y, vx, vy)

        self.duration = duration
        self.radius = radius
        self.timer = 0
        self.col1 = col1
        self.col2 = col2

    def update(self, tdelta):
        self.timer += tdelta

        if self.timer >= self.duration:
            self.gs.remove_particle(self)

    def draw(self, sfc):
        # Interpolate linearly between color1 and color2 based on timer
        alpha = self.timer / self.duration
        color = [(1 - alpha) * c1 + alpha * c2 for c1,
                 c2 in zip(self.col1, self.col2)]
        pygame.draw.circle(sfc, color, (self.p.x, self.p.y), self.radius)


class FireParticle(Particle):
    def __init__(self, gamescene, x, y, angle):
        speed = 10
        radius = random.randint(4, 8)
        super().__init__(gamescene, x, y,
                         speed * math.cos(angle), speed * math.sin(angle),
                         duration=300, radius=radius,
                         col1=(255, 220, 100), col2=(64, 0, 0))
        self.p.bounce = 0
        self.p.gmul = 0
        self.p.drfric = 0.9
