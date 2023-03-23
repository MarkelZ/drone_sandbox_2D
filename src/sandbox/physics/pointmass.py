

class PointMass:
    def __init__(self, engine, x=0, y=0):
        # Parameters
        self.engine = engine
        self.x = x          # X position
        self.y = y          # Y position

        # Physics variables
        self.vx = 0         # X speed
        self.vy = 0         # Y speed
        self.grradius = 0   # Radius for ground collision

        # Physics coefficients
        self.mass = 0       # Mass
        self.gmul = 1       # Gravity multiplier
        self.drfric = 0.99  # Air friction (drag)
        self.grfric = 0.9   # Ground friction
        self.bounce = 0.75  # Bounciness

    def update(self, tdelta):
        pass
