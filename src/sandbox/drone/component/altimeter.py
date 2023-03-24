from component import MeasurablePositionComponent, TriggerableComponent


class AltiMeter(MeasurablePositionComponent, TriggerableComponent):
    def __init__(self, child, threshold):
        assert isinstance(child, MeasurablePositionComponent)
        self.c = child
        self.threshold = threshold

        self.color_off1 = (0, 255, 128)
        self.color_off2 = (0, 156, 16)
        self.color_on1 = (200, 255, 128)
        self.color_on2 = (200, 156, 16)

    def get_position(self):
        return self.c.get_position()

    def is_triggered(self):
        return self.c.get_position() > self.threshold
