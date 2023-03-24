import pygame
from drone.component.component import Component, MeasurablePositionComponent, PointMassComponent, TriggerableComponent
from physics.pointmass import PointMass


class Wheel(Component, MeasurablePositionComponent, PointMassComponent, TriggerableComponent):
    def __init__(self, engine, x, y, power, child1, child2):
        # Check that the children have the right type
        assert isinstance(child1, TriggerableComponent)
        assert isinstance(child2, TriggerableComponent)
        self.c1 = child1
        self.c2 = child2

        # Create a pointmass with a wheel's properties
        self.p = PointMass(engine, x, y)
        self.p.grradius = 16
        self.p.bounce = 0.99
        self.p.drfric = 0.99
        self.p.grfric = 0.99
        self.p.mass += 10

        # Power of the wheel
        self.power = power / 100

        # Render settings
        self.color1 = (216, 216, 255)
        self.color2 = (72, 64, 64)
        self.tirewidth = 2

    def update(self, tdelta):
        if self.c1.is_triggered():
            self.p.vx += self.power
        if self.c2.is_triggered():
            self.p.vx -= self.power

    def draw(self, sfc):
        pygame.draw.circle(
            sfc, self.color1, (self.p.x, self.p.y), self.p.grradius)
        pygame.draw.circle(
            sfc, self.color2, (self.p.x, self.p.y), self.p.grradius - 2)

    def get_position(self):
        return (self.p.x, self.p.y)

    def get_pointmass(self):
        return self.p

    def is_triggered(self):
        return self.c1.is_triggered() or self.c2.is_triggered()

    def get_draw_priority():
        return 0

    def get_update_priority():
        return 0
