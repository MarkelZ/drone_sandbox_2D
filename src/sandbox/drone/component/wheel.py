from component import MeasurablePositionComponent, PointMassComponent, TriggerableComponent
from physics.pointmass import PointMass


class Vertex(MeasurablePositionComponent, PointMassComponent, TriggerableComponent):
    def __init__(self, engine, x, y, power, child1, child2):
        # Check that the children have the right type
        assert isinstance(child1, TriggerableComponent)
        assert isinstance(child2, TriggerableComponent)
        self.c1 = child1
        self.c2 = child1

        # Create a pointmass with a wheel's properties
        self.p = PointMass(engine, x, y)
        self.p.bounce = 0.8
        self.p.grradius = 16
        self.p.bounce = 0.8
        self.p.grfric = 0.995
        self.p.mass += 10

        # Power of the wheel
        self.power = power

    def update(self, tdelta):
        if self.c1.is_triggered():
            self.p.vx += self.power
        if self.c2.is_triggered():
            self.p.vx -= self.power

    def get_position(self):
        return (self.p.x, self.p.y)

    def get_pointmass(self):
        return self.p

    def is_triggered(self):
        return self.c1.is_triggered() or self.c2.is_triggered()
