import math
import random
from drone.particle.particle import Particle, SmokeParticle


class Missile(Particle):
    def __init__(self, gamescene, x, y, angle, speed):
        super().__init__(gamescene, x, y,
                         speed * math.cos(angle), speed * math.sin(angle),
                         duration=1000, radius=12,
                         col1=(220, 64, 196), col2=(255, 128, 255))
        self.p.bounce = 0
        self.p.gmul = 0.5
        self.p.drfric = 0.99
        self.p.grfric = 0

    def update(self, tdelta):
        super().update(tdelta)

        if self.timer >= self.duration or self.check_ground():
            self.despawn()

    def check_ground(self):
        dist = self.gs.engine.ground - self.p.y - self.radius
        if dist < 0:
            self.p.y = self.gs.engine.ground + self.radius
            return True
        return False

    def despawn(self):
        expl = Explosion(self.gs, self.p.x, self.p.y, 2000)
        self.gs.add_particle(expl)

        super().despawn()


class Explosion(Particle):
    def __init__(self, gamescene, x, y, power):
        super().__init__(gamescene, x, y,
                         0, 0,
                         duration=80, radius=100,
                         col1=(255, 255, 255), col2=(220, 196, 156))

        self.p.bounce = 0
        self.p.gmul = 0
        self.p.drfric = 0
        self.p.grfric = 0

        self.num_particles = 64
        self.gs.engine.generate_explosion(x, y, power)

    def despawn(self):
        for _ in range(self.num_particles):
            p = SmokeParticle(self.gs, self.p.x, self.p.y)
            self.gs.add_particle(p)

        super().despawn()
