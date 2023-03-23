

class PointMass:
    def __init__(self, engine, x, y, vx=0, vy=0):
        # Parameters
        self.engine = engine
        self.x = x          # X position
        self.y = y          # Y position

        # Physics variables
        self.vx = vx        # X speed
        self.vy = vy        # Y speed
        self.grradius = 0   # Radius for ground collision
        self.mass = 1       # Mass

        # Physics coefficients
        self.gmul = 1       # Gravity multiplier
        self.drfric = 0.99  # Air friction (drag)
        self.grfric = 0.9   # Ground friction
        self.bounce = -0.75  # Bounciness

    def update(self, tdelta):
        # Apply gravity
        self.vy += self.engine.gravity * self.gmul

        # Apply drag
        self.vx *= self.drfric
        self.vy *= self.drfric

        # Move with velocity
        self.x += self.vx
        self.y += self.vy

        # Solve collision with ground
        diff = self.engine.ground - self.y - self.grradius
        if diff < 0:
            self.y = self.engine.ground - self.grradius
            self.vy = self.vy * self.bounce
            self.vx *= self.grfric
