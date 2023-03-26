

class Drone:
    def __init__(self, gamestate, path=None):
        self.gs = gamestate
        self.components = self.load_components(path)
        # TODO: sort components by component type for updating and drawing

    def load_components(self, path):
        self.components = []
        # TODO: load from path

    def update(self, tdelta):
        for comp in self.components:
            comp.update(tdelta)

    def draw(self, sfc):
        for comp in self.components:
            comp.draw(sfc)
