from component import MeasurablePositionComponent, MeasurableAngleComponent, TriggerableComponent


class AngleMeter(MeasurablePositionComponent, MeasurableAngleComponent, TriggerableComponent):
    def __init__(self, child, threshold):
        assert isinstance(child, MeasurableAngleComponent)
        assert isinstance(child, MeasurablePositionComponent)
        self.c = child
        self.threshold = threshold

    def get_position(self):
        return self.c.get_position()

    def get_angle(self):
        return self.c.get_angle()

    def is_triggered(self):
        return self.c.get_angle() > self.threshold
