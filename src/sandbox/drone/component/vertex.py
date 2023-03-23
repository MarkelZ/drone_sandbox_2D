from component import MeasurablePositionComponent, PointMassComponent
from physics.pointmass import PointMass


class Vertex(MeasurablePositionComponent, PointMassComponent):
    def __init__(self, x, y):
        self.p = PointMass(x, y)
        self.p.grradius = 1
        self.p.bounce = 0.5

    def update(self, tdelta):
        pass

    def get_position(self):
        return (self.p.x, self.p.y)

    def get_pointmass(self):
        return self.p
