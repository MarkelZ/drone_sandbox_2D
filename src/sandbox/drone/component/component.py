import abc


class Component(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def update(self, tdelta):
        pass

    @abc.abstractmethod
    def draw(self, camera):
        pass

    @abc.abstractmethod
    def get_draw_priority():
        return 0

    @abc.abstractmethod
    def get_update_priority():
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


class PushableComponent(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def push(self, pushx, pushy):
        pass
