import pygame
from drone.component.component import Component, PushableComponent, MeasurablePositionComponent, MeasurableAngleComponent, TriggerableComponent, PointMassComponent
from math import atan2
from physics.rigidlink import RigidLink


class LinkComponent(Component, PushableComponent, MeasurablePositionComponent, MeasurableAngleComponent, TriggerableComponent):
    def __init__(self, engine, v1, v2, breakcoef, mass, color):
        # Check that the children have the right type
        assert isinstance(v1, PointMassComponent)
        assert isinstance(v2, PointMassComponent)
        p1 = v1.get_pointmass()
        p2 = v2.get_pointmass()

        # Create rigid link and distribute mass of link to children
        self.l = RigidLink(engine, p1, p2, None, breakcoef=breakcoef)
        p1.mass += mass
        p2.mass += mass

        # Foreground color
        self.color = color

    def update(self, tdelta):
        if self.l.isbroken:
            # TODO: break and create particles
            pass

    def draw(self, camera):
        if not self.l.isbroken:
            camera.render_line(self.color, self.l.p1.x, self.l.p1.y,
                               self.l.p2.x, self.l.p2.y, 4)

    def get_position(self):
        return ((self.l.p1.x + self.l.p2.x) / 2, (self.l.p1.y + self.l.p2.y) / 2)

    def get_angle(self):
        return atan2(self.l.p2.y - self.l.p1.y, self.l.p2.x - self.l.p1.x)

    def is_triggered(self):
        return self.l.isbroken

    def push(self, pushx, pushy):
        self.l.p1.push(pushx, pushy)
        self.l.p2.push(pushx, pushy)

    def get_draw_priority(self):
        return 0

    def get_update_priority(self):
        return 0


class LinkCarbon(LinkComponent):
    def __init__(self, engine, v1, v2):
        super().__init__(engine, v1, v2, 1.75, 10, (255, 216, 128))


class LinkAluminum(LinkComponent):
    def __init__(self, engine, v1, v2):
        super().__init__(engine, v1, v2, 2, 20, (128, 216, 255))
