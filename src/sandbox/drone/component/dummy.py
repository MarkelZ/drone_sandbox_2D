from drone.component.component import Component, MeasurablePositionComponent, MeasurableAngleComponent, TriggerableComponent, PointMassComponent


class _Dummy(Component, MeasurablePositionComponent, MeasurableAngleComponent, TriggerableComponent):
    def __init__(self):
        pass

    def update(self, tdelta):
        pass

    def draw(self, sfc):
        pass

    def get_position(self):
        return 0, 0

    def get_angle(self):
        return 0

    def is_triggered(self):
        return False

    def get_draw_priority(self):
        return 7

    def get_update_priority(self):
        return 7


dummy = _Dummy()


def get_dummy():
    return dummy
