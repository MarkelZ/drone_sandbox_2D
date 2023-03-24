from drone.drone import Drone
from drone.component.vertex import Vertex
from drone.component.linkcomponent import LinkCarbon
from drone.component.anglemeter import AngleMeter


def create_test_drone(engine):
    testdrone = Drone(engine)
    v1 = Vertex(engine, 100, 100)
    v1.p.vx = 30  # test
    v2 = Vertex(engine, 30, 200)
    v2.p.vy = -30  # test
    v3 = Vertex(engine, 170, 200)
    v3.p.vy = 30  # test
    l1 = LinkCarbon(engine, v1, v2)
    l2 = LinkCarbon(engine, v2, v3)
    l3 = LinkCarbon(engine, v3, v1)
    a = AngleMeter(l2, 0.5)
    testdrone.components = [v1, v2, v3, l1, l2, l3, a]
    return testdrone
