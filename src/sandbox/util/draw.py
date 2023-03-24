import pygame
import math


def draw_rect(sfc, center_x, center_y, width, height, angle, color):
    """
    Draw a rectangle with the given center, width, height, and angle, on the given Pygame screen
    with the given color.
    """
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
        sfc, color, [(x1, y1), (x2, y2), (x3, y3), (x4, y4)])
