import abc


class Component():
    def update(self, tdelta):
        pass

    def draw(self, sfc):
        pass

    def get_layer():
        return 0


class PointMassComponent(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_pointmass(self):
        pass


class MeasurableAngleComponent(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_angle(self):
        pass


class MeasurablePositionComponent(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_position(self):
        pass


class TriggerableComponent(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def is_triggered(self):
        pass
