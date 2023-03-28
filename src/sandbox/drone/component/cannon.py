import random
import pygame
from drone.component.component import Component, MeasurablePositionComponent, MeasurableAngleComponent, TriggerableComponent, PushableComponent
from drone.particle.particle import FireParticle
from math import sin, cos
from drone.particle.projectile import Missile


class Cannon(Component, MeasurablePositionComponent, MeasurableAngleComponent, TriggerableComponent):
    def __init__(self, gamestate, v, t, power, angle):
        # Check that the children have the right type
        assert isinstance(v, PushableComponent)
        assert isinstance(v, MeasurablePositionComponent)
        assert isinstance(v, MeasurableAngleComponent)
        assert isinstance(t, TriggerableComponent)
        self.v = v
        self.t = t
        self.gs = gamestate

        # Cannon parameters
        self.power = power
        self.firerate = 500
        self.knockback = 10
        self.timer = 0
        self.relangle = angle  # Angle relative to v
        self.angle = self.v.get_angle() + self.relangle
        self.position = self.v.get_position()
        self.triggered = False

        # Render settings
        self.color = (156, 198, 220)
        self.width = 30
        self.length = 20

    def update(self, tdelta):
        self.angle = self.v.get_angle() + self.relangle
        self.position = self.v.get_position()

        self.timer += tdelta
        if self.timer > self.firerate:
            self.triggered = self.t.is_triggered()
        else:
            self.triggered = False

        if self.triggered:
            # Shoot missile
            x, y = self.position
            mx = x + cos(self.angle) * self.length
            my = y + sin(self.angle) * self.length
            m = Missile(self.gs, mx, my, self.angle, 50)
            self.gs.add_particle(m)

            # Apply knockback
            self.v.push(-self.knockback * cos(self.angle),
                        -self.knockback * sin(self.angle))
            self.timer = 0

    def draw(self, camera):
        # Position of the base of the cannon
        x, y = self.position

        l2 = self.length / 2
        o_x = x + cos(self.angle) * l2
        o_y = y + sin(self.angle) * l2

        # Draw a circle for the base
        camera.render_rect(self.color, o_x, o_y, self.width,
                           self.length, self.angle)
        camera.render_circle(self.color, x, y, self.width / 2 - 4)

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
