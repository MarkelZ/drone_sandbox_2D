from math import sqrt


class RigidLink:
    def __init__(self, engine, p1, p2, length=None, breakcoef=2):
        self.engine = engine
        self.p1 = p1
        self.p2 = p2
        self.length = length if length != None else self.get_currentlength()

        self.breakcoef = breakcoef
        self.maxlength = self.length * breakcoef
        self.isbroken = False

        # Add to engine
        self.engine.add_rigidlink(self)

    def update(self, tdelta):
        # Distance between p1 and p2
        dist = self.get_currentlength()

        # If the distance is too great, break link
        if dist > self.maxlength:
            self.breaklink()
        # Else, constrain link
        elif dist > 0:
            # Normalized direction
            dirx = (self.p2.x - self.p1.x) / dist
            diry = (self.p2.y - self.p1.y) / dist

            # Difference between current length and link length
            difflength = self.length - dist

            # Proportion of masses
            alpha = self.p2.mass / (self.p1.mass + self.p2.mass)
            coalpha = alpha - 1

            # calculate differences in inertia
            mx1 = -dirx * difflength * alpha
            my1 = -diry * difflength * alpha
            mx2 = -dirx * difflength * coalpha
            my2 = -diry * difflength * coalpha

            # Constrain points accordingly
            self.p1.x += mx1
            self.p1.y += my1
            self.p2.x += mx2
            self.p2.y += my2

            # Update velocities
            self.p1.vx += mx1
            self.p1.vy += my1
            self.p2.vx += mx2
            self.p2.vy += my2

    def breaklink(self):
        self.engine.remove_rigidlink(self)
        self.isbroken = True

    def get_currentlength2(self):
        dx = self.p1.x - self.p2.x
        dy = self.p1.y - self.p2.y
        return dx*dx + dy*dy

    def get_currentlength(self):
        return sqrt(self.get_currentlength2())
