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
            self.despawn()

    def draw(self, sfc):
        # Interpolate linearly between color1 and color2 based on timer
        alpha = self.timer / self.duration
        color = [(1 - alpha) * c1 + alpha * c2 for c1,
                 c2 in zip(self.col1, self.col2)]
        pygame.draw.circle(sfc, color, (self.p.x, self.p.y), self.radius)

    def despawn(self):
        self.gs.remove_particle(self)


class FireParticle(Particle):
    def __init__(self, gamescene, x, y, angle):
        speed = random.random() * 7 + 3
        radius = random.randint(4, 8)
        super().__init__(gamescene, x, y,
                         speed * math.cos(angle), speed * math.sin(angle),
                         duration=300, radius=radius,
                         col1=(255, 230, 100), col2=(64, 16, 0))
        self.p.bounce = 0
        self.p.gmul = -0.2
        self.p.drfric = 0.9


class SmokeParticle(Particle):
    def __init__(self, gamescene, x, y):
        speed = random.random() * 15 + 5
        radius = random.randint(8, 16)
        theta = random.random() * -math.pi
        duration = random.randint(400, 900)
        super().__init__(gamescene, x, y,
                         speed * math.cos(theta), speed * math.sin(theta),
                         duration=duration, radius=radius,
                         col1=(156, 132, 128), col2=(64, 64, 96))
        self.p.bounce = 0
        self.p.gmul = -0.1
        self.p.drfric = 0.95
