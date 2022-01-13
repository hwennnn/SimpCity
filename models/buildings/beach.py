from models.buildings.building import Building


class Beach(Building):
    def __init__(self, name, x, y):
        Building.__init__(self, name, x, y)

    def retrieveBuildingScore(self, grid=None):
        return 3 if self.y in (0, 3) else 1
