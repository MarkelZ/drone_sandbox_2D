import json
from drone.component.dummy import get_dummy
from drone.component.vertex import Vertex
from drone.component.wheel import Wheel
from drone.component.linkcomponent import LinkCarbon
from drone.component.anglemeter import AngleMeter
from drone.component.altimeter import AltiMeter
from drone.component.input import InputComponent
from drone.component.booster import Booster
from drone.component.cannon import Cannon


class Drone:
    def __init__(self, gamestate, path=None):
        self.gs = gamestate
        self.load_components(path)

        # Sort components by uptade and draw priorities
        comp_update_list = [(comp, comp.get_update_priority())
                            for comp in self.components]
        comp_update_list.sort(key=lambda x: x[1])
        self.comp_update_list = [x[0] for x in comp_update_list]

        comp_draw_list = [(comp, comp.get_draw_priority())
                          for comp in self.components]
        comp_draw_list.sort(key=lambda x: x[1])
        self.comp_draw_list = [x[0] for x in comp_draw_list]

    def update(self, tdelta):
        for comp in self.comp_update_list:
            comp.update(tdelta)

    def draw(self, sfc):
        for comp in self.comp_draw_list:
            comp.draw(sfc)

    def get_camera_component(self):
        return self.camera_component

    def load_components(self, path):
        self.camera_component = None
        if path == None:
            self.components = []
            return

        gs = self.gs
        engine = gs.engine

        dummy = get_dummy()

        with open(path) as f:
            data = json.load(f)
            components = {'dummy': dummy}
            for label, args in data.items():
                comp_type = args['type']
                if comp_type == 'InputComponent':
                    value = args['value']
                    components[label] = InputComponent(value)
                elif comp_type == 'Vertex':
                    x = args['x']
                    y = args['y']
                    components[label] = Vertex(engine, x, y)
                elif comp_type == 'Wheel':
                    x = args['x']
                    y = args['y']
                    power = args['power']

                    child1_label = args['child1']
                    child2_label = args.get('child2', 'dummy')
                    child1 = components[child1_label]
                    child2 = components[child2_label]

                    components[label] = Wheel(
                        engine, x, y, power, child1, child2)
                elif comp_type == 'LinkCarbon':
                    v1_label = args['v1']
                    v2_label = args['v2']
                    v1 = components[v1_label]
                    v2 = components[v2_label]

                    components[label] = LinkCarbon(engine, v1, v2)
                elif comp_type == 'AngleMeter':
                    threshold1 = args['threshold1']
                    threshold2 = args['threshold2']

                    child_label = args['child']
                    child = components[child_label]

                    components[label] = AngleMeter(
                        child, threshold1, threshold2)
                elif comp_type == 'AltiMeter':
                    threshold = args['threshold']

                    child_label = args['child']
                    child = components[child_label]

                    components[label] = AltiMeter(engine, child, threshold)
                elif comp_type == 'Booster':
                    power = args['power']
                    angle = args['angle']

                    v_label = args['v']
                    t_label = args.get('t', 'dummy')
                    v = components[v_label]
                    t = components[t_label]

                    components[label] = Booster(gs, v, t, power, angle)
                elif comp_type == 'Cannon':
                    power = args['power']
                    angle = args['angle']

                    v_label = args['v']
                    t_label = args.get('t', 'dummy')
                    v = components[v_label]
                    t = components[t_label]

                    components[label] = Cannon(gs, v, t, power, angle)
                elif comp_type == 'CameraComponent':
                    child_label = args['child']
                    self.camera_component = components[child_label]
                else:
                    assert False, 'Unknown component type \'' + \
                        comp_type + '\' when parsing file \'' + path + '\'.'

        self.components = [c for c in components.values()]
