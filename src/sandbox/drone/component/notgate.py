from component import MeasurablePositionComponent, TriggerableComponent


class NotGate(MeasurablePositionComponent, TriggerableComponent):
    def __init__(self, child):
        assert isinstance(child, MeasurablePositionComponent)
        assert isinstance(child, TriggerableComponent)
        self.c = child

    def get_position(self):
        return self.c.get_position()

    def is_triggered(self):
        return not self.c.is_triggered()
