from models.buildings.building import Building
from models.enums import Buildings


class House(Building):
    def __init__(self, name, x, y):
        Building.__init__(self, name, x, y)

    def retrieveBuildingScore(self, grid):
        pass
