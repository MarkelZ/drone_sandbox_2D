import numpy as np
import pygame
from drone.component.component import Component, MeasurablePositionComponent, TriggerableComponent


class AltiMeter(Component, MeasurablePositionComponent, TriggerableComponent):
    def __init__(self, engine, child, threshold):
        assert isinstance(child, MeasurablePositionComponent)
        self.c = child
        self.engine = engine
        self.threshold = threshold
        self.triggered = False
        self.altitude = 0

        self.color_back_off = (64, 200, 64)
        self.color_fore_off = (128, 255, 128)
        self.color_back_on = (200, 64, 64)
        self.color_fore_on = (255, 128, 128)
        self.width = 10
        self.height = 10

    def update(self, tdelta):
        _, y = self.c.get_position()
        self.altitude = self.engine.ground - y
        self.triggered = self.altitude > self.threshold

    def draw(self, sfc):
        center_x, center_y = self.c.get_position()

        # Corners of the rectangle
        h_half = self.height / 2
        w_half = self.width / 2
        x1, y1 = center_x - w_half, center_y - h_half

        col_back = self.color_back_on if self.triggered else self.color_back_off
        col_fore = self.color_fore_on if self.triggered else self.color_fore_off

        sigmoid = 2.0 / (1.0 +
                         np.exp(-2 * self.altitude / self.engine.ground)) - 1
        offset = max(sigmoid, 0.0) * self.height
        pygame.draw.rect(sfc, col_fore, pygame.Rect(
            x1, y1, self.width, self.height))
        pygame.draw.rect(sfc, col_back, pygame.Rect(
            x1, y1, self.width, self.height - offset))

    def get_position(self):
        return self.c.get_position()

    def is_triggered(self):
        return self.triggered

    def get_draw_priority():
        return 0

    def get_update_priority():
        return 0
