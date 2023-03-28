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
            # Accelerate vertex
            self.v.push(-self.power * cos(self.angle),
                        -self.power * sin(self.angle))

            # Spawn fire particles
            x, y = self.position
            mid_x = x + cos(self.angle) * self.height
            mid_y = y + sin(self.angle) * self.height
            for _ in range(self.particle_amount):
                dw = self.particle_dtheta
                theta = self.angle + (random.random() * 2 * dw - dw)
                self.gs.add_particle(FireParticle(
                    self.gs, mid_x, mid_y, theta))

    def draw(self, camera):
        x, y = self.position
        camera.render_triangle(
            self.color, x, y, self.width, self.height, self.angle)

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
