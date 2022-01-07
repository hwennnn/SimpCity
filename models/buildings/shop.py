from models.buildings.building import Building


class Shop(Building):
    def __init__(self, name, x, y):
        Building.__init__(self, name, x, y)

    def retrieveBuildingScore(self, grid):
        pass
