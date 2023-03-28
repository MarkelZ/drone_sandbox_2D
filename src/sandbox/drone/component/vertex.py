import pygame
from drone.component.component import Component, MeasurablePositionComponent, PointMassComponent
from physics.pointmass import PointMass


class Vertex(Component, MeasurablePositionComponent, PointMassComponent):
    def __init__(self, engine, x, y,):
        self.p = PointMass(engine, x, y)
        self.p.grradius = 4
        self.p.bounce = 0.5

        self.color = (0, 255, 64)

    def update(self, tdelta):
        pass

    def draw(self, camera):
        camera.render_circle(self.color, self.p.x, self.p.y, self.p.grradius)

    def get_draw_priority(self):
        return 1

    def get_update_priority(self):
        return 7

    def get_position(self):
        return (self.p.x, self.p.y)

    def get_pointmass(self):
        return self.p
