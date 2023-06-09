import pygame
import math
from drone.drone import Drone
from drone.component.vertex import Vertex
from drone.component.wheel import Wheel
from drone.component.linkcomponent import LinkCarbon
from drone.component.anglemeter import AngleMeter
from drone.component.input import InputComponent
from drone.component.booster import Booster
from drone.component.cannon import Cannon


def create_test_drone(gamestate):
    engine = gamestate.engine

    # Create the drone
    testdrone = Drone(gamestate)

    # Input
    k_right = InputComponent(pygame.K_d)
    k_left = InputComponent(pygame.K_a)
    k_up = InputComponent(pygame.K_w)
    k_attack = InputComponent(pygame.K_SPACE)

    # Components
    v1 = Vertex(engine, 0, 40)
    v2 = Vertex(engine, 160, 0)
    v3 = Vertex(engine, 0, 80)
    v4 = Vertex(engine, 160, 80)
    v5 = Vertex(engine, 400, 40)
    v6 = Vertex(engine, 240, 0)
    v7 = Vertex(engine, 400, 80)
    v8 = Vertex(engine, 240, 80)

    w1 = Wheel(engine, 60, 120, 100, k_right, k_left)
    w2 = Wheel(engine, 340, 120, 100, k_right, k_left)

    l1 = LinkCarbon(engine, v1, v2)
    l2 = LinkCarbon(engine, v2, v4)
    l3 = LinkCarbon(engine, v4, v3)
    l4 = LinkCarbon(engine, v3, v1)
    l5 = LinkCarbon(engine, v3, v2)
    l6 = LinkCarbon(engine, v1, v4)

    l7 = LinkCarbon(engine, v5, v6)
    l8 = LinkCarbon(engine, v6, v8)
    l9 = LinkCarbon(engine, v8, v7)
    l10 = LinkCarbon(engine, v7, v5)
    l11 = LinkCarbon(engine, v7, v6)
    l12 = LinkCarbon(engine, v5, v8)

    l13 = LinkCarbon(engine, v2, v6)
    l14 = LinkCarbon(engine, v4, v8)
    l15 = LinkCarbon(engine, v2, v8)
    l16 = LinkCarbon(engine, v6, v4)

    l17 = LinkCarbon(engine, v3, w1)
    l18 = LinkCarbon(engine, v4, w1)

    l19 = LinkCarbon(engine, v7, w2)
    l20 = LinkCarbon(engine, v8, w2)

    l21 = LinkCarbon(engine, v1, w1)
    l22 = LinkCarbon(engine, v2, w1)
    l23 = LinkCarbon(engine, v5, w2)
    l24 = LinkCarbon(engine, v6, w2)

    a1 = AngleMeter(l13, 0.1, 1.5)
    a2 = AngleMeter(l14, -1.5, -0.1)

    # b1 = Booster(gamestate, l14, k_space, 2, math.pi / 2)

    b4 = Booster(gamestate, l3, k_up, 3, -math.pi / 2)
    b5 = Booster(gamestate, l9, k_up, 3, math.pi / 2)

    b2a = Booster(gamestate, l4, a1, 1, 0)
    b2b = Booster(gamestate, l4, a2, 1, math.pi)
    b3a = Booster(gamestate, l10, a2, 1, 0)
    b3b = Booster(gamestate, l10, a1, 1, math.pi)

    b6 = Booster(gamestate, l2, k_right, 2, math.pi / 2)
    b7 = Booster(gamestate, l8, k_left, 2, -math.pi / 2)

    c1 = Cannon(gamestate, l14, k_attack, 10, math.pi / 2)

    # Add components to drone
    testdrone.components = [v1, v2, v3, v4, v5, v6, v7, v8,
                            w1, w2,
                            l1, l2, l3, l4, l5, l6, l7, l8,
                            l9, l10, l11, l12, l13, l14, l15,
                            l16, l17, l18, l19, l20, l21, l22, l23, l24,
                            a1, a2, b2a, b2b, b3a, b3b, b4, b5, b6, b7, c1,
                            k_right, k_left, k_up, k_attack]

    return testdrone
