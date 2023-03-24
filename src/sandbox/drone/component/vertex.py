import pygame
from drone.component.component import Component, MeasurablePositionComponent, PointMassComponent
from physics.pointmass import PointMass


class Vertex(Component, MeasurablePositionComponent, PointMassComponent):
    def __init__(self, engine, x, y,):
        self.p = PointMass(engine, x, y)
        self.p.grradius = 4
        self.p.bounce = 0.5

        self.color = (0, 255, 64)

    def add_to_engine(self, engine):
        engine.add_pointmass(self.p)

    def update(self, tdelta):
        pass

    def draw(self, sfc):
        pygame.draw.circle(
            sfc, self.color, (self.p.x, self.p.y), self.p.grradius)

    def get_draw_priority():
        return 0

    def get_update_priority():
        return 0

    def get_position(self):
        return (self.p.x, self.p.y)

    def get_pointmass(self):
        return self.p
