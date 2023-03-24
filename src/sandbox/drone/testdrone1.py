import pygame
import math
from drone.drone import Drone
from drone.component.vertex import Vertex
from drone.component.wheel import Wheel
from drone.component.linkcomponent import LinkCarbon
from drone.component.anglemeter import AngleMeter
from drone.component.altimeter import AltiMeter
from drone.component.input import InputComponent
from drone.component.booster import Booster


def create_test_drone(engine):
    # Create the drone
    testdrone = Drone(engine)

    # Input
    k_right = InputComponent(pygame.K_RIGHT)
    k_left = InputComponent(pygame.K_LEFT)
    k_space = InputComponent(pygame.K_SPACE)

    # Components
    v1 = Vertex(engine, 100, 100)
    v2 = Wheel(engine, 30, 200, 50, k_right, k_left)
    v3 = Wheel(engine, 170, 200, 50, k_right, k_left)
    l1 = LinkCarbon(engine, v1, v2)
    l2 = LinkCarbon(engine, v2, v3)
    l3 = LinkCarbon(engine, v3, v1)
    a = AngleMeter(l2, 0.5, 1.5)
    z = AltiMeter(engine, v1, 400)
    b = Booster(l2, k_space, 2, math.pi / 2)

    # Give spin to drone
    v1.p.vx = 30
    v2.p.vy = -30
    v3.p.vy = 30

    # Add components to drone
    testdrone.components = [v1, v2, v3, l1,
                            l2, l3, a, z, b, k_right, k_left, k_space]

    return testdrone
