import pygame
from drone.component.component import Component, TriggerableComponent


class InputComponent(Component, TriggerableComponent):
    def __init__(self, key):
        self.triggered = False
        self.key = key

    def update(self, tdelta):
        keys = pygame.key.get_pressed()
        self.triggered = keys[self.key]

    def draw(self, camera):
        pass

    def is_triggered(self):
        return self.triggered

    def get_draw_priority(self):
        return 7

    def get_update_priority(self):
        return 0
