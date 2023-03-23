from component import MeasurablePositionComponent, TriggerableComponent


class AltiMeter(MeasurablePositionComponent, TriggerableComponent):
    def __init__(self, child, threshold):
        assert isinstance(child, MeasurablePositionComponent)
        self.c = child
        self.threshold = threshold

    def get_position(self):
        return self.c.get_position()

    def is_triggered(self):
        return self.c.get_position() > self.threshold
