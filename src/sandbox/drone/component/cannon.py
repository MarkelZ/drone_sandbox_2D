import random
import pygame
from drone.component.component import Component, MeasurablePositionComponent, MeasurableAngleComponent, TriggerableComponent, PushableComponent
from drone.particle.particle import FireParticle
from math import sin, cos
from util.draw import draw_rect
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
        self.color = (196, 156, 156)
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
            m = Missile(self.gs, self.position[0],
                        self.position[1], self.angle, 20)
            self.gs.add_particle(m)

            # Apply knockback
            self.v.push(-self.knockback * cos(self.angle),
                        -self.knockback * sin(self.angle))
            self.timer = 0

    def draw(self, sfc):
        # Position of the base of the cannon
        x, y = self.position

        l2 = self.length / 2
        o_x = x + cos(self.angle) * l2
        o_y = y + sin(self.angle) * l2

        # Draw a circle for the base
        draw_rect(sfc, o_x, o_y, self.width,
                  self.length, self.angle, self.color)
        pygame.draw.circle(sfc, self.color, self.position, self.width / 2 - 4)

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
