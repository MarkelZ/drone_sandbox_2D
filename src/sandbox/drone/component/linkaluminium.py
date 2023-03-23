from component import MeasurablePositionComponent, MeasurableAngleComponent, TriggerableComponent, PointMassComponent
from math import atan2
from physics.rigidlink import RigidLink


class LinkCarbon(MeasurablePositionComponent, MeasurableAngleComponent, TriggerableComponent):
    def __init__(self, v1, v2):
        assert isinstance(v1, PointMassComponent)
        assert isinstance(v2, PointMassComponent)
        p1 = v1.get_pointmass()
        p2 = v2.get_pointmass()
        self.l = RigidLink(p1, p2, None, breakcoef=2.5)
        p1.mass += 20
        p2.mass += 20

    def update(self, tdelta):
        if self.l.isbroken:
            # TODO: break and create particles
            pass

    def get_position(self):
        return ((self.l.p1.x + self.l.p2.x) / 2, (self.l.p1.y + self.l.p2.y) / 2)

    def get_angle(self):
        return atan2(self.l.p2.x - self.l.p1.x, self.l.p2.y - self.l.p1.y)

    def is_triggered(self):
        return self.l.isbroken
