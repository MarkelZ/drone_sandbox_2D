from drone.drone import Drone
from drone.component.vertex import Vertex
from drone.component.linkcarbon import LinkCarbon


def create_test_drone(engine):
    testdrone = Drone(engine)
    v1 = Vertex(engine, 100, 100)
    v2 = Vertex(engine, 30, 200)
    v3 = Vertex(engine, 170, 200)
    l1 = LinkCarbon(engine, v1, v2)
    l2 = LinkCarbon(engine, v2, v3)
    l3 = LinkCarbon(engine, v3, v1)
    testdrone.components = [v1, v2, v3, l1, l2, l3]
    return testdrone
