import math

import pygame
from drone.component.component import MeasurablePositionComponent


class Camera:
    def __init__(self, width, height):
        self.comp = None
        self.x = 0
        self.y = 0
        self.width = width
        self.height = height
        self.half_width = width / 2
        self.half_height = height / 2

        self.vx = 0
        self.vy = 0
        self.max_dv = 10  # Maximum acceleration
        self.dv_coef = 0.5
        self.halt = 0.9

    def set_surface(self, sfc):
        self.sfc = sfc

    def attach_to_component(self, comp):
        assert isinstance(comp, MeasurablePositionComponent)
        self.x, self.y = comp.get_position()
        self.vx = 0
        self.vy = 0
        self.comp = comp

    def update(self, tdelta):
        x, y = self.comp.get_position()
        self.x, self.y = x - self.half_width, y - self.half_height

    def update_old(self, tdelta):
        x, y = self.comp.get_position()
        dx = x - self.x - self.half_width
        dy = y - self.y - self.half_height
        dist = math.sqrt(dx * dx + dy * dy)

        if dist <= 0.01:
            return

        dv = min(dist * self.dv_coef, self.max_dv)
        normal_dx = dx / dist
        normal_dy = dy / dist

        self.vx += normal_dx * dv
        self.vy += normal_dy * dv
        self.vx *= self.halt
        self.vy *= self.halt

        self.x += self.vx
        self.y += self.vy

    def world_to_view(self, x, y):
        return x - self.x, y - self.y

    def render_circle(self, color, center_x, center_y, radius):
        x, y = self.world_to_view(center_x, center_y)

        # There is a pygame bug that does not let draw
        # circles with negative coordinates :/
        if x < 0 or y < 0:
            return

        pygame.draw.circle(self.sfc, color, (x, y), radius)

    def render_line(self, color, x1, y1, x2, y2, width):
        x1, y1 = self.world_to_view(x1, y1)
        x2, y2 = self.world_to_view(x2, y2)
        pygame.draw.line(self.sfc, color, (x1, y1), (x2, y2), width)

    def render_axis_aligned_rect(self, color, x, y, width, height):
        x, y = self.world_to_view(x, y)
        pygame.draw.rect(self.sfc, color, pygame.Rect(x, y, width, height))

    def render_rect(self, color, center_x, center_y, width, height, angle):
        center_x, center_y = self.world_to_view(center_x, center_y)

        half_width = width / 2.0
        half_height = height / 2.0
        cos_ang = math.cos(-angle)
        sin_ang = math.sin(-angle)

        # Compute the coordinates of the corners of the rectangle
        x1 = center_x - half_width * cos_ang - half_height * sin_ang
        y1 = center_y + half_width * sin_ang - half_height * cos_ang
        x2 = center_x + half_width * cos_ang - half_height * sin_ang
        y2 = center_y - half_width * sin_ang - half_height * cos_ang
        x3 = center_x + half_width * cos_ang + half_height * sin_ang
        y3 = center_y - half_width * sin_ang + half_height * cos_ang
        x4 = center_x - half_width * cos_ang + half_height * sin_ang
        y4 = center_y + half_width * sin_ang + half_height * cos_ang

        # Draw the rectangle using pygame.draw.polygon
        pygame.draw.polygon(
            self.sfc, color, [(x1, y1), (x2, y2), (x3, y3), (x4, y4)])

    def render_triangle(self, color, top_x, top_y, width, height, angle):
        # Top vertex of the triangle
        x, y = self.world_to_view(top_x, top_y)

        # Cosine and sine of the angle
        cos_a = math.cos(angle)
        sin_a = math.sin(angle)

        # Midpoint of the base of the triangle
        mid_x = x + cos_a * height
        mid_y = y + sin_a * height

        # Vector perpendicular to the height / parallel to the base
        perp_x = -sin_a * width / 2
        perp_y = cos_a * width / 2

        # Set of points of the triangle
        points = [(x, y),
                  (mid_x + perp_x, mid_y + perp_y),
                  (mid_x - perp_x, mid_y - perp_y)]

        # Draw polygon
        pygame.draw.polygon(self.sfc, color, points)
