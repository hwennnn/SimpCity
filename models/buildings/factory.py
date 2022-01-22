from models.buildings.building import Building


class Factory(Building):
    def __init__(self, name, x, y):
        Building.__init__(self, name, x, y)

    def retrieveBuildingScore(self, grid):  # pragma: no cover
        pass
