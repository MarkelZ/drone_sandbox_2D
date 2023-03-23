
class Engine:
    def __init__(self, width, height):
        # Parameters
        self.width = width
        self.height = height
        self.ground = height

        # Physics variables
        self.gravity = -1

        # Physics objects
        self.points = []
        self.links = []
        self.points_to_add = []
        self.links_to_add = []
        self.points_to_remove = []
        self.links_to_remove = []

    def update(self, tdelta):
        # Update all point-masses
        for p in self.points:
            p.update(tdelta)

        # Update all rigid links
        for l in self.links:
            l.update(tdelta)

        # Add and remove points
        self.points += self.points_to_add
        self.points = [
            p for p in self.points if p not in self.points_to_remove]

        # Add and remove links
        self.points += self.points_to_add
        self.points = [
            p for p in self.points if p not in self.points_to_remove]

    def change_size(self, width, height, updateground=False):
        self.width = width
        self.height = height

        # Update ground level too only if enabled
        if updateground:
            self.ground = height

    def generate_explosion(self, x, y, power):
        pass

    def add_pointmass(self, p):
        self.points_to_add.append(p)

    def add_rigidlink(self, r):
        self.links_to_add.append(r)

    def remove_pointmass(self, p):
        self.points_to_remove.append(p)

    def remove_rigidlink(self, r):
        self.links_to_remove.append(r)
