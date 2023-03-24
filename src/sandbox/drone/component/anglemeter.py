import pygame
from drone.component.component import Component, MeasurablePositionComponent, MeasurableAngleComponent, TriggerableComponent
from util.draw import draw_rect
from math import pi, sin, cos


class AngleMeter(Component, MeasurablePositionComponent, MeasurableAngleComponent, TriggerableComponent):
    def __init__(self, child, threshold1, threshold2):
        assert isinstance(child, MeasurableAngleComponent)
        assert isinstance(child, MeasurablePositionComponent)
        self.c = child
        self.threshold1 = threshold1  # In radians!
        self.threshold2 = threshold2  # In radians!
        self.triggered = False
        self.angle = 0

        # Render parameters
        self.color_back_off = (64, 200, 64)
        self.color_fore_off = (128, 255, 128)
        self.color_back_on = (200, 64, 64)
        self.color_fore_on = (255, 128, 128)
        self.width = 20
        self.height = 10
        self.radius = (self.height / 2) - 1
        self.maxoffset = self.width / 2 - self.radius - 1

    def update(self, tdelta):
        self.angle = self.c.get_angle()
        self.triggered = self.angle > self.threshold1 and self.angle < self.threshold2

    def draw(self, sfc):
        center_x, center_y = self.c.get_position()
        col_back = self.color_back_on if self.triggered else self.color_back_off
        col_fore = self.color_fore_on if self.triggered else self.color_fore_off
        draw_rect(sfc, center_x, center_y, self.width,
                  self.height, self.angle, col_back)
        offset = -self.maxoffset * sin(self.angle)
        pygame.draw.circle(
            sfc, col_fore, (center_x + offset * cos(self.angle), center_y + offset * sin(self.angle)), self.radius)

    def get_position(self):
        return self.c.get_position()

    def get_angle(self):
        return self.angle

    def is_triggered(self):
        return self.triggered

    def get_draw_priority():
        return 0

    def get_update_priority():
        return 0
