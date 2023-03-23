

class RigidLink:
    def __init__(self, engine, p1, p2, breakcoef=1.5):
        self.engine = engine
        self.p1 = p1
        self.p2 = p2
        self.breakcoef = breakcoef

    def update(self, tdelta):
        pass
