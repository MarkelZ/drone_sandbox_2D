import random
import pygame
from drone.component.component import Component, MeasurablePositionComponent, MeasurableAngleComponent, TriggerableComponent, PushableComponent
from drone.particle.particle import FireParticle
from math import sin, cos


class Booster(Component, MeasurablePositionComponent, MeasurableAngleComponent, TriggerableComponent):
    def __init__(self, gamestate, v, t, power, angle):
        # Check that the children have the right type
        assert isinstance(v, PushableComponent)
        assert isinstance(v, MeasurablePositionComponent)
        assert isinstance(v, MeasurableAngleComponent)
        assert isinstance(t, TriggerableComponent)
        self.v = v
        self.t = t
        self.gs = gamestate

        # Booster parameters
        self.power = power
        self.relangle = angle  # Angle relative to v
        self.angle = self.v.get_angle() + self.relangle
        self.position = self.v.get_position()
        self.triggered = False

        # Render settings
        self.color = (200, 200, 255)
        self.width = 30
        self.height = 20
        self.particle_dtheta = 0.5
        self.particle_amount = 1

    def update(self, tdelta):
        self.angle = self.v.get_angle() + self.relangle
        self.position = self.v.get_position()
        self.triggered = self.t.is_triggered()

        if self.triggered:
            self.v.push(-self.power * cos(self.angle),
                        -self.power * sin(self.angle))

    def draw(self, sfc):
        # Position of the topmost point of the booster
        x = self.position[0]
        y = self.position[1]

        # Cosine and sine of the angle
        cos_a = cos(self.angle)
        sin_a = sin(self.angle)

        # Midpoint of the base of the booster
        mid_x = x + cos_a * self.height
        mid_y = y + sin_a * self.height

        # Vector perpendicular to the height / parallel to the base
        perp_x = -sin_a * self.width / 2
        perp_y = cos_a * self.width / 2

        # Set of points of the booster polygon
        points = [(x, y),
                  (mid_x + perp_x, mid_y + perp_y),
                  (mid_x - perp_x, mid_y - perp_y)]

        # Draw polygon
        pygame.draw.polygon(
            sfc, self.color, points)

        # Generate fire particle if triggered
        if self.triggered:
            for _ in range(self.particle_amount):
                dw = self.particle_dtheta
                theta = self.angle + (random.random() * 2 * dw - dw)
                self.gs.add_particle(FireParticle(
                    self.gs, mid_x, mid_y, theta))

    def get_position(self):
        return self.position

    def get_angle(self):
        return self.angle

    def is_triggered(self):
        return self.triggered

    def get_draw_priority():
        return 0

    def get_update_priority():
        return 0
